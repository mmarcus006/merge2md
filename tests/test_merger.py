"""Unit tests for the merger module."""
import pytest
import tempfile
import subprocess
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock, call

from merge2md.merger import MarkdownMerger


class TestMarkdownMerger:
    """Test the MarkdownMerger class."""
    
    @pytest.fixture
    def merger(self):
        """Create a MarkdownMerger instance."""
        return MarkdownMerger()
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)
    
    def test_merge_empty_blocks(self, merger):
        """Test merging empty list of blocks."""
        result = merger.merge([])
        assert result == ""
    
    def test_merge_single_block(self, merger):
        """Test merging a single block."""
        result = merger.merge(["# Hello World"])
        assert result == "# Hello World"
    
    def test_merge_multiple_blocks(self, merger):
        """Test merging multiple blocks with separator."""
        blocks = ["# Document 1", "# Document 2", "# Document 3"]
        result = merger.merge(blocks)
        
        expected = "# Document 1\n\n---\n\n# Document 2\n\n---\n\n# Document 3"
        assert result == expected
    
    def test_merge_with_header(self, merger):
        """Test merging with a header."""
        blocks = ["## Section 1", "## Section 2"]
        result = merger.merge(blocks, header="Main Title")
        
        expected = "# Main Title\n\n---\n\n## Section 1\n\n---\n\n## Section 2"
        assert result == expected
    
    def test_merge_strips_whitespace(self, merger):
        """Test that merge strips whitespace from blocks."""
        blocks = ["  # Document 1  \n\n", "\n\n# Document 2\n\n"]
        result = merger.merge(blocks)
        
        expected = "# Document 1\n\n---\n\n# Document 2"
        assert result == expected
    
    def test_merge_empty_blocks_with_header(self, merger):
        """Test merging empty blocks with header."""
        result = merger.merge([], header="Title")
        assert result == "# Title"
    
    def test_export_markdown(self, merger, temp_dir):
        """Test exporting to markdown file."""
        content = "# Test Document\n\nThis is a test."
        output_path = temp_dir / "output.md"
        
        merger.export(content, output_path)
        
        # Verify file was created and contains the content
        assert output_path.exists()
        assert output_path.read_text(encoding="utf-8") == content
    
    def test_export_unsupported_format(self, merger, temp_dir):
        """Test exporting to unsupported format raises error."""
        content = "# Test"
        output_path = temp_dir / "output.docx"
        
        with pytest.raises(ValueError, match="Unsupported output format: .docx"):
            merger.export(content, output_path)
    
    @patch('merge2md.merger.pypandoc.convert_file')
    def test_export_pdf_with_pypandoc(self, mock_convert, merger, temp_dir):
        """Test PDF export when pypandoc is available."""
        # Force _HAS_PYPANDOC to True
        with patch('merge2md.merger._HAS_PYPANDOC', True):
            content = "# Test Document"
            output_path = temp_dir / "output.pdf"
            
            merger.export(content, output_path)
            
            # Verify pypandoc was called correctly
            mock_convert.assert_called_once()
            call_args = mock_convert.call_args
            
            # Check that a temporary file was used
            temp_file_path = call_args[0][0]
            assert temp_file_path.endswith('.md')
            
            # Check other arguments
            assert call_args[0][1] == "pdf"
            assert call_args[1]["outputfile"] == str(output_path)
    
    @patch('merge2md.merger.subprocess.run')
    @patch('merge2md.merger.shutil.which')
    def test_export_pdf_with_pandoc_subprocess(self, mock_which, mock_run, merger, temp_dir):
        """Test PDF export using subprocess when pypandoc is not available."""
        # Force _HAS_PYPANDOC to False and pandoc to be available
        with patch('merge2md.merger._HAS_PYPANDOC', False):
            mock_which.return_value = "/usr/bin/pandoc"
            
            content = "# Test Document"
            output_path = temp_dir / "output.pdf"
            
            merger.export(content, output_path)
            
            # Verify subprocess.run was called correctly
            mock_run.assert_called_once()
            call_args = mock_run.call_args[0][0]
            
            assert call_args[0] == "pandoc"
            assert call_args[1].endswith('.md')  # temp file
            assert call_args[2] == "-o"
            assert call_args[3] == str(output_path)
            assert mock_run.call_args[1]["check"] is True
    
    @patch('merge2md.merger.subprocess.run')
    @patch('merge2md.merger.shutil.which')
    def test_export_pdf_no_pandoc(self, mock_which, mock_run, merger, temp_dir):
        """Test PDF export raises error when pandoc is not available."""
        # Force _HAS_PYPANDOC to False and pandoc to be unavailable
        with patch('merge2md.merger._HAS_PYPANDOC', False):
            mock_which.return_value = None
            
            content = "# Test Document"
            output_path = temp_dir / "output.pdf"
            
            with pytest.raises(RuntimeError, match="pandoc not found"):
                merger.export(content, output_path)
    
    def test_markdown_to_pdf_creates_temp_file(self, merger, temp_dir):
        """Test that _markdown_to_pdf creates a temporary file with content."""
        with patch('merge2md.merger._HAS_PYPANDOC', True):
            with patch('merge2md.merger.pypandoc.convert_file') as mock_convert:
                content = "# Test\n\nContent with unicode: é"
                output_path = temp_dir / "output.pdf"
                
                merger._markdown_to_pdf(content, output_path)
                
                # Get the temp file path from the call
                temp_file_path = mock_convert.call_args[0][0]
                
                # The temp file should have been created and written to
                # We can't check its content directly as it's deleted,
                # but we can verify the call was made correctly
                assert temp_file_path.endswith('.md')
    
    def test_export_case_insensitive_extension(self, merger, temp_dir):
        """Test that export handles extensions case-insensitively."""
        content = "# Test"
        
        # Test uppercase .MD
        output_path = temp_dir / "output.MD"
        merger.export(content, output_path)
        assert output_path.exists()
        assert output_path.read_text(encoding="utf-8") == content
        
        # Test mixed case .Md
        output_path2 = temp_dir / "output2.Md"
        merger.export(content, output_path2)
        assert output_path2.exists()
    
    @patch('merge2md.merger.pypandoc.convert_file')
    def test_export_pdf_case_insensitive(self, mock_convert, merger, temp_dir):
        """Test PDF export with uppercase extension."""
        with patch('merge2md.merger._HAS_PYPANDOC', True):
            content = "# Test"
            output_path = temp_dir / "output.PDF"
            
            merger.export(content, output_path)
            
            # Should still call pypandoc
            mock_convert.assert_called_once()
    
    def test_separator_constant(self, merger):
        """Test that the separator is defined correctly."""
        assert merger.SEP == "\n\n---\n\n"
    
    def test_merge_with_empty_string_blocks(self, merger):
        """Test merging blocks that contain empty strings."""
        blocks = ["# Title", "", "## Section"]
        result = merger.merge(blocks)
        
        # Empty strings should be preserved but stripped
        expected = "# Title\n\n---\n\n\n\n---\n\n## Section"
        assert result == expected
    
    def test_merge_different_format_content(self, merger):
        """Test merging content from different file formats."""
        # Simulate content from different file types
        blocks = [
            "# PDF Document\n\nThis content was extracted from a PDF file.",
            "# Word Document\n\n## Chapter 1\n\nContent from a DOCX file.",
            "# HTML Page\n\n- Item 1\n- Item 2\n\nExtracted from HTML.",
            "| Name | Value |\n|------|-------|\n| A | 1 |\n| B | 2 |\n\nCSV data converted to markdown table.",
            "# AsciiDoc Content\n\n**Bold** and *italic* text from AsciiDoc."
        ]
        
        result = merger.merge(blocks, header="Multi-Format Document")
        
        # Check that all content is present
        assert "# Multi-Format Document" in result
        assert "PDF Document" in result
        assert "Word Document" in result
        assert "HTML Page" in result
        assert "CSV data converted" in result
        assert "AsciiDoc Content" in result
        
        # Check separators
        assert result.count("\n\n---\n\n") == 5  # Header + 5 blocks = 5 separators

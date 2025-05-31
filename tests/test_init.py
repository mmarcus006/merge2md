"""Test the public API exposed by __init__.py."""
import pytest
from pathlib import Path
from unittest.mock import patch, Mock

from merge2md import convert_and_merge, ConversionSettings, DoclingMarkdownConverter
from docling.datamodel.base_models import InputFormat


class TestPublicAPI:
    """Test the public API functions."""
    
    @pytest.fixture
    def temp_dir(self, tmp_path):
        """Create a temporary directory with test files."""
        # Create test files
        (tmp_path / "test.pdf").write_text("PDF content")
        (tmp_path / "test.docx").write_text("Word content")
        (tmp_path / "test.html").write_text("<html><body>HTML content</body></html>")
        (tmp_path / "test.csv").write_text("Name,Value\nA,1\nB,2")
        (tmp_path / "test.md").write_text("# Markdown content")
        return tmp_path
    
    @patch('merge2md.converter.DocumentConverter')
    def test_convert_and_merge_basic(self, mock_converter_class, temp_dir):
        """Test basic convert_and_merge functionality."""
        # Setup mock
        mock_converter = Mock()
        mock_converter_class.return_value = mock_converter
        mock_converter.convert.return_value = Mock(
            document=Mock(export_to_markdown=Mock(return_value="# Converted"))
        )
        
        # Test files
        files = [
            temp_dir / "test.pdf",
            temp_dir / "test.docx",
            temp_dir / "test.html"
        ]
        output = temp_dir / "output.md"
        
        # Call the function
        result = convert_and_merge(files, output, title="Test Title")
        
        # Verify
        assert result == output
        assert output.exists()
        content = output.read_text()
        assert "# Test Title" in content
        assert "# Converted" in content
    
    @patch('merge2md.converter.DocumentConverter')
    def test_convert_and_merge_with_settings(self, mock_converter_class, temp_dir):
        """Test convert_and_merge with custom settings."""
        # Setup mock
        mock_converter = Mock()
        mock_converter_class.return_value = mock_converter
        mock_converter.convert.return_value = Mock(
            document=Mock(export_to_markdown=Mock(return_value="# Converted"))
        )
        
        # Custom settings
        settings = ConversionSettings(
            ocr=False,
            languages=["de", "fr"],
            dpi=600,
            allowed_formats=[InputFormat.PDF, InputFormat.DOCX]
        )
        
        files = [temp_dir / "test.pdf"]
        output = temp_dir / "output.md"
        
        # Call the function
        result = convert_and_merge(files, output, settings=settings)
        
        # Verify settings were passed correctly
        assert result == output
        assert output.exists()
        
        # Check that DocumentConverter was initialized with correct settings
        call_kwargs = mock_converter_class.call_args[1]
        assert 'allowed_formats' in call_kwargs
        assert call_kwargs['allowed_formats'] == settings.allowed_formats
    
    @patch('merge2md.converter.DocumentConverter')
    @patch('merge2md.merger.pypandoc.convert_file')
    def test_convert_and_merge_pdf_output(self, mock_pypandoc, mock_converter_class, temp_dir):
        """Test convert_and_merge with PDF output."""
        # Force pypandoc to be available
        with patch('merge2md.merger._HAS_PYPANDOC', True):
            # Setup mock
            mock_converter = Mock()
            mock_converter_class.return_value = mock_converter
            mock_converter.convert.return_value = Mock(
                document=Mock(export_to_markdown=Mock(return_value="# PDF Content"))
            )
            
            files = [temp_dir / "test.pdf"]
            output = temp_dir / "output.pdf"
            
            # Call the function
            result = convert_and_merge(files, output)
            
            # Verify pypandoc was called for PDF conversion
            assert result == output
            mock_pypandoc.assert_called_once()
    
    def test_imports(self):
        """Test that all expected exports are available."""
        from merge2md import convert_and_merge, ConversionSettings, DoclingMarkdownConverter
        
        assert callable(convert_and_merge)
        assert ConversionSettings is not None
        assert DoclingMarkdownConverter is not None
    
    def test_conversion_settings_defaults(self):
        """Test ConversionSettings default values."""
        settings = ConversionSettings()
        
        assert settings.ocr is True
        assert settings.languages == ["en"]
        assert settings.dpi == 300
        assert len(settings.allowed_formats) == 8
        
        # Check all default formats
        expected_formats = [
            InputFormat.PDF,
            InputFormat.IMAGE,
            InputFormat.DOCX,
            InputFormat.HTML,
            InputFormat.PPTX,
            InputFormat.ASCIIDOC,
            InputFormat.CSV,
            InputFormat.MD,
        ]
        for fmt in expected_formats:
            assert fmt in settings.allowed_formats
    

    
    @patch('merge2md.converter.DocumentConverter')
    @patch('merge2md.__init__.show_completion_dialog')
    def test_convert_and_merge_filename_only(self, mock_dialog, mock_converter_class, temp_dir):
        """Test convert_and_merge with filename only (no path)."""
        # Setup mock
        mock_converter = Mock()
        mock_converter_class.return_value = mock_converter
        mock_converter.convert.return_value = Mock(
            document=Mock(export_to_markdown=Mock(return_value="# Converted"))
        )
        
        files = [temp_dir / "test.pdf"]
        
        # Call with just filename (no path) - use .md to avoid PDF conversion in test
        result = convert_and_merge(files, Path("output.md"))
        
        # Should use Downloads folder
        assert result.parent == Path.home() / "Downloads"
        # Name might have number suffix if file exists
        assert result.name.startswith("output") and result.name.endswith(".md")
    
    @patch('merge2md.converter.DocumentConverter')
    @patch('merge2md.__init__.show_completion_dialog')
    def test_convert_and_merge_no_notification(self, mock_dialog, mock_converter_class, temp_dir):
        """Test convert_and_merge with notification disabled."""
        # Setup mock
        mock_converter = Mock()
        mock_converter_class.return_value = mock_converter
        mock_converter.convert.return_value = Mock(
            document=Mock(export_to_markdown=Mock(return_value="# Converted"))
        )
        
        files = [temp_dir / "test.pdf"]
        output = temp_dir / "output.md"
        
        # Call with notification disabled
        result = convert_and_merge(files, output, show_notification=False)
        
        # Should not show notification
        mock_dialog.assert_not_called()
    

    
    def test_get_default_output_path_import(self):
        """Test that get_default_output_path is available."""
        from merge2md import get_default_output_path
        
        path = get_default_output_path("test.md")
        assert path.parent == Path.home() / "Downloads"
        assert path.name.startswith("test") and path.name.endswith(".md")
    
    def test_show_completion_dialog_import(self):
        """Test that show_completion_dialog is available."""
        from merge2md import show_completion_dialog
        assert callable(show_completion_dialog) 
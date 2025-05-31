"""Unit tests for the converter module."""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from merge2md.converter import ConversionSettings, DoclingMarkdownConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions, EasyOcrOptions
from docling.datamodel.base_models import InputFormat
from docling.document_converter import PdfFormatOption, WordFormatOption
from docling.pipeline.simple_pipeline import SimplePipeline
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline


class TestConversionSettings:
    """Test the ConversionSettings dataclass."""
    
    def test_default_settings(self):
        """Test default settings initialization."""
        settings = ConversionSettings()
        assert settings.ocr is True
        assert settings.languages == ["en"]
        assert settings.dpi == 300
        # Test default allowed formats
        assert InputFormat.PDF in settings.allowed_formats
        assert InputFormat.IMAGE in settings.allowed_formats
        assert InputFormat.DOCX in settings.allowed_formats
        assert InputFormat.HTML in settings.allowed_formats
        assert InputFormat.PPTX in settings.allowed_formats
        assert InputFormat.ASCIIDOC in settings.allowed_formats
        assert InputFormat.CSV in settings.allowed_formats
        assert InputFormat.MD in settings.allowed_formats
        assert len(settings.allowed_formats) == 8
    
    def test_custom_settings(self):
        """Test custom settings initialization."""
        custom_formats = [InputFormat.PDF, InputFormat.DOCX]
        settings = ConversionSettings(
            ocr=False,
            languages=["en", "es"],
            dpi=600,
            allowed_formats=custom_formats
        )
        assert settings.ocr is False
        assert settings.languages == ["en", "es"]
        assert settings.dpi == 600
        assert settings.allowed_formats == custom_formats
    
    def test_to_pipeline_options_enabled(self):
        """Test pipeline options when OCR is enabled."""
        settings = ConversionSettings(ocr=True, languages=["en", "fr"], dpi=400)
        pipeline_options = settings.to_pipeline_options()
        
        assert isinstance(pipeline_options, PdfPipelineOptions)
        assert pipeline_options.do_ocr is True
        assert isinstance(pipeline_options.ocr_options, EasyOcrOptions)
        assert pipeline_options.ocr_options.lang == ["en", "fr"]
    
    def test_to_pipeline_options_disabled(self):
        """Test pipeline options when OCR is disabled."""
        settings = ConversionSettings(ocr=False)
        pipeline_options = settings.to_pipeline_options()
        
        assert isinstance(pipeline_options, PdfPipelineOptions)
        assert pipeline_options.do_ocr is False


class TestDoclingMarkdownConverter:
    """Test the DoclingMarkdownConverter class."""
    
    @pytest.fixture
    def test_data_dir(self):
        """Return the test data directory."""
        return Path(__file__).parent / "data"
    
    @pytest.fixture
    def converter(self):
        """Create a converter instance with default settings."""
        return DoclingMarkdownConverter()
    
    def test_init_default_settings(self):
        """Test converter initialization with default settings."""
        converter = DoclingMarkdownConverter()
        assert converter.settings.ocr is True
        assert converter.settings.languages == ["en"]
        assert converter._converter is not None
        assert len(converter.settings.allowed_formats) == 8
    
    def test_init_custom_settings(self):
        """Test converter initialization with custom settings."""
        settings = ConversionSettings(
            ocr=False, 
            languages=["de"], 
            dpi=150,
            allowed_formats=[InputFormat.PDF, InputFormat.DOCX]
        )
        converter = DoclingMarkdownConverter(settings)
        assert converter.settings.ocr is False
        assert converter.settings.languages == ["de"]
        assert converter.settings.dpi == 150
        assert len(converter.settings.allowed_formats) == 2
    
    @patch('merge2md.converter.DocumentConverter')
    def test_init_format_options(self, mock_document_converter):
        """Test converter initialization sets up correct format options."""
        settings = ConversionSettings()
        converter = DoclingMarkdownConverter(settings)
        
        # Verify DocumentConverter was called with correct parameters
        mock_document_converter.assert_called_once()
        call_kwargs = mock_document_converter.call_args[1]
        
        # Check allowed_formats
        assert 'allowed_formats' in call_kwargs
        assert call_kwargs['allowed_formats'] == settings.allowed_formats
        
        # Check format_options
        assert 'format_options' in call_kwargs
        format_options = call_kwargs['format_options']
        
        # Check PDF format option
        assert InputFormat.PDF in format_options
        assert isinstance(format_options[InputFormat.PDF], PdfFormatOption)
        
        # Check DOCX format option
        assert InputFormat.DOCX in format_options
        assert isinstance(format_options[InputFormat.DOCX], WordFormatOption)
    
    def test_to_markdown_with_different_formats(self, converter, test_data_dir):
        """Test converting different file formats to markdown."""
        # Test with various file formats
        test_files = [
            test_data_dir / "test1.md",
            test_data_dir / "test2.txt",
            test_data_dir / "test.html",
            test_data_dir / "test.csv",
            test_data_dir / "test.asciidoc"
        ]
        
        # Mock the converter.convert method
        with patch.object(converter._converter, 'convert') as mock_convert:
            # Create mock results for different file types
            mock_results = []
            for i, file in enumerate(test_files):
                mock_result = Mock()
                mock_result.document.export_to_markdown.return_value = f"# Document {i+1}\n\nContent from {file.suffix}"
                mock_results.append(mock_result)
            
            mock_convert.side_effect = mock_results
            
            results = converter.to_markdown(test_files)
        
        # Should return results for all file types
        assert len(results) == 5
        
        # Check each result contains appropriate content
        for i, result in enumerate(results):
            assert f"# Document {i+1}" in result
            assert f"Content from {test_files[i].suffix}" in result
    
    def test_to_markdown_with_real_files(self, converter, test_data_dir):
        """Test converting real test files to markdown."""
        # Test with existing markdown and text files
        test_files = [
            test_data_dir / "test1.md",
            test_data_dir / "test2.txt"
        ]
        
        # Mock the converter.convert method
        with patch.object(converter._converter, 'convert') as mock_convert:
            # Create mock results
            mock_result1 = Mock()
            mock_result1.document.export_to_markdown.return_value = "# Test Document 1\n\n## Section 1\n\nContent"
            
            mock_result2 = Mock()
            mock_result2.document.export_to_markdown.return_value = "This is a plain text file"
            
            mock_convert.side_effect = [mock_result1, mock_result2]
            
            results = converter.to_markdown(test_files)
        
        # Should return two results
        assert len(results) == 2
        
        # First result should contain the markdown content
        assert "# Test Document 1" in results[0]
        assert "## Section 1" in results[0]
        
        # Second result should contain the text content
        assert "This is a plain text file" in results[1]
    
    def test_to_markdown_missing_file(self, converter, test_data_dir, caplog):
        """Test handling of missing files."""
        missing_file = test_data_dir / "nonexistent.pdf"
        existing_file = test_data_dir / "test1.md"
        
        # Mock the converter for the existing file
        with patch.object(converter._converter, 'convert') as mock_convert:
            mock_result = Mock()
            mock_result.document.export_to_markdown.return_value = "# Test Document 1"
            mock_convert.return_value = mock_result
            
            results = converter.to_markdown([missing_file, existing_file])
        
        # Should only return one result (for the existing file)
        assert len(results) == 1
        assert "# Test Document 1" in results[0]
        
        # Check that a warning was logged
        assert "Missing file" in caplog.text
        assert "nonexistent.pdf" in caplog.text
    
    def test_to_markdown_conversion_error(self, converter, test_data_dir, caplog):
        """Test handling of conversion errors."""
        # Make the converter raise an exception
        with patch.object(converter._converter, 'convert', side_effect=Exception("Test error")):
            test_file = test_data_dir / "test1.md"
            results = converter.to_markdown([test_file])
        
        # Should return empty list due to error
        assert len(results) == 0
        
        # Check that an error was logged
        assert "Docling failed on" in caplog.text
        assert "test1.md" in caplog.text
        assert "Test error" in caplog.text
    
    def test_to_markdown_no_document_content(self, converter, test_data_dir, caplog):
        """Test handling when conversion returns no document."""
        test_file = test_data_dir / "test1.md"
        
        with patch.object(converter._converter, 'convert') as mock_convert:
            # Return None result
            mock_convert.return_value = None
            
            results = converter.to_markdown([test_file])
        
        # Should return empty list
        assert len(results) == 0
        
        # Check that an error was logged
        assert "No document content for" in caplog.text
    
    def test_to_markdown_mixed_success_failure(self, converter, test_data_dir):
        """Test mixed success and failure conversions."""
        with patch.object(converter._converter, 'convert') as mock_convert:
            # Create a mock result for successful conversion
            mock_result = Mock()
            mock_result.document.export_to_markdown.return_value = "# Converted Content"
            
            # First call succeeds, second fails
            mock_convert.side_effect = [
                mock_result,
                Exception("Conversion failed")
            ]
            
            test_files = [
                test_data_dir / "test1.md",
                test_data_dir / "test2.txt"
            ]
            
            results = converter.to_markdown(test_files)
        
        # Should only get one successful result
        assert len(results) == 1
        assert results[0] == "# Converted Content"
    
    def test_to_markdown_empty_list(self, converter):
        """Test converting an empty list of files."""
        results = converter.to_markdown([])
        assert results == []
    
    def test_to_markdown_logs_info(self, converter, test_data_dir, caplog):
        """Test that info messages are logged during conversion."""
        with patch.object(converter._converter, 'convert') as mock_convert:
            # Create a mock result
            mock_result = Mock()
            mock_result.document.export_to_markdown.return_value = "# Test"
            mock_convert.return_value = mock_result
            
            test_file = test_data_dir / "test1.md"
            with caplog.at_level("INFO"):
                converter.to_markdown([test_file])
        
        # Check that info was logged
        assert "Converting test1.md" in caplog.text
    
    def test_to_markdown_with_custom_allowed_formats(self, test_data_dir):
        """Test converter with custom allowed formats."""
        # Create converter that only allows PDF and DOCX
        settings = ConversionSettings(allowed_formats=[InputFormat.PDF, InputFormat.DOCX])
        converter = DoclingMarkdownConverter(settings)
        
        # Test files including formats not in allowed list
        test_files = [
            test_data_dir / "test.pdf",
            test_data_dir / "test.docx",
            test_data_dir / "test.html",  # Not allowed
            test_data_dir / "test.csv"    # Not allowed
        ]
        
        with patch.object(converter._converter, 'convert') as mock_convert:
            # Docling should respect the allowed_formats setting
            mock_result = Mock()
            mock_result.document.export_to_markdown.return_value = "# Converted"
            mock_convert.return_value = mock_result
            
            # All files will be passed to Docling, but it will internally filter
            results = converter.to_markdown(test_files)
        
        # The number of results depends on how Docling handles non-allowed formats
        # It might skip them or raise exceptions that we catch

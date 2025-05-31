"""Unit tests for the converter module."""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from merge2md.converter import ConversionSettings, DoclingMarkdownConverter
from docling.core.errors import DoclingConversionError
from docling.ocr.easyocr import EasyOcrOptions


class TestConversionSettings:
    """Test the ConversionSettings dataclass."""
    
    def test_default_settings(self):
        """Test default settings initialization."""
        settings = ConversionSettings()
        assert settings.ocr is True
        assert settings.languages == ["en"]
        assert settings.dpi == 300
    
    def test_custom_settings(self):
        """Test custom settings initialization."""
        settings = ConversionSettings(
            ocr=False,
            languages=["en", "es"],
            dpi=600
        )
        assert settings.ocr is False
        assert settings.languages == ["en", "es"]
        assert settings.dpi == 600
    
    def test_to_ocr_options_enabled(self):
        """Test OCR options when OCR is enabled."""
        settings = ConversionSettings(ocr=True, languages=["en", "fr"], dpi=400)
        ocr_options = settings.to_ocr_options()
        
        assert isinstance(ocr_options, EasyOcrOptions)
        assert ocr_options.languages == ["en", "fr"]
        assert ocr_options.dpi == 400
    
    def test_to_ocr_options_disabled(self):
        """Test OCR options when OCR is disabled."""
        settings = ConversionSettings(ocr=False)
        ocr_options = settings.to_ocr_options()
        
        assert ocr_options is None


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
    
    def test_init_custom_settings(self):
        """Test converter initialization with custom settings."""
        settings = ConversionSettings(ocr=False, languages=["de"], dpi=150)
        converter = DoclingMarkdownConverter(settings)
        assert converter.settings.ocr is False
        assert converter.settings.languages == ["de"]
        assert converter.settings.dpi == 150
    
    @patch('merge2md.converter.DocumentConverter')
    def test_init_with_ocr_disabled(self, mock_document_converter):
        """Test converter initialization with OCR disabled."""
        settings = ConversionSettings(ocr=False)
        converter = DoclingMarkdownConverter(settings)
        
        # Verify DocumentConverter was called with ocr_options=None
        mock_document_converter.assert_called_once_with(ocr_options=None)
    
    def test_to_markdown_with_real_files(self, converter, test_data_dir):
        """Test converting real test files to markdown."""
        # Test with existing markdown and text files
        test_files = [
            test_data_dir / "test1.md",
            test_data_dir / "test2.txt"
        ]
        
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
        
        results = converter.to_markdown([missing_file, existing_file])
        
        # Should only return one result (for the existing file)
        assert len(results) == 1
        assert "# Test Document 1" in results[0]
        
        # Check that a warning was logged
        assert "Missing file" in caplog.text
        assert "nonexistent.pdf" in caplog.text
    
    @patch('merge2md.converter.DocumentConverter.convert_to_markdown')
    def test_to_markdown_conversion_error(self, mock_convert, converter, test_data_dir, caplog):
        """Test handling of conversion errors."""
        # Make the mock raise a DoclingConversionError
        mock_convert.side_effect = DoclingConversionError("Test error")
        
        test_file = test_data_dir / "test1.md"
        results = converter.to_markdown([test_file])
        
        # Should return empty list due to error
        assert len(results) == 0
        
        # Check that an error was logged
        assert "Docling failed on" in caplog.text
        assert "test1.md" in caplog.text
        assert "Test error" in caplog.text
    
    @patch('merge2md.converter.DocumentConverter.convert_to_markdown')
    def test_to_markdown_mixed_success_failure(self, mock_convert, converter, test_data_dir):
        """Test mixed success and failure conversions."""
        # Create a mock result for successful conversion
        mock_result = Mock()
        mock_result.content = "# Converted Content"
        
        # First call succeeds, second fails
        mock_convert.side_effect = [
            mock_result,
            DoclingConversionError("Conversion failed")
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
    
    @patch('merge2md.converter.DocumentConverter.convert_to_markdown')
    def test_to_markdown_logs_info(self, mock_convert, converter, test_data_dir, caplog):
        """Test that info messages are logged during conversion."""
        # Create a mock result
        mock_result = Mock()
        mock_result.content = "# Test"
        mock_convert.return_value = mock_result
        
        test_file = test_data_dir / "test1.md"
        with caplog.at_level("INFO"):
            converter.to_markdown([test_file])
        
        # Check that info was logged
        assert "Converting test1.md" in caplog.text

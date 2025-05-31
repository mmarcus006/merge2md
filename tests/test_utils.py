"""Unit tests for the utils module."""
import pytest
from pathlib import Path

from merge2md.utils import natural_sort


class TestNaturalSort:
    """Test the natural_sort function."""
    
    def test_natural_sort_numbers(self):
        """Test natural sorting with numbers in filenames."""
        paths = [
            Path("file10.txt"),
            Path("file2.txt"), 
            Path("file1.txt"),
            Path("file20.txt"),
            Path("file3.txt")
        ]
        
        sorted_paths = natural_sort(paths)
        
        expected = [
            Path("file1.txt"),
            Path("file2.txt"),
            Path("file3.txt"),
            Path("file10.txt"),
            Path("file20.txt")
        ]
        
        assert sorted_paths == expected
    
    def test_natural_sort_mixed_extensions(self):
        """Test natural sorting with different file extensions."""
        paths = [
            Path("doc10.pdf"),
            Path("doc2.txt"),
            Path("doc1.pdf"),
            Path("doc20.docx"),
            Path("doc3.md")
        ]
        
        sorted_paths = natural_sort(paths)
        
        expected = [
            Path("doc1.pdf"),
            Path("doc2.txt"),
            Path("doc3.md"),
            Path("doc10.pdf"),
            Path("doc20.docx")
        ]
        
        assert sorted_paths == expected
    
    def test_natural_sort_case_insensitive(self):
        """Test that natural sort is case insensitive."""
        paths = [
            Path("File10.txt"),
            Path("file2.txt"),
            Path("FILE1.txt"),
            Path("FiLe3.txt")
        ]
        
        sorted_paths = natural_sort(paths)
        
        # Should be sorted by number, ignoring case
        expected = [
            Path("FILE1.txt"),
            Path("file2.txt"),
            Path("FiLe3.txt"),
            Path("File10.txt")
        ]
        
        assert sorted_paths == expected
    
    def test_natural_sort_no_numbers(self):
        """Test natural sorting with no numbers in filenames."""
        paths = [
            Path("zebra.txt"),
            Path("apple.txt"),
            Path("banana.txt"),
            Path("Apple.txt")  # uppercase
        ]
        
        sorted_paths = natural_sort(paths)
        
        expected = [
            Path("apple.txt"),
            Path("Apple.txt"),
            Path("banana.txt"),
            Path("zebra.txt")
        ]
        
        assert sorted_paths == expected
    
    def test_natural_sort_empty_list(self):
        """Test natural sorting with empty list."""
        assert natural_sort([]) == []
    
    def test_natural_sort_single_item(self):
        """Test natural sorting with single item."""
        paths = [Path("file.txt")]
        assert natural_sort(paths) == paths
    
    def test_natural_sort_complex_names(self):
        """Test natural sorting with complex filenames."""
        paths = [
            Path("report_2023_10_v2.pdf"),
            Path("report_2023_2_v1.pdf"),
            Path("report_2023_10_v1.pdf"),
            Path("report_2023_2_v10.pdf")
        ]
        
        sorted_paths = natural_sort(paths)
        
        expected = [
            Path("report_2023_2_v1.pdf"),
            Path("report_2023_2_v10.pdf"),
            Path("report_2023_10_v1.pdf"),
            Path("report_2023_10_v2.pdf")
        ]
        
        assert sorted_paths == expected
    
    def test_natural_sort_with_paths(self):
        """Test natural sorting with full paths."""
        paths = [
            Path("/tmp/file10.txt"),
            Path("/tmp/file2.txt"),
            Path("/tmp/file1.txt")
        ]
        
        sorted_paths = natural_sort(paths)
        
        expected = [
            Path("/tmp/file1.txt"),
            Path("/tmp/file2.txt"),
            Path("/tmp/file10.txt")
        ]
        
        assert sorted_paths == expected
    
    def test_natural_sort_preserves_type(self):
        """Test that natural sort returns a list."""
        # Pass a generator
        paths = (Path(f"file{i}.txt") for i in [3, 1, 2])
        result = natural_sort(paths)
        
        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0] == Path("file1.txt")
    
    def test_natural_sort_docling_formats(self):
        """Test natural sorting with all Docling-supported file formats."""
        paths = [
            Path("doc10.pdf"),
            Path("doc2.docx"),
            Path("doc1.html"),
            Path("doc20.pptx"),
            Path("doc3.csv"),
            Path("doc5.asciidoc"),
            Path("doc4.md"),
            Path("doc15.png"),
            Path("doc12.jpg")
        ]
        
        sorted_paths = natural_sort(paths)
        
        expected = [
            Path("doc1.html"),
            Path("doc2.docx"),
            Path("doc3.csv"),
            Path("doc4.md"),
            Path("doc5.asciidoc"),
            Path("doc10.pdf"),
            Path("doc12.jpg"),
            Path("doc15.png"),
            Path("doc20.pptx")
        ]
        
        assert sorted_paths == expected 
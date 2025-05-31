"""Unit tests for the notifier module."""
import pytest
from pathlib import Path
from unittest.mock import patch, call
import subprocess

from merge2md.notifier import show_completion_dialog, get_default_output_path


class TestNotifier:
    """Test the notification functions."""
    
    @patch('merge2md.notifier.subprocess.run')
    def test_show_completion_dialog_success(self, mock_run, tmp_path):
        """Test showing success dialog."""
        output_path = tmp_path / "test.md"
        output_path.write_text("content")
        
        show_completion_dialog(output_path, success=True)
        
        # Verify osascript was called
        mock_run.assert_called_once()
        call_args = mock_run.call_args
        
        assert call_args[0][0][0] == "osascript"
        assert call_args[0][0][1] == "-e"
        script = call_args[0][0][2]
        
        # Check script contains expected elements
        assert "Conversion Complete" in script
        assert "File saved as: test.md" in script
        assert '"Open in Finder", "OK"' in script
        assert str(output_path) in script
    
    @patch('merge2md.notifier.subprocess.run')
    def test_show_completion_dialog_failure(self, mock_run, tmp_path):
        """Test showing failure dialog."""
        output_path = tmp_path / "test.md"
        
        show_completion_dialog(output_path, success=False)
        
        # Verify osascript was called
        mock_run.assert_called_once()
        script = mock_run.call_args[0][0][2]
        
        # Check script contains expected elements
        assert "Conversion Failed" in script
        assert "An error occurred during conversion." in script
        assert '"OK"' in script
        assert "Open in Finder" not in script
    
    @patch('merge2md.notifier.subprocess.run')
    @patch('merge2md.notifier.logger')
    def test_show_completion_dialog_exception(self, mock_logger, mock_run, tmp_path, capsys):
        """Test fallback when AppleScript fails."""
        mock_run.side_effect = Exception("Script failed")
        output_path = tmp_path / "test.md"
        
        show_completion_dialog(output_path, success=True)
        
        # Check warning was logged
        mock_logger.warning.assert_called_once()
        
        # Check fallback message was printed
        captured = capsys.readouterr()
        assert "✅ Conversion complete!" in captured.out
        assert str(output_path) in captured.out
    
    @patch('merge2md.notifier.subprocess.run')
    def test_show_completion_dialog_user_cancel(self, mock_run, tmp_path):
        """Test that user canceling dialog doesn't raise exception."""
        # Simulate user clicking cancel
        mock_run.return_value.returncode = 1
        output_path = tmp_path / "test.md"
        
        # Should not raise exception
        show_completion_dialog(output_path, success=True)
        
        assert mock_run.called
    
    def test_get_default_output_path_basic(self):
        """Test getting default output path."""
        path = get_default_output_path("test.md")
        
        assert path.parent == Path.home() / "Downloads"
        assert path.name == "test.md"
    
    def test_get_default_output_path_with_existing_file(self, tmp_path, monkeypatch):
        """Test handling of existing files."""
        # Mock home directory to use temp path
        downloads = tmp_path / "Downloads"
        downloads.mkdir()
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        
        # Create existing files
        (downloads / "merged.md").write_text("existing")
        (downloads / "merged_1.md").write_text("existing")
        
        # Should get next available number
        path = get_default_output_path("merged.md")
        assert path.name == "merged_2.md"
        assert path.parent == downloads
    
    def test_get_default_output_path_creates_downloads(self, tmp_path, monkeypatch):
        """Test that Downloads folder is created if it doesn't exist."""
        # Mock home directory to use temp path
        monkeypatch.setattr(Path, "home", lambda: tmp_path)
        
        # Downloads doesn't exist yet
        assert not (tmp_path / "Downloads").exists()
        
        path = get_default_output_path("test.pdf")
        
        # Should create Downloads folder
        assert (tmp_path / "Downloads").exists()
        assert path.parent == tmp_path / "Downloads"
    
    def test_get_default_output_path_different_extensions(self):
        """Test with different file extensions."""
        for ext in [".md", ".pdf", ".txt", ".html"]:
            filename = f"output{ext}"
            path = get_default_output_path(filename)
            # May have number suffix if file exists
            assert path.name.startswith("output") and path.name.endswith(ext)
            assert path.suffix == ext 
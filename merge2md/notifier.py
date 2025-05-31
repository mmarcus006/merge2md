"""
macOS notification system for merge2md completion.

Uses AppleScript via osascript to show native macOS dialogs.
"""
from __future__ import annotations

import subprocess
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def show_completion_dialog(output_path: Path, success: bool = True) -> None:
    """
    Show a macOS dialog notifying the user that the conversion is complete.
    
    Parameters
    ----------
    output_path : Path
        The path to the output file
    success : bool
        Whether the conversion was successful
    """
    try:
        output_path = output_path.resolve()  # Get absolute path
        parent_dir = output_path.parent
        filename = output_path.name
        
        if success:
            title = "Conversion Complete"
            message = f"File saved as: {filename}"
            buttons = '{"Open in Finder", "OK"}'
            default_button = 1
        else:
            title = "Conversion Failed"
            message = "An error occurred during conversion."
            buttons = '{"OK"}'
            default_button = 1
        
        # Build AppleScript command
        script = f'''
        tell application "System Events"
            activate
            set theResult to display dialog "{message}" ¬
                with title "{title}" ¬
                buttons {buttons} ¬
                default button {default_button} ¬
                with icon note
            
            if button returned of theResult is "Open in Finder" then
                tell application "Finder"
                    activate
                    reveal POSIX file "{output_path}"
                end tell
            end if
        end tell
        '''
        
        # Execute AppleScript
        subprocess.run(
            ["osascript", "-e", script],
            check=False,  # Don't raise exception if user cancels
            capture_output=True,
            text=True
        )
        
    except Exception as e:
        logger.warning(f"Could not show completion dialog: {e}")
        # Fall back to terminal message
        if success:
            print(f"\n✅ Conversion complete! File saved to: {output_path}")
        else:
            print(f"\n❌ Conversion failed.")


def get_default_output_path(filename: str = "merged.md") -> Path:
    """
    Get the default output path in the user's Downloads folder.
    
    Parameters
    ----------
    filename : str
        The filename to use (default: "merged.md")
        
    Returns
    -------
    Path
        Path to the file in the Downloads folder
    """
    downloads = Path.home() / "Downloads"
    downloads.mkdir(exist_ok=True)  # Ensure Downloads folder exists
    
    # If file already exists, add a number suffix
    output_path = downloads / filename
    if output_path.exists():
        base = output_path.stem
        ext = output_path.suffix
        counter = 1
        while output_path.exists():
            output_path = downloads / f"{base}_{counter}{ext}"
            counter += 1
    
    return output_path 
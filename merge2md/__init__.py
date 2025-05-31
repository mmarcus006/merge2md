"""Top-level package for merge2md.

Exposes a compact public API (`convert_and_merge`) so other Python
programs—or your Automator script—can call the core logic directly.
"""
from pathlib import Path
from typing import Iterable, Optional

from .converter import DoclingMarkdownConverter, ConversionSettings
from .merger import MarkdownMerger
from .notifier import get_default_output_path, show_completion_dialog

__all__ = ["convert_and_merge", "ConversionSettings", "DoclingMarkdownConverter", 
         "get_default_output_path", "show_completion_dialog"]
__version__: str = "0.1.0"

def convert_and_merge(
    paths: Iterable[Path],
    output: Optional[Path] = None,
    *,
    title: Optional[str] = None,
    settings: Optional[ConversionSettings] = None,
    show_notification: bool = True,
) -> Path:
    """
    Convert *paths* to Markdown (via Docling) and merge into *output*.

    Parameters
    ----------
    paths
        Collection of file paths or `Path` objects.
    output
        Destination path. If None, uses "merged.md" in Downloads folder.
        Extension determines output format: `.md` for Markdown, `.pdf` for PDF.
    title
        Optional H1 heading inserted at the top of the merged document.
    settings
        Optional `ConversionSettings` instance for fine-tuning OCR.
    show_notification
        Whether to show a completion notification (macOS only).

    Returns
    -------
    Path
        The *output* path, for convenience.
    """
    # Determine output path
    if output is None:
        output = get_default_output_path("merged.md")
    elif not output.parent.parts:
        # If only filename provided, put in Downloads
        output = get_default_output_path(output.name)
    
    try:
        converter = DoclingMarkdownConverter(settings=settings)
        md_blocks = converter.to_markdown(paths)
        merger = MarkdownMerger()
        merged_md = merger.merge(md_blocks, header=title)
        merger.export(merged_md, output)
        
        if show_notification:
            show_completion_dialog(output, success=True)
        
        return output
    except Exception as e:
        if show_notification:
            show_completion_dialog(output, success=False)
        raise
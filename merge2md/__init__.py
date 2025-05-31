"""Top-level package for merge2md.

Exposes a compact public API (`convert_and_merge`) so other Python
programs—or your Automator script—can call the core logic directly.
"""
from pathlib import Path
from typing import Iterable, Optional

from .converter import DoclingMarkdownConverter, ConversionSettings
from .merger import MarkdownMerger

__all__ = ["convert_and_merge", "ConversionSettings", "DoclingMarkdownConverter"]
__version__: str = "0.1.0"


def convert_and_merge(
    paths: Iterable[Path],
    output: Path,
    *,
    title: Optional[str] = None,
    settings: Optional[ConversionSettings] = None,
) -> Path:
    """
    Convert *paths* to Markdown (via Docling) and merge into *output*.

    Parameters
    ----------
    paths
        Collection of file paths or `Path` objects.
    output
        Destination path.  Extension determines output format:
        `.md` for Markdown, `.pdf` for PDF.
    title
        Optional H1 heading inserted at the top of the merged document.
    settings
        Optional `ConversionSettings` instance for fine-tuning OCR.

    Returns
    -------
    Path
        The *output* path, for convenience.
    """
    converter = DoclingMarkdownConverter(settings=settings)
    md_blocks = converter.to_markdown(paths)
    merger = MarkdownMerger()
    merged_md = merger.merge(md_blocks, header=title)
    merger.export(merged_md, output)
    return output
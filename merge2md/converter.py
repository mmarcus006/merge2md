"""
High-level wrapper around Docling's :class:`DocumentConverter`.

Separating this logic keeps I/O, OCR fine-tuning, and exception
handling in one place so the CLI (and any GUI later) can stay lean.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Sequence

from docling.document_converter import DocumentConverter
from docling.ocr.easyocr import EasyOcrOptions
from docling.core.errors import DoclingConversionError

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class ConversionSettings:
    """User-tunable knobs for Docling + EasyOCR."""

    ocr: bool = True
    languages: Sequence[str] = field(default_factory=lambda: ["en"])
    dpi: int = 300  # Higher dpi improves OCR but slows conversion.
    # Add more Docling options as needed (table model, layout model, …).

    def to_ocr_options(self) -> EasyOcrOptions | None:
        """Translate settings to Docling's `EasyOcrOptions`."""
        if not self.ocr:
            return None
        return EasyOcrOptions(languages=list(self.languages), dpi=self.dpi)


class DoclingMarkdownConverter:
    """
    Convert arbitrary files to Markdown strings using Docling.

    Example
    -------
    >>> conv = DoclingMarkdownConverter()
    >>> md = conv.to_markdown([Path("report.pdf")])[0]
    """

    def __init__(self, settings: ConversionSettings | None = None) -> None:
        self.settings = settings or ConversionSettings()
        self._converter = DocumentConverter(
            ocr_options=self.settings.to_ocr_options()
        )

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #
    def to_markdown(self, paths: Iterable[Path]) -> List[str]:
        """
        Convert *paths* (any supported format) to Markdown.

        Files that fail conversion are logged and skipped.

        Returns
        -------
        list[str]
            Markdown blocks in the same order as *paths*.
        """
        md_blocks: list[str] = []

        for path in paths:
            if not path.exists():  # guard clause
                logger.warning("Missing file: %s – skipping", path)
                continue

            try:
                logger.info("Converting %s …", path.name)
                md_blocks.append(self._converter.convert_to_markdown(path).content)
            except DoclingConversionError as exc:
                logger.error("Docling failed on %s (%s)", path, exc)

        return md_blocks
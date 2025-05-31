"""
High-level wrapper around Docling's :class:`DocumentConverter`.

Separating this logic keeps I/O, OCR fine-tuning, and exception
handling in one place so the CLI (and any GUI later) can stay lean.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Sequence, Optional, Dict, Any

from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, EasyOcrOptions
from docling.document_converter import PdfFormatOption, WordFormatOption
from docling.pipeline.simple_pipeline import SimplePipeline
from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline
from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class ConversionSettings:
    """User-tunable knobs for Docling + EasyOCR."""

    ocr: bool = True
    languages: Sequence[str] = field(default_factory=lambda: ["en"])
    dpi: int = 300  # Higher dpi improves OCR but slows conversion.
    # Supported formats - all formats that Docling can handle
    allowed_formats: List[InputFormat] = field(default_factory=lambda: [
        InputFormat.PDF,
        InputFormat.IMAGE,
        InputFormat.DOCX,
        InputFormat.HTML,
        InputFormat.PPTX,
        InputFormat.ASCIIDOC,
        InputFormat.CSV,
        InputFormat.MD,
    ])

    def to_pipeline_options(self) -> PdfPipelineOptions:
        """Create pipeline options with OCR settings."""
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = self.ocr
        if self.ocr:
            pipeline_options.ocr_options = EasyOcrOptions(
                lang=list(self.languages)
            )
        return pipeline_options


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
        
        # Create format options for different file types
        format_options: Dict[InputFormat, Any] = {}
        
        # PDF format with OCR options
        format_options[InputFormat.PDF] = PdfFormatOption(
            pipeline_cls=StandardPdfPipeline,
            backend=PyPdfiumDocumentBackend,
            pipeline_options=self.settings.to_pipeline_options()
        )
        
        # Word format with simple pipeline
        format_options[InputFormat.DOCX] = WordFormatOption(
            pipeline_cls=SimplePipeline
        )
        
        # Create converter with all supported formats
        self._converter = DocumentConverter(
            allowed_formats=self.settings.allowed_formats,
            format_options=format_options
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
                # Convert document
                result = self._converter.convert(str(path))
                # Export to markdown
                if result and result.document:
                    md_content = result.document.export_to_markdown()
                    md_blocks.append(md_content)
                else:
                    logger.error("No document content for %s", path)
            except Exception as exc:
                logger.error("Docling failed on %s (%s)", path, exc)

        return md_blocks
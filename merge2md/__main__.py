"""
Command-line interface for merge2md.

Usage
-----
$ python -m merge2md *.pdf *.docx -o merged.pdf --title "Pack"
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from .converter import ConversionSettings, DoclingMarkdownConverter
from .merger import MarkdownMerger
from .utils import natural_sort

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d | %(message)s",
)

LOGGER = logging.getLogger(__name__)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="merge2md",
        description="Batch-convert files to Markdown and merge into one doc/PDF. "
                    "Supports PDF, Word (DOCX), PowerPoint (PPTX), HTML, CSV, "
                    "Markdown, AsciiDoc, and image files.",
    )
    ap.add_argument(
        "files", 
        nargs="+", 
        help="One or more files or glob patterns. Supported formats: "
             "PDF, DOCX, PPTX, HTML, CSV, MD, AsciiDoc, images (PNG, JPG, etc.)"
    )
    ap.add_argument("-o", "--output", default="merged.md", help="Output path")
    ap.add_argument("--title", help="Optional H1 title in the merged file")
    ap.add_argument("--threads", type=int, default=4, help="Parallel workers")
    ap.add_argument(
        "--lang",
        dest="languages",
        action="append",
        help="Language code for OCR (can be used multiple times)",
    )
    ap.add_argument("--no-ocr", action="store_true", help="Disable OCR entirely")
    return ap.parse_args(argv)


def _collect_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        p = Path(pattern)
        paths.extend(p.parent.glob(p.name))
    return natural_sort(paths)


def main(argv: list[str] | None = None) -> None:  # pragma: no cover
    args = _parse_args(argv)
    paths = _collect_paths(args.files)
    if not paths:
        LOGGER.error("No files matched.")
        sys.exit(1)

    settings = ConversionSettings(
        ocr=not args.no_ocr,
        languages=args.languages or ["en"],
    )
    converter = DoclingMarkdownConverter(settings=settings)
    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        md_blocks = pool.submit(converter.to_markdown, paths).result()

    merger = MarkdownMerger()
    merged = merger.merge(md_blocks, header=args.title)
    merger.export(merged, Path(args.output))


if __name__ == "__main__":  # pragma: no cover
    main()
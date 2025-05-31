"""
Markdown concatenation and optional PDF export.

Uses **pandoc** via pypandoc *if available*, else falls back to a
sub-process call so the code works even if pypandoc isn't installed.
"""
from __future__ import annotations

import logging
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)

try:
    import pypandoc

    _HAS_PYPANDOC = True
except ImportError:  # pragma: no cover
    _HAS_PYPANDOC = False


class MarkdownMerger:
    """Merge Markdown blocks and export `.md` or `.pdf`."""

    SEP: str = "\n\n---\n\n"

    # ------------------------------------------------------------------ #
    # Public helpers
    # ------------------------------------------------------------------ #
    def merge(self, md_blocks: List[str], *, header: Optional[str] = None) -> str:
        """
        Stitch Markdown pieces together with a horizontal-rule separator.

        Parameters
        ----------
        md_blocks
            Individual Markdown fragments.
        header
            Optional H1 heading injected *once* at the very top.

        Returns
        -------
        str
            Single Markdown document.
        """
        merged: list[str] = []
        if header:
            merged.append(f"# {header}")

        if not md_blocks:  # guard clause
            return self.SEP.join(merged) if merged else ""

        merged.extend(block.strip() for block in md_blocks)
        return self.SEP.join(merged)

    # ------------------------------------------------------------------ #
    # Export
    # ------------------------------------------------------------------ #
    def export(self, merged_md: str, out_path: Path) -> None:
        """
        Write *merged_md* to *out_path*.

        * If `out_path.suffix == ".md"` → write as UTF-8 text.
        * If `== ".pdf"` → round-trip through Pandoc.
        """
        logger.info("Writing %s", out_path)
        suffix = out_path.suffix.lower()

        if suffix == ".md":
            out_path.write_text(merged_md, encoding="utf-8")
        elif suffix == ".pdf":
            self._markdown_to_pdf(merged_md, out_path)
        else:  # pragma: no cover
            raise ValueError(f"Unsupported output format: {suffix}")

    # ------------------------------------------------------------------ #
    # Private helpers
    # ------------------------------------------------------------------ #
    def _markdown_to_pdf(self, markdown: str, out_path: Path) -> None:
        """Convert *markdown* → PDF via Pandoc."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as tmp:
            tmp.write(markdown.encode())

        if _HAS_PYPANDOC:
            pypandoc.convert_file(tmp.name, "pdf", outputfile=str(out_path))
        else:
            if not shutil.which("pandoc"):  # pragma: no cover
                raise RuntimeError("pandoc not found (brew install pandoc)")
            subprocess.run(
                ["pandoc", tmp.name, "-o", str(out_path)],
                check=True,
            )
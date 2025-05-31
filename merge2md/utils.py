"""Utility helpers that don't deserve an external dependency."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List


def natural_sort(paths: Iterable[Path]) -> List[Path]:
    """
    Return *paths* sorted in “natural” (human) order.

    So `file2.pdf` comes before `file10.pdf`.
    """
    def _key(p: Path):
        parts = re.split(r"(\\d+)", p.name)
        return [int(part) if part.isdigit() else part.lower() for part in parts]

    return sorted(paths, key=_key)
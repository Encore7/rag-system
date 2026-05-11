from __future__ import annotations

import hashlib
from pathlib import Path


def sha256_file(path: Path) -> str:
    """_summary_

    Args:
        path (Path): path to file

    Returns:
        str: SHA256 hash of the file contents
    """
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

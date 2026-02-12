"""Core configuration for the app, loaded from environment variables."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Core configuration for the app, loaded from environment variables."""

    database_url: str
    inbox_dir: Path
    out_dir: Path

    processed_dir: Path
    failed_dir: Path

    # scheduling + safety
    max_retries: int
    run_limit: int
    max_wall_s: int
    claim_limit: int
    lease_ttl_s: int
    poll_s: float
    mode: str  # batch|daemon

    # arxiv
    arxiv_categories: str
    arxiv_max_results: int


def load_settings() -> Settings:
    """
    Docstring for load_settings

    :return: Settings object containing the configuration loaded from environment variables
    :rtype: Settings
    """
    database_url = os.environ["DATABASE_URL"]

    inbox_dir = Path(os.environ.get("INBOX_DIR", "data/inbox"))
    out_dir = Path(os.environ.get("OUT_DIR", "data/out"))

    processed_dir = out_dir / "processed"
    failed_dir = out_dir / "failed"

    max_retries = int(os.environ.get("MAX_RETRIES", "2"))
    run_limit = int(os.environ.get("RUN_LIMIT", "200"))
    max_wall_s = int(os.environ.get("MAX_WALL_S", "3600"))
    claim_limit = int(os.environ.get("CLAIM_LIMIT", "25"))
    lease_ttl_s = int(os.environ.get("LEASE_TTL_S", "1800"))
    poll_s = float(os.environ.get("POLL_S", "5"))
    mode = os.environ.get("MODE", "batch").lower()

    arxiv_categories = os.environ.get("ARXIV_CATEGORIES", "cs.LG stat.ML")
    arxiv_max_results = int(os.environ.get("ARXIV_MAX_RESULTS", "200"))

    if mode not in {"batch", "daemon"}:
        raise ValueError(f"MODE must be batch|daemon, got: {mode}")

    return Settings(
        database_url=database_url,
        inbox_dir=inbox_dir,
        out_dir=out_dir,
        processed_dir=processed_dir,
        failed_dir=failed_dir,
        max_retries=max_retries,
        run_limit=run_limit,
        max_wall_s=max_wall_s,
        claim_limit=claim_limit,
        lease_ttl_s=lease_ttl_s,
        poll_s=poll_s,
        mode=mode,
        arxiv_categories=arxiv_categories,
        arxiv_max_results=arxiv_max_results,
    )

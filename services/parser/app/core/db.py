from __future__ import annotations

import psycopg
from psycopg.rows import tuple_row

from services.parser.app.core.config import Settings


def connect(settings: Settings) -> psycopg.Connection:
    """_summary_

    Args:
        settings (Settings): config object containing database_url

    Returns:
        psycopg.Connection: database connection
    """
    return psycopg.connect(settings.database_url, row_factory=tuple_row)

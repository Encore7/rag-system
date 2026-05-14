"""Metrics for the app."""

from __future__ import annotations

from prometheus_client import Counter, Histogram

DOCS_DISCOVERED = Counter("docs_discovered_total", "PDFs discovered in inbox")
DOCS_CLAIMED = Counter("docs_claimed_total", "Docs claimed for processing")
DOCS_PARSED = Counter("docs_parsed_total", "Docs parsed successfully")
DOCS_FAILED = Counter("docs_failed_total", "Docs failed")
PARSE_SECONDS = Histogram("parse_seconds", "Time spent parsing a document")
ELEMENTS_EMITTED = Histogram("elements_emitted", "Elements emitted per doc")

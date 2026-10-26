"""The official SingStat Table Builder page for a table ID -- one rule for all of Sage.

Table Builder files tables by type, and the page address includes it:
  M...  time series          https://tablebuilder.singstat.gov.sg/table/TS/Mxxxxxx
  D...  data cubes           https://tablebuilder.singstat.gov.sg/table/DC/D...
  C...  cross-tabulations    https://tablebuilder.singstat.gov.sg/table/CT/Cxxxxxx
Several places used to hard-code /TS/, which gave broken links for C... tables and
made source checks reject them ("official-source-mismatch").

Used by: ui/question_bank.py, utils/chart_gallery.py, utils/core_secure.py,
utils/discovery_controller.py, utils/hybrid_discovery.py, utils/kb.py,
utils/pipeline_audit.py, utils/scope_chart_bridge.py, utils/table_tools.py.
"""

from __future__ import annotations

import re

BASE = "https://tablebuilder.singstat.gov.sg"


def table_section(table_id: str) -> str:
    """Table Builder section for an ID: TS (M...), DC (D...) or CT (other)."""
    tid = str(table_id or "").strip().upper()
    return "TS" if tid.startswith("M") else "DC" if tid.startswith("D") else "CT"


def table_page_url(table_id: str) -> str:
    """Official page URL for a lettered table ID; '' for anything else (e.g. legacy numeric IDs)."""
    tid = str(table_id or "").strip().upper()
    if not re.fullmatch(r"[A-Z][A-Z0-9]{2,18}", tid):
        return ""
    return f"{BASE}/table/{table_section(tid)}/{tid}"


def table_page_path(table_id: str) -> str:
    """The URL path of a table's official page ("" for an invalid ID)."""
    url = table_page_url(table_id)
    return url[len(BASE) :] if url else ""

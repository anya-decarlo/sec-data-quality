"""SEC EDGAR access layer.

Pulls companyfacts payloads from data.sec.gov and caches them under
data/raw/ so runs are reproducible and we stay polite to EDGAR's
10-request/second fair-use limit. Raw JSON is kept verbatim: the accession
numbers inside it are the lineage anchors for every number we emit.

SEC asks automated clients to send a User-Agent with contact info; set
SEC_USER_AGENT or pass --user-agent on the CLI.
"""

from __future__ import annotations

import json
import os
import time
import urllib.request
from pathlib import Path

from .models import Fact

DEFAULT_USER_AGENT = "sec-data-quality-portfolio contact@example.com"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"


def _get_json(url: str, user_agent: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ticker_to_cik(ticker: str, user_agent: str, cache_dir: Path) -> int:
    """Resolve a ticker to a CIK via EDGAR's published mapping (cached)."""
    cache = cache_dir / "company_tickers.json"
    if cache.exists():
        mapping = json.loads(cache.read_text())
    else:
        mapping = _get_json(TICKERS_URL, user_agent)
        cache.write_text(json.dumps(mapping))
    for row in mapping.values():
        if row["ticker"].upper() == ticker.upper():
            return int(row["cik_str"])
    raise KeyError(f"ticker {ticker!r} not found in EDGAR mapping")


def fetch_companyfacts(
    ticker: str,
    raw_dir: Path,
    user_agent: str = DEFAULT_USER_AGENT,
    pause: float = 0.2,
) -> Path:
    """Download (or reuse cached) companyfacts JSON for a ticker."""
    raw_dir.mkdir(parents=True, exist_ok=True)
    cik = ticker_to_cik(ticker, user_agent, raw_dir)
    out = raw_dir / f"CIK{cik:010d}_{ticker.upper()}.json"
    if out.exists():
        return out
    time.sleep(pause)  # stay well under the fair-use rate
    payload = _get_json(FACTS_URL.format(cik=cik), user_agent)
    out.write_text(json.dumps(payload))
    return out


def load_facts(path: Path) -> list[Fact]:
    """Flatten a companyfacts payload into Fact records."""
    payload = json.loads(path.read_text())
    entity = payload.get("entityName", "unknown")
    cik = int(payload["cik"])
    facts: list[Fact] = []
    for taxonomy, tags in payload.get("facts", {}).items():
        for tag, meta in tags.items():
            label = meta.get("label", tag)
            for unit, rows in meta.get("units", {}).items():
                for r in rows:
                    facts.append(
                        Fact(
                            entity=entity,
                            cik=cik,
                            taxonomy=taxonomy,
                            tag=tag,
                            label=label,
                            unit=unit,
                            val=r.get("val"),
                            start=r.get("start"),
                            end=r.get("end"),
                            fy=r.get("fy"),
                            fp=r.get("fp"),
                            form=r.get("form"),
                            filed=r.get("filed"),
                            accn=r.get("accn"),
                            frame=r.get("frame"),
                        )
                    )
    return facts

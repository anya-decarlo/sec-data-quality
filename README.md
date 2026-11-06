# sec-data-quality

Data-quality checks, reconciliation reports, issue logs, and lineage
documentation for SEC EDGAR financial data — built to answer two questions
for every number the pipeline emits:

1. **Where did this number come from?** (lineage)
2. **Is it fit for use?** (fitness verdict)

Zero-dependency Python 3 (stdlib only). Data source is SEC EDGAR's public
XBRL `companyfacts` API, which returns every tagged fact a company has
reported — each stamped with the filing's accession number, form, and filed
date. Those accession numbers are the lineage anchors.

## Quick start

```bash
# offline demo on synthetic data with planted defects — no network needed
python3 -m sec_data_quality sample

# real data (caches raw JSON under data/raw/, reruns are offline)
python3 -m sec_data_quality run --tickers AAPL MSFT

# reuse whatever is already cached, or pick specific XBRL tags
python3 -m sec_data_quality run --offline
python3 -m sec_data_quality run --tickers TSLA --metrics Assets NetIncomeLoss

# tests
python3 -m unittest discover -s tests
```

SEC asks automated clients to identify themselves; set `SEC_USER_AGENT`
(e.g. `"your-app you@example.com"`) — a placeholder default is used
otherwise.

## Deliverables (written to `outputs/`)

| File | What it proves |
|---|---|
| `issue_log.csv` | Every finding: stable rule ID, severity (INFO/WARN/ERROR), entity, tag, period, message, and the fact indices affected |
| `lineage.csv` / `.jsonl` | One row per emitted number: value + the exact filing it came from (`source_filing_accn`, `source_form`, `source_filed_date`, EDGAR endpoint) and its fitness verdict |
| `reconciliation.csv` + `summary.md` | Cross-filing and quarters-vs-annual comparisons with MATCH / RESTATED / MISMATCH / PASS / FAIL / IMPLIED verdicts |
| `fitness_summary.csv` | FIT / REVIEW / NOT-FIT counts per entity and tag — a headline answer to "is this data usable" |
| `summary.md` | Human-readable run report tying it all together |

## Fitness verdicts

- **FIT** — no findings attached; use it.
- **REVIEW** — WARN attached (e.g. the number was restated and resolved);
  a human should glance before relying on it.
- **NOT-FIT** — ERROR attached (filings disagree, impossible value, missing
  lineage) or the number was superseded by a later filing.

## Checks

| Rule | Severity | What it catches |
|---|---|---|
| DQ001 | ERROR | Fact missing `accn`/`filed`/`end` — can't establish lineage |
| DQ002 | WARN | Identical fact reported twice within one filing |
| DQ003 | ERROR/WARN | Start ≥ end, or duration implausible for any reported period |
| DQ004 | ERROR | Negative value where the tag cannot be negative (revenue, assets…) |
| DQ005 | WARN | Same tag reported under multiple units (USD vs USD/shares mix) |
| DQ006 | WARN | >20× year-over-year swing — usually a thousands-vs-dollars unit error |
| REC001 | WARN | Same period restated in a later filing (later filing wins) |
| REC002 | ERROR | Same period reported with different values, no clean resolution |
| REC003 | ERROR | Sum of quarterly facts doesn't tie to the annual figure (±0.5%) |

### Reconciliation details

- **CROSS_FILING**: same tag + same period compared across distinct
  filings. Values that agree are MATCH; a later filing reporting a
  different value is RESTATED (the superseded facts are marked NOT-FIT in
  lineage); unresolved disagreement is MISMATCH.
- **QUARTERS_VS_ANNUAL**: the four quarter-length facts inside a fiscal
  year should sum to the annual figure. Note this *legitimately* fails for
  diluted EPS — per-share values don't add when the share count moves —
  which is exactly the kind of thing an issue log exists to record.
- **IMPLIED_Q4**: companies almost never tag a standalone Q4 fact, so when
  exactly three quarters are reported the pipeline derives the fourth as
  `annual − Q1−Q2−Q3` and records it as a derived number, not a sourced one.

## Methodology notes / gotchas baked into the rules

- `fp` in companyfacts is the **filing's** fiscal period, not the fact's
  duration — a 9-month YTD fact in a Q3 10-Q is correctly ~272 days.
  Period checks therefore use duration bounds, not `fp` labels.
- `*IncomeLoss` tags can legitimately be negative (a loss), so the sign
  check only covers tags where negative is impossible.
- Reconciliation picks the **latest-filed** fact per filing per period, so
  amendments (10-K/A, 10-Q/A) correctly supersede the originals.
- Quarterly tie-out compares against the latest annual value; mixing an
  original quarter with a restated annual is a real, flagged failure.

## Layout

```
sec_data_quality/
  edgar.py        fetch + cache EDGAR payloads; parse to Fact records
  checks.py       DQ001–DQ006 quality rules
  reconcile.py    cross-filing + quarters-vs-annual reconciliation
  fitness.py      per-number fitness verdicts, supersession
  report.py       writes the five deliverables
  pipeline.py     orchestration
  cli.py          `sample` / `fetch` / `run`
  sample_data.py  synthetic issuer with planted defects (offline demo)
tests/            unittest suite over the synthetic payload
data/raw/         cached EDGAR JSON (reproducibility + rate-limit hygiene)
outputs/          generated deliverables
```

## Ideas this doesn't cover yet

- Frames API cross-checks (`/api/xbrl/frames`) to compare an entity's
  value against the population-wide figure for the same period
- Segment/dimensional data — companyfacts drops dimensioned facts, so
  segment-level reconciliation needs the filing XBRL itself
- Severity-weighted per-entity quality score

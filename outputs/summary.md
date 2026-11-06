# Data Quality & Reconciliation Report

- Entities: Apple Inc., MICROSOFT CORP
- Facts examined: 2,976
- Findings: 79 (ERROR 32, WARN 47, INFO 0)
- Reconciliations run: 1,023

## Fitness for use

| FIT | REVIEW | NOT-FIT |
|---|---|---|
| 2,706 | 91 | 179 |

## Reconciliation detail

### Cross Filing

(889 comparisons; 70 non-MATCH shown, capped at 100 — full detail in reconciliation.csv)

| Entity | Tag | Period | Left | Right | Δ | Verdict |
|---|---|---|---|---|---|---|
| Apple Inc. | `Assets` | as of 2008-09-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 39,572,000,000 | 10-K filed 2010-10-27 (accn 0001193125-10-238044): 36,171,000,000 | -3,401,000,000 | MISMATCH |
| Apple Inc. | `Assets` | as of 2009-09-26 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 53,851,000,000 | 10-K filed 2011-10-26 (accn 0001193125-11-282113): 47,501,000,000 | -6,350,000,000 | RESTATED |
| Apple Inc. | `Assets` | as of 2015-09-26 | 10-K filed 2015-10-28 (accn 0001193125-15-356351): 290,479,000,000 | 10-K filed 2016-10-26 (accn 0001628280-16-020309): 290,345,000,000 | -134,000,000 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2007-09-30..2008-09-27 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 5.36 | 10-K filed 2010-10-27 (accn 0001193125-10-238044): 6.78 | +1.42 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2008-09-28..2009-06-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 4.47 | 10-Q filed 2010-07-21 (accn 0001193125-10-162840): 6.30 | +1.83 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2009-03-29..2009-06-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 1.35 | 10-K filed 2010-10-27 (accn 0001193125-10-238044): 2.01 | +0.66 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2008-09-28..2009-09-26 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 6.29 | 10-K filed 2011-10-26 (accn 0001193125-11-282113): 9.08 | +2.79 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2011-09-25..2012-09-29 | 10-K filed 2012-10-31 (accn 0001193125-12-444068): 44.15 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 6.31 | -37.84 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2012-09-30..2012-12-29 | 10-Q filed 2013-01-24 (accn 0001193125-13-022339): 13.81 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 1.97 | -11.84 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2012-12-30..2013-03-30 | 10-Q filed 2013-04-24 (accn 0001193125-13-168288): 10.09 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 1.44 | -8.65 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2012-09-30..2013-06-29 | 10-Q filed 2013-07-24 (accn 0001193125-13-300670): 31.44 | 10-Q filed 2014-07-23 (accn 0001193125-14-277160): 4.49 | -26.95 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2013-03-31..2013-06-29 | 10-Q filed 2013-07-24 (accn 0001193125-13-300670): 7.47 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 1.07 | -6.40 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2012-09-30..2013-09-28 | 10-K filed 2013-10-30 (accn 0001193125-13-416534): 39.75 | 10-K filed 2015-10-28 (accn 0001193125-15-356351): 5.68 | -34.07 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2013-06-30..2013-09-28 | 10-K filed 2013-10-30 (accn 0001193125-13-416534): 8.26 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 1.18 | -7.08 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2013-09-29..2013-12-28 | 10-Q filed 2014-01-28 (accn 0001193125-14-024487): 14.50 | 10-K filed 2015-10-28 (accn 0001193125-15-356351): 2.07 | -12.43 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2013-09-29..2014-03-29 | 10-Q filed 2014-04-24 (accn 0001193125-14-157311): 26.16 | 10-Q filed 2015-04-28 (accn 0001193125-15-153166): 3.74 | -22.42 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2013-12-29..2014-03-29 | 10-Q filed 2014-04-24 (accn 0001193125-14-157311): 11.62 | 10-K filed 2015-10-28 (accn 0001193125-15-356351): 1.66 | -9.96 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2017-10-01..2018-09-29 | 10-K filed 2018-11-05 (accn 0000320193-18-000145): 11.91 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 2.98 | -8.93 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2018-09-30..2018-12-29 | 10-Q filed 2019-01-30 (accn 0000320193-19-000010): 4.18 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 1.05 | -3.13 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2018-12-30..2019-03-30 | 10-Q filed 2019-05-01 (accn 0000320193-19-000066): 2.46 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 0.61 | -1.85 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2019-03-31..2019-06-29 | 10-Q filed 2019-07-31 (accn 0000320193-19-000076): 2.18 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 0.55 | -1.63 | MISMATCH |
| Apple Inc. | `EarningsPerShareDiluted` | 2018-09-30..2019-09-28 | 10-K filed 2019-10-31 (accn 0000320193-19-000119): 11.89 | 10-K filed 2021-10-29 (accn 0000320193-21-000105): 2.97 | -8.92 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2019-06-30..2019-09-28 | 10-K filed 2019-10-31 (accn 0000320193-19-000119): 3.03 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 0.76 | -2.27 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2019-09-29..2019-12-28 | 10-Q filed 2020-01-29 (accn 0000320193-20-000010): 4.99 | 10-Q filed 2021-01-28 (accn 0000320193-21-000010): 1.25 | -3.74 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2019-09-29..2020-03-28 | 10-Q filed 2020-05-01 (accn 0000320193-20-000052): 7.56 | 10-Q filed 2021-04-29 (accn 0000320193-21-000056): 1.89 | -5.67 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2019-12-29..2020-03-28 | 10-Q filed 2020-05-01 (accn 0000320193-20-000052): 2.55 | 10-Q filed 2021-04-29 (accn 0000320193-21-000056): 0.64 | -1.91 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2019-09-29..2020-06-27 | 10-Q filed 2020-07-31 (accn 0000320193-20-000062): 10.16 | 10-Q filed 2021-07-28 (accn 0000320193-21-000065): 2.54 | -7.62 | RESTATED |
| Apple Inc. | `EarningsPerShareDiluted` | 2020-03-29..2020-06-27 | 10-Q filed 2020-07-31 (accn 0000320193-20-000062): 2.58 | 10-Q filed 2021-07-28 (accn 0000320193-21-000065): 0.65 | -1.93 | RESTATED |
| Apple Inc. | `NetIncomeLoss` | 2006-10-01..2007-09-29 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 3,496,000,000 | 10-K/A filed 2010-01-25 (accn 0001193125-10-012091): 3,495,000,000 | -1,000,000 | RESTATED |
| Apple Inc. | `NetIncomeLoss` | 2007-09-30..2008-09-27 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 4,834,000,000 | 10-K filed 2010-10-27 (accn 0001193125-10-238044): 6,119,000,000 | +1,285,000,000 | RESTATED |
| Apple Inc. | `NetIncomeLoss` | 2008-09-28..2009-06-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 4,039,000,000 | 10-Q filed 2010-07-21 (accn 0001193125-10-162840): 5,703,000,000 | +1,664,000,000 | RESTATED |
| Apple Inc. | `NetIncomeLoss` | 2009-03-29..2009-06-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 1,229,000,000 | 10-K filed 2010-10-27 (accn 0001193125-10-238044): 1,828,000,000 | +599,000,000 | RESTATED |
| Apple Inc. | `NetIncomeLoss` | 2008-09-28..2009-09-26 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 5,704,000,000 | 10-K filed 2011-10-26 (accn 0001193125-11-282113): 8,235,000,000 | +2,531,000,000 | RESTATED |
| Apple Inc. | `OperatingIncomeLoss` | 2006-10-01..2007-09-29 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 4,409,000,000 | 10-K/A filed 2010-01-25 (accn 0001193125-10-012091): 4,407,000,000 | -2,000,000 | RESTATED |
| Apple Inc. | `OperatingIncomeLoss` | 2007-09-30..2008-09-27 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 6,275,000,000 | 10-K filed 2010-10-27 (accn 0001193125-10-238044): 8,327,000,000 | +2,052,000,000 | RESTATED |
| Apple Inc. | `OperatingIncomeLoss` | 2008-09-28..2009-06-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 5,465,000,000 | 10-Q filed 2010-07-21 (accn 0001193125-10-162840): 8,056,000,000 | +2,591,000,000 | RESTATED |
| Apple Inc. | `OperatingIncomeLoss` | 2009-03-29..2009-06-27 | 10-Q filed 2009-07-22 (accn 0001193125-09-153165): 1,672,000,000 | 10-Q filed 2010-07-21 (accn 0001193125-10-162840): 2,632,000,000 | +960,000,000 | RESTATED |
| Apple Inc. | `OperatingIncomeLoss` | 2008-09-28..2009-09-26 | 10-K filed 2009-10-27 (accn 0001193125-09-214859): 7,658,000,000 | 10-K filed 2011-10-26 (accn 0001193125-11-282113): 11,740,000,000 | +4,082,000,000 | RESTATED |
| MICROSOFT CORP | `Assets` | as of 2015-06-30 | 10-K filed 2015-07-31 (accn 0001193125-15-272806): 176,223,000,000 | 10-K filed 2016-07-28 (accn 0001193125-16-662209): 174,472,000,000 | -1,751,000,000 | MISMATCH |
| MICROSOFT CORP | `Assets` | as of 2016-06-30 | 10-K filed 2016-07-28 (accn 0001193125-16-662209): 193,694,000,000 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 193,468,000,000 | -226,000,000 | RESTATED |
| MICROSOFT CORP | `Assets` | as of 2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 241,086,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 250,312,000,000 | +9,226,000,000 | RESTATED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2015-07-01..2015-09-30 | 10-Q filed 2015-10-22 (accn 0001193125-15-350718): 0.57 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 0.61 | +0.04 | RESTATED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2015-07-01..2015-12-31 | 10-Q filed 2016-01-28 (accn 0001193125-16-441821): 1.20 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 1.23 | +0.03 | RESTATED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2015-07-01..2016-06-30 | 10-K filed 2016-07-28 (accn 0001193125-16-662209): 2.10 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 2.56 | +0.46 | MISMATCH |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2016-07-01..2016-09-30 | 10-Q filed 2016-10-20 (accn 0001193125-16-742796): 0.60 | 10-Q filed 2017-10-26 (accn 0001564590-17-020171): 0.72 | +0.12 | MISMATCH |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2016-07-01..2016-12-31 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 1.26 | 10-Q filed 2018-01-31 (accn 0001564590-18-001129): 1.52 | +0.26 | RESTATED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2016-10-01..2016-12-31 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 0.66 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 0.80 | +0.14 | MISMATCH |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2016-07-01..2017-03-31 | 10-Q filed 2017-04-27 (accn 0001564590-17-007547): 1.87 | 10-Q filed 2018-04-26 (accn 0001564590-18-009307): 2.22 | +0.35 | RESTATED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2017-01-01..2017-03-31 | 10-Q filed 2017-04-27 (accn 0001564590-17-007547): 0.61 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 0.70 | +0.09 | MISMATCH |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2016-07-01..2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 2.71 | 10-K filed 2019-08-01 (accn 0001564590-19-027952): 3.25 | +0.54 | RESTATED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2017-04-01..2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 0.83 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 1.03 | +0.20 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2015-07-01..2015-09-30 | 10-Q filed 2015-10-22 (accn 0001193125-15-350718): 4,620,000,000 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 4,902,000,000 | +282,000,000 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2015-07-01..2015-12-31 | 10-Q filed 2016-01-28 (accn 0001193125-16-441821): 9,618,000,000 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 9,920,000,000 | +302,000,000 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2015-10-01..2015-12-31 | 10-Q filed 2016-01-28 (accn 0001193125-16-441821): 4,998,000,000 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 5,018,000,000 | +20,000,000 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2015-07-01..2016-06-30 | 10-K filed 2016-07-28 (accn 0001193125-16-662209): 16,798,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 20,539,000,000 | +3,741,000,000 | MISMATCH |
| MICROSOFT CORP | `NetIncomeLoss` | 2016-07-01..2016-09-30 | 10-Q filed 2016-10-20 (accn 0001193125-16-742796): 4,690,000,000 | 10-Q filed 2017-10-26 (accn 0001564590-17-020171): 5,667,000,000 | +977,000,000 | MISMATCH |
| MICROSOFT CORP | `NetIncomeLoss` | 2016-07-01..2016-12-31 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 9,890,000,000 | 10-Q filed 2018-01-31 (accn 0001564590-18-001129): 11,934,000,000 | +2,044,000,000 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2016-10-01..2016-12-31 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 5,200,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 6,267,000,000 | +1,067,000,000 | MISMATCH |
| MICROSOFT CORP | `NetIncomeLoss` | 2016-07-01..2017-03-31 | 10-Q filed 2017-04-27 (accn 0001564590-17-007547): 14,691,000,000 | 10-Q filed 2018-04-26 (accn 0001564590-18-009307): 17,420,000,000 | +2,729,000,000 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2017-01-01..2017-03-31 | 10-Q filed 2017-04-27 (accn 0001564590-17-007547): 4,801,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 5,486,000,000 | +685,000,000 | MISMATCH |
| MICROSOFT CORP | `NetIncomeLoss` | 2016-07-01..2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 21,204,000,000 | 10-K filed 2019-08-01 (accn 0001564590-19-027952): 25,489,000,000 | +4,285,000,000 | RESTATED |
| MICROSOFT CORP | `NetIncomeLoss` | 2017-04-01..2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 6,513,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 8,069,000,000 | +1,556,000,000 | RESTATED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2015-07-01..2016-06-30 | 10-K filed 2016-07-28 (accn 0001193125-16-662209): 20,182,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 26,078,000,000 | +5,896,000,000 | MISMATCH |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2016-07-01..2016-09-30 | 10-Q filed 2016-10-20 (accn 0001193125-16-742796): 5,225,000,000 | 10-Q filed 2017-10-26 (accn 0001564590-17-020171): 6,715,000,000 | +1,490,000,000 | MISMATCH |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2016-07-01..2016-12-31 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 11,402,000,000 | 10-Q filed 2018-01-31 (accn 0001564590-18-001129): 14,620,000,000 | +3,218,000,000 | RESTATED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2016-10-01..2016-12-31 | 10-Q filed 2017-01-26 (accn 0001564590-17-000654): 6,177,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 7,905,000,000 | +1,728,000,000 | MISMATCH |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2016-07-01..2017-03-31 | 10-Q filed 2017-04-27 (accn 0001564590-17-007547): 16,996,000,000 | 10-Q filed 2018-04-26 (accn 0001564590-18-009307): 21,343,000,000 | +4,347,000,000 | RESTATED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2017-01-01..2017-03-31 | 10-Q filed 2017-04-27 (accn 0001564590-17-007547): 5,594,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 6,723,000,000 | +1,129,000,000 | MISMATCH |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2016-07-01..2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 22,326,000,000 | 10-K filed 2019-08-01 (accn 0001564590-19-027952): 29,025,000,000 | +6,699,000,000 | RESTATED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2017-04-01..2017-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 5,330,000,000 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 7,682,000,000 | +2,352,000,000 | RESTATED |

### Quarters Vs Annual

(69 comparisons; 9 non-MATCH shown, capped at 100 — full detail in reconciliation.csv)

| Entity | Tag | Period | Left | Right | Δ | Verdict |
|---|---|---|---|---|---|---|
| Apple Inc. | `EarningsPerShareDiluted` | 2011-09-25..2012-09-29 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 6.31 | sum of 4 quarterly facts: 44.16 | -37.85 | FAIL |
| Apple Inc. | `EarningsPerShareDiluted` | 2017-10-01..2018-09-29 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 2.98 | sum of 4 quarterly facts: 11.87 | -8.89 | FAIL |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2007-07-01..2008-06-30 | 10-K filed 2010-07-30 (accn 0001193125-10-171791): 1.87 | sum of 4 quarterly facts: 1.88 | -0.01 | FAIL |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2012-07-01..2013-06-30 | 8-K filed 2015-10-27 (accn 0001193125-15-353706): 2.58 | sum of 4 quarterly facts: 2.60 | -0.02 | FAIL |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2014-07-01..2015-06-30 | 10-K filed 2017-08-02 (accn 0001564590-17-014900): 1.48 | sum of 4 quarterly facts: 1.46 | +0.02 | FAIL |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2015-07-01..2016-06-30 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 2.56 | sum of 4 quarterly facts: 2.09 | +0.47 | FAIL |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2017-07-01..2018-06-30 | 10-K filed 2020-07-30 (accn 0001564590-20-034944): 2.13 | sum of 4 quarterly facts: 2.11 | +0.02 | FAIL |
| MICROSOFT CORP | `NetIncomeLoss` | 2015-07-01..2016-06-30 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 20,539,000,000 | sum of 4 quarterly facts: 16,798,000,000 | +3,741,000,000 | FAIL |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2015-07-01..2016-06-30 | 10-K filed 2018-08-03 (accn 0001564590-18-019062): 26,078,000,000 | sum of 4 quarterly facts: 20,182,000,000 | +5,896,000,000 | FAIL |

### Implied Q4

(65 comparisons; 65 non-MATCH shown, capped at 100 — full detail in reconciliation.csv)

| Entity | Tag | Period | Left | Right | Δ | Verdict |
|---|---|---|---|---|---|---|
| Apple Inc. | `EarningsPerShareDiluted` | 2020-09-27..2021-09-25 | 10-K filed 2023-11-03 (accn 0000320193-23-000106): 5.61 | sum of 3 reported quarters: 4.38 | +1.23 | IMPLIED |
| Apple Inc. | `EarningsPerShareDiluted` | 2021-09-26..2022-09-24 | 10-K filed 2024-11-01 (accn 0000320193-24-000123): 6.11 | sum of 3 reported quarters: 4.82 | +1.29 | IMPLIED |
| Apple Inc. | `EarningsPerShareDiluted` | 2022-09-25..2023-09-30 | 10-K filed 2025-10-31 (accn 0000320193-25-000079): 6.13 | sum of 3 reported quarters: 4.66 | +1.47 | IMPLIED |
| Apple Inc. | `EarningsPerShareDiluted` | 2023-10-01..2024-09-28 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 6.08 | sum of 3 reported quarters: 5.11 | +0.97 | IMPLIED |
| Apple Inc. | `EarningsPerShareDiluted` | 2024-09-29..2025-09-27 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 7.46 | sum of 3 reported quarters: 5.62 | +1.84 | IMPLIED |
| Apple Inc. | `EarningsPerShareDiluted` | 2025-09-28..2026-09-26 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 8.98 | sum of 3 reported quarters: 6.87 | +2.11 | IMPLIED |
| Apple Inc. | `NetIncomeLoss` | 2020-09-27..2021-09-25 | 10-K filed 2023-11-03 (accn 0000320193-23-000106): 94,680,000,000 | sum of 3 reported quarters: 74,129,000,000 | +20,551,000,000 | IMPLIED |
| Apple Inc. | `NetIncomeLoss` | 2021-09-26..2022-09-24 | 10-K filed 2024-11-01 (accn 0000320193-24-000123): 99,803,000,000 | sum of 3 reported quarters: 79,082,000,000 | +20,721,000,000 | IMPLIED |
| Apple Inc. | `NetIncomeLoss` | 2022-09-25..2023-09-30 | 10-K filed 2025-10-31 (accn 0000320193-25-000079): 96,995,000,000 | sum of 3 reported quarters: 74,039,000,000 | +22,956,000,000 | IMPLIED |
| Apple Inc. | `NetIncomeLoss` | 2023-10-01..2024-09-28 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 93,736,000,000 | sum of 3 reported quarters: 79,000,000,000 | +14,736,000,000 | IMPLIED |
| Apple Inc. | `NetIncomeLoss` | 2024-09-29..2025-09-27 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 112,010,000,000 | sum of 3 reported quarters: 84,544,000,000 | +27,466,000,000 | IMPLIED |
| Apple Inc. | `NetIncomeLoss` | 2025-09-28..2026-09-26 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 132,175,000,000 | sum of 3 reported quarters: 101,464,000,000 | +30,711,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2008-09-28..2009-09-26 | 10-K filed 2011-10-26 (accn 0001193125-11-282113): 11,740,000,000 | sum of 3 reported quarters: 8,056,000,000 | +3,684,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2009-09-27..2010-09-25 | 8-K filed 2013-04-24 (accn 0001193125-13-170623): 18,385,000,000 | sum of 3 reported quarters: 12,938,000,000 | +5,447,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2010-09-26..2011-09-24 | 10-K filed 2013-10-30 (accn 0001193125-13-416534): 33,790,000,000 | sum of 3 reported quarters: 25,080,000,000 | +8,710,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2011-09-25..2012-09-29 | 8-K filed 2015-01-28 (accn 0001193125-15-023732): 55,241,000,000 | sum of 3 reported quarters: 44,297,000,000 | +10,944,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2012-09-30..2013-09-28 | 10-K filed 2015-10-28 (accn 0001193125-15-356351): 48,999,000,000 | sum of 3 reported quarters: 38,969,000,000 | +10,030,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2013-09-29..2014-09-27 | 10-K filed 2016-10-26 (accn 0001628280-16-020309): 52,503,000,000 | sum of 3 reported quarters: 41,338,000,000 | +11,165,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2014-09-28..2015-09-26 | 10-K filed 2017-11-03 (accn 0000320193-17-000070): 71,230,000,000 | sum of 3 reported quarters: 56,607,000,000 | +14,623,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2015-09-27..2016-09-24 | 10-K filed 2018-11-05 (accn 0000320193-18-000145): 60,024,000,000 | sum of 3 reported quarters: 48,263,000,000 | +11,761,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2016-09-25..2017-09-30 | 10-K filed 2019-10-31 (accn 0000320193-19-000119): 61,344,000,000 | sum of 3 reported quarters: 48,224,000,000 | +13,120,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2017-10-01..2018-09-29 | 10-K filed 2020-10-30 (accn 0000320193-20-000096): 70,898,000,000 | sum of 3 reported quarters: 54,780,000,000 | +16,118,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2018-09-30..2019-09-28 | 10-K filed 2021-10-29 (accn 0000320193-21-000105): 63,930,000,000 | sum of 3 reported quarters: 48,305,000,000 | +15,625,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2019-09-29..2020-09-26 | 10-K filed 2022-10-28 (accn 0000320193-22-000108): 66,288,000,000 | sum of 3 reported quarters: 51,513,000,000 | +14,775,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2020-09-27..2021-09-25 | 10-K filed 2023-11-03 (accn 0000320193-23-000106): 108,949,000,000 | sum of 3 reported quarters: 85,163,000,000 | +23,786,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2021-09-26..2022-09-24 | 10-K filed 2024-11-01 (accn 0000320193-24-000123): 119,437,000,000 | sum of 3 reported quarters: 94,543,000,000 | +24,894,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2022-09-25..2023-09-30 | 10-K filed 2025-10-31 (accn 0000320193-25-000079): 114,301,000,000 | sum of 3 reported quarters: 87,332,000,000 | +26,969,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2023-10-01..2024-09-28 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 123,216,000,000 | sum of 3 reported quarters: 93,625,000,000 | +29,591,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2024-09-29..2025-09-27 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 133,050,000,000 | sum of 3 reported quarters: 100,623,000,000 | +32,427,000,000 | IMPLIED |
| Apple Inc. | `OperatingIncomeLoss` | 2025-09-28..2026-09-26 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 158,063,000,000 | sum of 3 reported quarters: 122,432,000,000 | +35,631,000,000 | IMPLIED |
| Apple Inc. | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2020-09-27..2021-09-25 | 10-K filed 2023-11-03 (accn 0000320193-23-000106): 365,817,000,000 | sum of 3 reported quarters: 282,457,000,000 | +83,360,000,000 | IMPLIED |
| Apple Inc. | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2021-09-26..2022-09-24 | 10-K filed 2024-11-01 (accn 0000320193-24-000123): 394,328,000,000 | sum of 3 reported quarters: 304,182,000,000 | +90,146,000,000 | IMPLIED |
| Apple Inc. | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2022-09-25..2023-09-30 | 10-K filed 2025-10-31 (accn 0000320193-25-000079): 383,285,000,000 | sum of 3 reported quarters: 293,787,000,000 | +89,498,000,000 | IMPLIED |
| Apple Inc. | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2023-10-01..2024-09-28 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 391,035,000,000 | sum of 3 reported quarters: 296,105,000,000 | +94,930,000,000 | IMPLIED |
| Apple Inc. | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2024-09-29..2025-09-27 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 416,161,000,000 | sum of 3 reported quarters: 313,695,000,000 | +102,466,000,000 | IMPLIED |
| Apple Inc. | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2025-09-28..2026-09-26 | 10-K filed 2026-11-03 (accn 0000320193-26-000026): 478,834,000,000 | sum of 3 reported quarters: 364,357,000,000 | +114,477,000,000 | IMPLIED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2020-07-01..2021-06-30 | 10-K filed 2023-07-27 (accn 0000950170-23-035122): 8.05 | sum of 3 reported quarters: 5.88 | +2.17 | IMPLIED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2021-07-01..2022-06-30 | 8-K filed 2024-12-03 (accn 0000950170-24-132722): 9.65 | sum of 3 reported quarters: 7.41 | +2.24 | IMPLIED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2022-07-01..2023-06-30 | 10-K filed 2025-07-30 (accn 0000950170-25-100235): 9.68 | sum of 3 reported quarters: 7.00 | +2.68 | IMPLIED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2023-07-01..2024-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 11.80 | sum of 3 reported quarters: 8.86 | +2.94 | IMPLIED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2024-07-01..2025-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 13.64 | sum of 3 reported quarters: 9.99 | +3.65 | IMPLIED |
| MICROSOFT CORP | `EarningsPerShareDiluted` | 2025-07-01..2026-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 17.95 | sum of 3 reported quarters: 13.15 | +4.80 | IMPLIED |
| MICROSOFT CORP | `NetIncomeLoss` | 2020-07-01..2021-06-30 | 10-K filed 2023-07-27 (accn 0000950170-23-035122): 61,271,000,000 | sum of 3 reported quarters: 44,813,000,000 | +16,458,000,000 | IMPLIED |
| MICROSOFT CORP | `NetIncomeLoss` | 2021-07-01..2022-06-30 | DEF 14A filed 2026-10-21 (accn 0001193125-26-427849): 72,738,000,000 | sum of 3 reported quarters: 55,998,000,000 | +16,740,000,000 | IMPLIED |
| MICROSOFT CORP | `NetIncomeLoss` | 2022-07-01..2023-06-30 | DEF 14A filed 2026-10-21 (accn 0001193125-26-427849): 72,361,000,000 | sum of 3 reported quarters: 52,280,000,000 | +20,081,000,000 | IMPLIED |
| MICROSOFT CORP | `NetIncomeLoss` | 2023-07-01..2024-06-30 | DEF 14A filed 2026-10-21 (accn 0001193125-26-427849): 88,136,000,000 | sum of 3 reported quarters: 66,100,000,000 | +22,036,000,000 | IMPLIED |
| MICROSOFT CORP | `NetIncomeLoss` | 2024-07-01..2025-06-30 | DEF 14A filed 2026-10-21 (accn 0001193125-26-427849): 101,832,000,000 | sum of 3 reported quarters: 74,599,000,000 | +27,233,000,000 | IMPLIED |
| MICROSOFT CORP | `NetIncomeLoss` | 2025-07-01..2026-06-30 | DEF 14A filed 2026-10-21 (accn 0001193125-26-427849): 133,749,000,000 | sum of 3 reported quarters: 97,983,000,000 | +35,766,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2008-07-01..2009-06-30 | 10-K filed 2011-07-28 (accn 0001193125-11-200680): 20,363,000,000 | sum of 3 reported quarters: 16,376,000,000 | +3,987,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2009-07-01..2010-06-30 | 10-K filed 2012-07-26 (accn 0001193125-12-316848): 24,098,000,000 | sum of 3 reported quarters: 18,168,000,000 | +5,930,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2010-07-01..2011-06-30 | 8-K filed 2013-11-26 (accn 0001193125-13-455144): 27,161,000,000 | sum of 3 reported quarters: 20,990,000,000 | +6,171,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2011-07-01..2012-06-30 | 10-K filed 2014-07-31 (accn 0001193125-14-289961): 21,763,000,000 | sum of 3 reported quarters: 21,571,000,000 | +192,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2012-07-01..2013-06-30 | 8-K filed 2015-10-27 (accn 0001193125-15-353706): 26,764,000,000 | sum of 3 reported quarters: 20,691,000,000 | +6,073,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2020-07-01..2021-06-30 | 10-K filed 2023-07-27 (accn 0000950170-23-035122): 69,916,000,000 | sum of 3 reported quarters: 50,821,000,000 | +19,095,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2021-07-01..2022-06-30 | 8-K filed 2024-12-03 (accn 0000950170-24-132722): 83,383,000,000 | sum of 3 reported quarters: 62,849,000,000 | +20,534,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2022-07-01..2023-06-30 | 10-K filed 2025-07-30 (accn 0000950170-25-100235): 88,523,000,000 | sum of 3 reported quarters: 64,269,000,000 | +24,254,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2023-07-01..2024-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 109,433,000,000 | sum of 3 reported quarters: 81,508,000,000 | +27,925,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2024-07-01..2025-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 128,528,000,000 | sum of 3 reported quarters: 94,205,000,000 | +34,323,000,000 | IMPLIED |
| MICROSOFT CORP | `OperatingIncomeLoss` | 2025-07-01..2026-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 155,237,000,000 | sum of 3 reported quarters: 114,634,000,000 | +40,603,000,000 | IMPLIED |
| MICROSOFT CORP | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2020-07-01..2021-06-30 | 10-K filed 2023-07-27 (accn 0000950170-23-035122): 168,088,000,000 | sum of 3 reported quarters: 121,936,000,000 | +46,152,000,000 | IMPLIED |
| MICROSOFT CORP | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2021-07-01..2022-06-30 | 8-K filed 2024-12-03 (accn 0000950170-24-132722): 198,270,000,000 | sum of 3 reported quarters: 146,405,000,000 | +51,865,000,000 | IMPLIED |
| MICROSOFT CORP | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2022-07-01..2023-06-30 | 10-K filed 2025-07-30 (accn 0000950170-25-100235): 211,915,000,000 | sum of 3 reported quarters: 155,726,000,000 | +56,189,000,000 | IMPLIED |
| MICROSOFT CORP | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2023-07-01..2024-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 245,122,000,000 | sum of 3 reported quarters: 180,395,000,000 | +64,727,000,000 | IMPLIED |
| MICROSOFT CORP | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2024-07-01..2025-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 281,724,000,000 | sum of 3 reported quarters: 205,283,000,000 | +76,441,000,000 | IMPLIED |
| MICROSOFT CORP | `RevenueFromContractWithCustomerExcludingAssessedTax` | 2025-07-01..2026-06-30 | 10-K filed 2026-07-29 (accn 0001193125-26-323660): 331,839,000,000 | sum of 3 reported quarters: 241,832,000,000 | +90,007,000,000 | IMPLIED |

## Issue log (top 20 by severity)

- **[ERROR] REC002** — Apple Inc. `Assets` as of 2008-09-27: filings disagree on Assets: values [36171000000, 39572000000] across 4 filings
- **[ERROR] REC002** — Apple Inc. `Assets` as of 2015-09-26: filings disagree on Assets: values [290345000000, 290479000000] across 5 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2011-09-25..2012-09-29: filings disagree on EarningsPerShareDiluted: values [6.31, 44.15] across 5 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2012-09-30..2012-12-29: filings disagree on EarningsPerShareDiluted: values [1.97, 13.81] across 5 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2012-12-30..2013-03-30: filings disagree on EarningsPerShareDiluted: values [1.44, 10.09] across 5 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2013-03-31..2013-06-29: filings disagree on EarningsPerShareDiluted: values [1.07, 7.47] across 5 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2017-10-01..2018-09-29: filings disagree on EarningsPerShareDiluted: values [2.98, 11.91] across 3 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2018-09-30..2018-12-29: filings disagree on EarningsPerShareDiluted: values [1.05, 4.18] across 4 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2018-12-30..2019-03-30: filings disagree on EarningsPerShareDiluted: values [0.61, 2.46] across 4 filings
- **[ERROR] REC002** — Apple Inc. `EarningsPerShareDiluted` 2019-03-31..2019-06-29: filings disagree on EarningsPerShareDiluted: values [0.55, 2.18] across 4 filings
- **[ERROR] REC002** — MICROSOFT CORP `Assets` as of 2015-06-30: filings disagree on Assets: values [174472000000, 176223000000] across 6 filings
- **[ERROR] REC002** — MICROSOFT CORP `EarningsPerShareDiluted` 2015-07-01..2016-06-30: filings disagree on EarningsPerShareDiluted: values [2.1, 2.56] across 3 filings
- **[ERROR] REC002** — MICROSOFT CORP `EarningsPerShareDiluted` 2016-07-01..2016-09-30: filings disagree on EarningsPerShareDiluted: values [0.6, 0.72] across 3 filings
- **[ERROR] REC002** — MICROSOFT CORP `EarningsPerShareDiluted` 2016-10-01..2016-12-31: filings disagree on EarningsPerShareDiluted: values [0.66, 0.8] across 4 filings
- **[ERROR] REC002** — MICROSOFT CORP `EarningsPerShareDiluted` 2017-01-01..2017-03-31: filings disagree on EarningsPerShareDiluted: values [0.61, 0.7] across 4 filings
- **[ERROR] REC002** — MICROSOFT CORP `NetIncomeLoss` 2015-07-01..2016-06-30: filings disagree on NetIncomeLoss: values [16798000000, 20539000000] across 3 filings
- **[ERROR] REC002** — MICROSOFT CORP `NetIncomeLoss` 2016-07-01..2016-09-30: filings disagree on NetIncomeLoss: values [4690000000, 5667000000] across 3 filings
- **[ERROR] REC002** — MICROSOFT CORP `NetIncomeLoss` 2016-10-01..2016-12-31: filings disagree on NetIncomeLoss: values [5200000000, 6267000000] across 4 filings
- **[ERROR] REC002** — MICROSOFT CORP `NetIncomeLoss` 2017-01-01..2017-03-31: filings disagree on NetIncomeLoss: values [4801000000, 5486000000] across 4 filings
- **[ERROR] REC002** — MICROSOFT CORP `OperatingIncomeLoss` 2015-07-01..2016-06-30: filings disagree on OperatingIncomeLoss: values [20182000000, 26078000000] across 3 filings
- … and 59 more; see issue_log.csv

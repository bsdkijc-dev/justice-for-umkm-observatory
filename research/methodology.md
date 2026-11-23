# Research Methodology & Indicator Framework

## 1. Analytical Engine & Reproducibility
All empirical analyses are implemented in DuckDB, Pandas, PyArrow (Parquet), and Jupyter notebooks (`analysis/notebooks/01`–`12`) with strict zero-imputation rules: missing values remain null/empty with explicit completeness flags.

## 2. Fifteen Documented Indicators (IND01–IND15)

| ID | Indicator Name | Numerator | Denominator | Unit | Primary Sources | Key Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IND01** | UMKM Legal Information Access Rate | UMKM reporting access to relevant legal info | Total surveyed/observed UMKM | `%` | DS06, DS07 | Self-reported survey data cannot be generalized beyond sample frame |
| **IND02** | UMKM Formal Legal Assistance Access Rate | UMKM using licensed advocate, OBH, or Posbakum | UMKM experiencing a legal dispute | `%` | DS02, DS06, DS07 | Informal advice excluded unless documented |
| **IND03** | Dispute Resolution Cost Ratio | Direct + indirect dispute resolution costs | Clearly defined business financial measure (e.g., monthly revenue/profit) | `ratio` | DS03, DS05, DS07 | Only comparable, lawfully collected financial denominators permitted |
| **IND04** | Dispute Resolution Duration | Days from dispute/filing start_date to end_date | N/A (distribution: median, IQR, mean) | `days` | DS01, DS04, DS07 | Pre-filing negotiation duration often unobserved in court records |
| **IND05** | Unpaid Invoice Exposure | Total value or share of unpaid commercial invoices | Total commercial receivables or sampled UMKM | `IDR` / `%` | DS01, DS07 | Selection bias in litigated claims vs. unlitigated defaults |
| **IND06** | Business Interruption During Disputes | UMKM reporting operational halt/slowdown | UMKM experiencing a dispute | `%` | DS07 | Survey perception; requires triangulation with DS05 |
| **IND07** | Mediation Utilization Rate | Disputes entering court-annexed or external mediation | Total eligible disputes | `%` | DS01, DS07 | Private informal mediation rarely recorded in public registries |
| **IND08** | Documented Dispute Settlement Rate | Disputes resolved via settlement/akta perdamaian | Total documented disputes | `%` | DS01, DS07 | Excludes undocumented settlements |
| **IND09** | Evidence-Based Remedy Execution Rate | Winning claims with documented compliance/execution | Total winning claims with enforceable remedy | `%` | DS01, DS07 | Post-judgment execution records are frequently incomplete in public directories |
| **IND10** | Legal Knowledge Accessibility | Verified plain-language legal resources per topic/province | Target legal information domains | `count` / `score` | DS06, DS09 | Availability does not guarantee comprehension or uptake |
| **IND11** | Geographic Legal Service Access | Districts with verified OBH/Posbakum/court access | Total districts in target geography | `%` | DS02, DS06 | Physical presence does not measure capacity or affordability |
| **IND12** | Business Continuity After Dispute | Enterprises remaining operational post-dispute | Enterprises experiencing dispute in period | `%` | DS05, DS07 | Survey perceptions must be labeled separately from longitudinal registry survival |
| **IND13** | Employment Continuity | Workers retained during/after dispute | Pre-dispute workforce in affected UMKM | `%` | DS05, DS07 | Requires longitudinal employment records |
| **IND14** | Business Survival (Longitudinal) | UMKM active at `t + k` | UMKM cohort active at `t` | `%` | DS05 | Valid only where longitudinal business data exist; never infer from court decisions alone |
| **IND15** | Business Growth (Longitudinal) | Change in revenue/employment/productivity | Baseline economic metric | `%` | DS05 | Valid only where reliable longitudinal economic evidence exists |

> **Labeling Rule:** Never substitute survey perceptions for verified economic outcomes without explicitly labeling them as self-reported perceptions.

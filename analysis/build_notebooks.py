"""Generate all 12 reproducible Jupyter notebooks (01-12) in analysis/notebooks/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple


NOTEBOOKS: List[Tuple[str, str, str, str]] = [
    (
        "01_umkm_source_inventory.ipynb",
        "01 — UMKM Source Inventory & Governance Audit",
        "Audit official judicial, economic, legal, and legal-aid sources (`sources/official_sources.csv`).",
        "import pandas as pd\ndf = pd.read_csv('../../sources/official_sources.csv')\nprint(df[['source_id', 'source_owner', 'category', 'verification_status']].to_string(index=False))",
    ),
    (
        "02_umkm_dispute_taxonomy.ipynb",
        "02 — Standardized UMKM Dispute Taxonomy (CAT-01 to CAT-08)",
        "Validate multi-label dispute classification rules and `UNKNOWN` preservation on synthetic records.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds01_umkm_legal_disputes.parquet')\nprint(df['dispute_category'].value_counts(dropna=False))",
    ),
    (
        "03_umkm_judicial_case_analysis.ipynb",
        "03 — Judicial Case Metadata Analysis (RQ01, RQ09, RQ10)",
        "Analyze court distribution, claim patterns, outcomes, appeals, and execution status (synthetic pipeline test).",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds01_umkm_legal_disputes.parquet')\nprint(pd.crosstab(df['court_level'], df['judgment_outcome']))",
    ),
    (
        "04_umkm_geographic_distribution.ipynb",
        "04 — Geographic Distribution & Urban/Rural Access (RQ11, H6)",
        "Examine provincial and district distribution of disputes and access barriers.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds01_umkm_legal_disputes.parquet')\nprint(df.groupby(['province', 'business_size']).size().unstack(fill_value=0))",
    ),
    (
        "05_dispute_resolution_costs.ipynb",
        "05 — Dispute Resolution Costs & Cash Flow Pressure (RQ02, RQ05, H1, H4)",
        "Compare direct and indirect costs across resolution channels (synthetic pipeline test).",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds03_dispute_resolution_costs.parquet')\nprint(df.groupby('resolution_channel')[['direct_cost', 'indirect_cost']].median())",
    ),
    (
        "06_dispute_duration.ipynb",
        "06 — Dispute Duration & Operational Delays (RQ06, H2)",
        "Measure dispute duration distributions across channels and categories.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds04_dispute_duration.parquet')\nprint(df.groupby('resolution_channel')['duration_days'].describe())",
    ),
    (
        "07_contractual_security.ipynb",
        "07 — Contractual Security & Unpaid Invoices (RQ07, H5)",
        "Analyze commercial contract disputes (`CAT-01`), wanprestasi, and unpaid invoice exposure.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds01_umkm_legal_disputes.parquet')\nprint(df[df['dispute_category'] == 'CAT-01']['claim_type'].value_counts())",
    ),
    (
        "08_umkm_economic_indicators.ipynb",
        "08 — Official UMKM Economic Indicators (IND14, IND15)",
        "Evaluate macroeconomic and credit indicators with explicit denominator and period checks.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds05_umkm_economic_indicators.parquet')\nprint(df.groupby(['indicator_name', 'business_size'])['indicator_value'].mean())",
    ),
    (
        "09_access_to_justice_barriers.ipynb",
        "09 — Access to Justice Barriers & Legal Aid (RQ04, RQ08, H3, H7)",
        "Assess information, cost, distance, complexity, and trust barriers alongside legal aid coverage.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds02_umkm_access_barriers.parquet')\nprint(pd.crosstab(df['geographic_area'], df['barrier_category']))",
    ),
    (
        "10_umkm_business_resilience.ipynb",
        "10 — UMKM Business Resilience & Continuity (RQ14, H8)",
        "Evaluate business continuity and employment retention indicators without inferring survival from judgments alone.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds07_umkm_dispute_survey.parquet')\nprint(pd.crosstab(df['dispute_experience'], df['business_impact']))",
    ),
    (
        "11_survey_analysis.ipynb",
        "11 — UMKM Dispute Experience Survey Analysis (Gated Pilot)",
        "Analyze de-identified survey responses (`DS07`) with consent verification.",
        "import pandas as pd\ndf = pd.read_parquet('../../data/synthetic/ds07_umkm_dispute_survey.parquet')\nprint(df['consent_status'].value_counts())\nprint(df['resolution_channel'].value_counts())",
    ),
    (
        "12_policy_impact_framework.ipynb",
        "12 — Policy Intelligence & Evaluation Framework (RQ12, RQ13)",
        "Map validated findings to policy proposals (`DS10`) and evaluation indicators.",
        "import pandas as pd\ndf = pd.read_csv('../../data/synthetic/ds10_policy_recommendations.csv')\nprint(df[['recommendation_id', 'research_question', 'responsible_policy_area', 'review_status']].to_string(index=False))",
    ),
]


def make_notebook(title: str, desc: str, code: str) -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n\n",
                    f"{desc}\n\n",
                    "> **Notice:** Default execution loads `data/synthetic/` for pipeline verification. Never cite synthetic outputs as empirical findings.\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in code.splitlines()],
            },
        ],
    }


def main() -> None:
    out_dir = Path("analysis/notebooks")
    out_dir.mkdir(parents=True, exist_ok=True)
    for fname, title, desc, code in NOTEBOOKS:
        nb = make_notebook(title, desc, code)
        (out_dir / fname).write_text(json.dumps(nb, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {len(NOTEBOOKS)} notebooks in {out_dir}")


if __name__ == "__main__":
    main()

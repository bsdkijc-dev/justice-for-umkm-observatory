# Methodological & Data Limitations Register

1. **Non-Inference of UMKM Status in Court Records:** Public judgments in *Direktori Putusan Mahkamah Agung* rarely state a litigant's statutory PP No. 7/2021 capital or annual sales tier. Inferring UMKM status from a party's name or case title introduces severe misclassification bias and is strictly prohibited.
2. **Selection Bias in Litigated Disputes:** Court cases represent only disputes that reached formal adjudication; they exclude the vast majority of UMKM disputes resolved informally, abandoned due to cost/distance, or settled pre-filing.
3. **Incomplete Execution / Enforcement Data:** Public court directories document judgments and appeals more consistently than post-judgment *eksekusi* (enforcement) or voluntary compliance, creating a structural blind spot for **RQ10** and **IND09**.
4. **Cross-Source Compatibility:** Economic data from BPS, Kementerian UMKM, OSS, BI, and OJK use differing reporting periods, sectoral classifications, and formal vs. informal coverage. Incompatible datasets must not be merged without explicit harmonization notes.
5. **Survey & Interview Representativeness:** Convenience or association-based samples cannot be represented as nationally representative without documented probability sampling and weighting.
6. **Correlation vs. Causation:** Observational associations between legal access, dispute costs, and business survival/growth are subject to confounding (e.g., pre-existing financial distress) and must not be reported as causal effects.
7. **Synthetic Data Boundary:** All files in `data/synthetic/` are strictly for pipeline, schema, and notebook validation. They contain zero empirical findings and must never be cited as real-world evidence.

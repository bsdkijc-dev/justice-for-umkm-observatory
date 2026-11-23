# Hypothesis Register (H1–H8)

These are **testable hypotheses**, not established findings. Test them only with appropriate data, controlling for business size, sector, business age, geography, and other observable characteristics. **Do not claim causation from simple correlation.**

| ID | Hypothesis Statement | Key Variables | Control Variables | Analytical Notebook |
| :--- | :--- | :--- | :--- | :--- |
| **H1** | Higher dispute resolution costs are associated with greater financial pressure on small businesses. | `direct_cost`, `indirect_cost`, cash flow pressure | `business_size`, `business_sector`, `province`, `business_age_group` | `05_dispute_resolution_costs.ipynb` |
| **H2** | Longer unresolved payment disputes are associated with greater working capital constraints. | `duration_days`, unpaid invoice exposure, working capital | `business_size`, `business_sector`, `resolution_channel` | `06_dispute_duration.ipynb` |
| **H3** | Limited legal information is associated with lower use of formal dispute resolution. | Legal info access, `resolution_channel` | `business_size`, `province`, `digital_channel`, `formal_status` | `09_access_to_justice_barriers.ipynb` |
| **H4** | Access to appropriate mediation may reduce some dispute resolution costs. | `resolution_channel = mediation`, `direct_cost`, `duration_days` | `dispute_category`, `business_size`, `claim_type` | `05_dispute_resolution_costs.ipynb` |
| **H5** | Contract uncertainty is associated with greater business transaction risk. | Contract clarity, breach/unpaid invoice incidence | `business_size`, `business_sector`, `formal_status` | `07_contractual_security.ipynb` |
| **H6** | Geographic distance from legal services may increase access barriers. | Urban/rural, distance to court/OBH, `barrier_category` | `province`, `district`, `digital_channel` | `04_umkm_geographic_distribution.ipynb` |
| **H7** | Businesses with access to legal assistance may demonstrate different dispute resolution experiences from businesses without assistance. | Legal assistance access, `outcome_category`, `duration_days` | `business_size`, `dispute_category`, `claim_type` | `09_access_to_justice_barriers.ipynb` |
| **H8** | Unresolved legal disputes may be associated with business interruption or closure risk. | Unresolved dispute duration, `business_impact`, continuity | `business_size`, `business_sector`, `business_age_group` | `10_umkm_business_resilience.ipynb` |

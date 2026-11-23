# Standardized UMKM Dispute Taxonomy (v1.0)

Every dispute classification in the Observatory must:
- Apply explicit **inclusion** and **exclusion** criteria.
- Record **source** and **extraction_confidence** (`0.0`–`1.0`).
- Allow **multiple dispute categories** when a case spans domains (primary category + secondary tags).
- Preserve **`UNKNOWN`** when evidence is insufficient rather than forcing a guess.

## Categories (CAT-01 to CAT-08)

### CATEGORY 01 — COMMERCIAL CONTRACTS (`CAT-01`)
- **Subcategories:** Breach of contract (`wanprestasi`), unpaid invoices, supplier disputes, distributor disputes, service agreements, contract termination.
- **Inclusion Criteria:** Civil or commercial disputes arising from written or oral business-to-business (B2B) or service agreements involving an enterprise's core commercial operations.
- **Exclusion Criteria:** Pure consumer retail complaints (use `CAT-04`), formal bank loan/credit facilities (use `CAT-02`), or employment contracts (use `CAT-05`).

### CATEGORY 02 — FINANCIAL AND CREDIT DISPUTES (`CAT-02`)
- **Subcategories:** Business loans (KUR/commercial), financing agreements (*pembiayaan*), debt collection, collateral disputes (*hak tanggungan*/*fidusia*), guarantee disputes, financial service complaints.
- **Inclusion Criteria:** Disputes with banks, BPR, multifinance, fintech lending, or cooperatives concerning credit, financing, security interests, or debt restructuring outside formal bankruptcy.
- **Exclusion Criteria:** Trade credit / unpaid B2B invoices without a financial institution (use `CAT-01`), or formal PKPU/bankruptcy proceedings (use `CAT-08`).

### CATEGORY 03 — LAND AND PROPERTY (`CAT-03`)
- **Subcategories:** Commercial lease disputes (*sewa-menyewa*), land ownership disputes, building and property disputes, business premises disputes.
- **Inclusion Criteria:** Disputes over physical premises, kiosks, workshops, warehouses, or land used for enterprise operations.
- **Exclusion Criteria:** Mortgage/collateral foreclosure where the underlying dispute is loan default (tag `CAT-02` primary, `CAT-03` secondary).

### CATEGORY 04 — CONSUMER AND MARKETPLACE (`CAT-04`)
- **Subcategories:** Consumer claims, e-commerce disputes, online marketplace transactions, product liability, refund and payment disputes.
- **Inclusion Criteria:** Disputes between an enterprise and end consumers or digital marketplace platforms regarding goods/services, refunds, platform suspension, or BPSK claims.
- **Exclusion Criteria:** B2B wholesale supply contracts (use `CAT-01`).

### CATEGORY 05 — EMPLOYMENT (`CAT-05`)
- **Subcategories:** Unpaid wages, employment agreements, termination disputes (PHK), social security obligations (BPJS), other industrial relations disputes.
- **Inclusion Criteria:** Disputes between UMKM employers and workers regarding labour rights or industrial relations.
- **Exclusion Criteria:** Independent contractor B2B service agreements (use `CAT-01`).
- **Scope Note:** Avoid duplicating the research scope of the **Indonesia Labour Justice Observatory (ILJO)**. Employment disputes are analyzed here strictly as an interconnected operational/financial risk category for UMKM, with detailed PHI labour adjudication referred to ILJO.

### CATEGORY 06 — ADMINISTRATIVE AND REGULATORY (`CAT-06`)
- **Subcategories:** Business licensing (OSS/NIB/PIRT/halal), administrative decisions (TUN), regulatory compliance, tax-related disputes, local government services (*retribusi*/zoning).
- **Inclusion Criteria:** Disputes involving government agencies, local authorities, tax authorities, or licensing bodies affecting enterprise operations.
- **Exclusion Criteria:** Purely private commercial or criminal matters.

### CATEGORY 07 — INTELLECTUAL PROPERTY (`CAT-07`)
- **Subcategories:** Trademark disputes, copyright disputes, brand infringement, licensing disputes.
- **Inclusion Criteria:** Disputes concerning registered or unregistered marks, copyrights, industrial designs, or IP licensing involving UMKM products or brands.
- **Exclusion Criteria:** General unfair competition or marketplace account disputes without an IP claim (use `CAT-04`).

### CATEGORY 08 — INSOLVENCY AND BUSINESS FAILURE (`CAT-08`)
- **Subcategories:** Debt restructuring (PKPU), bankruptcy (*kepailitan*), creditor claims, business closure, insolvency-related litigation.
- **Inclusion Criteria:** Formal PKPU, bankruptcy petitions in Commercial Court (*Pengadilan Niaga*), or legal proceedings directly tied to enterprise insolvency/liquidation.
- **Exclusion Criteria:** Routine bilateral debt collection without insolvency proceedings (use `CAT-01` or `CAT-02`).

### `UNKNOWN`
- **Inclusion Criteria:** Documented dispute where available metadata or text does not support assignment to `CAT-01` through `CAT-08` with confidence >= 0.50.

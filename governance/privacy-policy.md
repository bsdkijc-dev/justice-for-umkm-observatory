# Privacy & Re-Identification Protection Policy

1. **Data Minimization & Purpose Limitation:** Collect only variables strictly required for RQ01–RQ14.
2. **Strictly Prohibited Fields in Public Datasets:** Never publish personal identification numbers (NIK/NPWP), bank account details, private business contact details (phone/email), precise home or business street addresses, confidential contracts, non-public financial records, identifiable survey responses, or restricted judicial documents.
3. **Respondent Contact Segregation:** If operational contact details are ever needed for follow-up interviews, store them in an encrypted, access-controlled vault completely separate from research datasets, linked only by an opaque `respondent_code`.
4. **Re-Identification Risk Assessment:** Assess quasi-identifier uniqueness (e.g., rare `province` + `district` + `business_sector` + `business_size` combinations) even after direct identifiers are removed. Apply geographic aggregation or k-anonymity suppression before public release.
5. **Automated Privacy Gate:** Every dataset candidate must pass `processing/privacy_review.py` before staging for Kaggle or GitHub Pages.

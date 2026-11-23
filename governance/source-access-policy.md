# Source Access & Polite Collection Policy

1. **Access != Redistribution:** Public web availability does not grant automated mass-collection or redistribution rights. Verify license and terms of use for every source.
2. **Prefer Official Downloads & APIs:** Prioritize official bulk downloads, BPS/OJK/BI statistical tables, and JDIH legal portals over HTML scraping.
3. **Polite Web Collection Rules:**
   - Check `robots.txt` before any automated HTTP request.
   - Enforce conservative rate limits (minimum 3.0s crawl delay) and exponential backoff on HTTP 429/5xx.
   - Cache retrieved responses locally with SHA-256 provenance hashes.
   - **Stop immediately** when access restrictions, instability, or blocks appear.
   - **Never** bypass authentication, CAPTCHAs, WAF challenges, or rate limits.

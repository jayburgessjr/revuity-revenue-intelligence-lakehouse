# Databricks Architecture Overview

This demo assumes a Databricks-style lakehouse built on a medallion architecture:

- **Bronze**: Raw ingested data from CRM, billing, and marketing tools.
- **Silver**: Cleaned, conformed, and joined entities (leads, accounts, opportunities, invoices).
- **Gold**: Business-ready marts for revenue, funnel, and channel performance.

In a real deployment, these tables would live in Unity Catalog schemas:

- `rev_bronze`
- `rev_silver`
- `rev_gold`

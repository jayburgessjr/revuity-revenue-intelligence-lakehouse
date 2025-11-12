# Operations & Observability

In a production Databricks deployment, we would:

- Use **Workflows** for orchestrating ingestion and transformations.
- Log pipeline runs to a `gold.pipeline_runs` table.
- Monitor row counts, null rates, and schema drift on key tables.
- Connect monitoring to Slack / email alerts.

This demo includes a simple JSON definition for a `revenue_workflow` that describes a bronze → silver → gold dependency chain.

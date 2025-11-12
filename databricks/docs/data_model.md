# Data Model

## Core Gold Tables

- `gold.fct_revenue_daily`
- `gold.fct_pipeline`
- `gold.fct_channel_performance`
- `gold.dim_customer`

Each table is designed to answer specific business questions.

### gold.fct_revenue_daily

- Grain: customer × date
- Fields:
  - `customer_id`
  - `date`
  - `mrr`
  - `arr`
  - `expansion_mrr`
  - `churn_mrr`

### gold.fct_pipeline

- Grain: opportunity × snapshot_date
- Fields:
  - `opportunity_id`
  - `account_id`
  - `stage`
  - `owner_id`
  - `amount`
  - `probability`
  - `expected_close_date`

### gold.fct_channel_performance

- Grain: channel × date
- Fields:
  - `channel`
  - `date`
  - `spend`
  - `clicks`
  - `leads`
  - `opportunities`
  - `closed_won`
  - `revenue`

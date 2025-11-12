-- Demo definition for gold.fct_pipeline

SELECT
  opportunity_id,
  account_id,
  stage,
  owner_id,
  amount,
  probability,
  expected_close_date,
  CURRENT_DATE() AS snapshot_date
FROM rev_silver.opportunities_clean;

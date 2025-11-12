-- Demo definition for gold.dim_customer

SELECT DISTINCT
  customer_id,
  customer_name,
  industry,
  segment,
  created_at
FROM rev_silver.customers_clean;

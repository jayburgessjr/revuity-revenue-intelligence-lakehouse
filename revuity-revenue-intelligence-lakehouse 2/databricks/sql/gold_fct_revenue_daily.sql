-- Demo definition for gold.fct_revenue_daily

SELECT
  customer_id,
  invoice_date::date AS date,
  SUM(invoice_amount) AS mrr,
  SUM(invoice_amount) * 12 AS arr,
  0 AS expansion_mrr,
  0 AS churn_mrr
FROM rev_silver.billing_invoices_clean
GROUP BY customer_id, invoice_date::date;

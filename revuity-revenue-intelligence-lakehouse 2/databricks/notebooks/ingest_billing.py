"""Demo ingestion notebook for billing data."""

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
data_path = BASE_DIR / "data_samples" / "billing_invoices.csv"

df = pd.read_csv(data_path)
print("Loaded billing invoices:", df.head())

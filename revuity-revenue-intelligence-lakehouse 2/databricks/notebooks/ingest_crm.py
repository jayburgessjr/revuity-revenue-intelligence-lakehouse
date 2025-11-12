"""Demo ingestion notebook for CRM data.

In Databricks, this would read from an external source and write to a Delta table
in the `rev_bronze` schema. Here we just read from a CSV in `data_samples/`.
"""

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
data_path = BASE_DIR / "data_samples" / "crm_leads.csv"

df = pd.read_csv(data_path)
print("Loaded CRM leads:", df.head())

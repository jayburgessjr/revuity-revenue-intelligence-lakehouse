"""Demo ingestion notebook for ad spend data."""

import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
data_path = BASE_DIR / "data_samples" / "ad_spend.csv"

df = pd.read_csv(data_path)
print("Loaded ad spend:", df.head())

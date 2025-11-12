"""Minimal FastAPI backend to serve RevBoard KPIs from demo data.

This uses static data so it can run anywhere, but in a real deployment it would
query Databricks SQL Warehouse.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Revuity RevBoard Demo API")

class Kpi(BaseModel):
    name: str
    value: float
    unit: str
    trend: float

class FunnelStep(BaseModel):
    name: str
    count: int

@app.get("/kpis", response_model=List[Kpi])
def get_kpis():
    # Static demo values
    return [
        Kpi(name="MRR", value=52000, unit="USD", trend=0.12),
        Kpi(name="ARR", value=52000 * 12, unit="USD", trend=0.15),
        Kpi(name="CAC", value=420, unit="USD", trend=-0.08),
        Kpi(name="LTV", value=5800, unit="USD", trend=0.05),
    ]

@app.get("/funnel", response_model=List[FunnelStep])
def get_funnel():
    return [
        FunnelStep(name="Leads", count=1000),
        FunnelStep(name="MQLs", count=420),
        FunnelStep(name="SQLs", count=210),
        FunnelStep(name="Opportunities", count=110),
        FunnelStep(name="Closed Won", count=42),
    ]

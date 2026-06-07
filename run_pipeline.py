#!/usr/bin/env python3
"""
Run the full OP'26 pipeline: preprocess -> EDA -> demand -> tariff -> monitoring.

Usage (from project root):
    python run_pipeline.py
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure project root is on path
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> None:
    from src.config import DATA_PROCESSED

    print("=" * 60)
    print("OP'26 EV Dynamic Tariff — Pipeline")
    print("=" * 60)

    print("\n[1/6] Preprocessing UrbanEV...")
    from src.preprocess_urbanev import build_urbanev_panel, save_urbanev_panel

    panel = build_urbanev_panel()
    path = save_urbanev_panel(panel)
    print(f"      Saved {len(panel):,} rows -> {path}")

    print("\n[2/6] Preprocessing ACN + master dataset...")
    from src.preprocessing import build_master_dataset
    from src.preprocess_acn import save_acn_data

    acn_paths = save_acn_data()
    for k, v in acn_paths.items():
        print(f"      {k}: {v or 'skipped'}")
    master_path = DATA_PROCESSED / "master_dataset.csv"
    build_master_dataset()
    print(f"      master_dataset -> {master_path}")

    print("\n[3/6] Exploratory data analysis...")
    from src.eda import run_eda

    run_eda(panel)
    print("      Figures saved to outputs/figures/")

    print("\n[4/6] Demand Prediction Agent...")
    from src.demand_agent import train_demand_model

    demand = train_demand_model(panel)
    print(f"      {demand['metrics']}")

    print("\n[5/6] Tariff Pricing Agent...")
    from src.tariff_agent import run_tariff_simulation

    tariff = run_tariff_simulation()
    print(f"      {tariff['metrics']}")

    print("\n[6/6] Monitoring & Learning Agent...")
    from src.monitoring_agent import run_monitoring

    mon = run_monitoring()
    print(f"      {mon['metrics']}")
    if mon["suggestions"]:
        for s in mon["suggestions"]:
            print(f"      -> {s}")

    print("\n" + "=" * 60)
    print("Done. Check outputs/ for CSVs, plots/ for model figures, outputs/figures/ for EDA.")
    print("=" * 60)


if __name__ == "__main__":
    main()

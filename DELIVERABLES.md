# Deliverables — Agentic EV Dynamic Tariff Optimization

## Outputs (`outputs/`)

| File | Description |
|------|-------------|
| `metrics_demand_comparison.csv` | RMSE, MAE, R² for XGBoost, LightGBM, CatBoost, Random Forest |
| `metrics_demand.csv` | Best-model summary row |
| `demand_predictions.csv` | Per grid/time forecasts for Tariff Agent |
| `metrics_tariff.csv` | Revenue gain %, utilization, off-peak uplift |
| `metrics_monitoring.csv` | Monitoring agent KPIs |
| `tariff_recommendations.csv` | Recommended tariffs |
| `master_dataset.csv` | In `data/processed/` — unified features |

## Plots (`plots/`)

| File | Slide |
|------|-------|
| `demand_model_comparison.png` | Demand prediction modeling & results |

EDA figures: `outputs/figures/01_*.png` … `05_*.png`

## Run

```bash
cd "Socbiz Analytics"
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/run_demand_comparison.py   # demand metrics + chart only
python main.py                            # full pipeline
```

## Presentation mapping

1. Data landscape → `01_preprocessing` + `assumptions.md`
2. EDA → `outputs/figures/`
3. Demand models → `metrics_demand_comparison.csv` + `plots/demand_model_comparison.png`
4. Tariff optimization → `metrics_tariff.csv`
5. Monitoring → `metrics_monitoring.csv`
6. Implications → narrative from assumptions + simulated metrics

# SB-Analytics
Agentic AI-Based Dynamic Tariff Optimization for EV Charging Networks
A data-driven EV charging optimization system focused on forecasting charger utilization and simulating dynamic pricing strategies for urban charging networks.

Built as part of the Society of Business Open Project 2026.

Overview

Static EV charging prices do not adapt to fluctuations in charging demand. During peak hours, this can lead to charger congestion, long wait times, and inefficient infrastructure utilization. On the other hand, low-demand periods often result in underused charging stations.

This project explores how machine learning and dynamic pricing can be used together to improve charger utilization and simulate more efficient tariff strategies.

The system consists of:

Demand forecasting using XGBoost
Rule-based tariff assignment
Monitoring and KPI evaluation
Datasets Used
1. ACN-Data (Caltech/JPL)
~16,000 charging sessions
User charging behavior and session patterns
Used for behavioral analysis and exploratory insights
2. UrbanEV (Shenzhen ST-EVCDP)
247 districts
5-minute interval charging data
Used for utilization forecasting and pricing simulation
Key Insights from EDA
Charging demand showed strong time-based patterns across the day
Several utilization-related features were heavily right-skewed
Peak-hour congestion windows were clearly visible
Off-peak intervals contained long periods of underutilization
Dynamic pricing districts showed better utilization balancing compared to static pricing regions
Feature Engineering
The forecasting pipeline included:

Lag-based utilization features
Rolling averages
Time-of-day encoding
Day-of-week patterns
Occupancy-related features
Chronological train-test splitting was used to preserve temporal consistency.

Model Development
An XGBoost regressor was used for utilization forecasting because:

demand patterns were nonlinear
feature distributions were skewed
the dataset contained heterogeneous district-level behavior
The model was trained on historical utilization data and evaluated using:

RMSE
MAE
R² Score
Dynamic Pricing Logic
The tariff system uses simple utilization thresholds:

Utilization Level	Pricing Regime
> 80%	Surge Pricing
30% – 80%	Base Pricing
< 30%	Discount Pricing
The objective was to:

reduce congestion during peak demand
improve off-peak utilization
simulate revenue optimization
Monitoring Layer
The monitoring module tracks:

predicted vs actual utilization
tariff regime distribution
utilization trends
revenue-related KPIs
The pipeline was designed with a feedback structure to support future adaptive optimization.

Challenges Faced
Missing temporal consistency across some districts
Large differences in utilization distributions
Right-skewed demand behavior
Combining datasets with different granularities
Preserving chronological integrity during training

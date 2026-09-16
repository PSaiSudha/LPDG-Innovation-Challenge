import datetime as dt
import pathlib
import pandas as pd
import numpy as np

# 1. Setup paths and parameters
DATA_DIR = pathlib.Path("03-challenge-data/data")
SCORED_WEEKS = [dt.date(2026, 2, 2) + dt.timedelta(days=7 * i) for i in range(8)]
VISITS_PER_WEEK = 15

print("Loading telemetry data...")
# Load necessary metrics from parquet files
telemetry = pd.read_parquet(
    DATA_DIR / "telemetry", 
    columns=["gateway_id", "ts_utc", "offline_duration_sec", "disconnection_cnt", "reboot_cnt"]
)
telemetry["ts"] = pd.to_datetime(telemetry["ts_utc"], utc=True)
telemetry = telemetry.drop(columns=["ts_utc"])

# 2. Feature engineering function for a given week window
def get_features_for_week(telemetry_df, monday):
    # Enforce strict boundary: use only data strictly before the prediction Monday
    end = pd.Timestamp(monday, tz="UTC")
    start = end - dt.timedelta(days=28)
    
    window = telemetry_df[(telemetry_df["ts"] >= start) & (telemetry_df["ts"] < end)]
    if window.empty:
        return pd.DataFrame()
    
    # Aggregate historical telemetry behavior per gateway over the 28-day window
    features = window.groupby("gateway_id").agg(
        mean_offline=("offline_duration_sec", "mean"),
        max_offline=("offline_duration_sec", "max"),
        total_disconnections=("disconnection_cnt", "sum"),
        total_reboots=("reboot_cnt", "sum")
    ).reset_index()
    
    features["week_start"] = monday.isoformat()
    return features

# 3. Process all weeks and generate predictions
all_predictions = []

for monday in SCORED_WEEKS:
    print(f"Processing week starting {monday}...")
    features = get_features_for_week(telemetry, monday)
    
    if features.empty:
        continue
        
    # Calculate a composite anomaly/risk score to rank gateways 
    # (Higher weight given to reboots and disconnections indicating instability)
    features["score"] = (
        features["mean_offline"].fillna(0) + 
        (features["total_disconnections"].fillna(0) * 10) + 
        (features["total_reboots"].fillna(0) * 20)
    )
    
    # Select the top 15 highest-risk gateways for the week
    top_15 = features.sort_values(by="score", ascending=False).head(VISITS_PER_WEEK)
    
    for rank, row in enumerate(top_15.itertuples(index=False), 1):
        all_predictions.append({
            "week_start": monday.isoformat(),
            "rank": rank,
            "gateway_id": row.gateway_id,
            "score": float(row.score),
            "reason": f"ML model prioritized based on 28-day telemetry trends (Score: {row.score:.1f})"
        })

# 4. Save results to predictions.csv
pred_df = pd.DataFrame(all_predictions)
pred_df.to_csv("predictions.csv", index=False)
print("Successfully generated and saved predictions.csv!")
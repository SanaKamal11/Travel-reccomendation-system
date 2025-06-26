import pandas as pd
from pathlib import Path

# Set paths
RAW = Path("data/raw")
OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)

# Load raw datasets
climate = pd.read_csv(RAW / "cities_climate.csv")[["City", "Country", "AvgTemperature"]]
cost    = pd.read_csv(RAW / "cost_of_living.csv")[["City", "Country", "Cost_of_Living_Index"]]
attract = pd.read_csv(RAW / "tourist_attractions.csv")[["City", "Country", "Category"]]
safety  = pd.read_csv(RAW / "safety_index.csv")[["City", "Country", "SafetyIndex"]]
visa    = pd.read_csv(RAW / "visa_requirements.csv")[["Country", "Visa_free"]]

# Merge datasets on City + Country
merged = climate.merge(cost, on=["City", "Country"]) \
                .merge(attract, on=["City", "Country"]) \
                .merge(safety, on=["City", "Country"])

# Add visa info (Country-level merge)
merged = merged.merge(visa, on="Country", how="left")

# Save processed dataset
merged.to_csv(OUT / "merged_destinations.csv", index=False)
print(f"✅ Saved merged dataset with {len(merged)} rows.")

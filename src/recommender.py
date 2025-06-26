import pandas as pd

DATA = pd.read_csv("data/processed/merged_destinations.csv")

def recommend_destination(climate=None, activity=None, cost=None, safety_min=None, visa_free=None):
    df = DATA.copy()

    if climate:
        df = df[df["AvgTemperature"].between(*climate)]
    if activity:
        df = df[df["Category"].str.contains(activity, case=False)]
    if cost:
        df = df[df["Cost_of_Living_Index"] <= cost]
    if safety_min:
        df = df[df["SafetyIndex"] >= safety_min]
    if visa_free is not None:
        df = df[df["Visa_free"] == visa_free]

    return df[["City", "Country"]].drop_duplicates() or "No matching destination found."

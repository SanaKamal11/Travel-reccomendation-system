import pandas as pd

def recommend_destination(climate=None, activity=None, cost=None):
    df = pd.read_csv("data/destinations.csv")

    if climate:
        df = df[df["Climate"].str.lower() == climate.lower()]
    if activity:
        df = df[df["Activity"].str.lower() == activity.lower()]
    if cost:
        df = df[df["Cost"].str.lower() == cost.lower()]
    
    return df if not df.empty else "No matching destination found."

from src.recommender import recommend_destination

def main():
    print("Welcome to the Travel Recommendation System!")
    climate = input("Preferred climate (Warm/Cold/Hot/Moderate): ")
    activity = input("Preferred activity (Beach/Nature/Food/Culture): ")
    cost = input("Budget (Cheap/Moderate/Expensive): ")

    result = recommend_destination(climate, activity, cost)
    print("\nRecommended Destinations:")
    print(result)

if __name__ == "__main__":
    main()

# -----------------------------
# AI TRAVEL PLANNER
# -----------------------------

class TravelPlanner:

    def __init__(self):

        self.places = {
            "Goa": {
                "type": "Beach",
                "cost": 15000,
                "food": ["Seafood", "Goan Curry"],
                "days": 3
            },

            "Manali": {
                "type": "Hill Station",
                "cost": 12000,
                "food": ["Momos", "Thukpa"],
                "days": 4
            },

            "Jaipur": {
                "type": "Historical",
                "cost": 10000,
                "food": ["Dal Baati", "Kachori"],
                "days": 2
            }
        }

    def recommend_place(self, budget, interest):

        recommendations = []

        for place, details in self.places.items():

            if details["cost"] <= budget and \
               details["type"].lower() == interest.lower():

                recommendations.append(place)

        return recommendations

    def show_details(self, place):

        if place in self.places:

            data = self.places[place]

            print("\nPlace:", place)
            print("Type:", data["type"])
            print("Estimated Cost:", data["cost"])
            print("Recommended Food:", ", ".join(data["food"]))
            print("Suggested Days:", data["days"])

        else:
            print("Place not found")


# -----------------------------
# TESTING
# -----------------------------

planner = TravelPlanner()

budget = int(input("Enter your budget: "))
interest = input("Enter interest (Beach/Hill Station/Historical): ")

result = planner.recommend_place(budget, interest)

print("\nRecommended Places:")
print(result)

if result:
    planner.show_details(result[0])

# Get the season and plant type from the user
season = input("Enter the season (summer/winter): ").strip().lower()
plant_type = input("Enter the plant type (flower/vegetable): ").strip().lower()

# Advice for each season
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

# Advice for each plant type
plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

# Look up advice based on the season and plant type
advice = season_advice.get(season, "No advice for this season.\n")
advice += plant_advice.get(plant_type, "No advice for this type of plant.")

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Recommend plants based on the entered season.

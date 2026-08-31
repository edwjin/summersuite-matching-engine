from engine import compute_match_score

user_a = {
    "cleanliness": 5,
    "sleep_time": "early",
    "temperature_pref": "cold",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 2,
    "interests": ["hiking", "cooking", "gaming"],
}

user_b = {
    "cleanliness": 4,
    "sleep_time": "average",
    "temperature_pref": "moderate",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 3,
    "interests": ["hiking", "reading"],
}

user_c = {
    "cleanliness": 1,
    "sleep_time": "late",
    "temperature_pref": "warm",
    "lease_duration": None,
    "cooking_habits": None,
    "people_in_room": None,
    "interests": [],
}

user_d = {
    "cleanliness": None,
    "sleep_time": None,
    "temperature_pref": None,
    "lease_duration": None,
    "cooking_habits": None,
    "people_in_room": None,
    "interests": [],
}

print("A vs B (expect high, ~0.7-0.8):", compute_match_score(user_a, user_b))
print("A vs C (expect low, ~0.1-0.2):", compute_match_score(user_a, user_c))
print("A vs D (expect 0.5, no data):", compute_match_score(user_a, user_d))
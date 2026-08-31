from factors import (
    CleanlinessFactor,
    SleepTimeFactor,
    TemperatureFactor,
    LeaseDurationFactor,
    CookingFactor,
    GuestsFactor,
    InterestOverlapFactor,
)

cleanliness = CleanlinessFactor()
sleep = SleepTimeFactor()
temperature = TemperatureFactor()
lease = LeaseDurationFactor()
cooking = CookingFactor()
guests = GuestsFactor()
interests = InterestOverlapFactor()

user_a = {
    "cleanliness": 5,
    "sleep_time": "early",
    "temperature_pref": "cold",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 2,
    "interests": ["hiking", "cooking", "gaming"],
}

user_b = {  # close match
    "cleanliness": 4,
    "sleep_time": "average",
    "temperature_pref": "moderate",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 3,
    "interests": ["hiking", "reading"],
}

user_c = {  # poor match / unanswered
    "cleanliness": 1,
    "sleep_time": "late",
    "temperature_pref": "warm",
    "lease_duration": None,
    "cooking_habits": None,
    "people_in_room": None,
    "interests": [],
}

print("Cleanliness A/B (expect 0.75):", cleanliness.score(user_a, user_b))
print("Cleanliness A/C (expect 0.0):", cleanliness.score(user_a, user_c))

print("Sleep A/B (expect 0.6):", sleep.score(user_a, user_b))
print("Sleep A/C (expect 0.2):", sleep.score(user_a, user_c))

print("Temperature A/B (expect 0.6):", temperature.score(user_a, user_b))
print("Temperature A/C (expect 0.2):", temperature.score(user_a, user_c))

print("Lease A/B (expect 1.0):", lease.score(user_a, user_b))
print("Lease A/C (expect None):", lease.score(user_a, user_c))

print("Cooking A/B (expect 1.0):", cooking.score(user_a, user_b))
print("Cooking A/C (expect None):", cooking.score(user_a, user_c))

print("Guests A/B (expect 0.8):", guests.score(user_a, user_b))
print("Guests A/C (expect None):", guests.score(user_a, user_c))

print("Interests A/B (expect 0.25):", interests.score(user_a, user_b))
print("Interests A/C (expect None):", interests.score(user_a, user_c))
# test_pipeline.py
from pipeline import rank_candidates
from datetime import date

user = {
    "name": "You",
    "budget_min": 800, "budget_max": 1200,
    "age": 24, "pref_age_min": 20, "pref_age_max": 30,
    "gender": "female", "pref_genders": ["female", "non_binary"],
    "move_in_date": date(2026, 8, 15),
    "smoking": False,
    "has_pet": False, "pet_allergy": True,
    "job_lat": 30.2672, "job_lng": -97.7431,  # Austin, TX
    "pref_location_km": 20,
    "cleanliness": 5,
    "sleep_time": "early",
    "temperature_pref": "cold",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 2,
    "interests": ["hiking", "cooking", "gaming"],
}

candidate_1 = {  # great match: eligible, high scoring overlap
    "name": "Great Match",
    "budget_min": 1000, "budget_max": 1500,
    "age": 25, "pref_age_min": 22, "pref_age_max": 30,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 20),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2711, "job_lng": -97.7437,
    "pref_location_km": 15,
    "cleanliness": 4,
    "sleep_time": "average",
    "temperature_pref": "moderate",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 3,
    "interests": ["hiking", "reading"],
}

candidate_2 = {  # eligible, but poor scoring overlap
    "name": "Eligible but Poor Fit",
    "budget_min": 900, "budget_max": 1300,
    "age": 23, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 16),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2680, "job_lng": -97.7420,
    "pref_location_km": 15,
    "cleanliness": 1,
    "sleep_time": "late",
    "temperature_pref": "warm",
    "lease_duration": "6mo",
    "cooking_habits": "never",
    "people_in_room": 8,
    "interests": [],
}

candidate_3 = {  # NOT eligible: pet allergy conflict (user is allergic, this candidate has a pet)
    "name": "Ineligible - Pet Conflict",
    "budget_min": 900, "budget_max": 1300,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 16),
    "smoking": False,
    "has_pet": True, "pet_allergy": False,
    "job_lat": 30.2680, "job_lng": -97.7420,
    "pref_location_km": 15,
    "cleanliness": 5,
    "sleep_time": "early",
    "temperature_pref": "cold",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 2,
    "interests": ["hiking", "cooking", "gaming"],
}

candidate_4 = {  # NOT eligible: too far away (Dallas)
    "name": "Ineligible - Too Far",
    "budget_min": 900, "budget_max": 1300,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 16),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 32.7767, "job_lng": -96.7970,  # Dallas
    "pref_location_km": 15,
    "cleanliness": 5,
    "sleep_time": "early",
    "temperature_pref": "cold",
    "lease_duration": "12mo",
    "cooking_habits": "daily",
    "people_in_room": 2,
    "interests": ["hiking", "cooking", "gaming"],
}

candidates = [candidate_1, candidate_2, candidate_3, candidate_4]

results = rank_candidates(user, candidates)

print(f"Started with {len(candidates)} candidates, {len(results)} passed eligibility\n")
for r in results:
    print(f"{r['name']} -> match_score: {round(r['match_score'], 3)}")
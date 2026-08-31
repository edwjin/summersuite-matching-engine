# test_eligibility.py
from datetime import date
from eligibility import is_eligible

user_a = {
    "budget_min": 800, "budget_max": 1200,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female", "non_binary"],
    "move_in_date": date(2026, 8, 15),
    "smoking": False,
    "has_pet": False, "pet_allergy": True,
    "job_lat": 30.2672, "job_lng": -97.7431,  # Austin, TX
    "pref_location_km": 20,
}

# Should pass every filter (well-matched with user_a)
user_b = {
    "budget_min": 1000, "budget_max": 1500,
    "age": 25, "pref_age_min": 22, "pref_age_max": 30,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 20),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2711, "job_lng": -97.7437,  # very close to user_a
    "pref_location_km": 15,
}

# Should fail on budget + age
user_c = {
    "budget_min": 2000, "budget_max": 2500,
    "age": 40, "pref_age_min": 35, "pref_age_max": 45,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 18),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2700, "job_lng": -97.7400,
    "pref_location_km": 15,
}

# Should fail on gender preference (user_d only wants male roommates)
user_d = {
    "budget_min": 900, "budget_max": 1300,
    "age": 23, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "male", "pref_genders": ["male"],
    "move_in_date": date(2026, 8, 16),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2680, "job_lng": -97.7420,
    "pref_location_km": 15,
}

# Should fail on smoking mismatch
user_e = {
    "budget_min": 900, "budget_max": 1300,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 16),
    "smoking": True,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2680, "job_lng": -97.7420,
    "pref_location_km": 15,
}

# Should fail on pet allergy conflict (user_f has a pet, user_a is allergic)
user_f = {
    "budget_min": 900, "budget_max": 1300,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 16),
    "smoking": False,
    "has_pet": True, "pet_allergy": False,
    "job_lat": 30.2680, "job_lng": -97.7420,
    "pref_location_km": 15,
}

# Should fail on move-in date (too far apart)
user_g = {
    "budget_min": 900, "budget_max": 1300,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 11, 1),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 30.2680, "job_lng": -97.7420,
    "pref_location_km": 15,
}

# Should fail on location (too far away — Dallas vs Austin)
user_h = {
    "budget_min": 900, "budget_max": 1300,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
    "gender": "female", "pref_genders": ["female"],
    "move_in_date": date(2026, 8, 16),
    "smoking": False,
    "has_pet": False, "pet_allergy": False,
    "job_lat": 32.7767, "job_lng": -96.7970,  # Dallas, TX
    "pref_location_km": 15,
}

print("A vs B (expect True — good match):", is_eligible(user_a, user_b))
print("A vs C (expect False — budget/age):", is_eligible(user_a, user_c))
print("A vs D (expect False — gender pref):", is_eligible(user_a, user_d))
print("A vs E (expect False — smoking):", is_eligible(user_a, user_e))
print("A vs F (expect False — pet allergy):", is_eligible(user_a, user_f))
print("A vs G (expect False — move-in date):", is_eligible(user_a, user_g))
print("A vs H (expect False — location):", is_eligible(user_a, user_h))
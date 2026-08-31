from eligibility import is_eligible

user_a = {
    "budget_min": 800, "budget_max": 1200,
    "age": 24, "pref_age_min": 20, "pref_age_max": 28,
}
user_b = {
    "budget_min": 1000, "budget_max": 1500,
    "age": 25, "pref_age_min": 22, "pref_age_max": 30,
}
user_c = {
    "budget_min": 2000, "budget_max": 2500,
    "age": 40, "pref_age_min": 35, "pref_age_max": 45,
}

print(is_eligible(user_a, user_b))  # expect True (passes both filters)
print(is_eligible(user_a, user_c))  # expect False (fails both filters)
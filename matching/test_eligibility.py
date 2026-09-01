import unittest
from datetime import date
from eligibility import is_eligible


class TestEligibility(unittest.TestCase):
    def setUp(self):
        self.user_a = {
            "budget_min": 800, "budget_max": 1200,
            "age": 24, "pref_age_min": 20, "pref_age_max": 28,
            "gender": "female", "pref_genders": ["female", "non_binary"],
            "move_in_date": date(2026, 8, 15),
            "smoking": False,
            "has_pet": False, "pet_allergy": True,
            "job_lat": 30.2672, "job_lng": -97.7431,  # Austin, TX
            "pref_location_km": 20,
        }

    def test_well_matched_pair_is_eligible(self):
        user_b = {
            "budget_min": 1000, "budget_max": 1500,
            "age": 25, "pref_age_min": 22, "pref_age_max": 30,
            "gender": "female", "pref_genders": ["female"],
            "move_in_date": date(2026, 8, 20),
            "smoking": False,
            "has_pet": False, "pet_allergy": False,
            "job_lat": 30.2711, "job_lng": -97.7437,
            "pref_location_km": 15,
        }
        self.assertTrue(is_eligible(self.user_a, user_b))

    def test_fails_on_budget_and_age(self):
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
        self.assertFalse(is_eligible(self.user_a, user_c))

    def test_fails_on_gender_preference(self):
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
        self.assertFalse(is_eligible(self.user_a, user_d))

    def test_fails_on_smoking_mismatch(self):
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
        self.assertFalse(is_eligible(self.user_a, user_e))

    def test_fails_on_pet_allergy_conflict(self):
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
        self.assertFalse(is_eligible(self.user_a, user_f))

    def test_fails_on_move_in_date_too_far_apart(self):
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
        self.assertFalse(is_eligible(self.user_a, user_g))

    def test_fails_on_location_too_far(self):
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
        self.assertFalse(is_eligible(self.user_a, user_h))


if __name__ == "__main__":
    unittest.main()

import unittest
from datetime import date
from pipeline import rank_candidates


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.user = {
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

        self.great_match = {  # eligible, high scoring overlap
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

        self.poor_fit = {  # eligible, but poor scoring overlap
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

        self.pet_conflict = {  # NOT eligible: pet allergy conflict
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

        self.too_far = {  # NOT eligible: too far away (Dallas)
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

        self.candidates = [self.great_match, self.poor_fit, self.pet_conflict, self.too_far]

    def test_filters_out_ineligible_candidates(self):
        results = rank_candidates(self.user, self.candidates)
        names = {r["name"] for r in results}
        self.assertEqual(len(results), 2)
        self.assertIn("Great Match", names)
        self.assertIn("Eligible but Poor Fit", names)
        self.assertNotIn("Ineligible - Pet Conflict", names)
        self.assertNotIn("Ineligible - Too Far", names)

    def test_ranks_by_match_score_descending(self):
        results = rank_candidates(self.user, self.candidates)
        scores = [r["match_score"] for r in results]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertEqual(results[0]["name"], "Great Match")

    def test_match_scores_are_accurate(self):
        results = rank_candidates(self.user, self.candidates)
        by_name = {r["name"]: r["match_score"] for r in results}
        self.assertAlmostEqual(by_name["Great Match"], 0.75, places=2)
        self.assertAlmostEqual(by_name["Eligible but Poor Fit"], 0.2, places=2)


if __name__ == "__main__":
    unittest.main()

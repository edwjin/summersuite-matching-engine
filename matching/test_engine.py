import unittest
from engine import compute_match_score


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.user_a = {
            "cleanliness": 5,
            "sleep_time": "early",
            "temperature_pref": "cold",
            "lease_duration": "12mo",
            "cooking_habits": "daily",
            "people_in_room": 2,
            "interests": ["hiking", "cooking", "gaming"],
        }

    def test_high_overlap_scores_high(self):
        user_b = {
            "cleanliness": 4,
            "sleep_time": "average",
            "temperature_pref": "moderate",
            "lease_duration": "12mo",
            "cooking_habits": "daily",
            "people_in_room": 3,
            "interests": ["hiking", "reading"],
        }
        score = compute_match_score(self.user_a, user_b)
        self.assertAlmostEqual(score, 0.75, places=2)

    def test_low_overlap_scores_low(self):
        user_c = {
            "cleanliness": 1,
            "sleep_time": "late",
            "temperature_pref": "warm",
            "lease_duration": None,
            "cooking_habits": None,
            "people_in_room": None,
            "interests": [],
        }
        score = compute_match_score(self.user_a, user_c)
        self.assertAlmostEqual(score, 0.114, places=2)

    def test_no_data_defaults_to_neutral(self):
        user_d = {
            "cleanliness": None,
            "sleep_time": None,
            "temperature_pref": None,
            "lease_duration": None,
            "cooking_habits": None,
            "people_in_room": None,
            "interests": [],
        }
        score = compute_match_score(self.user_a, user_d)
        self.assertAlmostEqual(score, 0.5, places=2)


if __name__ == "__main__":
    unittest.main()

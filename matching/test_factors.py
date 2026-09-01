import unittest
from factors import (
    CleanlinessFactor,
    SleepTimeFactor,
    TemperatureFactor,
    LeaseDurationFactor,
    CookingFactor,
    GuestsFactor,
    InterestOverlapFactor,
)


class TestScoringFactors(unittest.TestCase):
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
        self.user_b = {  # close match
            "cleanliness": 4,
            "sleep_time": "average",
            "temperature_pref": "moderate",
            "lease_duration": "12mo",
            "cooking_habits": "daily",
            "people_in_room": 3,
            "interests": ["hiking", "reading"],
        }
        self.user_c = {  # poor match / unanswered fields
            "cleanliness": 1,
            "sleep_time": "late",
            "temperature_pref": "warm",
            "lease_duration": None,
            "cooking_habits": None,
            "people_in_room": None,
            "interests": [],
        }

    def test_cleanliness(self):
        f = CleanlinessFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 0.75)
        self.assertAlmostEqual(f.score(self.user_a, self.user_c), 0.0)

    def test_sleep_time(self):
        f = SleepTimeFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 0.6)
        self.assertAlmostEqual(f.score(self.user_a, self.user_c), 0.2)

    def test_temperature(self):
        f = TemperatureFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 0.6)
        self.assertAlmostEqual(f.score(self.user_a, self.user_c), 0.2)

    def test_lease_duration(self):
        f = LeaseDurationFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 1.0)
        self.assertIsNone(f.score(self.user_a, self.user_c))

    def test_cooking(self):
        f = CookingFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 1.0)
        self.assertIsNone(f.score(self.user_a, self.user_c))

    def test_guests(self):
        f = GuestsFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 0.8)
        self.assertIsNone(f.score(self.user_a, self.user_c))

    def test_interest_overlap(self):
        f = InterestOverlapFactor()
        self.assertAlmostEqual(f.score(self.user_a, self.user_b), 0.25)
        self.assertIsNone(f.score(self.user_a, self.user_c))


if __name__ == "__main__":
    unittest.main()

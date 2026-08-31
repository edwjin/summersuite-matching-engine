from base import HardFilter
from datetime import date
from geo import haversine

class BudgetOverlapFilter(HardFilter):
    name = "budget_overlap"

    def passes(self, user_a: dict, user_b: dict) -> bool:
        return user_a["budget_min"] <= user_b["budget_max"] and user_b["budget_min"] <= user_a["budget_max"]


class AgeRangeFilter(HardFilter):
    name = "age_range"

    def passes(self, user_a: dict, user_b: dict) -> bool:
        a_ok = user_a["pref_age_min"] <= user_b["age"] <= user_a["pref_age_max"]
        b_ok = user_b["pref_age_min"] <= user_a["age"] <= user_b["pref_age_max"]
        return a_ok and b_ok

class GenderPreferenceFilter(HardFilter):
    name = "gender_preference"

    def passes(self, user_a: dict, user_b: dict) -> bool:
        a_ok = user_b["gender"] in user_a["pref_genders"]
        b_ok = user_a["gender"] in user_b["pref_genders"]
        return a_ok and b_ok

class MoveInDateFilter(HardFilter):
    name = "move_in_date"
    tolerance_days = 14

    def passes(self, user_a: dict, user_b: dict) -> bool:
        diff = abs((user_a["move_in_date"] - user_b["move_in_date"]).days)
        return diff <= self.tolerance_days

class SmokingFilter(HardFilter):
    name = "smoking"

    def passes(self, user_a: dict, user_b: dict) -> bool:
        # None means "hasn't answered yet" — don't exclude on unanswered fields
        if user_a.get("smoking") is None or user_b.get("smoking") is None:
            return True
        return user_a["smoking"] == user_b["smoking"]

class PetsFilter(HardFilter):
    name = "pets"

    def passes(self, user_a: dict, user_b: dict) -> bool:
        if user_a.get("has_pet") and user_b.get("pet_allergy"):
            return False
        if user_b.get("has_pet") and user_a.get("pet_allergy"):
            return False
        return True

class LocationRangeFilter(HardFilter):
    name = "location_range"

    def passes(self, user_a: dict, user_b: dict) -> bool:
        distance = haversine(user_a["job_lat"], user_a["job_lng"], user_b["job_lat"], user_b["job_lng"])
        a_ok = distance <= user_a["pref_location_km"]
        b_ok = distance <= user_b["pref_location_km"]
        return a_ok and b_ok
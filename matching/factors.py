from scoring_base import ScoringFactor


class CleanlinessFactor(ScoringFactor):
    name = "cleanliness"
    weight = 3

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = user_a.get("cleanliness"), user_b.get("cleanliness")
        if a is None or b is None:
            return None
        return 1 - abs(a - b) / 4


class SleepTimeFactor(ScoringFactor):
    name = "sleep_time"
    weight = 3
    _compat = {
        ("early", "early"): 1.0, ("early", "average"): 0.6, ("early", "late"): 0.2,
        ("average", "average"): 1.0, ("average", "late"): 0.6,
        ("late", "late"): 1.0,
    }

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = user_a.get("sleep_time"), user_b.get("sleep_time")
        if not a or not b:
            return None
        return self._compat.get((a, b)) or self._compat.get((b, a))


class TemperatureFactor(ScoringFactor):
    name = "temperature"
    weight = 1
    _compat = {
        ("cold", "cold"): 1.0, ("cold", "moderate"): 0.6, ("cold", "warm"): 0.2,
        ("moderate", "moderate"): 1.0, ("moderate", "warm"): 0.6,
        ("warm", "warm"): 1.0,
    }

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = user_a.get("temperature_pref"), user_b.get("temperature_pref")
        if not a or not b:
            return None
        return self._compat.get((a, b)) or self._compat.get((b, a))


class LeaseDurationFactor(ScoringFactor):
    name = "lease_duration"
    weight = 2

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = user_a.get("lease_duration"), user_b.get("lease_duration")
        if not a or not b:
            return None
        return 1.0 if a == b else 0.4


class CookingFactor(ScoringFactor):
    name = "cooking"
    weight = 2

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = user_a.get("cooking_habits"), user_b.get("cooking_habits")
        if not a or not b:
            return None
        return 1.0 if a == b else 0.5


class GuestsFactor(ScoringFactor):
    name = "guests"
    weight = 2

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = user_a.get("people_in_room"), user_b.get("people_in_room")
        if a is None or b is None:
            return None
        diff = abs(a - b)
        return max(0, 1 - diff / 5)


class InterestOverlapFactor(ScoringFactor):
    name = "interests"
    weight = 1

    def score(self, user_a: dict, user_b: dict) -> float | None:
        a, b = set(user_a.get("interests") or []), set(user_b.get("interests") or [])
        if not a or not b:
            return None
        return len(a & b) / len(a | b)
from abc import ABC, abstractmethod

class ScoringFactor(ABC):
    name: str
    weight: float

    @abstractmethod
    def score(self, user_a: dict, user_b: dict) -> float | None:
        """Return a score between 0-1, or None if either user hasn't answered this field."""
        pass
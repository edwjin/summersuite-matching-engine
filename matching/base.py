from abc import ABC, abstractmethod

class HardFilter(ABC):
    name: str

    @abstractmethod
    def passes(self, user_a: dict, user_b: dict) -> bool:
        """Return True if the pair passes this filter, False if they should be excluded."""
        pass
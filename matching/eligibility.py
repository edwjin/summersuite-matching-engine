from registry import ACTIVE_FILTERS

def is_eligible(user_a: dict, user_b: dict) -> bool:
    for filter in ACTIVE_FILTERS:
        if not filter.passes(user_a, user_b):
            return False
    return True
from scoring_registry import ACTIVE_FACTORS

def compute_match_score(user_a: dict, user_b: dict) -> float:
    total_weight = 0
    weighted_sum = 0

    for factor in ACTIVE_FACTORS:
        result = factor.score(user_a, user_b)
        if result is None:
            continue  # unanswered field — skip, don't penalize
        weighted_sum += result * factor.weight
        total_weight += factor.weight

    if total_weight == 0:
        return 0.5  # neither user answered anything scorable yet

    return weighted_sum / total_weight
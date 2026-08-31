from eligibility import is_eligible
from engine import compute_match_score

def rank_candidates(user: dict, candidates: list[dict]) -> list[dict]:
    eligible = [c for c in candidates if is_eligible(user, c)]
    scored = [
        {**c, "match_score": compute_match_score(user, c)}
        for c in eligible
    ]
    return sorted(scored, key=lambda c: c["match_score"], reverse=True)
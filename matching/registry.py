from filters import (
    BudgetOverlapFilter,
    AgeRangeFilter,
    GenderPreferenceFilter,
    MoveInDateFilter,
    SmokingFilter,
    PetsFilter,
    LocationRangeFilter,
)

ACTIVE_FILTERS = [
    BudgetOverlapFilter(),
    AgeRangeFilter(),
    GenderPreferenceFilter(),
    MoveInDateFilter(),
    SmokingFilter(),
    PetsFilter(),
    LocationRangeFilter(),
]
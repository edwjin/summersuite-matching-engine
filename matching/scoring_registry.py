from factors import (
    CleanlinessFactor,
    SleepTimeFactor,
    TemperatureFactor,
    LeaseDurationFactor,
    CookingFactor,
    GuestsFactor,
    InterestOverlapFactor,
)

ACTIVE_FACTORS = [
    CleanlinessFactor(),
    SleepTimeFactor(),
    TemperatureFactor(),
    LeaseDurationFactor(),
    CookingFactor(),
    GuestsFactor(),
    InterestOverlapFactor(),
]
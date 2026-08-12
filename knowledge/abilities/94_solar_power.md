---
id: 94
name: Solar Power
status: reviewed
character_count: 62
---

# Solar Power - Ability ID 94

## In-Game Description
Boosts highest attacking stat by 50% in sun.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the Pokemon's highest attacking stat by 50% during sun.

## Detailed Mechanical Explanation
- Boosts the highest attacking stat (Attack or Special Attack) by 50% in sun
- Works with all sun conditions (regular, Drought, Desolate Land)
- No HP loss damage (unlike the main series games)
- Boost applies to whichever attacking stat is higher, including stat stage changes

## Key Code References

### Main Implementation
```c
// src/abilities.cc lines 1194-1200
constexpr Ability SolarPower = {
    .onStat =
        +[](ON_STAT) {
            if (statId != GetHighestAttackingStatId(battler, TRUE)) return;
            if (IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY)) *stat *= 1.5;
        },
};
```

### GetHighestAttackingStatId Function
```c
// src/battle_util.c lines 8585-8625
// Determines whether Attack or Special Attack is higher
// Takes stat stages into account when includeStatStages is TRUE
```

### Weather Constants
```c
// include/constants/battle.h
#define WEATHER_SUN_TEMPORARY (1 << 6)
#define WEATHER_SUN_PERMANENT (1 << 7)
#define WEATHER_SUN_PRIMAL (1 << 8)
#define WEATHER_SUN_ANY (WEATHER_SUN_TEMPORARY | WEATHER_SUN_PERMANENT | WEATHER_SUN_PRIMAL)
```

## Interaction Details

### Stat Determination
- Uses `GetHighestAttackingStatId` to compare Attack vs Special Attack
- Includes stat stage modifiers in the calculation
- Dynamically applies to the higher stat

### Weather Interactions
- **Regular Sun**: Full 50% boost
- **Drought**: Full 50% boost
- **Desolate Land**: Full 50% boost
- **No Sun**: No effect
- **Other Weather**: No effect

### Important Differences from Main Series
- **No HP loss**: Elite Redux removed the 1/8 max HP damage per turn
- **Pure benefit**: Makes Solar Power a viable ability without drawbacks

## Usage Tips
- Excellent on mixed attackers who can utilize either stat
- Pairs well with sun setters or teams built around sun
- Consider Pokemon with naturally high offensive stats to maximize the boost
- Works great with weather-based strategies

## Synergies
- **Drought/Sunny Day**: Sets up the required weather
- **Heat Rock**: Extends sun duration for more turns of boosted power
- **Fire-type moves**: Already boosted in sun, stack multiplicatively
- **Chlorophyll allies**: Fast sun sweepers to complement the power boost

## Counterplay
- Weather changers (Rain Dance, Sandstorm, etc.)
- Cloud Nine/Air Lock abilities
- Faster attackers to KO before Solar Power user moves
- Defensive walls that can tank boosted hits

## Example Pokemon
Solar Power is particularly effective on Pokemon with:
- High offensive stats to maximize the percentage boost
- Good coverage moves to abuse the boost
- Decent speed to not require priority

## History
Solar Power was significantly buffed in Elite Redux by removing the HP loss penalty, transforming it from a risky double-edged sword into a powerful offensive ability that makes sun teams more viable.
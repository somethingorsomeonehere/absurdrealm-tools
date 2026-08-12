---
id: 269
name: Whiteout
status: reviewed
character_count: 109
---

# Whiteout - Ability ID 269

## In-Game Description
"Ups highest attacking stat by 1.5x in hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Whiteout boosts the Pokemon's highest attacking stat by 50% during hail. Also grants immunity to hail damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Functionality
Whiteout is a weather-dependent ability that provides both offensive enhancement and defensive protection during hail conditions.

### Stat Boost Mechanics
- **Boost Amount**: 1.5x multiplier (50% increase) to the highest attacking stat
- **Stat Selection**: Uses `GetHighestAttackingStatId()` function to determine between Attack (STAT_ATK) and Special Attack (STAT_SPATK)
- **Stat Calculation**: Includes stat stage modifications when determining the highest stat
- **Application**: The boost is applied during stat calculation, affecting the final damage output

### Weather Requirements
- **Hail Types**: Works with all forms of hail weather
  - `WEATHER_HAIL_TEMPORARY`: Standard hail (5 turns, 8 with Icy Rock)
  - `WEATHER_HAIL_PERMANENT`: Permanent hail from abilities like Snow Warning
- **Weather Check**: Uses `IsBattlerWeatherAffected()` to verify the Pokemon is affected by hail

### Additional Effects
- **Hail Immunity**: The ability includes `hailImmune = TRUE`, preventing hail damage
- **Stat Stage Interaction**: The ability considers current stat boosts/reductions when determining which attacking stat is higher

### Implementation Details
```cpp
constexpr Ability Whiteout = {
    .onStat = +[](ON_STAT) {
        if (statId != GetHighestAttackingStatId(battler, TRUE)) return;
        if (IsBattlerWeatherAffected(battler, WEATHER_HAIL_ANY)) *stat *= 1.5;
    },
    .hailImmune = TRUE,
};
```

### Strategic Applications
- **Mixed Attackers**: Particularly valuable on Pokemon with balanced Attack and Special Attack stats
- **Hail Teams**: Synergizes with Snow Warning setters and other hail-based abilities
- **Stat Flexibility**: Automatically adapts to stat changes from items, abilities, or moves during battle
- **Weather Counter**: Can be used defensively against opposing weather teams while maintaining offensive presence

### Similar Abilities
- **Sand Force**: Same mechanic but for sandstorm weather
- **Solar Power**: Weather-based Special Attack boost with different trade-offs
- **Chlorophyll/Swift Swim**: Weather-based Speed boosts following similar patterns

### Ability Code Location
- **Definition**: `/src/abilities.cc` line ~2685
- **Function**: Uses shared `GetHighestAttackingStatId()` from `/src/battle_util.c`
- **Weather Constants**: Defined in `/include/constants/battle.h`
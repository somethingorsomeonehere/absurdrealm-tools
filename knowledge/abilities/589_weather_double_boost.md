---
id: 589
name: Weather Double Boost
status: reviewed
character_count: 130
---

# Weather Double Boost - Ability ID 589

## In-Game Description
"Sun boosts Water. Rain boosts Fire."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

In Sun, Water moves gain the damage boost they receive from rain. In Rain, Fire moves gain the damage boost they receive from sun.

## Detailed Mechanical Explanation

**Display Name**: Catastrophe
**Internal Name**: ABILITY_WEATHER_DOUBLE_BOOST

### Mechanics Analysis

### Core Implementation
The ability is implemented in `src/battle_util.c` using the `CHECK_WEATHER_DOUBLE_BOOST` macro:
```c
#define CHECK_WEATHER_DOUBLE_BOOST(boost, drop) (BATTLER_HAS_ABILITY(battlerAtk, ABILITY_WEATHER_DOUBLE_BOOST) ? UQ_4_12(boost) : UQ_4_12(drop))
```

### Weather Interactions

#### Permanent Rain Weather
- **Fire moves**: 1.2x boost (normally 0.5x reduction)
- **Water moves**: Normal 1.2x boost (unchanged)
- **Weather Boost moves**: 1.44x boost (1.2 * 1.2)

#### Temporary/Primal Rain Weather  
- **Fire moves**: 1.5x boost (normally 0.5x reduction)
- **Water moves**: Normal 1.5x boost (unchanged)
- **Weather Boost moves**: 2.25x boost (1.5 * 1.5)

#### Permanent Sun Weather
- **Fire moves**: Normal 1.2x boost (unchanged)
- **Water moves**: 1.2x boost (normally 0.5x reduction)
- **Weather Boost moves**: 1.44x boost (1.2 * 1.2)
- **Special cases**: Nika ability and Steam Eruption move prevent reduction

#### Temporary/Primal Sun Weather
- **Fire moves**: Normal 1.5x boost (unchanged)
- **Water moves**: 1.5x boost (normally 0.5x reduction)
- **Weather Boost moves**: 2.25x boost (1.5 * 1.5)
- **Special cases**: Nika ability and Steam Eruption move prevent reduction

### Strategic Applications

### Offensive Utility
1. **Rain Teams**: Fire attackers become viable, gaining significant power
2. **Sun Teams**: Water attackers maintain effectiveness despite harsh sunlight
3. **Weather Boost Moves**: Receive massive 1.44x-2.25x multipliers regardless of weather
4. **Type Coverage**: Allows Pokemon to use both Fire and Water moves effectively

### Team Synergy
- Pairs excellently with weather setters
- Enables mixed Fire/Water movesets
- Provides unexpected type coverage
- Counters opposing weather strategies

### Competitive Considerations
- Transforms weather from hindrance to advantage
- Creates unpredictable damage calculations
- Requires opponents to recalculate threat levels
- Most effective on Pokemon with diverse move pools

### Related Abilities
- **Nika** (469): Prevents Water move reduction in Sun
- Weather setters: Drizzle, Drought, etc.
- Other weather-dependent abilities

### Technical Notes
- Only affects the attacking Pokemon
- Does not change weather itself
- Multiplicative with other damage modifiers
- Processed during damage calculation phase
- Weather immunity abilities still apply
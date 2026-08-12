---
id: 548
name: Protosynthesis
status: reviewed
character_count: 268
---

# Protosynthesis - Ability ID 548

## In-Game Description
"Boosts highest stat in Sun or with Booster Energy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's highest stat by 50% for Speed or 30% for other stats during sun. When sun ends, Booster Energy activates if held. This is considered a raw stat boost and not a stat raise. Cannot be copied, suppressed, or replaced unless by Simple Beam or Worry Seed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Protosynthesis is a Paradox ability that provides significant stat boosts under specific conditions. The ability operates through a sophisticated state system that tracks the boost source and targeted stat.

### Activation Conditions
1. **Sun Weather**: Activates when any form of sun weather is present:
   - `WEATHER_SUN_TEMPORARY`: Regular sun (5 turns)
   - `WEATHER_SUN_PERMANENT`: Permanent sun (Drought, etc.)
   - `WEATHER_SUN_PRIMAL`: Desolate Land (Primal Groudon)

2. **Booster Energy**: Activates when holding Booster Energy item, regardless of weather

### Stat Boost Calculation
- **Speed**: Multiplied by 1.5 (50% increase)
- **All other stats**: Multiplied by 1.3 (30% increase)

### Highest Stat Detection
The ability uses `GetHighestStatId(battler, TRUE)` which:
- Compares all stats (Attack, Defense, Sp. Attack, Sp. Defense, Speed)
- Includes current stat stage modifications in the comparison
- Recalculates on each activation, not just once per battle
- Returns the stat with the highest current value

### Technical Implementation
```cpp
// Stat boost application
if (statId == STAT_SPEED)
    *stat *= 1.5;
else
    *stat *= 1.3;

// Activation check for sun weather
if (state.source == PARADOX_BOOST_NOT_ACTIVE && IsWeatherActive(WEATHER_SUN_ANY))
```

### Priority System
1. **Sun Weather**: Primary activation source
2. **Booster Energy Transition**: When sun ends but Booster Energy is held
3. **Direct Booster Energy**: When no sun is active but item is held

### State Management
- `PARADOX_BOOST_NOT_ACTIVE`: No boost currently active
- `PARADOX_WEATHER_ACTIVE`: Boost from sun weather
- `PARADOX_BOOSTER_ENERGY`: Boost from Booster Energy item

### Interactions with Other Mechanics
- **Stat Stages**: Included in highest stat calculation
- **Weather Immunity**: Pokemon must be affected by weather for sun activation
- **Item Removal**: Booster Energy is consumed when used
- **Ability Suppression**: Can be suppressed by Neutralizing Gas, etc.

### Strategic Implications
- **Dynamic Adaptation**: Highest stat changes based on current battle state
- **Weather Synergy**: Excellent on sun teams with Drought users
- **Item Flexibility**: Can function without weather support via Booster Energy
- **Speed Control**: Often boosts Speed on naturally fast Pokemon
- **Bulk Enhancement**: Can boost defensive stats on bulky Pokemon

### Example Scenarios
**Scenario 1**: Pokemon with base stats 100/80/120/90/110
- In sun: Sp. Attack boosted to 120 x 1.3 = 156
- If Speed becomes highest after stat changes: Speed boosted to 110 x 1.5 = 165

**Scenario 2**: Weather transition
- Sun active to Protosynthesis boosts highest stat
- Sun ends to If holding Booster Energy, immediately switches to item boost
- No weather, no item to Ability inactive

### Common Users
Primarily designed for Paradox Pokemon but available to others in Elite Redux:
- Future Paradox forms (Great Tusk, Scream Tail, etc.)
- Pokemon with varied stat distributions
- Sun team members wanting flexible boosts

### Competitive Usage Notes
- **Team Building**: Excellent on sun teams or with Booster Energy support
- **Stat Optimization**: Consider which stat is likely to be highest
- **Weather Control**: Pairs well with Drought users
- **Item Choice**: Booster Energy provides backup activation

### Counters
- **Weather Removal**: Changing weather removes sun-based boost
- **Ability Suppression**: Neutralizing Gas, Mold Breaker effects
- **Item Removal**: Knock Off, Trick remove Booster Energy
- **Stat Reduction**: Lowering stats can change which is highest

### Synergies
- **Sun Setters**: Drought, Desolate Land users
- **Weather Extenders**: Heat Rock extends sun duration
- **Stat Boosters**: Moves that raise stats can influence which gets boosted
- **Speed Control**: Pairs with other speed-boosting effects

### Version History
- Added in Elite Redux as a signature Paradox ability
- Shares mechanics with Quark Drive (Electric Terrain version)
- Part of the modern Paradox Pokemon design philosophy
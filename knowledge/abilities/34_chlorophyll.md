---
id: 34
name: Chlorophyll
status: reviewed
character_count: 45
---

# Chlorophyll - Ability ID 34

## In-Game Description
"This Pokemon's Speed gets a 1.5x boost if sun is active."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the Pokemon's Speed by 50% during sun.

## Detailed Mechanical Explanation
*For Discord/reference use*

**CHLOROPHYLL** is a stat-boosting ability that increases Speed in sunlight conditions.

### Activation Mechanics:
- **Trigger**: During stat calculation when Speed is being calculated (onStat hook)
- **Condition**: Battler must be affected by any form of sun weather
- **Boost**: 1.5x Speed multiplier (50% increase)
- **Weather Types**: All sun conditions (WEATHER_SUN_ANY)

### Sun Weather Compatibility:
1. **Temporary Sun**: 8 turns from Drought/Sunny Day (12 with Heat Rock)
2. **Permanent Sun**: Infinite duration from certain field effects
3. **Primal Sun**: Desolate Land from Primal Groudon (cannot be overridden)

### Sun Weather Effects (Context):
- **Fire-type moves**: 1.5x power (1.2x in permanent sun)
- **Water-type moves**: 0.5x power (reduced damage)
- **Solar Beam/Solar Blade**: Skip charging turn, full power
- **Synthesis/Morning Sun/Moonlight**: Restore 67% HP instead of 50%
- **Thunder/Hurricane**: 50% accuracy (reduced from 100%)

### Ability Synergies:
- **Solar Power**: Also activated by sun, boosts Sp. Attack but causes HP loss
- **Leaf Guard**: Prevents status conditions in sun
- **Flower Gift**: Boosts Attack and Sp. Defense of team in sun
- **Harvest**: 100% chance to restore consumed berry in sun (50% otherwise)

### Technical Implementation:
```c
constexpr Ability Chlorophyll = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY)) *stat *= 1.5;
        },
};
```

### Strategic Applications:
1. **Sun Sweepers**: Fast Pokemon like Venusaur can outspeed and use Solar Beam
2. **Speed Control**: Enables slower Pokemon to become speed threats
3. **Weather Teams**: Core component of sun-based team compositions
4. **Heat Rock Synergy**: Extended sun duration maximizes Chlorophyll uptime

### Counters and Limitations:
- **Weather Change**: Immediately loses boost when sun ends or is replaced
- **Cloud Nine/Air Lock**: Negates weather effects, disabling Chlorophyll
- **Primal Weather**: Primordial Sea (heavy rain) prevents sun activation entirely
- **Trick Room**: Speed boosts become detrimental in reversed speed priority

### Common Chlorophyll Users:
- **Venusaur**: Classic sun sweeper with Solar Beam access
- **Lilligant**: Special attacker with Quiver Dance setup potential
- **Leafeon**: Physical attacker with Swords Dance capabilities
- **Tropius**: Bulky utility with Harvest synergy

### Competitive Notes:
- Essential for sun teams requiring speed control
- Heat Rock nearly mandatory for consistent sun duration
- Vulnerable to weather wars with other weather setters
- Most effective when paired with immediate sun activation (Drought lead)

### Version History:
- Gen 3: Introduced as permanent weather ability
- Gen 6+: Adapted to temporary weather system
- Elite Redux: 8-turn base duration, 12 with Heat Rock, maintains 1.5x multiplier
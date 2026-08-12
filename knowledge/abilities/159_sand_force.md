---
id: 159
name: Sand Force
status: reviewed
character_count: 87
---

# Sand Force - Ability ID 159

## In-Game Description
"Ups highest attacking stat by 1.5x in sand."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the Pokemon's highest attacking stat by 50% in sand. Immune to sandstorm damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

Sand Force is a weather-dependent ability that provides both offensive power and defensive protection in sandstorm conditions.

### Core Mechanics
- **Stat Boost**: Multiplies the Pokemon's highest attacking stat by 1.5x (50% increase)
- **Stat Selection**: Uses `GetHighestAttackingStatId()` to determine whether Attack or Special Attack is higher
- **Weather Dependency**: Only activates during sandstorm weather conditions
- **Sandstorm Immunity**: The Pokemon takes no damage from sandstorm weather

### Activation Conditions
```cpp
if (statId != GetHighestAttackingStatId(battler, TRUE)) return;
if (IsBattlerWeatherAffected(battler, WEATHER_SANDSTORM_ANY)) *stat *= 1.5;
```

The ability triggers when:
1. The stat being calculated is the Pokemon's highest attacking stat
2. Sandstorm weather is active (`WEATHER_SANDSTORM_ANY`)
3. The Pokemon is affected by weather (not holding items like Safety Goggles)

### Technical Implementation
- **Function**: `SandForce.onStat` callback
- **Weather Check**: `WEATHER_SANDSTORM_ANY` includes both temporary and permanent sandstorm
- **Stat Calculation**: Applies during stat calculation phase, before other modifiers
- **Immunity Flag**: `sandImmune = TRUE` prevents sandstorm damage

### Sandstorm Weather Types
Sand Force works with all sandstorm variants:
- **Temporary Sandstorm**: From moves like Sandstorm (5 turns)
- **Permanent Sandstorm**: From abilities like Sand Stream
- **All Sandstorm Effects**: Any weather condition flagged as `WEATHER_SANDSTORM_ANY`

### Stat Selection Logic
The ability uses `GetHighestAttackingStatId()` which:
- Compares Attack and Special Attack base stats
- Includes stat stage modifications if specified
- Returns `STAT_ATK` or `STAT_SPATK` depending on which is higher
- Considers current battle conditions and stat changes

### Damage Calculations
**Without Sand Force**: Standard damage calculation
**With Sand Force**: Attacking stat x 1.5 before damage formula

Example with 252 Attack EV Landorus-T:
- Base Attack: 145
- With EVs/Nature: ~350 Attack
- Sand Force boost: 350 x 1.5 = 525 effective Attack
- **Net damage increase**: ~50% more physical damage

### Strategic Applications
1. **Mixed Attackers**: Automatically boosts the higher attacking stat
2. **Weather Teams**: Core member of sandstorm-based teams
3. **Wallbreaking**: Significant power boost for breaking defensive cores
4. **Defensive Utility**: Sandstorm immunity allows safe switching

### Notable Users
Sand Force appears on various Pokemon in Elite Redux:
- **Sandslash**: Physical attacker with solid bulk
- **Dugtrio**: Speed and trapping with power boost
- **Golem**: Tank that benefits from mixed attacking potential
- **Landorus**: Legendary with incredible offensive presence
- **Garchomp**: Dragon/Ground type with versatile movepool

### Interactions with Other Abilities
- **Sand Stream**: Perfect partner ability for automatic sandstorm
- **Sand Bender**: Combines Sand Stream + Sand Force effects
- **Sand Rush**: Speed boost companion for comprehensive sand support
- **Weather Control**: Allows switching between weather conditions

### Competitive Usage
**Strengths**:
- Substantial 50% damage increase in preferred weather
- Automatically selects optimal attacking stat
- Sandstorm immunity provides longevity
- Works well with sand-setting teammates

**Weaknesses**:
- Completely weather-dependent
- Vulnerable to weather changing moves/abilities
- No benefit outside of sandstorm
- Competing weather conditions shut it down

### Counters and Checks
1. **Weather Control**: Rain Dance, Sunny Day, Hail override sandstorm
2. **Weather Abilities**: Drizzle, Drought, Snow Warning change conditions
3. **Air Lock/Cloud Nine**: Suppress all weather effects
4. **Safety Goggles**: Prevents weather damage but doesn't affect Sand Force boost

### Team Synergies
**Sand Core Partners**:
- Sand Stream setters (Tyranitar, Hippowdon)
- Sand Rush sweepers for speed control
- Rock/Steel/Ground types for weather immunity
- Excadrill for Rapid Spin support

**Move Synergies**:
- **Earthquake**: STAB Ground move benefits from Attack boost
- **Stone Edge**: Rock moves get power boost if Attack is higher
- **Stealth Rock**: Hazard setting while benefiting from power
- **U-turn**: Pivoting move that can hit hard with boosted Attack

### Version History
Sand Force maintains consistent mechanics across Elite Redux versions, providing reliable sandstorm-based offense for dedicated weather teams.
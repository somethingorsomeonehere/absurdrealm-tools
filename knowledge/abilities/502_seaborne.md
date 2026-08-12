---
id: 502
name: Seaborne
status: reviewed
character_count: 91
---

# Seaborne - Ability ID 502

## In-Game Description
"Drizzle + Swift Swim."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entry, sets rain weather for 8 turns. During rain, the user's Speed is boosted by 50%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Seaborne is a powerful combination ability that merges two distinct weather-related effects:
1. **Drizzle component**: Automatically sets rain weather upon entering battle
2. **Swift Swim component**: Provides 50% Speed boost during any rain weather

The ability essentially makes the Pokemon both a weather setter and a weather abuser simultaneously.

### Activation Conditions
**Drizzle Component:**
- **Entry trigger**: Activates automatically when the Pokemon enters battle
- **Weather setting**: Sets rain weather for 8 turns (Elite Redux extended duration)
- **Priority**: Cannot override Primal weather (Desolate Land/Primordial Sea)
- **Failure cases**: Shows "blocked by primal weather" message if primal weather is active

**Swift Swim Component:**
- **Weather requirement**: Any form of rain weather must be active
  - Regular rain (from Rain Dance, Drizzle, or this ability)
  - Heavy rain (from Downpour - unused but supported)
  - Permanent rain (from abilities like Drizzle)
  - Primordial Sea (primal rain weather)
- **Speed boost**: Multiplies Speed stat by 1.5 (50% increase)
- **Continuous effect**: Active as long as rain weather persists

### Technical Implementation
```c
// Seaborne combines two existing ability implementations
constexpr Ability Seaborne = {
    .onEntry = Drizzle.onEntry,    // Sets rain on entry
    .onStat = SwiftSwim.onStat,    // Speed boost in rain
};

// Drizzle component (entry effect)
.onEntry = +[](ON_ENTRY) -> int {
    if (TryChangeBattleWeather(battler, ENUM_WEATHER_RAIN, TRUE)) {
        BattleScriptPushCursorAndCallback(BattleScript_DrizzleActivates);
        return TRUE;
    } else if (gBattleWeather & WEATHER_PRIMAL_ANY && WEATHER_HAS_EFFECT) {
        BattleScriptPushCursorAndCallback(BattleScript_BlockedByPrimalWeatherEnd3);
        return NO_ANNOUNCE;
    }
    return FALSE;
},

// Swift Swim component (speed boost)
.onStat = +[](ON_STAT) {
    if (statId == STAT_SPEED && IsBattlerWeatherAffected(battler, WEATHER_RAIN_ANY)) 
        *stat *= 1.5;
},
```

### Weather Interactions
**Rain Types Supported:**
- `WEATHER_RAIN_TEMPORARY`: From Rain Dance or similar moves
- `WEATHER_RAIN_DOWNPOUR`: Unused variant but supported
- `WEATHER_RAIN_PERMANENT`: From Drizzle-type abilities
- `WEATHER_RAIN_PRIMAL`: From Primordial Sea

**Weather Override Behavior:**
- Cannot set rain if Desolate Land (extremely harsh sunlight) is active
- Cannot set rain if Primordial Sea is already active (redundant)
- Can be overridden by other weather-setting abilities or moves
- Will show appropriate failure messages when blocked

### Important Interactions
**Entry Scenarios:**
- **Normal entry**: Sets rain and immediately gains Speed boost
- **Primal weather active**: Cannot set rain, but gains Speed boost if Primordial Sea is active
- **Other weather active**: Overrides existing non-primal weather with rain
- **Multiple weather setters**: Last one to enter determines weather

**Speed Boost Mechanics:**
- **Stat calculation**: Applied during Speed stat calculations, not a temporary boost
- **Stackable**: Can stack with other Speed modifiers (Choice Scarf, stat boosts, etc.)
- **Persistent**: Lasts as long as rain weather is active
- **Immediate**: Takes effect instantly when rain becomes active

**Battle AI Recognition:**
```c
case ABILITY_SEABORNE:
case ABILITY_DRIZZLE:
    return AI_SCORE_RAIN;  // AI values this for rain setting
```

### Strategic Implications
**Offensive Advantages:**
- **Self-sufficient setup**: Provides both weather and Speed boost
- **Immediate threat**: Can sweep right after entry
- **Water move synergy**: Rain boosts Water-type moves by 50%
- **Thunder accuracy**: Perfect accuracy Thunder in rain

**Defensive Considerations:**
- **Weather dependency**: Speed boost lost if weather changes
- **Priority moves**: Still vulnerable to priority attacks
- **Weather wars**: Competing weather setters can nullify benefits
- **Ability suppression**: Completely shut down by Mold Breaker variants

### Current Users
**Manaphy** (SPECIES_MANAPHY):
- **Type**: Water
- **Base Stats**: 100/100/100/100/100/100 (600 BST legendary)
- **Ability Slots**: 
  - Seaborne (changeable)
  - Power Spot (changeable)
  - Healer (changeable)
- **Innate Abilities**: Change of Heart, Parental Bond, High Tide
- **Role**: Legendary Water-type with exceptional versatility

### Competitive Usage Notes
**Team Composition:**
- **Rain team core**: Serves as both setter and sweeper
- **Speed control**: Provides reliable Speed advantage
- **Weather support**: Enables other rain abusers on the team
- **Wallbreaking**: 50% Water move boost + Speed for breaking defensive cores

**Item Synergies:**
- **Damp Rock**: Extends rain duration from 8 to 12 turns
- **Life Orb**: Raw power boost to capitalize on Speed advantage
- **Choice items**: Stack with Speed boost for overwhelming pressure
- **Leftovers**: Sustain for longer rain presence

### Counters
**Weather Control:**
- **Opposing weather**: Drought, Sand Stream, Snow Warning abilities
- **Weather moves**: Sunny Day, Sandstorm, Hail to override rain
- **Primal abilities**: Desolate Land prevents rain setting entirely
- **Cloud Nine/Air Lock**: Negates weather effects completely

**Speed Control:**
- **Priority moves**: Aqua Jet, Sucker Punch bypass Speed advantage
- **Trick Room**: Reverses Speed advantage completely
- **Paralysis**: Reduces Speed and adds chance of full paralysis
- **Choice Scarf**: Faster Choice Scarf users can still outspeed

**Ability Suppression:**
- **Mold Breaker**: Ignores ability completely
- **Neutralizing Gas**: Suppresses ability while active
- **Skill Swap/Role Play**: Can steal or change the ability
- **Simple Beam**: Changes ability to Simple

### Synergies
**Rain Team Members:**
- **Swift Swim users**: Double Speed boost synergy
- **Rain Dish users**: Passive healing in shared weather
- **Thunder users**: Perfect accuracy in rain
- **Water Absorb**: Immunity to Water moves in rain teams

**Move Synergies:**
- **Hurricane**: Perfect accuracy in rain
- **Thunder**: Perfect accuracy + high damage
- **Surf/Hydro Pump**: 50% damage boost in rain
- **Weather Ball**: Becomes Water-type with 100 BP in rain

### Version History
- **Elite Redux exclusive**: Combination ability not found in official games
- **Generation concept**: Combines Generation III (Drizzle) and Generation III (Swift Swim) mechanics
- **Extended weather**: Benefits from Elite Redux's 8-turn weather duration
- **Legendary exclusive**: Currently only available to Manaphy

### Design Philosophy
Seaborne represents the ultimate rain ability, combining weather control with immediate offensive presence. It eliminates the traditional setup requirement of rain teams by providing both the weather condition and the Speed boost in a single ability slot, making it exceptionally powerful for legendary Pokemon like Manaphy.
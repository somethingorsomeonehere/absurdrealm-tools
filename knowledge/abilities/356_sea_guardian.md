---
id: 356
name: Sea Guardian
status: reviewed
character_count: 140
---

# Sea Guardian - Ability ID 356

## In-Game Description
"When entering battle during rain, boosts the highest stat by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When entering battle during rain, Sea Guardian boosts your highest stat by one stage. Works with any rain type. Triggers once per switch-in.

## Detailed Mechanical Explanation

### Overview

Sea Guardian is a weather-dependent entry ability that provides an immediate stat boost when switching into battle during rain conditions. The ability intelligently selects the Pokemon's highest current stat (including existing modifications) and raises it by one stage, making it highly adaptable to different battle situations.

## Mechanics

### Activation Requirements
- **Weather**: Any form of rain weather must be active
- **Trigger**: Activates on entry (switching in or battle start)
- **One-time**: Only triggers once per battle entry

### Weather Detection
The ability recognizes all rain types:
- Standard Rain (5/8 turns)
- Permanent Rain effects
- Primordial Sea (infinite rain)

### Stat Selection Process
1. Calculates current values for all five battle stats
2. Includes existing stat stage modifications
3. Selects the highest total value
4. Applies +1 stage boost to that stat

## Code Implementation

**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 3753-3763)

```cpp
constexpr Ability SeaGuardian = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(IsBattlerWeatherAffected(battler, WEATHER_RAIN_ANY))
        CHECK(ChangeStatBuffs(battler, 1, GetHighestStatId(battler, TRUE), MOVE_EFFECT_AFFECTS_USER, NULL))
        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        return TRUE;
    },
};
```

### Key Functions
- `IsBattlerWeatherAffected()`: Checks for rain weather affecting the Pokemon
- `GetHighestStatId(battler, TRUE)`: Determines highest stat including current stages
- `ChangeStatBuffs()`: Applies the +1 stage boost

## Strategic Applications

### Offensive Usage
- Boosts Attack for physical sweepers in rain
- Enhances Special Attack for special attackers
- Provides Speed boosts for fast pivots

### Defensive Usage
- Improves bulk with Defense/Special Defense boosts
- Adapts to current battle conditions automatically

### Weather Team Synergy
- Perfect for Rain teams with Drizzle setters
- Combines well with Swift Swim and other rain abilities
- Provides immediate value upon entry

## Pokemon Distribution

Sea Guardian appears on 16 different Pokemon, including:

**Water-type Legends**: Gyarados, Suicune, Milotic, Kyogre, Palkia
**Mega Forms**: Mega Kingdra variants, Mega Gallade Redux
**Redux Variants**: Gible/Gabite/Garchomp Redux line
**Mixed Types**: Various Water-types and rain-associated Pokemon

## Competitive Analysis

### Strengths
- Immediate stat boost without turn investment
- Adapts to current battle state intelligently
- Strong synergy with rain teams
- Unpredictable boost target makes it hard to counter

### Weaknesses
- Weather dependency limits activation
- One-time use per entry
- Can be disrupted by weather removal
- Boost can be negated by stat reset moves

### Counters
- **Weather Control**: Removes rain conditions
- **Clear Smog/Haze**: Resets stat boosts
- **Air Lock/Cloud Nine**: Negates weather effects
- **Rapid weather changes**: Can prevent activation

## Related Abilities

- **Majestic Moth**: Similar highest stat boost without weather requirement
- **Intrepid Sword/Dauntless Shield**: Fixed stat boosts on entry
- **Download**: Context-sensitive stat boost ability
- **Weather-dependent abilities**: Swift Swim, Chlorophyll, etc.

## Battle Messages

When Sea Guardian activates:
- Shows ability activation message
- Displays stat boost notification
- Updates battle display with new stat stage

## Technical Notes

- Uses standard stat boost mechanics
- Cannot boost beyond +6 stages
- Fails if already at maximum boost for the highest stat
- Weather immunity abilities can prevent activation
- Works in all battle formats (singles, doubles, etc.)

## Code References

- **Implementation**: `src/abilities.cc:3753-3763`
- **Weather Check**: `src/battle_util.c` (IsBattlerWeatherAffected)
- **Stat Selection**: `src/battle_util.c` (GetHighestStatId)
- **Battle Script**: `data/battle_scripts_1.s` (BattleScript_AttackerAbilityStatRaiseEnd3)
- **Ability ID**: 356 (ABILITY_SEA_GUARDIAN)


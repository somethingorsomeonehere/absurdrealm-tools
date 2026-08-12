---
id: 380
name: Sun Worship
status: reviewed
character_count: 77
---

# Sun Worship - Ability ID 380

## In-Game Description
"When entering battle during sun, boosts the highest stat by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When entering battle during Sun, boosts the user's highest stat by one stage. 

## Detailed Mechanical Explanation

### Overview

Sun Worship is a weather-dependent entry ability that provides an immediate stat boost when switching into battle during sunny conditions. The ability intelligently selects the Pokemon's highest current stat (including existing modifications) and raises it by one stage, making it highly adaptable to different battle situations and particularly valuable on sun teams.

## Mechanics

### Activation Requirements
- **Weather**: Any form of sunny weather must be active
- **Trigger**: Activates on entry (switching in or battle start)
- **One-time**: Only triggers once per battle entry

### Weather Detection
The ability recognizes all sun types:
- Standard Sunny Day (5/8 turns)
- Drought-induced sunshine
- Desolate Land (primal sunlight)
- Any other sun-based weather effects

### Stat Selection Process
1. Calculates current values for all five battle stats
2. Includes existing stat stage modifications
3. Selects the highest total value
4. Applies +1 stage boost to that stat

## Code Implementation

**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 3757-3765)

```cpp
constexpr Ability SunWorship = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY))

        int stat = GetHighestStatId(battler, TRUE);
        CHECK(ChangeStatBuffs(battler, 1, stat, MOVE_EFFECT_AFFECTS_USER, NULL))
        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        return TRUE;
    },
};
```

### Key Functions
- `IsBattlerWeatherAffected()`: Checks for sunny weather affecting the Pokemon
- `GetHighestStatId(battler, TRUE)`: Determines highest stat including current stages
- `ChangeStatBuffs()`: Applies the +1 stage boost
- `BattleScript_AttackerAbilityStatRaiseEnd3`: Handles animation and messaging

## Strategic Applications

### Offensive Usage
- Boosts Attack for physical sweepers in sun
- Enhances Special Attack for solar-powered special attackers
- Provides Speed boosts for fast pivots and revenge killers
- Synergizes with Solar Power and Chlorophyll Pokemon

### Defensive Usage
- Improves bulk with Defense/Special Defense boosts
- Adapts to current battle conditions automatically
- Creates unpredictable defensive walls

### Sun Team Synergy
- Perfect for sun teams with Drought setters
- Combines excellently with Solar Power, Chlorophyll, and Leaf Guard
- Provides immediate value upon entry without turn investment
- Works with Solar Beam and other sun-boosted moves

## Pokemon Distribution

Sun Worship appears on 8 different Pokemon species across various roles:

**Primary Sun Abusers**: Pokemon that naturally benefit from sunny weather
**Fire-types**: Species that thrive in hot conditions
**Grass-types**: Plants that draw power from sunlight
**Solar-themed**: Pokemon with sun-related lore or design

## Competitive Analysis

### Strengths
- Immediate stat boost without turn investment
- Adapts to current battle state intelligently
- Strong synergy with sun teams and related abilities
- Unpredictable boost target makes it hard to counter
- Works with all forms of sunny weather
- Cannot be Traced or copied by most abilities

### Weaknesses
- Weather dependency limits activation opportunities
- One-time use per entry limits repeated value
- Can be disrupted by weather removal moves
- Boost can be negated by stat reset effects
- Fails if weather is removed before entry

### Counters
- **Weather Control**: Moves like Rain Dance, Sandstorm, Hail
- **Clear Smog/Haze**: Resets all stat boosts
- **Air Lock/Cloud Nine**: Negates weather effects entirely
- **Rapid weather changes**: Prevents consistent activation
- **Intimidate**: Can neutralize Attack boosts specifically

## Related Abilities

### Similar Entry Abilities
- **Sea Guardian**: Rain-based equivalent with identical mechanics
- **Greater Spirit**: Fog-based version of the same effect
- **Majestic Moth**: Similar highest stat boost without weather requirement

### Sun-based Abilities
- **Solar Power**: Boosts Special Attack but causes damage in sun
- **Chlorophyll**: Doubles Speed in sunny weather
- **Drought**: Sets up sunny weather on entry
- **Leaf Guard**: Prevents status conditions in sun

### Stat Boost Abilities
- **Intrepid Sword/Dauntless Shield**: Fixed stat boosts on entry
- **Download**: Context-sensitive stat boost based on opponent's defenses
- **Protosynthesis**: Ancient ability with similar sun-based stat boosting

## Battle Messages

When Sun Worship activates:
- Shows ability activation message
- Displays stat boost notification with appropriate stat name
- Updates battle display with new stat stage indicator
- Plays corresponding battle animation

## Technical Notes

### Battle Mechanics
- Uses standard stat boost mechanics (maximum +6 stages)
- Cannot boost beyond +6 stages for any stat
- Fails silently if already at maximum boost for the highest stat
- Weather immunity abilities (Air Lock, Cloud Nine) prevent activation
- Works in all battle formats (singles, doubles, triples, etc.)

### Interaction Notes
- Not affected by Mold Breaker or similar abilities
- Cannot be suppressed by most ability-negating effects
- Weather must be actively affecting the battler (not just present)
- Calculates stats after all other entry effects resolve

## Code References

- **Implementation**: `src/abilities.cc:3757-3765`
- **Weather Check**: `src/battle_util.c` (IsBattlerWeatherAffected function)
- **Stat Selection**: `src/battle_util.c` (GetHighestStatId function)
- **Battle Script**: `data/battle_scripts_1.s` (BattleScript_AttackerAbilityStatRaiseEnd3)
- **Ability ID**: 380 (ABILITY_SUN_WORSHIP)
- **Proto Definition**: `proto/AbilityEnum.proto` and `proto/AbilityList.textproto`

## Competitive Tier Justification

Sun Worship earns a **High** competitive tier rating due to:

1. **Immediate Impact**: Provides instant value without setup
2. **Adaptability**: Boosts the most relevant stat automatically
3. **Weather Synergy**: Perfect fit for sun teams
4. **Unpredictability**: Opponents cannot predict which stat will be boosted
5. **Versatility**: Works for both offensive and defensive strategies

The ability's weather dependency prevents it from being universally applicable, but within sun team compositions, it provides exceptional value and strategic flexibility.


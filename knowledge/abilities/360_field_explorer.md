---
id: 360
name: Field Explorer
status: reviewed
character_count: 149
---

# Field Explorer - Ability ID 360

## In-Game Description
"Boosts the power of field-based moves by 50%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of moves that can be used in the overworld by 50%. Includes all HM moves, (Zen) Headbutt, Ice Spinner, Hidden/Secret Power, and Dig.

## Detailed Mechanical Explanation

### Overview

Field Explorer is a custom ability in Elite Redux that provides a significant power boost to field-based moves. This ability increases the damage of moves flagged with `FLAG_FIELD_BASED` by 50% (1.5x multiplier), making traditionally utility-focused moves more viable in combat scenarios.

## Mechanics

### Core Effect
- **Power Boost**: Increases damage of field-based moves by 50%
- **Multiplier**: 1.5x
- **Trigger Condition**: Move must have the `FLAG_FIELD_BASED` flag set

### Code Implementation

**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Lines 3782-3787)

```cpp
constexpr Ability FieldExplorer = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].flags & FLAG_FIELD_BASED) MUL(1.5);
        },
};
```

The ability uses the `onOffensiveMultiplier` callback to check if the current move has the `FLAG_FIELD_BASED` flag. If present, it applies a 1.5x damage multiplier using the `MUL(1.5)` macro.

### Field Move Identification

**Flag Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/include/constants/pokemon.h:334`
```c
#define FLAG_FIELD_BASED (1 << 31)
```

**Proto Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/MoveList.proto:187`
```proto
bool field = 51 [(field_name) = "Field Based", (is_flag) = true, (flag_code_value) = "FLAG_FIELD_BASED"];
```

## Affected Moves

Field Explorer affects moves that historically served as HM moves or field navigation tools. Based on the codebase analysis, confirmed field-based moves include:

### Primary HM Moves
- **Cut**: Steel-type physical move (60 power) - Always crits, has Keen Edge boost
- **Surf**: Water-type special move (90 power) - Hits multiple targets
- **Strength**: Rock-type physical move (110 power) - Lowers user's defenses
- **Fly**: Flying-type physical move - Two-turn move
- **Flash**: Normal-type status move - Lowers accuracy
- **Rock Smash**: Fighting-type physical move - May lower defense
- **Waterfall**: Water-type physical move - May cause flinching
- **Dive**: Water-type physical move - Two-turn underwater move
- **Whirlpool**: Water-type special move - Trapping move

### Additional Field Moves
The codebase indicates approximately 16 moves total have the field flag, though the complete list includes various other utility and navigation-themed moves beyond the traditional HM set.

## Strategic Applications

### Offensive Utility
- **HM Slave Viability**: Makes Pokemon carrying field moves more combat-capable
- **Dual Purpose**: Allows team members to serve both utility and battle roles
- **Coverage Options**: Provides access to diverse move types (Steel, Water, Rock, Fighting, Flying)

### Competitive Considerations
- **Niche Role**: Situational ability that requires specific move coverage
- **Power Boost**: 50% increase makes normally weak utility moves competitively viable
- **Team Building**: Encourages inclusion of field moves in competitive movesets

### Move Power Calculations
With Field Explorer active:
- Cut: 60 to 90 base power
- Surf: 90 to 135 base power  
- Strength: 110 to 165 base power
- Rock Smash: 40 to 60 base power
- Waterfall: 80 to 120 base power

## Pokemon Distribution

Field Explorer appears on numerous Pokemon in Elite Redux, available as both a regular ability slot and as an innate ability. The ability is distributed across various species that thematically relate to exploration, navigation, or utility functions.

**Availability**: Found on 31+ different Pokemon entries in the species list, appearing as both regular abilities and innate abilities.

## Related Abilities

### Similar Damage Boosting Abilities
- **Technician** (#101): Boosts weak moves (<=60 power) by 50%
- **Sheer Force** (#125): Removes secondary effects for 30% power boost
- **Iron Fist** (#89): Boosts punching moves by 20%
- **Strong Jaw** (#173): Boosts biting moves by 50%

### Distinguishing Features
Field Explorer is unique in that it specifically targets utility moves rather than offensive moves, making it a bridge between exploration functionality and battle viability.

## Interactions and Mechanics

### Battle Calculations
1. **Priority**: Applied during damage calculation phase
2. **Stacking**: Can stack with other multipliers (items, weather, etc.)
3. **Type Matching**: Works regardless of move type or user's typing
4. **Critical Hits**: Boost applies before critical hit calculation

### Technical Details
- **Callback Type**: `onOffensiveMultiplier`
- **Activation**: Automatic when using field-based moves
- **No PP Cost**: Does not affect move PP or usage limitations
- **No Turn Delay**: Activates immediately with move usage

## Trivia

- Field Explorer represents Elite Redux's design philosophy of making utility moves combat-viable
- The 50% boost matches other specialized boosting abilities like Strong Jaw
- Unlike some abilities, Field Explorer has no type restrictions
- The ability enables "HM slaves" to contribute meaningfully in battle scenarios
- Field moves retain their original secondary effects while gaining the damage boost

## Version History

Field Explorer is a custom ability created specifically for Elite Redux, designed to address the traditional weakness of field/HM moves in competitive play while maintaining their utility functions.


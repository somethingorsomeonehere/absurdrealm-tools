---
id: 280
name: Crystallize
status: reviewed
character_count: 83
---

# Crystallize - Ability ID 280

## In-Game Description
"Rock-type moves become Ice and get a 1.1x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Crystallize converts all Rock-type moves to Ice-type and boosts their power by 10%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Crystallize is a type-conversion ability that transforms all Rock-type moves into Ice-type moves while providing a damage boost.

### Core Mechanics
- **Type Conversion**: All Rock-type moves become Ice-type before damage calculation
- **Power Boost**: Converted moves receive a 1.1x (10%) damage multiplier
- **STAB Interaction**: Ice-type Pokemon gain STAB on converted moves
- **Type Effectiveness**: Converted moves use Ice-type effectiveness chart

### Technical Implementation
```cpp
constexpr Ability Crystallize = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_ICE && gBattleStruct->ateBoost[battler]) MUL(1.1);
        },
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(moveType == TYPE_ROCK)
        *ateBoost = TRUE;
        return TYPE_ICE + 1;
    },
};
```

### Affected Moves (All 34 Rock-type moves)
**Physical Attacks**: Stone Edge, Rock Slide, Rock Blast, Head Smash, Accelerock, Diamond Storm, Thousand Arrows
**Status Moves**: Stealth Rock, Sandstorm, Rock Polish, Wide Guard
**Special Attacks**: Power Gem, Ancient Power, Meteor Beam
**And 21+ other Rock-type moves**

### Activation Conditions
- Pokemon must have Crystallize ability
- Move must originally be Rock-type
- Works on all Rock moves: physical, special, and status
- Functions in all battle formats

### Damage Calculations
**Example with Stone Edge (base 100 power)**:
- Normal Stone Edge: 100 base power
- With Crystallize: 100 x 1.1 = 110 effective power
- Against Fire-type: 110 x 2.0 = 220 damage multiplier (Ice super effective)
- With STAB (Ice user): 110 x 1.5 = 165 base power before type effectiveness

### Strategic Implications
**Advantages**:
- Converts poor Rock typing to superior Ice offensive typing
- Ice hits Flying, Grass, Ground, Dragon for super effective damage
- Removes Rock's weaknesses to Fighting, Ground, Steel, Water, Grass
- 10% power boost improves overall damage output

**Disadvantages**:
- Loses Rock's advantages against Flying, Fire, Ice, Bug
- Ice resisted by Fire, Water, Ice, Steel types
- Status moves like Stealth Rock become Ice-type (changes interactions)

### Common Users
- **Mega Slaking**: Innate ability, benefits from powerful Rock moves
- **Mega Slaking (Ape Shift)**: Alternative form with same benefit
- **Mega Glalie**: Primary ability choice, enhances offensive capabilities

### Competitive Usage
- **Physical Sweeper Role**: Stone Edge becomes reliable Ice STAB
- **Mixed Attacker**: Benefits both physical and special Rock moves
- **Hazard Control**: Stealth Rock becomes Ice-type entry hazard
- **Coverage Tool**: Provides Ice coverage for non-Ice types

### Interactions with Other Abilities/Items
- **Refrigerate/Pixilate/Aerilate**: Does not stack with other -ate abilities
- **Normalize**: Crystallize takes precedence over Normalize
- **Liquid Voice**: Only affects sound moves, doesn't interfere
- **Choice Items**: Compatible, locks into converted Ice move
- **Weakness Policy**: Activates based on Ice typing, not original Rock

### Counters
- **Fire-types**: Resist converted Ice moves
- **Water-types**: Resist Ice, common defensive types
- **Steel-types**: Resist Ice, often defensive walls
- **Thick Fat**: Reduces Ice damage by 50%
- **Flash Fire**: Doesn't apply to Ice moves

### Synergies
- **Snow Warning**: Sets up hail for additional Ice synergy
- **Slush Rush**: Speed boost in hail complements Ice typing
- **Ice Body**: Healing in hail pairs well with Ice moves
- **Aurora Veil**: Defensive support for Ice-type teams

### Version History
- Introduced in Elite Redux as part of expanded ability roster
- ID 280 in the ability enum
- Similar to other -ate abilities but specifically Rock to Ice conversion
- Unique 1.1x multiplier distinguishes it from standard 1.2x -ate abilities
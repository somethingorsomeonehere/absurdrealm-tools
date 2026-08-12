---
id: 544
name: Airborne
status: reviewed
character_count: 91
---

# Airborne - Ability ID 544

## In-Game Description
"Boosts own & ally's Flying-type moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the power of Flying-type moves by 30% for both the user and its allies in battle. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Power Multiplier**: 1.3x (30% boost) to all Flying-type moves
- **Scope**: Affects both the user and ally Pokemon in double battles
- **Move Type Detection**: Checks if `moveType == TYPE_FLYING` (type constant 2)
- **Application**: Uses `onOffensiveMultiplier` callback with `APPLY_ON_ALLY` flag

### Technical Implementation
```cpp
constexpr Ability Airborne = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FLYING) MUL(1.3);
        },
    .onOffensiveMultiplierFor = APPLY_ON_ALLY,
};
```

### Activation Conditions
- Must be a Flying-type move
- Works in both single and double battles
- In doubles, affects both user and ally simultaneously
- No weather, terrain, or status requirements

### Affected Moves (All Flying-type moves including)
- Physical moves: Aerial Ace, Brave Bird, Drill Peck, Fly, etc.
- Special moves: Air Slash, Hurricane, Heat Wave (if Flying-type), etc.
- Status moves: No effect on status moves as they don't deal damage

### Interactions with Other Mechanics
- **Stacks multiplicatively** with other power boosts (items, abilities, weather)
- **Type-changing abilities**: If a move becomes Flying-type via Aerilate, Airborne will boost it
- **Z-moves and Max moves**: Boosted if they are Flying-type
- **Multi-hit moves**: Each hit receives the 1.3x boost

### Strategic Implications
- **Team Synergy**: Excellent for Flying-type teams or mixed teams with Flying attackers
- **Double Battle Focus**: Particularly powerful in VGC/double format
- **Coverage Support**: Helps Pokemon with Flying STAB or coverage moves
- **Wallbreaking**: 30% boost can turn 2HKOs into potential OHKOs

### Example Damage Calculations
- Brave Bird (120 BP) to 156 effective BP with Airborne
- Hurricane (110 BP) to 143 effective BP with Airborne
- Air Slash (75 BP) to 97.5 effective BP with Airborne

### Common Users
Flying-type Pokemon that benefit from team support, particularly those used in double battles or on Flying-type themed teams.

### Competitive Usage Notes
- **VGC Viability**: Strong in doubles format where ally support is most valuable
- **Team Building**: Pairs well with multiple Flying-type attackers
- **Counterplay**: Flying-type moves are still resisted by Rock, Electric, and Steel types

### Counters
- **Type Resistances**: Rock, Electric, Steel types take reduced damage
- **Abilities**: Storm Drain doesn't affect this, but abilities that change move types can alter interactions
- **Items**: Air Balloon makes Pokemon immune to Ground but doesn't affect Flying moves

### Synergies
- **Flying Gem**: Stack with consumable item for massive one-time boost
- **Tailwind**: Speed support for Flying-type teammates
- **Flying-type STAB**: Combines with natural same-type attack bonus for 1.95x total multiplier

### Version History
- Added in Elite Redux as part of the expanded ability roster
- ID 544 in the ability enum (ABILITY_AIRBORNE)
- Uses modern ally support mechanics introduced in Elite Redux
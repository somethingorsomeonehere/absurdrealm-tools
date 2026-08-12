---
id: 571
name: Fire Scales
status: reviewed
character_count: 97
---

# Fire Scales - Ability ID 571

## In-Game Description
"Halves damage taken by Special moves. Does NOT double SpDef."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves all incoming special attack damage. Multiplicative with other sources of damage reduction.   

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fire Scales applies a 50% damage reduction to all incoming special attacks through the `onDefensiveMultiplier` callback in the battle damage calculation engine.

### Technical Implementation
```cpp
constexpr Ability FireScales = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_SPECIAL(move)) MUL(.5);
        },
    .breakable = TRUE,
};
```

### Key Differences from Similar Abilities
- **vs Marvel Scale**: Marvel Scale increases Defense AND Special Defense stats by 50% when status afflicted. Fire Scales directly reduces special damage by 50% with no stat changes or status requirements.
- **vs Ice Scales**: Fire Scales uses identical code to Ice Scales - both halve special damage taken.
- **vs Thick Fat**: Fire Scales affects ALL special moves, while Thick Fat only affects Fire and Ice-type moves.

### Activation Conditions
- Activates against any special attack (moves with special damage category)
- No status condition, weather, or HP threshold requirements
- Always active when the Pokemon has this ability

### Affected Moves
Fire Scales affects all moves categorized as special attacks, including:
- All special attacking moves (Flamethrower, Surf, Thunderbolt, etc.)
- Special Z-moves and Max moves
- Multi-hit special moves (each hit is reduced)
- Variable power special moves

### Interactions with Other Mechanics
- **Damage Calculation Order**: Applied during the defensive multiplier phase, after type effectiveness but before final damage calculation
- **Critical Hits**: Still reduces damage even on critical hits
- **STAB/Type Effectiveness**: Reduction applies after STAB and type effectiveness calculations
- **Other Damage Reductions**: Stacks multiplicatively with other damage reduction effects
- **Mold Breaker Effects**: Can be bypassed by abilities that ignore defensive abilities
- **Breakable**: Listed as breakable = TRUE, meaning it can be suppressed by certain effects

### Strategic Implications
- **Special Wall**: Transforms Pokemon into effective special walls regardless of base Special Defense
- **Type Coverage**: Provides universal special defense unlike type-specific resistances
- **HP Investment**: Allows for more HP investment since special bulk is effectively doubled
- **Mixed Attackers**: Forces opponents to rely more heavily on physical attacks

### Example Damage Calculations
- 100 Base Power special move normally dealing 200 damage to deals 100 damage
- Super effective special move (2x damage) dealing 400 damage to deals 200 damage
- Critical hit special move dealing 300 damage to deals 150 damage

### Common Users
Based on the codebase analysis, Fire Scales appears on:
- Charizard Mega Z (as an innate ability alongside Hellblaze and Flame Shield)
- Several other Fire-type Pokemon as either a regular or innate ability

### Competitive Usage Notes
- **Team Role**: Excellent for special defensive pivots and walls
- **Item Synergy**: Works well with Leftovers, Assault Vest alternatives, or offensive items
- **Move Coverage**: Pairs well with moves that punish physical attackers (Will-O-Wisp, etc.)

### Counters
- **Physical Attacks**: Fire Scales provides no protection against physical moves
- **Status Moves**: Non-damaging moves are unaffected
- **Mold Breaker**: Abilities like Mold Breaker, Teravolt, and Turboblaze ignore Fire Scales
- **Ability Suppression**: Gastro Acid, Simple Beam, and similar moves disable the effect

### Synergies
- **Physical Bulk**: Pokemon with naturally high Defense benefit most
- **Recovery Moves**: Pairs excellently with reliable recovery
- **Status Moves**: Can freely use status moves while tanking special attacks
- **Entry Hazards**: Can safely set hazards against special attackers

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Shares implementation code with Ice Scales ability
- Distinguishes itself from Marvel Scale through damage reduction vs. stat boost mechanics
---
id: 272
name: Prism Scales
status: reviewed
character_count: 121
---

# Prism Scales - Ability ID 272

## In-Game Description
"Takes 30% less damage from Special attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prism Scales reduces damage from all Special attacks by 30%. Stacks multiplicatively with other damage reduction sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Damage Reduction**: Multiplies incoming special attack damage by 0.7 (30% reduction)
- **Activation**: Triggers automatically when the Pokemon is targeted by any special attack
- **Move Classification**: Uses the `IS_MOVE_SPECIAL(move)` check to determine if a move is special

### Technical Implementation
```c
constexpr Ability PrismScales = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_SPECIAL(move)) MUL(.7);
        },
    .breakable = TRUE,
};
```

### Activation Conditions
- Target must have Prism Scales ability
- Incoming move must be classified as special
- Ability must not be suppressed or broken

### Numerical Values
- **Damage Multiplier**: 0.7 (30% damage reduction)
- **Effective HP Increase**: ~43% more bulk against special attacks
- **Breakable**: Yes, can be bypassed by Mold Breaker, Teravolt, Turboblaze

### Complete List of Affected Moves
All moves with the Special category are affected, including:
- Standard special attacks (Flamethrower, Surf, Thunderbolt, etc.)
- Multi-hit special moves (each hit reduced by 30%)
- Variable power special moves (Weather Ball, Hidden Power, etc.)
- Status moves that deal damage (Seismic Toss, Night Shade are NOT affected as they're physical)

### Interactions with Other Abilities/Mechanics
- **Mold Breaker Effects**: Completely bypassed by Mold Breaker, Teravolt, Turboblaze
- **Type Resistances**: Stacks multiplicatively with type resistances and weaknesses
- **Critical Hits**: Critical hits still receive the 30% reduction
- **Multi-hit Moves**: Each individual hit is reduced by 30%
- **Weather/Terrain**: Does not interact with weather or terrain effects
- **Items**: Stacks with defensive items like Assault Vest

### Strategic Implications
- **Defensive Core**: Excellent for special tanks and defensive pivots
- **Special Walls**: Transforms moderate special defense into excellent special bulk
- **Synergy with HP**: Most effective on Pokemon with high HP stats
- **Team Role**: Ideal for checking special attackers and special-based weather teams

### Example Damage Calculations
```
Base Damage: 100
With Prism Scales: 100 x 0.7 = 70 damage
Effective Bulk Increase: 100/70 = ~43% more special bulk
```

If combined with a 2x type resistance:
```
Base Damage: 100
Type Resistance: 100 x 0.5 = 50
With Prism Scales: 50 x 0.7 = 35 damage
Total Reduction: 65% damage reduction
```

### Common Users
Based on the codebase analysis, Prism Scales appears as both a regular ability and innate ability on various Pokemon, including:
- Several Dragon-type Pokemon (often Water/Dragon combinations)
- Defensive wall Pokemon with high special defense
- Legendary and pseudo-legendary Pokemon as an innate ability

### Competitive Usage Notes
- **Meta Positioning**: Strong in special attack-heavy metagames
- **Team Building**: Pairs well with physical walls to create balanced defensive cores
- **Prediction**: Most effective when switched into predicted special attacks
- **Longevity**: Increases staying power significantly against special attackers

### Counters
- **Mold Breaker**: Completely negates the ability
- **Physical Attacks**: No protection against physical moves
- **Mixed Attackers**: Can be overwhelmed by opponents using both attack stats
- **Ability-changing Moves**: Gastro Acid, Worry Seed, etc. can remove the ability

### Synergies
- **Assault Vest**: Stacks with AV's special defense boost
- **Recovery Moves**: More effective healing due to reduced damage taken
- **Leftovers/Rocky Helmet**: Passive damage becomes more significant relative to damage taken
- **Marvel Scale**: If status inflicted, provides additional defense boost

### Version History
- Added as ability ID 272 in Elite Redux
- Functions as both regular and innate ability
- Breakable by standard ability-breaking effects
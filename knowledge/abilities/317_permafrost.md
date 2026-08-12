---
id: 317
name: Permafrost
status: reviewed
character_count: 106
---

# Permafrost - Ability ID 317

## In-Game Description
"Reduces super-effective damage by 35%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

### Technical Implementation

### Core Mechanics
- **Trigger Condition**: `typeEffectivenessModifier >= UQ_4_12(2.0)` (2.0x type effectiveness or higher)
- **Damage Multiplier**: `MUL(.65)` (65% of original damage, 35% reduction)
- **Callback Type**: `onDefensiveMultiplier`
- **Breakable**: `TRUE` (can be suppressed by abilities like Mold Breaker, Teravolt, Turboblaze)

### Code Implementation
```c
constexpr Ability Permafrost = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (typeEffectivenessModifier >= UQ_4_12(2.0)) MUL(.65);
        },
    .breakable = TRUE,
};
```

### Damage Calculation Order
1. Base damage calculation
2. Type effectiveness applied (2.0x, 4.0x, etc.)
3. **Permafrost reduction applied (0.65x multiplier)**
4. Other defensive modifiers (items, abilities, etc.)
5. Final damage dealt

## Strategic Analysis

### Strengths
- **Consistent Protection**: Reduces all super-effective damage by 35%
- **Type Coverage**: Works against any type matchup that deals super-effective damage
- **Passive Activation**: No setup or conditions required beyond taking super-effective hits
- **Stacking Potential**: Can combine with other defensive abilities and items

### Weaknesses
- **No Neutral/Resisted Protection**: Only affects super-effective moves
- **Mold Breaker Vulnerability**: Can be completely bypassed by abilities that ignore other abilities
- **Status Move Immunity**: Doesn't protect against status moves regardless of type effectiveness

### Competitive Viability
- **Tier**: Mid-tier defensive ability
- **Best Users**: Pokemon with multiple type weaknesses or frail defensive stats
- **Synergy**: Pairs well with type-resist berries, Assault Vest, or other defensive items

## Related Abilities

### Similar Abilities
- **Primal Armor** (Ability #318): Reduces super-effective damage by 50% instead of 35%
- **Filter/Solid Rock**: Also reduce super-effective damage by 25% in standard games
- **Permafrost Clone** (Ability #582): Identical implementation using the same callback

### Ability Comparisons
| Ability | Damage Reduction | Breakable | Additional Effects |
|---------|------------------|-----------|-------------------|
| Permafrost | 35% | Yes | None |
| Primal Armor | 50% | Yes | None |
| Filter | 25% | Yes | None |
| Wonder Guard | 100% | Yes | Only allows super-effective damage |

## Pokemon Distribution

### Primary Users (Notable Examples)
- Ice-type Pokemon and their evolutionary lines
- Legendary/Mythical Ice-types
- Fossil Pokemon revived forms
- Select defensive-oriented Pokemon

### Common Combinations
- **With Snow Warning**: Ice-types that set up hail/snow
- **With Ice Body**: Gradual HP recovery in hail
- **With Thick Fat**: Additional resistance to Fire/Ice moves
- **With Sturdy**: Protection from OHKO moves combined with super-effective reduction

## Battle Applications

### Defensive Strategies
1. **Tank Setup**: Use the damage reduction to survive super-effective hits while setting up
2. **Pivot Play**: Stay in against super-effective moves to maintain momentum
3. **Endurance**: Extend longevity in matches with common super-effective coverage

### Counterplay
1. **Mold Breaker Users**: Completely bypasses the ability
2. **Neutral Damage**: Focus on moves that don't trigger the reduction
3. **Status Moves**: Use status effects that ignore the damage reduction
4. **Multi-hit Moves**: Each hit is reduced but total damage can still be significant

## Notes
- The ability uses the same threshold as Wonder Guard (UQ_4_12(2.0)) to determine super-effectiveness
- Damage reduction is multiplicative, not additive, with other defensive modifiers
- The ability is part of Elite Redux's expanded defensive ability pool for balancing offensive power creep
- Thematically appropriate for Ice-types and cold-weather Pokemon
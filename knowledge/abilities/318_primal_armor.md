---
id: 318
name: Primal Armor
status: reviewed
character_count: 106
---

# Primal Armor - Ability ID 318

## In-Game Description
"Takes 50% less damage from Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 50%. Multiplicative with other sources of damage reduction.


## Detailed Mechanical Explanation

### Basic Information
- **Name**: Primal Armor
- **ID**: 318 (ABILITY_PRIMAL_ARMOR)
- **Short Description**: Takes 50% less damage from Super-effective moves.

### Technical Implementation

### Code Structure
```cpp
constexpr Ability PrimalArmor = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (typeEffectivenessModifier >= UQ_4_12(2.0)) MUL(.5);
        },
    .breakable = TRUE,
};
```

### Trigger Condition
- **Activation**: When `typeEffectivenessModifier >= UQ_4_12(2.0)`
- **Fixed-Point Math**: `UQ_4_12(2.0)` represents 2.0x type effectiveness using the game's fixed-point arithmetic system
- **Threshold**: Only activates against moves that deal 2x or greater type effectiveness damage

### Damage Calculation
- **Multiplier**: `MUL(.5)` = 50% damage reduction
- **Effect**: Super-effective moves deal half damage (2x becomes 1x, 4x becomes 2x)
- **Timing**: Applied during the defensive multiplier calculation phase

### Properties
- **Breakable**: `TRUE` - Can be suppressed by Mold Breaker and similar abilities
- **Stackable**: Yes - Can stack with other damage reduction effects
- **Priority**: Applied during the defensive multiplier calculation phase

## Game Mechanics

### Activation Scenarios
1. **2x Super-Effective**: Damage reduced from 2x to 1x (normal effectiveness)
2. **4x Super-Effective**: Damage reduced from 4x to 2x (still super-effective but manageable)
3. **Higher Multipliers**: Any move with effectiveness ≥ 2.0x gets the reduction

### Interaction with Other Effects
- **Berries**: Stacks with type-resist berries (e.g., Wacan Berry for Electric moves)
- **Items**: Stacks with damage-reducing items
- **Weather**: Works independently of weather effects
- **Critical Hits**: Reduction applies to critical hit damage as well
- **Other Abilities**: Can stack with partner abilities like Friend Guard

### Similar Abilities Comparison
| Ability | Reduction | Threshold | Breakable |
|---------|-----------|-----------|-----------|
| Primal Armor | 50% | ≥2.0x | Yes |
| Filter | 35% | ≥2.0x | Yes |
| Solid Rock | 35% | ≥2.0x | Yes |
| Prism Armor | 35% | ≥2.0x | No |

## Strategic Usage

### Pokemon with Primal Armor
Based on trainer data analysis, Primal Armor appears as an innate ability on:
- **Mega Aggron** (as innate ability)
- **Bastiodon** (as innate ability)
- **Mega Steelix** (as main or innate ability)
- **Regigigas** (as selectable ability)
- **Primal Kyogre** (as innate ability)
- **Dialga** (as innate ability)
- **Zygarde** (as innate ability)
- **Palkia** (as innate ability, uncommon)

### Defensive Synergy
- **Steel Types**: Particularly effective on Steel-types that resist many moves already
- **Bulky Pokemon**: Maximizes survivability of naturally tanky Pokemon
- **Multi-Type Weakness**: Essential for Pokemon with multiple weaknesses (like Rock/Steel types)

### Counter-Strategies
- **Mold Breaker**: Completely bypasses Primal Armor
- **Neutral Moves**: Use moves that don't trigger the ability
- **Status Moves**: Primal Armor doesn't affect status moves or indirect damage
- **Multi-Hit Moves**: Each hit gets reduced, but multiple hits can still accumulate damage

## Usage Context
Primal Armor is typically found on legendary/pseudo-legendary Pokemon and defensive walls as an innate ability in Elite Redux's 4-ability system. It's especially common on Steel-type walls and Primal/Mega evolved forms, providing them with exceptional bulk against their few remaining weaknesses.

## Development Notes
- Part of Elite Redux's enhanced defensive ability suite
- Provides stronger damage reduction than Filter/Solid Rock (50% vs 35%)
- Balanced by being breakable unlike Prism Armor
- Commonly paired with other defensive abilities in the innate ability system
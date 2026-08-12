---
id: 308
name: Tectonize
status: reviewed
character_count: 135
---

# Tectonize - Ability ID 308

## In-Game Description
"Normal-type moves become Ground and Ground gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Tectonize converts all Normal-type moves into Ground-type moves and grants STAB for Ground-type moves, regardless of the user's typing.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Tectonize is an ATE (Ate-type) ability that functions similar to abilities like Pixilate, Refrigerate, and Aerilate. It provides two key effects:

1. **Type Conversion**: All Normal-type moves used by the Pokemon become Ground-type moves
2. **STAB Provision**: The Pokemon gains STAB (Same-Type Attack Bonus) for Ground-type moves, regardless of its actual typing

### Technical Implementation
```cpp
constexpr Ability Tectonize = {
    ATE_ABILITY(TYPE_GROUND),
};

#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Activation Conditions
- The ability only affects Normal-type moves
- The move must be used by the Pokemon with Tectonize
- Conversion happens before damage calculation and type effectiveness checks

### Damage Calculation
**Important Note**: Unlike some other games, Tectonize in Elite Redux does NOT provide an inherent damage boost. The ability only converts type and provides STAB. Some other ATE abilities like Normalize, Crystallize, and Superconductor have explicit 1.1x multipliers, but standard ATE abilities like Tectonize do not.

### Affected Moves (Common Examples)
- **Tackle** to Ground-type physical move
- **Quick Attack** to Ground-type priority move  
- **Hyper Beam** to Ground-type special move with recharge
- **Body Slam** to Ground-type move with paralysis chance
- **Double-Edge** to Ground-type move with recoil
- **Boomburst** to Ground-type sound move
- **Return/Frustration** to Ground-type moves based on friendship
- **Explosion/Self-Destruct** to Ground-type suicide moves

### Type Effectiveness Changes
When Normal moves become Ground-type via Tectonize:
- **Super effective against**: Electric, Fire, Poison, Rock, Steel (2x damage)
- **Not very effective against**: Bug, Grass (0.5x damage)  
- **No effect against**: Flying (0x damage)
- **Normal effectiveness**: All other types (1x damage)

### STAB Calculation
- If the Pokemon has Ground as a natural type: 1.5x damage multiplier
- If the Pokemon does not have Ground as a natural type: Still gets 1.5x via Tectonize's STAB provision
- This means even Normal/Flying Pokemon would get STAB on converted Ground moves

### Strategic Implications

**Advantages**:
- Converts typically neutral Normal moves into super-effective hits against common types
- Provides STAB on Ground moves for non-Ground Pokemon
- Useful on physically oriented Pokemon with strong Normal movesets
- Can turn priority moves like Quick Attack into Ground-type priority

**Disadvantages**:
- Converted moves become completely ineffective against Flying types
- Loses neutral coverage that Normal typing typically provides
- No inherent damage boost like some other abilities
- Can be countered by Flying types or Levitate ability

### Common Users
Based on the codebase analysis, Tectonize can be found on:
- **Gliscor** (Ground/Flying) - Natural STAB stacking
- **Gabite** (Dragon/Ground) - Natural STAB stacking  
- **Bunnelby** (Normal/Ground) - Converts Normal STAB to Ground STAB
- **Diggersby** (Normal/Ground) - Converts Normal STAB to Ground STAB
- **Lycanroc** (Rock/Ground) - Gains Ground STAB on Normal moves

### Competitive Usage Notes
- Best used on Pokemon with strong physical Attack stats and good Normal movesets
- Particularly effective against teams heavy on Electric, Fire, Rock, or Steel types
- Should be paired with coverage moves to handle Flying types
- Works well with choice items due to consistent type conversion

### Counters
- **Flying-type Pokemon**: Completely immune to converted Ground moves
- **Levitate ability**: Grants immunity to the converted Ground moves  
- **Air Balloon**: Temporarily immune until popped
- **Telepathy**: In doubles, prevents damage from ally's converted moves

### Synergies
- **Choice Band/Specs**: Boosts the converted moves significantly
- **Life Orb**: Increases damage output of all converted moves
- **Ground Gem**: Would boost converted moves (if held item)
- **Earthquake**: Natural Ground STAB to complement converted moves
- **Rock/Steel moves**: Coverage for Flying types that counter Ground moves

### Version History
- Introduced in Elite Redux as ability ID 308
- Functions as a standard ATE ability without damage boost
- Part of the expanded ability system in Elite Redux
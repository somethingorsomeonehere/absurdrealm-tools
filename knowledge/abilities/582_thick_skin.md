---
id: 582
name: Thick Skin
status: reviewed
character_count: 106
---

# Thick Skin - Ability ID 582

## In-Game Description
"Takes 35% less damage from Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Damage Reduction**: Reduces damage by 35% from super-effective moves (moves with 2.0x type effectiveness or higher)
- **Activation Condition**: Only triggers when `typeEffectivenessModifier >= UQ_4_12(2.0)` (2.0x effectiveness or greater)
- **Multiplier Applied**: `MUL(.65)` - multiplies incoming damage by 0.65 (equivalent to 35% reduction)

### Technical Implementation
```cpp
constexpr Ability PermafrostClone = {
    .onDefensiveMultiplier = Permafrost.onDefensiveMultiplier,
    .breakable = TRUE,
};

// Referenced from Permafrost ability:
constexpr Ability Permafrost = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (typeEffectivenessModifier >= UQ_4_12(2.0)) MUL(.65);
        },
    .breakable = TRUE,
};
```

### Affected Moves
- **2x effectiveness moves**: Take 35% less damage (effective ~1.3x instead of 2x)
- **4x effectiveness moves**: Take 35% less damage (effective ~2.6x instead of 4x)
- **Normal/resisted moves**: No effect, damage remains unchanged

### Example Damage Calculations
- **Original 2x damage**: 200 HP to **With Thick Skin**: 130 HP (65% of original)
- **Original 4x damage**: 400 HP to **With Thick Skin**: 260 HP (65% of original)
- **Original 1x damage**: 100 HP to **With Thick Skin**: 100 HP (no change)

### Interactions with Other Abilities/Mechanics
- **Breakable**: Can be disabled by Mold Breaker, Teravolt, Turboblaze, etc.
- **Stacks multiplicatively** with other damage reduction effects
- **Type effectiveness items** (Expert Belt, etc.) are calculated before this ability
- **Does not affect** status moves or moves with fixed damage
- **Weather/terrain effects** are calculated separately

### Strategic Implications
- **Defensive utility**: Allows normally frail Pokemon to survive super-effective hits
- **Pivot potential**: Enables safe switching against predicted super-effective moves
- **Coverage punishment**: Discourages opponents from relying solely on type advantage
- **Bulk enhancement**: Effectively increases bulk against super-effective attacks only

### Common Users
Based on SpeciesList analysis, Thick Skin appears on:
- Several defensive-oriented Pokemon
- Mixed bulky attackers that benefit from super-effective damage reduction
- Pokemon with multiple other defensive abilities (as innate abilities)

### Competitive Usage Notes
- **Tier placement**: Found on various tier Pokemon including Tier 5 legendaries
- **Role compression**: Allows offensive Pokemon to check their usual counters
- **Prediction rewarded**: Most effective when predicting opponent's super-effective moves
- **Setup potential**: Provides opportunities to set up against predicted coverage moves

### Counters
- **Mold Breaker family**: Completely bypasses the ability
- **Neutral damage**: Focus on neutral effectiveness moves to avoid the reduction
- **Status moves**: Thick Skin doesn't affect status conditions or entry hazards
- **Multi-hit moves**: Each hit gets reduced, but cumulative damage can still overwhelm
- **Chip damage**: Residual damage from hazards, weather, etc. is unaffected

### Synergies
- **Assault Vest**: Combines well for both physical and special bulk
- **Leftovers/Recovery**: Maximizes the defensive value gained from damage reduction
- **Intimidate**: Further reduces physical super-effective damage
- **Screen support**: Stacks multiplicatively with Light Screen/Reflect
- **Resist Berries**: Can be used alongside type-resist berries for massive damage reduction

### Version History
- **Elite Redux**: Implemented as ABILITY_PERMAFROST_CLONE (ID 582)
- **Internal name**: Uses the same mechanics as the original Permafrost ability
- **Display name**: Shows as "Thick Skin" to players
- **Classification**: Defensive ability, breakable by standard ability-bypassing effects
---
id: 208
name: Schooling
status: reviewed
character_count: 247
---

# Schooling - Ability ID 208

## In-Game Description
"If Lv. 20 or more: changes into School form until 1/4 HP or less."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When at level 20 or above, transforms into School Form. Reverts to Solo Form when HP drops to 25% or less. This form change triggers automatically upon entry and at end of each turn. Cannot be overridden, suppressed, swapped, or copied in any way.

## Detailed Mechanical Explanation
*For Discord/reference use*

Schooling is a unique form-changing ability that allows certain Pokemon to transform between two distinct forms based on level requirements and HP thresholds. 

### Core Mechanics
- **Level Requirement**: Must be level 20 or above to activate
- **HP Threshold**: Form changes when HP drops to 25% (1/4) or less of maximum HP
- **Transformation Direction**: 
  - Solo Form to School Form when HP > 25% and level ≥ 20
  - School Form to Solo Form when HP <= 25%

### Activation Conditions
```cpp
// From abilities.cc - Schooling ability definition
constexpr Ability Schooling = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(gBattleMons[battler].level >= 20)
        return TryTransformAttacker(ability, battler, ABILITY_BS_PUSH_CURSOR_AND_CALLBACK);
    },
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK(gBattleMons[battler].level >= 20)
        return TryTransformAttacker(ability, battler, ABILITY_BS_PUSH_CURSOR_AND_CALLBACK);
    },
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

### Technical Implementation
The ability uses the HP-based transformation system:
```cpp
// From battle_util.c - HP transformation data
{ABILITY_SCHOOLING, SPECIES_WISHIWASHI_SCHOOL, SPECIES_WISHIWASHI, 4},
{ABILITY_SCHOOLING, SPECIES_UNOWN_REVELATION, SPECIES_UNOWN, 4},
```

The `4` indicates HP is divided by 4 (25% threshold).

### Transformation Logic
```cpp
// High HP Form to Low HP Form (School to Solo)
if (species == gHpTransformations[i].highHpSpecies && 
    gBattleMons[battler].hp <= gBattleMons[battler].maxHP / gHpTransformations[i].hpFraction) {
    // Transform to Solo form
}

// Low HP Form to High HP Form (Solo to School)  
if (species == gHpTransformations[i].lowHpSpecies && 
    gBattleMons[battler].hp > gBattleMons[battler].maxHP / gHpTransformations[i].hpFraction) {
    // Transform to School form
}
```

### Numerical Values/Percentages
- **HP Threshold**: Exactly 25% (1/4) of maximum HP
- **Level Requirement**: Minimum level 20
- **Priority**: Checks occur on entry and at end of each turn

### Complete List of Affected Pokemon
In Elite Redux, Schooling affects:
1. **Wishiwashi** (Solo Form ↔ School Form)
2. **Unown** (Regular ↔ Revelation Form)

### Stat Changes
The form change typically provides significant stat improvements:
- **Wishiwashi School Form**: Dramatically increased HP, Attack, Defense, and Special Defense
- **Unown Revelation Form**: Enhanced combat capabilities compared to base Unown

### Interactions with Other Abilities/Mechanics
- **Unsuppressable**: Cannot be suppressed by abilities like Gastro Acid
- **Transform Block**: Cannot activate if Pokemon is already transformed by moves like Transform
- **Status Check**: Blocked by STATUS2_TRANSFORMED flag
- **Alive Check**: Pokemon must be alive (HP > 0) to transform

### Strategic Implications
- **Offensive Potential**: School Form provides significantly better offensive and defensive stats
- **HP Management**: Players must carefully manage HP to maintain preferred form
- **Level Timing**: Evolution timing becomes crucial - transforming at level 20+ provides immediate power spike
- **Predictability**: Opponents can predict form changes based on visible HP

### Example Battle Scenarios
1. **Entry Transform**: Level 20+ Wishiwashi enters at full HP to automatically becomes School Form
2. **Damage Threshold**: School Form takes damage reducing HP to 24% to reverts to Solo Form
3. **Healing Recovery**: Solo Form heals above 25% HP to transforms back to School Form at turn end
4. **Low Level Block**: Level 19 Wishiwashi cannot transform regardless of HP

### Common Users
- **Wishiwashi**: Primary user, transforms from weak Solo to powerful School form
- **Unown**: In Elite Redux, gains Revelation form with enhanced battle capabilities

### Competitive Usage Notes
- **Tank Role**: School Form often serves as a bulky pivot or tank
- **Setup Sweeper**: High stats in School Form enable setup opportunities  
- **HP Threshold Play**: Strategic damage calculation around 25% threshold
- **Level Requirement**: Must reach level 20 before ability becomes relevant

### Counters
- **Consistent Damage**: Keeping HP below 25% prevents School Form
- **Status Effects**: Sleep, paralysis can limit effectiveness regardless of form
- **Ability Suppression**: While unsuppressable, form changes can be prediction-based
- **Priority Moves**: Can revenge kill before form change occurs

### Synergies
- **Leftovers/Recovery**: Help maintain HP above threshold
- **Substitute**: Protect while in powerful School Form
- **Entry Hazards**: Damage on switch-in can affect form immediately
- **Healing Support**: Teammate healing enables form maintenance

### Version History
- Introduced in Generation VII
- Elite Redux implementation adds Unown Revelation form
- Maintains original 25% HP threshold and level 20 requirement
- Added unsuppressable flag for competitive balance
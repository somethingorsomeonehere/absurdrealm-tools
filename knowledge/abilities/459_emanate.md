---
id: 459
name: Emanate
status: reviewed
character_count: 112
---

# Emanate - Ability ID 459

## In-Game Description
"Normal-type moves become Psychic and Psychic gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*


Converts all Normal-type moves to Psychic-type and grants STAB for Psychic moves, regardless of the user's type. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Emanate is an "-ate" family ability that transforms Normal-type moves into Psychic-type moves while providing offensive benefits. It belongs to the same family as Pixilate, Aerilate, and other type-converting abilities.

### Primary Effects
1. **Type Conversion**: All Normal-type moves become Psychic-type
2. **Power Boost**: Converted moves receive a 1.2x power multiplier
3. **STAB Bonus**: Grants STAB (Same Type Attack Bonus) on all Psychic-type moves
4. **Move Pool Expansion**: Effectively gives access to powerful Psychic variants of Normal moves

### Activation Conditions
- **Move Type**: Only affects Normal-type moves for conversion
- **STAB Application**: Applies to all Psychic-type moves (converted and natural)
- **Power Boost**: Only applies to converted Normal moves, not natural Psychic moves
- **Timing**: Conversion happens before damage calculation

### Technical Implementation
```c
// Emanate uses the ATE_ABILITY macro with TYPE_PSYCHIC
constexpr Ability Emanate = {
    ATE_ABILITY(TYPE_PSYCHIC),
};

// This expands to:
.onMoveType = +[](ON_MOVE_TYPE) -> int {
    CHECK(moveType == TYPE_NORMAL)    // Only converts Normal moves
    *ateBoost = TRUE;                 // Sets power boost flag
    return TYPE_PSYCHIC + 1;          // Returns new type
},
.onStab = +[](ON_STAB) -> int { 
    return moveType == TYPE_PSYCHIC;  // STAB for Psychic moves
}
```

### Damage Calculation
- **Converted Normal moves**: Base power x 1.2 (ATE boost) x 1.5 (STAB) = 1.8x total
- **Natural Psychic moves**: Base power x 1.5 (STAB only)
- **Other move types**: No modification

### Move Interactions
**Powerful Normal moves that become Psychic:**
- **Hyper Beam** to Psychic Hyper Beam (150 to 180 BP + STAB)
- **Double-Edge** to Psychic Double-Edge (120 to 144 BP + STAB) 
- **Return/Frustration** to Psychic Return/Frustration (variable power + boost)
- **Boomburst** to Psychic Boomburst (140 to 168 BP + STAB)
- **Extreme Speed** to Psychic Extreme Speed (80 to 96 BP + STAB + priority)

**Natural Psychic moves enhanced:**
- All existing Psychic moves gain STAB bonus
- No power boost, just the 1.5x STAB multiplier

### Type Effectiveness Changes
After conversion, moves hit based on Psychic-type effectiveness:
- **Super Effective**: Fighting, Poison (2x damage)
- **Not Very Effective**: Steel, Psychic (0.5x damage)
- **No Effect**: Dark-type Pokemon (0x damage)

### Important Interactions
- **Wonder Guard**: Converted moves can hit Wonder Guard if Psychic is super effective
- **Abilities**: Affects interactions with Psychic-immune abilities
- **Items**: Benefits from Psychic-boosting items (Twisted Spoon, Psychium Z)
- **Terrain**: Affected by Psychic Terrain when used on grounded Pokemon
- **Weather**: No direct weather interactions

### Strategic Applications
**Offensive Versatility:**
- Transforms weak Normal coverage into powerful Psychic attacks
- Provides STAB bonus to existing Psychic movepool
- Excellent for mixed attackers with both Normal and Psychic moves

**Coverage Considerations:**
- Loses Normal's neutral coverage against most types
- Gains super effective coverage against Fighting and Poison
- Becomes walled by Dark-types completely

**Team Synergy:**
- Works well with Psychic Terrain support
- Benefits from Choice items and life orb
- Pairs with Pokemon that can handle Dark-types

### Counters and Limitations
**Hard Counters:**
- Dark-type Pokemon (complete immunity to converted moves)
- Pokemon with Psychic-type resistances (Steel, Psychic)

**Ability Counters:**
- **Mold Breaker**: Ignores the ability entirely
- **Wonder Guard**: Only affected if Psychic is super effective
- **Magic Guard**: Prevents recoil damage from converted moves

**Strategic Counters:**
- Dark-type teammates or coverage
- Steel-type walls with recovery
- Priority moves that outspeed converted Extreme Speed

### Optimal Users
**Ideal Pokemon characteristics:**
- High Attack or Special Attack stats
- Access to powerful Normal moves
- Natural Psychic STAB moves
- Good speed or bulk to utilize the power boost

**Common Movesets:**
- Physical: Double-Edge, Extreme Speed, Return, Psychic Fangs
- Special: Hyper Beam, Boomburst, Psychic, Psyshock
- Mixed: Combination of both for maximum coverage

### Competitive Viability
**Strengths:**
- Significantly boosts power of common Normal moves
- Provides STAB to both converted and natural Psychic moves
- Excellent for wallbreaking with boosted moves

**Weaknesses:**
- Complete shutdown by Dark-types
- Reduces neutral coverage compared to Normal typing
- Predictable type conversions

### Version History
- Elite Redux custom ability (ID 459)
- Part of the "-ate" ability family
- Follows standard ATE_ABILITY implementation pattern
- Balanced around 1.2x power boost for converted moves

### Synergy with Other Abilities
- Can be paired with other abilities in Elite Redux's multi-ability system
- Works well with offensive stat boosters
- Combines with priority-granting abilities for devastating Extreme Speed
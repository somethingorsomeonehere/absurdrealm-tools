---
id: 413
name: Draconize
status: reviewed
character_count: 125
---

# Draconize - Ability ID 413

## In-Game Description
"Normal-type moves become Dragon and Dragon gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Dragon-type moves and grants STAB for Dragon-type moves, regardless of the user's typing.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Draconize is an offensive ability that transforms the type of Normal-type moves and provides enhanced STAB coverage. It belongs to the "Ate" family of abilities, which convert Normal-type moves to different types while providing bonus damage.

### Activation Conditions
- **Move type conversion**: All Normal-type moves become Dragon-type
- **STAB application**: Grants STAB bonus for all Dragon-type moves (including converted ones)
- **Power boost**: Converted moves receive a 20% power increase (ateBoost mechanism)
- **Always active**: No conditional requirements, works on all Normal-type moves

### Technical Implementation
```cpp
// Draconize uses the ATE_ABILITY macro with Dragon type
constexpr Ability Draconize = {
    ATE_ABILITY(TYPE_DRAGON),
};

// ATE_ABILITY macro definition
#define ATE_ABILITY(type)
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(moveType == TYPE_NORMAL)  // Only affects Normal moves
        *ateBoost = TRUE;               // 20% power boost
        return type + 1;                // Convert to Dragon type
    },
    .onStab = +[](ON_STAB) -> int { return moveType == type; }  // STAB for Dragon moves
```

### Move Conversions
**Common Normal moves that become Dragon:**
- **Hyper Beam** to Dragon Hyper Beam (150 to 180 power with boost)
- **Body Slam** to Dragon Body Slam (85 to 102 power with boost)
- **Quick Attack** to Dragon Quick Attack (40 to 48 power with boost)
- **Extreme Speed** to Dragon Extreme Speed (80 to 96 power with boost)
- **Boomburst** to Dragon Boomburst (140 to 168 power with boost)
- **Return/Frustration** to Dragon Return/Frustration (variable power + 20%)

### Damage Calculations
1. **Base conversion**: Normal move becomes Dragon-type
2. **Ate boost**: Move power multiplied by 1.2 (20% increase)
3. **STAB bonus**: 1.5x multiplier for Dragon-type moves on Dragon-type user
4. **Type effectiveness**: Dragon-type matchups apply

**Example calculation (Body Slam on Dragon-type user):**
- Base power: 85
- Ate boost: 85 x 1.2 = 102
- STAB: 102 x 1.5 = 153 effective power
- Final damage depends on stats and type effectiveness

### Strategic Implications
- **Mixed coverage**: Provides reliable Dragon STAB from Normal movepool
- **Priority moves**: Dragon Quick Attack/Extreme Speed for powerful priority
- **Status moves**: Normal status moves become Dragon-type (may affect interactions)
- **Versatile attacking**: Access to diverse Dragon-type movepool via Normal moves
- **STAB consistency**: All Dragon moves get STAB, not just converted ones

### Type Matchup Considerations
**Dragon-type is:**
- **Super effective against**: Dragon
- **Not very effective against**: Steel
- **Resisted by**: Steel
- **Weak to**: Ice, Dragon, Fairy

### Common Users
- Dragon-type Pokemon with diverse Normal movepools
- Mixed attackers wanting reliable Dragon coverage
- Pokemon with powerful Normal-type signature moves
- Speedy Dragon types utilizing priority Normal moves

### Competitive Usage Notes
- **Movepool expansion**: Effectively gives Dragon STAB to entire Normal movepool
- **Power boost**: 20% damage increase makes converted moves very threatening
- **Priority advantage**: Dragon priority moves are uncommon and valuable
- **Coverage typing**: Dragon hits most types neutrally for consistent damage
- **Fairy weakness**: Makes user more vulnerable to Fairy-type moves and users

### Synergies
- **Life Orb**: Stacks with ate boost for massive damage output
- **Choice items**: Powerful Dragon moves with item boost
- **Dragon Dance**: Set up sweeping with boosted Dragon moves
- **Tera Dragon**: In systems with Tera, can maximize Dragon STAB
- **Speed control**: Priority Dragon moves for speed tier advantage

### Counters
- **Fairy-types**: Immune to Dragon-type attacks completely
- **Steel-types**: Resist Dragon-type moves effectively
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable conversion
- **Haze/Clear Smog**: Remove setup if user tries to sweep
- **Priority moves**: Ice Shard can revenge kill weakened Dragon users

### Notable Interactions
- **Multi-hit moves**: Each hit gets the conversion and boost
- **Status moves**: Normal status moves become Dragon-type (may change effectiveness)
- **Hidden Power**: If typed as Normal, converts to Dragon
- **Z-moves/Max moves**: Converted moves use Dragon-type Z-crystals/Max effects
- **Ability changes**: If ability is changed mid-battle, conversion stops

### Version History
- Elite Redux exclusive ability (ID 413)
- Part of the expanded Ate ability family
- Designed to give Dragon-types access to diverse Normal movepool
- Provides unique Dragon-type priority and coverage options

### Comparison to Similar Abilities
- **Refrigerate**: Normal to Ice conversion (similar mechanism)
- **Pixilate**: Normal to Fairy conversion (similar power boost)
- **Aerilate**: Normal to Flying conversion (same ate boost)
- **Galvanize**: Normal to Electric conversion (consistent power boost)
- **Normalize**: Converts all moves to Normal (opposite effect)
---
id: 393
name: Spectralize
status: reviewed
character_count: 110
---

# Spectralize - Ability ID 393

## In-Game Description
"Normal-type moves become Ghost and Ghost gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves to Ghost-type and grants STAB for Ghost moves, regardless of the user's typing.

## Technical Implementation Details
*From `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` lines 3983-3985*

```cpp
constexpr Ability Spectralize = {
    ATE_ABILITY(TYPE_GHOST),
};
```

**ATE_ABILITY Macro Implementation (lines 285-291):**
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

**Core Mechanics:**
1. **Type Conversion**: All Normal-type attacking moves become Ghost-type (checked at `moveType == TYPE_NORMAL`)
2. **STAB Grant**: Pokemon gains STAB for ALL Ghost-type moves regardless of natural typing
3. **ateBoost Flag**: Sets the ateBoost flag for converted moves (used for tracking and potential interactions)

**Important Implementation Notes:**
- Uses the standard ATE_ABILITY macro with `TYPE_GHOST` parameter
- NO automatic power boost (unlike some custom -ate abilities in Elite Redux)
- Only affects attacking moves (status moves like Thunder Wave remain Normal-type)
- The ability is registered in the ability table at line 9237: `{ABILITY_SPECTRALIZE, Spectralize}`

## Strategic Analysis and Applications

### Offensive Applications
**Move Transformation Benefits:**
- **Body Slam** to Ghost-type STAB move with paralysis chance
- **Hyper Voice** to Powerful Ghost-type special attack that hits through Substitute
- **Return/Frustration** to Ghost-type STAB moves with variable power
- **Quick Attack** to Ghost-type priority move
- **Explosion** to Ghost-type suicide move (though still hits Ghost types due to explosive mechanics)

**Type Coverage Advantages:**
- Super-effective against Fighting and Psychic types (2x damage)
- Neutral against most types that resist Normal (Rock, Steel)
- Can hit Normal types neutrally instead of being resisted

### Defensive Considerations
**Weaknesses Created:**
- Converted moves now resisted by Dark types (0.5x damage)
- Steel types become immune to converted moves (0x damage)
- Lose the benefit of Fighting types taking normal damage from Normal moves

### Competitive Tier Analysis: HIGH

**Tier Justification:**
1. **Meta Relevance**: Ghost is an excellent offensive type in competitive play
2. **Coverage Value**: Provides super-effective hits against common Fighting and Psychic types
3. **STAB Access**: Grants Ghost STAB to any Pokemon, significantly boosting power output
4. **Move Pool Synergy**: Many Pokemon have extensive Normal-type movepools that benefit greatly

**Optimal Usage Scenarios:**
- **Mixed Attackers**: Pokemon with both physical and special Normal moves
- **Coverage Seekers**: Non-Ghost types needing Ghost-type attacks
- **STAB Maximizers**: Pokemon wanting to boost their Normal-type moves with STAB

## Related Abilities and Comparisons

### Other ATE_ABILITY Implementations
**Standard -ate Abilities (Type Conversion + STAB only):**
- **Refrigerate** (ID 174): Normal to Ice
- **Pixilate** (ID 182): Normal to Fairy  
- **Aerilate** (ID 184): Normal to Flying
- **Galvanize** (ID 206): Normal to Electric

**Enhanced -ate Abilities (with custom power boosts):**
- **Steelworker** (ID 200): Steel-type moves + Dark/Ghost resistance
- **Normalize** (ID 96): All moves to Normal with 1.1x power boost for converted moves

### Key Differences from Main Series
**Elite Redux Implementation:**
- No automatic 1.2x power boost (unlike main series -ate abilities)
- Only provides type conversion and STAB access
- Makes the ability more balanced but still highly valuable

**Power Calculation:**
- Converted move: Base Power x 1.5 (STAB only)
- Main series equivalent: Base Power x 1.2 x 1.5 = 1.8x total

### Synergy Abilities
**Abilities that complement Spectralize:**
- **Technician**: Boosts weak converted moves like Quick Attack
- **Adaptability**: Would double STAB bonus if present (though not applicable in 4-ability system)
- **Skill Link**: Enhances multi-hit Normal moves that get converted

## Battle Interactions and Edge Cases

### Status Move Handling
- **Thunder Wave, Sleep Powder, etc.**: Remain Normal-type (not converted)
- **Only attacking moves are affected by type conversion**

### Special Interactions
**SpectralShroud Synergy (ID 386):**
- SpectralShroud checks for `gBattleStruct->ateBoost[battler]` and `moveType == TYPE_GHOST`
- 30% chance to badly poison target when using converted Ghost moves
- Creates powerful synergy between the two Ghost-themed abilities

### Elite Redux 4-Ability System Integration
**Recommended Slot Usage:**
- **Changeable Slot**: When flexibility is needed for different matchups
- **Innate Slot**: When consistent Ghost coverage is core to the Pokemon's strategy

**Multi-Ability Combinations:**
- Can stack with other offensive abilities for devastating combinations
- Works well with stat-boosting abilities to maximize converted move power

## Notable Pokemon Beneficiaries
*Based on usage patterns in TrainerList.textproto and SpeciesList.textproto*

**High-Value Users:**
- Pokemon with extensive Normal-type movepools
- Mixed attackers with both physical and special Normal moves
- Pokemon needing Ghost coverage for competitive viability
- Pokemon that can take advantage of Fighting/Psychic matchups

This ability represents one of the most valuable type-conversion abilities in Elite Redux, offering immediate offensive improvement and meta-relevant coverage to any Pokemon that can utilize it effectively.
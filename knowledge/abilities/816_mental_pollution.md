---
id: 816
name: Mental Pollution (N)
status: reviewed
character_count: 128
---

# Mental Pollution (N) - Ability ID 816

## In-Game Description
"Nulls abilities when confused except others with this ability."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Nullifies all opposing Pokemon's abilities and innates while they are confused. Pokemon with Mental Pollution remain unaffected. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Ability Nullification**: When a Pokemon is confused, all of its abilities become inactive if any opponent has Mental Pollution
- **Exception Rule**: Pokemon with Mental Pollution are immune to this effect from other Mental Pollution users
- **Status Requirement**: Only affects confused Pokemon - those without confusion status are unaffected
- **Field-Wide Effect**: Mental Pollution affects all confused opponents, not just specific targets

### Activation Conditions
- At least one Pokemon with Mental Pollution must be active on the field
- Target Pokemon must have the confusion status (STATUS2_CONFUSION)
- The affected Pokemon cannot have Mental Pollution itself

### Technical Implementation
**Current Status**: Partially implemented
- Defined in `src/abilities.cc` with `.breakable = TRUE`
- Missing core logic in ability checking functions
- Would require modification to `IsSuppressed()` or `GetBattlerAbility()` functions

```c
// Proposed implementation in IsSuppressed function:
if (gBattleMons[battler].status2 & STATUS2_CONFUSION) {
    // Check if any opponent has Mental Pollution
    for (int i = 0; i < gBattlersCount; i++) {
        if (GetBattlerSide(i) != GetBattlerSide(battler) && 
            BattlerHasAbility(i, ABILITY_MENTAL_POLLUTION, FALSE)) {
            // Don't suppress if this battler also has Mental Pollution
            if (!HasAbilityIgnoringSuppression(battler, ABILITY_MENTAL_POLLUTION)) {
                return TRUE; // Suppress the ability
            }
        }
    }
}
```

### Affected Abilities
- **All abilities** are nullified when confused (except Mental Pollution itself)
- Includes passive abilities, entry abilities, and reactive abilities
- Both changeable and innate abilities are affected

### Interactions with Other Mechanics
- **Mold Breaker**: Mental Pollution is breakable, so Mold Breaker can ignore it
- **Gastro Acid**: If Mental Pollution is suppressed by Gastro Acid, it won't nullify abilities
- **Neutralizing Gas**: Takes precedence over Mental Pollution
- **Ability Shield**: Would protect from Mental Pollution's ability suppression
- **Confusion Immunity**: Pokemon immune to confusion are unaffected

### Strategic Implications
- **Synergy with Confusion**: Requires reliable confusion-inducing moves or abilities
- **Team Support**: Benefits teammates by shutting down opposing abilities
- **Setup Requirement**: Must establish confusion before Mental Pollution takes effect
- **Risk/Reward**: Powerful disruption but requires status condition setup

### Common Users
*Note: This is a custom Elite Redux ability - no official Pokemon naturally have it*

### Competitive Usage Notes
- **Priority Target**: Pokemon with Mental Pollution become high-priority threats
- **Counter Strategy**: Focus on preventing confusion or removing Mental Pollution users
- **Team Building**: Pairs well with confusion-inducing moves and priority moves

### Counters
- **Confusion Prevention**: Lum Berry, Mental Herb, Misty Terrain
- **Ability Restoration**: Switching out removes confusion and restores abilities  
- **Mold Breaker**: Ignores Mental Pollution entirely
- **Fast KO**: Eliminate Mental Pollution users before they can capitalize

### Synergies
- **Confuse Ray**: Reliable confusion inducement
- **Swagger**: Confusion + Attack boost for opponents
- **Sweet Kiss**: Fast confusion move
- **Supersonic**: Early-game confusion option
- **Priority Moves**: Capitalize on disabled defensive abilities

### Version History
- **Elite Redux**: Custom ability introduction with ID 816
- **Implementation**: Currently has basic definition but lacks functional code
- **(N) Designation**: Indicates this is an innate ability slot in Elite Redux's 4-ability system
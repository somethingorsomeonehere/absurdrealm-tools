---
id: 369
name: Bad Company
status: reviewed
character_count: 16
---

# Bad Company - Ability ID 369

## In-Game Description
"Prevents defensive stat drops from own moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Not implemented. 

## Detailed Mechanical Explanation

### Overview
Bad Company is a defensive ability that prevents the user from suffering the defensive stat drops typically associated with certain powerful moves. This ability allows Pokemon to use high-power attacks without the usual defensive drawbacks.

## Technical Implementation

### Source Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: 3835-3837
- **Battle Script Reference**: `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_script_commands.c`, line 2738

### Code Implementation
```cpp
constexpr Ability BadCompany = {
    .randomizerBanned = TRUE,
};
```

### Battle Logic Implementation
The ability's effect is implemented in the battle script commands:
```c
case MOVE_EFFECT_DEF_SPDEF_DOWN:  // Close Combat
    if (!BATTLER_HAS_ABILITY(gBattlerAttacker, ABILITY_BAD_COMPANY)) {
        BattleScriptCall(BattleScript_DefSpDefDown);
    }
    break;
```

## Mechanics

### Primary Effect
- **Stat Protection**: Prevents Defense and Special Defense from dropping when using moves with `MOVE_EFFECT_DEF_SPDEF_DOWN` effect
- **Triggers On**: Moves that normally lower the user's Defense and Special Defense after dealing damage

### Affected Moves
Based on the codebase analysis, moves that use `EFFECT_CLOSE_COMBAT` are affected:

1. **Close Combat** (Fighting-type)
   - Power: 120, Accuracy: 100%, PP: 5
   - Normally lowers user's Defense and Sp. Defense by 1 stage each

2. **Dragon Ascent** (Flying-type)  
   - Power: 120, Accuracy: 100%, PP: 5
   - Normally lowers user's Defense and Sp. Defense by 1 stage each

3. **Strength** (Rock-type, modified version)
   - Uses the same CLOSE_COMBAT effect
   - Normally lowers user's defensive stats

### Battle Script Details
- **Effect ID**: `MOVE_EFFECT_DEF_SPDEF_DOWN` (enum value 57)
- **Script**: `BattleScript_DefSpDefDown` is bypassed when Bad Company is present
- **Implementation**: Direct check in `battle_script_commands.c`

## Strategic Analysis

### Advantages
1. **Offensive Consistency**: Allows repeated use of high-power moves without defensive penalties
2. **Defensive Integrity**: Maintains bulk while using powerful attacks
3. **Setup Potential**: Can use stat-boosting moves without fear of defensive drops
4. **Longevity**: Extends the Pokemon's staying power in battles

### Disadvantages
1. **Limited Scope**: Only affects specific moves with defensive stat drops
2. **Randomizer Banned**: Cannot appear in randomized games (`randomizerBanned = TRUE`)
3. **Situational**: Requires access to affected moves to be useful
4. **No Additional Benefits**: Provides no other combat advantages

### Competitive Applications

#### Ideal Users
- **Physical Attackers**: Pokemon that learn Close Combat or Dragon Ascent
- **Mixed Attackers**: Those who want to maintain defensive capabilities
- **Bulky Sweepers**: Pokemon that rely on both offense and defense

#### Team Synergy
- **Entry Hazard Weak Teams**: Maintains bulk against hazard damage
- **Stall Breakers**: Can repeatedly use powerful moves without losing bulk
- **Late-Game Cleaners**: Preserves defensive stats for endgame scenarios

#### Counters and Limitations
- **Status Moves**: Still vulnerable to stat-lowering status effects
- **Other Stat Drops**: Doesn't protect against Attack, Speed, or accuracy drops
- **Non-Affected Moves**: Other recoil or stat-dropping moves still function normally

## Related Abilities

### Similar Protective Abilities
- **Clear Body** (#29): Prevents all stat decreases from opponents
- **White Smoke** (#73): Prevents stat decreases from opponents (not self-inflicted)
- **Full Metal Body** (#230): Similar to Clear Body with additional effects

### Key Differences
- Bad Company only protects against specific self-inflicted Defense/Sp. Defense drops
- Does not protect against opponent-caused stat changes
- More limited in scope than general stat protection abilities

## Pokemon Distribution
*Note: Specific Pokemon with this ability would need to be checked in the protobuf species data*

## Trivia
- The ability name "Bad Company" likely references the cost-benefit nature of powerful moves
- This is one of the few abilities that specifically counteracts move-based stat penalties
- The implementation suggests it was designed specifically for Close Combat-style moves
- Banned from randomizer to prevent overpowered combinations with certain Pokemon

## Version History
- Added in Elite Redux as ability #369
- Currently marked as "Not implemented right now. Has no effect." in protobuf description, but actually functional in battle code
- Randomizer banned since implementation


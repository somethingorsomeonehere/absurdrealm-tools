---
id: 130
name: Cursed Body
status: reviewed
character_count: 160
---

# Cursed Body - Ability ID 130

## In-Game Description
"30% chance to disable moves if enemy makes contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user has a 30% chance to disable the attacker's move for 4 turns when hit by contact moves. The disabled move cannot be selected until the effect wears off. 

## Detailed Mechanical Explanation

### Activation Conditions
1. **Trigger**: When the Pokemon with Cursed Body is hit by a move
2. **Contact Requirement**: The attacking move must make contact
3. **Probability**: 30% chance to activate
4. **Target**: The attacker's move that just hit

### Effect Details
- **Disable Duration**: 4 turns
- **Move Disabled**: The move that triggered Cursed Body
- **PP Requirement**: The attacker must have PP remaining for the move
- **Protection Check**: Respects abilities that protect from restricting effects

### Technical Implementation
From `src/abilities.cc`:
```c
constexpr Ability CursedBody = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK_NOT(gVolatileStructs[attacker].disabledMove)
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(IsAbilityStatusProtected(attacker, CHECK_RESTRICTING))
        CHECK(gBattleMons[attacker].pp[gChosenMovePos])
        CHECK(Random() % 100 < 30)

        gVolatileStructs[attacker].disabledMove = gChosenMove;
        gVolatileStructs[attacker].disableTimer = 4;
        PREPARE_MOVE_BUFFER(gBattleTextBuff1, gChosenMove);
        BattleScriptCall(BattleScript_CursedBodyActivates);
        return TRUE;
    },
};
```

### Battle Message
When Cursed Body activates:
- "{Attacker}'s {Move} was disabled by {Defender}'s Cursed Body!"

## Strategic Analysis

### Strengths
1. **Defensive Disruption**: Can shut down key offensive moves
2. **Contact Punishment**: Deters physical attackers
3. **No Setup Required**: Works passively without any action needed
4. **Stacking Pressure**: Multiple chances throughout battle

### Weaknesses
1. **RNG Dependent**: Only 30% chance limits reliability
2. **Contact Only**: Doesn't work against special moves or non-contact moves
3. **Single Move**: Only disables one move, not the entire moveset
4. **Temporary**: 4 turns is relatively short

### Synergies
- **Bulky Pokemon**: More chances to trigger with higher survivability
- **Stall Teams**: Adds another layer of disruption
- **Substitute**: Forces contact moves to break Sub, increasing trigger chances
- **Protect/Detect**: Wastes disable turns while staying safe

## Competitive Usage

### Ideal Pokemon Characteristics
- High defensive stats to survive multiple hits
- Access to recovery moves
- Alternative defensive abilities to consider

### Common Strategies
1. **Lead Disruption**: Use on leads to potentially disable setup moves
2. **Physical Wall**: Combine with high Defense to punish physical attackers
3. **Pivot Mon**: Switch in on predicted contact moves for disable chance

### Counters
- Special attackers with non-contact moves
- Multi-hit moves (only first hit can be disabled)
- Pokemon with multiple coverage options
- Taunt to prevent recovery stalling

## Notable Pokemon
Pokemon that typically have access to Cursed Body often include Ghost-types and defensive Pokemon that benefit from move disruption.


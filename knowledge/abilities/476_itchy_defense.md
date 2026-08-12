---
id: 476
name: Itchy Defense
status: reviewed
character_count: 206
---

# Itchy Defense - Ability ID 476

## In-Game Description
"Causes infestation when hit by a contact move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Itchy Defense traps attackers with Infestation when the user is successfully hit by a contact move. The trapped opponent loses 1/8th of their maximum HP damage each turn for 4-5 turns and cannot switch out. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Itchy Defense is a defensive ability that automatically inflicts the Infestation trapping effect on any attacker that hits the user with a contact move. This creates a powerful deterrent against physical attackers by punishing direct contact.

### Activation Conditions
- **Contact requirement**: The attacking move must have the contact flag
- **Hit requirement**: The move must successfully connect (not miss, be blocked by Protect, etc.)
- **Damage requirement**: The ability checks ShouldApplyOnHitAffect, so it likely requires actual damage
- **Status check**: Will not trigger if the attacker is already trapped (STATUS2_WRAPPED)

### Trapping Effect Details
- **Damage**: 1/8 of the trapped Pokemon's maximum HP per turn
- **Duration**: 4-5 turns (randomly determined)
  - Base duration: 4-5 turns (Random() % 2 + 4)
  - With Grip Claw: 7 turns
- **Move association**: The trap is treated as if caused by the move Infestation
- **Switch prevention**: Trapped Pokemon cannot switch out or flee

### Technical Implementation
```c
// Itchy Defense triggers when hit by contact moves
constexpr Ability ItchyDefense = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))           // Must be valid hit
        CHECK(IsMoveMakingContact(move, attacker))        // Must be contact move
        CHECK_NOT(gBattleMons[attacker].status2 & STATUS2_WRAPPED) // Not already trapped
        
        // Apply trap status
        gBattleMons[attacker].status2 |= STATUS2_WRAPPED;
        
        // Set duration (4-5 turns, 7 with Grip Claw)
        if (GetBattlerHoldEffect(battler, TRUE) == HOLD_EFFECT_GRIP_CLAW)
            gVolatileStructs[attacker].wrapTurns = 7;
        else
            gVolatileStructs[attacker].wrapTurns = (Random() % 2) + 4;
        
        // Set as Infestation effect
        gBattleStruct->wrappedMove[attacker] = MOVE_INFESTATION;
        gBattleStruct->wrappedBy[attacker] = battler;
        
        BattleScriptCall(BattleScript_AttackerBecameInfested);
        return TRUE;
    },
};
```

### Important Interactions
- **Multiple hits**: Each contact hit can potentially trigger, but won't stack if already trapped
- **Substitute**: Contact moves that hit substitute will not trigger the ability
- **Magic Guard**: Trapped Pokemon with Magic Guard will not take the end-of-turn damage
- **Shed Shell**: Pokemon holding Shed Shell can still switch out despite being trapped
- **Ghost types**: In Gen 6+, Ghost types can still switch out despite being trapped
- **Rapid Spin**: Can remove the trap status from the trapped Pokemon

### Status Priority and Timing
- **Activation timing**: Triggers immediately after taking damage from contact move
- **End-of-turn damage**: Occurs during end-of-turn effects, dealing 1/8 max HP
- **Duration countdown**: Decreases by 1 each turn until reaching 0
- **Trap release**: Pokemon is freed when duration reaches 0

### Grip Claw Interaction
The ability specifically checks if the defending Pokemon (with Itchy Defense) has Grip Claw:
- **Extended duration**: Increases trap duration from 4-5 turns to 7 turns
- **Strategic use**: Makes the ability more threatening with proper item support

### AI Behavior
The AI recognizes this ability and will:
- **Contact avoidance**: Avoid using contact moves when possible
- **Trap evaluation**: Uses AI_SCORE_WRAP to evaluate the threat level
- **Move selection**: May prefer special/non-contact moves against this ability

### Contact Move Examples
**Triggers on**: Tackle, Scratch, Bite, Thunder Punch, Ice Punch, Close Combat, U-turn
**Doesn't trigger on**: Thunderbolt, Surf, Earthquake, Rock Slide, Stealth Rock

### Strategic Implications
- **Physical deterrent**: Heavily discourages physical attackers
- **Switch control**: Can trap key threats and prevent pivoting
- **Residual damage**: Provides consistent damage over multiple turns
- **Item synergy**: Works well with Grip Claw for extended trapping
- **Defensive utility**: Punishes common physical moves like U-turn and contact priority moves

### Common Users
- Defensive Pokemon that frequently take contact moves
- Pokemon with high defensive stats that can survive to activate the effect
- Stall-oriented team members looking to punish physical attackers

### Competitive Usage Notes
- **Anti-physical**: Excellent against physical sweepers and U-turn users
- **Trap damage**: Provides chip damage that can wear down bulky threats
- **Switch advantage**: Can force favorable matchups by preventing switches
- **Multi-hit weakness**: Abilities like Skill Link can potentially activate multiple times
- **Item dependency**: Grip Claw significantly improves effectiveness

### Counters
- **Special moves**: Use non-contact moves to avoid triggering
- **Long Reach**: Ability makes contact moves non-contact
- **Shed Shell**: Allows escape from trap status
- **Magic Guard**: Prevents end-of-turn damage from trap
- **Ghost typing**: Can switch out despite being trapped (Gen 6+)
- **Rapid Spin**: Can remove trap status
- **Substitute**: Blocks the ability from triggering

### Synergies
- **Grip Claw**: Extends trap duration from 4-5 turns to 7 turns
- **Binding Band**: Increases trap damage from 1/8 to 1/6 max HP
- **Bulky builds**: High defensive stats ensure survival to activate effect
- **Status moves**: Can use the trapped turns to set up or inflict status
- **Entry hazards**: Combine with hazards to maximize damage over time

### Version History
- New ability in Elite Redux
- Uses modern binding mechanics (1/8 HP damage per turn)
- Follows Gen 6+ trap escape rules for Ghost types
- AI properly evaluates the threat level

### Related Abilities
- **Rough Skin**: Also punishes contact moves but with immediate damage
- **Iron Barbs**: Similar to Rough Skin but Steel-type themed
- **Aftermath**: Punishes fainting from contact moves
- **Flame Body/Static/Poison Point**: Inflict status from contact moves
- **Gooey/Tangling Hair**: Reduce Speed from contact moves
---
id: 253
name: Perish Body
status: reviewed
character_count: 155
---

# Perish Body - Ability ID 253

## In-Game Description
"If hit, casts Perish Song."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by a contact move, Perish Body activates Perish Song on both the user and the attacker. Both Pokemon will faint in 3 turns unless they switch out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Perish Body is a defensive contact-triggered ability that applies Perish Song status to both the ability user and the attacking Pokemon when hit by a contact move.

### Activation Conditions
1. **Contact Move Requirement**: Only triggers when hit by moves that make contact (checked via `IsMoveMakingContact(move, attacker)`)
2. **Damage Requirement**: Must be hit by a move that would apply on-hit effects (`ShouldApplyOnHitAffect(battler)`)
3. **Attacker Alive**: The attacking Pokemon must still be alive after the move
4. **Attacker Not Already Affected**: Will not trigger if the attacker already has Perish Song status

### Effect Implementation
- **Defender (Ability User)**: Only gets Perish Song if not already affected
- **Attacker**: Always gets Perish Song (unless already affected, preventing activation)
- **Timer**: Both Pokemon get a 3-turn countdown timer
- **Battle Message**: Displays via `BattleScript_PerishBodyActivates`

### Strategic Applications
1. **Physical Deterrent**: Discourages physical attackers from making contact
2. **Forced Switching**: Creates pressure for both players to switch out
3. **Defensive Trading**: User can sacrifice itself to take down a valuable physical attacker
4. **Mind Games**: Opponent must decide whether the physical attack is worth the Perish Song trade

### Important Interactions
- **Multiple Activations**: Can trigger multiple times per battle against different attackers
- **Switch Immunity**: Switching out removes Perish Song status, negating the countdown
- **Status Immunity**: Does not bypass immunities to Perish Song itself
- **Contact Immunity**: Pokemon with Long Reach or other non-contact abilities are safe
- **Already Affected Check**: Prevents stacking or resetting timers on already affected Pokemon

### Competitive Viability
This ability transforms defensive Pokemon into potential revenge killers against physical attackers. It's particularly effective against setup sweepers who rely on contact moves, as they must choose between continuing their sweep and risking fainting in 3 turns, or switching out and losing their setup.

The symmetric nature (affecting both user and attacker) makes it a high-risk, high-reward ability that requires careful timing and strategic switching to maximize value while minimizing the user's own risk.
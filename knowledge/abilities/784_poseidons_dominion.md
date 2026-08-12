---
id: 784
name: Poseidons Dominion
status: reviewed
character_count: 201
---

# Poseidons Dominion - Ability ID 784

## In-Game Description
"Attacks with Whirlpool on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Whirlpool upon switching into battle, a 50 BP Water-type Special move that traps the opponent for 4-5 turns. The target takes 1/8 max HP damage each turn and cannot switch out until the trap ends.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Poseidons Dominion** is an on-entry ability that automatically uses the move Whirlpool when the Pokemon switches into battle. Here's how it works mechanically:

### Implementation Details
- **Trigger**: Activates immediately upon switching in (`onEntry` callback)
- **Move Used**: Whirlpool (50 Base Power, 90% Accuracy, Water-type)
- **Target Selection**: Automatically targets any alive opposing Pokemon
- **Move Power Override**: Uses default Whirlpool power (movePower parameter is 0)

### Whirlpool Move Properties
- **Type**: Water
- **Category**: Special
- **Base Power**: 50
- **Accuracy**: 90%
- **Effect**: EFFECT_TRAP - traps opponent for 2-5 turns
- **Target**: Selected opponent
- **Contact**: Yes
- **Description**: "Traps and hurts the foe in a whirlpool for 2 to 5 turns"

### Battle Mechanics
1. **Entry Activation**: When the Pokemon switches in, UseEntryMove() is called
2. **Target Detection**: The ability searches for alive opposing battlers
3. **Move Execution**: If a valid target exists and CanUseExtraMove() conditions are met, Whirlpool is queued as an extra attack
4. **Trap Effect**: If Whirlpool hits, the target becomes trapped for 2-5 turns, taking damage each turn and being unable to switch out

### Strategic Applications
- **Entry Hazard**: Provides immediate battlefield control upon switching in
- **Trap Utility**: Forces opponents to stay in battle, preventing strategic switches
- **Chip Damage**: Continuous damage over multiple turns
- **Water-type STAB**: Benefits from Same Type Attack Bonus if the user is Water-type
- **Field Control**: Similar to other trapping moves like Fire Spin or Sand Tomb

### Counters and Limitations
- **Accuracy**: 90% accuracy means it can miss
- **Ghost-types**: Can switch out despite being trapped
- **Rapid Spin**: Can remove the trap effect
- **Magic Guard**: Prevents trap damage
- **Substitute**: Can block the initial trap attempt

This ability effectively gives the Pokemon a free Whirlpool attack whenever it enters battle, making it valuable for controlling the battlefield and applying pressure to opposing teams.
---
id: 106
name: Aftermath
status: reviewed
character_count: 128
---

# Aftermath - Ability ID 106

## In-Game Description
"If faints by a contact move, attacker takes 25% of max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses a 100 BP Explosion or Outburst (whichever is higher) when knocked out. Using explosion moves will always Flinch the target.

## Detailed Mechanical Explanation

Aftermath is a reactive ability that triggers when specific conditions are met:

### Activation Conditions:
1. The Pokemon with Aftermath must faint (HP reaches 0)
2. The fainting blow must be from a contact move
3. The attacker must still be on the field

### Damage Calculation:
- Deals exactly 25% of the attacker's maximum HP as damage
- Minimum damage is 1 HP (if calculation results in 0)
- This damage is considered "passive damage" and ignores type effectiveness

### Interactions:
- **Bypasses Substitute**: The damage hits the attacker directly, ignoring any Substitute
- **Magic Guard**: Pokemon with Magic Guard are immune to Aftermath damage
- **Multi-hit moves**: Only triggers once, even if a multi-hit contact move causes the faint
- **Non-contact moves**: No effect (special attacks, status moves, etc.)
- **Indirect damage**: No effect (poison, burn, sandstorm, etc.)

### Technical Implementation:
The ability uses the `onDefender` hook and checks:
- If the defender (ability holder) is no longer alive
- If the move that caused the faint was a contact move
- If standard on-hit effects should apply to the attacker
- If the attacker has Magic Guard protection

The damage is calculated as `attacker.maxHP / 4` and applied through a special battle script that handles the HP reduction and potential fainting of the attacker.

### Strategic Uses:
- Deterrent against physical attackers
- Revenge killing tool for sacrificial plays
- Synergizes with Focus Sash strategies
- Effective against frail physical sweepers
- Can secure KOs even after fainting

### Common Pokemon with Aftermath:
This ability appears on various Pokemon as both a regular ability and innate ability, often found on explosive or volatile-themed Pokemon that fit the "going out with a bang" concept.
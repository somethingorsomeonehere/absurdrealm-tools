---
id: 234
name: Intrepid Sword
status: reviewed
character_count: 88
---

# Intrepid Sword - Ability ID 234

## In-Game Description
"On entry, raises Attack by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Intrepid Sword raises the Pokemon's Attack stat by one stage when switching into battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Trigger**: When the Pokemon with Intrepid Sword switches into battle (entry ability)

**Effect**: Raises the user's Attack stat by one stage (+50% Attack)

**Technical Details**:
- Uses the same code structure as Dauntless Shield but for Attack instead of Defense
- Checks if the stat can be raised using `CanRaiseStat(battler, STAT_ATK)` before activating
- Uses `SetStatChanger(STAT_ATK, 1)` to apply exactly one stage boost
- Calls `BattleScript_BattlerAbilityStatRaiseOnSwitchIn` for the battle message
- Cannot be prevented by abilities like Clear Body, White Smoke, or Hyper Cutter that prevent stat reduction
- Will fail if the Pokemon's Attack is already at maximum (+6 stages)
- Activates every time the Pokemon switches in, not just the first time

**Pokemon with this Ability**:
- Mega Gallade (all three ability slots, plus innate abilities: Dual Wield, Fatal Precision, Avenger)
- Used as innate ability on certain other Pokemon

**Related Abilities**:
- Dauntless Shield (ID 235): Same effect but raises Defense instead of Attack
- Embody Aspect variants: Similar entry stat boosts for different stats
- Crowned Sword (ID 527): Combines Intrepid Sword with Anger Point effects

**Notes**:
- This is a signature ability from Pokemon Sword/Shield, faithfully implemented in Elite Redux
- The ability is particularly powerful in Elite Redux's 4-ability system when used as an innate ability
- Triggers before any other entry effects or abilities that might depend on stats
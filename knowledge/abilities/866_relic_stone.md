---
id: 866
name: Relic Stone
status: reviewed
character_count: 103
---

# Relic Stone - Ability ID 866

## In-Game Description
Other battlers don't benefit from STAB.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

While the user is on field, every other Pokemon does not receive a STAB bonus from typing or abilities. 

## Detailed Mechanical Explanation

### Technical Implementation
- **Function**: Modifies `StabMultiplierInHalves()` in `src/battle_util.c`
- **Mechanism**: When any battler except the attacker has Relic Stone, the function returns 2 (1.0x multiplier) instead of normal STAB values
- **Scope**: Field-wide effect that impacts all other battlers
- **Breakable**: Yes - can be suppressed by Mold Breaker and similar abilities
- **Interaction**: Prevents both regular STAB (1.5x) and Adaptability STAB (2.0x)

## Battle Mechanics
1. Checks if any battler on the field (except the attacker) has Relic Stone
2. If found, forces STAB multiplier to 1.0x for ALL battlers except Relic Stone users
3. Applies to all move types and does not discriminate between physical/special moves
4. Effect persists as long as a Relic Stone user remains active in battle

## Strategic Usage
- Excellent for defensive teams facing STAB-reliant sweepers
- Particularly effective against mono-type teams that rely heavily on STAB damage
- Can neutralize powerful Adaptability users like Porygon-Z or Crawdaunt
- Synergizes well with diverse movepool teams that don't rely on STAB
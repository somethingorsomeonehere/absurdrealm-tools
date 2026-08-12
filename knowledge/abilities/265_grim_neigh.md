---
id: 265
name: Grim Neigh
status: reviewed
character_count: 117
---

# Grim Neigh - Ability ID 265

## In-Game Description
"KOs raise Sp. Atk by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grim Neigh boosts the Pokemon's Special Attack by one stage when it causes an opponent to faint with a direct attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Trigger Condition:** 
- When this Pokemon causes an enemy Pokemon to faint through direct attack damage

**Effect:**
- Raises the user's Special Attack stat by 1 stage (+50% Special Attack)
- Applied using the MoxieClone function with STAT_SPATK parameter

**Technical Implementation:**
- Uses the `onBattlerFaints` callback with `APPLY_ON_ATTACKER`
- Calls `MoxieClone(battler, STAT_SPATK)` to handle the stat boost
- Follows the same logic as Moxie but boosts Special Attack instead of Attack

**Interaction Notes:**
- Only triggers on direct KOs from the ability holder's attacks
- Does not trigger from:
  - Poison/burn damage finishing off a target
  - Entry hazard damage
  - Recoil damage from the opponent's moves
  - Weather damage
- Can stack multiple times if multiple KOs occur
- Works in double battles when this Pokemon KOs any opponent
- The boost persists until the Pokemon switches out or the battle ends
- Can be stolen by Trace, Role Play, or similar ability-copying moves

**Competitive Usage:**
- Excellent on special sweepers like Spectrier (original user)
- Creates snowball potential in battle - each KO makes subsequent KOs easier
- Particularly strong in formats with multiple weak opponents
- Synergizes well with moves that can OHKO weakened targets
- Can turn close 2HKOs into guaranteed OHKOs after the first boost

**Related Abilities:**
- **Moxie:** Attack version of this ability
- **Chilling Neigh:** Attack version, functionally identical to Moxie
- **Beast Boost:** Boosts highest stat on KO instead of fixed stat
- **Soul-Heart:** Special Attack boost on any Pokemon fainting nearby
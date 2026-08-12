---
id: 618
name: Fragrant Daze
status: reviewed
character_count: 89
---

# Fragrant Daze - Ability ID 618

## In-Game Description
"30% chance to confuse on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

30% chance to inflict confusion on contact moves, both when attacking and being attacked.

## Detailed Mechanical Explanation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Function**: `FragrantDaze` (lines 6488-6499)
- **Trigger**: `ON_EITHER` - activates when receiving damage

### Mechanics
1. **Trigger Condition**: Activates when the user is hit by a move
2. **Contact Requirement**: Only triggers on moves that make contact (`IsMoveMakingContact`)
3. **Confusion Check**: Verifies the attacker can be confused (`CanBeConfused`)
4. **Hit Effect Check**: Confirms ability should apply (`ShouldApplyOnHitAffect`)
5. **Probability**: 30% chance (`Random() % 100 < 30`)
6. **Effect**: Applies confusion status via `AbilityStatusEffectSafe`

### Strategic Applications
- **Defensive Utility**: Punishes physical attackers with potential confusion
- **Contact Moves Only**: Ineffective against special attacks or non-contact physical moves
- **Status Disruption**: Can disrupt opponent's offensive momentum through confusion
- **Type Synergy**: Works well on Pokemon that can tank physical hits

### Pokemon with Fragrant Daze
- **Furfrou Debutante Form**: Has as one of three regular abilities
- **Flairgrance**: Has as an innate ability (always active)

### Technical Details
- **Ability ID**: 618 in the enum system
- **Proto Definition**: Located in `AbilityList.textproto`
- **Status Effect**: Uses `MOVE_EFFECT_CONFUSION` 
- **Safety Check**: Uses `AbilityStatusEffectSafe` to prevent invalid applications

### Interactions and Limitations
- Does not affect Pokemon immune to confusion
- Only triggers on contact moves (Tackle, Bite, etc.)
- Does not trigger on special attacks or non-contact physical moves
- 30% activation rate provides balanced risk/reward
- Can be blocked by abilities that prevent status conditions
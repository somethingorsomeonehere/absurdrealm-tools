---
id: 260
name: Unseen Fist
status: reviewed
character_count: 118
---

# Unseen Fist - Ability ID 260

## In-Game Description
"Contact moves strike through protection."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Unseen Fist allows all contact moves to bypass protection moves and ignore any secondary effects associated with them. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**Unseen Fist** is a powerful offensive ability that negates the defensive utility of protection moves when using contact attacks.

**Core Mechanics:**
- Contact moves completely bypass protection from Protect, Detect, King's Shield, Spiky Shield, Baneful Bunker, Obstruct, and similar moves
- The protection effect is ignored, allowing damage to be dealt normally
- Secondary effects from protection moves (poison from Baneful Bunker, stat reduction from King's Shield/Obstruct) still apply
- Only affects moves that have the "contact" flag in their move data
- Shell Side Arm is specially coded to work with this ability when damage category is swapped

**Battle Implementation:**
In the game code, Unseen Fist is checked in the `ProtectionOverlap` function in `battle_util.c`. When determining if a move is blocked by protection, the game checks if the attacker has Unseen Fist and the move makes contact. If both conditions are true, the function returns FALSE, meaning protection is bypassed.

**Strategic Applications:**
- Excellent for breaking through defensive strategies that rely on protection moves
- Particularly effective against stall teams and defensive Pokemon
- Allows setup sweepers to maintain momentum without being stopped by protection
- Pairs well with high-power contact moves like Close Combat, Flare Blitz, or Brave Bird

**Related Abilities:**
- Final Blow: A combination ability that includes Unseen Fist + Fatal Precision effects
- Both abilities share the same protection-bypassing code in the battle engine

**Counters and Limitations:**
- Only works with contact moves - special attacks and non-contact physical moves don't benefit
- Doesn't bypass immunities (Ghost immunity to Normal/Fighting, etc.)
- Status moves and non-damaging contact moves also bypass protection but don't deal damage
- Opposing Pokemon can still use evasion, type immunities, or abilities like Wonder Guard for defense

This ability transforms contact-based attackers into reliable offensive forces that can't be easily walled by protection spam.
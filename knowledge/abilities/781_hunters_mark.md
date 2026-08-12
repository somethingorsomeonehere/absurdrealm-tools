---
id: 781
name: Hunter's Mark
status: reviewed
character_count: 296
---

# Hunter's Mark - Ability ID 781

## In-Game Description
"Ambush + Deadeye."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees a critical hit on the user's first turn after switching in or at the start of battle. The user is unable to miss arrow-based attacks and cannon moves (only moves blocked by Bulletproof). Additionally, when landing critical hits, the attack targets the opponent's weaker defensive stat.

## Detailed Mechanical Explanation
*For Discord/reference use*

Hunter's Mark is a powerful combination ability that merges two distinct combat abilities:

**Deadeye Component:**
- **Perfect Accuracy**: Grants 100% accuracy (never misses) to:
  - All Mega Launcher boosted moves (pulse moves, beam moves, ballistic moves)
  - All arrow-based moves (marked with `arrow: true` in move data)
- **Critical Hit Targeting**: When landing a critical hit, the ability calculates both the target's Defense and Special Defense stats, then automatically targets whichever is lower, maximizing damage output

**Ambush Component:**
- **First Turn Critical**: All attacks made on the user's first turn in battle are guaranteed critical hits
- This effect only applies to the very first turn the Pokemon is on the field

**Synergy Effects:**
The combination creates a devastating opening strategy - first turn attacks are guaranteed critical hits that will target the opponent's weaker defensive stat while also having perfect accuracy if using compatible moves.

**Compatible Move Types:**
- **Mega Launcher Boosted**: Hyper Beam, Flash Cannon, Focus Blast, Signal Beam, Moongeist Beam, Steel Beam, and many others
- **Arrow-Based**: All moves with the `arrow: true` flag, including Diamond Arrow, Archer Shot, Volt Bolt, and various custom projectile moves

**Strategic Applications:**
1. **Opening Gambit**: Devastating first-turn damage with guaranteed critical hits
2. **Ranged Specialist**: Perfect accuracy with projectile and beam attacks
3. **Stat Manipulation**: Critical hits bypass defensive boosts while targeting weaker stats
4. **Coverage Options**: Works with diverse move types due to broad compatibility

This ability is particularly effective on Pokemon with high Attack or Special Attack stats and access to compatible moves, making them formidable opening sweepers or specialized ranged attackers.
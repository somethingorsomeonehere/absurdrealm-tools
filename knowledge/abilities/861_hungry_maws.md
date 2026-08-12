---
id: 861
name: Hungry Maws
status: reviewed
character_count: 182
---

# Hungry Maws - Ability ID 861

## In-Game Description
This Pokemon's bite and jaw moves are boosted by 30%, with healing on KO.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Bite and jaw moves are boosted by 30%. Restores 50% max HP when defeating foes with biting moves or 25% with other moves. Only activates when knocking out a target with a direct hit.

## Detailed Mechanical Explanation

### Mechanics

### Strong Jaw Component
- Boosts damage of bite/jaw moves by 30% (1.3x multiplier)
- Affects moves with the `FLAG_STRONG_JAW_BOOST` flag
- Enhanced moves include: Bite, Crunch, Thunder Fang, Ice Fang, Fire Fang, Hyper Fang, Super Fang, Poison Fang, Psychic Fangs, Jaw Lock, Bolt Beak, Fishious Rend, and many more

### Jaws of Carnage Component
- Heals when KOing opponents with attacking moves
- **50% HP recovery** when KOing with Strong Jaw boosted moves
- **25% HP recovery** when KOing with non-Strong Jaw moves
- Only triggers on KO by the ability holder (attacker)
- Requires the Pokemon to not be at full HP to activate healing

## Implementation
- Combines `StrongJaw.onOffensiveMultiplier` for damage boost
- Uses `JawsOfCarnage.onBattlerFaints` for healing on KO
- Healing amount determined by whether the finishing move has `FLAG_STRONG_JAW_BOOST`

## Synergy
Perfect combination ability that rewards aggressive play with jaw-based moves, providing both offensive power and sustain for maintaining battle presence.
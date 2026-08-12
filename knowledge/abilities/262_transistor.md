---
id: 262
name: Transistor
status: reviewed
character_count: 112
---

# Transistor - Ability ID 262

## In-Game Description
"Boosts the power of Electric-type moves by 1.5x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transistor increases the power of all Electric-type moves by 50%. Stacks additively with other damage modifiers.

## Detailed Mechanical Explanation
*For Discord/reference use*

Transistor is a straightforward damage-boosting ability that provides a consistent 1.5x power multiplier to all Electric-type moves used by the Pokemon that has this ability.

**Key Mechanics:**
- **Type-Specific Boost**: Only affects Electric-type moves, regardless of move category (physical, special, or status moves that deal damage)
- **Multiplicative Stacking**: The 1.5x multiplier stacks multiplicatively with other damage modifiers such as STAB (Same Type Attack Bonus), type effectiveness, items like Choice Band/Specs, stat boosts, weather effects, and field effects
- **Move Coverage**: Affects all damaging Electric moves including but not limited to:
  - Physical: Thunder Punch, Wild Charge, Spark, Volt Tackle
  - Special: Thunderbolt, Thunder, Discharge, Electro Ball
  - Multi-hit: Pin Missile (if Electric-type through Normalize + Electrify combo)

**Implementation Details:**
- Implemented via the `onOffensiveMultiplier` callback in the Elite Redux ability system
- Triggers during damage calculation phase before final damage is applied
- Does not affect non-damaging Electric moves (Thunder Wave, etc.)
- The boost is applied even if the move is resisted or not very effective

**Competitive Usage:**
Transistor is essentially the Electric-type equivalent of abilities like Blaze, Torrent, and Overgrow, but provides a constant boost rather than an emergency boost at low HP. This makes it particularly valuable for Electric-type Pokemon that want consistent damage output throughout the battle.

**Similar Abilities:**
- Dragon's Maw (Dragon-type moves)
- Steelworker (Steel-type moves) 
- Pixilate/Aerilate/Refrigerate (type conversion + boost)
- Tough Claws (contact moves)
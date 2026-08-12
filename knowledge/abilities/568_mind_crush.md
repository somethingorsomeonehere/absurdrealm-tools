---
id: 568
name: Mind Crush
status: reviewed
character_count: 117
---

# Mind Crush - Ability ID 568

## In-Game Description
"Biting moves use Special Attack and deal 30% more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Biting moves use the Special Attack (still targets enemy's Defense unless stated otherwise) and deal 30% more damage. 

## Detailed Mechanical Explanation

Mind Crush transforms biting moves to use Special Attack instead of Attack while also boosting their damage by 30%, creating a unique niche for special attackers to utilize the typically physical biting move pool.

### Mechanics
- **Affected Moves**: All moves with FLAG_STRONG_JAW_BOOST (biting moves)
- **Dual Effect**:
  1. Category conversion: Makes biting moves use Special Attack stat
  2. Damage boost: 1.3x multiplier (30% increase)
- **Move Examples**: Bite, Crunch, Fire Fang, Ice Fang, Thunder Fang, Poison Fang, Psychic Fangs, Bug Bite, Hyper Fang, Fishious Rend

### Code Implementation
The ability modifies damage calculation to:
1. Force biting moves to calculate damage using Special Attack
2. Apply a 1.3x damage multiplier to the final damage

### Strategic Applications
- **Special Attacker Viability**: Allows high SpA Pokemon to use biting moves effectively
- **Coverage Options**: Provides physical coverage moves for special attackers
- **Damage Output**: 30% boost makes it stronger than Strong Jaw for special attackers
- **Mixed Attacker Potential**: Creates unique offensive profiles

### Comparison to Similar Abilities
- **Strong Jaw**: Boosts biting moves but keeps them physical
- **Mind Crunch**: Changes to special + 30% boost
- **Gnashing Cannon**: Combines Mind Crunch + Mega Launcher effects

### Notable Interactions
- Works with all biting moves regardless of original category
- The 30% boost stacks with other damage modifiers
- Particularly effective on Pokemon with high SpA but access to good biting moves


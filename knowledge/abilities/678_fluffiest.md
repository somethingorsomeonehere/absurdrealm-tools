---
id: 678
name: Fluffiest
status: reviewed
character_count: 141
---

# Fluffiest - Ability ID 678

## In-Game Description
Quarters contact damage taken. 2x weak to fire.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from contact moves by 75%. Fire-type moves to deal x4 damage to the user. Multiplicative with other forms of damage reduction.

## Detailed Mechanical Explanation

### Technical Implementation
- `onDefensiveMultiplier`: Applies 0.25x multiplier to contact damage and 2.0x multiplier to Fire-type moves
- Breakable ability that can be suppressed by Mold Breaker and similar effects
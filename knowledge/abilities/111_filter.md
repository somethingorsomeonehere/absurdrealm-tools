---
id: 111
name: Filter
status: reviewed
character_count: 106
---

# Filter - Ability ID 111

## In-Game Description
"Takes 35% less damage from Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

Filter is a defensive ability that triggers when the Pokemon takes damage from a super-effective move. Here's how it works:

1. **Damage Reduction**: When hit by a super-effective move (2x damage or higher), Filter reduces the final damage to 65% of what it would normally be
   - A 2x super-effective move effectively becomes 1.3x damage
   - A 4x super-effective move effectively becomes 2.6x damage

2. **Calculation Timing**: The reduction is applied as a defensive multiplier after type effectiveness is calculated but before the final damage is dealt

3. **Breakable Ability**: Filter is marked as a "breakable" ability, meaning it can be bypassed by:
   - Mold Breaker
   - Teravolt
   - Turboblaze
   - Any other ability-ignoring effects

4. **Stacking**: Filter stacks multiplicatively with other damage reduction effects like:
   - Light Screen/Reflect
   - Defensive stat boosts
   - Other damage-reducing abilities or items

5. **Type Coverage**: This ability is particularly valuable for Pokemon with multiple weaknesses, as it provides blanket protection against all super-effective hits regardless of type

The ability is identical in function to Solid Rock and Prism Armor, differing only in name and which Pokemon can have it.
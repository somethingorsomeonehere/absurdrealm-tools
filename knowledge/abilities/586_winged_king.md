---
id: 586
name: Winged King
status: reviewed
character_count: 43
---

# Winged King - Ability ID 586

## In-Game Description
"Ups 'supereffective' by 33%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Super effective attacks are boosted by 33%.

## Detailed Mechanical Explanation

Winged King enhances super-effective attacks by applying an additional 1.33x damage multiplier. This ability specifically triggers when the base type effectiveness multiplier is 2.0x or higher (super-effective). The 33% boost is multiplicative, meaning a 2x super-effective attack becomes 2.66x damage, while 4x super-effective attacks become 5.32x damage.

The ability works by intercepting the offensive damage calculation after type effectiveness is determined. It only affects moves that would naturally deal super-effective damage - neutral and not very effective attacks are unmodified.

This ability is also used by Iron Serpent, sharing the exact same implementation and mechanics.

## Trigger Conditions

- Pokemon with Winged King uses an attacking move
- The move deals super-effective damage (2x or 4x type effectiveness)
- Triggers during damage calculation phase, after type effectiveness is applied

## Numerical Effects

- **2x super-effective**: 2.0 x 1.33 = 2.66x total damage
- **4x super-effective**: 4.0 x 1.33 = 5.32x total damage
- **Neutral/resisted moves**: No change (1.0x, 0.5x, 0.25x remain unchanged)

## Interactions

- **Stacks multiplicatively** with STAB (Same Type Attack Bonus), items, and other damage modifiers
- **Example**: Super-effective STAB move = 2.0 (type) x 1.5 (STAB) x 1.33 (Winged King) = 3.99x damage
- Works with physical and special attacks equally
- Applies to all move types and damage categories
- Functions in all battle formats and conditions

## Special Cases

- Does not affect moves that become super-effective through abilities like Scrappy or type-changing effects - only natural type matchups
- The ability checks the final type effectiveness multiplier, so moves hitting dual-types correctly calculate (e.g., 2x effectiveness against one type, neutral against the other = no boost)

## Notes

This ability significantly enhances wallbreaking potential and coverage moves. Pokemon with diverse movepools benefit most, as they can reliably trigger the boost against various targets. The multiplicative stacking makes super-effective STAB moves particularly devastating, often securing OHKOs against would-be checks and counters.
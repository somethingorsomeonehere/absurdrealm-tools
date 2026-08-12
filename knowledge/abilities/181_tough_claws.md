---
id: 181
name: Tough Claws
status: reviewed
character_count: 33
---

# Tough Claws - Ability ID 181

## In-Game Description
"Boosts the power of contact moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact moves are boosted by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

Tough Claws provides a 1.3x (30%) damage multiplier to any move that makes contact with the target, as determined by the `IsMoveMakingContact()` function. The ability is implemented through the `onOffensiveMultiplier` callback, which applies the multiplier during damage calculation.

### Key Mechanics:
- **Contact Detection**: Uses the same contact detection system as abilities like Static and Gooey
- **Multiplier Application**: Applied during offensive damage calculation, stacking multiplicatively with other damage boosts
- **Move Types Affected**: While most contact moves are physical attacks, the ability works with any move flagged as making contact
- **Implementation**: Shares the same code implementation as Big Pecks' offensive multiplier

### Common Contact Moves:
- Most physical attacking moves (Tackle, Body Slam, Earthquake doesn't count)
- Multi-hit moves that make contact (each hit gets the boost)
- Priority moves that make contact (Quick Attack, Mach Punch)
- Status moves that make contact are not boosted (they don't deal damage)

### Notable Interactions:
- Stacks with other damage multipliers (STAB, type effectiveness, items)
- Works with Parental Bond (each hit gets the boost)
- Does not boost moves that don't make contact (Hyper Beam, Flamethrower, etc.)
- The boost is applied before accuracy checks and other battle calculations

This ability is particularly valuable for physical attackers with access to strong contact moves, making it a staple ability for melee-focused Pokemon builds.
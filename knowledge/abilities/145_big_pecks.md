---
id: 145
name: Big Pecks
status: reviewed
character_count: 41
---

# Big Pecks - Ability ID 145

## In-Game Description
"Boosts the power of contact moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of contact moves by 30%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Big Pecks in Elite Redux has been completely reworked from its vanilla effect (which prevented Defense stat reduction). The new implementation provides a 1.3x (30%) multiplier to the power of any move that makes contact with the target.

### Technical Details:
- **Contact Detection**: Uses `IsMoveMakingContact(move, battler)` to determine if a move makes contact
- **Damage Calculation**: Applied during the offensive multiplier phase of damage calculation
- **Move Types**: Affects both physical and special moves that make contact
- **Stacking**: This multiplier stacks with other damage-boosting effects like STAB, type effectiveness, and items

### Contact Move Examples:
- **Physical**: Tackle, Quick Attack, Scratch, Bite, Thunder Punch, Ice Punch
- **Special**: Grass Knot, Petal Dance (if it makes contact in this hack)
- **Status**: Does not affect non-damaging moves

### Pokemon That Learn Big Pecks:
Big Pecks is typically found on bird Pokemon and other creatures with prominent beaks or claws, making thematic sense for enhanced contact-based attacks.

### Competitive Usage:
This ability transforms Big Pecks into a powerful offensive tool, making it particularly valuable for Pokemon with strong contact move pools. The 30% boost is significant enough to change damage calculations and KO thresholds in competitive play.
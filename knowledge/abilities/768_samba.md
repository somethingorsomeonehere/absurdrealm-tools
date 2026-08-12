---
id: 768
name: Samba
status: reviewed
character_count: 192
---

# Samba - Ability ID 768

## In-Game Description
"Striker + Dancer"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the power of all kicking moves by 30%. Includes Pyro Ball. When any Pokemon on the field uses a dance move, this Pokemon immediately uses the same move after. Triggers once per move.

## Detailed Mechanical Explanation
*For Discord/reference use*

Samba is a dual-component ability that combines two distinct effects:

**Striker Component (Offensive Boost):**
- Provides a 1.3x (30%) damage multiplier to moves flagged as striker moves
- Affects moves with FLAG_STRIKER_BOOST in their move data
- Also affects moves with FLAG_IRON_FIST_BOOST if the user has Junshi Sanda ability
- This boost applies during damage calculation before type effectiveness

**Dancer Component (Move Copying):**
- Automatically copies any dance move used by any Pokemon on the battlefield
- Triggers on moves with FLAG_DANCE in their move data
- Also triggers on non-status moves if the original user has Taekkyeon ability
- Uses UseOutOfTurnAttack to execute the copied move immediately after the original
- The copied move uses the same target selection as the original move

**Implementation Details:**
- Samba inherits `.onOffensiveMultiplier` from Striker ability
- Samba inherits `.onCopyMove` from Dancer ability
- Both effects function independently and simultaneously
- The ability provides both offensive power and battlefield awareness
- Striker boost only applies to specific move types, not all moves
- Dancer copying occurs regardless of the original move's success or failure

**Strategic Applications:**
- Excellent for Pokemon that learn both striking moves and dance moves
- Provides consistent offensive pressure while gaining utility from opponent's dance moves
- Works well in doubles/multi-battle formats where dance moves are more common
- The striker boost makes physical attacking moves significantly more threatening
- Can potentially copy beneficial dance moves from allies in doubles battles
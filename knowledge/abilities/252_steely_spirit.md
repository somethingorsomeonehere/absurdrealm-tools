---
id: 252
name: Steely Spirit
status: reviewed
character_count: 104
---

# Steely Spirit - Ability ID 252

## In-Game Description
"Boosts own & ally's Steel-type moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Steely Spirit increases the power of Steel-type moves by 30% for both the user and its allies in battle. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanic:**
- Provides a 1.3x (30%) power multiplier to all Steel-type moves
- Applies to both the user's own Steel-type moves AND allied Pokemon's Steel-type moves
- Functions as an offensive multiplier in the damage calculation

**Technical Implementation:**
- Uses `onOffensiveMultiplier` callback with type checking (`moveType == TYPE_STEEL`)
- Has `onOffensiveMultiplierFor = APPLY_ON_ALLY` flag, enabling the ally support mechanic
- Multiplier applies during damage calculation before other modifiers

**Battle Applications:**
- Excellent for Steel-type teams or mixed teams with multiple Steel-type attackers
- Particularly valuable in doubles battles where both Pokemon can benefit simultaneously
- Synergizes well with powerful Steel-type moves like Iron Head, Meteor Mash, and Steel Beam
- Stacks multiplicatively with other damage modifiers (items, weather, etc.)

**Strategic Considerations:**
- Best used on bulky Steel-types that can stay on the field to support teammates
- Pairs exceptionally well with Steel-type attackers like Metagross, Lucario, or Dialga
- The ally support makes this ability unique among type-boosting abilities
- Consider team positioning in doubles to maximize both Pokemon benefiting from the boost

**Comparison to Similar Abilities:**
- Similar to abilities like Battery (Special Attack boost for allies) but type-specific
- More specialized than general power-boosting abilities like Huge Power
- The ally component makes it more team-oriented than most offensive abilities

**Elite Redux Context:**
- Multiple Pokemon in Elite Redux have access to this ability, both as innate and regular abilities
- Commonly found on Steel-type Pokemon and mechanically-themed species
- Works well within Elite Redux's 4-ability system as either a changeable or fixed ability
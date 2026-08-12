---
id: 174
name: Refrigerate
status: reviewed
character_count: 104
---

# Refrigerate - Ability ID 174

## In-Game Description
"Normal-type moves become Ice and Ice gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves to Ice-type and grants STAB for Ice moves, regardless of the user's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Type Conversion Mechanics:**
- All Normal-type moves used by the Pokemon are converted to Ice-type
- This conversion happens before damage calculation and type effectiveness checks
- The converted moves are treated as Ice-type for all purposes including STAB, weaknesses, resistances, and immunities

**STAB (Same Type Attack Bonus):**
- The Pokemon gains STAB for ALL Ice-type moves, regardless of whether the Pokemon naturally has Ice typing
- STAB provides a 1.5x damage multiplier
- This applies to both naturally Ice-type moves and converted Normal moves

**Elite Redux Implementation Differences:**
- Unlike main series Pokemon games, Refrigerate in Elite Redux does NOT provide the standard 1.2x power boost to converted moves
- The ability only provides type conversion and STAB access
- This makes the ability slightly weaker than its main series counterpart but still valuable for accessing Ice STAB

**Strategic Applications:**
- Allows non-Ice types to hit Water, Ground, Flying, and Dragon types super-effectively with converted Normal moves
- Particularly powerful on Pokemon with strong Normal-type movepools like Body Slam, Return, Hyper Voice
- Grants Ice STAB to Pokemon that wouldn't normally have it
- Can be countered by Steel types (immune to Ice) and Fire types (resist Ice)

**Move Examples:**
- Normal moves like Tackle, Body Slam, Hyper Voice become Ice-type with STAB
- Existing Ice moves like Ice Beam continue to get STAB
- Status moves remain unaffected by type conversion

**Interaction Notes:**
- Works with the Elite Redux 4-ability system as either a changeable or innate ability
- Can stack with other offensive abilities for powerful combinations
- Doesn't affect moves that are already Ice-type (they just get STAB if applicable)
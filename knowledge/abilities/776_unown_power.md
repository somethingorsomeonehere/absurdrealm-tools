---
id: 776
name: Unown Power
status: reviewed
character_count: 216
---

# Unown Power - Ability ID 776

## In-Game Description
"Mystic Power + Hidden and Secret Power hit Super-effectively."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants the 1.5x STAB damage bonus to all moves regardless of type matching. Does not boost moves that already receive a STAB bonus. Hidden/Secret Power is always super effective (x2).

Detailed Mechanical Explanation 
## Detailed Mechanical Explanation
*For Discord/reference use*

Unown Power is a hybrid ability that combines two distinct effects:

### Mystic Power Component (STAB on All Moves)
- **Effect**: Grants Same Type Attack Bonus (STAB) to ALL moves, regardless of type matching
- **Implementation**: Uses `.onStab = +[](ON_STAB) -> int { return TRUE; }` which always returns TRUE for STAB calculation
- **Benefit**: Every move gets a 1.5x damage multiplier, making the Pokemon extremely versatile offensively

### Super-Effective Hidden/Secret Power Component
- **Effect**: Forces Hidden Power and Secret Power to deal super-effective (2x) damage against all targets
- **Implementation**: Uses `.onAfterTypeEffectiveness` callback that checks if the effectiveness multiplier is less than 2.0x for these specific moves, then forces it to 2.0x
- **Mechanics**: `if (*mod < UQ_4_12(2.0) && (move == MOVE_HIDDEN_POWER || move == MOVE_SECRET_POWER)) *mod = UQ_4_12(2.0);`

### Move Details
- **Hidden Power**: Special move with 80 base power, variable type based on IVs (EFFECT_HIDDEN_POWER)
- **Secret Power**: Physical move with 80 base power, Normal-type with variable effects (EFFECT_HIDDEN_POWER)
- Both moves become universally super-effective (2x) with this ability

### Overall Impact
- **Total Multiplier**: Hidden Power and Secret Power get both STAB (1.5x) AND super-effective (2x) = 3.0x total multiplier
- **All Other Moves**: Get STAB (1.5x) regardless of type
- **Strategic Value**: Transforms Unown into a versatile attacker with guaranteed effectiveness on signature moves

### Pokemon with This Ability
- **Unown (Revelation Form)**: A legendary variant with enhanced stats (138 Attack/Special Attack, 133 Defense/Special Defense)
- **Ability Slot**: Innate ability (always active alongside other abilities)
- **Tier**: Tier 1 legendary Pokemon

### Restrictions
- **Randomizer Banned**: This ability is marked as `randomizerBanned = TRUE`, preventing it from appearing on random Pokemon during randomizer runs
- **Form-Specific**: Only available on the special Revelation form of Unown, not regular Unown forms

This ability effectively makes Unown Revelation a formidable special attacker with guaranteed super-effective coverage through Hidden Power and Secret Power, while maintaining offensive presence with STAB on all other moves.
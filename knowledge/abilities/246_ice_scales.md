---
id: 246
name: Ice Scales
status: reviewed
character_count: 97
---

# Ice Scales - Ability ID 246

## In-Game Description
"Halves damage taken by Special moves. Does NOT double SpDef."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves all incoming Special Attack damage. Multiplicative with other sources of damage reduction.   

## Detailed Mechanical Explanation
*For Discord/reference use*

Ice Scales is a defensive ability that reduces damage from special moves by 50%. It functions as a damage multiplier applied during damage calculation, specifically using the `onDefensiveMultiplier` hook with a 0.5x multiplier when the incoming move is classified as special (checked via `IS_MOVE_SPECIAL(move)`).

### Key Mechanics:
- **Damage Reduction**: Applies a 0.5x multiplier to all special move damage
- **Timing**: Applied during damage calculation, after stat calculations
- **Move Classification**: Only affects moves flagged as special attacks
- **Suppression**: Can be bypassed by abilities like Mold Breaker (marked as `breakable = TRUE`)
- **Stacking**: Does not stack with other damage reduction effects

### Comparison to Similar Abilities:
- **Fur Coat**: Physical counterpart that halves physical move damage
- **Prism Scales**: Similar concept but reduces special damage by 30% instead of 50%
- **Solid Rock/Filter**: Reduce super effective damage rather than all special damage

### Counterplay:
- Mold Breaker, Teravolt, Turboblaze can ignore the damage reduction
- Physical attacks are unaffected
- Status moves and indirect damage (like Stealth Rock) bypass the protection
- Critical hits still deal increased damage, but the base damage is still halved

### Notable Users in Elite Redux:
Based on trainer data analysis, Ice Scales is commonly found on:
- Glaceon (defensive wall sets)
- Various Ice-type Pokemon as a defensive utility ability
- Often paired with other defensive abilities in the 4-ability system

This ability is particularly valuable in the Elite Redux metagame due to the prevalence of special attackers and the 4-ability system allowing for defensive synergies.
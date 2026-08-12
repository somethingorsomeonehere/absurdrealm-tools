---
id: 283
name: Christmas Spirit
status: reviewed
character_count: 156
---

# Christmas Spirit - Ability ID 283

## In-Game Description
"Takes 50% less damage if hail is active."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Christmas Spirit reduces all incoming damage by 50% during hail weather. Grants immunity to hail damage. Multiplicative with other damage reduction sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

Christmas Spirit is a powerful defensive ability that provides significant damage reduction in hail weather conditions. Here are the complete mechanics:

### Damage Reduction
- Reduces all incoming damage by exactly 50% (multiplies by 0.5) when hail is active
- Uses the `onDefensiveMultiplier` hook, meaning it applies after type effectiveness but before other defensive calculations
- Works against all attack types: physical, special, and status moves that deal damage
- Stacks multiplicatively with other damage reduction effects (like resistances, items, or other abilities)

### Weather Compatibility
- Activates during any form of hail weather (`WEATHER_HAIL_ANY`)
- Works with temporary hail from moves like Hail
- Works with permanent hail effects
- Does NOT work with other weather conditions (sun, rain, sandstorm, fog, strong winds)

### Hail Immunity
- The Pokemon is completely immune to hail damage (`hailImmune = TRUE`)
- This immunity is separate from the damage reduction and always active
- Prevents the typical 1/16 HP loss per turn that non-Ice types suffer in hail

### Ability Properties
- **Breakable**: Can be suppressed by abilities like Mold Breaker (`breakable = TRUE`)
- **Interaction with Other Abilities**: Stacks with other defensive abilities and effects
- **Battle Switching**: Effect applies immediately when switching into hail weather
- **Weather Changes**: Effect activates/deactivates instantly when hail starts/ends

### Strategic Implications
- Exceptional defensive utility in hail teams
- Pairs well with hail-setting moves or abilities
- Creates powerful defensive cores when combined with other damage reduction
- Particularly effective against mixed attackers since it reduces both physical and special damage equally

### Example Damage Calculations
- Super effective move dealing 200 damage to 100 damage with Christmas Spirit
- With additional 25% resistance: 200 x 0.75 x 0.5 = 75 damage
- Stacks with items like Assault Vest for special attacks

This ability transforms Pokemon into exceptional defensive walls in hail weather, making them nearly impossible to KO with single attacks while providing complete immunity to hail's passive damage.
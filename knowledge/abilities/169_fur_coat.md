---
id: 169
name: Fur Coat
status: reviewed
character_count: 89
---

# Fur Coat - Ability ID 169

## In-Game Description
"Halves damage taken by Physical moves. Does NOT double Defense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves all incoming Attack damage. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

Fur Coat is a defensive ability that reduces damage from physical moves by 50%. It represents thick, protective fur that acts as natural armor against physical attacks.

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Implementation**: Uses `onDefensiveMultiplier` callback
- **Breakable**: Yes (can be suppressed by Mold Breaker-type abilities)

### Mechanics
```cpp
constexpr Ability FurCoat = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_PHYSICAL(move)) MUL(.5);
        },
    .breakable = TRUE,
};
```

- Multiplies physical move damage by 0.5 (50% reduction)
- Only affects moves that use the Physical attack stat
- Does not affect Special moves, status moves, or indirect damage
- Can be suppressed by abilities like Mold Breaker, Turboblaze, Teravolt

## Battle AI Rating
**Rating**: 7/10 - Considered a strong defensive ability by the battle AI.

## Pokemon with Fur Coat
This ability appears on 40+ Pokemon in Elite Redux, including:

### As Primary/Changeable Ability
- Various furry Normal-types
- Some defensive Pokemon

### As Innate Ability
- Wigglytuff line (Jigglytuff, Wigglytuff)
- Furret line (Sentret, Furret) 
- Teddiursa line (Teddiursa, Ursaring, Ursaluna)
- Many other furry Pokemon species
- Some legendary/mythical Pokemon

## Related Abilities
- **Ice Scales**: Special move equivalent (halves Special move damage)
- **Prismatic Fur**: Combination ability that includes Fur Coat
- **Filter/Solid Rock**: Reduce super effective damage instead of all physical damage

## Strategic Notes
- Excellent for physically defensive Pokemon
- Pairs well with high HP or Special Defense
- Can be worked around with Special attacks
- Mold Breaker-type abilities can suppress it
- Does not stack with other damage reduction abilities

## Lore/Thematic Connection
Represents the protective qualities of thick fur found on many mammals. The ability name and effect directly reference how dense fur can provide cushioning and protection against physical impacts in nature.
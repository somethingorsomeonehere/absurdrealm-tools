---
id: 264
name: Chilling Neigh
status: reviewed
character_count: 102
---

# Chilling Neigh - Ability ID 264

## In-Game Description
"KOs raise Attack by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When this Pokemon knocks out an opponent with a direct attack, its Attack stat increases by one stage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Chilling Neigh is a signature ability that triggers whenever the Pokemon with this ability defeats an opponent through direct attack damage. Here are the complete mechanics:

### Core Mechanics
- **Trigger Condition**: Must directly knock out an opponent with an attacking move
- **Effect**: Raises the user's Attack stat by one stage (+50% Attack)
- **Timing**: Activates immediately after the target faints
- **Stacking**: Multiple KOs provide multiple Attack boosts (up to +6 stages maximum)

### Implementation Details
- Uses the same core function as Moxie but targets Attack stat specifically (STAT_ATK = 1)
- Implemented via `MoxieClone(battler, STAT_ATK)` function
- Requires `HasAttackerFaintedTarget()` check to verify the KO was from this Pokemon's attack
- Uses `ChangeStatBuffs()` with MOVE_EFFECT_AFFECTS_USER flag

### Important Interactions
- **As One (Ice Rider)**: Combines this ability with Unnerve - both effects activate simultaneously
- **Crowned King**: Combines this with Unnerve and Grim Neigh for both Attack and Special Attack boosts
- **Status Moves**: Does NOT activate from indirect damage (poison, burn, etc.)
- **Substitute/Endure**: Does NOT activate if the target survives with 1 HP
- **Multi-hit Moves**: Only needs the final hit to cause the KO

### Comparison with Related Abilities
- **Moxie**: Identical mechanics, but Chilling Neigh is typically associated with Ice-type legendary Pokemon
- **Grim Neigh**: Sister ability that raises Special Attack instead of Attack
- **Beast Boost**: Raises the highest stat instead of specifically Attack

### Competitive Applications
- Excellent for physical sweepers that can secure KOs
- Particularly powerful in formats with weaker defensive Pokemon
- Pairs well with Choice items or Life Orb for initial KO power
- Strong in late-game cleanup scenarios

### Code Location
- Defined in `src/abilities.cc` as `constexpr Ability ChillingNeigh`
- Listed in ability mapping at ID 264 (ABILITY_CHILLING_NEIGH)
- Description stored in `proto/AbilityList.textproto`
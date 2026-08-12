---
id: 114
name: Storm Drain
status: reviewed
character_count: 152
---

# Storm Drain - Ability ID 114

## In-Game Description
"Redirects Water moves. Absorbs them, ups highest Atk."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user draws in Water-type moves and gains immunity to them. Additionally, Water-type moves boost the highest attacking stat of the user by one stage.

## Detailed Mechanical Explanation

Storm Drain is a defensive ability with offensive benefits that provides complete immunity to Water-type moves while boosting the user's offensive capabilities.

**Core Mechanics:**
- Redirects all single-target Water-type moves aimed at the user's partner to this Pokemon
- Completely absorbs redirected Water moves, taking no damage
- Upon absorbing a Water move, raises the Pokemon's highest attacking stat by one stage
- The ability determines which stat to boost by comparing current Attack vs Special Attack, including stat stage modifiers
- Multi-target Water moves (like Surf in doubles) are not redirected but still absorbed if they hit this Pokemon

**Technical Implementation Details:**
- Uses `redirectType = TYPE_WATER` to handle move redirection
- The `onAbsorb` handler checks for Water-type moves and returns `ABSORB_RESULT_STAT`
- Uses `GetHighestAttackingStatId(battler, TRUE)` to determine whether to boost Attack or Special Attack
- The TRUE parameter means it considers stat stages when determining the highest attacking stat
- Classified as a "breakable" ability, meaning it can be suppressed by Mold Breaker and similar effects

**Strategic Applications:**
- Excellent in double battles where it can protect partners from Water attacks
- Provides a safe switch-in against predicted Water moves
- Can turn defensive plays into offensive momentum through stat boosts
- Pairs well with Pokemon weak to Water in doubles
- The adaptive stat boost ensures both physical and special attackers benefit optimally

**Interaction Notes:**
- Water-type status moves are also redirected and absorbed
- Hidden Power Water and other moves that become Water-type are affected
- The ability activates even if the user is already immune to Water (e.g., through typing)
- Stat boosts can accumulate if multiple Water moves are absorbed
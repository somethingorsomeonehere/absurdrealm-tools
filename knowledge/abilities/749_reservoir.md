---
id: 749
name: Reservoir
status: reviewed
character_count: 207
---

# Reservoir - Ability ID 749

## In-Game Description
"Water Absorb + Storm Drain."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user is draws in Water-type moves and gain immunity to them. Additionally, Water-type moves boost the highest attacking stat of the user by one stage and heal for 25% of their max HP when absorbing them.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Reservoir is a powerful defensive-offensive ability that combines the effects of Water Absorb and Storm Drain. When the Pokemon is hit by Water-type moves, it both heals HP and gains a stat boost, making it an exceptional ability for pivot Pokemon and mixed attackers.

### Activation Conditions
- **Move type requirement**: Must be hit by a Water-type move
- **Healing effect**: Recovers 25% of maximum HP (same as Water Absorb)
- **Stat boost effect**: Raises the highest attacking stat by one stage (same as Storm Drain)
  - Chooses between Attack and Special Attack based on which is higher
  - If tied, prioritizes Attack stat
- **Move redirection**: Single-target Water moves are redirected to this Pokemon (like Storm Drain)

### Technical Implementation
```c
constexpr Ability Reservoir = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_WATER);
        *statId = GetHighestAttackingStatId(battler, TRUE);
        return ABSORB_RESULT_STAT | ABSORB_RESULT_HEAL;
    },
    .redirectType = TYPE_WATER,
    .breakable = TRUE,
};
```

The ability combines both ABSORB_RESULT_HEAL (Water Absorb effect) and ABSORB_RESULT_STAT (Storm Drain effect) using bitwise OR operation.

### Important Interactions
- **Multi-hit moves**: Each hit triggers both healing and stat boost
- **Substitute**: Doesn't block the effects if substitute is broken
- **Maximum HP**: Still triggers stat boost even if at full HP
- **Stat boost cap**: Won't boost if already at +6 in the relevant attacking stat
- **Move redirection**: Only affects single-target moves, not spread moves like Surf
- **Priority**: Redirection happens before damage calculation

### Strategic Implications
- **Dual threat**: Both defensive (healing) and offensive (stat boost) benefits
- **Team support**: Redirects Water moves away from teammates
- **Setup potential**: Can use Water-type attacks as setup opportunities
- **Mixed attacker synergy**: Benefits both physical and special attackers
- **Water immunity**: Essentially immune to Water-type damage in most scenarios

### Common Users
- Mixed attackers who can use both Attack and Special Attack
- Pivot Pokemon that need sustainability
- Pokemon weak to Water that want to turn the weakness into a strength
- Team supporters who can redirect dangerous Water moves

### Competitive Usage Notes
- Excellent on teams weak to common Water attackers like Kingdra or Rotom-Wash
- Provides both immediate healing and long-term offensive presence
- Can force opponents to avoid Water-type coverage moves
- Particularly valuable in formats with powerful Water-type threats
- Works well with Pokemon that have good mixed offensive stats

### Counters
- **Non-Water attacks**: Ability only works against Water-type moves
- **Mold Breaker effects**: Ignore the ability entirely
- **Multi-target moves**: Surf, Origin Pulse aren't redirected
- **Status moves**: Only affects damaging Water moves
- **Ability suppression**: Neutralizing Gas, Core Enforcer disable it

### Synergies
- **Mixed movesets**: Pokemon with both physical and special attacks
- **Recovery moves**: Stacks with other healing for incredible sustain
- **Stat-boosting items**: Life Orb, Expert Belt work well with boosted stats
- **Team positioning**: Pairs with Pokemon weak to Water coverage
- **Weather**: Rain teams can provide consistent Water move opportunities

### Differences from Components
**vs Water Absorb:**
- Adds stat boost and move redirection
- More offensive utility beyond just healing

**vs Storm Drain:**
- Adds healing component for sustainability
- Dual benefit makes it much more powerful

### Version History
- New ability introduced in Elite Redux
- ID 749 represents the final ability milestone in the current ability set
- Combines two classic abilities for modern competitive utility
- Designed for mixed attackers and pivot Pokemon
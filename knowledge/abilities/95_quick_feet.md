---
id: 95
name: Quick Feet
status: reviewed
character_count: 112
---

# Quick Feet - Ability ID 95

## In-Game Description
Ups Speed by 1.5x if suffering from a status condition.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Speed stat by 50% when suffering from any status condition. Negates the Speed drop from paralysis status.

## Detailed Mechanical Explanation

### Basic Information
- **Effect**: Boosts Speed by 50% when afflicted with any status condition
- **Introduced**: Generation IV

### Speed Boost
- Increases Speed stat by 50% (1.5x multiplier) when the Pokemon has any status condition
- Works with all status conditions: burn, poison, paralysis, sleep, freeze, and bleed (Elite Redux-specific)
- The speed boost is calculated after all other speed modifiers

### Paralysis Interaction
- Quick Feet uniquely ignores the Speed reduction from paralysis
- While paralyzed Pokemon normally have their Speed cut (by 50% in Gen 7+ or 75% in earlier gens), Quick Feet users maintain full Speed and gain the 50% boost on top
- This makes paralysis potentially beneficial for Quick Feet users, turning a typical disadvantage into a speed advantage

### Strategic Uses
- Commonly paired with Flame Orb or Toxic Orb for self-inflicted status
- Can turn status moves from opponents into speed advantages
- Particularly effective with paralysis due to negating the speed drop
- Synergizes with Facade, which doubles in power when statused

### Notable Users
- Ursaring and Ursaluna often use Quick Feet with Flame Orb/Toxic Orb strategies
- Poochyena, Mightyena, Grumpig, and Linoone also have access to this ability


## Competitive Analysis

### Advantages
- Reliable speed boost through self-inflicted status
- Turns defensive status moves into setup opportunities
- Makes paralysis a positive rather than negative
- Good synergy with status-boosted moves like Facade

### Disadvantages
- Requires taking status damage each turn (burn/poison)
- Sleep and freeze prevent attacking, limiting usefulness
- Takes up item slot if using status orbs
- Vulnerable to being outsped before status is applied

### Common Sets
1. **Physical Sweeper**: Flame Orb + Facade + Quick Feet for boosted speed and doubled Facade damage
2. **Toxic Orb Variant**: For Poison Heal synergy or longer battles where burn damage is too much
3. **Switch-in Set**: Switching into expected status moves to activate the boost

## Code Implementation
Location: `src/abilities.cc`
```c
constexpr Ability QuickFeet = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && HasAnyStatusOrAbility(battler)) *stat *= 1.5;
        },
};
```

The ability checks if the Pokemon has any status condition via `HasAnyStatusOrAbility()` and applies a 1.5x multiplier to the Speed stat. The paralysis speed drop immunity is handled separately in `battle_main.c`.
---
id: 65
name: Overgrow
status: reviewed
character_count: 74
---

# Overgrow - Ability ID 65

## In-Game Description
"Boosts Grass-type moves by 1.2x, or 1.5x when under 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Grass-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

**OVERGROW** is a passive offensive ability that provides damage multipliers to Grass-type moves based on the user's current HP status.

### Activation Mechanics:
- **Trigger**: Automatic on any Grass-type move used by the ability holder
- **Type**: Offensive multiplier (onOffensiveMultiplier hook)
- **HP Threshold**: 1/3 of maximum HP (gBattleMons[battler].maxHP / 3)
- **No Animation**: Silent activation with no battle message

### Damage Multipliers:
1. **Above 1/3 HP**: 1.2x damage multiplier to Grass-type moves
2. **At or Below 1/3 HP**: 1.5x damage multiplier to Grass-type moves

### Move Interactions:
- **Affected Moves**: All Grass-type moves (Physical, Special, Status moves with damage)
- **Examples**: Vine Whip, Razor Leaf, Solar Beam, Leaf Storm, Giga Drain, Energy Ball
- **Status Moves**: Does not affect non-damaging status moves like Sleep Powder
- **Multi-hit Moves**: Each hit receives the full multiplier
- **Variable Power**: Works with moves like Grass Knot and Low Kick

### Technical Implementation:
```c
constexpr Ability Overgrow = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_GRASS),
};

#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
            else                                                             \
                MUL(1.2);                                                    \
        }                                                                    \
    }
```

### Stacking and Interactions:
- **STAB**: Stacks multiplicatively with Same Type Attack Bonus (1.5x)
  - Normal: 1.2x x 1.5x = 1.8x total
  - Pinch: 1.5x x 1.5x = 2.25x total
- **Items**: Stacks with type-boosting items like Miracle Seed
- **Weather**: Stacks with beneficial weather effects
- **Abilities**: Does not stack with other damage-boosting abilities on the same Pokemon
- **Critical Hits**: Multiplier applies before critical hit calculation

### Strategic Applications:
1. **Consistent Boost**: Provides reliable 1.2x boost throughout battle
2. **Comeback Potential**: 1.5x boost when low on HP creates clutch moments
3. **HP Management**: Players may strategically take damage to reach pinch range
4. **Substitute Strategy**: Using Substitute to reach 1/3 HP threshold safely

### Pokemon with Overgrow:
- Commonly found as an innate ability on Grass-type starter Pokemon and their evolutionary lines
- Appears as an innate ability in Elite Redux's multi-ability system
- Paired with other abilities like Chlorophyll, Thick Fat, and Poison Absorb

### Competitive Notes:
- **Early Game**: 1.2x boost provides consistent damage advantage
- **Late Game**: 1.5x boost can secure crucial KOs when low on HP
- **Team Synergy**: Pairs well with healing support to control HP ranges
- **Risk vs Reward**: Low HP requirement creates high-risk, high-reward scenarios

### Related Abilities:
- **Blaze** (Fire-type equivalent)
- **Torrent** (Water-type equivalent) 
- **Swarm** (Bug-type equivalent)
- **Forest Rage** (Boosted version: 1.3x/1.8x multipliers)

### Version History:
- Gen 3-8: Standard swarm-type ability with 1.5x boost at 1/3 HP
- Elite Redux: Enhanced to provide 1.2x boost at full HP, 1.5x at 1/3 HP threshold
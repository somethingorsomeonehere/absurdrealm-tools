---
id: 634
name: Last Stand
status: reviewed
character_count: 182
---

# Last Stand - Ability ID 634

## In-Game Description
"Def and SpDef increase as HP drops. Max 1.6x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Defense and Special Defense increase linearly as HP decreases. Multiplier scales from 1.0x at full HP to 1.6x at 0% HP. At 50% HP provides 1.3x boost, at 25% HP provides 1.45x boost.

## Detailed Mechanical Explanation

**Last Stand** provides a dynamic defensive boost that scales continuously with missing HP percentage, making the Pokemon more defensive as it becomes more damaged.

### Core Formula
`stat x (1 + 0.6 x missingHPPercent)`

Where `missingHPPercent` is calculated as `(maxHP - currentHP) / maxHP`

### Implementation
- **File Location**: `/src/abilities.cc` (lines 6594-6601)
- **Hook**: `onStat` - triggers during Defense/Special Defense calculations
- **Real-time Updates**: Recalculates with each HP change during battle
- **Both Stats**: Applies to both Defense AND Special Defense simultaneously

## Trigger Conditions

- **Continuous Effect**: No specific trigger - always active when calculating defensive stats
- **HP Dependent**: Effect strength depends on current HP percentage
- **Real-time**: Updates immediately when HP changes during battle

## Numerical Effects

### Key HP Breakpoints
- **100% HP**: 1.00x multiplier (no boost)
- **75% HP**: 1.15x multiplier (15% boost)
- **50% HP**: 1.30x multiplier (30% boost) 
- **25% HP**: 1.45x multiplier (45% boost)
- **10% HP**: 1.54x multiplier (54% boost)
- **1% HP**: 1.594x multiplier (59.4% boost)
- **0% HP**: 1.60x multiplier (60% boost - theoretical maximum)

### Scaling Characteristics
- **Linear Progression**: No breakpoints or thresholds
- **Maximum Multiplier**: 1.6x (60% increase) at 0% HP
- **Practical Maximum**: 1.594x at 1% HP (effectively maximum)

## Interactions

- **Mold Breaker**: Can suppress this ability's effects
- **Stat Modifications**: Applies after other stat stage changes
- **Healing**: Defensive power decreases as HP is restored
- **Damage**: Defensive power increases as HP is lost

## Special Cases

- **Full HP**: Provides no benefit when at maximum health
- **Critical HP**: Most powerful when at 1% HP (common survival threshold)
- **Percentage Based**: Works regardless of total HP amount
- **Both Stats**: Unlike most abilities, affects two different stats

## Notes

- **High-Risk/High-Reward**: Encourages staying at low HP for maximum benefit
- **Endgame Power**: Becomes extremely powerful in late-battle scenarios
- **Survival Tool**: Helps ensure survival when HP gets critically low
- **Unique Scaling**: One of the few abilities with continuous, linear scaling
- **Strategic HP Management**: Optimal play may involve managing HP deliberately
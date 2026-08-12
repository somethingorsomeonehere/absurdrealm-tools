---
id: 342
name: Seaweed
status: reviewed
character_count: 186
---

# Seaweed - Ability ID 342

## In-Game Description
"Grass-types resist Fire attacks and deal 2x damage to Fire-types."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

If user is Grass-type, they take half damage from Fire-type attacks and deals 2x damage to Fire-type Pokemon with Grass-type moves. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

### Overview

Seaweed is a specialized ability that creates powerful Fire-Grass type interactions, reflecting the aquatic nature of seaweed and its resistance to fire while being naturally effective against fire-based threats. This ability provides both defensive and offensive benefits specifically related to Fire-type interactions.

## Mechanics

### Defensive Component
- **Condition**: User must be a Grass-type Pokemon
- **Effect**: Takes 50% damage from Fire-type attacks (0.5x multiplier)
- **Implementation**: `if (moveType == TYPE_FIRE && IS_BATTLER_OF_TYPE(battler, TYPE_GRASS)) RESISTANCE(0.5);`

### Offensive Component  
- **Condition**: User attacks Fire-type Pokemon with Grass-type moves
- **Effect**: Grass-type moves deal double damage (2.0x multiplier)
- **Implementation**: `if (moveType == TYPE_GRASS && IS_BATTLER_OF_TYPE(target, TYPE_FIRE)) RESISTANCE(2);`

### Technical Details
- **File Location**: `/src/abilities.cc` lines 3615-3625
- **Ability Definition**: `constexpr Ability Seaweed`
- **Breakable**: Yes (can be disabled by abilities like Mold Breaker)
- **Hooks**: `onOffensiveMultiplier` and `onDefensiveMultiplier`

## Code Implementation

```cpp
constexpr Ability Seaweed = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_GRASS && IS_BATTLER_OF_TYPE(target, TYPE_FIRE)) RESISTANCE(2);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE && IS_BATTLER_OF_TYPE(battler, TYPE_GRASS)) RESISTANCE(0.5);
        },
    .breakable = TRUE,
};
```

## Strategic Applications

### Defensive Usage
- **Fire Resistance**: Transforms normally super-effective Fire attacks into neutral damage
- **Switch-in Opportunities**: Allows safe switching into Fire-type attacks
- **Survivability**: Significantly improves longevity against Fire-type threats

### Offensive Usage
- **Fire-type Punishment**: Grass moves become devastatingly effective against Fire-types
- **STAB Synergy**: Combines with Grass-type STAB for massive damage output
- **Coverage Enhancement**: Makes Grass moves extremely threatening to Fire-types

## Competitive Analysis

### Strengths
- **Dual Benefit**: Both offensive and defensive components are valuable
- **Type Coverage**: Excellent against Fire-types, which are common threats
- **Synergy**: Works perfectly with Grass-type Pokemon's natural movepool
- **Utility**: Provides both defensive safety and offensive power

### Weaknesses
- **Type Dependency**: Both effects require the user to be Grass-type
- **Narrow Scope**: Only affects Fire-type interactions
- **Breakable**: Can be negated by Mold Breaker and similar abilities
- **Situational**: Effectiveness depends on opponent's team composition

### Meta Considerations
- **Fire-type Meta**: Becomes more valuable when Fire-types are prevalent
- **Team Support**: Excellent for Grass-type cores and water-themed teams
- **Niche Role**: Specialized anti-Fire tool rather than general utility

## Pokemon with Seaweed

All Pokemon with this ability have it as an innate ability:

### Grass/Water Types
- **Lotad** (Water/Grass) - Early game utility
- **Lombre** (Water/Grass) - Mid-evolution benefits  
- **Ludicolo** (Water/Grass) - Fully evolved offensive threat

### Pure Grass Types
- **Tangela** (Grass) - Defensive utility
- **Tangrowth** (Grass) - Bulky offensive applications

### Grass/Rock Types
- **Lileep** (Rock/Grass) - Fossil Pokemon utility
- **Cradily** (Rock/Grass) - Defensive wall applications

### Grass/Ghost Types
- **Dhelmise** (Ghost/Grass) - Unique typing combinations

## Related Abilities

### Similar Fire Resistance
- **Flash Fire**: Absorbs Fire attacks for stat boosts
- **Water Absorb**: Heals from Water attacks
- **Thick Fat**: Reduces Fire and Ice damage

### Type-Specific Offensive Boosts
- **Steelworker**: Boosts Steel-type moves
- **Transistor**: Boosts Electric-type moves  
- **Dragon's Maw**: Boosts Dragon-type moves

## Interactions and Synergies

### Move Synergies
- **Grass Knot**: Variable power against heavy Fire-types
- **Energy Ball**: Reliable STAB with potential stat drops
- **Leaf Storm**: High-power special attack option
- **Bullet Seed**: Multi-hit physical option

### Team Synergies
- **Rain Teams**: Supports Water-type core strategy
- **Grass Cores**: Enhances mono-Grass team viability
- **Anti-Fire Strategy**: Cornerstone of Fire-type countering

### Item Synergies
- **Life Orb**: Amplifies the doubled Grass damage further
- **Choice Specs**: Maximizes special Grass attack power
- **Leftovers**: Supports defensive Fire-switching role

## Conclusion

Seaweed is a highly specialized but extremely effective ability that excels in specific matchups. While narrow in scope, its dual nature makes it exceptionally powerful against Fire-type threats, providing both the defensive utility to switch in safely and the offensive power to threaten them in return. Its effectiveness is heavily dependent on the metagame presence of Fire-types, making it a situational but potentially game-changing ability for the right Pokemon and team compositions.
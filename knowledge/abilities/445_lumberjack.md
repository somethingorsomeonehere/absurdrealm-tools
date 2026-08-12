---
id: 445
name: Lumberjack
status: reviewed
character_count: 215
---

# Lumberjack - Ability ID 445

## In-Game Description
"Deals 1.5x damage to Grass. Takes 0.5x damage from Grass."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deals 1.5x damage to Grass-type Pokemon and takes 0.5x damage when attacked by Grass-type Pokemon. Based on attacker/defender Pokemon types, not move types. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Lumberjack is a dual-purpose ability that modifies both offensive and defensive damage calculations when facing Grass-type Pokemon. It provides a significant advantage against Grass-types while offering strong defensive utility.

### Activation Conditions
- **Offensive boost**: Deals 1.5x damage to any Pokemon with Grass typing
- **Defensive boost**: Takes 0.5x damage from attacks by Grass-type Pokemon
- **Type checking**: Uses `IS_BATTLER_OF_TYPE(target, TYPE_GRASS)` for precise type checking
- **Dual-type compatibility**: Affects Pokemon with Grass as primary or secondary type

### Technical Implementation
```c
constexpr Ability Lumberjack = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(target, TYPE_GRASS)) RESISTANCE(1.5);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(attacker, TYPE_GRASS)) RESISTANCE(.5);
        },
    .breakable = TRUE,
};
```

### Damage Calculation
- **Offensive multiplier**: 1.5x damage against Grass-types (50% increase)
- **Defensive multiplier**: 0.5x damage from Grass-types (50% reduction)
- **Stacking**: Multipliers apply to final damage calculation after type effectiveness
- **RESISTANCE macro**: Affects both resistance and modifier values for consistent damage scaling

### Important Interactions
- **Type effectiveness**: Stacks with natural type advantages/disadvantages
- **Dual typing**: Affects Pokemon with Grass as either type (e.g., Grass/Flying, Steel/Grass)
- **Forest Curse**: Also affects Pokemon given Grass typing via Forest Curse
- **Trick-or-Treat**: Does not affect Ghost typing added by Trick-or-Treat
- **Ability suppression**: Disabled by Mold Breaker, Neutralizing Gas, etc.

### Strategic Applications
- **Grass counter**: Excellent against Grass-heavy teams and stall cores
- **Wall breaking**: 1.5x multiplier helps break through bulky Grass walls
- **Defensive utility**: Reduces damage from common Grass moves like Giga Drain
- **Type synergy**: Pairs well with Fire, Flying, Ice, and Bug types
- **Meta positioning**: Strong in metas with prevalent Grass-types

### Breakable Ability
Lumberjack has `.breakable = TRUE`, meaning it can be suppressed by:
- **Mold Breaker**: Ignores ability when attacking
- **Neutralizing Gas**: Suppresses ability while active
- **Core Enforcer**: Suppresses ability after hitting with Z-move
- **Gastro Acid**: Suppresses ability until switching out
- **Simple Beam/Skill Swap**: Replaces ability

### Similar Abilities
Lumberjack follows the same pattern as other type-specialist abilities:
- **Dragonslayer**: 1.5x vs Dragon, 0.5x from Dragon
- **Fae Hunter**: 1.5x vs Fairy, 0.5x from Fairy  
- **Monster Hunter**: 1.5x vs Dark, 0.5x from Dark
- **Firefighter**: 1.5x vs Fire, 0.5x from Fire

### Competitive Usage
- **Team role**: Grass-type check and wall breaker
- **Coverage complement**: Pairs with moves that struggle against Grass-types
- **Defensive pivot**: Can switch into Grass attacks more safely
- **Speed control**: Helps against fast Grass sweepers like Chlorophyll users
- **Stall breaking**: Effective against Grass-type stallers and tanks

### Counters and Limitations
- **Non-Grass types**: No effect against 17 other types
- **Ability removal**: Vulnerable to ability suppression effects
- **Type changing**: Loses effectiveness if target loses Grass typing
- **Indirect damage**: Doesn't affect status damage, entry hazards, or weather
- **Setup moves**: Doesn't prevent stat boosts or status moves

### Synergies
- **Fire moves**: Complement Lumberjack's Grass advantage
- **Ice moves**: Additional Grass coverage with shared weaknesses
- **Flying moves**: Hit Grass/Ground types super effectively
- **Bug moves**: Often have good Grass matchups
- **Choice items**: Maximize damage output against Grass-types
- **Life Orb**: Further boost damage calculations

### Team Building Considerations
- **Grass-weak teams**: Provides insurance against Grass threats
- **Wall breaking**: Helps teams struggle with bulky Grass walls
- **Type coverage**: Fills gaps in offensive type coverage
- **Defensive utility**: Reduces need for dedicated Grass resists
- **Meta adaptation**: Strong in Grass-heavy metagames

### Version History
- Elite Redux exclusive ability
- Part of the type-specialist ability family
- Uses standard RESISTANCE macro for consistent damage scaling
- Breakable ability following modern ability conventions
---
id: 442
name: Fae Hunter
status: reviewed
character_count: 215
---

# Fae Hunter - Ability ID 442

## In-Game Description
"Deals 1.5x damage to Fairy. Takes 0.5x damage from Fairy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deals 1.5x damage to Fairy-type Pokemon and takes 0.5x damage when attacked by Fairy-type Pokemon. Based on attacker/defender Pokemon types, not move types. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fae Hunter is a dual-purpose ability that modifies type effectiveness specifically against Fairy-type Pokemon and moves. It provides both offensive and defensive benefits, making the user a dedicated Fairy-type counter.

### Activation Conditions
- **Offensive boost**: 1.5x damage multiplier when attacking Fairy-type Pokemon
- **Defensive boost**: 0.5x damage multiplier when taking damage from Fairy-type moves
- **Type checking**: Checks target's typing for offensive boost, attacker's move type for defensive boost
- **Always active**: No turn-based activation requirements

### Technical Implementation
```c
constexpr Ability FaeHunter = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(target, TYPE_FAIRY)) RESISTANCE(1.5);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(attacker, TYPE_FAIRY)) RESISTANCE(.5);
        },
    .breakable = TRUE,
};
```

### Important Interactions
- **Dual-type Pokemon**: Works on any Pokemon with Fairy as primary or secondary type
- **Move type checking**: Defensive boost applies to any Fairy-type move regardless of user's type
- **Damage calculation**: Applied as a standard damage multiplier in the damage formula
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, and Turboblaze
- **Stacks with type effectiveness**: Multiplies with existing type matchups

### Damage Calculations
- **Super effective fairy moves**: 0.5x multiplier reduces 2x to 1x damage
- **Not very effective fairy moves**: 0.5x multiplier reduces 0.5x to 0.25x damage
- **Neutral fairy moves**: 0.5x multiplier reduces 1x to 0.5x damage
- **Offensive vs Fairy**: 1.5x multiplier before type effectiveness calculations

### Strategic Implications
- **Fairy counter**: Excellent ability for countering Fairy-type threats
- **Offensive utility**: Allows neutral hits to become super effective damage
- **Defensive utility**: Makes Fairy attacks significantly weaker
- **Type coverage**: Provides pseudo-type advantage without changing actual typing
- **Team role**: Natural fit for anti-Fairy specialist roles

### Common Users
- Dark-type Pokemon that naturally resist Fairy moves
- Steel-type Pokemon with existing Fairy resistance
- Pokemon designed as Fairy-type counters
- Physical attackers that need Fairy-type coverage

### Competitive Usage Notes
- Excellent for checking powerful Fairy-type threats
- Provides both offensive and defensive value in one ability
- Does not replace actual type coverage but enhances it
- Allows switching into Fairy-type moves more safely
- Can turn neutral matchups into favorable ones

### Counters
- **Ability suppression**: Mold Breaker variants ignore the ability
- **Non-Fairy attackers**: Ability provides no benefit against other types
- **Status moves**: Doesn't affect non-damaging moves from Fairy-types
- **Indirect damage**: No protection from entry hazards, status conditions, or weather

### Synergies
- **Steel typing**: Stacks with natural Fairy resistance for even greater defense
- **Dark typing**: Complements natural Fairy resistance with offensive boost
- **Poison typing**: Enhances natural Fairy resistance and provides offensive advantage  
- **Physical coverage**: Pairs well with Poison Jab, Iron Head, or Steel Wing
- **Speed control**: Benefits from priority moves or speed boosts to outpace Fairies

### Meta Considerations
- **Fairy-type prevalence**: Value increases with Fairy-type usage in the meta
- **Versatile threats**: Particularly effective against dual-type Fairies
- **Entry hazard support**: Helps wear down Fairy-types for easier KOs
- **Team building**: Allows non-Steel/Poison types to handle Fairy threats
- **Coverage gaps**: Fills type coverage holes in team compositions

### Version History
- Custom ability created for Elite Redux
- Designed to provide specialized anti-Fairy utility
- Both offensive and defensive components for balanced effectiveness
- Breakable status prevents overcentralization
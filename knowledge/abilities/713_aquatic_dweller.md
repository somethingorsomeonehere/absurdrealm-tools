---
id: 713
name: Aquatic Dweller
status: reviewed
character_count: 199
---

# Aquatic Dweller - Ability ID 713

## In-Game Description
"Aquatic + Boosts the power of Water-type moves by 1.5x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Water to the user's current typing. Retains Water typing even upon losing the ability, going away only when switching out. Also boosts the power of Water-type moves by 50%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Aquatic Dweller is a combination ability that merges the effects of the Aquatic ability with a 1.5x multiplier for Water-type moves. This creates a powerful synergy between type addition and offensive capability.

### Component Effects

#### Aquatic Component
- **Type Addition**: Adds Water type to the Pokemon on entry
- **Timing**: Applied immediately when the Pokemon enters battle
- **Stacking**: If Pokemon already has Water type, no change occurs
- **Resistances**: Grants Water-type resistances (Fire, Water, Ice, Steel)
- **Weaknesses**: Adds Water-type weaknesses (Electric, Grass)

#### Water Move Boost Component
- **Damage Multiplier**: 1.5x boost to all Water-type moves
- **Move Coverage**: Affects all Water-type attacks (physical, special, status moves with damage)
- **STAB Interaction**: Stacks multiplicatively with STAB bonus
- **Calculation**: Applied before other damage modifiers

### Technical Implementation
```c
// Aquatic component - adds Water typing on entry
constexpr Ability Aquatic = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_WATER); },
};

// Aquatic Dweller - combines type addition with damage boost
constexpr Ability AquaticDweller = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_WATER) MUL(1.5);
        },
};
```

### Damage Calculation Examples
- **Without STAB**: Base Power x 1.5 (Aquatic Dweller)
- **With STAB**: Base Power x 1.5 (STAB) x 1.5 (Aquatic Dweller) = 2.25x total
- **Example**: Surf (95 BP) to 142.5 BP without STAB, 213.75 BP with STAB

### Important Interactions
- **Type Effectiveness**: Water typing affects matchups against all opponents
- **STAB Synergy**: Pokemon gains STAB on Water moves due to added typing
- **Move Learning**: Doesn't affect move learning or availability
- **Ability Suppression**: Both effects disabled if ability is suppressed
- **Type Changes**: Persists through most type-changing effects

### Strategic Implications
- **Offensive Power**: Massive boost to Water-type attack damage
- **Type Coverage**: Water typing provides additional resistances and coverage
- **STAB Stacking**: Creates extremely powerful Water attacks when combined with natural Water typing
- **Defensive Utility**: Water resistances help against common Fire and Steel attacks
- **Vulnerability**: Electric and Grass moves become more threatening

### Optimal Usage
- **Mixed Attackers**: Benefits both physical and special Water moves
- **Water-type Pokemon**: Incredible damage boost when STAB is already present
- **Non-Water Types**: Transforms them into pseudo-Water types with boosted attacks
- **Coverage Moves**: Makes Water-type coverage moves extremely threatening
- **Rain Teams**: Synergizes with rain for additional Water move boosts

### Competitive Applications
- **Sweeper Setup**: Creates powerful Water-type attackers from any Pokemon
- **Type Coverage**: Provides both offensive and defensive type utility
- **Team Support**: Water resistances help tank Fire/Steel attacks for the team
- **Late Game**: Powerful STAB Water moves can clean up weakened teams
- **Versatility**: Works on both offensive and defensive Pokemon builds

### Comparison to Similar Abilities
- **Pure Aquatic**: Only adds typing, no damage boost
- **Water-type Boost Abilities**: Only boost damage, don't change typing
- **Atlantic Ruler**: Combines with Swift Swim for speed boost as well
- **Adaptability**: Different multiplier system (2x STAB vs 1.5x type boost)

### Common Users
- Mixed attackers who can utilize both physical and special Water moves
- Non-Water types seeking Water coverage and resistances
- Pokemon with access to powerful Water-type moves
- Defensive Pokemon that benefit from Water-type resistances

### Counters
- **Electric Coverage**: Electric moves become super effective
- **Grass Coverage**: Grass moves become super effective
- **Ability Suppression**: Mold Breaker, Neutralizing Gas disable both effects
- **Type Changing**: Some moves can override the added Water typing
- **Defensive Walls**: Still need coverage for Water-resistant opponents

### Synergies
- **Rain Dance/Drizzle**: Additional 1.5x boost to Water moves (stacks multiplicatively)
- **Life Orb/Choice Items**: Further damage amplification
- **Water-type STAB**: Creates incredibly powerful Water attacks
- **Thunder Wave**: Electric moves to cover new Grass weakness
- **Ice Beam**: Coverage for Grass types that resist Water

### Version History
- Custom ability introduced in Elite Redux
- Combines existing Aquatic ability with damage multiplier
- Part of the expanded ability system in Elite Redux
- Used as a component in Atlantic Ruler (combines with Swift Swim)
---
id: 404
name: Mineralize
status: reviewed
character_count: 121
---

# Mineralize - Ability ID 404

## In-Game Description
"Normal-type moves become Rock and Rock gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Rock-type moves and grants STAB for Rock-type moves, regardless of the user's typing.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Mineralize is a type-changing ability that belongs to the "-ate" family of abilities. It fundamentally alters the Pokemon's movepool by converting all Normal-type moves into Rock-type moves while providing Same Type Attack Bonus (STAB) for Rock-type moves.

### Activation Conditions
- **Move type requirement**: Only affects Normal-type moves
- **Automatic conversion**: All Normal moves become Rock-type before damage calculation
- **STAB application**: Grants STAB (1.5x damage) for all Rock-type moves, including converted ones
- **Damage boost**: Provides additional 1.2x multiplier to converted moves (stacks with STAB)

### Technical Implementation
```c
// Mineralize uses the ATE_ABILITY macro with TYPE_ROCK
constexpr Ability Mineralize = {
    ATE_ABILITY(TYPE_ROCK),
};

// ATE_ABILITY macro definition:
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Damage Calculation
1. **Base power**: Normal move's base power
2. **Type conversion**: Move becomes Rock-type
3. **STAB bonus**: 1.5x multiplier for Rock-type moves
4. **-ate boost**: Additional 1.2x multiplier for converted moves
5. **Type effectiveness**: Rock-type effectiveness applies
6. **Final multiplier**: 1.5 x 1.2 = 1.8x total boost to converted Normal moves

### Important Interactions
- **Type effectiveness**: Converted moves use Rock-type effectiveness chart
  - Super effective: Bug, Fire, Flying, Ice (2x damage)
  - Not very effective: Fighting, Ground, Steel (0.5x damage)
  - Immune: None (Rock has no immunities)
- **Move selection**: Only Normal-type moves are affected
- **Hidden Power**: If Hidden Power is Normal-type, it becomes Rock-type
- **Struggle**: Not affected (Struggle is typeless, not Normal-type)
- **Ability suppression**: Doesn't work if ability is suppressed

### Strategic Implications
- **Movepool expansion**: Converts utility Normal moves into offensive Rock moves
- **STAB access**: Provides Rock STAB to non-Rock-type Pokemon
- **Type coverage**: Adds Rock-type offensive coverage
- **Damage boost**: Significant damage increase to former Normal moves
- **Neutral coverage**: Rock hits most types neutrally

### Common Converted Moves
- **Hyper Beam** to Rock-type Hyper Beam (150 BP + 1.8x multiplier)
- **Body Slam** to Rock-type Body Slam (85 BP + 1.8x multiplier)
- **Double-Edge** to Rock-type Double-Edge (120 BP + 1.8x multiplier)
- **Quick Attack** to Rock-type Quick Attack (40 BP + 1.8x multiplier + priority)
- **Extreme Speed** to Rock-type Extreme Speed (80 BP + 1.8x multiplier + +2 priority)
- **Facade** to Rock-type Facade (up to 140 BP + 1.8x multiplier when statused)

### Competitive Usage Notes
- **Physical attackers**: Best on physical attackers with Normal move access
- **Coverage supplement**: Provides Rock coverage without dedicating a move slot
- **STAB expansion**: Effective on non-Rock types that want Rock STAB
- **Priority access**: Can provide Rock-type priority via Quick Attack/Extreme Speed
- **Breaking strategies**: Rock-type moves can break through certain defensive types

### Synergies
- **Physical attacks**: Best with high Attack stat Pokemon
- **Rock-type moves**: Natural synergy with existing Rock moves
- **Coverage moves**: Pairs well with Fighting/Ground moves for type coverage
- **Priority moves**: Enhanced priority Normal moves become powerful Rock priority
- **Status moves**: Normal status moves also become Rock-type (rare but relevant)

### Counters
- **Steel types**: Resist Rock-type moves
- **Fighting types**: Resist Rock-type moves
- **Ground types**: Resist Rock-type moves
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Core Enforcer
- **Rock-immune abilities**: None exist, but Filter/Solid Rock reduce damage
- **Burn status**: Reduces physical damage from converted moves

### Pokemon That Would Benefit
- **High Attack stat**: Pokemon with strong physical stats
- **Normal move access**: Pokemon that naturally learn many Normal moves
- **Non-Rock types**: Pokemon that want Rock-type coverage
- **Priority users**: Pokemon that rely on Quick Attack or Extreme Speed
- **Coverage seekers**: Pokemon needing super-effective hits on Fire/Flying/Bug/Ice

### Version History
- New ability in Elite Redux
- Part of the expanded -ate ability family
- Provides Rock-type variant of popular conversion abilities
- Uses standard ATE_ABILITY implementation for consistency

### Related Abilities
- **Aerilate**: Converts Normal moves to Flying-type
- **Pixilate**: Converts Normal moves to Fairy-type
- **Refrigerate**: Converts Normal moves to Ice-type
- **Galvanize**: Converts Normal moves to Electric-type
- **All -ate abilities**: Share the same 1.2x damage boost and STAB mechanics
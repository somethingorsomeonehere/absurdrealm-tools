---
id: 526
name: Monster Hunter
status: reviewed
character_count: 213
---

# Monster Hunter - Ability ID 526

## In-Game Description
"Deals 1.5x damage to Dark. Takes 0.5x damage from Dark."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deals 1.5x damage to Dark-type Pokemon and takes 0.5x damage when attacked by Dark-type Pokemon. Based on attacker/defender Pokemon types, not move types. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Monster Hunter is a specialized combat ability that provides both offensive and defensive advantages specifically against Dark-type Pokemon and moves. It functions as both a damage amplifier and damage reducer.

### Activation Conditions
- **Offensive bonus**: Activates when attacking any Dark-type Pokemon
  - Applies 1.5x damage multiplier to all moves
  - Works on both physical and special attacks
  - Affects status moves that deal damage
- **Defensive bonus**: Activates when taking damage from Dark-type moves
  - Applies 0.5x damage reduction (halves damage)
  - Works against all Dark-type moves regardless of category
  - Reduces damage from multi-hit Dark moves per hit

### Technical Implementation
```c
// Monster Hunter offensive multiplier
constexpr Ability MonsterHunter = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(target, TYPE_DARK)) RESISTANCE(1.5);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(attacker, TYPE_DARK)) MUL(.5);
        },
    .breakable = TRUE,
};
```

### Important Interactions
- **Type effectiveness**: Stacks with type effectiveness multipliers
- **STAB**: Stacks with Same Type Attack Bonus
- **Other abilities**: Stacks with other damage-modifying abilities
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze
- **Multi-hit moves**: Each hit gets the modifier applied
- **Status moves**: Damage-dealing status moves get offensive bonus

### Damage Calculations
- **Against Dark-type**: Base damage x 1.5 x other modifiers
- **From Dark-type**: Base damage x 0.5 x other modifiers
- **Combined example**: If a Dark-type attacks this Pokemon with a Dark move:
  - Offensive: 1.5x (if this Pokemon attacks back)
  - Defensive: 0.5x (when taking the Dark move)

### Strategic Implications
- **Dark-type counter**: Excellent against Dark-type heavy teams
- **Pivot potential**: Can switch into Dark-type attacks safely
- **Offensive pressure**: Threatens Dark-types with increased damage
- **Type synergy**: Best on Pokemon weak to Dark types normally
- **Limited scope**: Only useful against Dark-type presence

### Meta Considerations
Elite Redux features many Dark-type Pokemon and moves, making Monster Hunter more valuable than in standard formats. The ability provides significant utility in both offensive and defensive roles.

### Common Matchups
- **Umbreon**: Takes half damage from Dark Pulse, deals 1.5x back
- **Tyranitar**: Resists Crunch, threatens with super-effective hits
- **Absol**: Reduces Night Slash damage, hits harder with coverage
- **Sableye**: Counters Foul Play, deals increased damage
- **Hydreigon**: Resists Dark moves, threatens with coverage moves

### Team Building Considerations
- **Dark-heavy metagame**: Most valuable in Dark-type rich environments
- **Coverage moves**: Pairs well with moves that hit Dark types super-effectively
- **Defensive core**: Can serve as a Dark-type check for teams
- **Offensive threats**: Gives offensive Pokemon an edge against Dark types

### Counters and Limitations
- **Non-Dark types**: Provides no benefit against other types
- **Ability suppression**: Mold Breaker variants ignore the ability
- **Weather/terrain**: Other effects may override damage calculations
- **Status conditions**: Doesn't affect non-damaging moves from Dark types
- **Entry hazards**: No protection against hazards from Dark types

### Synergies
- **Fighting-type moves**: Super-effective against Dark, get damage boost
- **Fairy-type moves**: Super-effective against Dark, get damage boost  
- **Bug-type moves**: Super-effective against Dark, get damage boost
- **Recovery moves**: Pairs well with defensive sets that can tank Dark hits
- **Priority moves**: Boosted priority against Dark types

### Pokemon Usage
Monster Hunter is typically found on Pokemon that either:
- Need help against Dark-type threats
- Want to specialize in Dark-type matchups
- Serve as dedicated Dark-type counters
- Benefit from both offensive and defensive Dark-type utility

### Version History
- Custom ability created for Elite Redux
- Designed to provide specialized Dark-type interaction
- Breakable status allows counterplay through ability suppression
- Part of the expanded ability roster for competitive diversity
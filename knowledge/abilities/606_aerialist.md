---
id: 606
name: Aerialist
status: reviewed
character_count: 238
---

# Aerialist - Ability ID 606

## In-Game Description
"Combines ground immunity with exceptional Flying-type prowess."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user is immune to Ground-type moves and other ground effects such as Spikes and terrains. Boosts the damage of Flying-type moves by 25%. Additionally, boosts the power of Flying-type moves by another 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation

Aerialist is a compound ability that combines the effects of two separate abilities:
- **Levitate**: Provides ground immunity and 1.25x Flying-type move power boost
- **Flock**: Implements Flying-type Swarm mechanics (1.2x power normally, 1.5x at <=33% HP)

### Code Structure
```cpp
constexpr Ability Aerialist = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            Levitate.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            Flock.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        },
    .breakable = TRUE,
    .levitate = TRUE,
};
```

### Core Mechanics

1. **Ground Immunity**: Complete immunity to Ground-type moves via `.levitate = TRUE`
2. **Flying-type Power Boosts**: 
   - Base: 1.25x multiplier from Levitate component
   - Additional: 1.2x multiplier from Flock component (normal HP)
   - Critical: 1.5x multiplier from Flock component (<=33% HP)
3. **Stackable Multipliers**: Both effects apply simultaneously to Flying-type moves
4. **Breakable**: Can be suppressed by Mold Breaker-type abilities

### Damage Calculations

For Flying-type moves:
- **Above 33% HP**: 1.25 x 1.2 = 1.5x power multiplier
- **At/Below 33% HP**: 1.25 x 1.5 = 1.875x power multiplier

### Strategic Applications

- **Defensive**: Complete Ground immunity provides crucial switching opportunities
- **Offensive**: Substantial Flying-type move power increases, especially when weakened
- **Positioning**: Levitate component allows safer positioning against Ground-type threats
- **Risk/Reward**: Higher damage potential when at low HP encourages aggressive play


### Related Abilities
- **Levitate** (ID 26): Provides ground immunity and base Flying boost
- **Flock** (ID 359): Provides Flying-type Swarm mechanics
- **Swarm** (ID 68): Original Bug-type version of the HP-based power boost mechanic
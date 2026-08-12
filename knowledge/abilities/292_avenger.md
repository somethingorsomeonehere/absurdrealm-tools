---
id: 292
name: Avenger
status: reviewed
character_count: 89
---

# Avenger - Ability ID 292

## In-Game Description
"If a party Pokemon fainted last turn, next move gets 1.5x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Avenger boosts the power of all moves by 50% for one turn after any party Pokemon faints. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Avenger is a revenge-based ability that provides a significant offensive boost following the loss of a party member. The ability functions through a side-timer system that tracks when a Pokemon has fainted.

### Activation Conditions
- Triggers when any Pokemon on the same side faints
- The retaliation timer is set to 2 when a Pokemon faints
- The ability provides the damage boost when `retaliateTimer > 0`
- Timer decrements by 1 at the end of each turn

### Numerical Values
- **Damage Multiplier**: 1.5x (50% boost)
- **Duration**: One turn after a party member faints
- **Timer Initial Value**: 2 (provides boost for 1 turn)

### Technical Implementation
```cpp
constexpr Ability Avenger = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gSideTimers[GET_BATTLER_SIDE(battler)].retaliateTimer) MUL(1.5);
        },
};
```

The timer is set when a Pokemon faints:
```cpp
// When player Pokemon faints
gSideTimers[0].retaliateTimer = 2;
// When opponent Pokemon faints  
gSideTimers[1].retaliateTimer = 2;
```

Timer decrements each turn:
```cpp
if (gSideTimers[B_SIDE_PLAYER].retaliateTimer > 0) 
    gSideTimers[B_SIDE_PLAYER].retaliateTimer--;
if (gSideTimers[B_SIDE_OPPONENT].retaliateTimer > 0) 
    gSideTimers[B_SIDE_OPPONENT].retaliateTimer--;
```

### Complete List of Affected Moves
- **All offensive moves** receive the 1.5x multiplier
- Applies to physical, special, and status moves that deal damage
- Works with multi-hit moves (each hit gets the boost)
- Compatible with STAB, type effectiveness, and other damage modifiers

### Interactions with Other Abilities/Mechanics
- **Stacks multiplicatively** with other damage boosts (STAB, type effectiveness, etc.)
- **Works alongside** Choice items, Life Orb, and other damage-boosting items
- **Compatible with** weather effects and terrain boosts
- **Functions in** both singles and doubles battles
- **Side-based effect**: Only applies to the side that lost a Pokemon

### Strategic Implications
- **Comeback Potential**: Excellent for turning the tide after losing a key team member
- **Late Game Power**: Becomes more valuable as the battle progresses and casualties mount
- **Doubles Synergy**: Particularly strong in doubles where sacrificial plays are more common
- **Revenge Killing**: Perfect for securing revenge KOs against threatening opponents

### Example Damage Calculations
Assuming a base 100 power move with STAB:
- **Normal**: 100 x 1.5 (STAB) = 150 power
- **With Avenger**: 100 x 1.5 (STAB) x 1.5 (Avenger) = 225 power
- **Effective boost**: 50% increase over normal STAB damage

### Common Users
Avenger is typically found on:
- **Revenge sweepers** that come in after a teammate falls
- **Late-game cleaners** that capitalize on weakened opposing teams  
- **Support Pokemon** that can deal significant damage when needed
- **Pokemon with wide movepools** to threaten multiple types

### Competitive Usage Notes
- **Team positioning**: Best on Pokemon that can switch in safely after a KO
- **Move selection**: Pairs well with high base power moves
- **Timing critical**: The one-turn window requires careful prediction
- **Risk vs Reward**: Losing a Pokemon is costly, but the power boost can be game-changing

### Counters
- **Priority moves**: Can revenge kill before Avenger activates
- **Defensive cores**: Walls can stall out the one-turn timer
- **Status moves**: Sleep, paralysis can waste the boosted turn
- **Protect/Detect**: Can stall out the timer duration

### Synergies
- **Choice Scarf**: Guarantees outspeeding for the revenge KO
- **Life Orb**: Stacks with Avenger for massive damage output
- **High critical hit moves**: Combined with the boost for potential OHKOs
- **Priority moves**: Ensures the boosted attack connects first

### Version History
- Introduced in Elite Redux as a revenge-based offensive ability
- Functions similarly to the move Retaliate but as a passive ability
- Part of the expanded ability roster focusing on situational power boosts
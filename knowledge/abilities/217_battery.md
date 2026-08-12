---
id: 217
name: Battery
status: reviewed
character_count: 119
---

# Battery - Ability ID 217

## In-Game Description
"Grants a 1.3x power boost to ally's Special attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Battery provides a 30% boost to ally Pokemon's Special attacks in double battles. Does not affect the user's own moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Battery boosts the power of Special attacks used by ally Pokemon by 30% (1.3x multiplier) in double battles and multi-battles.

### Activation Conditions
- Only works in double battles, triple battles, or multi-battles
- Must have an ally Pokemon on the field
- Applies to Special moves only (not Physical moves)
- Does not affect the Battery user's own moves

### Technical Implementation
```cpp
constexpr Ability Battery = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_MOVE_SPECIAL(move)) MUL(1.3);
        },
    .onOffensiveMultiplierFor = APPLY_ON_ALLY_ONLY,
};
```

The ability uses the `onOffensiveMultiplier` hook with `APPLY_ON_ALLY_ONLY` flag, meaning it only affects ally Pokemon's moves, not the user's own moves.

### Affected Moves
Battery affects ALL Special moves used by allies, including:
- **Offensive Special moves**: Thunderbolt, Flamethrower, Psychic, etc.
- **Status moves with Special category**: Some status moves are classified as Special
- **Variable power moves**: The boost applies to the final calculated power
- **Multi-hit moves**: Each hit receives the 30% boost

### Interactions with Other Abilities/Mechanics
- **Stacks multiplicatively** with other power-boosting effects
- **Works with** Choice Specs, Life Orb, type-boosting items
- **Compatible with** abilities like Adaptability, Sheer Force on the ally
- **Does not stack** with multiple Battery users (only one 1.3x boost applies)
- **Terrain effects**: Stacks with terrain boosts like Electric Terrain for Electric moves

### Strategic Implications
- **Support role**: Battery users are primarily support Pokemon
- **Team composition**: Best paired with Special attackers
- **Double battle meta**: Significantly more valuable in doubles than singles
- **Positioning**: Battery user should have good bulk to stay on field

### Example Damage Calculations
Base Thunderbolt (90 BP) from ally with Battery support:
- Without Battery: 90 base power
- With Battery: 90 x 1.3 = 117 base power
- With Battery + Choice Specs: 90 x 1.3 x 1.5 = 175.5 base power

### Common Users
Pokemon that commonly have Battery:
- **Charjabug**: Primary Battery user, evolves into Vikavolt
- **Support Pokemon**: Often given to bulky support Pokemon in doubles

### Competitive Usage Notes
- **Doubles tier**: Primarily used in VGC and doubles formats
- **Team synergy**: Requires careful team building around Special attackers
- **Speed control**: Battery users often need Trick Room or speed control
- **Protect usage**: Common to use Protect to maintain Battery support

### Counters
- **Single battles**: Completely ineffective in 1v1 battles
- **Physical attackers**: Does not boost Physical moves
- **Taunt**: Prevents Battery user from using support moves
- **Priority moves**: Can KO the Battery user before they provide support
- **Fake Out**: Can disrupt Battery user's setup

### Synergies
- **Choice Specs users**: Massive damage output with Battery support
- **Life Orb**: Stacks for additional power
- **Weakness Policy**: Battery can help trigger and then boost the activated sweeper
- **Terrain setters**: Electric Terrain + Battery creates powerful Electric-type synergy
- **Trick Room**: Slow Battery users work well in Trick Room teams

### Version History
- **Generation VII**: Introduced in Sun/Moon
- **Elite Redux**: Maintains standard 30% boost functionality
- **Double battle focus**: Designed specifically for multi-battle formats
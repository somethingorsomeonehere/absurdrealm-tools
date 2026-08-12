---
id: 512
name: Combustion
status: reviewed
character_count: 61
---

# Combustion - Ability ID 512

## In-Game Description
"Boosts the power of Fire-type moves by 1.5x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Combustion increases the power of all Fire-type moves by 50%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Combustion is an offensive ability that provides a consistent 1.5x power boost to all Fire-type moves used by the Pokemon. The boost is applied as a multiplicative modifier to the base power of Fire-type attacks.

### Activation Conditions
- **Move type requirement**: Only affects Fire-type moves
- **Timing**: Applied during damage calculation phase
- **Multiplier**: 1.5x (50% increase) to base power
- **Consistent**: Works on every Fire-type move, regardless of power or category

### Technical Implementation
```c
// Combustion boosts Fire-type moves by 1.5x
constexpr Ability Combustion = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE) MUL(1.5);
        },
};
```

### Move Coverage
Combustion affects all Fire-type moves including:
- **Physical moves**: Flare Blitz, Fire Punch, Fire Fang, Flame Wheel
- **Special moves**: Flamethrower, Fire Blast, Heat Wave, Overheat
- **Status moves**: N/A (only affects damaging moves)
- **Multi-hit moves**: Each hit gets the 1.5x boost
- **Variable power moves**: Boost applies to calculated base power

### Important Interactions
- **STAB stacking**: Stacks multiplicatively with STAB (1.5x x 1.5x = 2.25x total)
- **Item boosts**: Stacks with Charcoal, Heat Rock (if applicable)
- **Weather synergy**: Combines with sun's Fire-type boost
- **Critical hits**: Boost applies before crit calculation
- **Type effectiveness**: Calculated after type effectiveness modifiers

### Damage Calculation Order
1. Base power of Fire-type move
2. Combustion multiplier (x1.5)
3. STAB multiplier (x1.5 if Fire-type user)
4. Type effectiveness
5. Critical hit multiplier
6. Other modifiers (items, abilities, etc.)

### Strategic Implications
- **Offensive powerhouse**: Transforms Fire-type users into heavy hitters
- **STAB synergy**: Particularly powerful on Fire-type Pokemon
- **Move diversity**: Benefits all Fire-type moves equally
- **Sun team compatibility**: Excellent on sun teams for maximum Fire power
- **Wall breaking**: Helps break through defensive Pokemon
- **Choice item synergy**: Pairs well with Choice Band/Specs

### Common Users
- Fire-type attackers who want consistent damage
- Mixed attackers with Fire-type coverage
- Sun team sweepers and wallbreakers
- Pokemon with access to powerful Fire-type moves

### Competitive Usage Notes
- Superior to type-specific items for Fire-type specialists
- Allows flexibility in held item choice
- Particularly valuable on Pokemon with wide Fire-type movesets
- Excellent for both physical and special Fire attackers
- Can make weaker Fire moves competitively viable

### Synergies
- **Drought/Sunny Day**: Sun boosts Fire moves further
- **Solar Power**: Combines special attack boost with move power boost
- **Flash Fire**: Can absorb Fire moves to boost own Fire attacks
- **Life Orb**: Stacks for even higher damage output
- **Choice items**: Amplifies already powerful locked-in moves

### Counters
- **Water/Rock/Ground types**: Resist Fire moves despite the boost
- **Flash Fire**: Absorbs Fire moves and gains boost
- **Thick Fat**: Reduces Fire-type damage significantly
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Heatproof**: Halves Fire-type damage
- **Rain weather**: Reduces Fire-type move power

### Comparison to Similar Abilities
- **Technician**: Boosts weak moves; Combustion boosts all Fire moves
- **Tough Claws**: Boosts contact moves; Combustion is type-specific
- **Adaptability**: Boosts STAB; Combustion is more specialized
- **Sheer Force**: Removes secondary effects; Combustion is pure power

### Version History
- Elite Redux custom ability (ID 512)
- Simple but effective offensive ability design
- Provides consistent power boost for Fire-type specialists
- Fits well into the game's ability ecosystem
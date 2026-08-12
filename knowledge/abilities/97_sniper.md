---
id: 97
name: Sniper
status: reviewed
character_count: 87
---

# Sniper - Ability ID 97

## In-Game Description
Critical hits have a 2.25x dmg multiplier instead of 1.5x.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts critical hit damage from 1.5x to 2.25x by applying an additional 50% multiplier. 

## Detailed Mechanical Explanation

### Basic Information
- **Name**: Sniper
- **Description**: Critical hits have a 2.25x dmg multiplier instead of 1.5x.
- **Breakable**: No (standard ability)

### Game Mechanics

### Technical Implementation
Located in `src/abilities.cc`:
```cpp
constexpr Ability Sniper = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (isCrit) MUL(1.5);
        },
};
```

### Damage Calculation
- **Normal critical hit multiplier**: 1.5x (as of Gen 7+, configured in `B_CRIT_MULTIPLIER`)
- **With Sniper**: 2.25x (1.5 x 1.5 = 2.25)
- The ability applies an additional 1.5x multiplier on top of the base critical hit damage
- This stacks multiplicatively, not additively

### Related Abilities
- **Super Sniper**: An enhanced version that includes Sniper's effect plus additional mechanics for follow-up attacks
- **Assassinate**: Uses Sniper's offensive multiplier as part of its effect

## Strategy & Usage

### Optimal Builds
- Pair with moves that have high critical hit ratios (Focus Energy, moves with increased crit chance)
- Works excellently with items like Scope Lens or Razor Claw that boost critical hit rate
- Synergizes with abilities or moves that guarantee critical hits

### Popular Pokemon with Sniper
- **Fearow**: Flying-type physical attacker
- **Drizzile**: Water-type special attacker  
- **Rowlet**: Grass/Flying starter line
- **Arachtres**: Bug-type Pokemon
- **Purrloin**: Dark-type Pokemon
- **Meowth**: Normal-type Pokemon

### Battle Applications
- Turns critical hits into devastating blows with 2.25x damage
- Makes high-crit strategies extremely viable
- Particularly effective in late-game sweeps when combined with stat boosts
- Excellent for breaking through defensive Pokemon when landing critical hits

## Competitive Analysis

### Strengths
- Significantly increases damage output when landing critical hits
- Makes critical-focused strategies much more viable
- Can turn the tide of battle with well-timed crits
- No setup required - passive benefit whenever crits occur

### Weaknesses  
- Relies on RNG unless using guaranteed crit moves/setups
- No benefit on non-critical hits
- Competes with more consistent damage-boosting abilities
- Critical hits ignore positive defense boosts, which may not always be ideal

### Synergies
- **Items**: Scope Lens, Razor Claw, Lansat Berry
- **Moves**: Focus Energy, Night Slash, Leaf Blade, Cross Chop
- **Abilities that boost accuracy**: Ensures crit-focused moves connect
- **Speed control**: Allows getting off multiple attacks for more crit chances


## Notes
- The ability's code shows it multiplies by 1.5 when a crit occurs, which stacks with the base 1.5x crit multiplier
- Critical hits in Elite Redux use Gen 7+ mechanics (1.5x base multiplier)
- Sniper has no additional effects beyond the damage multiplication
- Cannot be suppressed by Mold Breaker as it's not marked as breakable
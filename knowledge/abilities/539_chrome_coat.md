---
id: 539
name: Chrome Coat
status: reviewed
character_count: 160
---

# Chrome Coat - Ability ID 539

## In-Game Description
"Reduces special damage taken by 40%, but decreases Speed by 10%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Chrome Coat reduces special damage by 40% but decreases Speed by 10%. Also triples the user's weight. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

Chrome Coat is a defensive ability that provides significant protection against special attacks while imposing a speed penalty.

### Core Mechanics
- **Special Damage Reduction**: Reduces all incoming special attack damage by 40% (multiplies damage by 0.6)
- **Speed Penalty**: Reduces the Pokemon's Speed stat by 10% (multiplies by 0.9)
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze, and similar abilities

### Activation Conditions
- Special damage reduction applies to ALL special moves that target the Pokemon
- Speed reduction is a permanent stat modification while the Pokemon has this ability
- Both effects are active simultaneously

### Technical Implementation
```cpp
.onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) {
    if (IS_MOVE_SPECIAL(move)) MUL(.6);
},
.onStat = +[](ON_STAT) {
    if (statId == STAT_SPEED) *stat *= .9;
},
.breakable = TRUE,
```

### Affected Moves
All special moves are affected by the damage reduction, including:
- All special attacking moves (Fire Blast, Thunderbolt, Surf, etc.)
- Fixed damage special moves
- Multi-hit special moves (each hit is reduced)
- Does NOT affect physical moves, status moves, or entry hazard damage

### Interactions with Other Abilities/Mechanics
- **Stacks multiplicatively** with other damage reduction effects (Multiscale, Filter, Solid Rock)
- Speed reduction stacks with other speed modifiers (paralysis, Choice Scarf, etc.)
- Can be suppressed by Mold Breaker variants, making the Pokemon lose both benefits and drawbacks
- Works with Assault Vest for maximum special bulk
- Speed reduction affects turn order calculations

### Strategic Implications
**Advantages:**
- Exceptional special wall capabilities
- Allows frail Pokemon to survive powerful special attacks
- Great for pivoting and absorbing hits

**Disadvantages:**
- Speed reduction makes the Pokemon slower and more vulnerable to being outsped
- No protection against physical attacks
- The speed penalty can prevent effective revenge killing

### Example Damage Calculations
Against a 252 SpA Modest Charizard Solar Beam (120 BP) on a 252 HP/252 SpD Bold Blastoise:
- **Without Chrome Coat**: ~45-53% damage
- **With Chrome Coat**: ~27-32% damage (60% of original)

### Common Users
Chrome Coat is typically found on:
- Defensive Steel-types that can afford the speed loss
- Bulky support Pokemon that prioritize survivability
- Pokemon designed for Trick Room teams where speed reduction is beneficial

### Competitive Usage Notes
- **Best suited for**: Defensive/support roles, Trick Room teams
- **Team synergy**: Pairs well with speed control and hazard setters
- **Meta considerations**: More valuable in special attack-heavy metas

### Counters
- **Physical attackers**: Can exploit the lack of physical damage reduction
- **Mold Breaker users**: Completely bypass the ability
- **Status moves**: No protection against burns, paralysis, or other status conditions
- **Entry hazards**: Stealth Rock and Spikes damage is unaffected

### Synergies
- **Assault Vest**: Stacks with Chrome Coat for incredible special bulk
- **Leftovers/Black Sludge**: Helps with longevity to make use of the bulk
- **Trick Room**: Speed reduction becomes an advantage
- **Filter/Solid Rock**: Can stack for even more damage reduction

### Version History
- Added in Elite Redux as part of the extended ability roster
- Shares speed reduction mechanics with Lead Coat (ID 296)
- Designed as the special equivalent to Lead Coat's physical damage reduction
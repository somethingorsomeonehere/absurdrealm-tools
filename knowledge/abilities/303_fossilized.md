---
id: 303
name: Fossilized
status: reviewed
character_count: 193
---

# Fossilized - Ability ID 303

## In-Game Description
"Halves dmg taken by Rock moves. Boosts own Rock moves by 1.2x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Fossilized reduces Rock-type damage by 50% and boosts the user's Rock moves by 20%. Damage reduction is multiplicative with other sources, while the damage boost is additive with other sources.
## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fossilized provides two distinct effects that work independently:

**Defensive Component:**
- Reduces damage from incoming Rock-type moves by 50%
- Applied as a defensive multiplier (`RESISTANCE(.5)`)
- Works against all Rock-type attacks regardless of physical/special classification

**Offensive Component:**
- Boosts the power of the user's Rock-type moves by 20% (1.2x multiplier)
- Applied as an offensive multiplier (`MUL(1.2)`)
- Affects all Rock-type moves used by the Pokemon

### Technical Implementation
```cpp
constexpr Ability Fossilized = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_ROCK) MUL(1.2);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_ROCK) RESISTANCE(.5);
        },
    .breakable = TRUE,
};
```

### Activation Conditions
- **Offensive Boost**: Activates whenever the Pokemon uses any Rock-type move
- **Defensive Resistance**: Activates whenever the Pokemon is targeted by any Rock-type move
- **Breakable**: This ability can be suppressed by Mold Breaker and similar effects

### Affected Moves (Rock-type)
Rock-type moves that receive the 1.2x boost include:
- **Physical**: Rock Slide, Stone Edge, Rock Blast, Head Smash, Accelerock
- **Special**: Power Gem, Ancient Power, Meteor Beam
- **Status**: Stealth Rock (damage calculation when triggered)

### Damage Calculations
**Offensive Boost Example:**
- Base Stone Edge (100 power) to 120 effective power
- With STAB (Same Type Attack Bonus): 100 x 1.5 (STAB) x 1.2 (Fossilized) = 180 effective power
- Critical hit potential makes this extremely dangerous

**Defensive Resistance Example:**
- Incoming Rock Slide (75 power) to 37.5 effective power against Fossilized Pokemon
- Super effective Rock moves against Flying-types: 2x x 0.5 = 1x neutral damage

### Interactions with Other Abilities/Mechanics
- **Stacks with**: STAB, items (Hard Stone, Rock Gem), Weather effects, terrain effects
- **Overridden by**: Mold Breaker, Teravolt, Turboblaze, Neutralizing Gas
- **No interaction with**: Abilities that modify type effectiveness (Solid Rock, Filter)
- **Breakable**: Yes - can be suppressed by ability-negating effects

### Strategic Implications
**Offensive Usage:**
- Transforms Rock-type moves into reliable STAB-level damage even for non-Rock types
- Excellent for mixed attackers using both physical and special Rock moves
- Synergizes with high critical hit ratio moves like Stone Edge

**Defensive Usage:**
- Provides resistance to one of the most common coverage types
- Reduces Stealth Rock damage significantly
- Helps against Rock-type priority moves like Accelerock

### Common Users
Fossilized is primarily found on fossil Pokemon as an innate ability:

**Primary Users:**
- **Kabuto line**: Kabuto, Kabutops - Water/Rock dual types benefit from both aspects
- **Omanyte line**: Omanyte, Omastar - Shell-based Pokemon with ancient origins  
- **Aerodactyl**: Including Mega form - Flying/Rock type gains crucial Rock resistance
- **Cranidos line**: Cranidos, Rampardos - Pure Rock types maximize offensive benefit
- **Shieldon line**: Shieldon, Bastiodon - Defensive Rock/Steel types utilize resistance
- **Anorith line**: Anorith, Armaldo - Bug/Rock types gain balanced benefits
- **Lileep line**: Lileep, Cradily - Rock/Grass types with defensive focus
- **Archen line**: Archen, Archeops - Rock/Flying types benefit from Rock resistance
- **Tyrunt line**: Tyrunt, Tyrantrum - Rock/Dragon types with offensive potential
- **Amaura line**: Amaura, Aurorus - Rock/Ice types gain defensive utility

### Competitive Usage Notes
**Tier 2-4 Usage:**
- Most fossil Pokemon are placed in mid to lower tiers due to stat distributions
- Fossilized helps boost their viability by improving their signature Rock-type coverage
- Particularly valuable on Pokemon with access to both physical and special Rock moves

**Meta Considerations:**
- Rock-type moves are common coverage options, making the resistance valuable
- 20% boost is significant but not overwhelming - maintains competitive balance
- Synergizes well with Choice items and setup moves

### Counters
- **Mold Breaker users**: Completely bypass both effects
- **Non-Rock coverage**: Use other types for neutral damage
- **Status moves**: Ability doesn't affect non-damaging moves
- **Multi-hit moves**: Each hit is reduced individually, but total damage can still be significant

### Synergies
**Item Synergies:**
- **Hard Stone**: Stacks with offensive boost (1.2 x 1.2 = 1.44x total)
- **Rock Gem**: One-time 1.3x boost stacks multiplicatively
- **Choice items**: Enhanced Rock-type moves become extremely powerful

**Team Synergies:**
- **Sandstorm support**: Many fossil Pokemon benefit from Sand immunity/boost
- **Stealth Rock support**: Reduced damage from opposing hazards
- **Rock Polish/Agility**: Speed control to utilize boosted Rock moves

### Version History
- **Elite Redux**: Introduced as signature ability for fossil Pokemon
- **Current Status**: Active and unchanged since implementation
- **Balance Notes**: 20% boost and 50% resistance provide meaningful but balanced effects

### Notes
- The ability name reflects the ancient, petrified nature of fossil Pokemon
- Thematically appropriate as these Pokemon have adapted to geological forces over millions of years
- Provides both offensive and defensive utility without being overpowered
- Helps distinguish fossil Pokemon from other Rock-types in the metagame
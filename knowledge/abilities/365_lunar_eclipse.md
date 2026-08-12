---
id: 365
name: Lunar Eclipse
status: reviewed
character_count: 133
---

# Lunar Eclipse - Ability ID 365

## In-Game Description
"Grants STAB to Fairy and Dark moves. Boosts Hypnosis accuracy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Lunar Eclipse grants STAB bonus to both Fairy and Dark-type moves regardless of the user's typing. Improves Hypnosis accuracy to 90%.

## Detailed Mechanical Explanation

### Overview

**Lunar Eclipse** is ability #365 in Elite Redux, providing a unique combination of offensive and utility benefits. It grants STAB (Same Type Attack Bonus) to both Fairy and Dark-type moves regardless of the Pokemon's actual typing, while also boosting the accuracy of Hypnosis from 60% to 97.5%.

## Mechanics

### STAB Enhancement
- **Effect**: Grants 1.5x damage multiplier to Fairy and Dark-type moves
- **Scope**: Works regardless of the Pokemon's actual typing
- **Stacking**: Does not stack with natural STAB if the Pokemon is already Fairy or Dark type

### Hypnosis Accuracy Boost
- **Base Accuracy**: 60%
- **Modified Accuracy**: 97.5% (60% x 1.5)
- **Reliability**: Makes Hypnosis one of the most reliable sleep moves in the game

## Code Implementation

### Primary Implementation
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
**Lines**: 3810-3813

```cpp
constexpr Ability LunarEclipse = {
    .onStab = +[](ON_STAB) -> int { return moveType == TYPE_DARK || moveType == TYPE_FAIRY; },
    .onAccuracy = Hypnotist.onAccuracy,
};
```

### Supporting Implementation
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
**Lines**: 3459-3465

```cpp
constexpr Ability Hypnotist = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(move == MOVE_HYPNOSIS);
        *accuracy *= 1.5;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

### Ability Registration
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
**Line**: 9210

```cpp
{ABILITY_LUNAR_ECLIPSE, LunarEclipse},
```

## Strategic Applications

### Offensive Versatility
- Pokemon gain access to two additional offensive types with STAB
- Particularly powerful on Pokemon with diverse movepools
- Enables unexpected coverage options

### Sleep Strategy Support
- Reliable sleep induction with 97.5% accurate Hypnosis
- Supports stall and setup strategies
- Combos well with Dream Eater, Nightmare, or setup moves

### Dual-Type Coverage
- Fairy-type moves provide excellent neutral coverage
- Dark-type moves hit Psychic and Ghost types super effectively
- Combined coverage helps against many common threats

## Pokemon with Lunar Eclipse

### As Innate Ability
1. **Lunatone** - Rock/Psychic type gains Fairy/Dark STAB
2. **Lunala** - Psychic/Ghost type with additional offensive options
3. **Necrozma (Dawn Wings)** - Psychic/Ghost type with enhanced coverage

### As Regular Ability
1. **Lycanroc (Eclipse)** - Rock/Ghost type with Fairy/Dark STAB
2. **Minior (All Core Forms)** - Rock/Flying type with dual offensive boost
   - Red, Orange, Yellow, Green, Blue, Indigo, Violet cores

## Competitive Analysis

### Strengths
- **Versatile Coverage**: Two additional STAB types greatly expand offensive options
- **Reliable Sleep**: Near-perfect Hypnosis accuracy enables consistent setup
- **Type Independence**: STAB granted regardless of actual typing
- **Synergistic Design**: Combines offensive and utility benefits effectively

### Weaknesses
- **Move Dependency**: Requires Fairy/Dark moves to utilize STAB benefit
- **Limited Sleep Move**: Only affects Hypnosis, not other sleep moves
- **Opportunity Cost**: Competes with other powerful abilities

### Tier Placement
Most Pokemon with Lunar Eclipse are in higher tiers (3-4), reflecting the ability's power level and the strong base stats of its users.

## Related Abilities

### Solar Flare (Ability #366)
- **Similarity**: Grants Fire-type STAB and has additional effects
- **Difference**: Solar Flare focuses on Fire-type moves and has weather synergy

### Hypnotist (Ability #327)
- **Relationship**: Lunar Eclipse inherits Hypnotist's accuracy boost
- **Difference**: Hypnotist only provides the sleep accuracy benefit

### Adaptability (Ability #91)
- **Similarity**: Both enhance STAB damage
- **Difference**: Adaptability enhances natural STAB to 2x, while Lunar Eclipse grants STAB to specific types

## Technical Notes

- The ability uses function pointers for both STAB checking and accuracy modification
- STAB check returns 1 (true) for Dark and Fairy types, 0 (false) otherwise
- Accuracy modification is multiplicative and applies specifically to Hypnosis
- Implementation follows Elite Redux's modular ability system design

## Thematic Design

Lunar Eclipse reflects the celestial event where the moon passes through Earth's shadow, symbolically representing the duality of light (Fairy) and shadow (Dark) types. The enhanced Hypnosis accuracy ties into the moon's traditional association with sleep and dreams, making this a thematically cohesive ability that bridges offensive and utility functions.


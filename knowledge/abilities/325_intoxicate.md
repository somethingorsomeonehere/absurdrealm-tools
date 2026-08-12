---
id: 325
name: Intoxicate
status: reviewed
character_count: 125
---

# Intoxicate - Ability ID 325

## In-Game Description
Normal-type moves become Poison and Poison gains STAB.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Poison-type moves and grants STAB for Poison-type moves, regardless of the user's typing.

## Mechanics

### Core Effect
- Converts all Normal-type moves used by the Pokemon into Poison-type moves
- Grants Same Type Attack Bonus (STAB) on all Poison-type moves
- The conversion happens before damage calculation
- Converted moves receive the ATE boost flag for additional power

### Implementation Details
- Uses the `ATE_ABILITY(TYPE_POISON)` macro
- Triggers on `onMoveType` callback to convert Normal to Poison
- Triggers on `onStab` callback to provide STAB for Poison moves
- Sets `*ateBoost = TRUE` for converted moves, which may provide additional effects

### Technical Behavior
- **Move Type Conversion**: Normal-type moves become Poison-type
- **STAB Application**: All Poison moves (original and converted) get 1.5x damage
- **Priority**: Conversion happens before type effectiveness calculation
- **Interaction**: Works with all Normal-type moves regardless of category (Physical/Special/Status)

## Pokemon with Intoxicate

### Primary Ability
- Various Poison-type Pokemon (multiple species found in SpeciesList.textproto)

### Innate Ability
- Multiple Pokemon have this as one of their innate abilities
- Often paired with other Poison-themed abilities

### Combination Abilities
- **Sludgy Mix**: Combines Intoxicate + Punk Rock effects

## Strategic Applications

### Offensive Strategy
- Converts typically neutral Normal moves into Poison attacks
- Provides STAB boost to increase damage output
- Excellent for Pokemon with diverse Normal-type movepools
- Synergizes with Poison-type offensive strategies

### Move Synergy
- Works with all Normal-type moves:
  - Physical attacks (Tackle, Body Slam, etc.)
  - Special attacks (Hyper Beam, Swift, etc.)
  - Status moves (converted but may not deal damage)

### Type Coverage
- Converts Normal moves to hit Grass and Fairy types for super-effective damage
- May struggle against Steel and Poison types (resistant/immune)
- Rock and Ground types resist converted moves

## Comparison to Similar Abilities

### Related ATE Abilities
- **Pixilate**: Normal to Fairy (ATE_ABILITY(TYPE_FAIRY))
- **Aerilate**: Normal to Flying (ATE_ABILITY(TYPE_FLYING))
- **Refrigerate**: Normal to Ice (ATE_ABILITY(TYPE_ICE))
- **Galvanize**: Normal to Electric (ATE_ABILITY(TYPE_ELECTRIC))

### Unique Aspects
- Only ability that converts Normal moves to Poison-type
- Particularly valuable for Poison-type Pokemon lacking diverse STAB options
- Strong synergy with Poison-type offensive strategies

## Competitive Viability
- **Tier**: High utility for Poison-type sweepers
- **Best Use**: Pokemon with strong Normal-type coverage moves
- **Synergy**: Pairs well with Poison-type offensive movesets
- **Counter**: Steel-types and Poison-types resist the converted attacks

## Code Implementation
```cpp
constexpr Ability Intoxicate = {
    ATE_ABILITY(TYPE_POISON),
};
```

The ability uses the standard ATE_ABILITY macro which provides:
- `onMoveType` callback for Normal to Poison conversion
- `onStab` callback for STAB on Poison moves
- `*ateBoost = TRUE` flag for converted moves
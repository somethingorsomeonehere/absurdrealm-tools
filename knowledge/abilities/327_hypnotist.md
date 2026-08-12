---
id: 327
name: Hypnotist
status: reviewed
character_count: 129
---

# Hypnotist - Ability ID 327

## In-Game Description
"Hypnosis accuracy is 90% when used by this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Hypnosis' accuracy to 90%. Does not lock to accuracy to 90%, the move still gets affected by accuracy/evasiveness changes.  

## Mechanical Analysis

### Core Effect
- **Trigger**: When the Pokemon uses Hypnosis
- **Calculation**: Hypnosis base accuracy (60%) x 1.5 = 90% accuracy
- **Implementation**: Uses `.onAccuracy` callback with `ACCURACY_MULTIPLICATIVE` priority
- **Scope**: Only affects Hypnosis move, no other sleep-inducing moves

### Technical Implementation
```cpp
constexpr Ability Hypnotist = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(move == MOVE_HYPNOSIS);
        *accuracy *= 1.5;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

### Accuracy Calculations
- **Base Hypnosis**: 60% accuracy
- **With Hypnotist**: 60% x 1.5 = 90% accuracy
- **With Wide Lens**: 90% x 1.1 = 99% accuracy (effective maximum)
- **Against Brightpowder**: 90% x 0.9 = 81% accuracy

## Strategic Applications

### Utility Focus
- **Sleep Support**: Reliable sleep induction for team support
- **Setup Opportunities**: Creates safe setup turns for teammates
- **Disruption**: Consistent sleep pressure against offensive threats
- **Combo Potential**: Works with Dream Eater, Nightmare, or wake-up moves

### Competitive Considerations
- **Niche Role**: Specialized utility rather than general power boost
- **Move Slot Pressure**: Requires dedicating a move slot to Hypnosis
- **Counterplay**: Sleep Clause, Sleep Talk, Lum Berry, Natural Cure
- **Meta Dependency**: Value fluctuates based on sleep move usage trends

## Distribution Analysis

### Notable Carriers
The ability appears on various Pokemon with different roles:
- **Psychic-types**: Natural thematic fit (Ralts line, Drowzee line)
- **Water-types**: Some Poliwag line members as innate ability
- **Support Pokemon**: Utility-focused species with sleep move access

### Common Contexts
- **Innate Ability**: Often appears as a fixed innate rather than selectable
- **Support Builds**: Preferred on bulky support Pokemon
- **Double Battles**: Enhanced value due to multiple sleep targets

## Related Abilities
- **Dreamcatcher**: Works synergistically with sleep strategies
- **Sweet Dreams**: Another sleep-related ability in Elite Redux
- **Bad Dreams**: Punishes sleeping opponents
- **Insomnia**: Defensive counterpart preventing sleep

## Optimization Notes
- **Best Users**: Bulky Pokemon that can survive after inducing sleep
- **Item Synergy**: Wide Lens for near-perfect accuracy, Focus Sash for survival
- **Move Combinations**: Hypnosis + Dream Eater, Hypnosis + setup moves
- **Team Support**: Most effective when supporting sweepers or setup Pokemon

## Historical Context
Hypnotist addresses the traditional unreliability of sleep moves in competitive play. By providing consistent accuracy to Hypnosis, it creates a niche for sleep-based utility strategies without making them overpowered, as the ability only affects one specific move rather than all sleep-inducing attacks.
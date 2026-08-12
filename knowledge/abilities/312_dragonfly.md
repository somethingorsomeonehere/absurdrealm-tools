---
id: 312
name: Dragonfly
status: reviewed
character_count: 254
---

# Dragonfly - Ability ID 312

## In-Game Description
"Adds Dragon type to itself. Avoids Ground attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Dragon to the user's current typing. Retains Dragon typing even upon losing the ability, going away only when switching out. Also gives the user immunity to Ground-type attacks and field effects that require you to be grounded.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dragonfly is a dual-function ability that combines type addition with Ground immunity:

1. **Type Addition**: On entry, adds Dragon type to the Pokemon using the same mechanism as Half Drake ability
2. **Levitation**: Provides complete immunity to Ground-type moves and hazards

### Activation Conditions
- **Type Addition**: Triggers automatically upon switching into battle
- **Ground Immunity**: Passive effect active at all times while the ability is not suppressed

### Technical Implementation
```cpp
constexpr Ability Dragonfly = {
    .onEntry = HalfDrake.onEntry,  // Adds Dragon type
    .breakable = TRUE,             // Can be suppressed
    .levitate = TRUE,              // Ground immunity
};

// Type addition implementation (from HalfDrake)
.onEntry = +[](ON_ENTRY) -> int { 
    return AddBattlerType(battler, TYPE_DRAGON); 
}
```

### Ground-Type Immunity Coverage
- **Moves**: All Ground-type attacks (Earthquake, Earth Power, Bulldoze, etc.)
- **Entry hazards**: Spikes damage
- **Arena effects**: Arena Trap cannot trap levitating Pokemon
- **Interactions**: Overridden by Gravity, Iron Ball, and Ingrain effects

### Type Addition Mechanics
- Adds Dragon type as an additional type (does not replace existing types)
- Creates dual typing for single-type Pokemon
- Creates triple typing for dual-type Pokemon (rare mechanic)
- Dragon typing persists until the Pokemon switches out or the ability is suppressed

### Strategic Implications
**Offensive Benefits:**
- Gains access to Dragon-type STAB on Dragon moves
- May create powerful type combinations (e.g., Ground/Bug/Dragon for Flygon line)

**Defensive Benefits:**
- Complete Ground immunity removes major weakness
- Dragon typing provides useful resistances (Fire, Water, Electric, Grass)

**Potential Drawbacks:**
- Dragon typing adds weakness to Ice, Dragon, and Fairy moves
- Ability can be suppressed by Mold Breaker effects
- Triple typing can create complex type interactions

### Common Users
- **Vibrava**: Ground/Bug to Ground/Bug/Dragon with Ground immunity
- **Flygon**: Ground/Dragon to Already Dragon type, gains Ground immunity

### Competitive Usage Notes
- Excellent for pivoting against Ground-type attacks
- Transforms Flygon into a unique Ground/Dragon that's immune to Ground moves
- Creates type synergy opportunities in team building
- Particularly valuable against Earthquake spam teams

### Counters
- **Ability Suppression**: Mold Breaker, Teravolt, Turboblaze ignore the Ground immunity
- **Status Effects**: Gravity grounds the Pokemon, removing Ground immunity
- **Items**: Iron Ball grounds the holder
- **Moves**: Ingrain removes levitation effect
- **Type Disadvantages**: Ice, Dragon, and Fairy moves become super effective

### Synergies
- **Flying-type moves**: Standard Levitate provides 1.25x boost to Flying moves
- **Ground-type moves**: Can use Ground moves while being immune to them
- **Dragon-type moves**: Gains STAB on Dragon moves
- **Magnet Rise**: Stacks with natural levitation for extended Ground immunity

### Version History
- Added as part of Elite Redux's expanded ability system
- Combines mechanics from Half Drake (type addition) and standard Levitate
- Unique implementation using shared ability components
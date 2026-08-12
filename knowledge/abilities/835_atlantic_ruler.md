---
id: 835
name: Atlantic Ruler
status: reviewed
character_count: 232
---

# Atlantic Ruler - Ability ID 835

## In-Game Description
Aquatic Dweller + Swift Swim.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Water to the user's current typing. Retains Water typing even upon losing the ability, going away only when switching out. Also boosts the power of Water-type moves by 50%. Boosts Speed by 50% during rain.

## Detailed Mechanical Explanation

### Components
- **Aquatic Dweller**: Boosts the power of Water-type moves by 1.5x
- **Swift Swim**: Boosts Speed by 1.5x in rain

### Key Details
- Does NOT add Water type (unlike the base Aquatic ability)
- Both effects are always active when conditions are met
- Water move boost applies regardless of weather
- Speed boost only applies during rain weather
- Breakable: Can be suppressed by Mold Breaker and similar abilities

### Implementation
```c
constexpr Ability AtlanticRuler = {
    .onOffensiveMultiplier = AquaticDweller.onOffensiveMultiplier,
    .onStat = SwiftSwim.onStat,
    .breakable = TRUE,
};
```

## Strategic Value
- Excellent on Water-type Pokemon for STAB synergy
- Rain teams benefit from both offensive and speed boosts
- Non-Water types can use this for surprise Water coverage
- Pairs well with Rain Dance or Drizzle teammates

## Notable Interactions
- Stacks with STAB for 2.25x damage on Water moves from Water-types
- Speed boost in rain can help outspeed threats
- Vulnerable to abilities that ignore other abilities
- Both effects function independently - you get the Water boost even without rain
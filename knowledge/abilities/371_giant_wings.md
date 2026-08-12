---
id: 371
name: Giant Wings
status: reviewed
character_count: 75
---

# Giant Wings - Ability ID 371

## In-Game Description
"Boosts the power of wing, wind or air-based moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Giant Wings boosts the power of all wing, wind, and air-based moves by 30%. 

## Detailed Mechanical Explanation

## Technical Implementation

### Source Code Location
- **File**: `/src/abilities.cc`
- **Lines**: 3846-3851
- **Function**: `GiantWings`

### Implementation Details
```cpp
constexpr Ability GiantWings = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].airBased) MUL(1.3);
        },
};
```

### Mechanic Breakdown
1. **Trigger Condition**: Move has the `air: true` flag (air-based)
2. **Effect**: Multiplies move power by 1.3x (30% increase)
3. **Activation**: Passive boost applied during damage calculation
4. **Scope**: Affects all moves with the air-based property

## Air-Based Moves Enhanced

### Notable Air-Based Moves
- **Wing Attack** (Power 90 to 117)
- **Hurricane** (Power 110 to 143)
- **Air Slash** (Power 90 to 117)
- **Razor Wind** (Power 80 to 104)
- **Fly** (Power 110 to 143)
- **Whirlwind** (Power 60 to 78)
- **Tailwind** (Status move, still boosted)
- **Defog** (Status move, still boosted)
- **Gust** (Power 60 to 78)
- **Aeroblast** (Power 100 to 130)

### Move Categories Enhanced
- **Wind-based attacks**: Hurricane, Whirlwind, Tailwind
- **Wing-based attacks**: Wing Attack, Fly, Brave Bird
- **Air manipulation**: Air Slash, Razor Wind, Gust
- **Utility moves**: Defog, Tailwind (damage multiplier applies to damaging variants)

## Strategic Analysis

### Competitive Applications
- **Flying-type Specialist**: Maximizes damage from core Flying-type moves
- **Weather Control**: Enhanced Tailwind provides both speed and damage benefits
- **Aerial Dominance**: Superior performance in air-based combat scenarios
- **Utility Enhancement**: Boosted utility moves like Defog become more threatening

### Synergistic Moves
- **High Base Power**: Hurricane and Fly become devastating with 1.3x multiplier
- **Multi-hit Potential**: Enhanced Wing Attack for consistent damage
- **Status Integration**: Tailwind provides both utility and combat enhancement
- **Coverage Options**: Air-based moves often have unique targeting properties

### Team Building Considerations
- **Flying-type Core**: Essential for Flying-type focused teams
- **Weather Synergy**: Pairs well with weather setters that boost accuracy
- **Speed Control**: Enhanced Tailwind provides both offensive and utility value
- **Entry Hazard Removal**: Boosted Defog variants become more threatening

## Competitive Viability

### Strengths
1. **Consistent Boost**: 30% damage increase is significant and reliable
2. **Move Variety**: Affects both offensive and utility air-based moves
3. **Type Synergy**: Natural fit for Flying-type Pokemon
4. **Unique Niche**: Specialized enhancement that few abilities provide

### Weaknesses
1. **Limited Move Pool**: Only affects air-based moves, not all Flying-type moves
2. **Type Dependency**: Less useful on non-Flying types with limited air-based options
3. **Weather Vulnerability**: Some air-based moves have accuracy issues
4. **Niche Application**: Specific to air-based combat scenarios

### Tier Assessment: Medium
- **Reasoning**: Provides significant power boost to a specific subset of moves. Excellent for specialized Flying-type builds but limited in general application. Most effective when paired with Pokemon that have extensive air-based movesets.

## Notable Pokemon with Giant Wings

### Primary Users (Regular Ability)
- Large Flying-type Pokemon with extensive air-based movesets
- Pokemon with access to Hurricane, Wing Attack, and utility air moves
- Particularly effective on Pokemon with:
  - High Attack/Special Attack stats
  - Natural Flying typing
  - Access to weather-setting moves

### Innate Users
- Several Pokemon have this as an innate ability
- Provides consistent enhancement to their signature air-based attacks
- Synergizes well with other Flying-type abilities

## Comparisons with Related Abilities

### Similar Type-Boosting Abilities
- **Levitate**: Provides 1.25x Flying-type boost vs Giant Wings' 1.3x air-based boost
- **Airborne**: Boosts Flying-type moves by 1.3x for allies vs Giant Wings' self-boost
- **Gale Wings**: Priority on Flying moves vs Giant Wings' power boost
- **Aerilate**: Converts Normal moves to Flying vs Giant Wings' direct enhancement

### Power Multiplier Comparisons
- **Iron Fist**: 1.3x boost to punching moves (similar concept)
- **Strong Jaw**: 1.3x boost to biting moves (parallel enhancement)
- **Mega Launcher**: 1.3x boost to pulse/aura moves (equivalent multiplier)

## Interaction Notes

### Battle Mechanics
- **Weather Interactions**: Hurricane gains perfect accuracy in rain while boosted
- **Multi-target**: Boost applies to each target hit by multi-target air moves
- **Critical Hits**: Boost applies before critical hit calculation
- **STAB Stacking**: Combines multiplicatively with Same Type Attack Bonus

### Edge Cases
- **Copycat/Mirror Move**: Boost applies when copying air-based moves
- **Metronome**: Can randomly select and boost air-based moves
- **Skill Swap**: Ability transfers with its boosting properties
- **Mold Breaker**: Cannot be bypassed by ability-ignoring effects

### Notable Interactions
- **Rain Dance + Hurricane**: Perfect accuracy Hurricane with 1.3x power boost
- **Tailwind**: Enhanced speed control with potential damage applications
- **Defog**: Utility move becomes more threatening with power boost
- **Multi-hit Moves**: Each hit receives the full 1.3x multiplier

## Conclusion

Giant Wings represents a specialized but powerful enhancement ability that maximizes the potential of air-based combat. While its application is narrower than general type-boosting abilities, it provides superior power multiplication (1.3x vs typical 1.25x) for its specific niche. The ability excels on Pokemon with extensive air-based movesets and integrates well with weather-based strategies.

The ability's design rewards specialization in aerial combat while maintaining relevance through both offensive and utility applications. For Pokemon that can effectively leverage multiple air-based moves, Giant Wings provides substantial value in competitive environments where maximizing damage output from signature moves is crucial.

This ability is particularly valuable in formats that emphasize type specialization and weather control, where the combination of enhanced power and strategic utility creates significant advantages in aerial combat scenarios.


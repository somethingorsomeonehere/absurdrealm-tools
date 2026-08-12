---
id: 340
name: Fatal Precision
status: reviewed
character_count: 72
---

# Fatal Precision - Ability ID 340

## In-Game Description
"Super-effective moves never miss and always crit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Super-effective damaging moves never miss and always land critical hits. 

## Detailed Mechanical Explanation

### Overview

Fatal Precision is an Elite Redux-exclusive ability that ensures super-effective damaging moves never miss and always score critical hits. This ability transforms Pokemon with diverse move coverage into highly reliable offensive threats, eliminating the risk-reward balance typically associated with powerful but less accurate moves.

## Mechanics

### Core Functionality

The ability provides two distinct effects when using super-effective damaging moves:

1. **Guaranteed Accuracy**: Super-effective moves automatically hit, bypassing all accuracy checks
2. **Guaranteed Critical Hits**: Super-effective moves always land critical hits

### Technical Implementation

The ability is implemented through two callback functions in `src/abilities.cc`:

#### Accuracy Component (Lines 3600-3604)
```cpp
.onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
    CHECK_NOT(IS_MOVE_STATUS(move))
    CHECK(CalcTypeEffectivenessMultiplier(move, moveType, battler, target, TRUE) >= UQ_4_12(2.0))
    return ACCURACY_HITS_IF_POSSIBLE;
},
```

#### Critical Hit Component (Lines 3605-3608)
```cpp
.onCrit = +[](ON_CRIT) -> int {
    CHECK(typeEffectiveness >= UQ_4_12(2.0))
    return ALWAYS_CRIT;
},
```

### Super-Effective Determination

The ability uses `CalcTypeEffectivenessMultiplier()` to determine if a move is super-effective. The threshold is `UQ_4_12(2.0)`, which represents a 2.0x type effectiveness multiplier (standard super-effective damage).

### Restrictions

- **Status Move Exclusion**: The ability explicitly checks `IS_MOVE_STATUS(move)` and does not activate for status moves
- **Type Effectiveness Requirement**: Must achieve at least 2.0x type effectiveness to trigger
- **Damage Moves Only**: Only affects moves that deal damage

## Strategic Applications

### Offensive Versatility
Fatal Precision rewards Pokemon with diverse move coverage, making them extremely reliable against their intended targets. This is particularly valuable for:
- **Mixed Attackers**: Pokemon that can threaten both physical and special walls
- **Coverage Specialists**: Pokemon with moves covering many different types
- **Revenge Killers**: Ensuring key KOs against faster threats

### Synergy Opportunities
The ability works excellently with:
- **Choice Items**: Guaranteeing the selected move hits and crits when super-effective
- **High Base Power Moves**: Critical hits on powerful moves create massive damage output
- **Multi-hit Moves**: Each hit that's super-effective will crit individually

### Competitive Applications
In competitive play, Fatal Precision provides:
- **Reliability**: Eliminates the frustration of missing crucial super-effective moves
- **Pressure**: Forces opponents to avoid type disadvantages entirely
- **Breaking Power**: Critical hits help break through defensive investment

## Pokemon with Fatal Precision

Based on the species data, Fatal Precision appears on a diverse range of Pokemon, including:

### Notable Users
- **Genesect Forms**: Multiple Genesect variants have this as a regular ability
- **Fighting-type Specialists**: Several Fighting-types use this for coverage moves
- **Mixed Attackers**: Various dual-typed Pokemon that benefit from coverage reliability
- **Legendary/Mythical Pokemon**: Some powerful Pokemon have this as an innate ability

### Distribution Pattern
The ability appears both as:
- **Regular Abilities**: Changeable through normal ability mechanics
- **Innate Abilities**: Permanent passive abilities that cannot be changed

## Interactions and Edge Cases

### Multi-Type Effectiveness
For moves that hit multiple types (such as against dual-typed Pokemon), the ability triggers if the combined effectiveness reaches 2.0x or higher.

### Ability Suppression
Fatal Precision can be suppressed by abilities like:
- **Mold Breaker**: Ignores the ability entirely
- **Neutralizing Gas**: Temporarily disables the ability

### Move Interaction Examples
- **Hidden Power**: Can trigger if super-effective against the target
- **Weather Ball**: Effectiveness depends on the weather-modified type
- **Flying Press**: Calculated against both Fighting and Flying type effectiveness

## Related Abilities

### Final Blow (Ability #425)
Final Blow combines Fatal Precision's effects with Unseen Fist, as seen in the code:
```cpp
constexpr Ability FinalBlow = {
    .onAccuracy = FatalPrecision.onAccuracy,
    .onCrit = FatalPrecision.onCrit,
};
```

### Synergistic Abilities
- **Sniper**: Multiplies the damage of Fatal Precision's guaranteed critical hits
- **Tough Claws**: Boosts contact moves that benefit from guaranteed crits
- **Sheer Force**: Can work alongside if the move doesn't have secondary effects

## Competitive Impact

### Tier Considerations
Fatal Precision significantly raises the competitive viability of Pokemon that possess it, particularly those with:
- Good offensive stats
- Access to diverse move coverage
- Strategic positioning in team compositions

### Counterplay
Opponents facing Fatal Precision users must:
- Avoid unfavorable type matchups entirely
- Use Pokemon that resist the user's coverage moves
- Employ priority moves or speed control
- Consider abilities that can suppress or bypass Fatal Precision

## Conclusion

Fatal Precision represents a powerful offensive ability that rewards strategic team building and move selection. By guaranteeing both accuracy and critical hits on super-effective moves, it transforms reliable coverage into devastating offensive pressure. The ability's implementation in Elite Redux showcases sophisticated battle mechanics that maintain competitive depth while providing exciting new tactical options.

The ability's code implementation is clean and efficient, with clear checks for move type and effectiveness that ensure it only activates under the intended conditions. Its distribution across various Pokemon types and roles makes it a versatile tool in both casual and competitive play.
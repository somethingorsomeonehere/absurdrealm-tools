---
id: 357
name: Molten Down
status: reviewed
character_count: 89
---

# Molten Down - Ability ID 357

## In-Game Description
"Fire-type moves deal super effective damage to Rock-types."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Molten Down makes Fire-type moves super effective against Rock-types instead of resisted. 

## Detailed Mechanical Explanation

### Overview

**Molten Down** is a powerful type-effectiveness modifying ability that fundamentally changes the Fire vs Rock type interaction. Instead of Fire-type moves being resisted by Rock-types (dealing 0.5x damage), they become super effective, dealing 2.0x damage.

## Code Implementation

### Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: 3765-3772
- **Enum Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityEnum.proto` (Line ~357)

### Technical Implementation

```cpp
constexpr Ability MoltenDown = {
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        CHECK(moveType == TYPE_FIRE)
        CHECK(defType == TYPE_ROCK)
        *mod = UQ_4_12(2.0);
        return TRUE;
    },
};
```

### Mechanism Analysis

1. **Trigger Condition**: Activates when a Fire-type move is used against a Rock-type Pokemon
2. **Effect**: Sets type effectiveness modifier to 2.0x (super effective)
3. **Priority**: Applied during type effectiveness calculation phase
4. **Format**: Uses UQ_4_12(2.0) fixed-point representation for 2.0x multiplier

## Strategic Applications

### Offensive Advantages
- **Wall Breaking**: Fire-types can now effectively threaten Rock-type walls like Tyranitar, Terrakion, and Aerodactyl
- **Coverage Enhancement**: Provides Fire-types with unexpected super effective coverage
- **Meta Disruption**: Forces Rock-type users to reconsider their defensive strategies

### Team Building Implications
- **Fire-type Viability**: Significantly increases the competitive viability of Fire-type Pokemon
- **Rock-type Counterplay**: Rock-types lose a key defensive matchup
- **Strategic Surprise**: Opponents may not expect super effective Fire moves against Rock-types

## Competitive Analysis

### Strengths
- **Game-Changing**: Completely reverses a traditionally poor matchup
- **Widespread Impact**: Affects many common competitive Pokemon
- **Unpredictable**: Creates surprise factor in battles
- **Synergy Potential**: Works well with other Fire-boosting abilities and items

### Limitations
- **Specific Scope**: Only affects Fire vs Rock interactions
- **No Defensive Benefit**: Doesn't improve Fire-type's defensive capabilities
- **Predictable Once Known**: Effect becomes expected after first use

### Comparison to Similar Abilities
- **Scrappy**: Allows Normal/Fighting to hit Ghost (0x -> 1x)
- **Corrosion**: Allows Poison to hit Steel super effectively (0.5x -> 2x)
- **Overcharge**: Allows Electric to hit Electric super effectively (0.5x -> 2x)

## Pokemon Distribution

### Primary Ability Users
The following Pokemon have Molten Down as a regular (changeable) ability:

1. **Charizard variants** - Enhanced offensive presence
2. **Magmar line** - Significant competitive boost
3. **Larvesta/Volcarona variants** - Already powerful, now more versatile
4. **Heatran variants** - Dual Fire/Steel typing with Rock coverage
5. **Various Fire-type legendaries** - Primal Groudon, other forms

### Innate Ability Users
Many Pokemon have Molten Down as an innate (permanent) ability:

1. **Slugma evolution line** - Core identity enhancement
2. **Tyranitar Redux line** - Interesting dual Fire/Rock typing synergy
3. **Various mixed-type Pokemon** - Provides Fire-type moves with Rock coverage

## Battle Interactions

### Type Chart Modification
- **Normal Interaction**: Fire vs Rock = 0.5x damage (resisted)
- **With Molten Down**: Fire vs Rock = 2.0x damage (super effective)
- **Net Change**: 4x effective damage increase (0.5x -> 2.0x)

### Calculation Priority
1. Base type effectiveness calculated
2. Ability modifiers applied (Molten Down triggers here)
3. Item modifiers applied
4. Final damage calculation

### Stacking Interactions
- **With STAB**: 2.0x (STAB) x 2.0x (Molten Down) = 4.0x total multiplier
- **With Items**: Can stack with Choice items, Life Orb, etc.
- **With Weather**: Sun boosts combine multiplicatively

## Counters and Counterplay

### Direct Counters
- **Water-types**: Still resist Fire moves and can threaten back
- **Dragon-types**: Neutral to Fire, often have good bulk
- **Flash Fire users**: Immune to Fire moves entirely
- **Ability suppression**: Gastro Acid, Mold Breaker variants

### Strategic Counterplay
- **Priority moves**: Bypass ability with faster attacks
- **Status moves**: Don't trigger type effectiveness
- **Substitute**: Blocks direct damage
- **Defensive positioning**: Switch to appropriate resists/immunities

## Competitive Meta Impact

### Tier Impact
- **Rock-types**: Generally drop in usage/effectiveness
- **Fire-types**: Significant viability increase
- **Water-types**: Become more valuable as Fire checks
- **Steel-types**: Maintain importance as Fire resists

### Team Building Considerations
- **Fire-type Inclusion**: More teams consider Fire-types viable
- **Rock-type Usage**: Requires more careful team support
- **Balance Shifts**: Meta adapts to new type interactions

## Related Abilities

### Similar Type-Effectiveness Modifiers
- **Corrosion** (#212): Poison hits Steel super effectively
- **Overcharge** (#349): Electric hits Electric super effectively  
- **Scrappy** (#113): Normal/Fighting hits Ghost neutrally

### Synergistic Abilities
- **Drought**: Boosts Fire-type moves further
- **Solar Power**: Increases Special Attack in sun
- **Flash Fire**: Provides Fire immunity and power boost

## Technical Notes

### Code Structure
- Uses standard `onTypeEffectiveness` callback
- Employs CHECK macros for condition validation
- Modifies effectiveness through direct assignment to `*mod`
- Returns TRUE to confirm modification applied

### Performance Considerations
- Minimal computational overhead
- Only triggers on specific type combinations
- No persistent state or complex calculations required

## Conclusion

Molten Down represents one of the most impactful type-effectiveness modifying abilities in Elite Redux. By fundamentally changing the Fire vs Rock matchup from resisted to super effective, it creates new strategic possibilities, enhances Fire-type viability, and forces adaptation in competitive play. Its straightforward implementation belies its significant impact on the battle system and competitive meta.

The ability exemplifies Elite Redux's approach to expanding strategic depth through innovative ability design while maintaining clear, understandable mechanics that players can learn and adapt to.


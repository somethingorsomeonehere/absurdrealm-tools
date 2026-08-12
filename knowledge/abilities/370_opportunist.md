---
id: 370
name: Opportunist
status: reviewed
character_count: 77
---

# Opportunist - Ability ID 370

## In-Game Description
"+1 priority vs foes below 1/2 max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to all moves when targeting opponents with 50% HP or less. 

## Detailed Mechanical Explanation

## Technical Implementation

### Source Code Location
- **File**: `/src/abilities.cc`
- **Lines**: 3839-3844
- **Function**: `Opportunist`

### Implementation Details
```cpp
constexpr Ability Opportunist = {
    .onPriority = +[](ON_PRIORITY) -> int {
        CHECK(gBattleMons[target].hp <= gBattleMons[target].maxHP / 2)
        return 1;
    },
};
```

### Mechanic Breakdown
1. **Trigger Condition**: Target Pokemon's current HP <= 50% of maximum HP
2. **Effect**: Adds +1 priority to all moves used against qualifying targets
3. **Activation**: Passive check during priority calculation phase
4. **Scope**: Only affects moves targeting Pokemon below half health

## Strategic Analysis

### Competitive Applications
- **Revenge Killer**: Excellent for finishing off weakened opponents before they can retaliate
- **Speed Control**: Bypasses Speed differences when targeting injured Pokemon
- **Setup Disruption**: Can interrupt opponents trying to set up after taking damage
- **Pressure Application**: Forces opponents to play more cautiously around 50% HP threshold

### Synergistic Moves
- **High Power Moves**: Maximizes knockout potential with priority boost
- **Multi-hit Moves**: Can secure KOs through Sturdy/Focus Sash with priority
- **Coverage Moves**: Ensures key matchups are won regardless of Speed tiers
- **Status Moves**: Priority healing/status prevention against weakened threats

### Team Building Considerations
- **Entry Hazard Support**: Damage accumulation helps trigger ability condition
- **Pivot Support**: Safe switching into weakened threats
- **Speed Tier Flexibility**: Less reliant on Speed investment for finishing
- **Role Compression**: Functions as both revenge killer and late-game cleaner

## Competitive Viability

### Strengths
1. **Consistent Activation**: 50% HP threshold is easily reached in competitive play
2. **Unpredictable Priority**: Opponents cannot predict when priority will activate
3. **Speed Independence**: Effective regardless of base Speed stat
4. **Versatile Application**: Works with any offensive moveset

### Weaknesses
1. **Conditional Nature**: No benefit against full-health opponents
2. **Prediction Dependence**: Requires accurate HP assessment
3. **Setup Vulnerability**: Doesn't help with initial positioning
4. **Priority Competition**: Competes with natural priority moves

### Tier Assessment: Medium
- **Reasoning**: Highly situational but powerful when active. Strong in revenge killing scenarios but limited in general application. Most effective in formats with consistent damage accumulation.

## Notable Pokemon with Opportunist

### Primary Users (Regular Ability)
- Various Pokemon across different types and roles
- Particularly effective on Pokemon with:
  - High Attack/Special Attack stats
  - Good coverage moves
  - Natural bulk for switching opportunities

### Innate Users
- Several Pokemon have this as an innate ability
- Provides constant pressure throughout the battle
- Synergizes with other offensive abilities

## Comparisons with Related Abilities

### Similar Priority Abilities
- **Quick Draw**: Random priority boost vs Opportunist's conditional guarantee
- **Gale Wings**: Type-specific priority vs HP-conditional priority
- **Prankster**: Status-only priority vs all-move priority against injured targets

### Strategic Alternatives
- **Moxie**: Snowball potential after KOs
- **Adaptability**: Consistent power boost vs situational priority
- **Life Orb**: Immediate power increase vs strategic positioning advantage

## Interaction Notes

### Battle Mechanics
- **Priority Stacking**: Combines with natural move priority (e.g., Quick Attack becomes +2)
- **Speed Ties**: Still subject to Speed tie resolution at same priority level
- **Multi-target**: Each target's HP is checked individually in doubles/triples
- **Accuracy Check**: Priority applies even if move misses (calculated before accuracy)

### Edge Cases
- **Substitute**: Checks actual HP, not Substitute HP
- **Disguise**: Triggers after Disguise breaks based on remaining HP
- **Focus Sash/Sturdy**: Extremely effective for finishing through these abilities
- **Healing**: Effect is recalculated each turn based on current HP

## Conclusion

Opportunist represents a unique approach to priority manipulation, rewarding players for accurate damage calculation and positioning. While situational, its ability to secure crucial knockouts makes it a valuable tool in the right hands. The ability excels in revenge killing scenarios and provides consistent late-game pressure, making it particularly effective in longer battles where HP management becomes critical.

The ability's design encourages aggressive play against weakened opponents while maintaining strategic depth through its conditional nature. For Pokemon that can effectively leverage this ability, it provides significant value in competitive environments where securing knockouts at the right moment can determine battle outcomes.


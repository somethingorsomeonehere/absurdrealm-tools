---
id: 162
name: Victory Star
status: reviewed
character_count: 83
---

# Victory Star - Ability ID 162

## In-Game Description
"Gives 1.2x accuracy boost to its own and its allies' moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's and their ally's accuracy by 1.2x when active in a double battle.

## Detailed Mechanical Explanation

### Implementation Details
```cpp
constexpr Ability VictoryStar = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        *accuracy *= 1.2;
        return ACCURACY_MULTIPLICATIVE;
    },
    .onAccuracyFor = APPLY_ON_ALLY,
};
```

### Key Properties
- **Accuracy Multiplier**: 1.2x (20% boost)
- **Application**: `APPLY_ON_ALLY` - affects both the user and allies in multi battles
- **Priority Type**: `ACCURACY_MULTIPLICATIVE` - multiplies with other accuracy modifiers
- **Breakable**: No (not marked as breakable)
- **Suppressible**: Yes (can be suppressed by abilities like Gastro Acid)

## Pokemon with Victory Star

Victory Star appears as both a regular ability and innate ability on several Pokemon:
- **Starmie**: Has Victory Star as an innate ability (alongside Natural Cure and Mystic Power)
- Multiple other Pokemon have it as either regular or innate abilities

## Comparison with Other Accuracy Abilities

| Ability | Accuracy Boost | Scope | Conditions |
|---------|---------------|--------|------------|
| Victory Star | 1.2x | Self + Allies | Always active |
| Compound Eyes | 1.3x | Self only | Always active |
| Keen Eye | 1.2x | Self only | Always active |
| Illuminate | 1.2x | Self only | Always active |
| No Guard | Perfect | Both sides | Bi-directional |

## Strategic Usage

### Advantages
- **Consistent reliability**: Makes 80% accuracy moves hit 96% of the time
- **Team support**: Benefits allies in double/multi battles
- **No conditions**: Unlike weather-based accuracy abilities, always works
- **Stacks multiplicatively**: Combines well with other accuracy boosts

### Best Move Synergies
- **Focus Blast**: 70% to 84% accuracy
- **Hydro Pump**: 80% to 96% accuracy  
- **Fire Blast**: Usually 85% to effectively 100% (capped)
- **Thunder**: 70% to 84% accuracy
- **Blizzard**: 70% to 84% accuracy (outside hail)

### Team Building
- Excellent on pivot Pokemon that can switch in allies
- Valuable in double battles for supporting partner
- Particularly useful with high-power, low-accuracy moves
- Works well with Choice item users who need consistent hits

## Technical Notes

- **Calculation**: Final accuracy = Move accuracy x 1.2 x other modifiers
- **Rounding**: Uses standard Pokemon accuracy calculation (out of 100)
- **Weather interaction**: Stacks with weather effects (Thunder in rain, Blizzard in hail)
- **Ability interaction**: Can be suppressed but not broken by moves like Brick Break

## Balance Considerations

Victory Star provides meaningful but not overwhelming accuracy improvement. The 20% boost is significant enough to make unreliable moves usable while not being so powerful as to make every move guaranteed to hit. The ally support aspect adds strategic depth in multi battles without being overpowered in singles.
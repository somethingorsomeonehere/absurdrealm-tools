---
id: 390
name: Mighty Horn
status: reviewed
character_count: 68
---

# Mighty Horn - Ability ID 390

## In-Game Description
"Boosts the power of horn and drill-based moves by 30%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mighty Horn boosts the power of horn and drill-based attacks by 30%.

## Detailed Mechanical Explanation

### Overview

**Mighty Horn** is a specialized offensive ability that enhances horn and drill-based attacks, providing a significant damage boost to moves that utilize these piercing appendages. This ability embodies the raw, primal power of creatures with prominent horns and drilling capabilities.

## Technical Implementation

### Location in Codebase
- **Primary Implementation**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 4028-4033)
- **Ability Registration**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (line 9234)
- **Proto Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityList.textproto` (lines 1960-1963)

### Code Analysis

```cpp
constexpr Ability MightyHorn = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].hornBased) MUL(1.3);
        },
};
```

The ability implements a simple but effective damage multiplier:
- **Trigger**: Activates when using moves with the `hornBased` flag
- **Effect**: Applies a 1.3x (30%) damage multiplier to qualifying moves
- **Timing**: Applied during offensive multiplier calculation phase

### Move Compatibility

Horn-based moves in Elite Redux are flagged with `horn: true` in the MoveList.textproto. Compatible moves include:

#### Core Horn Moves
- **Horn Attack** (MOVE_HORN_ATTACK) - 85 BP Normal-type physical move with high crit rate
- **Horn Drill** (MOVE_HORN_DRILL) - 95 BP Normal-type move that ignores abilities and stat changes
- **Furious Horns** - Multi-hit Normal-type move (2-5 hits, 25 BP each)

#### Drill-Based Moves
- **Drill Peck** (MOVE_DRILL_PECK) - 90 BP Flying-type move with high crit rate
- **Megahorn** - 120 BP Bug-type move that ignores stat changes
- **Various drill moves** across different types

#### Specialized Horn Moves
- **Steel Horn** - 80 BP Steel-type move that ignores abilities
- **Electric Horn** - 80 BP Electric-type move with paralysis chance
- **Water Horn** - 80 BP Water-type move with flinch chance
- **Fire Horn variants** - Various Fire-type horn moves with burn chances
- **Dragon Horn** - 80 BP Dragon-type move with bleed chance
- **Ice Horn** - 80 BP Ice-type move with defense reduction
- **Fighting Horn** - 85 BP Fighting-type move with high crit rate

## Strategic Analysis

### Offensive Potential
- **Damage Boost**: 30% increase to horn-based moves provides substantial offensive power
- **Type Coverage**: Horn moves span multiple types, offering good coverage options
- **Critical Hit Synergy**: Many horn moves have naturally high critical hit rates, amplifying damage potential
- **Stat Ignoring**: Several horn moves bypass stat changes and abilities, making them reliable

### Defensive Considerations
- **No Defensive Utility**: Mighty Horn provides no defensive benefits
- **Movepool Dependent**: Effectiveness relies entirely on access to horn-based moves
- **Predictable**: Opponents can anticipate the strategy and prepare counters

### Competitive Viability
**Tier**: Medium
- **Strengths**: Reliable damage boost, good move variety, synergy with high crit moves
- **Weaknesses**: Limited to specific move types, no utility beyond damage
- **Niche**: Effective on Pokemon with naturally good horn move access

## Related Abilities

### Abilities That Share MightyHorn's Implementation
Several abilities in Elite Redux reference `MightyHorn.onOffensiveMultiplier`, indicating they provide the same 30% boost to horn-based moves:

1. **Hunter's Horn** (Ability #464) - Combines soul-eating with horn enhancement
2. **Unicorn** (Ability #647) - Fairy-type moves become horn-based + horn boost
3. **Energized Horns** (Ability #751) - Horn boost + physical horn moves become special
4. **Venom Crown** (Ability #unknown) - Combines poison effects with horn enhancement
5. **Impaler** (Ability #unknown) - Horn moves can cause bleeding + horn boost

### Complementary Abilities
- **Keen Edge**: Boosts moves with cutting properties (some overlap with horn moves)
- **Sheer Force**: Removes secondary effects but boosts power
- **Strong Jaw**: Enhances biting moves (different physical appendage focus)

## Competitive Applications

### Team Building Considerations
1. **Physical Attackers**: Best suited for physical attackers with high Attack stats
2. **Critical Hit Builds**: Synergizes well with critical hit-focused strategies
3. **Multi-Type Coverage**: Horn moves provide access to multiple offensive types
4. **Wallbreaking**: The 30% boost helps break through defensive walls

### Counters and Limitations
1. **Rocky Helmet/Iron Barbs**: Contact moves trigger damage
2. **Intimidate**: Reduces physical attack power
3. **Defensive Typing**: Steel and Rock types resist many horn moves
4. **Protection Moves**: Some horn moves are blocked by Protect variants

### Setup Synergy
- **Swords Dance**: Multiplies the enhanced horn move damage
- **Choice Band**: Stacks multiplicatively with Mighty Horn
- **Critical Hit Boosts**: Enhances the natural crit rate of horn moves

## Pokemon Distribution

While the specific distribution isn't detailed in the implementation files, Mighty Horn would be thematically appropriate for:
- Pokemon with prominent horns (Tauros, Rhyhorn line, etc.)
- Drill-based Pokemon (Drilbur line, etc.)
- Beetle and insect Pokemon with horn-like protrusions

## Version History

- **Elite Redux**: Introduced as ability #390
- **Current Status**: Active and functional as of analysis date
- **Balance**: 30% multiplier provides meaningful but not overpowered enhancement

## Technical Notes

- **Battle AI**: The ability is recognized by battle AI for move selection optimization
- **Display**: Appears in Pokemon summary screens with appropriate boost indicators
- **Compatibility**: Works with all horn-flagged moves regardless of type or power
- **Stacking**: Multiplies with other damage modifiers (items, stat boosts, etc.)


## Summary

Mighty Horn represents a focused, thematic ability that rewards Pokemon for utilizing their natural horn and drill-based attacks. While not game-breaking, it provides a solid 30% damage boost that can turn mid-power horn moves into formidable offensive tools. The ability's medium competitive tier reflects its reliability within its niche while acknowledging its limited scope compared to more versatile abilities.

The implementation is clean and straightforward, making it easy to understand and predict in battle. For players building around horn-based Pokemon, Mighty Horn offers a reliable way to enhance their signature moves without being overpowered or complex to manage.
---
id: 270
name: Pyromancy
status: reviewed
character_count: 91
---

# Pyromancy - Ability ID 270

## In-Game Description
"Moves inflict burn 5x as often."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Pyromancy multiplies the burn chance of all moves by 5x. Does not interact with Flame Body.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Effect**: Multiplies the burn chance (`effectChance`) of all moves with `MOVE_EFFECT_BURN` by 5
- **Implementation**: Uses `onModifyEffectChance` hook to detect burn effects and apply 5x multiplier
- **Scope**: Affects all moves that can inflict burn, regardless of move type or category

### Practical Applications
**Common Burn Chances:**
- 10% burn chance to 50% burn chance (e.g., many Fire-type attacks)
- 20% burn chance to 100% burn chance (guaranteed)
- 30% burn chance to 100% burn chance (guaranteed, capped at 100%)

**Strategic Value:**
- Transforms unreliable burn effects into consistent status application
- Particularly powerful with moves that have moderate burn chances (10-20%)
- Makes burn-based strategies significantly more viable
- Synergizes well with burn damage and burn-based abilities

### Technical Implementation
```cpp
constexpr Ability Pyromancy = {
    .onModifyEffectChance =
        +[](ON_MODIFY_EFFECT_CHANCE) {
            if (moveEffect == MOVE_EFFECT_BURN) *effectChance *= 5;
        },
};
```

### Interactions
- **Caps at 100%**: Burn chances cannot exceed 100% even with the 5x multiplier
- **Works with all burn sources**: Affects primary effects, secondary effects, and ability-triggered burns
- **Stacks with other effects**: Works alongside other burn chance modifiers
- **No immunity bypass**: Still cannot burn Fire-types or Pokemon with burn immunity

### Competitive Considerations
- **Offensive utility**: Makes burn a reliable damage-over-time option
- **Defensive utility**: Burn reduces physical attack power by 50%
- **Meta impact**: Significantly improves viability of burn-focused movesets
- **Counterplay**: Fire-types and Guts ability users are natural counters
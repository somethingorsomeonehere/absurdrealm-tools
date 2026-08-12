---
id: 850
name: Lucky Wings
status: reviewed
character_count: 143
---

# Lucky Wings - Ability ID 850

## In-Game Description
Serene Grace + Giant Wings.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles the activation chance of the user's secondary effects on their attacks. Boosts the power of all wing, wind, and air-based moves by 30%.

## Detailed Mechanical Explanation

### Implementation Analysis

Lucky Wings is implemented as a combination ability in `src/abilities.cc`:

```cpp
constexpr Ability LuckyWings = {
    .onOffensiveMultiplier = GiantWings.onOffensiveMultiplier,
    .onModifyEffectChance = SereneGrace.onModifyEffectChance,
};
```

### Component Abilities

**Serene Grace Component:**
- **Effect**: Doubles the activation chance of move secondary effects
- **Implementation**: `onModifyEffectChance = +[](ON_MODIFY_EFFECT_CHANCE) { *effectChance *= 2; }`
- **Trigger**: Any move with a secondary effect (status conditions, stat changes, etc.)

**Giant Wings Component:**
- **Effect**: 30% power boost to air-based moves
- **Implementation**: `onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) { if (gBattleMoves[move].airBased) MUL(1.3); }`
- **Trigger**: Moves flagged as airBased in the move data

## Mechanical Details

1. **Effect Stacking**: Both components work independently and simultaneously
2. **Move Classification**: Air-based moves include moves like Fly, Aeroblast, Air Slash, Hurricane, etc.
3. **Secondary Effect Examples**: 
   - Air Slash's 30% flinch chance becomes 60%
   - Hurricane's 30% confusion chance becomes 60%
   - The power of both moves is also boosted by 30%

## Strategic Usage

Lucky Wings is particularly effective on Pokemon that:
- Have access to air-based moves with secondary effects
- Can benefit from both offensive power and utility
- Are naturally fast enough to capitalize on increased flinch chances

## Code Location
- Main implementation: `src/abilities.cc` (LuckyWings definition)
- Ability registry: `src/abilities.cc` (abilities array)
- Protobuf definition: `proto/AbilityList.textproto`
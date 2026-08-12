---
id: 608
name: Toxic Chain
status: reviewed
character_count: 119
---

# Toxic Chain - Ability ID 608

## In-Game Description
"30% chance to inflict badly poison on attacking moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user has a 30% to badly poison the target after landing any move. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation

### Core Mechanics
- **Ability ID**: 608 (ABILITY_TOXIC_CHAIN)
- **Trigger**: On attacking (onAttacker callback)
- **Activation Rate**: 30% chance per hit
- **Status Effect**: Badly Poison (MOVE_EFFECT_TOXIC)
- **Implementation**: Located in `src/abilities.cc` lines 6404-6412

### Technical Implementation
```cpp
constexpr Ability ToxicChain = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBePoisoned(battler, target, MOVE_NONE))
        CHECK(Random() % 100 < 30)

        return AbilityStatusEffect(MOVE_EFFECT_TOXIC);
    },
};
```

### Condition Checks
1. **ShouldApplyOnHitAffect(target)**: Standard check for secondary effects
2. **CanBePoisoned(battler, target, MOVE_NONE)**: Verifies target can be poisoned
3. **Random() % 100 < 30**: 30% activation probability

### Status Effect Details
- **MOVE_EFFECT_TOXIC**: Inflicts badly poison status
- **Badly Poison**: Damage increases each turn (1/16, 2/16, 3/16, etc.)
- **Different from regular poison**: Standard poison deals consistent 1/8 HP damage

### Strategic Applications
- **Contact Move Synergy**: Works with all attacking moves that hit the target
- **Multi-Hit Moves**: Each hit has independent 30% chance to poison
- **Type Coverage**: Provides utility against non-Poison/Steel types
- **Late Game Power**: Badly poison becomes increasingly threatening over time

### Interactions and Limitations
- **Immunity**: Poison-type and Steel-type Pokemon are immune
- **Abilities**: Blocked by abilities like Immunity, Poison Heal, etc.
- **Substitute**: May be blocked if target is behind substitute
- **Secondary Effect**: Only triggers on moves that successfully deal damage

### Comparison to Similar Abilities
- **Poison Touch**: 30% regular poison vs 30% badly poison
- **Effect Spore**: Multiple possible effects vs guaranteed poison type
- **Toxic Boost**: Activated by being poisoned vs inflicting poison

### Battle Applications
1. **Stall Teams**: Excellent for wearing down bulky opponents
2. **Hit-and-Run**: Apply poison then switch to preserve advantage
3. **Multi-Hit Users**: Pokemon with moves like Bullet Seed maximize chances
4. **Late Game Closer**: Badly poison can finish weakened opponents
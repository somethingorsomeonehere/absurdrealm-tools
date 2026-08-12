---
id: 852
name: Envenom
status: reviewed
character_count: 113
---

# Envenom - Ability ID 852

## In-Game Description
Moves have a 30% chance to poison the target.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user has a 30% to poison the target after landing any move. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation

### Implementation Details

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 8613-8621

### Mechanics Analysis

#### Core Function
```cpp
constexpr Ability Envenom = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBePoisoned(battler, target, MOVE_NONE))
        CHECK(Random() % 100 < 30)

        return AbilityStatusEffect(MOVE_EFFECT_POISON);
    },
};
```

#### Activation Conditions
1. **ShouldApplyOnHitAffect(target)**: Basic check for hit-based effects
2. **CanBePoisoned(battler, target, MOVE_NONE)**: Comprehensive poison immunity check
3. **Random() % 100 < 30**: 30% activation chance

#### Poison Immunity Checks
The `CanBePoisoned` function performs several checks:
- Target must not already have a status condition
- Checks for status immunity via `IsStatusImmune(battlerTarget, CHECK_POISON)`
- Verifies type compatibility via `CanPoisonType`

#### Type Restrictions
From `CanPoisonType` function:
- **Poison-type Pokemon**: Immune to poison
- **Steel-type Pokemon**: Immune to poison
- **Exception**: Certain abilities can override type immunity (e.g., abilities with `onCanStatusType`)

#### Effect Application
- Uses `AbilityStatusEffect(MOVE_EFFECT_POISON)` to apply regular poison
- Sets `HITMARKER_IGNORE_SAFEGUARD` flag, bypassing Safeguard protection
- Applies standard poison damage (1/8 HP per turn)

## Key Characteristics

### Strengths
- Reliable 30% chance on all damaging moves
- Bypasses Safeguard ability
- Works with any damaging move (contact or non-contact)
- Can pressure bulky defensive Pokemon

### Limitations
- Cannot poison already statused targets
- Ineffective against Poison and Steel types (unless overridden)
- Blocked by poison immunity abilities
- No effect on non-damaging moves

### Strategic Applications
- Excellent for wearing down walls and tanks
- Synergizes well with moves that force switches
- Particularly effective against defensive cores lacking Poison/Steel types
- Can pressure healing-reliant strategies

## Comparison to Similar Abilities
- **Poison Point**: Only triggers on contact moves (30% chance)
- **Poison Touch**: Only on contact moves (30% chance) 
- **Toxic Spikes**: Entry hazard, not move-based
- **Envenom**: Works on ALL damaging moves, regardless of contact

## Technical Notes
- Poison applied is regular poison (1/8 HP), not badly poisoned
- Effect triggers after damage calculation
- Subject to standard poison duration and cure methods
- Stacks with other status-inflicting effects if they occur first
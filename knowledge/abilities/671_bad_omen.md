---
id: 671
name: Bad Omen
status: reviewed
character_count: 192
---

# Bad Omen - Ability ID 671

## In-Game Description
Foes min roll. Takes 1/4 damage from crits.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Opponents deal minimum damage rolls when attacking, forcing 85% damage instead of 85-100% variance. Critical hits against this Pokemon deal only 25% of their normal damage instead of 150-200%. 

## Detailed Mechanical Explanation

### Implementation Status
**FULLY IMPLEMENTED** ✅

### Working Mechanics
✅ **Critical Hit Damage Reduction**: 
- When this Pokemon receives a critical hit, damage is multiplied by 0.25 (25% of normal damage)
- Implemented via `onDefensiveMultiplier` hook with `if (isCrit) MUL(.25)` in `abilities.cc:6952`

✅ **Minimum Damage Roll**: 
- "Foes min roll" forces opponents to deal 85% damage instead of 85-100% variance
- Implemented in `battle_util.c:7558` - sets damage roll to fixed 15 (minimum) instead of random 0-15

### Code Implementation
```cpp
constexpr Ability BadOmen = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (isCrit) MUL(.25);
        },
    .breakable = TRUE,
};
```

### Technical Details

#### Critical Hit Mechanics
- **Normal critical hits**: Deal 150% damage (200% in some games)
- **With Bad Omen**: Critical hits deal `150% x 0.25 = 37.5%` of base damage
- **Effective result**: Critical hits become weaker than normal attacks

#### Damage Variance Mechanics (Implemented)
- **Normal damage variance**: 85-100% of calculated damage (random roll 0-15)
- **With Bad Omen**: Forces opponents to always deal 85% (fixed roll of 15)
- **Implementation**: Located in `battle_util.c` damage calculation function

#### Suppression
- **`.breakable = TRUE`**: Ability can be suppressed by Mold Breaker, Teravolt, Turboblaze
- When suppressed, both critical hit reduction and minimum damage effects should be disabled

### User Questions Answered

#### "What's the Acc drop?"
**No accuracy drop exists.** Bad Omen doesn't affect accuracy at all. The confusion may stem from the phrase "may miss" in some descriptions, but this ability only affects damage calculations.

#### "Does it mean you take more damage, or you lose 1/4 HP whenever you get crit?"
**You take LESS damage.** Specifically:
- Critical hits deal only **25% of their normal damage** (75% damage reduction)
- It's **not** a flat 1/4 HP loss
- It's a **multiplicative damage reduction** applied to the critical hit

### Competitive Analysis

#### Strengths
- **Crit immunity**: Effectively makes critical hits deal less damage than normal attacks
- **Damage consistency**: Forces opponents into minimum damage rolls (85% damage)
- **Anti-setup**: Reduces effectiveness of high-crit moves and abilities

#### Weaknesses
- **Suppressible**: Mold Breaker variants completely negate the ability
- **Predictable**: Opponents always know they'll deal minimum damage
- **Situational**: Only helps against specific attack patterns

#### Strategic Usage
- **Tank builds**: Excellent for defensive Pokemon that need to survive critical hits
- **Stallbreaker counter**: Reduces effectiveness of high-crit rate strategies
- **Weather teams**: Pairs well with defensive weather setters

### Development Notes
- **Implementation complete**: Both mechanics fully functional across `abilities.cc` and `battle_util.c`
- **Testing verified**: Both critical hit reduction and minimum damage roll work correctly
- **Documentation**: Ability functions exactly as described in game text
---
id: 864
name: Chuckster (N)
status: reviewed
character_count: 155
---

# Chuckster (N) - Ability ID 864

## In-Game Description
Once per entry, take 1/2 damage and force-switch the target.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Once per entry when receiving a contact move, gain 50% damage reduction and force out the attacker. Multiplicative with other sources of damage  reduction. 

## Detailed Mechanical Explanation

**File Location:** `src/abilities.cc` (line ~8767)

**Current Implementation:**
```cpp
constexpr Ability Chuckster = {
    .breakable = TRUE,
};
```

**Ability ID:** 864 (ABILITY_CHUCKSTER)

## Mechanical Analysis

1. **Trigger Condition:** First damage taken after entering battle
2. **Effect 1:** Reduces incoming damage by 50%
3. **Effect 2:** Forces the attacker to switch out (similar to moves like Dragon Tail/Circle Throw)
4. **Frequency:** Once per battle entry (resets if the Pokemon switches out and back in)
5. **Breakable:** Yes (ability can be suppressed by Mold Breaker, etc.)

## Strategic Implications

- **Defensive Utility:** Provides immediate survivability boost upon entry
- **Momentum Control:** Forces opponent switches, potentially disrupting their strategy
- **Entry Hazard Synergy:** Forced switches activate entry hazards on the opponent
- **One-Time Use:** Must be used strategically as it only works once per battle entry

## Comparison to Similar Abilities

- **Disguise:** Blocks one hit completely but doesn't force switches
- **Ice Face:** Blocks physical damage once but doesn't force switches
- **Emergency Exit/Wimp Out:** Forces self to switch rather than opponent

## Notes

- The (N) designation indicates this is an innate ability in Elite Redux's 4-ability system
- Implementation appears minimal in current codebase, suggesting functionality may be handled elsewhere in battle system
- Classified as "breakable" meaning it can be suppressed by abilities like Mold Breaker
---
id: 773
name: Soothsayer
status: reviewed
character_count: 123
---

# Soothsayer - Ability ID 773

## In-Game Description
Resists all attacks for three turns on first entry.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On entry, all attacks received by the user are considered "not very effective" for 3 turns. Deactivates when switching out.

## Detailed Mechanical Explanation

### Basic Mechanics
- **Ability ID**: 773
- **Protobuf Description**: "Resists all attacks for three turns on first entry."
- **Trigger**: `onEntry` hook with single-use check
- **Effect**: `onAfterTypeEffectiveness` modifier
- **Duration**: 3 turns tracked by `GetAbilityState()/SetAbilityState()`

### Core Implementation
```cpp
constexpr Ability Soothsayer = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(!GetSingleUseAbilityCounter(battler, ability))
        SetSingleUseAbilityCounter(battler, ability, TRUE);
        SetAbilityState(battler, ability, 3);
        return SwitchInAnnounce(B_MSG_SWITCHIN_SOOTHSAYER);
    },
    .onEndTurn = +[](ON_END_TURN) -> int {
        int counter = GetAbilityState(battler, ability);
        if (counter) SetAbilityState(battler, ability, counter - 1);
        return FALSE;
    },
    .onAfterTypeEffectiveness =
        +[](ON_AFTER_TYPE_EFFECTIVENESS) {
            if (!GetAbilityState(battler, ability)) return;
            if (*mod >= UQ_4_12(1.0)) *mod = UQ_4_12(0.5);
        },
    .onAfterTypeEffectivenessFor = APPLY_ON_TARGET,
    .breakable = TRUE,
    .persistent = TRUE,
};
```

### Switching Mechanics - ANSWER TO USER QUESTION
**Does it refresh when switching, or does the count stay?**

**Answer: The count stays and continues to tick down even when switched out.**

Here's exactly how it works:
1. **First Switch-In Only**: `GetSingleUseAbilityCounter()` ensures it only activates once per battle per Pokemon
2. **Persistent State**: `.persistent = TRUE` means ability state is preserved when switching
3. **Turn Counter Continues**: The `onEndTurn` hook decrements the counter regardless of whether the Pokemon is currently on the field
4. **No Reset on Re-entry**: Subsequent switch-ins do nothing because the single-use counter is already set

### Damage Reduction Mechanics
- **Type Effectiveness Check**: Only affects moves with >= 1.0x effectiveness
- **Damage Reduction**: All qualifying attacks become 0.5x damage (equivalent to "not very effective")
- **Move Types Affected**: All move types that would normally do neutral or super-effective damage
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze

### Key Properties
- **Single Use**: Only works on the very first switch-in per battle
- **3-Turn Duration**: Countdown happens every end of turn
- **Persistent**: State maintained when switching out
- **Breakable**: Mold Breaker effects can suppress it
- **Universal Resistance**: Affects all attacks that deal normal or super-effective damage

### Discrepancy Note
The user mentioned "5 turns" but the actual implementation uses 3 turns. The protobuf description correctly states "three turns".

### Competitive Usage
This ability provides significant defensive utility for sweepers or tanks that need setup time, but only works once per battle. The persistent nature means switching doesn't waste the effect, but the turn counter continues to tick down regardless of field presence.

---
id: 373
name: Grip Pincer
status: reviewed
character_count: 275
---

# Grip Pincer - Ability ID 373

## In-Game Description
"50% chance to trap. Then ignores Defense & accuracy checks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Contact moves have a 50% chance to trap the target (like Wrap), preventing escape or switching. Against trapped targets, the user's moves ignore defensive stats changes and always hit. Trapped targets take 1/8 max HP damage each turn. Trap lasts 4-5 turns (7 with Grip Claw).

## Detailed Mechanical Explanation

### Trap Application
- **Trigger**: Activates when the ability holder uses a contact move
- **Application Chance**: 50% chance to apply trap status (STATUS2_WRAPPED)
- **Stack Prevention**: Cannot trap already-trapped targets
- **Target Requirement**: Target must be alive and affected by on-hit effects

### Trap Duration
- **Base Duration**: 4-5 turns (randomly chosen)
- **With Grip Claw**: 7 turns
- **Turn Counter**: Decreases at the end of each turn

### Trap Effects
1. **Movement Restriction**: 
   - Trapped Pokemon cannot switch out or flee
   - Ghost-types are still trapped (unlike Gen 6+ mechanics for regular trapping moves)
   - Shed Shell allows escape despite trap

2. **End-of-Turn Damage**:
   - Deals 1/8 of target's max HP at the end of each turn
   - Damage is dealt for the duration of the trap
   - Magic Guard prevents this damage

3. **Battle Advantages for Attacker**:
   - **Accuracy Bypass**: All moves from the Grip Pincer user against trapped targets automatically hit
   - **Defense Ignore**: Physical and special moves ignore the target's defensive stat stages when calculating damage
   - These benefits only apply to the Pokemon with Grip Pincer, not its allies

### Technical Implementation Details
**Location**: `/src/abilities.cc` lines 3860-3883

**Primary Implementation**:
```cpp
constexpr Ability GripPincer = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(gBattlerTarget))
        CHECK(IsBattlerAlive(battler))
        CHECK(IsMoveMakingContact(move, battler))
        CHECK_NOT(gBattleMons[target].status2 & STATUS2_WRAPPED)
        CHECK(Random() % 2)  // 50% chance

        gBattleMons[target].status2 |= STATUS2_WRAPPED;
        if (GetBattlerHoldEffect(battler, TRUE) == HOLD_EFFECT_GRIP_CLAW)
            gVolatileStructs[target].wrapTurns = 7;
        else
            gVolatileStructs[target].wrapTurns = (Random() % 2) + 4;

        gBattleStruct->wrappedMove[target] = gCurrentMove;
        gBattleStruct->wrappedBy[target] = battler;
        BattleScriptCall(BattleScript_GripPincerActivated);
        return TRUE;
    },
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(gBattleMons[target].status2 & STATUS2_WRAPPED)
        return ACCURACY_ALWAYS_HITS;
    },
};
```

**Defense Ignoring Implementation**:
`/src/battle_util.c` line 7252 - CalcDefenseStat function ignores positive defensive stat stages when target is wrapped by Grip Pincer user.

**Battle AI Implementation**:
`/src/battle_ai_ability.c` lines 366-368 - AI evaluates Grip Pincer with wrap scoring logic.

### Interaction Details
- The trap is linked to the specific move that triggered it (`gBattleStruct->wrappedMove[target]`)
- Trapper is recorded (`gBattleStruct->wrappedBy[target]`) for stat-ignoring checks
- If the Grip Pincer user faints, the trap persists until its natural expiration
- Multiple sources of trapping do not stack - only one trap can be active per target
- The ability popup shows when trap damage is dealt (line 2537-2538 in battle_util.c)

### Strategic Applications

**Competitive Tier: High**
- Extremely powerful ability that combines trapping, damage boost, and accuracy insurance
- Creates a "death sentence" scenario for many defensive Pokemon
- Forces opponents into unfavorable positioning decisions

**Primary Strategies**:
1. **Defensive Wall Breaking**: Ignores stat boosts and defensive investment
2. **Revenge Killing**: Trap weakened opponents to prevent switching
3. **Multi-Hit Synergy**: Increases trap application chances with moves like Fury Attack
4. **Grip Claw Synergy**: 7-turn trap duration becomes nearly insurmountable

**Optimal Pokemon Characteristics**:
- High contact move diversity
- Decent Speed to capitalize on trapped opponents  
- Bulk to survive retaliatory attacks
- Access to Grip Claw item

### Counters and Limitations
1. **Shed Shell**: Allows escape from trap status
2. **Magic Guard**: Prevents trap damage (but not other effects)
3. **Ghost-types**: Still trapped (unlike standard trapping moves in newer generations)
4. **Non-contact moves**: Cannot trigger the trap effect
5. **50% activation rate**: Not guaranteed on contact
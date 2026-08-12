---
id: 407
name: Retribution Blow
status: reviewed
character_count: 156
---

# Retribution Blow - Ability ID 407

## In-Game Description
"Uses Hyper Beam if any foe uses an stat boosting move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Automatically uses 150 BP Hyper Beam against opponents that boost stats. The triggered Hyper Beam has no recharge period, allowing normal actions next turn. 

## Detailed Mechanical Explanation

### Does the Hyper Beam put you in recharge?

**NO, the Hyper Beam from Retribution Blow does NOT cause recharge status.**

This is because of a specific check in the recharge effect implementation:

```c
case MOVE_EFFECT_RECHARGE:
    if (!gProcessingExtraAttacks) {
        gBattleMons[gEffectBattler].status2 |= STATUS2_RECHARGE;
        gVolatileStructs[gEffectBattler].rechargeTimer = 2;
        gLockedMoves[gEffectBattler] = gCurrentMove;
    }
    break;
```

When `gProcessingExtraAttacks` is true (which it is for abilities like Retribution Blow that use `UseOutOfTurnAttack`), the recharge status is **completely skipped**.

## Implementation Analysis

### Trigger Mechanism
- **Hook:** `onReactive` - This activates when stat stage checks are performed
- **Condition:** Any positive stat change (`> 0`) on the attacking opponent
- **Stat Check:** Loops through all stats (ATK, DEF, SPA, SPD, SPE) checking `gBattleStruct->statChangesToCheck[gBattlerAttacker][stat - 1]`

### Code Implementation
```cpp
constexpr Ability RetributionBlow = {
    .onReactive = +[](ON_REACTIVE) -> int {
        CHECK_NOT(gTurnStructs[battler].dancerUsedMove)
        CHECK(IsBattlerAlive(gBattlerAttacker))
        CHECK(gCurrentTurnActionNumber < gBattlersCount || gProcessingExtraAttacks)
        CHECK(gBattleStruct->statStageCheckState != STAT_STAGE_CHECK_NOT_NEEDED)
        for (int stat = STAT_ATK; stat < NUM_STATS; stat++) {
            if (gBattleStruct->statChangesToCheck[gBattlerAttacker][stat - 1] > 0) {
                UseOutOfTurnAttack(battler, gBattlerAttacker, ability, MOVE_HYPER_BEAM, 0);
                return FALSE;
            }
        }
        return FALSE;
    },
};
```

### Key Mechanics
1. **Trigger:** When any opponent uses a move that boosts any stat
2. **Attack:** Launches a 150 BP Normal-type Hyper Beam 
3. **No Recharge:** The extra attack system bypasses recharge effects
4. **Once Per Turn:** Protected by the extra attack system's dancer check
5. **Accuracy:** 100% accuracy, affected by normal accuracy checks
6. **Target:** Targets the specific opponent who used the stat-boosting move

### Strategic Implications
- This makes Retribution Blow extremely powerful as it provides a free 150 BP attack without drawbacks
- Punishes setup sweepers and stat-boosting strategies heavily
- The lack of recharge means the user can continue normal attacks next turn
- Forces opponents to be very careful about when they set up


## Detailed Explanation for Discord
**Retribution Blow** is a reactive ability that automatically triggers a powerful counterattack when opponents attempt to boost their stats. Here's exactly how it works:

**Trigger Condition:** Any time an opponent uses a move that increases any of their stats (Attack, Defense, Special Attack, Special Defense, or Speed), Retribution Blow activates.

**The Counterattack:** The user immediately launches a 150 BP Normal-type Hyper Beam at the stat-boosting opponent with 100% accuracy.

**Critical Mechanic:** Unlike normal Hyper Beam usage, the triggered attack does NOT cause recharge status. This is because it uses the extra attack system (`gProcessingExtraAttacks = true`), which explicitly bypasses recharge effects in the move effect code.

**Strategic Impact:** This ability is a massive deterrent to setup strategies. Pokemon with Retribution Blow essentially get a free 150 BP attack every time an opponent tries to set up, with no drawback. This makes it extremely punishing against:
- Setup sweepers using moves like Dragon Dance, Nasty Plot, etc.
- Support Pokemon using stat-boosting moves
- Any strategy relying on stat increases

The ability ensures that stat-boosting always comes with immediate, severe consequences while leaving the user free to act normally on their next turn.
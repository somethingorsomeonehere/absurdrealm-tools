---
id: 583
name: Gallantry
status: reviewed
character_count: 117
---

# Gallantry - Ability ID 583

## In-Game Description
"Gets no damage for first hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Negates the first instance of damage received. Moves still connect and secondary effects apply, but damage becomes 0.

## Detailed Mechanical Explanation

**Gallantry** is essentially a weaker, breakable version of **Cheating Death**.

**Implementation in abilities.cc (lines 6160-6170):**
```cpp
constexpr Ability Gallantry = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(GetSingleUseAbilityCounter(battler, ability))

        BattleScriptPushCursorAndCallback(BattleScript_BattlerHasASingleNoDamageHit);
        return TRUE;
    },
    .noDamageHits = 1,
    .breakable = TRUE,
    .persistent = TRUE,
};
```

**Key Differences from Cheating Death:**
1. **Number of Hits**: Blocks only 1 hit (`noDamageHits = 1`) vs Cheating Death's 2 hits
2. **Breakable**: `breakable = TRUE` - can be suppressed by abilities like Mold Breaker
3. **Simpler Counter Logic**: Uses `CHECK_NOT(GetSingleUseAbilityCounter(battler, ability))` instead of calculating remaining uses

## Trigger Conditions

- Activates when the Pokemon would take damage from an attack
- Only blocks the first 1 hit received in battle per Pokemon
- Can be suppressed by Mold Breaker, Teravolt, Turboblaze, etc.
- Does not activate on passive damage or entry hazards

## Numerical Effects

- **Hits Blocked**: Exactly 1 hit per battle
- **Damage Reduction**: 100% (damage becomes 0)
- **Suppression**: Can be bypassed by Mold Breaker abilities

## Interactions

**Counter System:**
The `GetSingleUseAbilityCounter` function retrieves a counter stored per Pokemon, per ability, per side:
```cpp
gBattleStruct->singleuseability[gBattlerPartyIndexes[battler]][index][GetBattlerSide(battler)]
```

**With Mold Breaker:**
- Unlike Cheating Death, Gallantry can be suppressed by Mold Breaker-type abilities
- When suppressed, the protection does not activate

**With Other Mechanics:**
- Move still makes contact (triggers contact abilities)
- Secondary effects still apply (status, stat changes)
- Shows hit animation but 0 damage

## Special Cases

**Multi-Hit Moves:**
- Gallantry blocks ONLY the first hit of multi-hit moves
- After the first hit is blocked, the counter increments to 1
- Subsequent hits in the same multi-hit attack deal normal damage
- Example: Against Bullet Seed (2-5 hits), only the first hit deals 0 damage; hits 2-5 deal full damage

**Battle Script Messages:**
- Always uses `BattleScript_BattlerHasASingleNoDamageHit` when entering with protection available
- No variable message based on remaining uses (unlike Cheating Death)

**Reset Behavior:**
- Both Gallantry and Cheating Death have `persistent = TRUE`
- Counter does NOT reset on switching
- Protection is consumed permanently once used

## Notes

- **Gallantry vs Cheating Death Summary:**
  - Gallantry: 1 hit protection, breakable by Mold Breaker
  - Cheating Death: 2 hit protection, unbreakable
  - Both persist through switching and last the entire battle per Pokemon

- Counter starts at 0, increments to 1 after first use, then blocks activation
- Designed as a more balanced alternative to Cheating Death's stronger protection

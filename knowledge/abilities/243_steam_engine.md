---
id: 243
name: Steam Engine
status: reviewed
character_count: 146
---

# Steam Engine - Ability ID 243

## In-Game Description
"Maximizes Speed if hit by a Fire-type or Water-type attack."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Steam Engine maximizes the Speed stat to +6 stages when hit by any Fire-type or Water-type move. The boost occurs immediately after taking damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

Steam Engine is a powerful defensive ability that converts incoming Fire or Water-type attacks into a massive Speed advantage. Here's how it works:

### Trigger Conditions
- Must be hit by a Fire-type or Water-type move
- The move must connect and deal damage (accuracy/hit confirmation required)
- Works regardless of damage amount - even 1 HP triggers the effect
- Activates after damage calculation but before the turn ends

### Stat Boost Mechanics
- Raises Speed by 12 stages (the maximum possible boost)
- This equals a +6 Speed stage boost, which is a 4x multiplier to base Speed
- The boost occurs immediately after taking damage
- Uses the same system as abilities like Anger Point (for Attack) and Justified (for Attack)

### Activation Requirements
- The ability holder must survive the attack
- ShouldApplyOnHitAffect() check must pass (no substitutes, etc.)
- CanRaiseStat() check must pass (Speed not already maxed)
- Works against both physical and special Fire/Water moves

### Strategic Applications
- Excellent for defensive pivots and revenge sweeping
- Turns common attacking types (Fire/Water) into setup opportunities
- Pairs well with bulky Pokemon that can survive strong hits
- Counters popular offensive types in the metagame

### Interactions and Edge Cases
- Does NOT activate on:
  - Moves that miss
  - Damage through Substitute
  - Status moves (even Fire/Water-type ones)
  - Indirect damage from items or other abilities
- DOES activate on:
  - Multi-hit moves (each hit can trigger if the first doesn't max Speed)
  - Recoil moves
  - Contact and non-contact moves equally
  - Moves boosted by weather, abilities, or items

### Code Implementation
```cpp
constexpr Ability SteamEngine = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(CanRaiseStat(battler, STAT_SPEED))
        CHECK(moveType == TYPE_FIRE || moveType == TYPE_WATER)

        SetStatChanger(STAT_SPEED, 12);
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        return TRUE;
    },
};
```

The ability uses the `onDefender` hook to trigger when the Pokemon takes damage, checks for Fire or Water move types, and then maximizes the Speed stat using `SetStatChanger(STAT_SPEED, 12)` where 12 represents the maximum stat stage boost.
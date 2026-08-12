---
id: 448
name: Electromorphosis
status: reviewed
character_count: 162
---

# Electromorphosis - Ability ID 448

## In-Game Description
"Charges up when getting hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by any move, the user becomes charged up, doubling the power of the next Electric-type move used. Charged status is consumed after one Electric move use.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Electromorphosis is an offensive ability that transforms damage taken into offensive power. When the Pokemon is hit by any damaging move, it gains a "charged up" status that doubles the power of its next Electric-type attack.

### Activation Conditions
- **Trigger**: Taking damage from any attack that triggers the onDefender callback
- **Status check**: Only activates if the Pokemon is not already charged up
- **Hit requirement**: Must pass the `ShouldApplyOnHitAffect` check
- **One-time effect**: Cannot stack multiple charges

### Power Boost Mechanics
- **Multiplier**: 2.0x damage for Electric-type moves when charged
- **Move requirement**: Only affects moves with base power (attacking moves)
- **Type restriction**: Only Electric-type moves receive the boost
- **Consumption**: The charge is consumed after using any Electric-type move with power

### Technical Implementation
```c
constexpr Ability Electromorphosis = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK_NOT(gStatuses3[battler] & STATUS3_CHARGED_UP)

        gStatuses3[battler] |= STATUS3_CHARGED_UP;
        BattleScriptCall(BattleScript_ElectromorphosisActivates);
        return TRUE;
    },
};

// In damage calculation:
if (gStatuses3[battlerAtk] & STATUS3_CHARGED_UP && moveType == TYPE_ELECTRIC) 
    MulModifier(&modifier, UQ_4_12(2.0));

// Charge consumption:
if (currentMoveType == TYPE_ELECTRIC && gBattleMoves[gCurrentMove].power)
    gStatuses3[gBattlerAttacker] &= ~STATUS3_CHARGED_UP;
```

### Important Interactions
- **Status moves**: Electric-type status moves don't consume the charge
- **Multi-hit moves**: Each hit can trigger the ability, but only one charge is gained
- **Substitute**: The ability can still activate even if protected by Substitute
- **Contact requirement**: Not required - any hit can trigger the charge
- **Ability bypass**: Mold Breaker and similar abilities don't prevent the charge gain

### Charge Duration
- **Persistence**: The charge lasts until consumed or the Pokemon switches out
- **Switch out**: Charge is lost when switching out
- **Fainting**: Charge is lost when fainting
- **Turn limit**: No turn limit - charge persists indefinitely until used

### Strategic Applications
- **Pivot strategy**: Take a hit, then pivot to an Electric-type move for massive damage
- **Revenge killing**: Use defensive switches to gain charges for counterattacks
- **Momentum shifts**: Transform opponent's offensive pressure into your own advantage
- **Type coverage**: Makes Electric-type moves significantly more threatening

### Synergies
- **Focus Sash**: Survive powerful hits to guarantee a charge
- **Assault Vest**: Tank special attacks while gaining charges
- **Electric-type STAB**: Combines with same-type attack bonus for massive damage
- **Choice items**: Locked Electric moves become extremely powerful after charging
- **Life Orb**: Stacks with the charge bonus for even higher damage output

### Comparison to Similar Abilities
- **Rattled**: Gives Speed boost instead of power boost
- **Justified**: Triggered by Dark moves only, boosts Attack stat
- **Stamina**: Boosts Defense instead of next move's power
- **Anger Point**: Requires critical hit, maxes Attack stat

### Competitive Viability
- **Offensive pressure**: Creates immediate threat after taking damage
- **Unpredictable**: Opponents must consider the charged state in their calculations
- **Risk/reward**: Requires taking damage to gain benefit
- **Electric synergy**: Most effective on Pokemon with strong Electric-type movesets

### Common Users
- Electric-type Pokemon with good mixed bulk
- Pokemon with powerful Electric-type coverage moves
- Defensive pivots that can absorb hits reliably
- Pokemon with recovery moves to maintain longevity

### Counters
- **Status moves**: Use non-damaging moves to avoid triggering the ability
- **Indirect damage**: Poison, burn, and entry hazards don't trigger the charge
- **Ability suppression**: Mold Breaker prevents the ability from activating
- **Type immunity**: Ground-types are immune to Electric attacks even when charged
- **Priority moves**: Strike before the charged Electric move can be used

### Version Notes
- Custom ability created for Elite Redux
- Part of the expanded ability roster for strategic depth
- Shares the charged up status with other charging abilities like Wind Power
- Activation message uses STRINGID_ELECTROMORPHOSIS_ACTIVATES (ID 686)
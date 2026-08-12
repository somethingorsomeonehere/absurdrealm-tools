---
id: 447
name: Furnace
status: reviewed
character_count: 109
---

# Furnace - Ability ID 447

## In-Game Description
"User gains +2 Speed when when hit by rocks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Furnace boosts Speed by +2 stages when hit by Rock-type moves or when switching in with Stealth Rock present. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Furnace is a reactive ability that converts Rock-type damage into Speed boosts. It provides immediate Speed increases through two distinct triggers, making it a powerful momentum ability for Pokemon that can survive Rock-type attacks.

### Activation Conditions
The ability has two separate activation mechanisms:

#### 1. Switch-In Activation (.onEntry)
- **Trigger**: When switching in with Rock-type Stealth Rock present on the field
- **Requirements**:
  - `SIDE_STATUS_STEALTH_ROCK` must be active on the battler's side
  - `stealthRockType` must be `TYPE_ROCK` (not Grass-type Creeping Thorns)
  - Battler must be alive after switching in
- **Effect**: Grants +2 Speed stages immediately upon entry
- **Script**: Uses `BattleScript_AttackerAbilityStatRaiseEnd3`

#### 2. Hit Reaction (.onDefender)
- **Trigger**: When hit by Rock-type moves during battle
- **Requirements**:
  - `ShouldApplyOnHitAffect(battler)` - move must hit and deal damage
  - `moveType == TYPE_ROCK` - attacking move must be Rock-type
  - `CanRaiseStat(battler, STAT_SPEED)` - Speed must be raisable
- **Effect**: Grants +2 Speed stages after taking Rock-type damage
- **Script**: Uses `BattleScript_TargetAbilityStatRaiseOnMoveEnd`

### Technical Implementation
```c
constexpr Ability Furnace = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(gSideStatuses[GetBattlerSide(battler)] & SIDE_STATUS_STEALTH_ROCK)
        CHECK(gSideTimers[GetBattlerSide(battler)].stealthRockType == TYPE_ROCK)
        CHECK(IsBattlerAlive(battler))
        CHECK(ChangeStatBuffs(battler, 2, STAT_SPEED, MOVE_EFFECT_AFFECTS_USER, NULL))

        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        return TRUE;
    },
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(moveType == TYPE_ROCK)
        CHECK(CanRaiseStat(battler, STAT_SPEED))

        SetStatChanger(STAT_SPEED, 2);
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        return TRUE;
    },
};
```

### Important Interactions

#### Stealth Rock Synergy
- **Activation requirement**: Only works with Rock-type Stealth Rock, not Grass-type Creeping Thorns
- **Entry hazards**: Triggers immediately when switching in if Rock Stealth Rock is present
- **Damage timing**: Speed boost occurs after taking Stealth Rock damage on switch-in
- **Multiple activations**: Can trigger on both switch-in and during battle with Rock moves

#### Battle Mechanics
- **Hit requirement**: Must take actual damage from Rock moves to trigger during battle
- **Multi-hit moves**: Can potentially trigger on each hit of multi-hit Rock moves
- **Status protection**: Ability functions normally even if Pokemon has status conditions
- **Stat boost caps**: Cannot raise Speed beyond +6 stages maximum

#### Ability Interactions
- **Mold Breaker**: Furnace can be suppressed by Mold Breaker and similar abilities
- **Simple**: If paired with Simple ability, Speed boosts become +4 instead of +2
- **Contrary**: Would reverse the Speed boost into a Speed drop if somehow combined
- **Magic Guard**: Protects from Stealth Rock damage but still allows the Speed boost

### Strategic Applications

#### Team Building Synergy
- **Rock-weak Pokemon**: Transforms Rock weakness into Speed advantage
- **Offensive sweepers**: Provides immediate setup opportunity after taking Rock damage
- **Stealth Rock punishment**: Punishes common entry hazard with Speed boosts
- **Momentum building**: Creates instant sweeping potential from defensive switches

#### Competitive Usage
- **Entry hazard meta**: Excellent in metagames with heavy Stealth Rock usage
- **Rock-type counters**: Can safely switch into Rock moves for Speed boosts
- **Speed control**: Provides immediate Speed tier advantage after activation
- **Surprise factor**: Opponents may not expect Speed boosts from Rock attacks

#### Common Scenarios
- **Stealth Rock switch-in**: Gain +2 Speed when switching into Stealth Rock
- **Rock move survival**: Tank Rock moves for Speed boosts and counterattack
- **Edge Quake response**: Turn common EdgeQuake strategies against opponents
- **Hazard stacking**: Benefit from opponent's Stealth Rock setup

### Counters and Limitations

#### Direct Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas, and similar abilities
- **Speed control**: Trick Room reverses the Speed advantage
- **Status conditions**: Paralysis can negate Speed boosts
- **Choice items**: Speed boosts don't help if locked into the wrong move

#### Situational Limitations
- **Rock immunity**: Flying types with Air Balloon avoid Rock Stealth Rock
- **Heavy Duty Boots**: Prevents Stealth Rock damage and thus the entry boost
- **Type changes**: Becoming Rock-resistant removes the hit activation
- **Magic Bounce**: Can reflect Rock moves before they trigger Furnace

#### Strategic Limitations
- **Setup requirement**: Needs Rock moves or Rock Stealth Rock to activate
- **Health cost**: Takes damage to gain Speed (except potentially with Magic Guard)
- **Timing dependency**: Opponent controls when Rock moves are used
- **Single activation**: Each Rock hit only gives one boost, not cumulative

### Comparison to Similar Abilities

#### Speed Boost Abilities
- **Speed Boost**: Gradual +1 each turn vs immediate +2 from Rock hits
- **Moody**: Random stat changes vs reliable Speed from specific trigger
- **Weak Armor**: +1 Speed from physical hits vs +2 Speed from Rock hits

#### Reactive Abilities
- **Anger Point**: +12 Attack from crits vs +2 Speed from Rock hits
- **Rattled**: +1 Speed from Dark/Bug/Ghost vs +2 Speed from Rock
- **Stamina**: +1 Defense when hit vs +2 Speed from Rock hits

### Version History
- Introduced in Elite Redux as a custom ability
- Part of the expanded ability system with unique triggers
- Designed to create counterplay against common Stealth Rock usage
- Synergizes with Elite Redux's extended battle mechanics

### Related Abilities
- **Molten Core**: Enhanced version that also absorbs Rock moves and removes Stealth Rock
- **Rocky Payload**: Another Rock-type interaction ability
- **Weak Armor**: Similar defensive reaction ability with stat changes
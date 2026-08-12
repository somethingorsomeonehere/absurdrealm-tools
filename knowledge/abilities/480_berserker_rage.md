---
id: 480
name: Berserker Rage
status: reviewed
character_count: 234
---

# Berserker Rage - Ability ID 480

## In-Game Description
"Tipping Point + Rampage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit, raises the user's Special Attack by 1 stage or maximizes it on critical hits. When the user knocks out an opponent, it instantly recovers from recharge status, allowing immediate use of moves like Hyper Beam without waiting.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Berserker Rage is a hybrid ability that combines two distinct effects from the Tipping Point and Rampage abilities. It provides both defensive stat boosts when taking damage and offensive momentum when scoring KOs.

### Dual Effect Components

#### Tipping Point Component (.onDefender)
- **Triggers**: When the Pokemon is hit by an attack
- **Condition**: Must be a hit that can apply on-hit effects (ShouldApplyOnHitAffect)
- **Normal hits**: Raises Special Attack by 1 stage
- **Critical hits**: Maximizes Special Attack (sets to +6 stages instantly)
- **Stat requirements**: Only works if Special Attack can be raised further

#### Rampage Component (.onBattlerFaints)
- **Triggers**: When the Pokemon KOs an opponent (APPLY_ON_ATTACKER)
- **Effect**: Instantly removes recharge status
- **Mechanics**: 
  - Sets rechargeTimer to 0
  - Removes STATUS2_RECHARGE flag
  - Allows immediate action on next turn

### Technical Implementation
```c
constexpr Ability BerserkerRage = {
    .onDefender = TippingPoint.onDefender,        // Stat boost when hit
    .onBattlerFaints = Rampage.onBattlerFaints,   // Recharge removal on KO
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,      // Apply to attacker
};

// Tipping Point mechanics
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(battler))
    CHECK(CanRaiseStat(battler, STAT_SPATK))
    
    if (gIsCriticalHit) {
        SetStatChanger(STAT_SPATK, 12);  // Max boost (+6)
        BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
    } else {
        SetStatChanger(STAT_SPATK, 1);   // +1 stage
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
    }
    return TRUE;
}

// Rampage mechanics
.onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
    SetAbilityState(battler, ability, TRUE);
    gVolatileStructs[battler].rechargeTimer = 0;
    gBattleMons[battler].status2 &= ~(STATUS2_RECHARGE);
    return FALSE;
}
```

### Recharge Move Interactions
The Rampage component works with any move that causes recharge status:
- **Hyper Beam**: Can use immediately after KO instead of waiting
- **Giga Impact**: No recharge turn needed after scoring KOs
- **Blast Burn/Hydro Cannon/Frenzy Plant**: Starter ultimate moves
- **Roar of Time**: Dialga's signature move
- **Rock Wrecker**: Rhyperior's signature move

### Critical Hit Synergy
The ability heavily rewards landing critical hits:
- **Normal scenario**: Take damage to gain +1 Special Attack
- **Critical hit scenario**: Take damage to instantly max Special Attack (+6)
- **Follow-up potential**: High Special Attack enables powerful special moves
- **Recharge recovery**: Can immediately use powerful moves after KOs

### Activation Conditions
- **Tipping Point**: Must be hit by an attack that can apply effects
- **Special Attack raise**: Must have room to increase Special Attack
- **Rampage**: Must score a KO while in recharge status
- **Both effects**: Can trigger in the same battle independently

### Strategic Applications

#### Offensive Pressure
- **Recharge spam**: Use Hyper Beam/Giga Impact more freely
- **KO momentum**: Chain powerful moves without downtime
- **Special sweeping**: Critical hits can instantly set up special sweeps
- **Mixed offense**: Physical recharge moves + special attack boosts

#### Risk/Reward Gameplay
- **Tank hits intentionally**: Build Special Attack through damage
- **Critical hit fishing**: Moves like Focus Energy become valuable
- **High-risk moves**: Recharge moves become safer with KO potential
- **Momentum swings**: Can turn defensive hits into offensive opportunities

### Counters and Limitations

#### Tipping Point Limitations
- **Special Attack cap**: Doesn't work if already at +6 Special Attack
- **Physical attackers**: Only boosts Special Attack, not Attack
- **Effect immunity**: Doesn't trigger on moves that can't apply effects
- **Substitute**: Blocked by Substitute protecting the target

#### Rampage Limitations
- **KO requirement**: Must actually KO the opponent to activate
- **Recharge timing**: Only helps if currently in recharge status
- **Single use**: Each KO only removes one recharge instance
- **Status moves**: Doesn't help with non-recharge status effects

### Synergies

#### Critical Hit Support
- **Focus Energy**: Guarantees critical hits for max Special Attack boosts
- **Scope Lens/Razor Claw**: Increases critical hit chance
- **Super Luck**: Natural critical hit rate boosts
- **High critical ratio moves**: Moves with higher crit chances

#### Recharge Move Arsenal
- **Hyper Beam**: Standard powerful Normal-type option
- **Giga Impact**: Physical equivalent for coverage
- **Blast Burn**: Fire-type starter move
- **Hydro Cannon**: Water-type starter move
- **Frenzy Plant**: Grass-type starter move

#### Special Attack Utilization
- **High base power specials**: Maximize damage with boosted stats
- **Coverage moves**: Use stat boosts with diverse move types
- **Choice items**: Stack with Choice Specs for massive damage
- **Life Orb**: Compound damage boosts further

### Competitive Usage
- **Mixed attacker role**: Use physical recharge moves and special follow-ups
- **Momentum controller**: Chain attacks without losing tempo
- **Setup sweeper**: Critical hits provide instant setup
- **Anti-stall**: Powerful moves can be used more freely
- **High-risk high-reward**: Rewards aggressive play patterns

### Pokemon Suitability
Ideal for Pokemon with:
- **High Special Attack**: Can utilize the stat boosts effectively
- **Mixed movepool**: Access to both physical recharge and special moves
- **Good bulk**: Can survive hits to trigger Tipping Point effect
- **Critical hit moves**: Can reliably trigger maximum stat boosts
- **Recharge move access**: Can utilize the Rampage component

### Version History
- Custom Elite Redux ability combining two existing effects
- Part of the expanded ability roster for enhanced strategic depth
- Designed to create high-risk, high-reward gameplay patterns
- Enables new archetype mixing recharge moves with special attacks
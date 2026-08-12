---
id: 528
name: Crowned Shield
status: reviewed
character_count: 167
---

# Crowned Shield - Ability ID 528

## In-Game Description
"Dauntless Shield + Stamina."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises Defense by 1 stage upon switching in. When hit, raises the user's Defense by 1 stage or maximizes it on critical hits. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Crowned Shield is an Elite Redux exclusive ability that combines two powerful defensive abilities: Dauntless Shield (entry effect) and Stamina (on-hit effect). This creates a Pokemon with exceptional defensive scaling potential.

### Component Abilities

#### Dauntless Shield Component (onEntry)
- **Effect**: Raises Defense by 1 stage upon switching in
- **Activation**: Triggers immediately when the Pokemon enters battle
- **Condition**: Must be able to raise Defense stat (not at +6)

#### Stamina Component (onDefender)
- **Effect**: Raises Defense when taking damage from moves
- **Normal hits**: +1 Defense stage
- **Critical hits**: Maxes out Defense (+12 stages to reach +6)
- **Condition**: Must be able to raise Defense stat

### Technical Implementation
```c
constexpr Ability CrownedShield = {
    .onEntry = DauntlessShield.onEntry,     // +1 Defense on switch-in
    .onDefender = Stamina.onDefender,       // +1 Defense on hit (+12 on crit)
};

// DauntlessShield component
.onEntry = +[](ON_ENTRY) -> int {
    CHECK(CanRaiseStat(battler, STAT_DEF))
    SetStatChanger(STAT_DEF, 1);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
    return TRUE;
},

// Stamina component  
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(battler))
    CHECK(CanRaiseStat(battler, STAT_DEF))
    
    if (gIsCriticalHit) {
        SetStatChanger(STAT_DEF, 12);  // Max out Defense
        BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
    } else {
        SetStatChanger(STAT_DEF, 1);   // +1 Defense
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
    }
    return TRUE;
},
```

### Activation Sequence
1. **Switch-in**: Immediately gains +1 Defense from Dauntless Shield
2. **Taking damage**: Each hit grants +1 Defense (or maxes Defense on crit)
3. **Stacking**: Can accumulate Defense boosts rapidly through combat

### Important Interactions
- **Critical hits**: Instantly maxes Defense at +6 stages
- **Multi-hit moves**: Each hit triggers Stamina component separately
- **Stat cap**: Cannot raise Defense beyond +6 (maxed out)
- **Ability suppression**: Both components disabled by Mold Breaker effects
- **Entry effects**: Only triggers once per switch-in
- **Substitutes**: Stamina doesn't trigger when substitute takes damage

### AI Behavior
The AI correctly evaluates both components:
- **Switch-in scoring**: `AI_SCORE_STAT(battlerAtk, STAT_DEF, 1)`
- **Damage scoring**: `AI_SCORE_STAT(battlerDef, STAT_DEF, 1) + AI_SCORE_ADJUST(moveState->critChance, AI_SCORE_STAT(battlerDef, STAT_DEF, 12))`

### Strategic Implications
- **Defensive powerhouse**: Can become incredibly bulky very quickly
- **Crit vulnerability**: Paradoxically benefits from being critically hit
- **Pivot potential**: Entry boost makes it excellent for switching
- **Wallbreaker counter**: Absorbs physical attacks to become stronger
- **Longevity**: Extended battles favor massive Defense accumulation

### Exclusive User
- **Zamazenta-Crowned Shield**: The only Pokemon with this ability
- **Legendary status**: Befitting of a powerful legendary Pokemon
- **Form-specific**: Only available on the Crowned Shield form

### Competitive Usage Notes
- **Physical wall**: Becomes nearly impregnable against physical attacks
- **Setup counter**: Punishes physical setup sweepers
- **Momentum shift**: Can turn defensive into offensive opportunities
- **Crit fishing**: Opponents may avoid high-crit moves against it
- **Special vulnerability**: Doesn't help against special attacks

### Counters
- **Special attacks**: Completely bypasses Defense boosts
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Core Enforcer
- **Stat reset**: Haze, Clear Smog, Spectral Thief
- **Unaware**: Ignores all stat boosts when calculating damage
- **Psych Up/Heart Swap**: Can steal the accumulated boosts
- **Trick Room**: May exploit the likely slow nature of the user

### Synergies
- **Body Press**: Damage scales with Defense boosts
- **Iron Defense**: Further Defense stacking
- **Rest**: Longevity to take advantage of boosts
- **Substitute**: Protects accumulated boosts
- **Leftovers/Rocky Helmet**: Passive recovery and contact damage
- **Assault Vest**: Special bulk to complement physical bulk

### Version History
- Elite Redux exclusive ability
- Combines two existing Gen 8 abilities (Dauntless Shield + Stamina)
- Represents the defensive counterpart to Crowned Sword
- Thematically appropriate for Zamazenta's legendary status

### Design Philosophy
Crowned Shield exemplifies Elite Redux's approach to legendary abilities:
- Combines multiple effects for unique power
- Creates distinct playstyles and strategies
- Rewards defensive play while maintaining counterplay options
- Balances power with specialized application
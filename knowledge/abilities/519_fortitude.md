---
id: 519
name: Fortitude
status: reviewed
character_count: 130
---

# Fortitude - Ability ID 519

## In-Game Description
"Boosts SpDef +1 when hit. Maxes SpDef on crit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit, raises the user's Special Defense by 1 stage or maximizes it on critical hits. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fortitude is a defensive ability that turns every hit into a potential Special Defense boost. The ability provides escalating defensive utility that can completely shut down special attackers over time.

### Activation Conditions
- **Trigger**: Any move that hits the Pokemon
- **Damage requirement**: Move must deal damage (status moves don't trigger)
- **Critical hit bonus**: Critical hits instantly max out Special Defense
- **Multi-hit moves**: Each hit triggers the ability separately
- **Contact requirement**: None - works with all damaging moves

### Technical Implementation
```c
// Fortitude triggers on defender when hit
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(battler))
    CHECK(CanRaiseStat(battler, STAT_SPDEF))

    if (gIsCriticalHit) {
        SetStatChanger(STAT_SPDEF, 12);  // Max out to +6
        BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
    } else {
        SetStatChanger(STAT_SPDEF, 1);   // Normal +1 boost
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
    }
    return TRUE;
},
```

### Stat Boost Details
- **Normal hit**: +1 Special Defense stage
- **Critical hit**: +6 Special Defense stages (maximum)
- **Stat cap**: Cannot exceed +6 stages total
- **Timing**: Boost applies after being hit, before end of turn

### Important Interactions
- **Multi-hit moves**: Each hit of moves like Bullet Seed triggers separately
- **Substitute**: Does not trigger when behind Substitute
- **Magic Guard**: Still triggers even if damage is negated
- **Critical hits**: Super Luck and Sniper synergize well with this ability
- **Stat reset**: Haze, Clear Smog, and switching out reset the boosts

### Strategic Implications
- **Wall potential**: Can become an impenetrable special wall
- **Momentum shift**: Forces opponents to use physical moves
- **Stall tactics**: Excellent for defensive builds
- **Critical vulnerability**: Ironically, critical hits help the defender
- **Setup sweeper**: Can use accumulated boosts for special attacks

### Common Users
Based on the code analysis, Fortitude appears on:
- Defensive Pokemon that appreciate stat boosts
- Pokemon with good Special Defense stat distribution
- Bulky support Pokemon that can utilize the defensive scaling
- Pokemon that can take advantage of the critical hit interaction

### Competitive Usage Notes
- **Defensive core**: Excellent on defensive teams
- **Special tank**: Can completely wall special attackers
- **Baton Pass**: Boosts can be passed to teammates
- **Rest synergy**: Can stall indefinitely with proper support
- **Critical interaction**: Opponents may avoid critical hit items

### Counters
- **Physical attacks**: Ability only affects Special Defense
- **Stat reset moves**: Haze, Clear Smog negate accumulated boosts
- **Taunt**: Prevents recovery moves and setup
- **Substitute**: Prevents ability from triggering
- **Ability suppression**: Mold Breaker bypasses the ability

### Synergies
- **Leftovers/Black Sludge**: Passive recovery while accumulating boosts
- **Rest**: Full recovery while maintaining defensive boosts
- **Calm Mind**: Stacks with Special Defense boosts for offensive presence
- **Stored Power**: Damage scales with accumulated stat boosts
- **Baton Pass**: Transfer boosts to offensive teammates

### Unique Aspects
- **Progressive scaling**: Becomes stronger with each hit taken
- **Critical hit reversal**: Turns opponent's luck against them
- **Defensive snowball**: Each hit makes subsequent hits weaker
- **Multi-hit punishment**: Makes multi-hit moves counterproductive
- **Flexible timing**: Works against any damaging move

### Version History
- Custom Elite Redux ability (ID 519)
- Part of the expanded ability system
- Designed to create unique defensive strategies
- Encourages mixed offensive/defensive team building
---
id: 83
name: Anger Point
status: reviewed
character_count: 121
---

# Anger Point - Ability ID 83

## In-Game Description
"Getting hit raises Atk by +1. Critical hits maximize Attack."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit, raises the user's Attack by 1 stage or maximizes it on critical hits. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

**ANGER POINT** is a defensive stat-boosting ability that converts incoming damage into offensive power, with special interactions for critical hits.

### Activation Mechanics:
- **Trigger**: onDefender hook - activates when hit by any damaging move
- **Requirements**: 
  - Must survive the hit (ShouldApplyOnHitAffect check)
  - Attack stat must be boostable (CanRaiseStat check)
  - No restrictions on move type, contact requirement, or damage source

### Stat Modification Rules:
1. **Regular Hits**: Attack +1 stage (1.5x to 2x to 2.5x to 3x to 3.5x to 4x)
2. **Critical Hits**: Attack maximized to +6 stages (4x multiplier)
   - Uses SetStatChanger(STAT_ATK, 12) - value 12 sets to maximum
   - Displays "Pokemon's Attack was maximized!" message
   - Bypasses normal stat stage progression

### Technical Implementation:
```c
constexpr Ability AngerPoint = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(CanRaiseStat(battler, STAT_ATK))

        if (gIsCriticalHit) {
            SetStatChanger(STAT_ATK, 12);
            BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
        } else {
            SetStatChanger(STAT_ATK, 1);
            BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        }
        return TRUE;
    },
};
```

### Interaction Rules:
- **Multi-hit moves**: Each hit can trigger Anger Point separately
- **Substitute**: Does not block Anger Point activation if the substitute is broken
- **Contact requirement**: None - works with all damaging moves
- **Type restrictions**: None - works against all move types
- **Status moves**: Does not trigger (only damaging moves)
- **Indirect damage**: Does not trigger on poison, burn, weather, or entry hazard damage

### Battle Script Messages:
- Regular hit: "[Pokemon]'s Anger Point raised its Attack!"
- Critical hit: "[Pokemon]'s Attack was maximized!"

### Strategic Applications:
1. **Defensive Pivot**: Converts chip damage into offensive pressure
2. **Crit-fishing Counter**: Turns opponent's critical hits against them
3. **Snowball Potential**: Each hit makes the Pokemon more dangerous
4. **Multi-hit Punishment**: Skill Link users accidentally boost the opponent multiple times

### Notable Users in Elite Redux:
- **Primeape Evolution Line**: Natural aggressive temperament
- **Machamp**: Mega form gains Anger Point as innate ability
- **Lycanroc-Midnight**: Competitive sets use Life Orb + Anger Point
- **Pinsir**: Mega evolution strategies
- **Tauros Variants**: Regional forms with different typings
- **Various Fighting-types**: Thematically appropriate for brawlers

### Competitive Considerations:
**Strengths:**
- Guaranteed activation on any hit (no RNG unlike other abilities)
- Critical hit punishment is severe (+6 Attack instantly)
- Stacks with held items like Life Orb or Choice Band
- Works well with priority moves for revenge killing

**Weaknesses:**
- Requires taking damage to activate
- Vulnerable to special attackers if Pokemon has low Special Defense
- Clear Body, White Smoke prevent stat reductions but don't help here
- Mold Breaker ignores this ability entirely

### Synergistic Moves:
- **Stone Edge/Cross Chop**: High crit ratio moves become risky to use against Anger Point
- **Priority moves**: Mach Punch, Quick Attack for immediate revenge
- **Recovery moves**: Rest, Roost to stay healthy while accumulating boosts
- **Setup moves**: Swords Dance becomes redundant but Substitute can help

### Counter-Strategies:
- **Special attacks**: Bypass the Attack boosts entirely
- **Status moves**: Thunder Wave, Will-O-Wisp don't trigger ability
- **Indirect damage**: Poison, burn, Stealth Rock chip damage
- **Mold Breaker**: Completely ignores the ability
- **Clear Smog/Haze**: Reset stat changes after they accumulate

### Version History:
- **Gen 4-5**: Original implementation with critical hit maximization
- **Gen 6+**: Standardized to current mechanics
- **Elite Redux**: Enhanced with consistent trigger conditions and interaction clarity
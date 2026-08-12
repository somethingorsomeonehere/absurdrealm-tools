---
id: 51
name: Keen Eye
status: reviewed
character_count: 73
---

# Keen Eye - Ability ID 51

## In-Game Description
"Immune to accuracy drops. Grants a 1.2x accuracy boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents accuracy stat stage drops. All moves gain a 1.2x accuracy boost. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**KEEN EYE** is a dual-purpose ability that provides both offensive accuracy enhancement and defensive stat protection.

### Accuracy Enhancement:
- **Boost**: All moves gain 1.2x accuracy multiplier
- **Application**: Multiplicative with base accuracy (100% to 120%, 85% to 102%, 70% to 84%)
- **Priority**: ACCURACY_MULTIPLICATIVE - applies after base accuracy calculations
- **Stacking**: Can stack with other accuracy boosts (e.g., X Accuracy items, Compound Eyes)

### Stat Protection:
- **Immunity**: Completely prevents accuracy stat reductions
- **Affected Moves**: Blocks Sand Attack, Smokescreen, Octazooka, Muddy Water, and any other accuracy-lowering effects
- **Mechanism**: Checked in battle_script_commands.c during stat modification attempts
- **Evasion**: Does NOT prevent opponent's evasion increases (Double Team still works against Keen Eye users)

### Technical Implementation:
```c
constexpr Ability KeenEye = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        *accuracy *= 1.2;
        return ACCURACY_MULTIPLICATIVE;
    },
    .breakable = TRUE,
};
```

**Stat Protection Code** (in battle_script_commands.c):
```c
// Line 4057: Prevents accuracy reductions
(BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_KEEN_EYE) && currStat == STAT_ACC)

// Line 9713: Shows ability popup when protection activates
(BATTLER_HAS_ABILITY(battler, ABILITY_KEEN_EYE) && statId == STAT_ACC && 
 (gBattleScripting.abilityPopupOverwrite = ABILITY_KEEN_EYE))
```

### Move Synergies:
1. **Thunder** (70% to 84% accuracy) - Excellent for rain teams
2. **Blizzard** (70% to 84% accuracy) - Reliable outside hail
3. **Focus Blast** (70% to 84% accuracy) - Much more consistent
4. **Stone Edge** (80% to 96% accuracy) - Near-perfect accuracy
5. **High Jump Kick** (90% to 108% accuracy) - Cannot miss when boosted

### Interaction Rules:
- **vs Evasion**: Ignores opponent's evasion boosts only if target has higher evasion stage
- **vs Accuracy Drops**: Completely immune to Sand Attack, Smokescreen, etc.
- **vs Mold Breaker**: Ability is breakable - Mold Breaker ignores both accuracy boost and stat protection
- **vs Minds Eye**: Similar stat protection, but Minds Eye also hits Ghost types normally

### Counters and Limitations:
1. **Mold Breaker family**: Turboblaze, Teravolt, Mold Breaker all bypass Keen Eye
2. **Evasion boosts**: Double Team, Minimize can still reduce hit chance
3. **Weather effects**: Sand Veil, Snow Cloak still function against Keen Eye users
4. **Breakable**: Unlike abilities like Clear Body, Keen Eye can be suppressed

### Competitive Analysis:
- **Tier Placement**: Utility ability, excellent on glass cannons needing move reliability
- **Common Users**: Flying-types (as innate ability), mixed attackers, Pokemon with powerful but inaccurate moves
- **Team Synergy**: Pairs well with choice items to ensure key moves connect
- **Meta Relevance**: Valuable in formats where accuracy is crucial (no evasion clause)

### Notable Pokemon with Keen Eye:
- **Pidgey line**: Innate ability, synergizes with Hurricane and Heat Wave
- **Tornadus forms**: Innate ability, excellent with Focus Blast and Hurricane
- **Various Fire/Fighting types**: Regular ability, helps with Focus Blast and Fire Blast consistency
- **Many Bird Pokemon**: Innate ability, commonly paired with Flock ability

### Calculation Examples:
- Thunder: 70% x 1.2 = 84% accuracy
- Focus Blast: 70% x 1.2 = 84% accuracy  
- Stone Edge: 80% x 1.2 = 96% accuracy
- Fire Blast: 85% x 1.2 = 102% accuracy (effectively 100%)
- Blizzard: 70% x 1.2 = 84% accuracy (outside hail)

### Version History:
- **Gen 3-4**: Only prevented accuracy reductions
- **Gen 5+**: Added evasion ignoring (implemented differently in Elite Redux)
- **Elite Redux**: Provides 1.2x accuracy boost instead of evasion ignoring, maintains stat protection

### Strategic Usage:
1. **Setup Sweepers**: Ensures key moves like Focus Blast connect during setup
2. **Choice Users**: Guarantees important coverage moves hit when locked in
3. **Weather Teams**: Thunder/Blizzard become much more reliable outside their ideal weather
4. **Anti-Evasion**: Partially counters evasion strategies through superior accuracy
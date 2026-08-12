---
id: 700
name: Color Spectrum
status: reviewed
character_count: 97
---

# Color Spectrum - Ability ID 700

## In-Game Description
"Same-type attacks get a 1.2x boost. Changes type each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

STAB moves are boosted by 20%. The user changes to a random Pure type at the start of every turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Color Spectrum is a unique ability that combines type-changing mechanics with modified STAB (Same-Type Attack Bonus). It provides unpredictability while maintaining offensive relevance through guaranteed type matching.

### Activation Conditions
- **STAB modifier**: Provides 1.2x damage multiplier for same-type attacks (reduced from normal 1.5x)
- **Type change timing**: Triggers at the end of each turn automatically
- **Type selection**: Randomly selects from all available types except:
  - TYPE_MYSTERY
  - TYPE_STELLAR  
  - Current type (prevents staying the same type)

### Technical Implementation
```c
// Color Spectrum implementation from abilities.cc
constexpr Ability ColorSpectrum = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        int newType;
        do {
            newType = Random() % NUMBER_OF_MON_TYPES;
        } while (newType == TYPE_MYSTERY || newType == TYPE_STELLAR || IS_BATTLER_OF_TYPE(battler, newType));

        gBattleMons[battler].type1 = newType;
        gBattleMons[battler].type2 = newType;
        gBattleMons[battler].type3 = TYPE_MYSTERY;
        PREPARE_TYPE_BUFFER(gBattleTextBuff1, newType);
        BattleScriptPushCursorAndCallback(BattleScript_AttackerBecameTheTypeFullEnd3);
        return TRUE;
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (StabMultiplierInHalves(battler, moveType, move) > 2) MUL(1.2);
        },
};
```

### Important Interactions
- **Dual typing**: Both type1 and type2 become the new type (pure typing)
- **type3 reset**: Third type slot is reset to TYPE_MYSTERY
- **STAB calculation**: Only applies the 1.2x multiplier when STAB would normally apply
- **Type effectiveness**: Resistances and weaknesses change each turn
- **Move type**: Doesn't affect the types of moves, only the user's typing

### Strategic Implications
- **Unpredictability**: Opponents can't predict resistances/weaknesses
- **STAB trade-off**: Weaker STAB (1.2x vs 1.5x) for guaranteed type matching
- **Coverage variety**: Effectively has access to all type matchups over time
- **Defensive uncertainty**: Type changes affect incoming damage calculations
- **Move selection**: Benefits from diverse move pools to match changing types

### Timing Considerations
- **Turn order**: Type change happens at end of turn, after damage calculation
- **Next turn**: New type is active for the following turn's calculations
- **Battle messages**: Displays type change message when it occurs
- **Status effects**: Type change doesn't affect existing status conditions

### Optimal Usage
- **Broad movepool**: Pokemon with diverse move types benefit most
- **Unpredictable attacker**: Excellent for catching opponents off-guard
- **Coverage moves**: Can potentially get STAB on any move type
- **Defensive mixup**: Changing resistances/weaknesses each turn
- **Late-game**: More effective as battle progresses and predictions become harder

### Potential Drawbacks
- **Reduced STAB**: 1.2x multiplier is weaker than standard 1.5x
- **Random nature**: Can change to disadvantageous types
- **No control**: Player can't influence type selection
- **Prediction difficulty**: Harder to plan your own strategies around
- **Type-specific moves**: Abilities that require specific types may be unreliable

### Synergies
- **Multi-type movesets**: Pokemon with Normal, Fighting, Flying, Electric, etc. moves
- **Adaptability**: Can complement other type-changing abilities
- **Coverage moves**: Shadow Ball, Thunderbolt, Ice Beam, etc.
- **Neutral moves**: Normal-type moves gain STAB when becoming Normal-type

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Type-locking moves**: Moves that lock typing (though rare)
- **Prediction-independent strategies**: Status moves, entry hazards
- **Priority moves**: Less affected by type changes
- **Multi-hit moves**: Type matters less with guaranteed damage

### Competitive Viability
- **Surprise factor**: High unpredictability value
- **Coverage efficiency**: Potential STAB on diverse moves
- **Meta disruption**: Difficult to prepare counters for
- **Risk/reward**: Balanced by reduced STAB multiplier
- **Longevity**: More valuable in longer battles

### Version History
- Elite Redux exclusive ability
- ID 700 in the ability list
- Combines type-changing with modified STAB mechanics
- Part of the expanded 700+ ability roster
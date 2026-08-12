---
id: 330
name: Majestic Moth
status: reviewed
character_count: 94
---

# Majestic Moth - Ability ID 330

## In-Game Description
"Boosts highest stat by 1 stage upon entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Majestic Moth raises the user's highest calculated base stat by 1 stage when it enters battle. 

## Detailed Mechanical Explanation

### Overview
Majestic Moth is an entry-triggered ability that automatically boosts the Pokemon's highest calculated stat by one stage when it enters battle. This ability provides immediate value by enhancing the Pokemon's strongest attribute.

### Mechanics

### Core Functionality
- **Trigger**: Activates when the Pokemon enters battle (switching in or battle start)
- **Effect**: Raises the highest calculated stat by +1 stage
- **Stat Analysis**: Considers all five battle stats (Attack, Defense, Special Attack, Special Defense, Speed)
- **Calculation**: Includes current stat stage modifiers when determining the highest stat

### Implementation Details
```cpp
constexpr Ability MajesticMoth = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(ChangeStatBuffs(battler, 1, GetHighestStatId(battler, TRUE), MOVE_EFFECT_AFFECTS_USER, NULL))
        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        return TRUE;
    },
};
```

### Stat Determination Process
1. **Stat Calculation**: Uses `GetHighestStatId(battler, TRUE)` with `includeStatStages = TRUE`
2. **Current Values**: Considers base stats + current stat stage modifiers
3. **Stage Multipliers**: Factors in stage boosts/drops using `gStatStageRatios`
4. **Selection**: Chooses the stat with the highest final calculated value
5. **Boost Application**: Applies +1 stage boost to the selected stat

### Important Notes
- The ability considers **current** stat stages when determining the highest stat
- If a Pokemon has +2 Attack stages but higher base Special Attack, it will boost whichever has the higher calculated total
- The boost is applied immediately upon entry, before any other entry effects
- Cannot boost HP (only the five battle stats are considered)

## Pokemon with Majestic Moth

### Primary Users (Innate Ability)
- **Venomoth line**: Offensive moth Pokemon that benefit from boosting their highest attacking stat
- **Volcarona variants**: Powerful special attackers that typically boost Special Attack
- **Dustox line**: Defensive moths that may boost Defense or Special Defense
- **Frosmoth line**: Ice-type moths with varied stat distributions
- **Paradox Moths**: Future/past variants with unique stat spreads

### Usage Patterns
- Most moths have high Special Attack, so they typically boost Special Attack
- Defensive variants may boost Defense or Special Defense depending on their spread
- Speed-oriented builds may boost Speed if it's their highest calculated stat

## Competitive Analysis

### Strengths
- **Immediate Value**: Provides an instant +1 boost without setup
- **Adaptive**: Boosts the most relevant stat for each individual Pokemon
- **Stacking**: Can work with existing stat boosts to determine the best stat to enhance
- **Reliability**: Always activates on entry, no conditions required

### Strategic Applications
- **Sweeper Support**: Enhances offensive stats for immediate pressure
- **Defensive Pivoting**: Boosts defensive stats when switching into threats
- **Speed Control**: Can boost Speed for faster Pokemon to maintain priority
- **Stat Stage Synergy**: Works well with moves that provide additional stat boosts

### Limitations
- **One-Time Effect**: Only activates on entry, not repeatedly
- **Predictable**: Opponents can anticipate which stat will be boosted
- **Stage Dependency**: Less effective if the Pokemon already has high stat stages
- **No HP Boost**: Cannot improve overall bulk through HP increases

## Interactions and Synergies

### Positive Interactions
- **Baton Pass**: Can pass the boosted stat to teammates
- **Stat Boost Moves**: Stacks with self-boosting moves for greater effect
- **Choice Items**: Provides initial boost before Choice item lock-in
- **Weak Armor/Stamina**: Can benefit from defensive stat boosts before taking damage

### Potential Conflicts
- **Clear Smog/Haze**: Stat boosts can be reset by these moves
- **Intimidate**: May alter Attack calculations before Majestic Moth triggers
- **Contrary**: Would lower the highest stat instead of raising it

## Optimal Usage

### Team Building
- **Stat Spreads**: Design EV spreads to influence which stat gets boosted
- **Move Synergy**: Pair with moves that benefit from the likely boosted stat
- **Entry Timing**: Switch in at optimal moments to maximize the boost's impact
- **Role Definition**: Clear offensive or defensive role helps predict boost target

### Prediction and Counterplay
- **Stat Analysis**: Opponents can predict which stat will be boosted by examining the Pokemon's stats
- **Timing Awareness**: Entry timing becomes crucial for both user and opponent
- **Stat Reset Moves**: Clear Smog, Haze, or Roar can remove the boost
- **Phazing**: Forcing switches can waste the entry boost

## Technical Implementation

### Function Flow
1. `OnEntry` trigger activates when Pokemon enters battle
2. `GetHighestStatId(battler, TRUE)` determines which stat to boost
3. `ChangeStatBuffs` applies the +1 stage increase
4. Battle script displays the stat boost message
5. Effect completes and battle continues

### Error Handling
- Uses `CHECK` macro to ensure stat boost is possible
- Fails gracefully if stat cannot be boosted (e.g., already at +6)
- Proper battle script integration for visual feedback

### Performance Considerations
- Minimal computational overhead
- Single function call for stat determination
- Standard stat boost mechanics integration


---
id: 394
name: Lethargy
status: reviewed
character_count: 106
---

# Lethargy - Ability ID 394

## In-Game Description
"Damage drops 20% each turn to 20%. Resets on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces the user's total damage by 20% at the start of each turn, capping at -80%. Resets after switching.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- **Stat Reset**: All stat changes (both positive and negative) are cleared upon switching in
- **Timer System**: Uses a 5-turn countdown timer that begins upon entry
- **Damage Reduction**: Offensive moves have drastically reduced power during the timer period
- **Gradual Recovery**: Power slowly increases each turn following a specific pattern
- **Switch Reset**: Timer resets to 5 whenever the Pokemon switches back in

**Technical Implementation:**
```cpp
constexpr Ability Lethargy = {
    .onEntry = +[](ON_ENTRY) -> int {
        TryResetBattlerStatChanges(battler, RESET_ALL_STATS);
        gVolatileStructs[battler].slowStartTimer = 5;
        BattleScriptPushCursorAndCallback(BattleScript_LethargyEnters);
        return TRUE;
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            switch (gVolatileStructs[battler].slowStartTimer) {
                case 0:
                case 1:
                    MUL(.2);
                    return;

                case 2:
                    MUL(.4);
                    return;

                case 3:
                    MUL(.6);
                    return;

                case 4:
                    MUL(.8);
                    return;
            }
        },
};
```
*Location: /Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc (lines 4052-4080)*

**Damage Multiplier Schedule:**
- **Turn 1-2 (Timer 5-4)**: 20% damage (.2x multiplier)
- **Turn 3 (Timer 3)**: 40% damage (.4x multiplier)  
- **Turn 4 (Timer 2)**: 60% damage (.6x multiplier)
- **Turn 5 (Timer 1)**: 80% damage (.8x multiplier)
- **Turn 6+ (Timer 0)**: 100% damage (no multiplier)

**Key Differences from Slow Start:**
- **Lethargy**: Only affects offensive power, not stats or speed
- **Slow Start**: Halves Attack, Special Attack, and Speed stats
- **Lethargy**: Clears all stat changes on entry
- **Slow Start**: No stat clearing effect
- **Lethargy**: Different damage reduction pattern (20/40/60/80% vs 50%)

**Damage Calculation Examples:**
```
Base move power: 100
Turn 1-2: 100 x 0.2 = 20 effective power
Turn 3:   100 x 0.4 = 40 effective power  
Turn 4:   100 x 0.6 = 60 effective power
Turn 5:   100 x 0.8 = 80 effective power
Turn 6+:  100 x 1.0 = 100 effective power
```

## Strategic Analysis

**Advantages:**
1. **Stat Reset Utility**: Can clear negative stat changes imposed by opponents
2. **Late-Game Power**: Eventually reaches full offensive potential
3. **Unpredictable**: Opponents may underestimate damage output in later turns

**Disadvantages:**
1. **Severe Early Weakness**: Nearly useless offensively for the first 2 turns
2. **Switch Vulnerability**: Any switching resets the entire recovery process
3. **Long Recovery**: Takes 5 full turns to reach maximum power
4. **No Defensive Benefits**: Provides no protection during vulnerable early turns

## Competitive Applications

**Usage Scenarios:**
- **Stall Teams**: Can function as a defensive pivot that eventually gains offensive presence
- **Setup Sweepers**: May work with extremely bulky Pokemon that can survive the early turns
- **Specific Counters**: Against setup opponents where stat clearing is valuable

**Team Support Required:**
- **Entry Hazard Control**: Essential to preserve HP during weak turns
- **Defensive Support**: Screens, Wish support, or defensive pivots
- **Switch Control**: Abilities or moves that prevent forced switching
- **Status Protection**: Sleep Talk or status immunity to avoid disruption

## Comparison with Related Abilities

**Similar Mechanics:**
- **Slow Start (ID 112)**: Also uses timer system but affects stats instead of damage
- **Truant (ID 54)**: Another severely limiting ability with periodic effects
- **Defeatist (ID 129)**: Conditional damage reduction based on HP

**Key Distinctions:**
- Most restrictive early-game ability in terms of offensive output
- Only ability that combines stat clearing with gradual power recovery
- Unique 5-stage damage progression system

## Competitive Notes

**Viability Assessment:**
- **Singles**: Very poor due to switch frequency and offensive pressure
- **Doubles**: Even worse due to faster pace and immediate threats
- **Specialized Formats**: May have niche applications in specific rulesets

**Common Strategies:**
- **Defensive Investment**: Maximum HP/Defense to survive early turns
- **Recovery Moves**: Essential for staying alive during vulnerability period  
- **Support Moves**: Focus on utility rather than offense initially
- **Prediction**: Switch timing becomes critical to avoid timer resets

**Interaction Notes:**
- Timer persists through status conditions and weather
- Damage reduction applies to all offensive moves regardless of type or category
- Stat clearing occurs before the timer is set, ensuring clean slate
- No interaction with abilities that modify damage calculations (stacks multiplicatively)

## Recommended Pokemon

**Ideal Candidates:**
- Extremely bulky Pokemon with high HP and defensive stats
- Pokemon with access to reliable recovery moves
- Pokemon that can function with support/utility moves early game
- Pokemon with powerful offensive movesets to capitalize on late-game power

**Poor Candidates:**
- Fast, frail offensive Pokemon
- Pokemon reliant on early-game pressure
- Setup sweepers that need immediate offensive presence
- Pokemon without recovery or defensive utility moves
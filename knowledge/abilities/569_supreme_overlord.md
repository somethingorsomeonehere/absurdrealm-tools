---
id: 569
name: Supreme Overlord
status: reviewed
character_count: 177
---

# Supreme Overlord - Ability ID 569

## In-Game Description
"Each fainted ally increases Attack and SpAtk by 10%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Attack and Special Attack by 10% for each fainted ally on your side, capped at 5 allies maximum for a 50% boost to both stats. Stacks additively with other damage boosts.

## Detailed Mechanical Explanation
*For Discord/reference use*

Supreme Overlord is a powerful late-game ability that converts team losses into offensive power. Here's how it works:

### Core Mechanics
- **Stat Boost**: Increases both Attack and Special Attack by 10% per fainted ally
- **Maximum Cap**: Limited to 5 fainted allies (50% boost maximum)
- **Activation Condition**: Only activates when `gFaintedMonCount[GetBattlerSide(battler)] > 0`
- **Side-Based**: Only counts fainted allies on the same side (player vs opponent)

### Technical Implementation
```cpp
// Entry check - only announces if there are fainted allies
CHECK(gFaintedMonCount[GetBattlerSide(battler)])

// Stat calculation with 5-ally cap
if (statId == STAT_ATK || statId == STAT_SPATK) 
    *stat = *stat * (10 + min(5, gFaintedMonCount[GetBattlerSide(battler)])) / 10;
```

### Boost Breakdown
- **1 fainted ally**: 10% boost (1.1x multiplier)
- **2 fainted allies**: 20% boost (1.2x multiplier) 
- **3 fainted allies**: 30% boost (1.3x multiplier)
- **4 fainted allies**: 40% boost (1.4x multiplier)
- **5+ fainted allies**: 50% boost (1.5x multiplier, capped)

### Affected Stats
- **Attack**: Physical moves get damage boost
- **Special Attack**: Special moves get damage boost
- **Other stats**: Unaffected (Defense, Special Defense, Speed, etc.)

### Activation Requirements
- At least one ally must have fainted during the battle
- The ability holder must be switched in after allies have fainted
- Switch-in announcement occurs when conditions are met

### Strategic Applications
- **Revenge Sweeper**: Ideal for cleaning up after team losses
- **Late-Game Powerhouse**: Becomes stronger as the battle progresses
- **Mixed Attackers**: Benefits both physical and special movesets equally
- **Endgame Scenarios**: Particularly powerful in 6v6 battles where multiple faints are common

### Damage Calculation Example
Base 100 Attack/Special Attack Pokemon with Supreme Overlord:
- **0 fainted**: 100 Attack/SpAtk (ability inactive)
- **1 fainted**: 110 Attack/SpAtk
- **2 fainted**: 120 Attack/SpAtk
- **3 fainted**: 130 Attack/SpAtk
- **4 fainted**: 140 Attack/SpAtk
- **5+ fainted**: 150 Attack/SpAtk (maximum)

### Common Users in Elite Redux
- Found as an innate ability on several Ghost and Dark-type Pokemon
- Often paired with offensive movesets and revenge-focused strategies
- Particularly effective on Pokemon with diverse move pools (mixed attackers)

### Competitive Implications
- **High Risk, High Reward**: Requires team sacrifices for maximum power
- **Momentum Shift**: Can turn losing positions into winning ones
- **Endgame Threat**: Forces opponents to play cautiously around late-game sweeps
- **Team Building**: Encourages aggressive early-game play to set up late-game revenge

### Interactions with Other Mechanics
- **Stacks multiplicatively** with other stat boosts (items, moves, etc.)
- **Works with both physical and special moves** equally
- **No interaction with status moves** (doesn't boost status move effects)
- **Persists through switches** as long as fainted count remains

### Counters and Limitations
- **Prevention**: Avoiding knockouts prevents the ability from activating
- **Priority Moves**: Can bypass the boosted stats with priority attacks
- **Status Effects**: Burn halves physical damage despite Attack boost
- **Defensive Strategies**: Walls can still tank boosted attacks
- **Speed Control**: Supreme Overlord doesn't boost Speed, leaving it vulnerable to faster threats

### Version History
- Introduced as part of Elite Redux's expanded ability roster
- Designed to create dramatic late-game scenarios and reward aggressive play
- Balanced with the 5-ally cap to prevent excessive snowballing

Supreme Overlord embodies the "never give up" mentality, turning desperate situations into opportunities for dramatic comebacks through the power of fallen allies.
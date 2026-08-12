---
id: 479
name: Dust Cloud
status: reviewed
character_count: 105
---

# Dust Cloud - Ability ID 479

## In-Game Description
"Attacks with Sand Attack on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Sand Attack on the opponent upon switching into battle, reducing the target's accuracy by one stage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dust Cloud is an entry hazard ability that automatically executes Sand Attack when the Pokemon switches into battle. This provides immediate accuracy disruption to the opposing Pokemon.

### Activation Conditions
- **Trigger**: Activates upon switching into battle
- **Target**: Automatically targets the opposing Pokemon
- **Move used**: Sand Attack (Ground-type status move)
- **Accuracy**: 100% accuracy (Sand Attack base accuracy)
- **Effect**: Reduces target's accuracy by 1 stage

### Technical Implementation
```c
constexpr Ability DustCloud = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_SAND_ATTACK, 0); 
    },
};
```

The UseEntryMove function handles the mechanics:
- Finds a valid opposing target
- Queues Sand Attack as an extra attack
- Uses 0 power (status move)
- Executes with 100% accuracy

### Sand Attack Move Details
- **Type**: Ground
- **Category**: Status
- **Power**: N/A (status move)
- **Accuracy**: 100%
- **PP**: 15 (not relevant for ability use)
- **Effect**: Lowers target's accuracy by 1 stage
- **Target**: Selected opponent

### Accuracy Stage Mechanics
- **Stage reduction**: -1 accuracy stage
- **Accuracy multiplier**: Each stage down reduces accuracy by ~16.67%
- **Stage -1**: 83.33% accuracy (5/6 multiplier)
- **Cumulative**: Can stack with other accuracy debuffs
- **Duration**: Persists until switched out or cured

### Important Interactions
- **Keen Eye**: Immune to accuracy reduction, making this ability ineffective
- **Clear Body/White Smoke**: Immune to stat reductions
- **Contrary**: Will increase accuracy instead of decreasing it
- **Defiant/Competitive**: May trigger attack/special attack boosts
- **Substitute**: Sand Attack cannot hit through Substitute
- **Ghost types**: Not immune (Sand Attack is Ground-type but targets all types)

### Activation Timing
- **Entry order**: Activates immediately upon switch-in
- **Priority**: Uses the extra attack system
- **Interruption**: Can be interrupted by faster priority moves
- **Multi-target**: In doubles, targets one opposing Pokemon

### Strategic Applications
- **Sweeper disruption**: Reduces accuracy of setup sweepers
- **Stall support**: Helps stall teams by causing missed attacks
- **Revenge killing**: Makes faster threats less reliable
- **Entry deterrent**: Discourages certain switch-ins
- **Passive utility**: Provides value without turn investment

### Limitations
- **One-time use**: Only activates once per switch-in
- **Accuracy immunity**: Hard countered by Keen Eye users
- **Status move**: Doesn't deal damage
- **Predictable**: Opponents know it's coming
- **Substitute**: Blocked by Substitute

### Common Counters
- **Keen Eye**: Complete immunity to accuracy reduction
- **Clear Body/White Smoke**: Prevents stat reduction
- **Substitute**: Blocks the Sand Attack
- **Rapid switching**: Resets accuracy stages
- **Haze/Clear Smog**: Removes accuracy debuffs

### Synergies
- **Stall teams**: Pairs well with defensive strategies
- **Entry hazards**: Combines with Stealth Rock/Spikes
- **Status spreaders**: Works with other disruptive abilities
- **Pivot moves**: U-turn/Volt Switch for repeated use
- **Accuracy-reducing moves**: Stacks with Muddy Water, Hurricane, etc.

### Competitive Usage
- **Niche utility**: Situational disruption tool
- **Anti-setup**: Counters accuracy-dependent setup sweepers
- **Prediction value**: Forces opponents to consider accuracy issues
- **Team support**: Provides passive utility for defensive teams

### Version History
- Custom ability in Elite Redux
- Based on the entry move system used by other abilities
- Uses standard Sand Attack mechanics with automatic targeting
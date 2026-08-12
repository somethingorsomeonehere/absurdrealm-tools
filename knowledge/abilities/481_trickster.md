---
id: 481
name: Trickster
status: reviewed
character_count: 138
---

# Trickster - Ability ID 481

## In-Game Description
"Uses Disable on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Disable on switch-in. Disable prevents the target from using their last-used move for 4 turns. Fails if the target has not moved yet.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Trickster is a disruptive entry ability that automatically casts Disable when switching into battle. This creates immediate pressure by limiting the opponent's moveset upon entry.

### Activation Conditions
- **Trigger**: Activates on switch-in (onEntry)
- **Target selection**: Targets the first alive opponent found
  - Checks opposing side positions in order
  - Must find at least one alive opponent to activate
- **Move execution**: Uses the actual Disable move with all its properties

### Technical Implementation
```c
// Trickster implementation in abilities.cc
constexpr Ability Trickster = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_DISABLE, 0); 
    },
};
```

The UseEntryMove function:
- Finds the first alive opponent
- Queues Disable as an extra attack
- Uses standard move targeting and execution
- Returns true if successful, false if no valid targets

### Disable Move Details
From MoveList.textproto:
- **Type**: Normal-type status move
- **Accuracy**: 100% (cannot miss)
- **PP**: 20 (not relevant for ability usage)
- **Effect**: EFFECT_DISABLE
- **Target**: Selected opponent
- **Description**: "Psychically disables one of the foe's moves"
- **Duration**: Several turns (typically 4-7 turns)

### Important Interactions
- **Move selection**: Targets the opponent's last-used move
- **No previous move**: If opponent hasn't used a move yet, Disable fails
- **Multiple opponents**: Only targets one opponent (first alive found)
- **Accuracy**: 100% accurate when used by Trickster
- **Timing**: Occurs immediately on switch-in before other actions
- **Ability suppression**: Doesn't work if ability is suppressed

### Strategic Applications
- **Lead disruption**: Excellent on lead Pokemon to disable setup moves
- **Revenge killer**: Disable the move that KO'd your previous Pokemon
- **Stall breaking**: Disable recovery moves or key defensive options
- **Pivot support**: Disable threats before pivoting out
- **Momentum control**: Force opponent into suboptimal plays

### Target Priority Logic
```c
// Target selection from UseEntryMove in battle_util.c
int opposingBattler = BATTLE_OPPOSITE(battler);
for (i = 0; i < 2; opposingBattler ^= BIT_FLANK, i++) {
    if (IsBattlerAlive(opposingBattler)) {
        target = opposingBattler;
        break;
    }
}
```

### Competitive Usage Notes
- **Entry hazard synergy**: Combines well with hazard setting
- **U-turn/Volt Switch**: Create disable pressure then pivot
- **Choice item counters**: Disable the locked-in move
- **Setup prevention**: Stop dangerous setup sweepers
- **Psychic immunity**: Doesn't affect Dark-type opponents (Disable is affected by type immunity)

### Limitations
- **Single use per switch-in**: Only activates once when entering
- **Requires previous move**: Target must have used a move to disable
- **Single target**: Can't disable multiple opponents simultaneously
- **Type immunity**: Dark-types are immune to Disable (Normal-type move blocked by Dark immunity)
- **Substitute**: Blocked by Substitute
- **Mental Herb**: Target can use Mental Herb to cure Disable

### Counters
- **Dark-type Pokemon**: Immune to Disable due to type immunity
- **Substitute**: Blocks the Disable effect
- **Mental Herb**: Cures Disable immediately
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Switching**: Target can switch out to escape Disable
- **Taunt immunity**: Some abilities prevent status moves

### Synergies
- **Entry hazards**: Stealth Rock, Spikes for chip damage
- **Pivot moves**: U-turn, Volt Switch, Flip Turn
- **Status moves**: Combine with other disruptive status
- **Pursuit trappers**: Trap opponents forced into bad positions
- **Setup sweepers**: Create opportunities for teammates to set up

### Battle Format Considerations
- **Singles**: Highly effective for momentum control
- **Doubles**: Less reliable due to multiple targets and faster pace
- **Switching games**: Excellent in formats with frequent switching
- **Stall teams**: Disrupts opposing stall strategies effectively

### Similar Abilities
- **Other entry abilities**: Intimidate, Download, Trace (different effects)
- **Status on entry**: None others specifically use status moves
- **Disable effects**: Only Cursed Body triggers Disable on contact

### Version History
- Elite Redux custom ability
- Part of the extended ability system (480+ IDs)
- Designed for disruptive switch-in pressure
- Uses the standard Disable move mechanics
---
id: 577
name: Sharing Is Caring
status: reviewed
character_count: 90
---

# Sharing Is Caring - Ability ID 577

## In-Game Description
"Stat changes are shared between all battlers."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All stat changes are shared between all battlers on the field, both positive and negative.

## Detailed Mechanical Explanation
*For Discord/reference use*

**SHARING IS CARING** is a unique field-effect ability that ensures all stat changes are immediately copied to every battler on the field.

### Activation Mechanics:
- **Trigger**: onReactive hook - responds to any stat change on the field
- **Scope**: Affects ALL battlers (both teams, singles and doubles)
- **Timing**: Stat copying happens immediately after any stat change
- **Script**: Uses BattleScript_PerformCopyStatEffects for visual feedback

### State Machine System:
The ability uses a three-state tracking system:
1. **STAT_STAGE_CHECK_NOT_NEEDED** (0): No pending stat changes
2. **STAT_STAGE_CHECK_NEEDED** (1): Stat changes detected, need copying
3. **STAT_STAGE_CHECK_IN_PROGRESS** (2): Currently copying stats

### Execution Flow:
1. Any battler's stats change (boost or drop)
2. System flags statStageCheckState as CHECK_NEEDED
3. onReactive detects the flag and initiates copying
4. docopystatchange command copies stats to all battlers
5. State updates to prevent infinite loops

### What Gets Shared:
- **Attack/Defense/Sp.Atk/Sp.Def/Speed**: All stat stages
- **Accuracy/Evasion**: Also shared
- **Positive Changes**: Swords Dance, Calm Mind, Dragon Dance, etc.
- **Negative Changes**: Intimidate, Screech, Sticky Web, etc.
- **Net Result**: Everyone has identical stat modifiers

### Technical Implementation:
```c
// From abilities.cc
constexpr Ability SharingIsCaring = {
    .onReactive = +[](ON_REACTIVE) -> void {
        // Check state machine flag
        if (abilityState->statStageCheckState == STAT_STAGE_CHECK_NEEDED) {
            // Prevent re-triggering
            abilityState->statStageCheckState = STAT_STAGE_CHECK_IN_PROGRESS;
            // Execute stat copying script
            BattleScriptPushCursorAndCallback(BattleScript_PerformCopyStatEffects);
        }
    },
};
```

### Pokemon with Sharing is Caring:
1. **Fidough (Partner form)** - Changeable ability option
   - Support-oriented variant
   - Creates chaotic stat environments

2. **Gholdengo** - Changeable ability option
   - High base stats benefit from level playing field
   - Good As Gold synergy for status immunity

### Strategic Implications:

**Advantages:**
- Completely shuts down setup sweepers
- Intimidate affects the user's team too
- Sticky Web slows down the setter's team
- No stat advantage = base stats matter more

**Disadvantages:**
- Cannot use your own setup moves effectively
- Opponent's debuffs help them too
- Speed control becomes very difficult
- Team building heavily restricted

### Competitive Notes:
- **Anti-Meta**: Hard counters stat-boosting strategies
- **Base Stats Focus**: Pokemon with naturally high stats excel
- **Item Reliance**: Choice items become more valuable
- **Ability Synergy**: Unaware teammates ignore shared boosts
- **Move Selection**: Prioritize attacks over setup moves

### Interaction Examples:
- Dragon Dance: All Pokemon get +1 Atk/Spe
- Intimidate: All Pokemon get -1 Atk (including Intimidator's team)
- Close Combat: All Pokemon get -1 Def/SpD
- Sticky Web: All grounded Pokemon get -1 Spe on entry

### Similar Abilities:
- **Egoist**: Copies positive stat changes from opponents
- **Neutralizing Gas**: Suppresses abilities but not stat changes
- **Haze**: Move that resets stats, not an ability
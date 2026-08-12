---
id: 473
name: Inversion
status: reviewed
character_count: 214
---

# Inversion - Ability ID 473

## In-Game Description
"Sets up Inverse Room on entry, lasts 3 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Inversion automatically sets up Inverse Room when the user enters battle, lasting 3 turns. Inverse Room reverses all type effectiveness interactions - super-effective moves become not very effective and vice versa. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Inversion is a field-controlling ability that automatically establishes Inverse Room when the Pokemon enters battle. This fundamentally changes the battle dynamic by reversing all type effectiveness calculations for all Pokemon on the field.

### Activation Conditions
- **Trigger**: Activates automatically when the Pokemon with Inversion enters battle
- **Duration**: Exactly 3 turns (INVERSE_ROOM_DURATION_SHORT)
- **Field status**: Sets STATUS_FIELD_INVERSE_ROOM
- **Reactivation**: Cannot be triggered again while Inverse Room is already active

### Type Effectiveness Reversal
Inverse Room completely reverses the type effectiveness chart:
- **Super effective (2x) becomes Not very effective (0.5x)**
- **Not very effective (0.5x) becomes Super effective (2x)**
- **Normal effectiveness (1x) remains unchanged**
- **No effect (0x) remains no effect**

### Technical Implementation
```c
constexpr Ability InverseRoom = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gFieldStatuses & STATUS_FIELD_INVERSE_ROOM)
        
        gFieldTimers.started.inverseRoom = TRUE;
        gFieldStatuses |= STATUS_FIELD_INVERSE_ROOM;
        gFieldTimers.inverseRoomTimer = INVERSE_ROOM_DURATION_SHORT; // 3 turns
        BattleScriptPushCursorAndCallback(BattleScript_InversedRoomActivated);
        return TRUE;
    },
};
```

### Type Effectiveness Examples
With Inverse Room active:
- **Fire vs Water**: Normally not very effective (0.5x) to becomes super effective (2x)
- **Water vs Fire**: Normally super effective (2x) to becomes not very effective (0.5x)
- **Electric vs Ground**: Normally no effect (0x) to remains no effect (0x)
- **Normal vs Ghost**: Normally no effect (0x) to remains no effect (0x)
- **Fighting vs Normal**: Normally normal effectiveness (1x) to remains normal (1x)

### Battle Messages
- **On activation**: "{POKÉMON}'s Inverse Room set up Inverse Room!"
- **Field effect**: "The type effectiveness were inverted!"
- **On end**: "The inverted dimensions returned to normal!"

### Duration and Timing
- **Timer**: 3 turns from activation
- **End of turn**: Timer decreases at end of each turn
- **Permanent effects**: Some room moves can set permanent duration with special flags
- **Turn 0**: Activates immediately on entry, timer starts counting

### Important Interactions
- **Ability negation**: Disabled by Clueless ability being on the field
- **Miracle Eye**: Can interact with Inverse Room calculations (double negation)
- **Inverse Battle flag**: Game can have multiple inversion effects that interact
- **Multiple inversions**: Effects can stack or cancel each other out
- **Weather independence**: Works regardless of weather conditions
- **Entry hazards**: Does not affect entry hazard damage calculations

### Strategic Implications
- **Team building**: Requires complete rethinking of type matchups
- **Lead potential**: Excellent as a lead Pokemon to set field conditions
- **Coverage moves**: Previously resisted moves become super effective
- **Defensive typing**: Resistances become weaknesses and vice versa
- **Speed control**: 3-turn duration means limited window of opportunity

### Competitive Usage
- **Anti-meta potential**: Counters common type effectiveness strategies
- **Surprise factor**: Can catch opponents off-guard with reversed matchups
- **Team support**: Benefits teammates with normally poor type matchups
- **Short duration**: Limited 3-turn window requires immediate capitalize
- **One-time use**: Cannot reactivate during battle once field effect ends

### Counters and Limitations
- **Clueless ability**: Completely negates Inverse Room while on field
- **Field condition override**: Other room moves can replace Inverse Room
- **Switch timing**: Opponents can switch to better matchups during effect
- **Duration management**: Only 3 turns to capitalize on reversed effectiveness
- **Entry timing**: Vulnerable if switched in during opponent's attack turn

### Pokemon That Learn This Ability
Based on the ability's unique nature and implementation:
- Likely exclusive to specific legendary or mythical Pokemon
- Pokemon with reality-warping or dimension-controlling themes
- Psychic-type Pokemon with space/time manipulation abilities

### Synergies
- **Room moves**: Pairs with other room effects for field control
- **Trick Room**: Can combine with speed reversal for total battle reversal
- **Entry hazards**: Opponents may switch more, triggering hazard damage
- **U-turn/Volt Switch**: Pivot moves gain value with changing field conditions
- **Priority moves**: Become more valuable with unpredictable type matchups

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Field condition system**: Uses the same mechanics as Trick Room and Wonder Room
- **Duration balance**: 3-turn limit prevents overpowered field control
- **Entry activation**: Automatic trigger makes it immediately impactful

### Ability Suppression Effects
- **Mold Breaker line**: Does not prevent field effect once established
- **Neutralizing Gas**: Does not disable already active field conditions
- **Simple Beam/Worry Seed**: Changing ability doesn't remove field effect
- **Gastro Acid**: Suppressing ability doesn't end ongoing Inverse Room

### Technical Notes
- Uses the same timer system as other room effects
- Shares field status bit with Inverse Room move effect
- Prevented from activating if field status already set
- Integrates with existing type effectiveness calculation system
- Battle script system handles all messages and animations
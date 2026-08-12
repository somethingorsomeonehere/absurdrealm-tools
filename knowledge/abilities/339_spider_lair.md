---
id: 339
name: Spider Lair
status: reviewed
character_count: 215
---

# Spider Lair - Ability ID 339

## In-Game Description
"Sets Sticky Web hazard on opponent's field upon entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets Sticky Web on opponent's field when the user enters battle. Lasts 5 turns and lowers Speed by 1 stage for any grounded Pokemon switching in. Cannot activate if Sticky Web is already present on opponent's field. 

## Detailed Mechanical Explanation

### Overview

Spider Lair is a powerful entry hazard ability that automatically sets Sticky Web on the opponent's side of the field upon switching in. This ability provides immediate battlefield control by guaranteeing that any Pokemon the opponent switches in will have their Speed lowered by one stage.

## Mechanics

### Core Functionality
- **Trigger**: Activates immediately when the Pokemon enters battle
- **Effect**: Sets Sticky Web on the opponent's side of the field
- **Duration**: Exactly 5 turns, then automatically wears off
- **Speed Reduction**: -1 stage to any Pokemon switching into the hazard
- **Message**: "Spider Lair activated!" (STRINGID_SPIDERLAIRACTIVATED)

### Technical Implementation
Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` at lines 3586-3597:

```cpp
constexpr Ability SpiderLair = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gSideStatuses[BATTLE_OPPOSITE(battler)] & SIDE_STATUS_STICKY_WEB)

        int side = GetOppositeSide(battler);
        gSideTimers[side].started.spiderWeb = TRUE;
        gSideStatuses[side] |= SIDE_STATUS_STICKY_WEB;
        gSideTimers[side].stickyWebTimer = 5;
        BattleScriptPushCursorAndCallback(BattleScript_SpiderLairActivated);
        return TRUE;
    },
};
```

### Key Differences from Regular Sticky Web
1. **Automatic Setup**: No turn investment required - activates on entry
2. **Fixed Duration**: Always lasts exactly 5 turns, regardless of other factors
3. **Can't Stack**: If Sticky Web is already present, Spider Lair won't activate
4. **Timer-Based**: Uses `stickyWebTimer` mechanic for automatic removal

### Timer Mechanics
The ability utilizes the battle engine's side timer system (located in `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_util.c` lines 1716-1724):

```c
if (gSideStatuses[side] & SIDE_STATUS_STICKY_WEB) {
    if (!gSideTimers[side].started.spiderWeb && gSideTimers[side].stickyWebTimer && --gSideTimers[side].stickyWebTimer == 0) {
        gSideStatuses[side] &= ~SIDE_STATUS_STICKY_WEB;
        gBattleCommunication[MULTISTRING_CHOOSER] = BATTLE_OPPOSITE(side);
        PREPARE_MOVE_BUFFER(gBattleTextBuff1, MOVE_STICKY_WEB);
        BattleScriptExecute(BattleScript_SideStatusWoreOff);
        effect++;
    }
}
```

## Strategic Applications

### Offensive Applications
- **Speed Control**: Immediately slows down opponent's switch-ins
- **Momentum Preservation**: Forces opponent to deal with hazard or accept Speed drops
- **Sweeper Support**: Creates favorable Speed tiers for slower sweepers
- **Pivot Strategies**: Enhances the effectiveness of slow pivot Pokemon

### Defensive Applications
- **Switch Punishment**: Discourages opponent from switching freely
- **Stall Support**: Provides passive advantage for defensive teams
- **Revenge Killing**: Makes it easier to outspeed and revenge kill threats

### Team Synergy
- **Hazard Stacking**: Combines well with Spikes, Stealth Rock, and Toxic Spikes
- **Slow Sweepers**: Particularly effective with Pokemon that need Speed control
- **Bulky Pivots**: Enhances the utility of tanky Pokemon that switch in frequently

## Competitive Analysis

### Advantages
1. **Guaranteed Setup**: Unlike the move Sticky Web, this ability can't be prevented
2. **Action Economy**: Provides hazard control without spending a turn
3. **Immediate Impact**: Takes effect the moment the Pokemon enters battle
4. **Consistent Duration**: Always lasts exactly 5 turns for predictable timing

### Limitations
1. **Single Use**: Only activates once per battle entry
2. **Limited Duration**: Automatically expires after 5 turns
3. **No Stacking**: Cannot layer multiple Sticky Webs
4. **Flying/Levitate Immunity**: Some Pokemon are unaffected by the hazard

### Counterplay
- **Rapid Spin/Defog**: Can remove the hazard early
- **Flying-types**: Immune to Sticky Web effects
- **Levitate**: Immune to ground-based hazards
- **Heavy Duty Boots**: Prevents hazard damage and stat reduction
- **Magic Bounce**: Reflects the hazard back to the user's side

## Pokemon with Spider Lair

Spider Lair is available to 15 different Pokemon species, primarily those with spider-like characteristics or web-spinning themes. Notable users include:

- Various Ariados forms and regional variants
- Spider-themed Bug-type Pokemon
- Several Water/Bug dual-types with aquatic spider motifs
- Legendary and mythical Pokemon with web-manipulation abilities

## Related Abilities

### Spider Lair Upgrade (Ability #752)
- **Enhanced Version**: Lasts 7 turns instead of 5
- **Same Mechanics**: Identical functionality with extended duration
- **Located at**: Lines 7773-7784 in abilities.cc
- **Available to**: Select high-tier Pokemon as an upgrade option

### Synergistic Abilities
- **Web Spinner**: Creates additional web-based effects
- **Sticky Hold**: Prevents item removal, maintaining hazard effectiveness
- **Compound Eyes**: Improves accuracy of follow-up moves

## Battle Script Reference

The ability uses `BattleScript_SpiderLairActivated` (defined in `/Users/joel/Github/eliteredux/eliteredux-source/data/battle_scripts_1.s` lines 12030-12033):

```assembly
BattleScript_SpiderLairActivated::
	printstring STRINGID_SPIDERLAIRACTIVATED
	waitmessage B_WAIT_TIME_LONG
	end3
```

## Conclusion

Spider Lair represents a powerful entry hazard ability that provides immediate battlefield control through automatic Sticky Web setup. Its fixed 5-turn duration creates a strategic timing element that both users and opponents must consider. The ability excels in both offensive and defensive team compositions, making it a valuable tool for Pokemon that can utilize its speed control effects effectively.

The existence of Spider Lair Upgrade demonstrates the developers' recognition of this ability's strategic value, providing an enhanced version for higher-tier Pokemon while maintaining the core mechanical identity of temporary, automatic hazard control.
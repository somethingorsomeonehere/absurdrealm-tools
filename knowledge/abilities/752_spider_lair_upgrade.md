---
id: 752
name: Spider Lair Upgrade
status: reviewed
character_count: 215
---

# Spider Lair Upgrade - Ability ID 752

## In-Game Description
"Casts Sticky Web on entry. Lasts 7 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets Sticky Web on opponent's field when the user enters battle. Lasts 7 turns and lowers Speed by 1 stage for any grounded Pokemon switching in. Cannot activate if Sticky Web is already present on opponent's field.

## Detailed Mechanical Explanation
*For Discord/reference use*

Spider Lair Upgrade is the enhanced version of Spider Lair (Ability #339), providing extended battlefield control through automatic Sticky Web setup with increased duration.

### Core Mechanics
- **Trigger**: Activates immediately when the Pokemon enters battle
- **Effect**: Sets Sticky Web on the opponent's side of the field
- **Duration**: Exactly 7 turns (2 turns longer than regular Spider Lair)
- **Speed Reduction**: -1 stage to any Pokemon switching into the hazard
- **Cannot Stack**: If Sticky Web is already present, ability won't activate
- **Message**: "Spider Lair activated!" (same as regular Spider Lair)

### Technical Implementation
Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`:

```cpp
constexpr Ability SpiderLairUpgrade = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gSideStatuses[BATTLE_OPPOSITE(battler)] & SIDE_STATUS_STICKY_WEB)

        int side = GetOppositeSide(battler);
        gSideTimers[side].started.spiderWeb = TRUE;
        gSideStatuses[side] |= SIDE_STATUS_STICKY_WEB;
        gSideTimers[side].stickyWebTimer = 7;  // 7 turns vs 5 for regular Spider Lair
        BattleScriptPushCursorAndCallback(BattleScript_SpiderLairActivated);
        return TRUE;
    },
};
```

### Activation Conditions
1. Pokemon must enter battle (switching in, battle start, or revival)
2. Sticky Web must not already be present on opponent's side
3. Activates regardless of Pokemon's HP, status, or other conditions
4. Cannot be prevented by most abilities (unlike the move Sticky Web)

### Timer Mechanics
The ability uses the battle engine's side timer system for automatic removal:

```c
if (gSideStatuses[side] & SIDE_STATUS_STICKY_WEB) {
    if (!gSideTimers[side].started.spiderWeb && gSideTimers[side].stickyWebTimer && 
        --gSideTimers[side].stickyWebTimer == 0) {
        gSideStatuses[side] &= ~SIDE_STATUS_STICKY_WEB;
        // Message: "Sticky Web wore off!"
    }
}
```

### Sticky Web Effects on Switch-ins
When an opposing Pokemon switches in while Sticky Web is active:
- Speed stat is lowered by 1 stage (-50% at stage -1, -66% at stage -2, etc.)
- Effect applies to all Pokemon except those with:
  - Flying type or Levitate ability (immune to ground-based hazards)
  - Heavy Duty Boots (prevents all entry hazard effects)
  - Magic Bounce (reflects the effect back)
  - Clear Body/White Smoke/Full Metal Body (prevents stat reduction)

### Differences from Regular Spider Lair
| Aspect | Spider Lair (ID 339) | Spider Lair Upgrade (ID 752) |
|--------|---------------------|-------------------------------|
| Duration | 5 turns | 7 turns |
| Setup message | Same | Same |
| Speed reduction | -1 stage | -1 stage |
| Activation conditions | Same | Same |
| Immunities | Same | Same |

### Strategic Applications

#### Offensive Use
- **Extended Speed Control**: 7 turns provides more opportunities to capitalize on speed advantage
- **Sweeper Setup**: Creates favorable speed tiers for bulky sweepers that need multiple turns
- **Momentum Maintenance**: Longer duration means less pressure to immediately capitalize
- **Late-Game Control**: More effective in longer battles where turn economy matters

#### Defensive Use
- **Stall Support**: Extended hazard presence for defensive teams
- **Switch Punishment**: Discourages opponent switching for nearly a quarter of the battle
- **Revenge Killing**: Makes it easier to outspeed threatening Pokemon consistently
- **Entry Control**: Provides reliable speed manipulation without move slot investment

### Team Synergy
- **Hazard Stacking**: Combines excellently with Spikes, Stealth Rock, and Toxic Spikes
- **Slow Sweepers**: Particularly valuable for Pokemon like Rhyperior, Conkeldurr, or Magnezone
- **Bulky Pivots**: Enhanced utility for tanks that switch frequently (Forretress, Skarmory)
- **Setup Sweepers**: Provides speed advantage for Pokemon running Swords Dance, Nasty Plot, etc.

### Competitive Analysis

#### Advantages over Regular Spider Lair
1. **Extended Duration**: 40% longer duration (7 vs 5 turns)
2. **Greater Value**: More switch-ins likely to be affected
3. **Better Late-Game**: Maintains relevance in longer battles
4. **Setup Window**: More time to set up sweepers behind the speed control

#### Limitations
1. **Single Use**: Still only activates once per battle entry
2. **No Reactivation**: Cannot set up new webs if original user switches out and back in
3. **Immunity Issues**: Same immunities as regular Sticky Web
4. **Removal Vulnerability**: Can still be cleared by Rapid Spin, Defog, or Court Change

### Counterplay
- **Entry Hazard Removal**: Rapid Spin, Defog, Tidy Up, and Court Change all remove Sticky Web
- **Flying Types**: Completely immune (Corviknight, Skarmory, Dragonite, etc.)
- **Levitate**: Ground immunity negates the effect (Rotom forms, Bronzong, etc.)
- **Heavy Duty Boots**: Prevents all entry hazard effects including speed reduction
- **Magic Bounce**: Reflects hazard back to user's side (Hatterene, Xatu)
- **Stat Boost Immunity**: Clear Body, White Smoke, Full Metal Body prevent speed reduction
- **Taunt + Setup**: Prevent defensive plays and set up before webs expire

### Example Damage Calculations
Sticky Web doesn't deal damage - it only reduces speed by 1 stage:
- Base 100 Speed to 67 Speed at -1 stage
- Base 80 Speed to 53 Speed at -1 stage  
- Base 60 Speed to 40 Speed at -1 stage

This often creates crucial speed tiers and revenge killing opportunities.

### Common Users
Spider Lair Upgrade is typically found on:
- **Elite Four / Champion teams**: High-tier trainers with upgraded abilities
- **Legendary encounters**: Enhanced versions of spider-themed legendaries
- **Post-game content**: Upgraded forms of Ariados and similar Pokemon
- **Battle facilities**: Advanced AI teams with optimized ability sets

### Competitive Usage Notes
- **Tier Placement**: High utility ability for both offensive and defensive teams
- **Format Considerations**: More valuable in longer formats (6v6 vs 3v3)
- **Lead Potential**: Excellent on defensive leads that can set hazards and pivot
- **Late-Game Insurance**: Provides speed control even if hazard stack is incomplete

### Version History
- **Elite Redux 1.0**: Introduced as upgrade to Spider Lair
- **Current**: 7-turn duration, identical mechanics to base version
- **Proto File Bug**: Listed as "Rising Dough" in AbilityList.textproto but correctly implemented

### Related Abilities
- **Spider Lair (ID 339)**: Base version with 5-turn duration
- **Web Spinner**: Creates additional web-based battlefield effects
- **Sticky Hold**: Synergizes by preventing item removal from hazard damage
- **Compound Eyes**: Improves accuracy of follow-up moves after speed control

### Conclusion
Spider Lair Upgrade represents one of the most powerful entry hazard abilities in Elite Redux, providing guaranteed speed control for nearly a quarter of most battles. The extended 7-turn duration makes it significantly more valuable than the base Spider Lair, offering both immediate tactical advantage and long-term strategic value. Its automatic activation and immunity to most disruption makes it a cornerstone ability for teams built around speed control and entry hazard strategies.
---
id: 714
name: Apple Pie
status: reviewed
character_count: 292
---

# Apple Pie - Ability ID 714

## In-Game Description
"Self Sufficient + Ripen."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Restores 1/16 of the Pokemon's maximum HP at the end of each turn. Ripen doubles all beneficial berry effects. Healing berries restore twice as much HP, stat-boosting berries raise stats by 2 stages, resist berries reduce super-effective damage by 75%, and PP-restoring berries restore 20 PP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Apple Pie is a combination ability that provides both passive healing and enhanced berry effectiveness. It merges two distinct but synergistic effects:

1. **Self Sufficient component**: Provides end-of-turn healing
2. **Ripen component**: Enhances all berry effects

### Self Sufficient Component

#### Healing Mechanics
- **Healing amount**: 1/16 of max HP per turn
- **Timing**: End of turn, after other end-of-turn effects
- **Minimum healing**: Always heals at least 1 HP
- **Turn restriction**: Does not activate on the first turn (gVolatileStructs.isFirstTurn != 2)
- **Full HP check**: Does not activate if already at full HP
- **Healing block**: Respects healing prevention effects

#### Technical Implementation
```c
// Self Sufficient healing at end of turn
gBattleMoveDamage = gBattleMons[battler].maxHP / 16;
if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
gBattleMoveDamage *= -1; // Negative = healing
```

### Ripen Component

#### Berry Effect Enhancement
Ripen doubles the effectiveness of all berry effects:

- **Healing berries**: Oran Berry, Sitrus Berry, etc. heal 2x amount
- **Stat boost berries**: Liechi Berry, Petaya Berry, etc. give +2 stages instead of +1
- **Status recovery berries**: Healing amount doubled
- **Damage berries**: Jaboca Berry, Rowap Berry deal 2x damage
- **Resist berries**: Damage reduction increased (0.5x to 0.25x)
- **PP restoration**: Leppa Berry restores 2x PP

#### Technical Implementation
```c
// Ripen effect check function
int HasRipenEffect(int battler) {
    return BATTLER_HAS_ABILITY(battler, ABILITY_RIPEN) || 
           BATTLER_HAS_ABILITY(battler, ABILITY_APPLE_PIE) || 
           BATTLER_HAS_ABILITY(battler, ABILITY_SUGAR_RUSH);
}

// Example: Healing berry with Ripen
if (HasRipenEffect(battlerId)) gBattleMoveDamage *= 2;
```

### Synergy Between Components

#### Strategic Combination
The two components work together excellently:
- **Consistent healing**: Self Sufficient provides reliable recovery
- **Emergency healing**: Enhanced berries provide burst healing when needed
- **Resource efficiency**: Berries become twice as effective
- **Longevity**: Multiple sources of healing for extended battles

#### Healing Stacking
- Self Sufficient healing occurs at end of turn
- Berry healing can occur during turn or at end
- Effects stack for significant recovery potential
- Leftovers and other healing items also stack

### Berry Interactions

#### Common Enhanced Berries
- **Oran Berry**: 20 HP to 40 HP healing
- **Sitrus Berry**: 25% max HP to 50% max HP healing
- **Liechi Berry**: +1 Attack to +2 Attack when HP <= 25%
- **Petaya Berry**: +1 Sp. Atk to +2 Sp. Atk when HP <= 25%
- **Leppa Berry**: +10 PP to +20 PP restoration
- **Jaboca/Rowap Berry**: 1/8 max HP to 1/4 max HP damage to attacker

#### Resist Berry Enhancement
- **Normal resist berries**: 50% damage reduction to 75% damage reduction
- **Super effective coverage**: Makes resist berries extremely potent
- **Defensive utility**: Significant damage mitigation against specific types

### Activation Conditions

#### Self Sufficient Activation
- Must not be at full HP
- Must be able to heal (not blocked by abilities/effects)
- Must not be the first turn of being on the field
- Activates automatically at end of turn

#### Ripen Activation
- Activates whenever a berry effect triggers
- Works with all berry types (healing, stat, damage, resist)
- Enhancement is automatic and passive
- Shows ability popup when triggered

### Strategic Implications

#### Team Building
- **Berry-focused builds**: Maximize berry utility
- **Stall strategies**: Multiple healing sources for longevity
- **Mixed offense/defense**: Stat berries become more impactful
- **Anti-weakness**: Resist berries provide significant protection

#### Item Synergies
- **Sitrus Berry**: Massive 50% HP healing
- **Liechi/Salac Berries**: Powerful stat boosts
- **Resist Berries**: Excellent defensive utility
- **Leppa Berry**: Extended PP sustainability

### Counters and Limitations

#### Counters
- **Heal Block**: Prevents Self Sufficient healing
- **Taunt**: Limits setup opportunities
- **Knock Off**: Removes berries entirely
- **Unnerve**: Prevents berry consumption
- **Magic Guard**: Negates offensive berry damage

#### Limitations
- **First turn delay**: No healing on switch-in turn
- **Berry dependency**: Ripen requires berries to be effective
- **Predictable**: Healing pattern is consistent
- **Item slot**: Requires berry item commitment

### Competitive Usage

#### Playstyle Fit
- **Bulky offensive**: Sustained damage with recovery
- **Stall/defensive**: Multiple healing sources
- **Setup sweepers**: Enhanced stat berries for boosting
- **Anti-meta**: Resist berries counter specific threats

#### Common Users
- Pokemon with naturally high bulk
- Setup sweepers who benefit from stat berries
- Defensive Pokemon needing multiple recovery sources
- Pokemon weak to common types (resist berry users)

### Version History
- Elite Redux exclusive combination ability
- Combines two distinct existing effects
- Part of the multi-ability system
- Designed for berry-centric strategies

### Technical Notes
- Both components use separate code paths
- Self Sufficient uses standard end-of-turn healing
- Ripen uses berry effect multiplication
- No interference between the two effects
- Ability popup shows for both components when triggered
---
id: 564
name: Eject Pack Ability
status: reviewed
character_count: 118
---

# Eject Pack Ability - Ability ID 564

## In-Game Description
"Flees when stats are lowered."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Automatically switches the user out when any of its stats are lowered, including self drops. Triggers once per battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger Condition**: Activates when any stat is lowered (Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, or Evasion)
- **Timing**: Triggers at the end of the turn during the `MOVEEND_EJECT_PACK` phase
- **Automatic Switch**: Forces the Pokemon to switch out immediately when triggered
- **Single-Use**: Uses a single-use ability counter - once triggered, it won't activate again in the same battle even if the Pokemon returns

### Persistent Ability Details
The ability is marked as `persistent = TRUE`, meaning:
- It cannot be suppressed by moves like Gastro Acid
- It cannot be copied by Trace or Role Play
- It cannot be swapped by Skill Swap
- It remains active even under unusual battle conditions

### Technical Implementation
```c
// Ability definition in abilities.cc
constexpr Ability EjectPackAbility = {
    .persistent = TRUE,
};

// Activation logic in battle_script_commands.c
if (IsBattlerAlive(battler) && gRoundStructs[battler].statFell && 
    gRoundStructs[battler].disableEjectPack == 0 &&
    BATTLER_HAS_ABILITY(battler, ABILITY_EJECT_PACK_ABILITY) && 
    !GetSingleUseAbilityCounter(battler, ABILITY_EJECT_PACK_ABILITY) &&
    CanBattlerSwitch(battler))
{
    SetSingleUseAbilityCounter(battler, ABILITY_EJECT_PACK_ABILITY, TRUE);
    // Trigger emergency exit
}
```

### Interaction Details
- **Stat Lowering Detection**: Uses `gRoundStructs[battler].statFell` flag to detect stat reductions
- **Disable Mechanism**: Can be disabled by `gRoundStructs[battler].disableEjectPack` flag (set by some abilities)
- **Switch Requirement**: Only activates if the Pokemon has valid party members to switch into
- **Speed Priority**: If multiple Pokemon have eject effects, only the fastest one activates

### Competitive Applications
1. **Pivot Strategy**: Allows safe switching when threatened by stat-lowering moves
2. **Intimidate Counter**: Automatically escapes Intimidate users
3. **Momentum Control**: Maintains battlefield control by avoiding stat debuffs
4. **Emergency Escape**: Provides guaranteed escape from dangerous situations

### Strategic Considerations
- **One-Time Use**: The single-use nature makes timing crucial
- **Predictable**: Opponents can exploit the automatic switching
- **Team Synergy**: Requires good team composition to capitalize on forced switches
- **Entry Hazard Vulnerability**: Switching into hazards can be costly

### Comparison to Eject Pack Item
- **Permanent**: Cannot be removed by Knock Off, Thief, or Trick
- **Reusable**: The ability persists across battles (unlike the consumed item)
- **Single Battle Use**: Limited to one activation per battle
- **Persistent Nature**: Cannot be suppressed or manipulated

### Notable Interactions
- **Blocked by**: Abilities that set `disableEjectPack` flag
- **Doesn't Trigger**: If no valid switch targets available
- **Priority**: Fastest Pokemon's eject effect activates first in multi-target scenarios
- **Ability Popup**: Shows "Tactical Retreat" name when activated
---
id: 46
name: Pressure
status: reviewed
character_count: 80
---

# Pressure - Ability ID 46

## In-Game Description
"Doubles foe's PP usage. Clears stat buffs on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles PP usage of opposing moves and clears all positive stat stages on entry. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**PRESSURE** is a passive ability that creates PP pressure on opponents while removing statistical advantages upon entry.

### Activation Mechanics:
- **Entry Effect**: Immediately upon entering battle (onEntry hook)
- **Stat Clearing**: Removes all positive stat buffs from opponents and all stat changes from user
- **Self-Clearing**: User's stat drops are cleared (beneficial effect)
- **Opponent Clearing**: All opponents' stat buffs are cleared (detrimental effect)
- **PP Effect**: Passive - no additional activation required

### PP Usage Mechanics:
1. **PP Doubling**:
   - Opposing moves cost 2 PP instead of 1
   - Only affects moves used against the Pressure user
   - Does not affect moves if the attacker also has Pressure
   - Applied during PP deduction phase after move execution

2. **Scope**:
   - Affects all attacking moves (including status moves)
   - Applies to both single and double battles
   - Multiple Pressure users stack effect (opponents lose 3 PP per move if facing 2 Pressure users)

### Entry Stat Clearing:
- **Self-Effect**: Clears user's stat drops (Attack -1 becomes neutral, etc.)
- **Opponent Effect**: Clears all positive stat buffs from opponents
- **Preserved**: Opponent stat drops remain unchanged
- **Implementation**: Uses `RESET_STAT_DROPS` for self, `RESET_STAT_BUFFS` for opponents
- **Message**: "All stat changes were eliminated!" if any stats were cleared

### Technical Implementation:
```c
constexpr Ability Pressure = {
    .onEntry = +[](ON_ENTRY) -> int {
        int loweredStats = 0;
        for (int i = 0; i < gBattlersCount; i++) {
            if (!IsBattlerAlive(i)) continue;
            loweredStats |= TryResetBattlerStatChanges(i, 
                i == battler ? RESET_STAT_DROPS : RESET_STAT_BUFFS);
        }
        
        if (loweredStats) {
            BattleScript_PressureRemoveStats(); // "All stat changes were eliminated!"
        }
        
        SwitchInAnnounce(B_MSG_SWITCHIN_PRESSURE); // "is exerting its pressure!"
        return TRUE;
    },
};

// PP Usage (in battle_script_commands.c):
if (!BATTLER_HAS_ABILITY(attacker, ABILITY_PRESSURE) && 
    IsAbilityOnOpposingSide(attacker, ABILITY_PRESSURE)) {
    ppToDeduct++; // Doubles PP usage
}
```

### Interaction Rules:
- **vs Setup Sweepers**: Immediately neutralizes stat buffs like Swords Dance, Nasty Plot
- **vs Stat Support**: Removes beneficial effects from Intimidate, Defiant triggers
- **PP Stalling**: Forces opponents to exhaust moves faster, especially problematic for low-PP moves
- **Self-Beneficial**: Clears negative stat changes from moves like Overheat, Superpower

### Competitive Applications:
1. **Defensive Pivot**: Entry hazard for stat-based strategies
2. **PP Stalling**: Synergizes with Recover, Toxic, Substitute strategies  
3. **Setup Counter**: Hard counters setup sweepers that rely on stat buffs
4. **Resource Management**: Forces opponents to use items like Leppa Berry earlier

### Counters and Limitations:
- **Ability Suppression**: Neutralizing Gas, Mold Breaker bypass the entry effect
- **Immediate Threat**: No defensive benefit if opponent can KO without setup
- **Status Immunity**: Doesn't prevent status moves that don't require PP (like Toxic Spikes)
- **Substitute**: Opponents behind Substitute take PP pressure but avoid stat clearing

### Synergistic Strategies:
- **Toxic Spikes + Pressure**: Forces opponents to waste PP while taking poison damage
- **Recover/Roost**: Pressure stalling with reliable recovery
- **Protect/Detect**: Maximizes PP waste by forcing opponents to use moves without damage
- **Choice Items**: Pressure bearers can force opponents to struggle faster

### Notable Users:
- Many legendary Pokemon have Pressure as their signature ability
- Commonly appears on defensive walls and stall Pokemon
- Particularly effective on Pokemon with access to recovery moves

### Calculations:
- **Standard Move (24 PP)**: Lasts 24 turns to 12 turns vs Pressure
- **Low PP Move (8 PP)**: Lasts 8 turns to 4 turns vs Pressure  
- **Two Pressure Users**: Opponent moves cost 3 PP each (1 base + 2 pressure)

### Version History:
- Gen 3-4: Original implementation with PP doubling only
- Elite Redux: Added stat clearing on entry, making it both offensive and defensive utility
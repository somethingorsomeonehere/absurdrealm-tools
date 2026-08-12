---
id: 410
name: Queen's Mourning
status: reviewed
character_count: 194
---

# Queen's Mourning - Ability ID 410

## In-Game Description
"Lowering any stats on its side raises SpAtk and SpDef."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Queen's Mourning triggers when the user or their ally has their stats lowered, immediately boosting the user's Special Attack and Special Defense by one stage. Does not activate from self drops.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Queen's Mourning is a reactive ability that triggers when any stat decrease occurs on the user's side of the field. Unlike abilities that only react to the user's own stat changes, Queen's Mourning monitors the entire team side for stat reductions.

### Activation Conditions
- **Trigger requirement**: Any stat decrease on the user's side of the field
  - Includes the Pokemon with Queen's Mourning
  - Includes the partner Pokemon in doubles/multi battles  
  - Does NOT include the opposing side's stat changes
- **Exclusion**: Does NOT trigger if the stat decrease comes from the partner Pokemon or the user itself
- **Timing**: Activates immediately after the stat decrease message
- **Stat boosts**: Raises Special Attack and Special Defense by +1 stage each

### Technical Implementation
```c
// Queen's Mourning triggers when DEFENDERSSTATFELL occurs
if ((stringId == STRINGID_DEFENDERSSTATFELL) && 
    (abilityBattler = IsAbilityOnSide(gBattlerTarget, ABILITY_QUEENS_MOURNING)) &&
    gTurnStructs[gBattlerTarget].changedStatsBattlerId != BATTLE_PARTNER(gBattlerTarget) &&
    gTurnStructs[gBattlerTarget].changedStatsBattlerId != gBattlerTarget) {
    
    // Set up ability popup and stat changes
    gBattleScripting.abilityPopupOverwrite = ABILITY_QUEENS_MOURNING;
    BattleScriptCall(BattleScript_QueensMourningActivated);
}

// Battle script raises Special Attack and Special Defense
BattleScript_QueensMourningActivated::
    jumpifstat BS_ABILITY_BATTLER, CMP_LESS_THAN, STAT_SPATK, MAX_STAT_STAGE, BattleScript_QueensMourning_AttackUpDoAnim
    jumpifstat BS_ABILITY_BATTLER, CMP_EQUAL, STAT_SPDEF, MAX_STAT_STAGE, BattleScript_QueensMourning_End
    // Raises Special Attack by +1 stage
    setstatchanger STAT_SPATK, 1, FALSE
    statbuffchange MOVE_EFFECT_AFFECTS_USER, BattleScript_QueensMourning_DefenseUpDoAnim
    // Raises Special Defense by +1 stage  
    setstatchanger STAT_SPDEF, 1, FALSE
    statbuffchange MOVE_EFFECT_AFFECTS_USER, BattleScript_QueensMourning_End
```

### Important Interactions
- **IsAbilityOnSide**: Uses the special function that checks both the user and partner for the ability
- **Self-exclusion**: Won't trigger if the stat decrease comes from the user or partner
- **Opponent targeting**: Only triggers when opponents lower stats on your side
- **Stat cap**: Won't raise stats that are already at maximum (+6)
- **Ability popup**: Shows the ability name when triggered
- **Animation timing**: Plays stat increase animations for both stats

### Doubles/Multi Battle Behavior
Queen's Mourning excels in doubles due to its side-based activation:
- **Partner protection**: Triggers when partner's stats are lowered
- **Team support**: Provides special bulk to the team
- **Intimidate counter**: Activates against Intimidate users
- **Stat spread**: Boosts both offensive and defensive special stats

### Strategic Implications
- **Anti-debuff**: Punishes opponents for using stat-lowering moves
- **Special tank**: Builds special bulk and power simultaneously  
- **Team synergy**: Excellent on teams that may face stat reduction
- **Intimidate counter**: Strong against physical Intimidate users
- **Opponent psychology**: Deters opponents from using debuff moves

### Activation Examples
**Triggers on:**
- Opponent uses Charm on your partner to Queen's Mourning activates
- Opponent uses Screech on the user to Queen's Mourning activates  
- Opponent's Intimidate lowers your Attack to Queen's Mourning activates
- Opponent uses Acid Spray on either ally to Queen's Mourning activates

**Does NOT trigger on:**
- Your own Overheat lowering your Special Attack
- Partner uses Superpower and lowers own stats
- Opponent's stats are lowered by your moves
- Burns/items lowering your own stats

### Common Users
- Special attackers who want both offense and defense
- Doubles support Pokemon
- Tanks that can capitalize on stat boosts
- Pokemon with naturally high Special Attack/Defense

### Competitive Usage Notes
- **Doubles focused**: Much stronger in doubles than singles
- **Intimidate meta**: Excellent in metas with common Intimidate
- **Stat boost stacking**: Can accumulate multiple boosts per battle
- **Unpredictable timing**: Opponents may not expect the trigger
- **Deters debuffs**: Makes opponents think twice about stat reduction

### Counters
- **Avoid stat moves**: Don't use stat-lowering moves against the team
- **Physical attacks**: Focus on raw damage rather than stat manipulation
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Stat reset**: Haze, Clear Smog to remove accumulated boosts
- **Taunt**: Prevent setup that could follow the stat boosts

### Synergies
- **Calm Mind/Nasty Plot**: Stack with natural stat boosts
- **Assault Vest**: Provides additional special bulk
- **Choice Specs**: Immediate power boost with SpAtk increases
- **Stored Power**: Benefits from accumulated stat boosts
- **Weakness Policy**: Can potentially stack with other reactive abilities

### Version History
- Elite Redux exclusive ability
- Designed to counter stat-lowering strategies
- Promotes more aggressive, damage-focused gameplay
- Particularly effective in the doubles-heavy Elite Redux meta

### Design Philosophy
Queen's Mourning represents a defensive response to stat manipulation, turning the opponent's debuff strategy into a boost for the user. The ability encourages direct damage over stat manipulation, creating more dynamic battle scenarios while providing teams with anti-debuff insurance.
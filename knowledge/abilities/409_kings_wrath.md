---
id: 409
name: King's Wrath
status: reviewed
character_count: 174
---

# King's Wrath - Ability ID 409

## In-Game Description
"Lowering any stats on its side raises Atk and Def."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

King's Wrath triggers when the user or their ally has their stats lowered, immediately boosting the user's Attack and Defense by one stage. Does not activate from self drops.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
King's Wrath is a reactive ability that converts ally stat reduction into personal stat boosts. When any Pokemon on the user's side (including partners in doubles) has their stats lowered, the King's Wrath user immediately gains +1 Attack and +1 Defense.

### Activation Conditions
- **Trigger**: Any stat reduction on the user's side of the field
- **Affected stats boosted**: Attack +1, Defense +1
- **Side-based**: Works for both user and partner in doubles battles
- **Timing**: Activates immediately after the stat reduction occurs
- **Stack limit**: Each activation can only boost up to maximum stat stages (+6)

### Technical Implementation
```c
// King's Wrath triggers when ally stats are lowered
if ((stringId == STRINGID_DEFENDERSSTATFELL) && 
    (abilityBattler = IsAbilityOnSide(gBattlerTarget, ABILITY_KINGS_WRATH)) &&
    gTurnStructs[gBattlerTarget].changedStatsBattlerId != BATTLE_PARTNER(gBattlerTarget) &&
    gTurnStructs[gBattlerTarget].changedStatsBattlerId != gBattlerTarget) {
    
    // Trigger King's Wrath battle script
    BattleScriptCall(BattleScript_KingsWrathActivated);
}
```

### Battle Script Analysis
```assembly
BattleScript_KingsWrathActivated::
    jumpifstat BS_ABILITY_BATTLER, CMP_LESS_THAN, STAT_ATK, MAX_STAT_STAGE, BattleScript_KingsWrath_AttackUpDoAnim
    jumpifstat BS_ABILITY_BATTLER, CMP_EQUAL, STAT_DEF, MAX_STAT_STAGE, BattleScript_KingsWrath_End
    
    # Boost Attack if not maxed
    setstatchanger STAT_ATK, 1, FALSE
    statbuffchange MOVE_EFFECT_AFFECTS_USER
    
    # Boost Defense if not maxed  
    setstatchanger STAT_DEF, 1, FALSE
    statbuffchange MOVE_EFFECT_AFFECTS_USER
```

### Important Interactions
- **Side-based activation**: Protects both user and doubles partner
- **Self-exclusion**: Does NOT trigger from the user's own stat reductions
- **Partner exclusion**: Does NOT trigger from the partner's own stat reductions (to prevent infinite loops)
- **Enemy moves**: Triggers from opponent stat-lowering moves like Intimidate, Snarl, etc.
- **Indirect effects**: Triggers from abilities like Sticky Web, stat-lowering items
- **Max stage limit**: Cannot boost beyond +6 Attack/Defense

### Strategic Applications
- **Intimidate counter**: Excellent against Intimidate users and physical attackers
- **Doubles synergy**: Protects partner from stat drops while gaining boosts
- **Defensive pivot**: Gains bulk while becoming more threatening
- **Anti-control**: Punishes opponents for using stat-lowering strategies
- **Setup deterrent**: Makes opponents think twice about stat reduction moves

### Trigger Sources
**Common stat-lowering effects that activate King's Wrath:**
- **Moves**: Snarl, Charm, Growl, Leer, Breaking Swipe, etc.
- **Abilities**: Intimidate, Sticky Web (on switch-in)
- **items**: King's Rock secondary effects on stat-lowering moves
- **Field effects**: Certain terrain or weather interactions

### Counters and Limitations
- **Self-targeting moves**: User's own stat drops don't trigger the ability
- **Ability suppression**: Neutralizing Gas, Mold Breaker bypass the ability
- **Stat boost prevention**: Clear Body, White Smoke prevent the beneficial boosts
- **Special attackers**: Only boosts physical stats, vulnerable to special attacks
- **Max stage limit**: Diminishing returns once Attack/Defense hit +6

### Competitive Analysis
**Strengths:**
- Excellent deterrent against stat-lowering strategies
- Dual stat boost provides both offense and defense
- Works in both singles and doubles formats
- Punishes common strategies like Intimidate pivoting

**Weaknesses:**
- Reactive rather than proactive ability
- Only boosts physical stats (Attack/Defense)
- Requires opponent to use stat-lowering effects
- Can be played around by savvy opponents

### Similar Abilities
- **Defiant**: Boosts Attack when stats are lowered (self-targeting)
- **Competitive**: Boosts Special Attack when stats are lowered (self-targeting)  
- **Queen's Mourning**: Sister ability that boosts Sp.Attack and Sp.Defense instead

### Synergies
- **Doubles partners**: Works well with Pokemon that commonly face stat drops
- **Physical attackers**: The Attack boost enhances offensive presence
- **Bulky setups**: Defense boost helps with survivability
- **Anti-Intimidate cores**: Essential for physical attackers in Intimidate metas

### AI Recognition
The battle AI recognizes King's Wrath as a stat-lowering deterrent ability and factors it into move selection when considering stat-reducing moves.

### Version History
- Added in Elite Redux as part of the expanded ability roster
- Designed as a side-protection ability for doubles and anti-Intimidate utility
- Paired with Queen's Mourning as special counterpart
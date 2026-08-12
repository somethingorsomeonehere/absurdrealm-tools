---
id: 529
name: Berserk DNA
status: reviewed
character_count: 135
---

# Berserk DNA - Ability ID 529

## In-Game Description
"Sharply ups highest attacking stat but confuses on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the higher of Attack or Special Attack by 2 stages upon entering battle. Causes confusion for 3 turns unless the user is immune.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Berserk DNA is an aggressive entry ability that provides a significant offensive boost at the cost of self-inflicted confusion. The ability activates immediately when the Pokemon switches into battle.

### Activation Sequence
1. **Entry trigger**: Activates when the Pokemon switches into battle
2. **Stat comparison**: Compares Attack vs Special Attack stats (including stat stages)
3. **Stat boost**: Raises the higher attacking stat by +2 stages (sharply raised)
4. **Confusion check**: If the Pokemon can be confused, applies confusion for 3 turns
5. **Message display**: Shows "POKÉMON goes berserk!" followed by stat boost message

### Technical Implementation
```c
// BerserkDna ability from abilities.cc
constexpr Ability BerserkDna = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, GetHighestAttackingStatId(battler, TRUE)))
        if (CanBeConfused(battler)) {
            gBattleMons[battler].status2 |= STATUS2_CONFUSION_TURN(3);
            BattleScriptPushCursorAndCallback(BattleScript_BerserkDNA);
        }
        else {
            BattleScriptPushCursorAndCallback(BattleScript_BerserkDNANoConfusion);
        }
        return TRUE;
    },
};
```

### Battle Script Mechanics
```assembly
BattleScript_BerserkDNA::
    printstring STRINGID_BERSERKDNA
    raisehighestattackingstat BS_ATTACKER, 2  // +2 stages to higher attacking stat
    setgraphicalstatchangevalues
    playanimation BS_ATTACKER, B_ANIM_STATS_CHANGE
    printstring STRINGID_BATTLERABILITYRAISEDSTAT
    chosenstatus2animation BS_ATTACKER, STATUS2_CONFUSION
    printstring STRINGID_PKMNWASCONFUSED
```

### Stat Selection Logic
The ability uses `GetHighestAttackingStatId(battler, TRUE)` which:
- Compares Attack vs Special Attack base stats
- Includes current stat stage modifications in comparison
- Returns the higher of the two stats
- Only considers Attack and Special Attack (not other stats)

### Confusion Mechanics
- **Duration**: Exactly 3 turns of confusion
- **Immunity bypass**: Cannot override confusion immunity
- **Checks**: Uses `CanBeConfused()` function which checks:
  - Not already confused
  - Not protected by abilities (Own Tempo, etc.)
  - Not immune via type or other mechanics

### Activation Conditions
- **Entry requirement**: Must switch into battle (not on initial deployment)
- **Stat boost requirement**: Must be able to raise the highest attacking stat
- **Stat maximum**: If the relevant stat is already at +6, the ability still triggers but no boost occurs

### Important Interactions
- **Stat stage comparison**: If both Attack and Special Attack are equal, defaults to Attack
- **Confusion immunity**: Pokemon with Own Tempo or similar get the boost without confusion
- **Clear Body/White Smoke**: Prevents the stat boost but may still apply confusion
- **Mental Herb**: Can cure confusion immediately after ability triggers
- **Persim Berry**: Automatically cures confusion after the ability activates

### Strategic Applications
- **Mixed attackers**: Particularly valuable on Pokemon with similar Attack/Special Attack
- **Late-game sweeping**: +2 boost provides immediate offensive pressure
- **Pivot usage**: Can be used on switching Pokemon for momentum
- **Confusion management**: Pairs well with Lum Berry or Mental Herb
- **Priority moves**: Use priority moves during confusion turns to minimize risk

### Pokemon with Berserk DNA
Based on codebase analysis, Pokemon with this ability include:
- **Mewtwo** (changeable ability alongside Mystic Power and Psychic Surge)
- **Deoxys-Speed** (as an innate ability)
- **Infernape-like forms** (as changeable ability with Gorilla Tactics/Anger Point)
- **Gyarados-Mega variants** (as innate ability)
- **Genesect-like forms** (as changeable ability with Corrosion/Power Core)

### Competitive Viability
**Strengths:**
- Immediate +2 offensive boost provides massive power spike
- Works on both physical and special attackers
- Cannot be suppressed by most defensive abilities
- Excellent for late-game sweeping scenarios

**Weaknesses:**
- Confusion can cause self-damage and move failure
- Vulnerable to stat-reducing moves after boost
- Entry requirement limits activation opportunities
- May boost wrong stat if opponent forces unfavorable switch

### Counters and Responses
- **Haze/Clear Smog**: Removes the stat boosts entirely
- **Intimidate**: Can partially offset Attack boosts
- **Spectral Thief**: Can steal the stat boosts
- **Topsy-Turvy**: Turns the boost into a debuff
- **Confusion abuse**: Force repeated switching to waste turns
- **Priority moves**: Can revenge kill during confusion turns

### Synergies
- **Lum Berry/Mental Herb**: Cures confusion while keeping boost
- **Focus Sash**: Survives confusion self-damage
- **Priority moves**: Bullet Punch, Aqua Jet for safe offense during confusion
- **Substitute**: Can block confusion damage while keeping boost
- **RestTalk**: Can potentially wake up and use moves through confusion

### Team Building Considerations
- Works best on Pokemon that can function as late-game sweepers
- Requires careful positioning to maximize entry opportunities
- Benefits from team support to handle confusion downside
- Excellent on Pokemon with good mixed attacking stats
- Can be used as a surprise factor in competitive play

### Version History
- Elite Redux exclusive ability (ID 529)
- Designed for high-risk, high-reward gameplay
- Part of the expanded ability system with 1000+ abilities
- Represents the concept of berserker rage with mechanical tradeoffs
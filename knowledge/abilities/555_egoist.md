---
id: 555
name: Egoist
status: reviewed
character_count: 115
---

# Egoist - Ability ID 555

## In-Game Description
"Raises its own stats when foes raise theirs."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Egoist copies stat boosts that enemy Pokemon receive and applies them to itself. Does not copy other Egoist boosts.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Egoist activates whenever any opponent gains positive stat boosts (+1, +2, etc.)
- The ability copies the exact same stat increases to the Egoist user
- Works on all battle stats: Attack, Defense, Speed, Special Attack, Special Defense, and Accuracy
- Multiple opponents' boosts are additive (if two foes each boost +1 Attack, Egoist user gets +2 Attack)

**Activation Conditions:**
- Triggers on any positive stat change from opposing Pokemon
- Works with moves, abilities, items, or any other stat-boosting effects
- Only affects enemy stat boosts - ally boosts are ignored
- Must be alive and on the field when stat boosts occur

**Technical Implementation:**
```c
constexpr Ability Egoist = {
    .onReactive = +[](ON_REACTIVE) -> int {
        // Check if stat stage checking is needed
        CHECK(gBattleStruct->statStageCheckState != STAT_STAGE_CHECK_NOT_NEEDED)
        
        // Loop through all opponents
        for (int opponent = GetOppositeSide(battler); opponent < gBattlersCount; opponent += 2) {
            // Check each stat for positive changes
            for (int stat = STAT_ATK; stat < ARRAY_COUNT(gBattleStruct->statChangesToCheck[opponent]); stat++) {
                if (gBattleStruct->statChangesToCheck[opponent][stat - 1] > 0) {
                    // Trigger copy stat effects
                    BattleScriptCall(BattleScript_PerformCopyStatEffects);
                    return TRUE;
                }
            }
        }
        return FALSE;
    },
};
```

**Copy Process:**
```c
// In VARIOUS_DO_COPY_STAT_CHANGE:
for (otherBattler = 0; otherBattler < gBattlersCount; otherBattler++) {
    if (GetBattlerSide(otherBattler) == GetBattlerSide(battler)) continue; // Skip allies
    if (gBattleStruct->statChangesToCheck[otherBattler][state.stat - 1] > 0)
        change += gBattleStruct->statChangesToCheck[otherBattler][state.stat - 1]; // Add boosts
}
```

**Strategic Implications:**
- **Anti-Setup Tool**: Completely negates setup strategies by copying all boosts
- **Doubles/Multi-Battle Advantage**: Gets multiplicative benefits when multiple opponents boost
- **Immediate Response**: No delay - boosts are copied instantly when opponents boost
- **Passive Defensive Option**: Requires no move slots, works automatically

**Example Scenarios:**
1. **Dragon Dance Counter**: Opponent uses Dragon Dance (+1 Attack, +1 Speed) to Egoist user also gets +1 Attack, +1 Speed
2. **Multiple Opponents**: In doubles, if both opponents boost +1 Attack to Egoist user gets +2 Attack total
3. **Calm Mind Chain**: Opponent uses Calm Mind (+1 SpAtk, +1 SpDef) to Egoist user matches the boosts

**Damage Calculations:**
- No direct damage - purely stat-based
- Copied boosts follow normal stat calculation formulas:
  - +1 stage = 1.5x multiplier
  - +2 stages = 2.0x multiplier
  - +3 stages = 2.5x multiplier
  - And so on...

**Common Users:**
Based on SpeciesList.textproto analysis, Egoist appears on several Pokemon as both regular and innate abilities, making it accessible across different team compositions.

**Competitive Usage Notes:**
- **Meta Positioning**: Excellent against setup-heavy metagames
- **Team Role**: Best used on defensive/support Pokemon that can capitalize on copied boosts
- **Timing**: Most effective when opponents are forced to boost early (speed control, sweeper preparation)

**Counters:**
- **Stat Resets**: Haze, Clear Smog, and other stat-clearing moves
- **Physical Attacks**: Directly attacking instead of boosting bypasses the ability
- **Negative Priority**: Using moves that lower opponent's stats instead of raising your own
- **Ability Suppression**: Gastro Acid, Simple Beam, or other ability-changing moves

**Synergies:**
- **Baton Pass Teams**: Can copy boosts then pass them to dedicated sweepers
- **Defensive Cores**: Combines well with recovery moves and status spreading
- **Speed Control**: Copied Speed boosts help with turn order manipulation
- **Multi-Hit Moves**: Benefits from copied Attack boosts with moves like Bullet Seed

**Version History:**
- Added in Elite Redux as part of the expanded ability roster
- Functions as a unique anti-setup tool in the competitive metagame
- Implementation uses the reactive ability system for immediate triggering
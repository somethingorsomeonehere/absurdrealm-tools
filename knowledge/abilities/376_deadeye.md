---
id: 376
name: Deadeye
status: reviewed
character_count: 239
---

# Deadeye - Ability ID 376

## In-Game Description
"Arrow & cannon moves never miss. Crits hit weakest defense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user is unable to miss arrow-based attacks and cannon moves (different from Mega Launcher moves, includes moves blocked by Bulletproof). Additionally, when landing critical hits, the attack targets the opponent's weaker defensive stat.

## Technical Implementation

### Source Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 3906-3921

### Implementation Details

```cpp
constexpr Ability Deadeye = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(IsMegaLauncherBoosted(battler, move) || gBattleMoves[move].arrowBased)
        return ACCURACY_HITS_IF_POSSIBLE;
    },
    .onChooseDefensiveStat = +[](ON_CHOOSE_DEFENSIVE_STAT) -> int {
        CHECK(gIsCriticalHit)
        u32 def = CalculateStat(target, STAT_DEF, 0, move, FALSE, ignoreDefensiveStatBoosts, battlerUnaware, FALSE);
        u32 spDef = CalculateStat(target, STAT_SPDEF, 0, move, FALSE, ignoreDefensiveStatBoosts, battlerUnaware, FALSE);
        if (def < spDef)
            return STAT_DEF;
        else if (spDef < def)
            return STAT_SPDEF;
        else
            return 0;
    },
},
```

### Mechanics Breakdown

#### 1. Perfect Accuracy (onAccuracy)
- **Trigger**: When using moves that are either:
  - **Mega Launcher boosted**: Determined by `IsMegaLauncherBoosted()` function (lines 3908)
  - **Arrow-based**: Moves with `gBattleMoves[move].arrowBased` flag set to true
- **Effect**: Returns `ACCURACY_HITS_IF_POSSIBLE`, ensuring these moves never miss
- **Examples of affected moves**:
  - Arrow moves: Diamond Arrow, moves with `arrow: true` flag
  - Mega Launcher moves: Aura Sphere, Dragon Pulse, Water Pulse, and other pulse/sphere moves

#### 2. Smart Critical Hit Targeting (onChooseDefensiveStat)
- **Trigger**: Only activates when `gIsCriticalHit` is true (line 3912)
- **Calculation**: 
  - Compares target's actual Defense and Special Defense stats using `CalculateStat()`
  - Accounts for stat boosts and modifications
  - Returns the stat ID of the weaker defensive stat
- **Logic**:
  - If Defense < Special Defense: Target Defense (`STAT_DEF`)
  - If Special Defense < Defense: Target Special Defense (`STAT_SPDEF`)
  - If equal: Return 0 (no preference, uses move's natural split)

### Supporting Functions

#### IsMegaLauncherBoosted Definition
Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_util.c`:
```cpp
int IsMegaLauncherBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_MEGA_LAUNCHER_BOOST) return TRUE;
    if (IS_MOVE_STATUS(move) || BattlerHasAbility(battler, ABILITY_GUNMAN, FALSE)) return TRUE;
    return FALSE;
}
```

## Strategic Analysis

### Offensive Applications
1. **Guaranteed Hit Pressure**: Never missing with arrow/cannon moves provides consistent offensive pressure
2. **Critical Hit Synergy**: Pairs excellently with high critical hit ratio moves or critical hit boosting items
3. **Defensive Stat Exploitation**: Critical hits become significantly more dangerous by always targeting weak points

### Competitive Viability
- **Tier Rating**: Medium
- **Strengths**:
  - Reliable accuracy for specific move types
  - Enhanced critical hit damage through smart targeting
  - Good synergy with critical hit focused builds
- **Limitations**:
  - Only affects specific move categories (arrows/cannons)
  - Critical hit component requires actually landing crits
  - Doesn't boost critical hit rate itself

### Team Building Considerations
1. **Move Selection**: Prioritize arrow-based moves and Mega Launcher compatible moves
2. **Item Synergy**: 
   - Scope Lens or Razor Claw for increased critical hit rates
   - Never-Miss Clause for moves
3. **Ability Combinations**: Works well with other precision-focused abilities

## Related Abilities

### Similar Accuracy Abilities
- **Artillery** (#377): Only affects Mega Launcher moves, not arrow moves
- **No Guard** (#99): Makes all moves hit but also allows opponent's moves to always hit
- **Compound Eyes** (#14): Increases accuracy by 30% but not guaranteed

### Critical Hit Related Abilities
- **Super Luck** (#105): Increases critical hit ratio
- **Sniper** (#97): Increases critical hit damage

### Combination Abilities
- **Hunter's Mark** (#435): Combines Ambush + Deadeye for stealth and precision

## Move Compatibility

### Arrow-Based Moves
- Diamond Arrow
- Various moves with `arrow: true` flag in move data
- Generally physical projectile attacks themed around archery

### Mega Launcher Moves
- Aura Sphere
- Dragon Pulse  
- Water Pulse
- Other pulse/sphere/aura moves
- All status moves (when used by Gunman ability holders)

## Competitive Impact
Deadeye provides a focused but powerful benefit for specific archetypes. The guaranteed accuracy component removes the risk factor from using arrow and cannon moves, while the critical hit enhancement can lead to devastating surprise KOs when crits land. Most effective on Pokemon with access to both arrow/cannon moves and ways to boost critical hit rates.
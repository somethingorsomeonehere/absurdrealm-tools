---
id: 395
name: Iron Barrage
status: reviewed
character_count: 164
---

# Iron Barrage - Ability ID 395

## In-Game Description
"Mega Launcher boost with perfect accuracy and priority penalties."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts pulse, beam, ball, and aura moves by 30%. Guarantees all moves hit regardless of accuracy checks. Moves with less than 80% base accuracy receive -3 priority.

## Detailed Mechanical Explanation

### Overview
Iron Barrage is a powerful hybrid ability that combines the offensive capabilities of Mega Launcher with the precision targeting of Sighting System. This unique combination creates a devastating artillery-focused ability perfect for projectile-based attackers.

## Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: 4082-4087
- **Definition**: 
```cpp
constexpr Ability IronBarrage = {
    .onOffensiveMultiplier = MegaLauncher.onOffensiveMultiplier,
    .onAccuracy = SightingSystem.onAccuracy,
    .onPriority = SightingSystem.onPriority,
    .megaLauncherBoost = TRUE,
};
```

### Component Abilities

#### Mega Launcher Component (Lines 1943-1949)
```cpp
constexpr Ability MegaLauncher = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IsMegaLauncherBoosted(battler, move)) MUL(1.3);
        },
    .megaLauncherBoost = TRUE,
};
```

#### Sighting System Component (Lines 3826-3833)
```cpp
constexpr Ability SightingSystem = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority { return ACCURACY_HITS_IF_POSSIBLE; },
    .onPriority = +[](ON_PRIORITY) -> int {
        CHECK(gBattleMoves[move].accuracy)
        CHECK(gBattleMoves[move].accuracy < 80);
        return -3;
    },
};
```

### Move Qualification Logic
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_util.c` (Lines 9177-9181)
```c
int IsMegaLauncherBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_MEGA_LAUNCHER_BOOST) return TRUE;
    if (IS_MOVE_STATUS(move) || BattlerHasAbility(battler, ABILITY_GUNMAN, FALSE)) return TRUE;
    return FALSE;
}
```

## Mechanics Breakdown

### 1. Damage Boost (Mega Launcher)
- **Effect**: 30% damage increase (1.3x multiplier)
- **Applies to**: Moves with `FLAG_MEGA_LAUNCHER_BOOST` flag
- **Boosted Moves Include**:
  - Water Gun (Priority +1, 40 BP to 52 BP effective)
  - Hydro Pump (110 BP to 143 BP effective)
  - Ice Beam (90 BP to 117 BP effective)
  - Psybeam (65 BP to 84.5 BP effective)
  - Bubble Beam (25 BP multi-hit to 32.5 BP per hit effective)
  - Aurora Beam
  - All status moves (regardless of flag)

### 2. Perfect Accuracy (Sighting System)
- **Effect**: `ACCURACY_HITS_IF_POSSIBLE` - essentially never-miss status
- **Applies to**: ALL moves used by the Pokemon
- **Benefit**: Turns unreliable moves into consistent threats

### 3. Priority Penalty (Sighting System)
- **Effect**: -3 priority reduction
- **Condition**: Only applies to moves with accuracy < 80%
- **Purpose**: Balance mechanism to prevent abuse of perfect accuracy on high-power, low-accuracy moves

## Current Users

### Mega Toucannon
- **Species**: `SPECIES_TOUCANNON_MEGA`
- **Type**: Normal/Steel
- **Stats**: 80/120/110/135/110/70 (BST: 625)
- **Ability Slots**: 
  - Regular: Sturdy, Filter, Sheer Force
  - **Innate**: Steel Barrel, **Iron Barrage**, Pyro Shells
- **Location**: Lines 143649-143669 in `proto/SpeciesList.textproto`

## Strategic Analysis

### Strengths
1. **Guaranteed Hit Rate**: Never miss with any move, making unreliable but powerful moves viable
2. **Significant Damage Boost**: 30% increase to all projectile attacks
3. **Versatile Coverage**: Boosts both offensive and status moves
4. **Synergy with Steel Typing**: Fits thematically with Mega Toucannon's Steel secondary type

### Weaknesses
1. **Priority Penalty**: Low-accuracy moves become slower, potentially allowing opponents to act first
2. **Limited Move Pool**: Effectiveness depends on access to Mega Launcher-boosted moves
3. **Predictable**: Opponents know exactly what to expect from boosted moves

### Optimal Strategy
1. **Pivot Around Boosted Moves**: Focus movesets on FLAG_MEGA_LAUNCHER_BOOST moves
2. **Mixed Attacking**: Use both physical and special projectile moves if available
3. **Status Support**: Leverage perfect accuracy on status moves for reliable debuffs
4. **Priority Management**: Be cautious with low-accuracy moves due to -3 priority

## Competitive Applications

### Singles Format
- **Role**: Special/Mixed Artillery Sweeper
- **Key Moves**: Hydro Pump, Ice Beam, status moves
- **Teammates**: Entry hazard setters, speed control support

### Doubles Format
- **Role**: Precision Support/Damage Dealer
- **Synergy**: Perfect accuracy makes it reliable for supporting teammates
- **Positioning**: Back-line attacker with guaranteed hit rates

### Tier Placement: High
Iron Barrage combines two powerful effects without significant drawbacks, making it exceptionally valuable for artillery-focused Pokemon. The perfect accuracy alone is game-changing, while the damage boost ensures offensive presence.

## Related Abilities

### Similar Abilities
- **Mega Launcher** (#178): Provides only the damage boost component
- **Sighting System** (#368): Provides only the accuracy and priority components
- **No Guard** (#99): Mutual perfect accuracy but no damage boost
- **Sniper** (#97): Different approach to projectile enhancement

### Comparison with Mega Launcher
Iron Barrage is strictly superior to Mega Launcher, adding perfect accuracy without losing any damage boost functionality.


## Version History
- **Implementation**: Elite Redux custom ability
- **Current Status**: Active on Mega Toucannon as innate ability
- **Balance**: Well-balanced through priority penalty on inaccurate moves
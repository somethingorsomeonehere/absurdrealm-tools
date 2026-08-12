---
id: 865
name: Heat Sink
status: reviewed
character_count: 140
---

# Heat Sink - Ability ID 865

## In-Game Description
Redirects Fire moves. Absorbs them, ups highest Atk.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Draws in Fire-type moves and gain immunity to them. Additionally, Fire-type moves boost the highest attacking stat of the user by one stage.

## Detailed Mechanical Explanation

### Technical Analysis

### Core Mechanics
- **Redirect Function**: Uses `redirectType = TYPE_FIRE` to attract Fire-type moves
- **Absorption**: Uses `onAbsorb` with `CHECK(moveType == TYPE_FIRE)` to absorb Fire moves
- **Stat Boost**: Calls `GetHighestAttackingStatId(battler, TRUE)` to determine which stat to boost
- **Result**: Returns `ABSORB_RESULT_STAT` to trigger stat increase

### Stat Selection Logic
The `GetHighestAttackingStatId` function compares:
- Current Attack stat (STAT_ATK = 1) 
- Current Special Attack stat (STAT_SPATK = 4)
- Includes stat stage modifications in the comparison (`includeStatStages = TRUE`)
- Returns the stat ID of whichever is higher

### Redirection Mechanics
- Only works in double battles where allies can be targeted
- Redirected moves are completely negated (no damage dealt)
- Cannot be bypassed by Propeller Tail or Stalwart abilities
- Does not redirect moves with the Snipe Shot effect

### Battle Flow
1. Enemy uses Fire-type move targeting an ally
2. Heat Sink redirects the move to the Heat Sink user
3. Move is absorbed (no damage taken)
4. System determines highest attacking stat (Atk vs SpAtk)
5. That stat is raised by one stage
6. Ability popup is displayed

### Interactions
- **Breakable**: Can be suppressed by abilities like Mold Breaker
- **Stackable**: Can potentially stack with other stat-boosting effects
- **Immunity**: Provides complete immunity to Fire-type damage when absorbed
- **Priority**: Absorption occurs before damage calculation

This ability is essentially a Fire-type version of classic redirection abilities like Lightning Rod (Electric) and Storm Drain (Water), but focuses on boosting offensive power rather than Special Attack specifically.
---
id: 677
name: Petrify
status: reviewed
character_count: 77
---

# Petrify - Ability ID 677

## In-Game Description
Clears stat buffs then lowers attack by one stage on entry.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Removes stat raises from opposing Pokemon, then drops their Speed by 1 stage.

## Detailed Mechanical Explanation

### Mechanical Details
- **Entry Effect Combination**: Uses `UseIntimidateClone()` for intimidate effect + `TryResetBattlerStatChanges()` for buff clearing
- **Intimidate Component**: Lowers opposing Pokemon's Attack by 1 stage
- **Buff Clearing**: Removes all positive stat changes (`RESET_STAT_BUFFS`) from opposing Pokemon
- **Target Scope**: Affects all opposing Pokemon in battle
- **Execution Order**: Intimidate effect occurs first, then buff clearing
- **Battle Script**: Uses `BattleScript_Petrify` when stats are cleared
- **Return Logic**: Returns true if either intimidate worked OR buffs were cleared

### Strategic Applications
- **Setup Counter**: Completely shuts down opponents who have been setting up with stat boosts
- **Entry Hazard**: Creates immediate pressure with Attack reduction plus boost removal
- **Reset Tool**: Forces opponents back to neutral stat stages while imposing Attack penalty
- **Doubles Utility**: Affects multiple targets, making it valuable in double battles
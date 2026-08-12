---
id: 868
name: Lightning Aspect
status: reviewed
character_count: 236
---

# Lightning Aspect - Ability ID 868

## In-Game Description
Absorbs electric moves then ups highest stat by +1.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Absorbs Electric moves for immunity and boosts higher attacking stat by +1. Compares Attack vs Special Attack to determine boost target. Excellent for setup against Electric attacks while providing defensive immunity and offensive gains

## Detailed Mechanical Explanation

### Implementation Details
- **File**: `src/abilities.cc` lines 8790-8797
- **Ability Type**: Absorption ability with stat boost
- **Breakable**: Yes (affected by Mold Breaker and similar abilities)

### How It Works
1. **Trigger Condition**: Pokemon is targeted by an Electric-type move
2. **Absorption**: The move deals no damage (complete immunity)
3. **Stat Selection**: Uses `GetHighestAttackingStatId(battler, TRUE)` to determine which attacking stat is higher:
   - Compares Attack vs Special Attack only
   - Includes current stat stages in the calculation
   - Returns either `STAT_ATK` (1) or `STAT_SPATK` (4)
4. **Stat Boost**: Raises the selected stat by +1 stage
5. **Result**: Returns `ABSORB_RESULT_STAT` flag

### Comparison with Similar Abilities
- **Lightning Rod**: Same mechanic, also absorbs Electric moves and boosts highest attacking stat
- **Volt Absorb**: Only heals HP when hit by Electric moves (no stat boost)
- **Motor Drive**: Raises Speed when hit by Electric moves (different target stat)

### Strategic Applications
- **Doubles/Multi-battles**: Can redirect Electric moves from allies
- **Stat Optimization**: Particularly valuable for mixed attackers or Pokemon with similar Attack/Special Attack
- **Counterplay**: Setup opportunity against Electric-type moves

### Technical Notes
- The `GetHighestAttackingStatId` function only considers Attack and Special Attack
- Stat stages are included in the comparison (modified stats vs base stats)
- The ability triggers before damage calculation, providing complete immunity
- Works with both single-target and multi-target Electric moves

### Code References
- Main implementation: `src/abilities.cc:8790-8797`
- Stat selection function: `src/battle_util.c:8585-8604`
- Absorption constants: `include/battle_util.h:370-373`
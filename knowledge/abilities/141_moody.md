---
id: 141
name: Moody
status: reviewed
character_count: 119
---

# Moody - Ability ID 141

## In-Game Description
"Sharply raises one stat and lowers another each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

At the end of each turn, randomly selects one stat to raise by 2 stages and another different stat to lower by 1 stage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**Trigger Timing**: End of turn (after all other end-of-turn effects)

**Mechanics**:
1. Checks if any stats can be raised or lowered
2. If possible, randomly selects one stat from Attack, Defense, Special Attack, Special Defense, or Speed to sharply raise (+2 stages)
3. If possible, randomly selects a different stat to lower (-1 stage)
4. The same stat cannot be both raised and lowered in the same turn
5. If only raising or only lowering is possible, only that effect occurs
6. Does not activate on the turn the Pokemon switches in

**Important Notes**:
- Uses the full stat range (Attack through Speed - 5 stats total)
- Respects stat stage limits (+6/-6)
- Cannot select a stat that's already at its maximum for raising or minimum for lowering
- The ability will not activate if no stat changes are possible
- In Elite Redux, this occurs after other end-of-turn effects like weather damage

**Strategic Applications**:
- Extremely unpredictable but potentially powerful
- Can create both advantages and disadvantages
- Best used on Pokemon that can capitalize on any stat boost
- Risk vs. reward ability - the stat drops can be as impactful as the boosts
- Pairs well with moves like Stored Power that scale with stat boosts

**Code Implementation**: 
- Located in `src/abilities.cc` lines 1617-1646
- Uses `SetStatChanger(i, 2)` for the +2 stage boost  
- Uses `SET_STATCHANGER2` for the -1 stage drop
- Calls `BattleScript_MoodyActivates` to display the effects
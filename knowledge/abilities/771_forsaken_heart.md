---
id: 771
name: Forsaken Heart
status: reviewed
character_count: 100
---

# Forsaken Heart - Ability ID 771

## In-Game Description
"KOs dealt anywhere on the field raise Attack by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises Attack by one stage when any Pokemon faints on the battlefield, including allies and enemies.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Trigger Condition**: Any Pokemon fainting on the battlefield (`.onBattlerFaintsFor = APPLY_ON_ANY`)

**Effect**: Raises the user's Attack stat by one stage using `ChangeStatBuffs(battler, 1, STAT_ATK, MOVE_EFFECT_AFFECTS_USER | STAT_BUFF_DONT_SET_BUFFERS, NULL)`

**Key Differences from Similar Abilities**:
- **Moxie**: Only triggers when the user defeats an opponent (APPLY_ON_ATTACKER)
- **Soul Heart**: Same trigger condition but raises Special Attack instead of Attack
- **Forsaken Heart**: Triggers on ANY faint, making it more versatile in doubles/triples

**Implementation Details**:
- Uses the `onBattlerFaints` callback with `APPLY_ON_ANY` scope
- Calls `BattleScript_RaiseStatOnFaintingTarget` for the stat boost animation
- The `STAT_BUFF_DONT_SET_BUFFERS` flag prevents setting battle buffers during the stat change
- Can potentially activate multiple times per turn in multi-battles

**Strategic Applications**:
- Extremely powerful in doubles/triples where multiple KOs can occur
- Benefits from team strategies that result in frequent fainting
- Can turn disadvantageous situations (ally defeats) into stat boosts
- Particularly effective on bulky attackers who can survive to accumulate multiple boosts

**Battle Script Flow**:
1. Any Pokemon faints
2. Check if user has Forsaken Heart
3. Attempt to raise Attack by 1 stage
4. Display ability activation message and stat boost animation
5. Continue with battle flow

This ability represents a dark, opportunistic fighting style where the user grows stronger from witnessing death on the battlefield, regardless of whether it's friend or foe.
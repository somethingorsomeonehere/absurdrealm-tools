---
id: 857
name: Royal Decree
status: reviewed
character_count: 157
---

# Royal Decree - Ability ID 857

## In-Game Description
"Queenly Majesty + Glare on entry once per battle."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents the user and its ally from being targeted by priority moves with priority higher than 0. Use Glare on entry, paralyzing the target. Once per battle.

## Detailed Mechanical Explanation

### Mechanical Analysis

### Primary Effects
1. **Entry Move**: Uses Glare automatically when entering battle
   - Targets a random opponent
   - Paralysis effect that ignores type immunity (Normal-type move that can paralyze Electric-types)
   - Only triggers once per battle via SingleUseAbilityCounter mechanism
   - 100% accuracy, 20 PP equivalent

2. **Priority Move Blocking**: Inherited from Queenly Majesty
   - Blocks all enemy priority moves (moves with priority > 0)
   - Protection extends to allies (onImmuneFor = APPLY_ON_ALLY)
   - Only blocks moves from opposing team, not allies
   - Does not activate during extra attacks (gProcessingExtraAttacks check)

### Implementation Details
- **Breakable**: Yes - can be suppressed by Mold Breaker and similar abilities
- **Immunity Script**: Uses BattleScript_DazzlingProtected for priority move blocking
- **Single Use Counter**: Prevents multiple Glare uses if the Pokemon switches out and back in during the same battle
- **Code Structure**: Combination ability that delegates priority blocking to QueenlyMajesty implementation

## Battle Applications
- **Lead Pokemon Utility**: Excellent for lead positions to immediately cripple fast threats
- **Support Role**: Protects team from priority moves like Quick Attack, Bullet Punch, Sucker Punch
- **Speed Control**: Paralysis provides long-term speed control beyond the initial entry
- **Anti-Priority Meta**: Hard counters priority-based strategies and revenge killers

## Interactions
- **Type Immunity Bypass**: Glare can paralyze Electric-types due to EFFECT_PARALYZE_IGNORE_TYPE
- **Substitute Interaction**: Priority move blocking works through Substitute
- **Multi-Battle Persistence**: Single-use counter may reset between different battle formats
- **Team Protection**: Allies benefit from priority move immunity while this Pokemon is active

This ability combines immediate battlefield control through guaranteed paralysis with ongoing strategic value via priority move denial, making it exceptionally powerful for both offensive and defensive team compositions.
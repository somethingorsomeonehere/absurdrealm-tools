---
id: 596
name: Radio Jam
status: reviewed
character_count: 97
---

# Radio Jam - Ability ID 596

## In-Game Description
"20% chance to disable opponent's last move when hitting with sound moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

20% chance to disable the last move used by the target after landing a sound move. Lasts 4 turns.

## Detailed Mechanical Explanation

### Implementation Analysis

Radio Jam is implemented as an `onAttacker` callback in `src/abilities.cc`. The ability triggers when the user successfully hits an opponent with a sound-based move.

### Trigger Conditions
1. **ShouldApplyOnHitAffect(target)** - Standard hit effect validation
2. **CanBeDisabled(target)** - Target must not already be disabled and not be protected by ability status immunity
3. **IsSoundMove(battler, move)** - Move must have the `FLAG_SOUND` flag
4. **Random() % 100 < 20** - 20% chance to activate

### Effect
When all conditions are met, the ability applies `MOVE_EFFECT_DISABLE` via `AbilityStatusEffect()`, which calls `DisableLastUsedMove()` on the target.

### Sound Move Types
Sound moves include moves with the `FLAG_SOUND` flag such as:
- Hyper Voice
- Roar
- Growl
- Supersonic
- Screech
- Sing
- And many others

### Strategic Applications

### Offensive Use
- Excellent for disrupting setup sweepers who rely on specific moves
- Can disable key coverage moves, forcing switches
- Particularly effective against mono-attackers
- Works well with sound-based movesets

### Defensive Applications
- Can disable powerful STAB moves
- Useful for stalling strategies
- Helps against Pokemon with limited movepools

### Synergy Opportunities
- Pairs well with other sound-based abilities like Liquid Voice, Punk Rock
- Works with sound moves that have additional effects
- Can be combined with moves that force the opponent to use specific moves

### Competitive Considerations

### Strengths
- 20% chance provides consistent pressure without being overpowered
- Works with a wide variety of sound moves
- Can disable any move, including status moves
- No immunities beyond standard disable immunity

### Limitations
- Only works with sound moves
- Requires hitting the opponent first
- Cannot disable if target is already disabled
- Blocked by abilities that prevent status conditions

### Counters
- Soundproof ability blocks the triggering moves entirely
- Abilities that prevent status conditions (Limber, etc.)
- Substitute blocks the disable effect
- Pokemon with diverse movepools are less affected


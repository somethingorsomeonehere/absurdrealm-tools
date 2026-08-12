---
id: 769
name: Junshi Sanda
status: reviewed
character_count: 181
---

# Junshi Sanda - Ability ID 769

## In-Game Description
"Punches and Kicks are both Punches and Kicks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Punching moves are also treated as kicking moves, benefiting from Striker-type abilities. Kicking moves are also treated as punching moves, benefiting from Iron Fist-type abilities. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Junshi Sanda is a unique ability that creates a dual classification system for physical fighting moves. It operates through modifications to the `IsIronFistBoosted` and `IsStrikerBoosted` functions in the battle engine.

### Core Mechanics:

**Punching to Kicking Conversion:**
- When a battler has Junshi Sanda, moves with `FLAG_IRON_FIST_BOOST` (punching moves) also return true for `IsStrikerBoosted`
- This means punching moves like Mach Punch, Thunder Punch, and Ice Punch gain all benefits that normally only apply to kicking moves

**Kicking to Punching Conversion:**
- When a battler has Junshi Sanda, moves with `FLAG_STRIKER_BOOST` (kicking moves) also return true for `IsIronFistBoosted`
- This means kicking moves like High Jump Kick, Jump Kick, and Low Kick gain all benefits that normally only apply to punching moves

### Implementation Details:

The ability is implemented in the battle utility functions:

```c
int IsIronFistBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_IRON_FIST_BOOST) return TRUE;
    // Other conditions...
    if (gBattleMoves[move].flags & FLAG_STRIKER_BOOST && BattlerHasAbility(battler, ABILITY_JUNSHI_SANDA, FALSE)) return TRUE;
    return FALSE;
}

int IsStrikerBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_STRIKER_BOOST) return TRUE;
    if (gBattleMoves[move].flags & FLAG_IRON_FIST_BOOST && BattlerHasAbility(battler, ABILITY_JUNSHI_SANDA, FALSE)) return TRUE;
    return FALSE;
}
```

### Ability Synergies:

**Punching Move Boosters that now affect kicks:**
- Iron Fist: 1.3x damage multiplier
- Power Fists: 1.3x damage + uses Sp. Def for damage calculation
- Magical Fists: 1.3x damage + uses Sp. Atk for damage calculation
- Precise Fist: Guaranteed critical hits + 5x effect chance
- Nika: 1.3x damage multiplier
- Atomic Punch: 1.3x damage + Steel-type move boost
- Vitality Strike: Heals 10% of damage dealt

**Kicking Move Boosters that now affect punches:**
- Striker: 1.3x damage multiplier
- Roundhouse: Never misses + targets lower defensive stat
- Combat Specialist: Both Iron Fist and Striker effects
- Striker Pixilate: 1.3x damage + converts Normal moves to Fairy

### Strategic Applications:

1. **Move Pool Expansion**: Pokemon with mixed punching/kicking movepools can maximize their ability synergies
2. **Team Building**: Creates new strategic possibilities for Pokemon that previously couldn't benefit from both types of abilities
3. **Ability Stacking**: In multi-ability formats, this can create powerful combinations with other physical attack enhancers
4. **Type Coverage**: Allows for more flexible movesets since both punch and kick categories receive equal treatment

### Notable Interactions:

- Works with all current and future abilities that check `IsIronFistBoosted` or `IsStrikerBoosted`
- Does not create its own damage multiplier - it enables existing multipliers to apply to both move types
- The ability is "passive" - it has no direct implementation in abilities.cc but works through the battle utility functions
- Compatible with multi-hit moves, status moves, and any other moves that carry the appropriate flags

This makes Junshi Sanda a powerful enabler ability that dramatically expands the potential synergies available to Pokemon with diverse physical movesets.
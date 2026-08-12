---
id: 640
name: Rhythmic
status: reviewed
character_count: 126
---

# Rhythmic - Ability ID 640

## In-Game Description
Deals 10% more damage for each repeated move use.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Each consecutive use of the same move increases damage by 10%. No maximum cap. Resets when switching moves or when moves fail. 

## Detailed Mechanical Explanation

**Rhythmic** works similarly to the Metronome item but with unlimited scaling potential. Each consecutive use of the same move increases damage output by exactly 10%.

### Core Implementation
```cpp
constexpr Ability Rhythmic = {
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) { 
        MulModifier(modifier, UQ_4_12(1.0) + 10 * gBattleStruct->sameMoveTurns[battler]); 
    },
};
```

### Damage Progression
- **Turn 1**: 100% damage (base, no boost)
- **Turn 2**: 110% damage (+10%)
- **Turn 3**: 120% damage (+20% total)
- **Turn 4**: 130% damage (+30% total)
- **Turn 10**: 200% damage (+100% total)
- **No Cap**: Continues scaling indefinitely

## Trigger Conditions

- **Same Move Requirement**: Must use the exact same move consecutively
- **Successful Hit**: Move must not fail (`MOVE_RESULT_NO_EFFECT`)
- **Ability to Act**: Battler must not be unable to use moves

### Reset Conditions
Counter resets to 0 when:
- A different move is used
- The move fails completely
- The battler was unable to use the move
- During Parental Bond's first hit (doesn't increment)

## Numerical Effects

- **Base Formula**: `1.0 + (10 * sameMoveTurns)`
- **Increment**: Exactly 10% per consecutive use
- **Scaling Type**: Linear, additive progression
- **No Maximum**: Unlike similar mechanics, has no built-in cap

## Interactions

### Comparison to Metronome Item
| Aspect | Rhythmic Ability | Metronome Item |
|--------|------------------|----------------|
| **Boost per use** | Fixed 10% | Variable (typically 20%) |
| **Maximum cap** | None (unlimited) | 100% (capped) |
| **Item requirement** | No item needed | Requires holding Metronome |
| **Availability** | Always active | Item must be obtained |

### Synergy Effects
- **Echoed Voice**: Uses same `sameMoveTurns` counter, potentially stacking effects
- **Choice Items**: Excellent synergy since they lock you into one move
- **Potential Metronome Stack**: Could theoretically stack with Metronome item if available

## Special Cases

- **Move Variations**: Different forms of the same move (e.g., Hidden Power types) count as different moves
- **Parental Bond**: First hit doesn't increment counter, second hit gets current bonus
- **Unlimited Scaling**: In extended battles, damage can theoretically reach 300%+ 
- **Turn Tracking**: Each battler has independent counters

## Notes

- **High Risk/High Reward**: Commitment to one move provides exponential damage growth
- **No Item Slot Cost**: Frees up held item for other strategies
- **Strategic Depth**: Encourages move prediction and strategic commitment
- **Potentially Overpowered**: Unlimited scaling could become game-breaking in extended battles
- **Choice Item Synergy**: Natural partnership with Choice Band/Specs/Scarf
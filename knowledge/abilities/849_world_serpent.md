---
id: 849
name: World Serpent
status: reviewed
character_count: 114
---

# World Serpent - Ability ID 849

## In-Game Description
Physical non-contact moves deal 20% more damage. Contact moves can trap.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Physical non-contact moves deal 20% more damage. Contact moves have a 50% chance to trap the target for 4-5 turns.

## Detailed Mechanical Explanation

### Mechanics

World Serpent is a combination ability that merges:
- **Long Reach**: Boosts physical non-contact moves by 20%
- **Grip Pincer**: Contact moves can trap targets with 50% chance

### Long Reach Component
- Applies a 1.2x multiplier to physical moves that don't make contact
- Works with moves like Rock Throw, Earthquake, etc.
- Does not affect special moves or contact moves

### Grip Pincer Component
- Only triggers on moves that make contact
- 50% chance to inflict Wrapped status (STATUS2_WRAPPED)
- Trap duration: 4-5 turns normally, 7 turns if holding Grip Claw
- Trapped targets cannot miss when attacking the trapper
- Cannot trap targets already wrapped/bound

## Implementation Details

From `src/abilities.cc`:
```cpp
constexpr Ability WorldSerpent = {
    .onAttacker = GripPincer.onAttacker,
    .onOffensiveMultiplier = LongReach.onOffensiveMultiplier,
    .onAccuracy = GripPincer.onAccuracy,
};
```

The ability inherits:
- Attack handler from Grip Pincer (for trapping effect)
- Offensive multiplier from Long Reach (for damage boost)
- Accuracy handler from Grip Pincer (for guaranteed hits on trapped foes)

## Strategic Notes

This ability creates an interesting dual strategy:
1. Use physical non-contact moves for consistent 20% damage boost
2. Use contact moves when you want to trap opponents

The combination encourages tactical move selection based on the situation - trap when beneficial, or maintain distance for damage boost.
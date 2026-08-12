---
id: 622
name: Beautiful Music
status: reviewed
character_count: 157
---

# Beautiful Music - Ability ID 622

## In-Game Description
"Sound moves gain 50% chance to infatuate targets, ignoring ALL gender restrictions."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sound moves gain 50% chance to infatuate targets on hit (cuts their Attack and Special Attack in half). Can infatuate any Pokemon unlike regular infatuation.

## Detailed Mechanical Explanation

Beautiful Music adds a 50% chance to infatuate targets when using sound-based moves, with the unique property of bypassing all gender restrictions. This makes it one of only two abilities (along with Pure Love) that can infatuate any Pokemon regardless of gender or lack thereof.

### Mechanics
- **Trigger**: When using any sound-based move (FLAG_SOUND)
- **Effect**: 50% chance to infatuate the target after hit
- **Special Property**: canInfatuateAny = TRUE (ignores gender restrictions)
- **Affected Moves**: All sound moves including Hyper Voice, Boomburst, Disarming Voice, Sing, Perish Song, etc.

### Code Implementation
Located in `src/abilities.cc`:
```cpp
constexpr Ability BeautifulMusic = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(Random() % 2)  // 50% chance
        CHECK(IsSoundMove(battler, move))
        return AbilityStatusEffect(MOVE_EFFECT_ATTRACT);
    },
    .canInfatuateAny = TRUE,
};
```

### AI Scoring
The AI recognizes this ability and adds a 50% weighted attract score when evaluating sound moves, helping it understand the utility of the secondary effect.

### Strategic Value
- Turns sound moves into dual-purpose attacks (damage + disable)
- Works on ALL Pokemon including genderless ones
- Synergizes with powerful sound moves like Boomburst
- Creates setup opportunities with 50% opponent immobilization chance


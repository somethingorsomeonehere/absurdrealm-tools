---
id: 291
name: Aurora Borealis
status: reviewed
character_count: 224
---

# Aurora Borealis - Ability ID 291

## In-Game Description
"Ice-type moves gain STAB. Moves always benefit from hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Aurora Borealis grants STAB to all Ice-type moves regardless of the Pokemon's typing. Weather Ball becomes Ice-type with doubled power, Aurora Veil works without hail, and weather-based Ice moves like Blizzard to never miss.

## Detailed Mechanical Explanation
*For Discord/reference use*

Aurora Borealis is a unique weather-manipulation ability that provides two key benefits:

### Core Mechanics

1. **Ice-type STAB**: All Ice-type moves gain Same Type Attack Bonus (1.5x damage) regardless of the Pokemon's actual typing
2. **Permanent Hail Benefits**: The Pokemon is treated as if it's in hail weather for all move calculations and effects

### Implementation Details

```cpp
constexpr Ability AuroraBorealis = {
    .onStab = +[](ON_STAB) -> int { return moveType == TYPE_ICE; },
    .hailImmune = TRUE,
};
```

### Weather-Related Benefits (Always Active)

The ability makes the Pokemon count as being in hail weather through the `HasAuroraBorealis()` function, which provides:

- **Weather Ball**: Becomes Ice-type with doubled power (120 base power instead of 50)
- **Aurora Veil**: Can be used without actual hail weather
- **Blizzard**: Never misses (bypasses accuracy check)
- **Sheer Cold**: Never misses (bypasses accuracy check) 
- **Freeze-Dry**: Never misses (bypasses accuracy check)

### Battle System Integration

```cpp
// Weather Ball type change
if (HasAuroraBorealis(battlerAtk)) return TYPE_ICE;

// Accuracy bypass for Ice moves
else if ((IsBattlerWeatherAffected(battlerDef, WEATHER_HAIL_ANY) || HasAuroraBorealis(battlerAtk)) &&
         (gBattleMoves[move].effect == EFFECT_FREEZE_DRY || move == MOVE_SHEER_COLD || move == MOVE_BLIZZARD))
    prio = ACCURACY_HITS_IF_POSSIBLE;

// Aurora Veil setup
if (!(IsBattlerWeatherAffected(gActiveBattler, WEATHER_HAIL_ANY) || HasAuroraBorealis(gActiveBattler))) {
    gMoveResultFlags |= MOVE_RESULT_MISSED;
}
```

### Strategic Implications

**Offensive Applications:**
- Non-Ice types can effectively use Ice-type moves with STAB
- Weather Ball becomes a reliable 120 base power Ice move
- Blizzard becomes a 110 base power move that never misses
- Enables Ice-type coverage without requiring Ice typing

**Defensive Applications:**
- Hail immunity prevents passive damage
- Can set up Aurora Veil for team support without weather dependency
- Enables defensive Ice-type strategies on non-Ice Pokemon

### Numerical Values
- STAB bonus: 1.5x damage multiplier for Ice moves
- Weather Ball power: 120 base power (doubled from 50)
- Accuracy boost: 100% hit rate for Blizzard, Sheer Cold, and Freeze-Dry
- Hail immunity: No passive damage from hail weather

### Interactions with Other Abilities/Mechanics

**Synergies:**
- **Adaptability**: Would boost Ice STAB to 2x instead of 1.5x
- **Skill Link**: Makes multi-hit Ice moves more reliable
- **Refrigerate/Pixilate**: Would not stack (Aurora Borealis only affects naturally Ice-type moves)

**Counters:**
- **Cloud Nine/Air Lock**: Negates the weather benefits but not the STAB
- **Magic Bounce**: Can reflect Aurora Veil back to the user
- **Infiltrator**: Bypasses Aurora Veil protection

### Common Users
This is a custom Elite Redux ability, so usage depends on which Pokemon are assigned this ability in the ROM hack's design.

### Competitive Usage Notes
- Excellent for providing Ice coverage to non-Ice types
- Enables reliable Blizzard spam without weather setup
- Weather Ball becomes a powerful neutral coverage option
- Aurora Veil support without weather dependency makes it valuable for team support

### Example Damage Calculations
Assuming 100 Attack/Special Attack stat against 100 Defense/Special Defense:

- **Ice Punch** (75 base power): ~56 damage to ~84 damage with Aurora Borealis STAB
- **Weather Ball** (50/120 base power): ~37 damage to ~89 damage with Aurora Borealis
- **Blizzard** (110 base power): ~82 damage to ~123 damage with Aurora Borealis STAB + guaranteed hit

### Version History
- Introduced in Elite Redux as a custom ability
- ID 291 in the ability enumeration
- Part of the extended ability system beyond the base game's 267 abilities
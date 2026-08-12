---
id: 604
name: Desert Spirit
status: reviewed
character_count: 222
---

# Desert Spirit - Ability ID 604

## In-Game Description
"Summons sandstorm on entry. Ground moves hit airborne Pokemon during sandstorm."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Summons sandstorm on entry, lasting 8 turns (12 with Smooth Stone). During sandstorm, the user's Ground-type moves bypass immunity and hit airborne Pokemon with normal effectiveness. The user is immune to sandstorm damage. 

## Detailed Mechanical Explanation

Desert Spirit (ID 604) is implemented in `src/abilities.cc` at line 6370 with the following mechanics:

### Entry Effect
- Uses `SandStream.onEntry` - summons sandstorm weather on switch-in
- Lasts 8 turns like standard weather abilities
- Can be blocked by Primal weather conditions

### Type Effectiveness Override
- Implements `onAfterTypeEffectiveness` callback
- Allows Ground-type moves to hit airborne Pokemon during sandstorm
- Checks: `*mod == 0 && !IsBattlerGrounded(target) && moveType == TYPE_GROUND && IsBattlerWeatherAffected(battler, WEATHER_SANDSTORM_ANY)`
- Overrides immunity by setting `*mod = UQ_4_12(1.0)` (normal effectiveness)

### Additional Properties
- `sandImmune = TRUE` - immune to sandstorm damage
- No other special properties or modifiers


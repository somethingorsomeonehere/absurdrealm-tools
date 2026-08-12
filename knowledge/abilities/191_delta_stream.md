---
id: 191
name: Delta Stream
status: reviewed
character_count: 227
---

# Delta Stream - Ability ID 191

## In-Game Description
"Strong Winds until switched out. Weather-based moves not usable."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Strong Winds lasting until user switches. Reduces super-effective damage to all active Flying-types to neutral. Blocks all weather-based moves from hitting opponents. Cannot be overridden except by other primal weather. 

## Detailed Mechanical Explanation
**Delta Stream** creates the primal weather "Strong Winds" that provides unique Flying-type protection and weather move immunity.

### Trigger Conditions
- Activates upon entering battle via `onEntry` hook
- Sets weather to `ENUM_WEATHER_STRONG_WINDS` (ID 7)
- Always succeeds unless another primal weather exists

### Weather Properties
1. **Primal Weather Classification**:
   - Part of `WEATHER_PRIMAL_ANY` group
   - Cannot be overridden by regular weather
   - Only replaceable by Desolate Land or Primordial Sea
   - Regular weather attempts show "remained unchanged"

2. **Duration**:
   - **Permanent** while ability holder in battle
   - Ends when user switches out or faints
   - No turn counter or limit
   - Not affected by weather items

### Primary Effects
1. **Flying-type Damage Reduction**:
   - Super-effective moves (2x or more) vs Flying-types to 1x damage
   - Affects ALL Flying-type Pokemon on field, not just user
   - Still shows "It's super effective!" but damage is neutral
   - Does not affect non-super-effective moves

2. **Weather-Based Move Immunity**:
   - Blocks ALL moves with `FLAG_WEATHER_BASED`
   - Only blocks when targeting opponents (self-targeting allowed)
   - Shows "Soundproof Protected" message (script reuse)
   - Affected moves include: Weather Ball, Solar Beam/Blade, Thunder, Hurricane, etc.

3. **Unique Properties**:
   - No weather damage (unlike hail/sand)
   - No type boosts/reductions
   - No accuracy changes
   - Pure defensive weather

### Special Interactions
- **Cloud Nine/Air Lock**: Cannot suppress primal weather
- **Weather Moves**: Sunny Day, Rain Dance, etc. fail
- **Multiple Delta Stream**: Last one maintains effect
- **Castform**: No form change (no wind form)

### Implementation Details
```cpp
constexpr Ability DeltaStream = {
    .onEntry = /* Sets strong winds */,
    .onImmune = /* Blocks weather-based moves */
};
```

- Uses `TryChangeBattleWeather` for activation
- `onImmune` hook intercepts weather-based moves
- Script: `BattleScript_DeltaStreamActivates`

### Strategic Notes
- Excellent for Flying-type teams
- Counters weather-based strategies
- Provides unique defensive utility
- Only primal weather with move blocking

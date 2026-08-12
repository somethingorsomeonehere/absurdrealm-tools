---
id: 189
name: Primordial Sea
status: reviewed
character_count: 271
---

# Primordial Sea - Ability ID 189

## In-Game Description
"Heavy Rain until switched out. Fire-type moves are unusable."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Heavy Rain that lasts until user switches. Completely nullifies all damaging Fire moves. Water moves gain 50% boost. Cannot be overridden except by other primal weather. Activates extra effects on rain related moves. Halves the effectiveness of sun related moves.

## Detailed Mechanical Explanation
**Primordial Sea** creates a special primal weather condition called "Heavy Rain" that provides extreme weather control and Fire-type immunity.

### Trigger Conditions
- Activates immediately when the Pokemon enters battle
- Uses `onEntry` hook to set `ENUM_WEATHER_RAIN_PRIMAL` (weather ID 6)
- Always succeeds unless another primal weather is active

### Weather Properties
1. **Primal Weather Classification**:
   - Part of `WEATHER_PRIMAL_ANY` group
   - Cannot be overridden by regular weather moves/abilities
   - Only replaceable by Desolate Land or Delta Stream
   - Regular weather changes show "The weather remained unchanged!"

2. **Duration**:
   - **Permanent** while the user remains in battle
   - Ends immediately when user switches out or faints
   - No turn counter like regular weather
   - Not affected by weather-extending items

### Primary Effects
1. **Fire-type Move Nullification**:
   - ALL damaging Fire-type moves automatically fail
   - Displays: "The Fire-type attack fizzled out in the heavy rain!"
   - Move accuracy is checked first, PP is consumed, then move fails
   - Status Fire moves (power = 0) are not affected
   - Multi-turn Fire moves are cancelled

2. **Standard Rain Effects**:
   - Water-type moves: 1.5x damage (50% boost)
   - Thunder and Hurricane: 100% accuracy
   - Weather Ball: Becomes Water-type, doubles in power
   - Solar Beam/Solar Blade: Power reduced to 50%
   - Moonlight/Morning Sun/Synthesis: Restore 1/4 HP

3. **Ability Interactions**:
   - Swift Swim: Doubles Speed
   - Rain Dish: Restores 1/16 HP per turn
   - Dry Skin: Restores 1/8 HP per turn
   - Hydration: Cures status conditions
   - Forecast: Castform becomes Water-type

### Special Mechanics
- **Priority System**: Primal weather has absolute priority over regular weather
- **Multiple Primal Users**: Last one to enter overwrites (Speed determines order)
- **Air Lock/Cloud Nine**: Cannot suppress primal weather effects
- **Weather Rocks**: Have no effect on duration

### Implementation Details
- Simple struct with `onEntry` hook in `src/abilities.cc`
- Triggers `BattleScript_PrimordialSeaActivates`
- Fire nullification handled in damage calculation with move type check
- Part of `WEATHER_RAIN_ANY` for general rain checks

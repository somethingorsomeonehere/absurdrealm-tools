---
id: 190
name: Desolate Land
status: reviewed
character_count: 234
---

# Desolate Land - Ability ID 190

## In-Game Description
"Intense Sun until switched out. Water-type moves are unusable."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Extremely Harsh Sunlight lasting until user switches. Completely nullifies all damaging Water moves. Fire moves gain 50% boost. Cannot be overridden except by other primal weather. Activates extra effects on sun related moves.

## Detailed Mechanical Explanation
**Desolate Land** creates the primal weather "Extremely Harsh Sunlight" that provides ultimate sun control and Water-type immunity.

### Trigger Conditions
- Activates when the Pokemon enters battle
- Uses `onEntry` hook to set `ENUM_WEATHER_SUN_PRIMAL`
- Always succeeds unless another primal weather is active

### Weather Properties
1. **Primal Weather Status**:
   - Classified as `WEATHER_PRIMAL_ANY`
   - Cannot be changed by regular weather moves/abilities
   - Only replaceable by Primordial Sea or Delta Stream
   - Weather change attempts show "The weather remained unchanged!"

2. **Duration**:
   - **Permanent** while user is in battle
   - Ends only when user switches out or faints
   - No turn limit or countdown
   - Weather rocks have no effect

### Primary Effects
1. **Water-type Move Nullification**:
   - ALL damaging Water-type moves fail completely
   - Message: "The Water-type attack evaporated in the extremely harsh sunlight!"
   - Accuracy check occurs, PP consumed, then move fails
   - Status Water moves (power = 0) still work
   - Multi-turn Water moves cancelled

2. **Enhanced Sun Effects**:
   - Fire-type moves: 1.5x damage (50% boost)
   - Water-type moves: Completely fail (not just reduced)
   - Thunder/Hurricane: 50% accuracy
   - Solar Beam/Solar Blade: No charge turn
   - Weather Ball: Fire-type, double power

3. **Status & Recovery**:
   - Prevents freezing
   - Thaws frozen Pokemon
   - Moonlight/Morning Sun/Synthesis: Restore 2/3 HP
   - Growth: +2 Attack and Special Attack

4. **Ability Interactions**:
   - Chlorophyll: Doubles Speed
   - Solar Power: 1.5x Special Attack, lose 1/8 HP
   - Flower Gift: Team gains Attack/Special Defense boost
   - Leaf Guard: Prevents status conditions
   - Harvest: 100% chance to restore berries

### Special Mechanics
- **Primal Priority**: Absolute priority over regular sun
- **vs Other Primals**: Can override other primal weather based on entry order
- **Air Lock/Cloud Nine**: Cannot suppress primal weather
- **Drought Interaction**: Drought fails if Desolate Land active

### Key Differences from Regular Sun
- Lasts until switch (not turn-limited)
- Water moves fail completely (not just -50%)
- Cannot be overridden by regular weather
- Part of exclusive primal weather category

### Implementation Details
- Simple `onEntry` implementation in `src/abilities.cc`
- Uses `BattleScript_DesolateLandActivates`
- Water nullification in damage calculation via move type check
- Part of `WEATHER_SUN_ANY` for general sun checks

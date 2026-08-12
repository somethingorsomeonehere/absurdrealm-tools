---
id: 70
name: Drought
status: reviewed
character_count: 164
---

# Drought - Ability ID 70

## In-Game Description
"Summons sun on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Summons harsh sunlight for 8 turns (12 with Heat Rock) on entry. Boosts Fire moves by 50%, reduces Water moves by 50%. Activates extra effects on sun related moves.

## Detailed Mechanical Explanation
**Drought** sets up harsh sunlight weather automatically when the Pokemon with this ability enters battle. This weather effect is identical to using the move Sunny Day, but doesn't consume a turn.

### Trigger Conditions
- Activates immediately upon entering battle (switch-in, battle start, or after fainting an opponent)
- Uses the `onEntry` hook in the ability system
- Cannot activate if primal weather is already present

### Weather Duration
- **Base Duration**: 8 turns (defined by `WEATHER_DURATION` constant)
- **Extended Duration**: 12 turns if the user holds Heat Rock
- **Turn Counting**: Duration counts down at the end of each turn

### Sun Weather Effects
1. **Type Modifications**:
   - Fire-type moves: 1.5x damage (50% boost)
   - Water-type moves: 0.5x damage (50% reduction)

2. **Move Changes**:
   - Solar Beam and Solar Blade: No charge turn required
   - Thunder and Hurricane: Accuracy reduced to 50%
   - Weather Ball: Becomes Fire-type and doubles in power
   - Moonlight/Morning Sun/Synthesis: Restore 2/3 HP instead of 1/2

3. **Status Effects**:
   - Prevents Pokemon from being frozen
   - Thaws already frozen Pokemon

4. **Ability Interactions**:
   - Activates Chlorophyll (doubles Speed)
   - Activates Solar Power (1.5x Special Attack, lose 1/8 HP per turn)
   - Activates Flower Gift (boosts team's Attack and Special Defense)
   - Activates Forecast (Castform becomes Fire-type)
   - Activates Leaf Guard (prevents status conditions)

### Special Interactions
- **Primal Weather**: Cannot override Desolate Land, Primordial Sea, or Delta Stream. If blocked, displays "The extremely harsh sunlight was not lessened at all!"
- **Weather Competition**: Can be overridden by other weather abilities or moves
- **Cloud Nine/Air Lock**: These abilities suppress sun's effects while active
- **Multiple Users**: If multiple Drought users enter simultaneously, speed determines order

### Implementation Details
- Located in `src/abilities.cc` at line 993
- Uses battle script `BattleScript_DroughtActivates`
- Returns `NO_ANNOUNCE` when blocked by primal weather to prevent duplicate ability announcement
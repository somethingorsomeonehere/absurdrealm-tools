---
id: 45
name: Sand Stream
status: reviewed
character_count: 212
---

# Sand Stream - Ability ID 45

## In-Game Description
"Summons a sandstorm on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Summons a Sandstorm for 8 turns (12 with Smooth Rock) on entry. Damages non-Rock/Ground/Steel types by 1/16 HP per turn. Rock-types gain a 50% Special Defense boost. Halves the effectiveness of sun related moves.

## Detailed Mechanical Explanation
**Sand Stream** automatically sets up a sandstorm when the Pokemon enters battle, providing the same effect as the move Sandstorm without using a turn.

### Trigger Conditions
- Activates immediately upon entering battle (switch-in, battle start, or after KO)
- Uses the `onEntry` hook in the ability system
- Fails if primal weather is active

### Weather Duration
- **Base Duration**: 8 turns (defined by `WEATHER_DURATION`)
- **Extended Duration**: 12 turns with Smooth Rock item
- Duration decreases at the end of each turn

### Sandstorm Effects
1. **Damage Per Turn**:
   - Deals 1/16 max HP damage to all Pokemon except:
     - Rock-type Pokemon
     - Ground-type Pokemon
     - Steel-type Pokemon
   - Also immune: Pokemon with Sand Veil, Sand Rush, Sand Force, Overcoat, or holding Safety Goggles

2. **Stat Modifications**:
   - Rock-type Pokemon: +50% Special Defense
   - No accuracy/evasion changes in Elite Redux (unlike base games)

3. **Move Changes**:
   - Weather Ball: Becomes Rock-type and doubles in power
   - Solar Beam/Solar Blade: Power reduced to 50%
   - Moonlight/Morning Sun/Synthesis: Restore 1/4 HP instead of 1/2

4. **Ability Interactions**:
   - Sand Veil: +25% evasion
   - Sand Rush: Doubles Speed
   - Sand Force: Rock/Ground/Steel moves get 30% power boost
   - Forecast: Castform becomes Rock-type (if applicable)

### Special Interactions
- **Primal Weather**: Cannot override Desolate Land, Primordial Sea, or Delta Stream. Shows special blocked message
- **Weather Priority**: Can override other non-primal weather
- **Multiple Sand Stream**: If multiple users enter, fastest goes last (overwrites others)
- **Cloud Nine/Air Lock**: Suppresses sandstorm effects while active

### Implementation Details
- Ability struct definition: `src/abilities.cc` line 787
- Uses `TryChangeBattleWeather` with `ENUM_WEATHER_SANDSTORM`
- Battle script: `BattleScript_SandstreamActivates`
- Weather duration constants in `include/battle_util.h`

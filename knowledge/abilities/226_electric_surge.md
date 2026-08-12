---
id: 226
name: Electric Surge
status: reviewed
character_count: 193
---

# Electric Surge - Ability ID 226

## In-Game Description
"Casts Electric Terrain on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Electric Terrain for 8 turns (12 with Terrain Extender) upon entry. Grounded Pokemon cannot fall asleep and Electric moves gain 30% power boost. Overrides other terrains when activated.

## Detailed Mechanical Explanation
**Electric Surge** automatically sets Electric Terrain when the Pokemon enters battle, providing powerful Electric-type support and sleep immunity.

### Trigger Conditions
- Activates immediately upon entering battle
- Uses `onEntry` hook with `TryChangeBattleTerrain`
- Overwrites any existing terrain (Grassy, Psychic, Misty)

### Terrain Duration
- **Base Duration**: 8 turns
- **Extended Duration**: 12 turns with Terrain Extender item
- Timer counts down at end of each turn
- Can be permanent in special battle conditions

### Electric Terrain Effects
1. **Electric-type Power Boost**:
   - Electric moves used by grounded Pokemon: 1.5x power (50% boost)
   - Only affects Pokemon touching the ground
   - Flying-types, Levitate, Magnet Rise users unaffected

2. **Sleep Prevention**:
   - Grounded Pokemon cannot fall asleep
   - Already sleeping Pokemon don't wake up
   - Rest fails for grounded Pokemon
   - Yawn fails to cause sleep on grounded targets

3. **Move Interactions**:
   - Rising Voltage: 2x base power (140) vs grounded targets
   - Nature Power: Becomes Thunderbolt
   - Secret Power: May cause paralysis
   - Camouflage: User becomes Electric-type

4. **Ability Synergies**:
   - Hadron Engine: Boosts Special Attack in Electric Terrain
   - Quark Drive: Activates stat boost
   - Surge Surfer: Doubles Speed on Electric Terrain

### Grounded vs Ungrounded
**Grounded** (affected by terrain):
- Non-Flying types without Levitate
- Not using Magnet Rise/Telekinesis
- Not holding Air Balloon

**Special Cases**:
- Pokemon with Electric Surge/Hadron Engine treated as terrain-affected even if not grounded
- Roost temporarily grounds Flying-types
- Gravity grounds all Pokemon

### Special Interactions
- **Weather**: Permanent Electric Terrain created by Rain Thunderstorm weather
- **Terrain Competition**: Only one terrain active at a time
- **Misty Terrain**: Overrides when Electric Surge activates
- **Max Moves**: Max Lightning extends duration

### Disabled Abilities
Electric Surge prevents these abilities from activating on switch-in:
- ABILITY_GENERATOR
- ABILITY_ENERGIZED

### Implementation Details
- Uses `STATUS_FIELD_ELECTRIC_TERRAIN` flag
- Script: `BattleScript_ElectricSurgeActivates`
- Terrain timer managed by `gFieldTimers.terrainTimer`
- Standard 1.5x multiplier (`UQ_4_12(1.5)`)
---
id: 229
name: Grassy Surge
status: reviewed
character_count: 168
---

# Grassy Surge - Ability ID 229

## In-Game Description
"Casts Grassy Terrain on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Grassy Terrain for 8 turns (12 with Terrain Extender) on entry. Grounded Pokemon heal 1/16 HP per turn and Grass moves gain 30% power. Overrides other terrains.

## Detailed Mechanical Explanation
**Grassy Surge** automatically establishes Grassy Terrain when the Pokemon enters battle, providing healing and Grass-type enhancement.

### Trigger Conditions
- Activates on battle entry via `onEntry` hook
- Uses `TryChangeBattleTerrain` to set terrain
- Replaces any existing terrain immediately

### Terrain Duration
- **Base Duration**: 8 turns
- **Extended Duration**: 12 turns with Terrain Extender
- Counts down at end of each turn
- Can be permanent with special flags

### Grassy Terrain Effects
1. **Passive Healing**:
   - Grounded Pokemon restore 1/16 max HP per turn
   - Healing occurs at turn end after status damage
   - Does not heal Pokemon at full HP
   - Cannot revive fainted Pokemon

2. **Grass-type Power Boost**:
   - Grass moves from grounded Pokemon: 1.5x power (50% boost)
   - Note: Config may reduce to 1.3x in Gen 8+ mechanics
   - Only affects grounded attackers

3. **Ground-type Move Interaction**:
   - **Elite Redux Specific**: NO damage reduction
   - Code shows `UQ_4_12(1.0)` modifier (100% damage)
   - Earthquake, Bulldoze, Magnitude unaffected
   - Different from mainline games (50% reduction)

4. **Move Changes**:
   - Nature Power: Becomes Energy Ball
   - Secret Power: May cause sleep
   - Camouflage: User becomes Grass-type
   - Grassy Glide: Gains priority in Grassy Terrain

5. **Ability Interactions**:
   - Grass Pelt: +50% Defense in Grassy Terrain
   - Grassy Surge users always count as grounded
   - Quark Drive: Can activate stat boosts

### Grounded Pokemon Definition
**Affected by terrain**:
- Non-Flying types
- No Levitate ability
- Not using Magnet Rise
- Air Balloon not active

**Always grounded**:
- Using Roost (temporary)
- Under Gravity effect
- Hit by Smack Down

### Special Mechanics
- **Terrain Override**: Removes Electric/Psychic/Misty Terrain
- **Max Overgrowth**: Sets terrain and deals damage
- **Terrain Pulse**: Becomes Grass-type, doubles power
- **Weather Independence**: Works alongside any weather

### Implementation Notes
- Status flag: `STATUS_FIELD_GRASSY_TERRAIN`
- Script: `BattleScript_GrassySurgeActivates`
- Healing handled in end-turn processing
- Power boost in damage calculation

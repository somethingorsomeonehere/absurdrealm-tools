---
id: 227
name: Psychic Surge
status: reviewed
character_count: 287
---

# Psychic Surge - Ability ID 227

## In-Game Description
"Casts Psychic Terrain on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Psychic Terrain for 8 turns (12 with Terrain Extender) on entry. Grounded Pokemon are immune to priority moves from opponents. Psychic moves gain 30% power boost. Expanding Force hits all foes with increased power. Nature Power becomes Psychic. Overrides other existing terrains.

## Detailed Mechanical Explanation
**Psychic Surge** automatically establishes Psychic Terrain upon entering battle, providing priority protection and Psychic-type enhancement.

### Trigger Conditions
- Activates immediately on battle entry
- Uses `onEntry` hook with `TryChangeBattleTerrain`
- Overwrites any existing terrain effect

### Terrain Duration
- **Base Duration**: 8 turns (not 5 like Gen 7)
- **Extended Duration**: 12 turns with Terrain Extender
- Timer decreases at turn end
- Can be permanent in special battles

### Psychic Terrain Effects
1. **Priority Move Protection**:
   - Grounded Pokemon immune to opponent's priority moves
   - Blocks: Quick Attack, Fake Out, Extreme Speed, etc.
   - Does NOT block ally's priority moves
   - Prankster status moves also blocked
   - Self-targeting priority moves still work

2. **Psychic-type Power Boost**:
   - Psychic moves from grounded users: 1.3x power (30% boost)
   - Standard terrain boost multiplier
   - Only affects grounded attackers

3. **Move Interactions**:
   - Expanding Force: Power 80to120, hits both opponents
   - Nature Power: Becomes Psychic
   - Secret Power: Lowers Speed by 1 stage
   - Camouflage: User becomes Psychic-type
   - Terrain Pulse: Psychic-type, double power

4. **Ability Synergies**:
   - Telepathy: Enhanced in Psychic Terrain
   - Psychic Surge users count as grounded
   - Quark Drive: Activates stat boosts

### Priority Blocking Details
**Blocked moves must be**:
- Priority > 0 (positive priority)
- Targeting a grounded opponent
- Used by an opponent (not ally)

**Common blocked moves**:
- Quick Attack, Mach Punch, Aqua Jet
- Fake Out, Extreme Speed, Sucker Punch
- Prankster-boosted status moves
- Gale Wings Flying moves

### Grounded vs Airborne
**Protected by terrain**:
- Non-Flying/Levitating Pokemon
- Not using Magnet Rise
- No Air Balloon

**Not protected**:
- Flying-types (unless Roosting)
- Levitate ability
- Magnet Rise/Telekinesis users

### Special Interactions
- **vs Other Terrains**: Removes when activated
- **Trick Room**: Works independently
- **Expanding Force**: Major synergy move
- **Max Mindstorm**: Sets terrain + damage

### Implementation Details
- Flag: `STATUS_FIELD_PSYCHIC_TERRAIN`
- Priority block: `CANCELLER_PSYCHIC_TERRAIN`
- Script: `BattleScript_PsychicSurgeActivates`
- Boost uses standard 1.3x multiplier

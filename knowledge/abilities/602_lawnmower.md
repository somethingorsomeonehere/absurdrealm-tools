---
id: 602
name: Lawnmower
status: reviewed
character_count: 184
---

# Lawnmower - Ability ID 602

## In-Game Description
"Removes terrain on switch-in. Stat up if terrain removed."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On switch-in, removes any active terrain and gains a stat boost: Defense +1 when removing Grassy or Electric Terrain, Special Defense +1 when removing Misty, Psychic, or Toxic Terrain. 

## Detailed Mechanical Explanation

**Lawnmower** is a terrain-clearing ability that triggers on switch-in, removing any active terrain and providing a stat boost based on which terrain was removed.

### Terrain Removal
The ability removes **all types of terrain**:
- Grassy Terrain
- Misty Terrain  
- Electric Terrain
- Psychic Terrain
- Toxic Terrain

### Stat Boost Logic
The ability provides **different stat boosts depending on which terrain is removed**:
- **Defense +1 Stage**: When removing Grassy Terrain or Electric Terrain
- **Special Defense +1 Stage**: When removing Misty Terrain, Psychic Terrain, or Toxic Terrain

## Trigger Conditions

- **On Entry**: Activates when the Pokemon switches into battle
- **Requirement**: Only triggers if any terrain is currently active (`STATUS_FIELD_TERRAIN_ANY`)
- **Failure Condition**: No activation if no terrain is present (fails silently)

## Numerical Effects

- **Stat Boost**: +1 stage to either Defense or Special Defense
- **Terrain Removal**: Complete removal of active terrain effect
- **Guaranteed**: Stat boost is guaranteed if terrain is removed

## Interactions

- **Terrain Setters**: Directly counters abilities like Electric Surge, Grassy Surge, etc.
- **Priority Moves**: Removing Psychic Terrain allows priority moves to work again
- **Status Effects**: Removing Misty Terrain removes status immunity
- **Move Power**: Removing terrain eliminates terrain-based move power boosts

## Special Cases

- **Multiple Terrains**: If somehow multiple terrains are active, removes all of them
- **Terrain Extension**: Works against extended terrain effects from items or moves
- **Team Strategy**: Can remove beneficial terrain from your own team for the stat boost

## Notes

- **Strategic Utility**: Provides terrain control plus defensive boost
- **Timing Dependent**: Switch-in timing becomes crucial for maximum benefit
- **Risk/Reward**: Must weigh removing beneficial terrain vs. gaining stat boost
- **AI Integration**: AI correctly evaluates terrain presence before switching in
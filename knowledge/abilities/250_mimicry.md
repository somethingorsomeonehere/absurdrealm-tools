---
id: 250
name: Mimicry
status: reviewed
character_count: 285
---

# Mimicry - Ability ID 250

## In-Game Description
"Changes type depending on active Terrain."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mimicry changes the Pokemon's type to match active terrain: Electric on Electric Terrain, Fairy on Misty Terrain, Grass on Grassy Terrain, or Psychic on Psychic Terrain. The type change persists until terrain ends or the Pokemon switches out. Retains type changes from moves like Soak.

## Detailed Mechanical Explanation
*For Discord/reference use*

Mimicry is a reactive ability that changes the Pokemon's type based on the active terrain:

### Terrain Type Mappings:
- **Electric Terrain** to Electric type
- **Misty Terrain** to Fairy type  
- **Grassy Terrain** to Grass type
- **Psychic Terrain** to Psychic type
- **No Terrain/Other** to Reverts to original type

### Activation Conditions:
1. **On Entry**: Activates when the Pokemon enters battle if terrain is already active
2. **On Terrain Change**: Activates whenever terrain changes during battle
3. **Must be alive**: Only works if the Pokemon is conscious

### Type Change Mechanics:
- Changes the Pokemon's **primary type** to match the terrain
- If the Pokemon already has the terrain's type, no change occurs
- The ability stores the original types (both type1 and type2) to restore later
- Type change is immediate and affects STAB, resistances, and weaknesses

### State Management:
- Uses `MimicryState` to track:
  - Original type1 and type2
  - Whether the ability is currently active
- When terrain ends or changes to non-matching terrain, reverts to stored original types

### Battle Messages:
- **Activation**: Uses `BattleScript_MimicryActivates` - "Battler's type changed to [Type]!"
- **Deactivation**: Uses `BattleScript_MimicryEnds` - "Mimicry ends!"

### Elite Redux Implementation Notes:
- Does **not** support Toxic Terrain (falls through to default case)
- Only works with the four standard terrains
- Type change persists through multiple turns until terrain expires
- Compatible with other type-changing effects and abilities

### Competitive Applications:
- Excellent for adapting to terrain-based teams
- Provides STAB for terrain-boosted moves
- Can exploit type matchups based on active terrain
- Requires terrain support to be effective
- Vulnerable when terrain is removed or expires
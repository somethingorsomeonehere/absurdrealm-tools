---
id: 841
name: Draconic Might
status: reviewed
character_count: 265
---

# Draconic Might - Ability ID 841

## In-Game Description
Draconize + Half Drake.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Dragon-type moves and grants STAB for Dragon-type moves, regardless of the user's typing. On entry, adds Dragon to the user's current typing. Retains Dragon typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation

### Mechanics

### Type Addition (Half Drake Component)
- Adds Dragon as a third type upon entering battle
- Dragon type cannot be removed by type-changing moves
- Grants STAB bonus to all Dragon-type moves

### Move Conversion (Draconize Component)
- Converts Normal-type moves to Dragon-type before damage calculation
- Converted moves receive STAB bonus from the added Dragon typing
- Works with physical and special Normal-type moves
- Does not affect status moves

### Damage Calculation
- Normal-type moves to Dragon-type moves
- Dragon-type moves get 1.5x STAB multiplier
- Combined effect: Normal moves deal 1.5x damage as Dragon-type
- Stacks with Adaptability for 2.0x STAB if present

## In-Game Appearance

When a Pokemon with Draconic Might enters battle:
1. "**[Pokemon] added the Dragon type!**" message appears
2. The Pokemon gains Dragon as a third type
3. All Normal-type attacks will hit as Dragon-type moves

## Competitive Analysis

### Advantages
- Transforms weak Normal moves into powerful Dragon attacks
- Provides excellent neutral coverage with Dragon-type
- Synergizes with high base power Normal moves (Return, Hyper Beam, etc.)
- Dragon STAB on a non-Dragon Pokemon can catch opponents off-guard

### Disadvantages
- Adds Dragon's weaknesses (Ice, Dragon, Fairy)
- Converted moves face Dragon immunities (Fairy-types)
- Steel-types resist Dragon moves
- Requires Normal-type moves in moveset to fully utilize

### Notable Interactions
- Multi-hit Normal moves (e.g., Tail Slap) become multi-hit Dragon moves
- Priority Normal moves (e.g., Fake Out, Quick Attack) become Dragon-type priority
- Works with sound-based Normal moves (e.g., Hyper Voice)
- Hidden Power (if Normal-type) converts to Dragon

## Comparison with Similar Abilities

- **Draconize**: Only converts moves, doesn't add Dragon typing
- **Half Drake**: Only adds Dragon type, doesn't convert moves
- **Aerilate/Pixilate/Refrigerate**: Similar -ate abilities for other types
- **Dragonfly**: Combines Half Drake with Levitate instead of move conversion

## Example Scenario

A Pokemon with Draconic Might uses Return:
- Return (Normal, 102 BP) to Dragon-type Return
- Gains STAB from added Dragon typing
- Final damage: 102 x 1.5 = 153 effective base power
- Hits as Dragon-type for type effectiveness

This ability essentially creates a pseudo-Dragon type that can utilize Normal-type movepool as Dragon STAB, offering unique offensive opportunities.
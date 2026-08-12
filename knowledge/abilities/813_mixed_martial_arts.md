---
id: 813
name: Mixed Martial Arts
status: reviewed
character_count: 130
---

# Mixed Martial Arts - Ability ID 813

## In-Game Description
"Normal moves are flagged as Punch + Kick moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Iron Fist and Striker moves, enabling them to benefit from related abilities and interactions.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Mixed Martial Arts modifies Normal-type moves by adding internal flags that categorize them as both punching and kicking moves. This allows Normal moves to interact with abilities and items that specifically boost punch or kick moves.

### Activation Conditions
- Triggers on any Normal-type move used by the Pokemon with this ability
- Works for both physical and special Normal-type moves
- Functions regardless of the move's actual animation or flavor text

### Technical Implementation
**Current Status**: The ability is currently implemented as a stub in the codebase with only `.breakable = TRUE` and no functional code.

**Expected Implementation**: Should modify the move flag checking system to treat Normal moves as having both `FLAG_IRON_FIST_BOOST` and potentially kick-move flags when used by a Pokemon with this ability.

```c
// Expected implementation pattern
constexpr Ability MixedMartialArts = {
    // Would need custom logic to modify move type checking
    // for Iron Fist, Strong Jaw, and similar abilities
    .breakable = TRUE,
};
```

### Affected Moves
All Normal-type moves would be considered both Punch and Kick moves, including:
- Tackle, Scratch, Quick Attack (basic attacks)
- Hyper Beam, Giga Impact (powerful moves)
- Return, Frustration (friendship-based moves)
- Extreme Speed, Fake Out (priority moves)
- And any other move with `TYPE_NORMAL`

### Interactions with Other Abilities
**Iron Fist**: Normal moves would gain the 1.3x damage multiplier
**Strong Jaw**: If kick moves are considered "jaw" moves, would gain 1.3x multiplier
**Reckless**: High-recoil Normal moves would gain additional boosting
**Sheer Force**: Normal moves with secondary effects would gain power boost

### Strategic Implications
- Transforms Normal-type attackers into versatile martial artists
- Provides significant damage boost to typically weak Normal moves
- Creates synergy with abilities that boost specific move types
- Makes Normal-type movesets more viable in competitive play

### Example Damage Calculations
**Quick Attack with Iron Fist boost**:
- Base: 40 BP x 1.5 (STAB) = 60 effective BP
- With Mixed Martial Arts: 40 BP x 1.5 (STAB) x 1.3 (Iron Fist) = 78 effective BP
- 30% damage increase over standard Quick Attack

**Hyper Beam combination**:
- Base: 150 BP x 1.5 (STAB) = 225 effective BP  
- With ability: 150 BP x 1.5 (STAB) x 1.3 (Iron Fist) = 292.5 effective BP
- Becomes one of the strongest moves in the game

### Common Users
*Note: This is a theoretical analysis since the ability is not fully implemented*

Would be most effective on:
- Normal-type Pokemon with high Attack stats
- Pokemon with access to diverse Normal-type movesets
- Mixed attackers who can utilize both physical and special Normal moves

### Competitive Usage Notes
- **Tier Impact**: Would significantly raise the viability of Normal-type attackers
- **Counters**: Steel and Rock types resist Normal moves regardless of boosting
- **Team Synergy**: Pairs well with Pokemon that can remove Steel/Rock types
- **Item Synergy**: Life Orb, Choice items would stack multiplicatively

### Counters
- **Steel-type Pokemon**: Immune to Normal-type moves entirely
- **Rock-type Pokemon**: Resist Normal moves, reducing effectiveness
- **Ghost-type Pokemon**: Immune to Normal-type physical moves
- **Intimidate**: Reduces physical Normal move damage
- **Burn**: Halves physical Normal move damage

### Synergies
- **Life Orb**: Stacks with ability boost for massive damage
- **Choice Band/Specs**: Further amplifies boosted Normal moves  
- **Adaptability**: Double STAB would stack with martial arts boost
- **Skill Link**: Makes multi-hit Normal moves incredibly powerful

### Version History
- **Elite Redux**: Introduced as Ability ID 813
- **Current Status**: Placeholder implementation without functional code
- **Future Updates**: Requires full implementation to be usable
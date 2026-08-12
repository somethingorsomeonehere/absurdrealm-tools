---
id: 216
name: Dancer
status: reviewed
character_count: 123
---

# Dancer - Ability ID 216

## In-Game Description
"Copies dance moves used by others."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When any Pokemon on the field uses a dance move, this Pokemon immediately uses the same move after. Triggers once per move.

## Detailed Mechanical Explanation
*For Discord/reference use*

Dancer is a unique ability that automatically triggers when any Pokemon (ally or opponent) uses a dance move on the battlefield.

### Core Mechanics
- **Automatic Activation**: When any battler uses a move with the FLAG_DANCE flag, Dancer triggers
- **Move Copying**: The Pokemon with Dancer immediately uses the same dance move that was just used
- **Out-of-Turn Usage**: The copied move is executed using UseOutOfTurnAttack, allowing it to occur immediately after the original move
- **No Power Modification**: The copied move uses its normal power and effects (movePower parameter is 0)

### Technical Implementation
```cpp
constexpr Ability Dancer = {
    .onCopyMove = +[](ON_COPY_MOVE) -> int {
        CHECK(IsDance(attacker, move))
        return UseOutOfTurnAttack(battler, target, ability, move, 0);
    },
};
```

The IsDance function checks:
1. If the move has FLAG_DANCE set in its flags
2. OR if the attacker has Taekkyeon ability and the move is not a status move

### Complete List of Dance Moves
1. **Swords Dance** - Raises Attack by 2 stages
2. **Petal Dance** - Physical Grass move that causes confusion after 2-3 turns
3. **Feather Dance** - Lowers target's Attack by 2 stages
4. **Teeter Dance** - Confuses all other Pokemon on the field
5. **Dragon Dance** - Raises Attack and Speed by 1 stage each
6. **Lunar Dance** - User faints, fully heals replacement Pokemon
7. **Quiver Dance** - Raises Special Attack, Special Defense, and Speed by 1 stage each
8. **Fiery Dance** - Special Fire move with 50% chance to raise Special Attack
9. **Revelation Dance** - Changes type to match user's primary type
10. **Aqua Step** - Water-type physical move

### Activation Conditions
- Any Pokemon on the field uses a dance move
- The Dancer Pokemon is still active and able to use moves
- The Dancer Pokemon hasn't already moved this turn (gTurnStructs check prevents infinite loops)

### Interactions with Other Abilities/Mechanics
- **Priority**: Dancer triggers immediately after the original move, before the turn continues
- **Multiple Dancers**: If multiple Pokemon have Dancer, they will all copy the move in turn order
- **Target Selection**: The copied move targets the same target as the original (or self for stat moves)
- **Taekkyeon Synergy**: Pokemon with Taekkyeon make all their non-status moves count as dance moves, creating synergy with Dancer teammates

### Strategic Implications
- **Team Support**: Excellent for copying beneficial stat-boosting dances from allies
- **Punishment**: Can backfire against opponents using setup moves like Dragon Dance or Quiver Dance
- **Double Battles**: Particularly powerful in doubles where ally setup moves can be copied
- **Prediction**: Opponents must be careful about using dance moves against Dancer users

### Example Scenarios
- Ally uses Dragon Dance to Dancer copies Dragon Dance to Both Pokemon get +1 Attack/Speed
- Opponent uses Quiver Dance to Dancer copies Quiver Dance to Dancer gets +1 SpA/SpD/Speed
- Teammate uses Swords Dance to Dancer copies Swords Dance to Dancer gets +2 Attack

### Common Users
In Elite Redux, Dancer is typically found on:
- Pokemon with naturally high offensive stats that benefit from setup moves
- Support Pokemon designed to capitalize on team synergy
- Pokemon with good speed to make use of copied priority moves

### Competitive Usage Notes
- **Team Building**: Build teams with beneficial dance moves to maximize Dancer's utility
- **Positioning**: In doubles, position Dancer users to benefit from ally setup moves
- **Mind Games**: Forces opponents to think twice about using setup moves

### Counters
- **Mold Breaker**: Bypasses Dancer entirely
- **Taunt**: Prevents the use of status dance moves
- **Priority Moves**: Can interrupt before Dancer gets to copy
- **Substitute**: Can block some dance move effects

### Synergies
- **Taekkyeon**: Makes the user's non-status moves count as dance moves for other Dancers
- **Setup Moves**: Any Pokemon with beneficial dance moves
- **Speed Control**: Pokemon that can ensure Dancer moves first after copying

### Version History
- Introduced in Generation VII as a standard ability
- In Elite Redux, maintains original functionality with no modifications
- Works with all dance moves including newer additions like Aqua Step
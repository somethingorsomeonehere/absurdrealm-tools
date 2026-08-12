---
id: 711
name: Lunar Affinity
status: reviewed
character_count: 145
---

# Lunar Affinity - Ability ID 711

## In-Game Description
"Copies lunar moves used by others."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Copies lunar moves when other Pokemon use them in battle. Includes Moonlight, Moonblast, Lunar Dance, and Lunar Blessing. Triggers once per move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Lunar Affinity is a reactive ability that automatically copies and executes lunar-typed moves when used by any Pokemon in battle. The ability activates through the `onCopyMove` trigger, checking if the move has the `lunar` property set to true.

### Activation Conditions
- **Move requirement**: The move must have `lunar: true` in its data
- **Timing**: Activates immediately after another Pokemon uses a lunar move
- **User independence**: Can copy moves from allies or opponents
- **No PP cost**: The copied move doesn't consume PP from the Lunar Affinity user

### Technical Implementation
```c
constexpr Ability LunarAffinity = {
    .onCopyMove = +[](ON_COPY_MOVE) -> int {
        CHECK(gBattleMoves[move].lunar)
        return UseOutOfTurnAttack(battler, target, ability, move, 0);
    },
};
```

### Lunar Moves in Elite Redux
The following moves trigger Lunar Affinity:
- **Moonlight**: Healing move that restores HP
- **Moonblast**: Fairy-type special attack with 20% chance to lower Special Attack
- **Lunar Dance**: Self-sacrifice move that fully heals the next Pokemon
- **Lunar Blessing**: Status move that provides beneficial effects

### Important Interactions
- **Out-of-turn execution**: Uses `UseOutOfTurnAttack` so it doesn't wait for turn order
- **Original stats**: The copied move uses the original user's offensive stats
- **Targeting**: Maintains the same target as the original move
- **No ability interaction**: The copy bypasses normal ability interactions
- **Status effects**: Copy isn't affected by the user's status conditions like paralysis

### Strategic Implications
- **Moonlight synergy**: Double healing when allies use Moonlight
- **Offensive copying**: Can copy powerful Moonblast attacks for extra damage
- **Support multiplication**: Copying Lunar Blessing multiplies support effects
- **Unpredictable timing**: Opponents can't predict when lunar moves will be copied

### Common Users
Based on the proto data, Lunar Affinity appears on:
- Pokemon in the "Lunar" category
- Certain Fairy-type and Psychic-type Pokemon
- Pokemon with celestial or moon-based themes

### Competitive Usage Notes
- **Double utility**: Turns opponent's lunar moves into advantages
- **Team support**: Amplifies ally lunar move effects
- **No resource cost**: Free move copying without PP expenditure
- **Timing advantage**: Out-of-turn activation can break prediction
- **Limited pool**: Only works with lunar-flagged moves

### Counters
- **Avoid lunar moves**: Don't use lunar moves against Lunar Affinity users
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable copying
- **Priority moves**: Fast moves can interrupt before copy triggers
- **Switching**: Remove the Lunar Affinity user from battle
- **Non-lunar alternatives**: Use non-lunar healing/support moves instead

### Synergies
- **Lunar move users**: Team with Pokemon that know lunar moves
- **Moonlight/Lunar Blessing**: Copy healing and support moves
- **Fairy-type teams**: Many Fairy-types learn Moonblast
- **Doubles/Triples**: More opportunities for lunar move copying
- **Weather teams**: Some lunar moves benefit from weather conditions

### Version History
- Custom ability in Elite Redux
- Part of the expanded lunar move system
- Unique reactive copying mechanic
- No equivalent in official Pokemon games

### Related Abilities
- **Lunar Eclipse**: Another lunar-themed ability in Elite Redux
- **Dancer**: Copies dance moves instead of lunar moves
- **Power of Alchemy**: Copies abilities instead of moves
- **Receiver**: Similar copying concept but for abilities
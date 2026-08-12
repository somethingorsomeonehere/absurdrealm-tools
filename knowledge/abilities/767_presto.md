---
id: 767
name: Presto
status: reviewed
character_count: 50
---

# Presto - Ability ID 767

## In-Game Description
"Sound moves get +1 priority at full HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to sound moves when at full HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Presto grants +1 priority to all sound-based moves when the user is at maximum HP. This ability functions through the `onPriority` callback, which checks two conditions:
1. **Full HP Check**: `BATTLER_MAX_HP(battler)` - The Pokemon must be at 100% HP
2. **Sound Move Check**: `IsSoundMove(battler, move)` - The move must have the sound flag

### Sound Move Classification
A move is considered a sound move if:
- It has the `FLAG_SOUND` flag in its move data, OR
- It's a Normal-type move and the user has the Reverbate ability (which converts Normal moves to sound moves)

Common sound moves include Growl, Roar, Sing, Supersonic, Screech, Snore, Uproar, Howl, Hyper Voice, Grasswhistle, and many others.

### Priority System
- Normal priority moves: 0
- Presto-boosted sound moves: +1 (when at full HP)
- This places them in the same priority bracket as moves like Quick Attack, Bullet Punch, etc.
- Higher priority moves (like Extreme Speed at +2) will still go first

### Strategic Applications
**Offensive Usage:**
- Hyper Voice becomes a priority special attack
- Sound-based status moves like Growl/Screech go first to set up
- Great for revenge killing or preventing setup

**Limitations:**
- Only works at full HP - any damage removes the priority boost
- Vulnerable to priority moves with higher priority than +1
- Limited to sound moves only, restricting move pool flexibility

### Synergies
- **Substitute**: Can protect HP to maintain full HP status
- **Leftovers/Recovery moves**: Help maintain the full HP requirement
- **Sound-based movesets**: Maximizes the ability's utility

### Known Users
- **Mega Primarina**: The primary user of this ability, fitting its musical theme as a sea lion performer

### Comparison to Similar Abilities
- **Prankster**: Gives +1 priority to status moves (broader category, no HP requirement)
- **Opportunist**: Gives +1 priority when targeting low HP opponents
- **Quick Feet**: Boosts speed under status conditions (different activation condition)

Presto represents a unique "perfect condition" ability that rewards maintaining full HP with enhanced musical combat prowess, perfectly thematic for performance-based Pokemon like Mega Primarina.
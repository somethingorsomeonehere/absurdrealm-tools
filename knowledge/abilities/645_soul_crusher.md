---
id: 645
name: Soul Crusher
status: reviewed
character_count: 83
---

# Soul Crusher - Ability ID 645

## In-Game Description
Hammer moves deal 10% more damage and use target's Special Defense.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Hammer moves gain a 10% damage boost and target Special Defense instead of Defense. 

## Detailed Mechanical Explanation

### Technical Implementation

The Soul Crusher ability affects hammer-based moves in two ways:

1. **Offensive Multiplier**: Applies a 1.1x damage multiplier to all hammer-based moves
2. **Defensive Stat Override**: Forces the target to use Special Defense instead of Defense when calculating damage from hammer-based moves

This creates a unique dynamic where physical hammer moves become more effective against physically defensive opponents, as they must rely on their typically weaker special defense stat.

### Affected Moves

Hammer-based moves include:
- Slam
- Crabhammer  
- Hammer Arm
- And other moves with the hammer flag

### Synergies

Soul Crusher works particularly well with:
- Pokemon with high Attack stats
- Movesets focused on hammer-based moves
- Strategies targeting physically bulky opponents

### Counterplay

- Use Pokemon with high Special Defense
- Avoid switching in physically defensive walls
- Utilize moves that don't rely on defensive stats (status moves, fixed damage)
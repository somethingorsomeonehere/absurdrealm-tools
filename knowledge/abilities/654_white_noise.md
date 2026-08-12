---
id: 654
name: White Noise
status: reviewed
character_count: 180
---

# White Noise - Ability ID 654

## In-Game Description
Static + Peaceful Rest.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user has a 30% chance to inflict paralysis on contact moves, both when attacking and being attacked. Restores 1/8 of the user's maximum HP at the end of each turn while in fog.

## Detailed Mechanical Explanation

### Implementation Details

White Noise is implemented as a composite ability that inherits:
- `onAttacker` and `onDefender` from Static ability
- `onEndTurn` from PeacefulRest ability

### Static Component
- Triggers when opponent makes contact with the user
- 30% chance to inflict paralysis on the attacker
- Only works with moves that make physical contact
- Bypassed by abilities that prevent status conditions

### Peaceful Rest Component  
- Activates during fog weather conditions
- Heals 1/8 of maximum HP at the end of each turn
- Requires the Pokemon to not be at full HP
- Must be able to heal (not blocked by Heal Block, etc.)
- Does not activate on the first turn after switching in
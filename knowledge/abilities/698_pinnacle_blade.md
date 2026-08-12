---
id: 698
name: Pinnacle Blade
status: reviewed
character_count: 123
---

# Pinnacle Blade - Ability ID 698

## In-Game Description
Slashing moves always hit and break protection and barriers.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All Keen Edge moves can never miss, and they bypass protection moves and ignore any secondary effects associated with them.

## Detailed Mechanical Explanation

### Mechanics
- **Accuracy Override**: Slashing moves never miss regardless of accuracy modifiers or evasion
- **Barrier Breaking**: Destroys Light Screen, Reflect, and Aurora Veil when using slashing moves  
- **Substitute Destruction**: Removes target's Substitute immediately upon hit
- **Protection Bypass**: Ignores Protect, Detect, and similar defensive moves
- **Move Requirement**: Only works with moves that have the FLAG_KEEN_EDGE_BOOST flag

### Code Implementation
The ability works through two main mechanisms:
1. **onInfiltrate**: Returns INFILTRATE_BREAK_SCREENS | INFILTRATE_SUBSTITUTE for slashing moves
2. **onAttacker**: Triggers after hit to remove barriers and protection effects
3. **IsBattlerProtected**: Returns FALSE for slashing moves, bypassing protection entirely
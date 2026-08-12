---
id: 567
name: Armor Tail
status: reviewed
character_count: 97
---

# Armor Tail - Ability ID 567

## In-Game Description
"Protects itself and ally from priority moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents the user and its ally from being targeted by priority moves with priority higher than 0.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Armor Tail provides complete immunity to priority moves for both the user and their ally in double battles. The ability specifically checks for moves with priority greater than 0 and blocks them from targeting protected Pokemon.

### Technical Implementation
```cpp
constexpr Ability ArmorTail = {
    .onImmune = QueenlyMajesty.onImmune,
    .onImmuneFor = APPLY_ON_ALLY,
    .breakable = TRUE,
};
```

The ability uses the same immunity logic as Queenly Majesty:
- Checks if the move has priority > 0
- Verifies attacker and target are on opposite sides
- Prevents the move from connecting and displays protection message

### Breakable Ability Mechanics
Since `breakable = TRUE`, Armor Tail can be bypassed by:
- Mold Breaker and variants (Teravolt, Turboblaze)
- Other abilities that ignore protective abilities
- The ability will still activate but won't prevent the priority move

### Priority Move Interactions
**Blocked Priority Moves:**
- +1 Priority: Quick Attack, Bullet Punch, Mach Punch
- +2 Priority: Extreme Speed, First Impression
- +3 Priority: Fake Out (first turn only)
- Custom priority moves with positive priority

**Not Affected:**
- Normal priority moves (0)
- Negative priority moves
- Status moves that don't target opponents directly

### Competitive Applications
**Defensive Utility:**
- Counters priority revenge killers like Talonflame and Lucario
- Protects frail setup sweepers from priority interruption
- Valuable in doubles for protecting both team members

**Strategic Team Building:**
- Pairs well with setup sweepers vulnerable to priority
- Effective on bulky support Pokemon in doubles
- Helps against priority-heavy metagames

**Counterplay:**
- Mold Breaker users can bypass the protection
- Non-priority moves remain fully effective
- Switching removes the protection for incoming Pokemon
---
id: 828
name: Overzealous
status: reviewed
character_count: 24
---

# Overzealous - Ability ID 828

## In-Game Description
User's super-effective moves have +1 prio.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Will not be implemented. 

## Detailed Mechanical Explanation

### Implementation Details
The ability is defined in `src/abilities.cc` as:
```cpp
constexpr Ability Overzealous = {
    .breakable = TRUE,
};
```

**Note**: The priority boost functionality appears to not be fully implemented yet. The ability should have an `onPriority` handler that checks if the move would be super-effective against the target and returns +1 priority bonus if true.

### Expected Implementation
The ability should work by:
1. Checking if the move would deal super-effective damage to the target
2. If super-effective (type effectiveness > 1.0x), add +1 to the move's priority
3. This check happens in the `GetMovePriority` function through the ability's `onPriority` handler

### Technical Notes
- Marked as `.breakable = TRUE`, meaning it can be suppressed by moves like Gastro Acid
- As an innate ability (N), it cannot be changed and is one of the Pokemon's three fixed innate abilities
- The priority boost should stack with the move's base priority (e.g., a super-effective Quick Attack would have +2 priority total)
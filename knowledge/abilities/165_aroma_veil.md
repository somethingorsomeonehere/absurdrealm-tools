---
id: 165
name: Aroma Veil
status: reviewed
character_count: 133
---

# Aroma Veil - Ability ID 165

## In-Game Description
"Protects team from infatuation, heal block, and disabling."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Protects the user and allies from infatuation, heal block effects, and disabling moves including Disable, Taunt, Encore, and Torment.

## Detailed Mechanical Explanation

### Core Implementation
- **File**: `src/abilities.cc` (lines 1831-1838)
- **Mechanism**: Uses `onStatusImmune` callback with `APPLY_ON_ALLY` flag
- **Breakable**: Yes (can be bypassed by Mold Breaker variants)

### Protection Scope
The ability protects against three categories of status effects:

1. **CHECK_INFATUATE** (bit 7): Protects from Attract
2. **CHECK_RESTRICTING** (bit 8): Protects from disabling moves:
   - Disable
   - Taunt  
   - Encore
   - Torment
3. **CHECK_HEAL_BLOCK** (bit 9): Protects from Heal Block and Psychic Noise

### Implementation Details
```cpp
constexpr Ability AromaVeil = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & (CHECK_INFATUATE | CHECK_RESTRICTING | CHECK_HEAL_BLOCK))
        return TRUE;
    },
    .onStatusImmuneFor = APPLY_ON_ALLY,
    .breakable = TRUE,
};
```

## Pokemon Distribution

### Notable Pokemon with Aroma Veil:
- **Cherrim** (ability choice)
- **Floette** (all forms, ability choice)
- **Florges** (all forms, ability choice)
- **Alcremie** (all forms, innate ability)
- **Aromatisse** variants (ability choice)
- Various Fairy-type and Grass-type Pokemon

### Usage Pattern
- Most commonly found on Fairy-type and Grass-type Pokemon
- Often appears as either a regular ability choice or innate ability
- Particularly prevalent in support-oriented Pokemon

## Competitive Analysis

### Strengths
- **Team Support**: Protects entire team from common status disruption
- **Anti-Control**: Counters popular control strategies (Taunt, Encore, Attract)
- **Heal Block Counter**: Prevents shutdown of recovery strategies
- **Doubles/Multi-Battle Utility**: Exceptional value in team formats

### Weaknesses  
- **Breakable**: Can be bypassed by Mold Breaker variants
- **Limited Scope**: Only protects against specific status categories
- **No Offensive Benefit**: Provides no damage or stat benefits
- **Situational**: Value depends heavily on opponent's team composition

### Strategic Applications
- **Support Teams**: Essential for stall and support-heavy strategies
- **Doubles Meta**: High value in doubles where control moves are common
- **Anti-Meta**: Counters teams relying heavily on status disruption
- **Recovery Protection**: Maintains team's healing capabilities

## Interactions and Edge Cases

### Ability Interactions
- **Mold Breaker variants**: Can ignore Aroma Veil protection
- **Magic Bounce**: May interact with reflected status moves
- **Substitutes**: Protection applies regardless of substitute presence

### Move Interactions
- **Attract**: Completely blocked for user and allies
- **Taunt/Encore/Disable/Torment**: All blocked for protected team
- **Heal Block/Psychic Noise**: Healing prevention is blocked
- **Sleep Talk**: Not affected (not a restricting status)

### Technical Notes
- Uses bitwise checking for multiple status categories
- Applied through battle system's ability status protection framework
- Protection is checked before move effect application
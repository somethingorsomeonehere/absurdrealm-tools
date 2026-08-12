---
id: 167
name: Cheek Pouch
status: reviewed
character_count: 10
---

# Cheek Pouch - Ability ID 167

## In-Game Description
"This ability has no effect."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

No effect.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Current Implementation Status
**IMPLEMENTED BUT DISABLED** - Cheek Pouch exists in the game code as an empty ability placeholder with no functionality.

**Code Implementation:**
```cpp
constexpr Ability CheekPouch = {
    .randomizerBanned = TRUE,
};
```

The ability is fully registered in the ability system and can be assigned to Pokemon, but it has been intentionally disabled and provides no actual effects.

### Official Pokemon Mechanics (What it SHOULD do)
In the official Pokemon games, Cheek Pouch:
- Restores 33% of maximum HP when consuming a Berry
- Triggers after the Berry's primary effect
- Works with stolen Berries (Bug Bite, Pluck)
- Blocked by Heal Block status condition
- Does not activate at full HP

### Technical Implementation Details
- **File Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Ability ID**: 167 (ABILITY_CHEEK_POUCH)
- **Current Status**: Placeholder implementation only
- **Randomizer**: Banned from random assignment (`randomizerBanned = TRUE`)

### Why It's Disabled
The ability appears to be intentionally disabled, possibly due to:
1. **Balance concerns** with Berry-based strategies
2. **Implementation complexity** with berry consumption timing
3. **Design decisions** to avoid certain playstyles

### Pokemon Distribution
Currently no Pokemon in Elite Redux have this ability assigned, which aligns with its disabled status.

### Activation Conditions (If Implemented)
Would trigger when:
- Pokemon consumes a held Berry (Sitrus, Oran, type-resist berries, etc.)
- Berry is consumed via Bug Bite or Pluck moves
- HP is not already at maximum
- Not blocked by Heal Block status

Would NOT trigger when:
- Using Berry via Fling move
- Using Berry via Natural Gift move  
- Consuming Berry directly from Bag outside battle

### Strategic Implications (If Active)
- **Defensive utility**: Extends survivability with Berry-based healing
- **Berry synergy**: Makes consumption Berries significantly more valuable
- **Heal Block counter**: Provides alternative healing that bypasses typical restrictions
- **Setup potential**: Allows for more aggressive plays knowing healing is available

### Counters and Interactions
- **Heal Block**: Would prevent the healing portion
- **Magic Guard**: Would still allow healing (not damage-based)
- **Ripen**: Could potentially stack for enhanced Berry effects + healing
- **Harvest**: Natural synergy for repeated Berry consumption

### Notes
This ability represents an interesting case where the developers have chosen to implement but disable an ability, rather than leaving it completely unimplemented. This suggests it may be enabled in future updates if balance concerns are addressed.
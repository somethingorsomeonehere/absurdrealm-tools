---
id: 392
name: Arctic Fur
status: reviewed
character_count: 103
---

# Arctic Fur - Ability ID 392

## In-Game Description
"Weakens incoming physical and special moves by 35%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces both physical and special damage by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

### Overview
Arctic Fur is a powerful universal defensive ability that reduces damage from all incoming attacks by 35%. Unlike abilities that only protect against physical or special moves, Arctic Fur provides comprehensive protection against both attack types, making it one of the most valuable defensive abilities in Elite Redux.

## Current Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 4047-4050
- **Function**: `ArcticFur`
- **Breakable**: Yes (can be suppressed by Mold Breaker-type abilities)

### Mechanics
```cpp
constexpr Ability ArcticFur = {
    .onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) { MUL(.65); },
    .breakable = TRUE,
};
```

**Technical Details:**
- Applies a 0.65 multiplier to all incoming damage (35% reduction)
- Affects both physical and special moves
- Does not affect status moves or indirect damage (weather, entry hazards, etc.)
- Can be suppressed by abilities like Mold Breaker, Turboblaze, Teravolt
- Triggers on every damage-dealing move regardless of type or category


## Battle AI Rating
**Rating**: 9/10 - Considered an exceptionally strong defensive ability by the battle AI due to its universal damage reduction.

## Strategic Analysis

### Competitive Applications
- **Tier Rating**: High - One of the premier defensive abilities in the game
- **Usage**: Essential for bulky defensive Pokemon and tanks
- **Synergy**: Excellent with high HP stats and recovery moves

### Strengths
- Universal damage reduction affects all attack types
- Significant 35% damage reduction provides substantial bulk
- Turns many 2HKOs into 3HKOs or 4HKOs
- Excellent for Pokemon with balanced defensive stats
- Works against all damage sources (physical, special, contact, non-contact)

### Weaknesses
- Breakable by Mold Breaker-type abilities
- Does not affect indirect damage (weather, spikes, burn, poison)
- No protection against status moves or stat drops
- Can be suppressed by Gastro Acid or similar effects

### Optimal Pokemon Types
- **Ice-types**: Thematically appropriate and benefit from the defensive boost
- **Normal-types**: Often have balanced stats that benefit from universal protection
- **Defensive tanks**: Pokemon with high HP and moderate defensive stats
- **Utility Pokemon**: Support Pokemon that need to survive to use their moves

## Related Abilities

### Similar Defensive Abilities
- **Fur Coat**: Only reduces physical damage by 50%
- **Ice Scales**: Only reduces special damage by 50%  
- **Filter/Solid Rock**: Only reduces super-effective damage by 25%
- **Thick Fat**: Only reduces Fire/Ice damage by 50%

### Comparison Analysis
Arctic Fur stands out as the only ability that provides universal damage reduction to both physical and special moves. While other abilities offer higher reduction percentages, they are limited to specific damage types. Arctic Fur's 35% reduction across all damage types makes it more versatile and reliable.

## Lore/Thematic Connection
Arctic Fur represents the dense, insulating fur of arctic mammals like polar bears, arctic foxes, and similar cold-climate animals. The thick fur provides natural protection against both physical impacts and harsh environmental conditions, translating to universal damage reduction in battle. The ability name and effect capture the protective qualities of adaptation to extreme cold environments.

## Usage Notes
- Most effective on Pokemon with high HP and balanced defensive stats
- Pairs excellently with recovery moves (Recover, Roost, etc.)
- Consider Pokemon with this ability for defensive cores and stall teams
- Can be role-played or skill-swapped to other Pokemon
- Suppressed by Neutralizing Gas while that Pokemon is on the field

## Competitive Viability
Arctic Fur is considered one of the top-tier defensive abilities in Elite Redux due to its universal application and significant damage reduction. Its 35% reduction is substantial enough to meaningfully impact battle outcomes while not being so powerful as to completely invalidate offensive strategies. The breakable nature ensures counterplay options exist while maintaining the ability's defensive value.
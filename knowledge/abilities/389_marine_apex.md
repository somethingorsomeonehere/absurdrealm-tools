---
id: 389
name: Marine Apex
status: reviewed
character_count: 117
---

# Marine Apex - Ability ID 389

## In-Game Description
"Deals 1.5x damage to Water-types and bypasses screens."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deal 1.5x damage to Water-type Pokemon and bypass defensive screens (Light Screen, Reflect, Aurora Veil)/Substitutes.

## Detailed Mechanical Explanation

### Overview
Marine Apex is a powerful offensive ability that combines type-specific damage enhancement with screen-bypassing capabilities. It represents the concept of an apex predator that dominates aquatic environments while possessing the cunning to bypass defensive barriers.

## Technical Implementation

### Source Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Definition**: Lines 4020-4026
- **Registration**: Line 9233

### Code Implementation
```cpp
constexpr Ability MarineApex = {
    .onInfiltrate = Infiltrator.onInfiltrate,
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(target, TYPE_WATER)) RESISTANCE(1.5);
        },
};
```

### Infiltrator Reference
```cpp
constexpr Ability Infiltrator = {
    .onInfiltrate = +[](ON_INFILTRATE) -> InfiltrateType { 
        return INFILTRATE_SCREENS | INFILTRATE_SUBSTITUTE; 
    },
};
```

## Mechanics

### Primary Effect: Anti-Water Damage Boost
- **Multiplier**: 1.5x damage against Water-type Pokemon
- **Implementation**: Uses the `RESISTANCE` macro which applies both resistance and damage modifiers
- **Trigger**: When attacking any Pokemon with Water typing (primary or secondary)

### Secondary Effect: Infiltrator Properties
- **Screen Bypass**: Ignores Light Screen, Reflect, and Aurora Veil
- **Substitute Bypass**: Attacks go through Substitute
- **Implementation**: Inherits the complete `onInfiltrate` function from Infiltrator

## Strategic Analysis

### Competitive Viability: Medium Tier
- **Strengths**: 
  - Strong counter to Water-type threats
  - Screen bypass provides utility against defensive teams
  - Combines offensive and utility aspects
- **Weaknesses**:
  - Situational damage boost (only vs Water-types)
  - No defensive benefits
  - Limited impact against non-Water teams

### Optimal Usage Scenarios
1. **Water-Heavy Metagames**: Excels when Water-types are prevalent
2. **Screen Teams**: Provides consistent damage output against defensive setups
3. **Mixed Attackers**: Benefits Pokemon that can capitalize on both physical and special attacks

## Pokemon Distribution

### Current Users
1. **Mega Relicanth**: Water/Rock type
   - Base Stats: 100/160/130/45/75/95
   - Other Abilities: Marine Apex (all slots)
   - Innate Abilities: Impenetrable, Reckless, Primal Armor

2. **Gardevoir Redux Mega**: Water/Dark type
   - Base Stats: 75/150/93/100/85/130
   - Ability Options: Swift Swim, Marine Apex, Ambush
   - Innate Abilities: Phantom, Impaler, Tag

## Related Abilities

### Similar Damage Boosting Abilities
- **Aquatic Dweller**: Boosts Water-type moves by 1.5x (enhances own type vs Marine Apex countering type)
- **Exploit Weakness**: Various type-specific damage boosts
- **Dragonslayer**: Anti-Dragon damage boost (similar concept, different type)

### Infiltrator Family
- **Infiltrator**: Base ability providing screen/substitute bypass
- **Spectral Shroud**: Combines Infiltrator with other effects
- **Phantom**: Related bypassing abilities

## Synergies and Counters

### Team Synergies
- **Physical Attackers**: Maximizes the 1.5x damage boost
- **Mixed Attackers**: Benefits from both damage boost and screen bypass
- **Anti-Stall Teams**: Screen bypass helps against defensive cores

### Counters
- **Non-Water Teams**: Reduces the ability's primary effectiveness
- **Priority Moves**: Can bypass the need for screen removal
- **Status Moves**: Ability doesn't affect non-damaging moves

## Competitive Applications

### Metagame Impact
- **Water-Type Check**: Provides reliable counter to Water-type threats
- **Screen Breaker**: Maintains offensive pressure against defensive teams
- **Role Compression**: Combines offensive and utility roles

### Recommended Movesets
- **Physical Focus**: High-power physical moves to maximize damage boost
- **Coverage Moves**: Ensures effectiveness beyond Water-type matchups
- **Status Moves**: Leverages screen bypass for support moves


## Conclusion

Marine Apex represents a well-designed ability that combines thematic coherence with practical utility. Its dual functionality makes it valuable in diverse team compositions, particularly in metagames where Water-types and defensive screens are common. While not overwhelmingly powerful, it provides consistent value and interesting strategic options for team builders.

The ability's design successfully captures the concept of an apex predator that dominates its preferred environment (aquatic) while possessing the cunning to bypass defensive measures, making it both flavorful and competitively relevant.
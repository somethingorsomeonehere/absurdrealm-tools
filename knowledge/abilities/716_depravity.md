---
id: 716
name: Depravity
status: reviewed
character_count: 271
---

# Depravity - Ability ID 716

## In-Game Description
"Merciless + Overcharge."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees critical hits against targets who are poisoned, paralyzed, bleeding, or have their speed lowered. The user's Electric-type moves become effective against Electric-type Pokemon, dealing 2x damage instead of 0.5x. Also allows the user to paralyze Electric-types.


## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Depravity is a powerful combination ability that merges two distinct offensive mechanics:

**Merciless Component:**
- Guarantees critical hits against targets with specific conditions
- Affected targets: poisoned, paralyzed, bleeding, speed-lowered, or holding Iron Ball
- 100% critical hit rate when conditions are met
- Standard 1.5x critical hit damage multiplier

**Overcharge Component:**
- Makes Electric-type moves super effective (2x damage) against Electric-type Pokemon
- Allows Electric-type Pokemon to be paralyzed (bypasses natural immunity)
- Overrides default Electric vs Electric resistance (0.5x to 2x)

### Technical Implementation
```cpp
constexpr Ability Depravity = {
    .onCrit = Merciless.onCrit,
    .onTypeEffectiveness = Overcharge.onTypeEffectiveness,
    .onCanStatusType = Overcharge.onCanStatusType,
};
```

The implementation directly inherits:
- **onCrit**: Merciless's critical hit logic
- **onTypeEffectiveness**: Overcharge's type effectiveness modification
- **onCanStatusType**: Overcharge's status immunity bypass

### Activation Conditions

**Merciless Triggers:**
1. Target has poison status (regular or badly poisoned)
2. Target is paralyzed
3. Target has bleeding status (Elite Redux exclusive)
4. Target's Speed stat stages are below 0 (any reduction)
5. Target holds Iron Ball item

**Overcharge Triggers:**
1. Using Electric-type moves against Electric-type Pokemon (super effective damage)
2. Attempting to paralyze Electric-type Pokemon (bypasses immunity)

### Numerical Values
- **Critical Hit Chance**: 100% when Merciless conditions are met
- **Critical Hit Damage**: 1.5x (standard critical multiplier)
- **Electric vs Electric Damage**: 2.0x (super effective instead of 0.5x not very effective)
- **Status Success**: Paralysis can affect Electric-types

### Strategic Synergies
**Devastating Combination:**
1. Use Thunder Wave to paralyze Electric-type opponents
2. Electric-type moves deal super effective damage to paralyzed Electric-types
3. Paralyzed status guarantees critical hits via Merciless
4. Result: 2x (super effective) x 1.5x (critical) = 3x total damage multiplier

**Self-Synergy Loop:**
- Paralysis enables guaranteed crits
- Electric moves can paralyze Electric-types
- Electric moves deal super effective damage to Electric-types
- Creates a self-reinforcing offensive loop

### Affected Moves
**All offensive moves** benefit from the critical hit component when conditions are met
**Electric-type moves** specifically benefit from both components:
- Thunder Wave: Can paralyze Electric-types
- Thunderbolt/Thunder: Deal super effective damage + guaranteed crits to paralyzed Electric-types
- Discharge: AoE paralysis and damage against Electric-types

### Interactions with Other Abilities/Items

**Enhanced by:**
- **Sniper**: Increases crit damage to 2.25x when Merciless triggers
- **Thunder Wave/Static**: Provides paralysis setup for guaranteed crits
- **Scope Lens**: Redundant for Merciless conditions but helps with other targets

**Countered by:**
- **Battle Armor/Shell Armor**: Prevents critical hits entirely
- **Lightning Rod/Volt Absorb**: Still redirect/absorb Electric moves
- **Limber**: Prevents paralysis (reduces Merciless triggers)
- **Natural Cure/Aromatherapy**: Removes status conditions

### Competitive Analysis

**Strengths:**
- **Dual offensive mechanics**: Benefits from both type advantage and critical hits
- **Self-synergy**: Components work together for maximum damage
- **Meta disruption**: Changes Electric vs Electric matchups completely
- **Versatile application**: Effective against both Electric and non-Electric targets

**Weaknesses:**
- **Self-vulnerability**: User becomes weak to Electric attacks
- **Condition dependency**: Merciless requires specific status conditions
- **Predictable**: Once revealed, opponents can play around the mechanics

### Usage Scenarios

**Primary Strategy:**
1. Lead with Thunder Wave against Electric-types
2. Follow up with Electric-type attacking moves
3. Achieve 3x damage from super effective + critical combination

**Secondary Strategy:**
1. Use against non-Electric poisoned/paralyzed targets for guaranteed crits
2. Exploit speed control teams with guaranteed crits on debuffed foes

### Example Damage Calculation
**Scenario**: Depravity user with Electric move vs paralyzed Electric-type
- Base damage: 100%
- Super effective (Overcharge): x2.0 = 200%
- Critical hit (Merciless): x1.5 = 300% total
- **Result**: Triple damage compared to normal effectiveness

### Common Users
Depravity is typically found on:
- Electric-type Pokemon with access to status moves
- Mixed attackers who can exploit both components
- Pokemon in high-tier trainer battles requiring maximum offensive pressure

### Team Building Considerations
- **Status support**: Teammates with Thunder Wave, Toxic Spikes
- **Speed control**: Sticky Web, paralysis support
- **Electric immunity**: Ground-types to handle opposing Electric attacks
- **Clerical support**: Heal Bell users to cure user's own status if needed

### Combination Ability Comparisons

**vs Merciless alone**: Adds type effectiveness manipulation and status bypass
**vs Overcharge alone**: Adds guaranteed critical hits against debuffed targets
**vs other combination abilities**: Among the most offensively oriented combinations

### Version History
- **Elite Redux**: Custom combination ability
- **Implementation**: Direct inheritance from component abilities
- **Balance**: High risk/high reward offensive ability

### Code References
- **Ability Definition**: `src/abilities.cc` - Depravity implementation
- **Component Abilities**: Merciless (ID 196), Overcharge (ID 349)
- **Ability Constant**: `ABILITY_DEPRAVITY = 716`
- **Proto Description**: `proto/AbilityList.textproto`
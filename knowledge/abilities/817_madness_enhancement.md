---
id: 817
name: Madness Enhancement (N)
status: reviewed
character_count: 135
---

# Madness Enhancement (N) - Ability ID 817

## In-Game Description
"Confuses self in fog, halves damage when confused."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Forces self-confusion when entering fog. All incoming damage is reduced by 50% when the user is confused and it will never hurt itself.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Madness Enhancement is an innate ability (indicated by the "(N)" suffix) that creates a risk-reward dynamic with confusion status and fog weather conditions.

### Primary Effects

#### 1. Fog-Induced Confusion
- **Trigger**: When the Pokemon with Madness Enhancement enters fog weather or when fog weather is set while the Pokemon is active
- **Effect**: The Pokemon automatically becomes confused
- **Duration**: Standard confusion duration (1-4 turns, randomly determined)
- **Cannot be prevented**: This self-inflicted confusion bypasses confusion immunity from other sources

#### 2. Confusion Damage Reduction
- **Trigger**: While the Pokemon is confused (from any source, not just fog)
- **Effect**: All incoming damage is reduced by 50%
- **Damage Types Affected**: 
  - Direct move damage
  - Physical and special attacks
  - Multi-hit moves (each hit reduced individually)
- **Damage Types NOT Affected**:
  - Self-inflicted confusion damage
  - Weather damage (sandstorm, hail)
  - Status condition damage (poison, burn, etc.)
  - Entry hazard damage
  - Recoil damage

### Technical Implementation
```c
// In abilities.cc
constexpr Ability MadnessEnhancement = {
    .breakable = TRUE,
};
```

The ability is marked as breakable, meaning it can be suppressed by abilities like Mold Breaker, Teravolt, or Turboblaze.

The actual fog confusion trigger and damage reduction mechanics are implemented in the battle engine's confusion and damage calculation systems.

### Fog Weather Interaction
- **WEATHER_FOG_ANY**: Includes all forms of fog weather
- **Entry Timing**: Confusion is applied when switching in during active fog or when fog is set up
- **Fog Mechanics**: Elite Redux fog weather reduces accuracy and has various type-specific interactions

### Activation Conditions
1. **Fog Confusion**: Automatically triggers when fog weather is present
2. **Damage Reduction**: Active whenever confusion status is present, regardless of source

### Strategic Implications

#### Advantages
- **Defensive Powerhouse**: 50% damage reduction makes the Pokemon extremely tanky while confused
- **Synergy Potential**: Works with other confusion-inducing moves or abilities
- **Weather Control**: Can be strategically used with fog-setting moves or abilities
- **Innate Nature**: Cannot be skill swapped, role played, or otherwise transferred

#### Disadvantages
- **Loss of Control**: Confusion severely limits move reliability (33% chance to attack normally in most generations)
- **Self-Damage Risk**: Confusion can cause self-inflicted damage
- **Weather Dependency**: Requires fog setup for consistent activation
- **Breakable**: Can be suppressed by mold breaker effects

### Damage Calculations
**Example**: A 100 base power move that would normally deal 200 damage:
- **Without Madness Enhancement**: 200 damage
- **With Madness Enhancement (confused)**: 100 damage (50% reduction)
- **With Madness Enhancement + other defensive modifiers**: Stacks multiplicatively

### Interactions with Other Mechanics

#### Confusion Sources
- Fog weather (automatic)
- Confuse Ray, Swagger, etc. (manual)
- Thrash/Petal Dance recoil confusion
- Chesto Berry/Heal Bell can remove the beneficial confusion

#### Ability Interactions
- **Mold Breaker family**: Suppresses both fog confusion and damage reduction
- **Own Tempo**: Prevents confusion entirely, negating the ability
- **Magic Guard**: Protects from confusion self-damage but not the 50% damage reduction benefit

#### Item Interactions
- **Chesto Berry**: Cures confusion, removing damage reduction
- **Persim Berry**: Same effect as Chesto Berry
- **Mental Herb**: Cures confusion if it was caused by certain moves

### Common Users
This is an innate ability, so it cannot be obtained through normal means like Skill Swap or Role Play. It is permanently assigned to specific Pokemon species.

### Competitive Usage Notes
- **Setup Sweeper Counter**: Extremely effective against physical and special attackers
- **Fog Team Core**: Essential component of fog-based weather teams
- **Stall Tactics**: Can be used to wall opposing sweepers while confused
- **Risk Management**: Requires careful timing to maximize benefits while minimizing confusion drawbacks

### Counters
- **Mold Breaker**: Completely negates the ability
- **Status Moves**: Confusion doesn't protect against status conditions
- **Taunt**: Prevents recovery moves while confused
- **Critical Hits**: Still deal increased damage even with 50% reduction

### Synergies
- **Fog Weather Setters**: Abilities like [Fog-setting abilities if any exist]
- **Confusion Recovery**: Heal Bell, Aromatherapy users
- **Defensive Support**: Light Screen, Reflect for additional damage reduction
- **Recovery Moves**: Rest, Recover to maintain HP while tanking

### Version History
- Added in Elite Redux as an innate ability
- Part of the expanded 4-ability system unique to Elite Redux
- (N) designation indicates innate/natural ability status

### Notes
- The ability description states "Confuses self in fog, halves damage when confused"
- This is one of the few abilities that intentionally inflicts a negative status for a defensive benefit
- The 50% damage reduction makes it one of the most potent defensive abilities when active
- Cannot be traced, skill swapped, or otherwise transferred due to innate nature
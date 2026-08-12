---
id: 741
name: Breakwater
status: reviewed
character_count: 129
---

# Breakwater - Ability ID 741

## In-Game Description
"Swift Swim + Stall."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Speed by 50% during rain. Reduces damage by 30% when moving before the opponent. Works when the user switches in mid-turn. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Breakwater is a combination ability that merges Swift Swim and Stall effects, providing both offensive speed boost and defensive damage reduction under specific conditions.

### Component Abilities

#### Swift Swim Component
- **Speed boost**: 1.5x Speed multiplier during rain weather
- **Weather requirement**: Any form of rain must be active
  - Regular rain (from Rain Dance or Drizzle)
  - Heavy rain (from Drizzle ability)
  - Primordial Sea (extremely heavy rain)
- **Immediate activation**: Speed boost applies as soon as rain is active

#### Stall Component  
- **Damage reduction**: 0.7x defensive multiplier (30% damage reduction)
- **Activation condition**: Only when the opponent moves after this Pokemon
- **Turn order dependency**: Based on gCurrentTurnActionNumber vs GetBattlerTurnOrderNum
- **Breakable**: Can be bypassed by Mold Breaker family abilities

### Technical Implementation
```c
constexpr Ability Breakwater = {
    .onDefensiveMultiplier = Stall.onDefensiveMultiplier,
    .onStat = SwiftSwim.onStat,
    .breakable = TRUE,
};
```

### Activation Conditions
1. **Swift Swim effect**: Active whenever rain weather is present
2. **Stall effect**: Active when this Pokemon moves before the opponent in turn order
3. **Both effects**: Can be active simultaneously for maximum benefit

### Strategic Applications

#### Rain Team Synergy
- **Speed control**: Outspeeds threats in rain weather
- **Bulk preservation**: Takes reduced damage when moving first
- **Weather dependency**: Requires rain setup for speed benefit
- **Turn order manipulation**: Benefits from priority moves or speed investment

#### Optimal Usage Scenarios
- **Defensive sweeper**: Set up moves while taking reduced damage
- **Rain dance teams**: Core member of rain-based strategies  
- **Speed tier manipulation**: Outspeed key threats in rain
- **Bulk enhancement**: Survive attacks that would otherwise KO

### Important Interactions

#### Weather Effects
- **Rain duration**: In Elite Redux, weather lasts 8 turns (extended from 5)
- **Weather override**: Speed boost lost if rain is replaced
- **Cloud Nine/Air Lock**: Negates weather-based speed boost
- **Multiple weather**: Only rain provides the speed benefit

#### Turn Order Mechanics
- **Priority moves**: Stall effect works with priority moves
- **Speed ties**: Turn order determines Stall activation
- **Choice items**: Speed boost helps with choice item effectiveness
- **Trick Room**: Stall becomes less reliable in reversed speed conditions

### Competitive Advantages
- **Dual utility**: Provides both offense and defense
- **Rain synergy**: Excellent fit for rain teams
- **Versatile positioning**: Works as both setup sweeper and tank
- **Unpredictable**: Opponents must account for both effects

### Potential Drawbacks  
- **Weather dependency**: Speed boost requires rain
- **Turn order requirement**: Stall effect situational
- **Breakable ability**: Mold Breaker bypasses Stall component
- **Complex positioning**: Requires careful turn order management

### Counters and Limitations
- **Weather override**: Harsh sun, sandstorm, or hail negates speed boost
- **Mold Breaker family**: Teravolt, Turboblaze bypass Stall effect
- **Faster priority**: High priority moves can bypass both effects
- **Multi-hit moves**: Can overwhelm even with damage reduction

### Synergistic Partners
- **Drizzle setters**: Politoed, Pelipper for automatic rain
- **Rain Dance users**: Manual weather setters as backup
- **Thunder users**: Perfect accuracy Thunder in rain
- **Water-type moves**: Boosted damage in rain weather

### Usage Tips
- **Lead with rain setter**: Ensure rain is active for speed boost
- **Priority move coverage**: Use priority to guarantee Stall activation
- **Speed investment**: Even with Swift Swim, some investment helps
- **Weather extension**: Damp Rock extends beneficial weather
- **Turn order awareness**: Monitor speed stats and turn order

### Version History
- Introduced in Elite Redux as combination ability
- ID 741 in the ability roster
- Combines two classic competitive abilities
- Part of the multi-ability system implementation
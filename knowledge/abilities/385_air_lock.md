---
id: 385
name: Air Lock
status: reviewed
character_count: 225
---

# Air Lock - Ability ID 385


## In-Game Description
"Clears weather and prevents its effects."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Clears weather on switch-in. While active, blocks all weather effects: no damage modifiers, no chip damage, no accuracy changes, prevents Aurora Veil, etc. Weather can be set but provides no benefits. Works on primal weather.

## Detailed Mechanical Explanation

### Basic Information
**Effect**: Clears weather and prevents its effects  
**Type**: Weather Control  
**Introduced**: Generation III  
**Elite Redux Tier**: A-

### Technical Implementation

### Core Mechanics
Air Lock operates through two distinct systems:

1. **Entry Effect**: Upon switching in, triggers `BattleScript_AnnounceAirLockCloudNine`
2. **Passive Suppression**: Blocks weather effects via the `WEATHER_HAS_EFFECT` macro

```c
constexpr Ability AirLock = {
    .onEntry = CloudNine.onEntry,
};
```

### Weather Suppression Code
```c
#define WEATHER_HAS_EFFECT \
    (!gFieldTimers.clearSkiesTimer && !IsAbilityOnField(ABILITY_CLOUD_NINE) && !IsAbilityOnField(ABILITY_AIR_LOCK) && !IsAbilityOnField(ABILITY_CLUELESS))
```

Air Lock prevents weather effects by making the `WEATHER_HAS_EFFECT` macro return false whenever a Pokemon with this ability is on the field.

## Complete Weather Interactions

### Blocked Effects
- **Sun (Harsh Sunlight)**:
  - Fire moves don't get 1.5x damage boost
  - Water moves don't get 0.5x damage reduction  
  - Solar Beam still requires 2 turns to charge
  - Chlorophyll doesn't double Speed
  - Solar Power doesn't activate
  - Morning Sun heals 50% HP instead of 67%

- **Rain (Heavy Rain)**:
  - Water moves don't get 1.5x damage boost
  - Fire moves don't get 0.5x damage reduction
  - Thunder/Hurricane don't get perfect accuracy
  - Swift Swim doesn't double Speed
  - Rain Dish doesn't restore HP
  - Dry Skin doesn't restore HP

- **Sandstorm**:
  - No chip damage to non-Rock/Ground/Steel types
  - Rock-types don't get 1.5x Special Defense
  - Sand Rush doesn't double Speed
  - Sand Veil doesn't boost evasion
  - Weather Ball remains Normal-type

- **Hail**:
  - No chip damage to non-Ice types
  - Blizzard doesn't get perfect accuracy
  - Snow Cloak doesn't boost evasion
  - Ice Body doesn't restore HP

- **Primal Weather**:
  - Desolate Land: Fire moves not un-weakened, Water moves can still be used
  - Primordial Sea: Water moves not super-boosted, Fire moves can still be used
  - Delta Stream: Flying-types lose weather immunity, super-effective moves deal normal damage

### Move Interactions
- **Weather Ball**: Remains Normal-type with 50 base power
- **Solar Beam/Solar Blade**: Still require 2-turn charge regardless of weather
- **Thunder/Hurricane**: 70% accuracy in all conditions
- **Blizzard**: 70% accuracy regardless of hail
- **Growth**: Only +1 Attack/Special Attack boost
- **Moonlight/Morning Sun/Synthesis**: Always heal 50% HP

## Strategic Analysis

### Offensive Applications
- **Anti-Weather Tech**: Hard counter to weather-based offense
- **Damage Consistency**: Enables reliable damage calculations
- **Speed Control**: Neutralizes weather-based speed boosts
- **Type Coverage**: Allows Fire moves in rain, Water moves in sun

### Defensive Applications  
- **Chip Damage Immunity**: Protects team from Sandstorm/Hail damage
- **Weather Stall**: Prevents weather-based healing and boosting
- **Entry Hazard Support**: Forces weather teams to constantly reset
- **Longevity**: Enables Pokemon weak to weather conditions

### Team Synergy
- **Stealth Rock**: Capitalizes on forced switches from weather teams
- **Mixed Attackers**: Benefit from consistent damage calculations  
- **Balanced Teams**: Provides neutral field conditions
- **Anti-Meta**: Counters weather-heavy metagames

## Competitive Viability: A-

### Strengths
- **Meta Relevance**: Strong against weather-dominated formats
- **Immediate Impact**: Entry effect immediately disrupts opponent strategy
- **Passive Value**: Continues providing utility while active
- **Universal Coverage**: Works against all weather types
- **Primal Counter**: One of few abilities that can clear primal weather

### Limitations  
- **Switch Dependency**: Effect ends when user switches out
- **Weather Reset**: Opponents can immediately set weather again
- **Non-Weather Matchups**: Provides no value against non-weather teams
- **Momentum Risk**: May require switching into unfavorable positions

### Common Counterplay
- **Direct Pressure**: Force Air Lock user out with strong attacks
- **Pivot Moves**: U-turn/Volt Switch to reset weather
- **Non-Weather Offense**: Use abilities that don't rely on weather
- **Speed Control**: Outspeed and eliminate before weather matters

## Notable Users

### Rayquaza
**Ability Setup**: Air Lock (Innate 1) + Weather Control (Innate 2) + Aerodynamics (Innate 3)
- **Role**: Premier weather control legendary
- **Synergy**: Multiple weather-related abilities for complete field control
- **Usage**: Anti-weather pivot and special attacking threat

## Related Abilities

### Cloud Nine (ID: 13)
- **Function**: Identical to Air Lock
- **Difference**: Flavor only - mechanically equivalent
- **Usage**: More commonly distributed ability

### Clueless (ID: 426)  
- **Function**: Blocks weather, terrain, AND room effects
- **Advantage**: More comprehensive field control
- **Trade-off**: Rarer distribution, may be overpowered

### Weather Control (ID: 354)
- **Function**: Extends weather duration and provides weather immunity
- **Synergy**: Often paired with Air Lock for complete weather mastery
- **Usage**: Enables selective weather control strategies

## Damage Calculations

### Rain Example
**Without Air Lock**:
- Surf (90 BP) in Rain to 135 effective BP (1.5x)
- Flamethrower (90 BP) in Rain to 45 effective BP (0.5x)

**With Air Lock**:
- Surf (90 BP) to 90 BP (no modifier)
- Flamethrower (90 BP) to 90 BP (no modifier)

### Sun Example  
**Without Air Lock**:
- Fire Blast (110 BP) in Sun to 165 effective BP (1.5x)
- Hydro Pump (110 BP) in Sun to 55 effective BP (0.5x)

**With Air Lock**:
- Fire Blast (110 BP) to 110 BP (no modifier)  
- Hydro Pump (110 BP) to 110 BP (no modifier)

## Advanced Interactions

### Priority Weather Setting
- Weather moves used on the same turn Air Lock switches in
- Air Lock clears weather first, then new weather is set
- Results in immediate weather reset to opponent's preferred condition

### Multi-Weather Scenarios
- If multiple weather setters are present, last one to act sets weather
- Air Lock user must predict weather setting to maximize disruption
- Creates complex switching mind games

### Primal Weather Interactions
- Air Lock can clear primal weather on entry
- Primal Pokemon can immediately reset their weather
- Results in weather "wars" with constant setting/clearing

## Team Building Considerations

### Core Partners
- **Stealth Rock setters**: Punish forced switches
- **Pivot moves**: Maintain momentum while controlling weather
- **Mixed coverage**: Exploit neutral weather conditions
- **Entry hazard support**: Capitalize on opponent switching

### Problematic Matchups
- **Non-weather teams**: Ability provides no value
- **Fast weather setters**: Can immediately reset after Air Lock
- **Priority moves**: Bypass speed-based weather interactions
- **Setup sweepers**: May not care about weather conditions

## Historical Context
Air Lock was introduced in Generation III as Rayquaza's signature ability, designed to represent its mastery over the sky and weather. In Elite Redux, it maintains its classic function while being enhanced through the multi-ability system, often paired with complementary weather-control abilities.

The ability's strategic value fluctuates with the metagame - extremely powerful in weather-heavy formats but situational in balanced metas. Its immediate entry effect and passive suppression make it one of the most impactful weather-control abilities available.

## Conclusion
Air Lock represents the pinnacle of anti-weather technology, providing both immediate disruption and sustained field control. While matchup-dependent, its ability to completely neutralize weather-based strategies makes it invaluable in appropriate team compositions. The combination of entry clearing and passive suppression creates unique strategic opportunities for timing switches and controlling battle tempo.

In Elite Redux's expanded ability system, Air Lock often works alongside other weather-control abilities to create comprehensive field management tools, making it a cornerstone ability for anti-weather and balanced team strategies.
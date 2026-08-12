---
id: 13
name: Cloud Nine
status: reviewed
character_count: 244
---

# Cloud Nine - Ability ID 13

## In-Game Description
"Clears weather and prevents its effects."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Cloud Nine clears all weather upon switch-in and nullifies weather effects (including Primal weathers) while the user remains on the field. Weather can still be set, but provides no damage boosts or ability triggers until the user switches out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cloud Nine operates through two distinct mechanisms:

1. **On-Entry Weather Removal**: When a Pokemon with Cloud Nine enters battle, it executes `BattleScript_AnnounceAirLockCloudNine` which:
   - Immediately removes any active weather condition
   - Displays appropriate messages about weather being cleared
   - Works on both regular and primal weather conditions

2. **Passive Weather Nullification**: While on field, Cloud Nine prevents ALL weather effects via the `WEATHER_HAS_EFFECT` macro:
   ```c
   #define WEATHER_HAS_EFFECT (!IsAbilityOnField(ABILITY_CLOUD_NINE))
   ```

### Complete List of Blocked Effects
- **Damage Effects**: No Sandstorm/Hail chip damage
- **Type Modifications**: 
  - Water moves don't get 50% boost in rain
  - Fire moves don't get 50% reduction in rain
  - Fire moves don't get 50% boost in sun
  - Water moves don't get 50% reduction in sun
- **Stat Modifications**: Rock-types don't get 50% SpDef boost in sand
- **Ability Activations**: 
  - Swift Swim/Chlorophyll/Sand Rush don't double Speed
  - Rain Dish/Dry Skin/Ice Body don't activate
  - Solar Power/Harvest don't trigger
- **Move Changes**:
  - Solar Beam/Solar Blade still require charging
  - Thunder/Hurricane don't get accuracy boosts
  - Weather Ball remains Normal-type
  - Morning Sun/Moonlight/Synthesis heal standard amounts

### Technical Implementation
- Located in `src/abilities.cc`
- Uses shared code with Air Lock ability
- AI evaluates with `AI_SCORE_REMOVE_WEATHER` rating
- The weather itself remains set but is completely ineffective

### Interactions with Other Abilities
- **Air Lock**: Functions identically to Cloud Nine
- **Clueless**: Prevents weather, terrain, AND room effects
- **Weather-setting abilities**: Can still activate but provide no benefit
- **Primal weather**: Cloud Nine clears even primal weather on entry

### Strategic Implications
- **Anti-Weather Tech**: Hard counter to weather-based strategies
- **Defensive Utility**: Protects team from chip damage and weather boosts
- **Speed Control**: Negates Swift Swim/Chlorophyll/Sand Rush threats
- **Offensive Disruption**: Removes opponent's weather-based damage boosts
- **Switch Timing**: Crucial to time switches for maximum weather denial

### Common Users
Pokemon with access to Cloud Nine in Elite Redux include various defensive and support-oriented species that benefit from weather control.

### Competitive Usage Notes
- Excellent on balanced teams that don't rely on weather
- Pairs well with setup sweepers who appreciate neutral conditions
- Can enable Fire-types to check Water-types in would-be rain
- Allows Ice-types to survive in would-be sun
- Creates "weather wars" where timing becomes critical

### Counters
- Weather setters can reset after Cloud Nine user switches
- Abilities that don't rely on weather (Intimidate, Regenerator, etc.)
- Direct offense to force Cloud Nine user out
- U-turn/Volt Switch to maintain momentum while resetting weather

### Synergies
- Stealth Rock setters (capitalize on forced switches)
- Pokemon weak to weather chip damage
- Mixed attackers who want consistent damage calculations
- Stall teams that prefer neutral conditions

### Version History
Elite Redux maintains the Gen 5+ implementation where Cloud Nine blocks weather effects rather than just preventing weather from being set (as in Gen 3-4).
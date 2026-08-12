---
id: 76
name: Air Lock
status: reviewed
character_count: 193
---

# Air Lock - Ability ID 76

## In-Game Description
"Clears weather and prevents its effects."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Clears all weather upon switch-in and nullifies weather effects while user remains on field. Weather can still be set but provides no benefits. Works on all weather including primal conditions. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**AIR LOCK** is an advanced weather control ability that provides complete weather neutrality to the battlefield.

### Core Mechanics
Air Lock operates through two distinct mechanisms:

1. **On-Entry Weather Removal**: When a Pokemon with Air Lock enters battle, it executes `BattleScript_AnnounceAirLockCloudNine` which:
   - Immediately removes any active weather condition
   - Displays appropriate messages about weather being cleared
   - Works on both regular and primal weather conditions

2. **Passive Weather Nullification**: While on field, Air Lock prevents ALL weather effects via the `WEATHER_HAS_EFFECT` macro:
   ```c
   #define WEATHER_HAS_EFFECT \
       (!gFieldTimers.clearSkiesTimer && !IsAbilityOnField(ABILITY_CLOUD_NINE) && !IsAbilityOnField(ABILITY_AIR_LOCK) && !IsAbilityOnField(ABILITY_CLUELESS))
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
```c
constexpr Ability AirLock = {
    .onEntry = CloudNine.onEntry,
};
```

Air Lock shares identical implementation with Cloud Nine, using the same battle script:
```assembly
BattleScript_AnnounceAirLockCloudNine::
	removeweather
	jumpifbyte CMP_EQUAL, cMULTISTRING_CHOOSER, B_MSG_REMOVE_WEATHER_FAILED, BattleScript_AnnounceAirLockCloudNine_Primal
	jumpifbyte CMP_LESS_THAN, cMULTISTRING_CHOOSER, B_MSG_SUN_ENDS, BattleScript_AnnounceAirLockCloudNine_Primal
	printfromtable gWeatherCleared
	goto BattleScript_AnnounceAirLockCloudNine_OnWeatherChanged
BattleScript_AnnounceAirLockCloudNine_Primal:
	printstring STRINGID_AIRLOCKACTIVATES
BattleScript_AnnounceAirLockCloudNine_OnWeatherChanged:
	waitmessage B_WAIT_TIME_LONG
	call BattleScript_OnWeatherChange
	end3
```

### Interactions with Other Abilities
- **Cloud Nine**: Functions identically to Air Lock
- **Clueless**: Prevents weather, terrain, AND room effects (more comprehensive)
- **Weather-setting abilities**: Can still activate but provide no benefit
- **Primal weather**: Air Lock clears even primal weather on entry
- **Delta Stream**: Air Lock can neutralize Rayquaza's own weather in mirrors

### Strategic Implications
- **Anti-Weather Tech**: Hard counter to weather-based strategies
- **Defensive Utility**: Protects team from chip damage and weather boosts
- **Speed Control**: Negates Swift Swim/Chlorophyll/Sand Rush threats
- **Offensive Disruption**: Removes opponent's weather-based damage boosts
- **Switch Timing**: Crucial to time switches for maximum weather denial
- **Mirror Matches**: Creates neutral conditions in weather wars

### Common Users
In Elite Redux, **Rayquaza** has Air Lock as an innate ability, alongside:
- Dragons Maw (ability slot 1)
- Air Blower (ability slot 2) 
- Violent Rush (ability slot 3)
- Air Lock (innate 1)
- Weather Control (innate 2)
- Aerodynamics (innate 3)

This makes Rayquaza the ultimate weather control Pokemon with multiple weather-related abilities.

### Competitive Usage Notes
- Excellent on balanced teams that don't rely on weather
- Pairs well with setup sweepers who appreciate neutral conditions
- Can enable Fire-types to check Water-types in would-be rain
- Allows Ice-types to survive in would-be sun
- Creates "weather wars" where timing becomes critical
- Essential for dealing with primal weather legendaries

### Example Damage Calculations
**Without Air Lock (Rain active):**
- Hydro Pump (110 BP) to 165 effective BP (1.5x boost)
- Fire Blast (110 BP) to 55 effective BP (0.5x reduction)

**With Air Lock (Weather nullified):**
- Hydro Pump: 110 BP (no boost)
- Fire Blast: 110 BP (no reduction)

### Counters
- Weather setters can reset after Air Lock user switches
- Abilities that don't rely on weather (Intimidate, Regenerator, etc.)
- Direct offense to force Air Lock user out
- U-turn/Volt Switch to maintain momentum while resetting weather
- Clueless ability (blocks even more effects than Air Lock)

### Synergies
- Stealth Rock setters (capitalize on forced switches)
- Pokemon weak to weather chip damage
- Mixed attackers who want consistent damage calculations
- Stall teams that prefer neutral conditions
- Other weather-immune abilities for redundancy

### Version History
Elite Redux maintains the Gen 5+ implementation where Air Lock blocks weather effects rather than just preventing weather from being set (as in Gen 3-4). The shared implementation with Cloud Nine ensures consistent behavior across both abilities.
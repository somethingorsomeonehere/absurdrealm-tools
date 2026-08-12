---
id: 59
name: Forecast
status: reviewed
character_count: 279
---

# Forecast - Ability ID 59

## In-Game Description
"Changes form with the weather. Attacks when setting weather."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Changes form and type to match active weather. When using weather setting moves, follows up with Weather Ball (100 BP, Special, matching type with set weather). Transforms on entry, weather changes, and turn end. Unsuppressable ability that works even under Mold Breaker effects.

## Detailed Mechanical Explanation
**Forecast** is Castform's signature ability that combines form transformation with automatic offensive follow-ups.

### Core Mechanics

#### Form Changes Based on Weather
1. **On Entry**: Checks weather and transforms Castform to appropriate form
2. **On Weather Change**: Immediately transforms when weather changes  
3. **On End Turn**: Checks if weather has ended and reverts form if needed

#### Weather-Setting Attack Trigger
When Castform uses any weather-setting move (Sunny Day, Rain Dance, Sandstorm, Hail, or Eerie Fog), Forecast triggers an automatic follow-up Weather Ball attack against the same target.

### Form Transformations
Castform transforms based on active weather conditions:
- **No Weather**: Castform (Normal-type)
- **Rain**: Castform-Rainy (Water-type)
- **Sun**: Castform-Sunny (Fire-type)
- **Sandstorm**: Castform-Sandy (Rock-type)
- **Hail**: Castform-Snowy (Ice-type)
- **Eerie Fog**: Castform-Foggy (Ghost-type)

### Weather Ball Follow-Up Details
- **Base Power**: 50 normally, doubles to 100 because weather is active
- **Type Changes**: Adapts to match the newly set weather
  - Rain to Water-type
  - Sun to Fire-type
  - Sandstorm to Rock-type  
  - Hail to Ice-type
  - Eerie Fog to Ghost-type
- **Targeting**: Uses same target as the weather-setting move
- **Trigger Condition**: Activates through `UseAttackerFollowUpMove` system

### Technical Implementation
- **Unsuppressable**: Works even under Mold Breaker effects
- **Follow-up System**: Uses `FOLLOWUP_ALLOW_FAILED` targeting
- **Form Detection**: Uses `ShouldChangeFormHpBased` weather-checking system
- **Attack Trigger**: Implemented via `onAttacker` callback

### Strategic Implications
This creates a powerful synergy where setting weather not only transforms Castform but also delivers an immediate 100-power STAB attack of the matching type. The ability essentially gives Castform a "free" strong attack whenever it sets up weather conditions, making it both a weather setter and immediate threat.
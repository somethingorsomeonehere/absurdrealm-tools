---
id: 2
name: Drizzle
status: reviewed
character_count: 270
---

# Drizzle - Ability ID 2

## In-Game Description
"Summons rain on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Drizzle summons rain weather when the Pokemon enters battle, lasting 8 turns (12 with Damp Rock held). Rain boosts Water moves by 50% and cuts Fire damage by 50%. Certain moves and abilities have special interactions with rain. Cannot override primal weather conditions.

## Detailed Mechanical Explanation
*For Discord/reference use*

**DRIZZLE** is a weather-summoning ability that automatically sets rain weather upon switch-in.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle (onEntry hook)
- **Duration**: 8 turns standard, 12 turns with Damp Rock
- **Weather Type**: Regular rain (not heavy rain)
- **Script**: Displays "{Pokemon} made it rain!" with rain animation

### Rain Weather Effects:
1. **Type Modifications**:
   - Water-type moves: 1.5x power
   - Fire-type moves: 0.5x power
   
2. **Move Changes**:
   - Thunder: 100% accuracy (bypasses accuracy checks)
   - Solar Beam/Solar Blade: 0.5x power
   - Weather Ball: Becomes Water-type, doubles power
   - Synthesis/Morning Sun/Moonlight: Restore 25% HP instead of 50%
   
3. **Ability Interactions**:
   - Activates: Swift Swim (2x Speed), Rain Dish (1/16 HP recovery), Dry Skin (1/8 HP recovery), Hydration (status cure)
   - Prevents: Solar Power damage, Flower Gift activation
   - Special: Forecast changes Castform to Water-type

### Interaction Rules:
- **vs Primal Weather**: Cannot override Desolate Land, Primordial Sea, or Delta Stream. Shows "The extremely harsh sunlight was not lessened at all!" or similar message
- **vs Other Weather**: Overrides sun, sandstorm, hail, and fog
- **Multiple Drizzle**: If multiple Pokemon with Drizzle enter simultaneously, speed determines order but only one rain activation occurs

### Technical Implementation:
```c
constexpr Ability Drizzle = {
    .onEntry = +[](ON_ENTRY) -> int {
        if (TryChangeBattleWeather(battler, ENUM_WEATHER_RAIN, TRUE)) {
            BattleScriptPushCursorAndCallback(BattleScript_DrizzleActivates);
            return TRUE;
        } else if (gBattleWeather & WEATHER_PRIMAL_ANY && WEATHER_HAS_EFFECT) {
            BattleScriptPushCursorAndCallback(BattleScript_BlockedByPrimalWeatherEnd3);
            return NO_ANNOUNCE;
        }
        return FALSE;
    },
};
```

### Competitive Notes:
- Pairs excellently with Swift Swim users for speed control
- Enables Thunder spam strategies
- Countered by other weather setters (especially primal abilities)
- Damp Rock is almost mandatory for serious rain teams to maximize weather duration

### Version History:
- Gen 3-5: Permanent weather
- Gen 6+: Limited to 5 turns (8 in Elite Redux)
- Elite Redux: 8 turns base, 12 with Damp Rock
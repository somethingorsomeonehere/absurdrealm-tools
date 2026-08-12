---
id: 44
name: Rain Dish
status: reviewed
character_count: 52
---

# Rain Dish - Ability ID 44

## In-Game Description
"Heals 1/8 of max HP every turn if rain is active."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Restores 1/8 max HP at the end of each turn in rain.

## Detailed Mechanical Explanation
*For Discord/reference use*

**RAIN DISH** is a passive healing ability that provides consistent HP recovery during rain weather conditions.

### Activation Mechanics:
- **Trigger**: End of each turn during rain weather (onEndTurn hook)
- **Healing Amount**: 1/8 of maximum HP (minimum 1 HP)
- **Weather Requirement**: Any rain type (WEATHER_RAIN_ANY)
- **Script**: Uses BattleScript_RainDishActivates with "restored HP a little" message

### Rain Weather Types That Activate:
1. **WEATHER_RAIN_TEMPORARY**: Standard rain from moves like Rain Dance
2. **WEATHER_RAIN_PERMANENT**: Permanent rain from abilities like Drizzle
3. **WEATHER_RAIN_PRIMAL**: Heavy rain from Primordial Sea
4. **WEATHER_RAIN_DOWNPOUR**: Unused rain type

### Healing Requirements:
- **Not at Full HP**: Must have current HP < maximum HP
- **Can Heal**: Must pass CanBattlerHeal() check
- **Not First Turn**: isFirstTurn flag must not equal 2
- **Weather Affected**: Must not be protected by Utility Umbrella

### Blocking Conditions:
Rain Dish healing is prevented by:
- **Heal Block**: STATUS3_HEAL_BLOCK status
- **Bleed**: STATUS1_BLEED status condition
- **Blood Stain**: IsBloodStainAffected() returns true
- **Permanence**: Opposing Pokemon has Permanence ability
- **Hemolysis**: Poisoned and opposing Pokemon has Hemolysis ability

### Item Interactions:
- **Big Root**: Increases healing from 1/8 to approximately 30% more
- **Utility Umbrella**: Blocks rain effects, preventing Rain Dish activation

### Technical Implementation:
```c
constexpr Ability RainDish = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(gVolatileStructs[battler].isFirstTurn != 2)
        CHECK(IsBattlerWeatherAffected(battler, WEATHER_RAIN_ANY))

        gBattleMoveDamage = gBattleMons[battler].maxHP / 8;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        gBattleMoveDamage *= -1;
        BattleScriptPushCursorAndCallback(BattleScript_RainDishActivates);
        return TRUE;
    },
};
```

### Healing Calculations:
- **Base Healing**: floor(MaxHP / 8)
- **Minimum**: 1 HP if calculation results in 0
- **With Big Root**: GetDrainedBigRootHp() applies ~30% bonus
- **Example**: 400 HP Pokemon heals 50 HP per turn (65 HP with Big Root)

### Synergies:
- **Rain Setters**: Drizzle, Primordial Sea users
- **Rain Dancers**: Pokemon that can use Rain Dance
- **Swift Swim**: Fast Pokemon that benefit from rain speed boost
- **Thunder Users**: Perfect accuracy Thunder in rain
- **Water Types**: Boosted Water-type moves in rain

### Counters:
- **Weather Changers**: Sun, sandstorm, hail setters override rain
- **Utility Umbrella**: Blocks weather effects including Rain Dish
- **Heal Block**: Taunt, Heal Block move users
- **Bleed Inflictors**: Moves that cause bleeding status
- **Air Lock/Cloud Nine**: Neutralize weather effects

### Competitive Usage:
- **Rain Teams**: Core component of rain-based strategies
- **Stall Pokemon**: Provides passive healing for defensive builds
- **Bulky Waters**: Enhances survivability of Water-type tanks
- **Weather Wars**: Vulnerable to opposing weather control

### Related Abilities:
- **Ice Body**: Identical effect but for hail weather (1/8 HP healing)
- **Dry Skin**: Also heals in rain (1/8 HP) but takes sun damage
- **Hydration**: Cures status conditions in rain instead of healing

### Version History:
- Gen 3: Introduced with 1/16 HP healing
- Gen 4: Healing increased to 1/8 HP
- Elite Redux: Maintains 1/8 HP healing with enhanced blocking conditions
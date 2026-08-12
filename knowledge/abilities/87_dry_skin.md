---
id: 87
name: Dry Skin
status: reviewed
character_count: 149
---

# Dry Skin - Ability ID 87

## In-Game Description
"Water/Rain heals. Fire/Sun hurts."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user heals 25% HP from Water-type moves and 12.5% HP each turn in rain. Takes 25% more damage from Fire moves and loses 12.5% HP per turn in sun. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**DRY SKIN** is a unique weather-dependent ability that combines water absorption, rain healing, fire weakness, and sun damage into one powerful mechanic.

### Core Mechanics:
- **Water Absorption**: Completely absorbs Water-type moves, healing 25% max HP
- **Rain Healing**: Restores 12.5% max HP at end of turn in rain
- **Fire Weakness**: Takes 1.25x damage from Fire-type moves
- **Sun Damage**: Loses 12.5% max HP at end of turn in sun

### Technical Implementation:
```c
constexpr Ability DrySkin = {
    .onAbsorb = WaterAbsorb.onAbsorb,  // Inherits Water Absorb's effect
    .onEndTurn = +[](ON_END_TURN) -> int {
        // Sun damage effect
        if (IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY) && !IsMagicGuardProtected(battler)) {
            gBattleMoveDamage = gBattleMons[battler].maxHP / 8;
            if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
            BattleScriptPushCursorAndCallback(BattleScript_SolarPowerActivates);
            return TRUE;
        }
        // Rain healing effect (calls RainDish)
        return RainDish.onEndTurn(DELEGATE_END_TURN);
    },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE) RESISTANCE(1.25);  // 25% more damage
        },
    .breakable = TRUE,
};
```

### Water Absorption Component:
- **Effect**: Nullifies all Water-type damage and heals 25% max HP
- **Trigger**: When targeted by any Water-type move
- **Multi-hit**: Each hit of a multi-hit Water move heals 25%
- **Status Moves**: Only damaging Water moves trigger healing

### Rain Healing Component:
- **Healing**: 12.5% max HP (1/8) at end of turn
- **Condition**: Must be in rain AND not at full HP
- **Script**: "Rain restored {Pokemon}'s HP!"
- **First Turn**: No healing on the turn Pokemon enters battle

### Fire Weakness Component:
- **Damage Multiplier**: 1.25x (25% more damage)
- **Applies To**: All Fire-type moves regardless of weather
- **Calculation**: Applied after type effectiveness
- **Stacking**: Multiplicative with other damage modifiers

### Sun Damage Component:
- **Damage**: 12.5% max HP (1/8) per turn
- **Weather Types**: Any sun variant (WEATHER_SUN_ANY)
- **Damage Protection**: Magic Guard prevents damage; Substitute does NOT
- **Minimum Damage**: Always at least 1 HP if calculation rounds to 0
- **Script**: Uses Solar Power's damage message

### Interaction Rules:
1. **Weather Priority**: 
   - In sun: Takes damage (no healing even if hit by Water move that turn)
   - In rain: Heals at end of turn
   - No weather: Only Water absorption and Fire weakness apply

2. **Ability Interactions**:
   - Magic Guard: Prevents sun damage but not Fire weakness
   - Cloud Nine/Air Lock: Negates weather-based effects
   - Mold Breaker: Bypasses Dry Skin entirely

3. **Move Interactions**:
   - Scald: Absorbed for healing despite being hot water
   - Steam Eruption: Fire-type, triggers weakness not absorption
   - Freeze-Dry: Not absorbed (Ice-type)

### Strategic Applications:
1. **Rain Teams**: Excellent passive recovery combined with Water immunity
2. **Anti-Water**: Complete Water immunity makes it a perfect Water counter
3. **Weather Wars**: Forces careful weather management from opponents
4. **Defensive Synergy**: Pairs well with Leftovers for additional recovery

### Competitive Notes:
- Mandatory rain support or careful sun avoidance
- Fire weakness is always active, making Fire coverage extremely threatening
- Can heal beyond single-hit KO range with multi-hit Water moves
- Sun teams hard counter Dry Skin users
- Excellent on defensive Pokemon that can switch into predicted Water attacks

### Canonical Dry Skin Users:
- Parasect, Croagunk, Toxicroak, Heliolisk, Thirst (fakemon)
- In Elite Redux: Available as changeable or innate ability on various Pokemon

### Damage/Healing Calculations:
- 400 HP Pokemon in rain: +50 HP per turn
- 400 HP Pokemon in sun: -50 HP per turn  
- 400 HP Pokemon hit by Surf: +100 HP
- 400 HP Pokemon hit by Flamethrower (neutral): 125 base damage to 156 damage

### Version History:
- Gen 4: Introduced with all current effects
- Elite Redux: Maintained canonical mechanics with weather system integration
---
id: 625
name: Greater Spirit
status: reviewed
character_count: 77
---

# Greater Spirit - Ability ID 625

## In-Game Description
"Upon entry in fog weather, raises highest base stat by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When entering battle during fog, boosts the user's highest stat by one stage.

## Detailed Mechanical Explanation

### Core Mechanics

**Trigger Condition**: Pokemon enters battle during fog weather (permanent or temporary)
**Effect**: Raises the Pokemon's highest stat by +1 stage upon entry
**Weather Types**: Activates during both `WEATHER_FOG_PERMANENT` and `WEATHER_FOG_TEMPORARY`

### Implementation Details

```cpp
constexpr Ability GreaterSpirit = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(IsBattlerWeatherAffected(battler, WEATHER_FOG_ANY))

        int stat = GetHighestStatId(battler, TRUE);
        CHECK(ChangeStatBuffs(battler, 1, stat, MOVE_EFFECT_AFFECTS_USER, NULL))
        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        return TRUE;
    },
};
```

**Key Functions**:
- `GetHighestStatId(battler, TRUE)`: Determines the Pokemon's highest base stat
- `IsBattlerWeatherAffected(battler, WEATHER_FOG_ANY)`: Checks for fog weather conditions
- `ChangeStatBuffs()`: Applies the +1 stat boost

### Strategic Applications

### Pokemon with Greater Spirit
Based on the codebase analysis, Greater Spirit appears on:
1. **Marowak variants** - Likely benefits Attack or Defense stats
2. **Crobat variants** - Typically boosts Speed (125 base)
3. **Sableye variants** - May boost various stats depending on form

### Team Synergy
- **Fog Setters**: Pairs excellently with Pokemon that can set fog weather
- **Stat-Based Strategies**: Amplifies already-strong stats for specialized roles
- **Switch-In Value**: Provides immediate battlefield presence when fog is active

### Competitive Usage
- **Entry Hazard Support**: The stat boost helps survive or pressure upon switching in
- **Role Compression**: Eliminates need for separate stat-boosting moves
- **Weather Team Core**: Essential component of fog-based team compositions

### Similar Abilities
Greater Spirit shares design patterns with other weather-conditional stat boosters:
- **Sea Guardian** (rain + highest stat boost)
- **Sun Worship** (sun + highest stat boost)
- **Protosynthesis** (sun + highest stat boost, with additional mechanics)
- **Quark Drive** (Electric Terrain + highest stat boost)

### Technical Notes

### Weather Detection
- Activates under `WEATHER_FOG_ANY` which includes both permanent and temporary fog
- Uses `IsBattlerWeatherAffected()` to ensure the Pokemon is actually affected by the weather
- Will not activate if the Pokemon has abilities that negate weather effects

### Stat Selection
- `GetHighestStatId(battler, TRUE)` parameter indicates it considers the Pokemon's actual highest stat
- In case of ties, the function follows a predetermined priority order
- Boost applies immediately upon entry, before other entry effects

### Interaction Notes
- Can be suppressed by abilities like Neutralizing Gas
- Boost can be stolen by abilities like Competitive or Defiant on opponents
- Works with Baton Pass to preserve the stat boost when switching out
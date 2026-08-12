---
id: 802
name: Rite Of Spring
status: reviewed
character_count: 77
---

# Rite Of Spring - Ability ID 802

## In-Game Description
"Chlorophyll + Solar Power."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's Speed and highest attacking stat by 50% when sun is active.

## Detailed Mechanical Explanation
*For Discord/reference use*

Rite Of Spring is a combination ability that provides the effects of both Chlorophyll and Solar Power simultaneously when the user is in sun weather.

### Core Mechanics

**Chlorophyll Component:**
- Multiplies the user's Speed stat by 1.5x (50% increase) when in sun weather
- Applies to the final Speed calculation after stat stages

**Solar Power Component:**
- Multiplies the user's highest attacking stat by 1.5x (50% increase) when in sun weather
- The "highest attacking stat" is determined by comparing base Attack vs base Special Attack (including stat stage modifications if `includeStatStages` is true)
- Uses the `GetHighestAttackingStatId()` function which compares only STAT_ATK and STAT_SPATK
- Applies to damage calculations before type effectiveness

### Activation Conditions
- Requires sun weather to be active: `WEATHER_SUN_ANY`
- This includes:
  - Regular Sun (Sunny Day)
  - Harsh Sunlight (Drought)
  - Primal Sun (Primal Groudon's Desolate Land)
- Weather must affect the battler (not blocked by abilities like Air Lock/Cloud Nine)

### Technical Implementation

```cpp
constexpr Ability RiteOfSpring = {
    .onStat =
        +[](ON_STAT) {
            SolarPower.onStat(DELEGATE_STAT);  // Boosts highest attacking stat
            Chlorophyll.onStat(DELEGATE_STAT); // Boosts Speed
        },
};
```

**Chlorophyll Implementation:**
```cpp
.onStat = +[](ON_STAT) {
    if (statId == STAT_SPEED && IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY)) 
        *stat *= 1.5;
}
```

**Solar Power Implementation:**
```cpp
.onStat = +[](ON_STAT) {
    if (statId != GetHighestAttackingStatId(battler, TRUE)) return;
    if (IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY)) 
        *stat *= 1.5;
}
```

### Affected Moves
All moves benefit from the Speed boost, while only attacking moves benefit from the offensive boost:
- **Speed Boost**: Affects turn order, Choice Scarf interactions, and priority calculations
- **Attack Boost**: Physical moves if Attack > Special Attack
- **Special Attack Boost**: Special moves if Special Attack > Attack

### Interactions with Other Abilities/Mechanics

**Positive Synergies:**
- **Growth**: Double stat boost in sun (both Attack and Special Attack +2)
- **Morning Sun/Synthesis**: Enhanced healing in sun
- **Flower Gift**: Additional Attack/Special Defense boost for team
- **Harvest**: Better berry recovery in sun
- **Sun-based moves**: Weather Ball becomes Fire-type, Solar Beam/Solar Blade skip charge turn

**Weather Interactions:**
- **Sand Stream/Snow Warning/Drizzle**: Overrides sun, disabling both effects
- **Cloud Nine/Air Lock**: Suppresses weather effects, disabling both boosts
- **Primal Groudon**: Provides strongest sun form, activating both effects

**Item Synergies:**
- **Heat Rock**: Extends sun duration for longer boost windows
- **Choice items**: Speed boost helps with being locked into moves
- **Life Orb**: Stacks with the offensive boost for massive damage

### Strategic Implications

**Offensive Potential:**
- Massive sweeping potential with both speed and power boosts
- Can function as both physical and special attacker depending on stat distribution
- Excellent for late-game cleanup scenarios

**Team Building:**
- Requires sun support (Drought users, Sunny Day setters)
- Benefits from entry hazard removal to safely switch in
- Pairs well with other sun abusers for weather team synergy

### Example Damage Calculations

**Without Sun:**
- Victreebel (110 Atk/110 SpA, higher stat varies by nature/EVs)
- Solar Blade: Base 125 power, no boost

**With Sun + Rite of Spring:**
- Same Victreebel with 1.5x Attack/Special Attack boost
- Solar Blade: Base 125 power x 1.5 stat boost x no charge turn = ~1.5x damage
- Speed also boosted by 1.5x for better sweep potential

### Common Users
Based on current implementation:
- **Victreebel**: Featured in trainer teams, physical/special mixed sets
- **Custom species**: Various Grass-type or sun-oriented Pokemon
- **Competitive usage**: Primarily on dedicated sun teams

### Competitive Usage Notes

**Strengths:**
- Incredible sweep potential under sun
- Flexible between physical and special sets
- No HP drain unlike traditional Solar Power
- Immediate speed control

**Weaknesses:**
- Completely weather dependent
- Vulnerable to weather change
- Requires team support for sun setting
- Predictable game plan

### Counters

**Direct Counters:**
- **Weather changers**: Pokemon with Sand Stream, Snow Warning, Drizzle
- **Cloud Nine/Air Lock users**: Golduck, Rayquaza (disables weather effects)
- **Priority moves**: Bypass speed advantage
- **Haze/Clear Smog**: Reset any stat changes (though ability boosts reapply)

**Defensive Answers:**
- **Fire-resistant tanks**: Effective against sun-boosted attacks
- **Sturdy + priority**: Survive one hit and revenge kill
- **Choice Scarf users**: Can still outspeed in some cases

### Version History
- Added in Elite Redux as combination ability #802
- Currently available on select species and trainer teams
- Part of the enhanced ability system with multiple simultaneous effects
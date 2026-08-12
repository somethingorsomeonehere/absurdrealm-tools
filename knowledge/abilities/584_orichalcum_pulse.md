---
id: 584
name: Orichalcum Pulse
status: reviewed
character_count: 104
---

# Orichalcum Pulse - Ability ID 584

## In-Game Description
"Summons sun on entry. Raises Atk by 1.33x in sun."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets sun on entry for 8 turns (12 with Heat Rock). While sun is active, boosts the user's Attack by 33%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Orichalcum Pulse is a dual-component ability that combines weather summoning with stat enhancement:

1. **Weather Summoning (Entry Effect)**:
   - Uses the same mechanism as Drought
   - Summons WEATHER_SUN_TEMPORARY on entry
   - Triggers the standard "The sunlight turned harsh!" message
   - Can be blocked by Primal Weather effects

2. **Attack Boost (Stat Modifier)**:
   - Applies a 1.33x multiplier to Attack stat specifically
   - Only active while any form of sun weather is present
   - Checked every time Attack stat is calculated

### Technical Implementation
```cpp
constexpr Ability OrichalcumPulse = {
    .onEntry = Drought.onEntry,  // Summons sun on switch-in
    .onStat = +[](ON_STAT) {
        if (statId != STAT_ATK) return;  // Only affects Attack
        if (IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY)) 
            *stat = *stat * 4 / 3;  // 1.33x multiplier (4/3 = 1.333...)
    },
};
```

### Weather Compatibility
Works with all sun weather types:
- **WEATHER_SUN_TEMPORARY**: Regular Sunny Day, Drought, Solar Beam
- **WEATHER_SUN_PERMANENT**: Infinite sun effects
- **WEATHER_SUN_PRIMAL**: Desolate Land (Primal Groudon's ability)

### Numerical Analysis
- **Base 100 Attack** to **133 Attack** in sun (+33 effective Attack points)
- **Base 150 Attack** to **200 Attack** in sun (+50 effective Attack points)
- The boost is multiplicative with other Attack modifiers (items, stat changes, etc.)

### Activation Conditions
1. **Entry Activation**: Always attempts to summon sun when switching in
2. **Stat Boost Activation**: Only when sun weather is active AND Attack stat is being calculated

### Strategic Implications
- **Immediate Sun Setup**: Guarantees sun weather for the team on switch-in
- **Physical Sweeper Support**: Significant Attack boost for physical movesets
- **Weather Control**: Can override other weather effects (except Primal Weather)
- **Turn Economy**: Saves a move slot by not needing Sunny Day

### Example Damage Calculations
Assuming 252+ Adamant Pokemon with base 100 Attack using 120 BP physical move:
- **Without Orichalcum Pulse**: ~280-330 damage to neutral target
- **With Orichalcum Pulse**: ~373-440 damage to neutral target
- **Damage increase**: Approximately 33% more damage output

### Common Users
Based on datamining, appears as an innate ability on Dragon-type legendary Pokemon, often paired with:
- Dragon's Maw (Dragon-type move boost)
- Winged King (likely Flying-type synergy)

### Competitive Usage Notes
- **Role**: Physical setup sweeper enabler
- **Synergy**: Excellent with Solar Beam users, Chlorophyll teammates
- **Timing**: Best used as lead or early switch to establish sun control
- **Coverage**: Pairs well with Fire-type moves that benefit from sun

### Counters
- **Weather Changers**: Drizzle, Sand Stream, Snow Warning users
- **Primal Weather**: Primordial Sea completely blocks the sun summoning
- **Cloud Nine/Air Lock**: Negates the Attack boost by removing weather effects
- **Defensive Walls**: High Defense Pokemon can still tank boosted attacks

### Synergies
- **Solar Beam**: Instant charging in summoned sun
- **Fire-type moves**: 1.5x damage boost from sun stacks with Attack boost
- **Chlorophyll teammates**: Doubled Speed from the summoned sun
- **Morning Sun/Synthesis**: Enhanced healing from sun weather

### Version History
- **Elite Redux Implementation**: Unique ability combining Drought's entry effect with Attack multiplication
- **Design Philosophy**: Provides both utility (weather) and offense (stat boost) in one ability slot
- **Balance Consideration**: Limited to Attack stat only, requires sun to maintain boost
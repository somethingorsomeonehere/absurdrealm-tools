---
id: 81
name: Snow Cloak
status: reviewed
character_count: 68
---

# Snow Cloak - Ability ID 81

## In-Game Description
"Evasion is boosted by 1.25x under hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces opponent accuracy by 25% during hail. Immune to hail damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**SNOW CLOAK** is a weather-dependent defensive ability that reduces incoming move accuracy during hail weather conditions.

### Core Mechanics:
- **Accuracy Reduction**: Incoming moves have their accuracy divided by 1.25 (20% reduction)
- **Weather Dependency**: Only functions during hail weather (WEATHER_HAIL_ANY)
- **Target Application**: Applied to the Snow Cloak user when they are targeted by moves
- **Hail Immunity**: User takes no damage from hail weather

### Activation Conditions:
- Must be in hail weather (natural or summoned)
- Applies to all moves targeting the Snow Cloak user
- Functions against physical, special, and status moves with accuracy checks

### Numerical Values:
- **Accuracy Modifier**: ÷1.25 (equivalent to 80% accuracy on incoming moves)
- **Example**: 100% accuracy move becomes 80% accuracy, 90% accuracy becomes 72%
- **Hail Immunity**: 100% protection from hail damage each turn

### Technical Implementation:
```c
constexpr Ability SnowCloak = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(IsBattlerWeatherAffected(target, WEATHER_HAIL_ANY));
        *accuracy /= 1.25;
        return ACCURACY_MULTIPLICATIVE;
    },
    .onAccuracyFor = APPLY_ON_TARGET,
    .breakable = TRUE,
    .hailImmune = TRUE,
};
```

### Affected Moves:
- **All moves with accuracy checks** (physical, special, status)
- **Does not affect**: Sure Hit moves (Swift, Shock Wave, etc.)
- **Does not affect**: Moves that bypass accuracy (No Guard interaction)

### Interactions with Other Abilities/Mechanics:
1. **Mold Breaker Effects**: Suppresses accuracy reduction but retains hail immunity
2. **No Guard**: Completely bypasses Snow Cloak's accuracy reduction
3. **Wide Lens/Zoom Lens**: Items that boost accuracy work against Snow Cloak
4. **Compound Eyes**: Accuracy-boosting abilities partially counter the reduction
5. **Sand Veil**: Functions identically but for sandstorm weather

### Strategic Implications:
- **Defensive Utility**: Provides consistent damage avoidance in hail teams
- **Weather Synergy**: Pairs with Snow Warning for immediate activation
- **Stall Potential**: Enables defensive strategies through move-missing
- **Setup Opportunities**: Missed moves allow safe setup time

### Example Damage Calculations:
- **100% accuracy move**: 80% chance to hit
- **90% accuracy move**: 72% chance to hit  
- **85% accuracy move**: 68% chance to hit
- **Thunder (70% in non-rain)**: 56% chance to hit

### Common Users:
- **Alolan Sandshrew**: Ice/Steel defensive wall
- **Swinub**: Early-game defensive option
- **Snover**: Weather setter with defensive utility
- **Vanilluxe**: Bulky special attacker
- **Cubchoo**: Pre-evolution utility
- **Frosmoth**: Special attacker with defensive backup

### Competitive Usage Notes:
- **Hail Teams**: Essential component of defensive hail strategies
- **Stall Teams**: Provides consistent damage avoidance
- **Mixed Success**: Less reliable than direct defensive stats
- **Weather Wars**: Vulnerable to weather changing

### Counters:
- **Weather Removal**: Sun, rain, sandstorm users remove hail
- **Mold Breaker**: Completely nullifies accuracy reduction
- **No Guard**: Bypasses accuracy reduction entirely
- **Sure Hit Moves**: Swift, Shock Wave, etc. ignore accuracy reduction
- **High Accuracy Items**: Wide Lens, Zoom Lens improve hit rates

### Synergies:
- **Snow Warning**: Automatic hail weather setup
- **Ice Body**: Additional hail-based recovery
- **Aurora Veil**: Enhanced defensive capabilities in hail
- **Blizzard**: Perfect accuracy in hail weather
- **Substitute**: Protected setup behind accuracy reduction

### Version History:
- **Gen 4**: Introduced alongside Diamond/Pearl
- **Gen 5**: Maintained functionality
- **Gen 6+**: Hail duration limited to 5 turns
- **Elite Redux**: Enhanced with extended weather duration (8 turns base)
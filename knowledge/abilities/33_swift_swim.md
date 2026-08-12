---
id: 33
name: Swift Swim
status: reviewed
character_count: 32
---

# Swift Swim - Ability ID 33

## In-Game Description
"This Pokemon's Speed gets a 1.5x boost if rain is active."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Speed by 50% during rain.

## Detailed Mechanical Explanation
*For Discord/reference use*

**SWIFT SWIM** is a weather-dependent ability that provides a significant speed boost under rain conditions.

### Activation Mechanics:
- **Trigger**: Passive - Speed calculation hook (onStat)
- **Condition**: Rain weather must be active AND affecting the battler
- **Multiplier**: 1.5x (50% boost) to Speed stat
- **Weather Types**: All rain variants (WEATHER_RAIN_ANY)

### Rain Weather Coverage:
Swift Swim activates under any of the following rain conditions:
1. **Temporary Rain**: Standard rain from Drizzle, Rain Dance (8 turns, 12 with Damp Rock)
2. **Heavy Rain/Downpour**: Currently unused in Elite Redux
3. **Permanent Rain**: Legacy permanent rain (very rare)
4. **Primordial Sea**: Kyogre's primal weather form

### Speed Calculation:
```c
constexpr Ability SwiftSwim = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && IsBattlerWeatherAffected(battler, WEATHER_RAIN_ANY)) *stat *= 1.5;
        },
};
```

### Interaction Rules:
- **Stacking**: Multiplicative with other speed modifiers (Choice Scarf, paralysis, etc.)
- **Weather Immunity**: Does NOT activate if the Pokemon is immune to weather effects
- **Turn Order**: Speed boost applies during stat calculation, affecting turn order immediately
- **Switch In**: Takes effect immediately upon entering battle if rain is already active

### Calculation Examples:
- Base 100 Speed to 150 Speed in rain
- Base 100 Speed + Choice Scarf (1.5x) in rain to 225 Speed (100 x 1.5 x 1.5)
- Base 100 Speed paralyzed (0.25x) in rain to 37.5 Speed (100 x 0.25 x 1.5)

### Synergistic Abilities and Effects:
- **Rain Setters**: Drizzle, Primordial Sea
- **Compound Abilities**: Seaborne (Drizzle + Swift Swim), Way of Swiftness (Pretentious + Swift Swim), Breakwater (Stall + Swift Swim), Atlantic Ruler (Aquatic Dweller + Swift Swim)
- **Rain Support**: Rain Dish (healing), Hydration (status cure), Thunder (100% accuracy)

### Strategic Applications:
1. **Rain Sweeper**: High-powered offensive Pokemon using the speed boost to outpace threats
2. **Rain Support**: Fast pivoting and utility moves in rain teams
3. **Choice Item Synergy**: Scarf users become nearly unstoppable under rain
4. **Priority Bypass**: Outspeeding priority move users with the speed boost

### Competitive Notes:
- Essential ability for rain team offensive cores
- Pairs excellently with water-type attackers benefiting from rain's 1.5x water move boost
- Vulnerable to weather changing (opposing weather setters)
- Completely nullified in other weather conditions
- Thunder becomes 100% accurate in rain, creating powerful special sweeper combinations

### Canonical Swift Swim Users:
- Water-types traditionally: Kingdra, Ludicolo, Kabutops, Seismitoad
- In Elite Redux: Various Pokemon including hybrid abilities that incorporate Swift Swim

### Version History:
- Gen 3+: Consistent 1.5x speed boost in rain
- Elite Redux: Maintained at 1.5x multiplier, works with extended weather system including Primordial Sea
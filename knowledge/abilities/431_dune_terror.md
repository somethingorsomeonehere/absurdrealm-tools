---
id: 431
name: Dune Terror
status: reviewed
character_count: 150
---

# Dune Terror - Ability ID 431

## In-Game Description
"Sand reduces damage by 35%. Boosts Ground moves by 20%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Dune Terror reduces damage taken by 35% during a sandstorm and boosts Ground-type moves by 20%. Damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dune Terror is a dual-purpose ability that provides both defensive and offensive benefits during sandstorm weather. It combines damage reduction with type-specific move boosting for excellent sandstorm synergy.

### Activation Conditions
- **Weather requirement**: Any form of sandstorm weather must be active for damage reduction
  - Regular sandstorm (from Sandstorm move)
  - Sand Stream ability sandstorm
  - Other sandstorm-generating effects
- **Ground-type boost**: Always active when using Ground-type moves during sandstorm
- **Damage reduction**: Applies to all incoming damage when sandstorm is active

### Technical Implementation
```c
constexpr Ability DuneTerror = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_GROUND) MUL(1.2);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IsBattlerWeatherAffected(battler, WEATHER_SANDSTORM_ANY)) MUL(.65);
        },
    .breakable = TRUE,
    .sandImmune = TRUE,
};
```

### Key Mechanics
- **Damage reduction**: 35% reduction (multiplier of 0.65) to all incoming damage during sandstorm
- **Ground-type boost**: 20% boost (multiplier of 1.2) to Ground-type moves during sandstorm
- **Sand immunity**: Pokemon is immune to sandstorm chip damage
- **Breakable**: Can be suppressed by Mold Breaker and similar abilities

### Important Interactions
- **Weather dependency**: Damage reduction only works in active sandstorm
- **Type coverage**: Ground-type boost helps with coverage and STAB moves
- **Sand immunity**: Built-in protection from sandstorm damage
- **Ability suppression**: Both effects disabled if ability is suppressed
- **Weather override**: Effects stop working when sandstorm ends

### Weather Duration
In Elite Redux, weather effects last 8 turns (not 5 like vanilla), making weather-dependent abilities more valuable and reliable.

### Strategic Implications
- **Sand team core**: Excellent ability for sandstorm team builds
- **Defensive wall**: 35% damage reduction makes Pokemon very bulky in sand
- **Ground-type synergy**: Boosts earthquake, earth power, and other Ground moves
- **Weather setter support**: Pairs well with Sand Stream users
- **Dual utility**: Provides both offense and defense in one ability

### Common Users
- Ground-type Pokemon who benefit from STAB Ground moves
- Bulky Pokemon who can tank hits with damage reduction
- Sand team supporters and walls
- Mixed attackers with Ground-type coverage

### Competitive Usage Notes
- Essential for dedicated sandstorm teams
- Provides significant bulk increase in sand weather
- Ground-type moves become very threatening with the boost
- Requires sand support to maximize effectiveness
- Can be paired with Smooth Rock for extended sandstorm duration

### Counters
- **Weather override**: Change weather to disable damage reduction
- **Cloud Nine/Air Lock**: Negates weather effects including damage reduction
- **Ability suppression**: Mold Breaker, Neutralizing Gas, etc.
- **Type immunities**: Flying types immune to Ground moves despite boost
- **Multi-hit moves**: Still deal reduced damage but can overwhelm

### Synergies
- **Sand Stream/Sandstorm**: Essential for ability activation
- **Earthquake/Earth Power**: Strong STAB moves get even stronger
- **Rock Slide/Stone Edge**: Rock types often pair well in sand teams
- **Stealth Rock**: Entry hazard support for sand teams
- **Ground-type coverage moves**: All benefit from the offensive boost

### Version History
- Custom Elite Redux ability (ID 431)
- Designed for sandstorm team synergy
- Combines defensive and offensive utility
- Part of Elite Redux's expanded ability roster

### Notable Features
- **Dual weather benefit**: Both offense and defense in same weather
- **Sand immunity**: Built-in protection from sandstorm damage
- **Breakable design**: Can be counterplayed with Mold Breaker effects
- **Type-specific boost**: Focused on Ground-type move enhancement
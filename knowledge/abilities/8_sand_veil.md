---
id: 8
name: Sand Veil
status: reviewed
character_count: 252
---

# Sand Veil - Ability ID 8

## In-Game Description
"Boosts evasion in a sandstorm. Immune to sandstorm damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

During sandstorm, enemy Pokemon's accuracy is divided by 1.25, and user is immune to sand damage. Bypassed by No Guard/Mold Breaker. (note to self: does this count as +1 evasion? does it just multiply the end result after accuracy/evasion buffs/nerfs?)

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sand Veil provides defensive benefits during sandstorm weather:

1. **Evasion Boost**
   - Reduces opponent's accuracy to 80% (divides by 1.25)
   - Only active during sandstorm weather
   - Stacks multiplicatively with other accuracy/evasion modifiers
   - Applied after other accuracy calculations

2. **Sandstorm Immunity**
   - Complete immunity to sandstorm chip damage
   - Normally non-Rock/Ground/Steel types take 1/16 max HP per turn
   - Allows non-immune types to benefit from sandstorm

### Technical Implementation

**Code Implementation** (`src/abilities.cc`):
```cpp
constexpr Ability SandVeil = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(IsBattlerWeatherAffected(target, WEATHER_SANDSTORM_ANY));
        *accuracy /= 1.25;
        return ACCURACY_MULTIPLICATIVE;
    },
    .onAccuracyFor = APPLY_ON_TARGET,
    .breakable = TRUE,
    .sandImmune = TRUE,
};
```

### Numerical Values
- **Evasion Multiplier**: 1.25x (opponent has 80% normal accuracy)
- **Effective Accuracy Reduction**: 20%
- **Sandstorm Damage Prevented**: 6.25% max HP per turn

### Accuracy Calculation Example
Base 100% accuracy move in sandstorm:
- 100% / 1.25 = **80% final accuracy**

With opponent's Hone Claws (+1 accuracy):
- 133% / 1.25 = **106.4% final accuracy**

### Interactions with Other Abilities/Mechanics
- **Sand Stream**: Partner ability to set sandstorm
- **Mold Breaker**: Bypasses the evasion boost
- **No Guard**: Ignores evasion entirely
- **Compound Eyes**: Partially offsets evasion boost
- **Weather Ball**: Becomes Rock-type in sandstorm

### Strategic Implications
1. **Defensive Pivot**: Harder to hit while taking no sand damage
2. **Setup Opportunity**: Evasion boost helps survive while setting up
3. **Stall Tactics**: Combined with Substitute/Protect
4. **Weather Synergy**: Core member of sand teams
5. **Type Coverage**: Allows non-immune types on sand teams

### Related Abilities
- **Sand Rush**: Speed boost in sandstorm
- **Sand Force**: Power boost in sandstorm
- **Desert Cloak**: Enhanced version with status immunity
- **Snow Cloak**: Hail equivalent

### Common Sand Veil Strategies
**SubVeil**: Substitute + Sand Veil for multiple evasion chances
**Double Team**: Stack evasion boosts (often banned)
**BrightPowder**: Additional evasion stacking
**Focus Sash**: Survive if evasion fails

### Competitive Usage Notes
- B-tier ability due to RNG reliance
- Banned in some competitive formats (evasion clause)
- Excellent for Battle Frontier/Tower
- Requires weather support to function
- Can frustrate opponents with miss streaks

### Example Pokemon with Sand Veil
- **Garchomp**: Fast physical attacker with ground immunity
- **Sandslash**: Physical wall with sand synergy
- **Gliscor**: Defensive pivot with recovery
- **Cacturne**: Mixed attacker with sand immunity
- **Krokorok/Krookodile**: Offensive sand abusers

### Counters
- **Weather Change**: Remove sandstorm entirely
- **No Guard**: Bypass evasion boost
- **Aerial Ace/Smart Strike**: Never-miss moves
- **Haze**: Reset evasion boosts
- **Cloud Nine**: Suppress weather effects

### Synergies
- **Tyranitar/Hippowdon**: Auto-set sandstorm
- **Sand Rush users**: Fast sand team core
- **Substitute**: Abuse evasion for free turns
- **Leftovers**: Stack with no sand damage
- **Rock Slide**: Spread move with flinch chance

### Weather Team Role
Sand Veil users typically serve as:
- Secondary sweepers after Sand Rush users
- Defensive pivots that don't take sand damage
- Setup sweepers that abuse evasion
- Substitute stallers

### Version History
- **All Generations**: Consistent 25% evasion boost in sand
- **Elite Redux**: Functions identically to main series with enhanced integration
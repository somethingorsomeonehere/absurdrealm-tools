---
id: 202
name: Slush Rush
status: reviewed
character_count: 88
---

# Slush Rush - Ability ID 202

## In-Game Description
"This Pokemon's Speed gets a 1.5x boost in hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the Pokemon's Speed stat by 50% during hail. Also grants immunity to hail damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Slush Rush is an offensive ability that provides a significant Speed boost during hail weather conditions, combined with immunity to hail damage. It's the hail counterpart to abilities like Swift Swim (rain) and Chlorophyll (sun).

### Activation Conditions
- **Weather requirement**: Any form of hail weather must be active
  - Regular hail (from Hail move or Snow Warning)
  - Enhanced hail effects (from various weather abilities)
- **Speed boost**: Multiplies Speed stat by 1.5x (50% increase)
- **Hail immunity**: Takes no damage from hail weather
- **Immediate activation**: Speed boost applies as soon as hail becomes active

### Technical Implementation
```c
constexpr Ability SlushRush = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && IsBattlerWeatherAffected(battler, WEATHER_HAIL_ANY)) *stat *= 1.5;
        },
    .hailImmune = TRUE,
};
```

### Speed Boost Mechanics
- **Base calculation**: Speed = (Base Speed x 1.5) + other modifiers
- **Stacking**: Stacks multiplicatively with other Speed modifiers
- **Nature interaction**: Applied after nature modifiers
- **Item interaction**: Works with Choice Scarf, Iron Ball, etc.
- **Stat stage interaction**: Applied after +/- stat stages

### Important Interactions
- **Weather dependency**: Only active when hail is present
- **Immediate application**: Speed changes take effect immediately when weather changes
- **Battle switching**: Maintains speed boost when switching in during hail
- **Ability suppression**: Doesn't work if ability is suppressed by Mold Breaker effects
- **Hail immunity**: Never takes hail damage regardless of type

### Weather Duration
In Elite Redux, weather effects last 8 turns (not 5 like vanilla), making weather-based abilities significantly more valuable for sustained offensive pressure.

### Strategic Implications
- **Hail team sweeper**: Primary role as fast offensive threat on hail teams
- **Weather abuse**: Can outspeed normally faster threats in hail
- **Setup opportunity**: Can use stat-boosting moves before opponents react
- **Revenge killing**: Excellent for cleaning up weakened teams
- **Weather dependent**: Vulnerable when hail isn't active

### Speed Tier Examples
Assuming base 80 Speed with neutral nature:
- **No hail**: 176 Speed at level 50
- **With Slush Rush**: 264 Speed at level 50
- **With +1 and Slush Rush**: 396 Speed at level 50

### Common Users in Elite Redux
Based on the species analysis, Slush Rush appears on various Ice-type and hail-oriented Pokemon:
- Fast Ice-type sweepers with strong offensive stats
- Pokemon with complementary hail-based abilities as innates
- Mixed attackers who benefit from speed control
- Pokemon paired with Snow Warning teammates

### Competitive Usage Notes
- Essential for hail-based offensive teams
- Requires hail support from Snow Warning or Hail move
- Best on Pokemon with strong offensive stats
- Can be paired with Icy Rock for extended hail duration
- Excellent for breaking through bulky teams with speed advantage

### Team Building Considerations
- **Weather setters**: Needs Snow Warning support or manual Hail setup
- **Coverage moves**: Benefits from diverse move pools to hit different types
- **Setup moves**: Can use Swords Dance, Nasty Plot, etc. more safely
- **Priority moves**: Still valuable for extreme speed control
- **Entry hazards**: Synergizes well with Spikes/Stealth Rock support

### Counters
- **Weather override**: Change weather to Sandstorm, Rain, or Sun
- **Cloud Nine/Air Lock**: Negates weather effects completely  
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Priority moves**: Bypass speed advantage entirely
- **Choice Scarf users**: May still outspeed depending on base stats
- **Trick Room**: Reverses speed advantage into disadvantage

### Synergies
- **Snow Warning**: Essential weather setter for activation
- **Aurora Veil**: Defensive setup move available in hail
- **Blizzard**: 100% accuracy in hail weather
- **Ice-type moves**: Often STAB for hail team members
- **Substitute**: Can set up safely with speed advantage
- **Life Orb/Choice items**: Maximize offensive potential

### Notable Movepool Synergies
Many Slush Rush users gain access to:
- **Blizzard**: Perfect accuracy STAB move in hail
- **Ice Shard**: Priority to handle other priority users
- **Earthquake**: Coverage for Steel and Fire types
- **Rock Slide**: Coverage for Flying types weak to Ice
- **U-turn/Volt Switch**: Momentum with speed advantage

### Version History
- **Generation VII**: Original introduction as signature ability
- **Elite Redux**: Benefits from 8-turn weather duration
- **Innate system**: Can appear as innate ability on certain species
- **Expanded distribution**: Available on more Pokemon than in official games

### Hail Team Core
Slush Rush users form the offensive core of hail teams alongside:
- Snow Warning setters for weather control
- Aurora Veil supporters for defensive setup
- Hail-immune walls for defensive backbone
- Priority users for speed control backup
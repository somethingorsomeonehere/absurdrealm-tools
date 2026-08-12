---
id: 873
name: Ice Plumes
status: reviewed
character_count: 97
---

# Ice Plumes - Ability ID 873

## In-Game Description
"Halves damage taken by Special moves. Does NOT double SpDef."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves all incoming Special Attack damage. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Ice Plumes is a defensive ability that reduces incoming special move damage by half. Unlike abilities that boost stats, Ice Plumes applies its damage reduction directly during damage calculation, making it immune to stat manipulation.

### Activation Conditions
- **Move requirement**: Target move must be classified as special (not physical or status)
- **Damage calculation**: Applied as a 0.5x multiplier during final damage calculation
- **Trigger timing**: Activates for every special move that hits the Pokemon
- **No conditions**: Always active when ability is not suppressed

### Technical Implementation
```c
// Ice Plumes defensive multiplier (same as Ice Scales)
constexpr Ability IcePlumes = {
    .onDefensiveMultiplier = 
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_SPECIAL(move)) MUL(.5);
        },
    .breakable = TRUE,
};
```

### What Counts as Special Moves
- **Standard special moves**: Surf, Flamethrower, Psychic, etc.
- **Variable moves**: Hidden Power (always special)
- **Weather-based**: Weather Ball, Solar Beam, etc.
- **Multi-hit specials**: Triple Axel (if special), Icicle Spear (if special)
- **Z-moves/Max moves**: If based on special move

### What Ice Plumes DOESN'T Affect
- **Physical moves**: Any move using Attack vs Defense calculation
- **Status moves**: Non-damaging moves (Thunder Wave, Will-O-Wisp)
- **Entry hazards**: Stealth Rock, Spikes damage on entry
- **Residual damage**: Poison, burn, weather damage
- **Recoil damage**: From own moves like Flare Blitz
- **Confusion damage**: Self-inflicted confusion damage

### Important Interactions
- **Damage calculation timing**: Applied after type effectiveness but before critical hits
- **Multi-hit moves**: Each hit reduced by 50%
- **Substitute**: Works normally when behind substitute
- **Critical hits**: Ice Plumes reduction applied before crit multiplier
- **Stat changes**: Unaffected by Special Defense boosts/drops since it's not a stat modifier
- **Weather**: No interaction with weather effects on damage

### Key Distinction from Stat Boosts
Unlike abilities that double Special Defense (like Marvel Scale for Defense), Ice Plumes:
- Cannot be negated by stat drops
- Cannot be Psych Up'd or Baton Pass'd
- Doesn't affect damage calculation for confusion
- Stacks multiplicatively with actual Special Defense boosts
- Works even at -6 Special Defense

### Stackability
Ice Plumes can stack with other damage reduction:
- **Light Screen**: 0.5x (doubles) x 0.5x (Ice Plumes) = 0.25x total
- **Aurora Veil**: 0.5x (singles) x 0.5x (Ice Plumes) = 0.25x total  
- **Assault Vest**: Special Defense boost stacks multiplicatively
- **Type resistances**: 0.5x resistance x 0.5x Ice Plumes = 0.25x total

### Ability Suppression
Ice Plumes can be bypassed by:
- **Mold Breaker**: Ignores defensive abilities
- **Teravolt/Turboblaze**: Same as Mold Breaker
- **Neutralizing Gas**: Suppresses all abilities in play
- **Ability swaps**: Skill Swap, Role Play, etc.

### Strategic Applications
- **Special wall**: Turns mediocre special bulk into exceptional
- **Mixed attackers counter**: Handles special moves while team covers physical
- **Weather independence**: Provides consistent bulk unlike weather-based defenses
- **Stat boost immunity**: Can't be weakened by Special Attack boosts on opponent
- **Setup counter**: Remains effective against Calm Mind sweepers

### Common Users
Ice Plumes is found as an innate ability on certain Ice-type Pokemon in Elite Redux, particularly:
- Bulky Ice-types that need special defensive presence
- Mixed defensive Pokemon who benefit from selective damage reduction
- Weather-independent defensive options

### Competitive Usage Notes
- **Pivot potential**: Can reliably tank special hits for safe switches
- **Stallbreaking**: Forces physical attackers or status moves
- **Team synergy**: Pairs well with physical walls for defensive core
- **Item flexibility**: No need for Assault Vest, can hold other items
- **Prediction reward**: Rewards switching into predicted special moves

### Counters and Answers
- **Physical attackers**: Ice Plumes offers no protection against physical moves
- **Status moves**: Unaffected by damage reduction
- **Mixed attackers**: Can use physical coverage to exploit
- **Mold Breaker users**: Bypass the ability entirely
- **Stat manipulation**: Lower Special Defense, then use physical moves
- **Entry hazards**: Chip damage not affected by ability

### Notable Calculations
With Ice Plumes active:
- **Neutral special hit**: 252 SpA to ~25% damage becomes ~12.5%
- **Super effective hit**: 2x effectiveness becomes 1x effective
- **STAB + super effective**: 3x becomes 1.5x
- **Critical hit**: Crit multiplier applied after Ice Plumes reduction

### Synergies
- **Physical bulk items**: Assault Vest not needed, can use Leftovers/Berry
- **Light Screen support**: Stacks for 75% special damage reduction
- **Aurora Veil**: Similar stacking effect
- **Recovery moves**: Pairs well with reliable healing
- **Physical attacking moves**: Complements special defensive role

### Version History
- New ability introduced in Elite Redux
- Functions identically to Ice Scales but with different thematic naming
- Available as innate ability on select Ice-type Pokemon
- Part of Elite Redux's expanded ability roster for enhanced team building options
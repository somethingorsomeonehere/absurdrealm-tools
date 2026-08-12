---
id: 102
name: Leaf Guard
status: reviewed
character_count: 63
---

# Leaf Guard - Ability ID 102

## In-Game Description
"Cures own status at the end of every turn in sun."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

During sun, cures all status conditions at the end of the turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Leaf Guard is a defensive ability that provides automatic status condition recovery during sunny weather conditions. The ability activates at the end of each turn when sun is active.

### Activation Conditions
- **Weather requirement**: Any form of sunny weather must be active
  - Regular sun (from Sunny Day or Drought)
  - Harsh sunlight (from Drought ability)
  - Extremely harsh sunlight (from Desolate Land)
- **Timing**: Activates at the end of turn, after all other end-of-turn effects
- **Status cure**: Removes all major status conditions:
  - Burn
  - Freeze
  - Paralysis
  - Poison (including badly poisoned)
  - Sleep

### Technical Implementation
```c
// Leaf Guard triggers at end of turn during sun
if (ability == ABILITY_LEAF_GUARD && IsWeatherSunny()) {
    // Cure status conditions
    if (battler->status1 != STATUS1_NONE) {
        battler->status1 = STATUS1_NONE;
        // Trigger status cure message
    }
}
```

### Important Interactions
- **Status damage timing**: Burn and poison damage still occur before the cure
- **Sleep Talk**: Can still use Sleep Talk on the turn you wake up
- **Rest**: Can use Rest and wake up same turn in sun
- **Toxic damage**: Resets badly poisoned counter when cured
- **Ability suppression**: Doesn't work if ability is suppressed

### Weather Duration
In Elite Redux, weather effects last 8 turns (not 5 like vanilla), making weather-based abilities more valuable.

### Strategic Implications
- **Sun team synergy**: Excellent on sun teams for status immunity
- **Status absorber**: Can switch into status moves freely in sun
- **Rest abuse**: Can use Rest for full recovery without sleep drawback
- **Anti-stall**: Counters toxic stall and burn strategies
- **Weather dependent**: Vulnerable when sun isn't active

### Common Users
- Grass-type Pokemon who benefit from sun
- Pokemon with Chlorophyll as secondary ability
- Sun team supporters and sweepers
- Bulky Grass types that fear status

### Competitive Usage Notes
- Pairs excellently with Drought setters
- Provides pseudo-immunity to status in sun
- Allows aggressive Rest usage for longevity
- Less reliable than status immunity abilities due to weather dependency
- Can be paired with Heat Rock for extended sun duration

### Counters
- **Weather override**: Change weather to disable the ability
- **Cloud Nine/Air Lock**: Negates weather effects
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Multi-hit moves**: Can break through before status cure
- **Entry hazards**: Not affected by Leaf Guard

### Synergies
- **Drought/Sunny Day**: Essential for ability activation
- **Solar Beam/Solar Blade**: No charge in same weather
- **Synthesis/Moonlight**: Enhanced recovery in sun
- **Growth**: Doubled stat boost in sun
- **Fire-type coverage**: Boosted in sun weather

### Version History
- Standard ability since Generation IV
- In Elite Redux, benefits from 8-turn weather duration
- Can be an innate ability on certain Grass-type Pokemon
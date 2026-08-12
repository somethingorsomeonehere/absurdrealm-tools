---
id: 463
name: Jungle's Guard
status: reviewed
character_count: 155
---

# Jungle's Guard - Ability ID 463

## In-Game Description
"Protects Grass-type allies from status and stat drops."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Jungle's Guard shields the user+Grass-type allies from status conditions and stat drops while healing the user's status at the end of each turn during sun. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Jungle's Guard is a hybrid ability that combines the protective capabilities of Flower Veil with the healing properties of Leaf Guard. It provides both team support for Grass-type allies and self-healing for the user.

### Flower Veil Component (Team Protection)
- **Status Immunity**: Prevents all major status conditions from affecting Grass-type allies
  - Sleep, poison, burn, paralysis, freeze, and bleed
  - Uses `CHECK_STATUS1` flag system for comprehensive protection
- **Stat Drop Protection**: Blocks all stat reductions to Grass-type allies
  - Protects Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, and Evasion
  - Counters Intimidate, stat-lowering moves, and ability-based stat drops
- **Application Rules**:
  - Only affects Grass-type Pokemon on the same side as the ability user
  - Does NOT protect the user unless they are also Grass-type
  - Can be bypassed by Mold Breaker and similar abilities
  - Works passively without turn activation requirement

### Leaf Guard Component (Self-Healing)
- **Status Healing**: Cures the user's own status conditions at the end of each turn during sunny weather
  - Works with regular sun, harsh sunlight (Drought), and extremely harsh sunlight (Desolate Land)
  - Removes burn, freeze, paralysis, poison, and sleep
  - Activates after damage from burn/poison is taken
- **Weather Requirement**: Only functions when any form of sun weather is active
- **Timing**: End-of-turn effect, after other turn-end processes

### Technical Implementation
```cpp
// Jungle's Guard uses FlowerVeil's protection system
constexpr Ability JunglesGuard = {
    .onStatusImmune = FlowerVeil.onStatusImmune,      // Status protection for allies
    .onStatusImmuneFor = FlowerVeil.onStatusImmuneFor, // APPLY_ON_ALLY flag
    .breakable = TRUE,
};
```

### Battle Script Integration
- **Stat Protection**: Handled via `IsFlowerVeilProtected()` function in battle script commands
- **Sun Healing**: Integrated with `IsLeafGuardProtected()` function for weather-based healing
- **Dual Functionality**: Ability is recognized by both protection systems

### Activation Conditions
1. **Team Protection**: Always active for Grass-type allies (weather-independent)
2. **Self-Healing**: Only active for the user during sunny weather conditions
3. **Type Restriction**: Protection only applies to Grass-type Pokemon
4. **Weather Dependency**: Healing component requires active sun weather

### Strategic Implications
- **Sun Team Core**: Essential ability for sun-based Grass teams
- **Dual Role**: Provides both support and self-sustaining capabilities
- **Type Synergy**: Perfect for Grass-type Pokemon who benefit from sun
- **Weather Extension**: Pairs well with Heat Rock for longer sun duration
- **Team Composition**: Encourages Grass-heavy team builds

### Important Interactions
- **Status Damage**: Burn and poison damage still occurs before healing
- **Stat Drop Messages**: Displays protection messages when blocking stat reductions
- **Weather Override**: Healing component disabled if sun is removed
- **Ability Suppression**: Both components disabled by Mold Breaker effects
- **Multiple Allies**: Can protect multiple Grass-type teammates simultaneously

### Competitive Analysis

#### Strengths
1. **Comprehensive Protection**: Covers both status and stat immunity for team
2. **Self-Sustaining**: Provides personal status recovery in optimal weather
3. **Weather Synergy**: Perfect for sun teams needing status security
4. **Team Support**: Excellent doubles ability for Grass-type cores
5. **Consistent Activation**: Protection works regardless of weather

#### Weaknesses
1. **Type Restriction**: Only protects Grass-type Pokemon
2. **Weather Dependent**: Healing requires sun to be active
3. **Breakable**: Countered by Mold Breaker and similar abilities
4. **Limited Self-Protection**: User must be Grass-type to benefit from protection
5. **Weather Competition**: Vulnerable to weather override strategies

### Common Usage Scenarios
- **Sun Sweeper Support**: Protecting Grass-type setup sweepers from status/stats
- **Doubles Cores**: Supporting powerful Grass attackers in doubles formats
- **Status Immunity**: Creating pseudo-immunity to common status strategies
- **Anti-Intimidate**: Protecting physical Grass attackers from Attack drops
- **Weather Teams**: Core member of sun-based team compositions

### Synergistic Abilities and Moves
- **Drought/Sunny Day**: Essential for healing component activation
- **Solar Beam/Solar Blade**: No charge in same weather conditions
- **Synthesis/Moonlight**: Enhanced recovery in sunny weather
- **Growth**: Doubled stat boosts during sun weather
- **Chlorophyll**: Speed doubling complements status immunity

### Counters and Counterplay
- **Weather Override**: Primal Kyogre, sand/hail setters disable healing
- **Non-Grass Types**: Ability provides no protection to other types
- **Mold Breaker**: Bypasses both protection and healing components
- **Cloud Nine/Air Lock**: Negates weather for healing component
- **Entry Hazards**: Not affected by Jungle's Guard protection

### Related Abilities
- **Flower Veil**: Provides identical team protection without healing
- **Leaf Guard**: Offers same healing without team protection
- **Aroma Veil**: Protects team from move restrictions (Taunt, Encore)
- **Sweet Veil**: Prevents sleep for entire team regardless of type

### Pokemon That Learn This Ability
*Note: Specific Pokemon assignments would need to be verified in species data files*

### Battle Messages
- **Status Protection**: "The veil of petals protected [Pokemon] from status!"
- **Stat Protection**: "[Pokemon] surrounded itself with a veil of petals!"  
- **Status Healing**: "[Pokemon]'s status was healed by the sunny weather!"

### Version History
- **Elite Redux**: Custom ability combining Flower Veil and Leaf Guard
- **Implementation**: Uses existing battle systems for both components
- **Balance**: Restricted to Grass-types to prevent overpowered usage

### Notes
- Ability ID 463 in the Elite Redux ability enum system
- Uses `ABILITY_JUNGLES_GUARD` constant throughout codebase
- Integrates with both `IsFlowerVeilProtected()` and `IsLeafGuardProtected()` functions
- Weather duration in Elite Redux is 8 turns, making healing more reliable
- Can be combined with other abilities as an innate ability in the 4-ability system
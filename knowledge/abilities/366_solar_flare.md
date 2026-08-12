---
id: 366
name: Solar Flare
status: reviewed
character_count: 135
---

# Solar Flare - Ability ID 366

## In-Game Description
"Chloroplast + Immolate. Fire moves gain STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts Normal-type moves to Fire-type and grants Fire-type STAB. Additionally activates any Sun related effects for the user's moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics

Solar Flare is a powerful combination ability that merges **Immolate** and **Chloroplast** effects, making it one of the most versatile offensive abilities in Elite Redux.

#### Immolate Component (ATE_ABILITY(TYPE_FIRE))
1. **Normal-to-Fire Type Conversion**
   - All Normal-type moves become Fire-type
   - Converted moves receive a 1.2x power boost (ate boost)
   - Includes physical moves like Body Slam, Scratch, Tackle
   - Includes special moves like Hyper Beam, Swift, Tri Attack

2. **Fire-type STAB**
   - Grants STAB (Same Type Attack Bonus) for Fire-type moves
   - 1.5x damage multiplier for all Fire-type attacks
   - Applies to both converted Normal moves and natural Fire moves

#### Chloroplast Component
3. **Weather Ball Enhancement**
   - Base power doubles from 50 to 100
   - Type changes to Fire-type
   - Works regardless of actual weather conditions

4. **Solar Move Instant Charging**
   - Solar Beam and Solar Blade execute immediately (no charging turn)
   - Same effect as using these moves in harsh sunlight

5. **Growth Double Boost**
   - Attack increases by +2 stages instead of +1
   - Special Attack increases by +2 stages instead of +1

### Implementation Details

**Code Location:** `src/abilities.cc` lines 3815-3820
```cpp
constexpr Ability SolarFlare = {
    .onOffensiveMultiplier = Immolate.onOffensiveMultiplier,
    .onMoveType = Immolate.onMoveType,
    .onStab = +[](ON_STAB) -> int { return moveType == TYPE_FIRE; },
    .chloroplast = TRUE,
};
```

**Immolate Reference:** Lines 3064-3066
```cpp
constexpr Ability Immolate = {
    ATE_ABILITY(TYPE_FIRE),
};
```

**ATE_ABILITY Macro:** Lines 285-291
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

**Battle Integration:**
- Move type conversion happens before damage calculation
- STAB bonus applies after type conversion
- Chloroplast effects are checked independently during move execution
- Ate boost flag is set for power calculation bonuses

### Pokemon with Solar Flare

#### Changeable Ability Slot
- **Victini** (Psychic/Fire) - Choice alongside Turboblaze and Power Spot
- **Gloom Evolution Line** (Grass to Grass/Fire) - Choice alongside Moody and Chlorophyll

#### Innate Ability Slot
- **Volcarona Line** (Bug/Fire) - Paired with Flower Gift and Chlorophyll
- **Solrock** (Rock/Psychic) - Paired with Levitate and Sturdy
- Various other Fire and Grass-type Pokemon as innate ability

### Strategic Applications

**Immediate Power Boost:**
- Normal moves like Return, Double-Edge become powerful Fire STAB attacks
- 1.2x ate boost + 1.5x STAB = 1.8x total multiplier for converted moves
- Weather Ball becomes 100 BP Fire move with STAB (150 effective BP)

**Setup Utility:**
- Growth provides immediate +2/+2 offensive stat boost
- Solar Beam becomes instant 120 BP STAB move
- No weather dependency for solar effects

**Coverage Enhancement:**
- Converts Normal coverage moves to Fire-type
- Provides Fire STAB for non-Fire types
- Weather Ball gives reliable Fire coverage regardless of weather

**Team Synergy:**
- Works excellently on sun teams without requiring sun weather
- Complements Grass/Fire dual types perfectly
- Provides immediate offensive presence without setup

### Competitive Analysis

**Strengths:**
- Extremely high immediate offensive power
- Weather independence for solar effects
- Versatile move conversion and enhancement
- No downsides or drawbacks

**Potential Counters:**
- Flash Fire immunity to Fire attacks
- Water-type resists Fire moves
- Opponent using Water moves on Weather Ball
- Priority moves can bypass setup attempts

**Tier Assessment:** High-tier competitive ability
- Immediate impact without setup required
- Significant power boost to multiple move categories
- Flexible enough for various team compositions

### Comparison to Related Abilities

**vs. Pure Immolate (ID 279):**
- Solar Flare adds Chloroplast benefits
- Better for Pokemon with solar moves in movepool
- More versatile overall

**vs. Pure Chloroplast (ID 268):**
- Solar Flare adds type conversion and STAB
- Significantly more offensive presence
- Better for mixed attackers

**vs. Other ATE abilities:**
- Similar conversion mechanics to Pixilate, Aerilate, etc.
- Unique in combining with weather-independent solar effects
- Fire-type often provides better neutral coverage

### Notable Interactions

**Move Interactions:**
- Explosion/Self-Destruct become Fire-type with STAB
- Hidden Power (if Normal) converts to Fire-type
- Z-moves and Max moves maintain Fire typing after conversion

**Ability Interactions:**
- Cannot be Skill Swapped due to its innate nature on most Pokemon
- Works with items like Charcoal for additional Fire-type boost
- Combines well with sun-setting moves for team support

**Weather Interactions:**
- Functions in any weather condition
- Provides sun effects without changing actual weather
- Allows team flexibility in weather choice

This ability represents one of Elite Redux's most powerful offensive combinations, providing immediate impact while maintaining strategic depth through its dual nature and weather independence.
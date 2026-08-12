---
id: 507
name: Fertilize
status: reviewed
character_count: 108
---

# Fertilize - Ability ID 507

## In-Game Description
"Normal-type moves become Grass and Grass gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves to Grass-type and grants STAB for Grass moves, regardless of the user's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fertilize is an "-ate" ability that converts Normal-type moves to Grass-type moves and provides Same Type Attack Bonus (STAB) for all Grass-type moves, regardless of the user's actual typing.

### Move Type Conversion
- **Normal to Grass**: All Normal-type moves become Grass-type
- **1.2x power boost**: Converted moves receive a 20% damage increase
- **STAB application**: All Grass-type moves (including converted ones) receive STAB bonus
- **Type effectiveness**: Converted moves use Grass-type effectiveness chart

### Technical Implementation
```c
// Fertilize uses the ATE_ABILITY macro for TYPE_GRASS
constexpr Ability Fertilize = {
    ATE_ABILITY(TYPE_GRASS),
};

// The macro provides:
// - onMoveType: Converts Normal moves to Grass + sets ateBoost flag
// - onStab: Grants STAB for Grass-type moves regardless of user typing
```

### Damage Calculation
1. Normal move is selected
2. Move type changes to Grass
3. Base power increased by 20% (ateBoost)
4. STAB multiplier applied (1.5x for Grass moves)
5. Type effectiveness calculated using Grass typing
6. Final damage: Base x 1.2 x 1.5 x type effectiveness

### Move Examples
**Commonly converted moves:**
- **Hyper Beam** to Grass Hyper Beam (150 to 180 to 270 with STAB)
- **Return/Frustration** to Grass Return (102 to 122.4 to 183.6 with STAB)
- **Body Slam** to Grass Body Slam (85 to 102 to 153 with STAB)
- **Double-Edge** to Grass Double-Edge (120 to 144 to 216 with STAB)
- **Facade** to Grass Facade (140 when statused to 168 to 252 with STAB)

### Important Interactions
- **Type immunity**: Normal moves can now be resisted by Steel types
- **Effectiveness changes**: Super effective vs Water/Ground/Rock, resisted by Fire/Grass/Poison/Flying/Bug/Dragon/Steel
- **Ability synergies**: Works with other Grass-boosting abilities if stacked
- **Hidden Power**: Does not affect Hidden Power (not Normal-type)
- **Weather synergy**: No direct weather interaction (unlike sun-boosted Fire -ate abilities)

### Strategic Applications
**Offensive advantages:**
- Massive power boost to Normal moves (44% total increase with STAB)
- Access to powerful Normal move coverage with Grass typing
- Surprise factor with unexpected Grass attacks

**Coverage considerations:**
- Gains super effective hits on Water, Ground, and Rock types
- Loses neutral damage to Steel types (now resisted)
- Vulnerable to Fire, Grass, Poison, Flying, Bug, Dragon, and Steel types

### Pokemon Distribution
**Regular ability users:**
- Growlithe Redux (Fire/Grass)
- Arcanine Redux (Fire/Grass) 
- Mega Arcanine Redux (Fire/Grass)
- Turtwig Redux (Flying/Fairy)
- Grotle Redux (Flying/Fairy)
- Torterra Redux (Flying/Fairy)
- Shaymin-Sky (Grass/Flying)

**Innate ability users:**
- Timburr (Fighting)
- Cursola (Ghost)

### Competitive Analysis
**Strengths:**
- Enormous power boost to Normal moves
- Excellent coverage against common types
- Versatile offensive tool
- Works regardless of user's typing

**Weaknesses:**
- Normal moves become resisted by many types
- No defensive utility
- Relies on Normal move availability
- Can be situational depending on matchup

### Team Building Considerations
- **Physical attackers**: Benefit most from strong Normal physical moves
- **Mixed attackers**: Can use both physical and special Normal moves
- **Coverage needs**: Provides unique Grass coverage option
- **Type synergy**: Works well on Pokemon that don't naturally get Grass STAB

### Counters and Counterplay
- **Steel types**: Resist converted Grass moves
- **Fire types**: Resist and often threaten with super effective coverage
- **Multi-type resistors**: Pokemon with Grass resistance via dual typing
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the conversion

### Version History
- Custom Elite Redux ability (ID 507)
- Based on standard -ate ability mechanics
- Available on both regular and regional form Pokemon
- Functions as both regular and innate ability

### Related Abilities
- **Pixilate** (Normal to Fairy)
- **Refrigerate** (Normal to Ice)  
- **Aerilate** (Normal to Flying)
- **Galvanize** (Normal to Electric)
- **Other -ate abilities** with similar mechanics but different types
---
id: 306
name: Nocturnal
status: reviewed
character_count: 157
---

# Nocturnal - Ability ID 306

## In-Game Description
"Boosts own Dark moves by 1.25x. Takes -25% dmg from Dark/Fairy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Dark-type moves receive a 25% boost, and the user takes 25% less damage from Dark and Fairy moves. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Nocturnal provides both offensive and defensive benefits centered around Dark-type moves and certain type resistances:

**Offensive Component:**
- Boosts the power of all Dark-type moves used by the Pokemon by 25% (1.25x multiplier)
- Applies to all Dark-type moves regardless of category (physical, special, or status moves that deal damage)

**Defensive Component:**
- Reduces incoming damage from Dark-type moves by 25% (0.75x multiplier)
- Reduces incoming damage from Fairy-type moves by 25% (0.75x multiplier)

### Technical Implementation
```cpp
constexpr Ability Nocturnal = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_DARK) MUL(1.25);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_DARK || moveType == TYPE_FAIRY) RESISTANCE(.75);
        },
    .breakable = TRUE,
};
```

### Activation Conditions
- **Offensive boost**: Automatically activates when the Pokemon uses any Dark-type move
- **Defensive resistance**: Automatically activates when the Pokemon is targeted by Dark or Fairy-type moves
- No additional conditions required - passive ability that works continuously

### Affected Moves (Dark-type examples)
**Physical Dark moves:**
- Bite: 60 to 75 BP
- Crunch: 80 to 100 BP  
- Night Slash: 70 to 87.5 BP
- Pursuit: 40 to 50 BP
- Sucker Punch: 70 to 87.5 BP
- Knock Off: 65 to 81.25 BP (before item boost)

**Special Dark moves:**
- Dark Pulse: 80 to 100 BP
- Shadow Ball: 80 to 100 BP
- Snarl: 55 to 68.75 BP
- Hex: 65 to 81.25 BP (before status condition boost)

### Damage Calculations
**Offensive Boost Example:**
- Base Dark Pulse (80 BP) to Boosted Dark Pulse (100 BP)
- With STAB (same-type attack bonus): 80 x 1.5 x 1.25 = 150 effective BP
- Equivalent to a 150 BP Dark move with STAB

**Defensive Resistance Example:**
- Incoming Dark Pulse (80 BP) to Reduced to 60 effective BP
- Incoming Moonblast (95 BP) to Reduced to 71.25 effective BP

### Interactions with Other Abilities/Mechanics
- **Stacks multiplicatively** with other damage modifiers (STAB, type effectiveness, items, etc.)
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze, and similar abilities
- **Works with** Adaptability (double STAB) for massive Dark-type damage output
- **Synergizes with** items like Black Glasses or Dread Plate for additional Dark-type boost
- **Defensive component** stacks with natural type resistances/immunities

### Strategic Usage
**Offensive Applications:**
- Excellent for Dark-type attackers and mixed attackers with strong Dark moves
- Particularly powerful on Pokemon with high Attack/Special Attack stats
- Makes Dark-type coverage moves significantly more threatening

**Defensive Applications:**
- Provides valuable resistance to common Dark and Fairy-type attacks
- Helps counter Fairy-type threats and opposing Dark-type Pokemon
- Reduces damage from powerful moves like Play Rough, Moonblast, Dark Pulse, Crunch

### Common Users
Based on the species list, Nocturnal appears on a diverse range of Pokemon including:
- **Dark-type specialists**: Sableye line, Absol line, Mightyena line
- **Night-themed Pokemon**: Noctowl line, Crobat line
- **Mixed attackers**: Various legendary and pseudo-legendary Pokemon
- **Defensive Pokemon**: Carbink line, defensive walls that benefit from the resistances

### Competitive Viability
**Strengths:**
- Reliable 25% damage boost to Dark moves without conditions
- Valuable defensive utility against two common offensive types
- No drawbacks or negative effects
- Passive ability that doesn't require setup

**Weaknesses:**
- Limited to boosting only Dark-type moves (unlike adaptability)
- Breakable by common abilities like Mold Breaker
- Doesn't provide coverage against Fighting, Bug, or Fairy weaknesses that Dark-types often have

### Counters and Counterplay
- **Mold Breaker variants** can ignore both offensive and defensive components
- **Fighting and Bug-type moves** still deal super effective damage to most Dark-types
- **Multi-hit moves** can wear down the defensive benefits over time
- **Status moves** and indirect damage bypass the ability entirely

### Synergistic Abilities and Items
**Ability Synergies:**
- Adaptability: Double STAB + Nocturnal boost = 2.5x Dark move power
- Tough Claws: Contact Dark moves get both boosts
- Strong Jaw: Bite/Crunch get both boosts

**Item Synergies:**
- Black Glasses: Additional 20% boost to Dark moves
- Dread Plate: Alternative 20% boost
- Life Orb: 30% boost to all moves (including boosted Dark moves)
- Choice items: Higher base power for already-boosted Dark moves

### Version History
- Introduced in Elite Redux as ability #306
- Consistently provides 1.25x offensive boost and 0.75x defensive multiplier
- Breakable status maintained throughout development
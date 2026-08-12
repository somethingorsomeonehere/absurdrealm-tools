---
id: 449
name: Rocky Payload
status: reviewed
character_count: 184
---

# Rocky Payload - Ability ID 449

## In-Game Description
"Boosts the power of Rock-type and throwing moves by 1.5x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Rocky Payload boosts Rock-type and throwing-based moves by 50%. Throwing moves include Rock Throw, Egg Bomb, Rock Slide, Rock Tomb, Fling, Rock Wrecker, Grav Apple, and Astral Barrage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rocky Payload is an offensive ability that provides a 1.5x power boost to two distinct categories of moves: Rock-type moves and moves flagged as "throwing-based". This creates a unique hybrid ability that combines type-based boosting with move category enhancement.

### Boosted Move Categories

#### Rock-Type Moves
All moves with Rock typing receive the 1.5x damage multiplier, including:
- Standard Rock attacks (Rock Slide, Stone Edge, Rock Blast)
- Status moves that deal Rock-type damage
- Hidden Power when it becomes Rock-type
- Moves that change type to Rock (e.g., Judgment with Stone Plate)

#### Throwing-Based Moves
Moves with the `throwingBased` flag in their data structure receive the boost regardless of their type:
- **Seismic Toss** (Fighting-type, fixed damage)
- **Rock Throw** (Rock-type, basic throwing attack)
- **Egg Bomb** (Normal-type, explosive projectile)
- **Rock Slide** (Rock-type, gets double boost as both Rock and throwing)
- **Rock Tomb** (Rock-type, gets double boost as both Rock and throwing)
- **Fling** (Dark-type, item-dependent power)
- **Rock Wrecker** (Rock-type, gets double boost as both Rock and throwing)
- **Sky Drop** (Flying-type, two-turn throwing move)
- **Grav Apple** (Grass-type, gravity-enhanced throwing)
- **Astral Barrage** (Ghost-type, multi-target throwing)

### Technical Implementation
```c
constexpr Ability RockyPayload = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_ROCK || gBattleMoves[move].throwingBased) MUL(1.5);
        },
};
```

### Double Boost Interaction
Some moves receive the Rocky Payload boost twice:
- **Rock Slide**: Rock-type AND throwing-based to 1.5x boost (not 2.25x)
- **Rock Tomb**: Rock-type AND throwing-based to 1.5x boost (not 2.25x)
- **Rock Throw**: Rock-type AND throwing-based to 1.5x boost (not 2.25x)
- **Rock Wrecker**: Rock-type AND throwing-based to 1.5x boost (not 2.25x)

The ability applies a single 1.5x multiplier even if a move qualifies for both categories.

### Activation Conditions
- **Offensive moves only**: Only affects damage-dealing moves
- **User must have ability**: Ability suppression prevents activation
- **No weather/terrain requirements**: Works unconditionally when active
- **Stacks with other boosts**: Combines multiplicatively with items, weather, etc.

### Strategic Implications

#### Strengths
- **Type coverage diversity**: Boosts moves across multiple types (Rock, Fighting, Normal, Dark, Flying, Grass, Ghost)
- **Fixed damage enhancement**: Boosts Seismic Toss and similar moves that ignore type effectiveness
- **Item synergy**: Enhanced Fling power with various held items
- **Consistent power**: No situational requirements or restrictions
- **Multi-hit compatibility**: Works with multi-hit throwing moves

#### Weaknesses
- **Limited move pool**: Only specific moves benefit from the boost
- **Type dependency**: Half the benefit relies on Rock-type moves
- **No defensive utility**: Purely offensive ability
- **Predictable**: Opponents can anticipate boosted moves
- **Item dependence**: Fling requires held items to be effective

### Competitive Usage Notes
- **Physical attackers**: Best suited for physically-oriented Pokemon
- **Coverage moves**: Throwing moves provide unique type coverage
- **Item strategies**: Fling becomes a viable coverage option
- **Rock-type STAB**: Excellent for Rock-type Pokemon seeking additional coverage
- **Niche applications**: Sky Drop and Seismic Toss gain unexpected power

### Synergies
- **Choice items**: Enhanced power with locked move selection
- **Life Orb**: Stacks for additional damage boost
- **Rock-type STAB**: Triple damage on Rock-type throwing moves (STAB + Rocky Payload)
- **Adaptability**: Theoretical 3x boost on Rock-type throwing moves
- **Expert Belt**: Super effective throwing moves gain additional power
- **Fling items**: King's Rock, Choice items, berries all become viable weapons

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas, etc.
- **Type resistances**: Steel and Fighting resist many boosted moves
- **Protect/Detect**: Blocks enhanced throwing attacks
- **Ghost immunity**: Immune to enhanced Seismic Toss
- **Levitate/Air Balloon**: Avoids enhanced Earthquake-like effects

### Notable Users
This ability would be particularly effective on:
- Rock-type physical attackers with diverse movepools
- Pokemon with access to both Rock moves and unique throwing moves
- Mixed attackers that can utilize both categories effectively
- Pokemon with Fling strategies and item manipulation

### Version History
- Custom Elite Redux ability (ID 449)
- Unique hybrid mechanic combining type and move category boosts
- Part of the extended ability roster beyond base game abilities
- Designed to create interesting team building decisions with move selection

### Interaction Notes
- **Z-Moves**: Base power boost applies before Z-Move conversion
- **Max Moves**: Enhanced base power carries over to Dynamax moves
- **Parental Bond**: Each hit gets the full 1.5x boost
- **Multi-hit moves**: Each hit receives the boost independently
- **Critical hits**: Boost applies before critical hit calculation
- **Weather effects**: Stacks multiplicatively with weather boosts/penalties
---
id: 200
name: Steelworker
status: reviewed
character_count: 169
---

# Steelworker - Ability ID 200

## In-Game Description
"Normal becomes Steel + Steel gains STAB. Resists Ghost/Dark."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Steelworker converts Normal-type moves to Steel-type and grants STAB for Steel moves regardless of typing. Additionally takes half damage from Dark and Ghost-type moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Steelworker is a hybrid ability that combines the ATE (type-conversion) family mechanics with unique defensive properties. It serves dual purposes as both an offensive type converter and a defensive resistance provider.

### Type Conversion Component (ATE_ABILITY)
- **Normal-to-Steel conversion**: All Normal-type moves used by the Pokemon become Steel-type
- **STAB access**: The Pokemon gains STAB (1.5x damage) for ALL Steel-type moves, regardless of original typing
- **Pre-damage conversion**: Type conversion occurs before damage calculation and type effectiveness
- **Elite Redux difference**: Unlike main series, no additional 1.2x power boost to converted moves

### Defensive Resistance Component
- **Dark-type resistance**: Incoming Dark-type moves deal half damage (0.5x multiplier)
- **Ghost-type resistance**: Incoming Ghost-type moves deal half damage (0.5x multiplier)
- **Unique defensive profile**: No other ability provides these specific resistances

### Technical Implementation
```c
constexpr Ability Steelworker = {
    ATE_ABILITY(TYPE_STEEL),  // NormaltoSteel conversion + Steel STAB
    .onAfterTypeEffectiveness =
        +[](ON_AFTER_TYPE_EFFECTIVENESS) {
            if (moveType == TYPE_DARK || moveType == TYPE_GHOST) *mod /= 2;
        },
    .onAfterTypeEffectivenessFor = APPLY_ON_TARGET,
    .breakable = TRUE,
};
```

### Strategic Applications

**Offensive Benefits:**
- Converts Normal moves like Body Slam, Return, Hyper Voice to Steel-type with STAB
- Grants Steel STAB to non-Steel types, allowing super-effective hits on Rock, Ice, Fairy
- Excellent for Pokemon with expansive Normal movepools
- Steel typing provides neutral coverage against most types

**Defensive Benefits:**
- Half damage from Dark moves (counters Knock Off, Crunch, Dark Pulse)
- Half damage from Ghost moves (counters Shadow Ball, Shadow Claw, Hex)
- Provides defensive utility typically unavailable to most Pokemon
- Creates favorable matchups against Dark and Ghost-type specialists

**Unique Positioning:**
- Only ability that combines type conversion with specific type resistances
- Allows offensive Pokemon to have defensive utility against common attacking types
- Particularly valuable in Elite Redux's multi-ability system as innate ability

### Common Users and Synergies
Based on species data analysis:
- **Magnezone line**: Natural Steel typing benefits from enhanced STAB coverage
- **Durant**: Bug/Steel with access to powerful Normal moves to convert
- **Dialga variants**: Legendary with Steel typing gains additional defensive utility
- **Custom Elite Redux Pokemon**: Various fan-made species utilize this unique combination

### Competitive Usage Notes
- **Team role flexibility**: Can function as both offensive converter and defensive pivot
- **Coverage enhancement**: Steel moves hit Rock, Ice, Fairy super-effectively
- **Dark/Ghost counter**: Hard counters common offensive types in competitive play
- **Multi-ability synergy**: Excellent as innate ability paired with other offensive abilities

### Type Effectiveness Interactions
**Steel-type moves become super-effective against:**
- Rock types (2x damage)
- Ice types (2x damage) 
- Fairy types (2x damage)

**Steel-type moves resisted by:**
- Steel types (0.5x damage)
- Fire types (0.5x damage)
- Water types (0.5x damage)
- Electric types (0.5x damage)

**Defensive resistances provided:**
- Dark moves to 0.5x damage taken
- Ghost moves to 0.5x damage taken

### Counters and Limitations
**Ability Suppression:**
- Mold Breaker ignores type conversion and resistances
- Neutralizing Gas suppresses the ability entirely
- Ability-changing moves remove Steelworker benefits

**Type Disadvantages:**
- Steel moves don't affect non-converted moves
- Still vulnerable to Fire, Fighting, Ground moves at normal effectiveness
- Fire types resist Steel moves and can exploit typical Steel weaknesses

**Strategic Counters:**
- Fire-type coverage to exploit typical Steel weaknesses
- Physical Fighting moves for neutral damage
- Status moves unaffected by type conversion
- Entry hazards and indirect damage bypass resistances

### Synergistic Combinations
**In Elite Redux 4-ability system:**
- **Iron Fist**: Boosts Steel-type punching moves converted from Normal
- **Sheer Force**: Enhances Steel moves with secondary effects
- **Tough Claws**: Boosts Steel-type contact moves
- **Adaptability**: Doubles STAB bonus for Steel moves

**Team Support:**
- **Magnet Rise users**: Cover Ground weakness common to Steel types
- **Fire-type coverage**: Handle Steel resistances
- **Status support**: Paralysis/burns help with Speed control

### Version History and Elite Redux Changes
- **Custom Elite Redux ability**: Unique combination not found in main series
- **Enhanced utility**: Provides both offensive and defensive benefits
- **Multi-ability compatibility**: Functions as changeable or innate ability
- **Balanced design**: Strong but has clear counters and limitations

### Notable Interactions
- **Return/Frustration**: High-power Normal moves become Steel with STAB
- **Multi-hit moves**: Each hit gets Steel typing and STAB
- **Hidden Power**: If Normal-type, converts to Steel (rare interaction)
- **Choice items**: Lock into Steel-type moves after conversion
- **Normalize interaction**: Steelworker overrides Normalize's type conversion
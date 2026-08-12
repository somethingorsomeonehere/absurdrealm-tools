---
id: 279
name: Immolate
status: reviewed
character_count: 115
---

# Immolate - Ability ID 279

## In-Game Description
"Normal-type moves become Fire and Fire gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immolate converts all Normal-type moves to Fire-type and grants STAB for Fire moves, regardless of the user's type. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Immolate is part of the "-ate" ability family that converts Normal-type moves to another type while providing STAB and damage bonuses.

### Core Mechanics
- **Type Conversion**: All Normal-type moves become Fire-type
- **STAB Application**: Fire-type moves receive Same Type Attack Bonus (1.5x damage)
- **Damage Bonus**: Converted moves receive an additional 10% damage multiplier (1.1x)
- **Total Multiplier**: Converted moves deal 1.5x (STAB) x 1.1x (ate bonus) = 1.65x base damage

### Activation Conditions
- Only applies to Normal-type moves used by the Pokemon with Immolate
- Works on both physical and special Normal-type moves
- Activates automatically when a Normal-type move is selected

### Technical Implementation
```c
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }

constexpr Ability Immolate = {
    ATE_ABILITY(TYPE_FIRE),
};
```

The `ateBoost` flag triggers a 1.1x damage multiplier in the damage calculation system.

### Affected Normal-Type Moves
All Normal-type moves become Fire-type, including but not limited to:
- **Physical**: Return, Body Slam, Double-Edge, Facade, Giga Impact, Quick Attack, Extreme Speed
- **Special**: Hyper Beam, Swift, Hidden Power (if Normal), Boomburst
- **Status**: Moves like Thunder Wave remain Normal-type (status moves aren't affected by type conversion)

### Interactions with Other Mechanics
- **Type Effectiveness**: Converted moves follow Fire-type effectiveness (weak to Water/Ground/Rock, resisted by Fire/Water/Rock/Dragon)
- **Weather**: Benefits from Sun (1.5x Fire move boost), hindered by Rain (0.5x Fire move reduction)
- **Items**: Works with Charcoal, Heat Rock effects, and other Fire-type boosting items
- **Abilities**: Synergizes with Flash Fire, Drought, and other Fire-type abilities
- **Protean/Libero**: If the user has Protean/Libero, they become Fire-type when using converted moves

### Strategic Implications
- **Movepool Expansion**: Gives Fire-types access to powerful Normal moves as Fire attacks
- **Coverage**: Normal moves typically have neutral coverage, now gain Fire typing advantages/disadvantages
- **Power Boost**: Significant damage increase for former Normal moves (65% total boost)
- **Typing Synergy**: Works exceptionally well on pure Fire-types who get STAB on both natural Fire moves and converted Normal moves

### Example Damage Calculations
Base Return (102 BP at max happiness):
- Without Immolate: 102 BP Normal move
- With Immolate: 102 x 1.5 (STAB) x 1.1 (ate bonus) = ~168 effective BP Fire move

### Common Users
**Pokemon with Immolate as innate ability:**
- Vulpix (innate)

**Pokemon with Immolate as regular ability:**
- Fennekin line (Fennekin, Braixen)
- Fuecoco line (Fuecoco, Crocalor, Skeledirge)

### Competitive Usage Notes
- **Niche Strategy**: Allows Fire-types to use Normal moves for coverage while maintaining Fire typing benefits
- **Sun Teams**: Excellent in sun-based teams where Fire moves get additional weather boost
- **Choice Item Synergy**: Works well with Choice items since all attacks become Fire-type
- **Priority Moves**: Quick Attack becomes a Fire-type priority move with STAB

### Counters
- **Water/Ground/Rock types**: Resist the converted Fire moves
- **Flash Fire users**: Immune to converted Fire attacks and get Attack boost
- **Weather Control**: Rain significantly reduces damage of converted moves
- **Heatran**: Immune to Fire moves due to Flash Fire ability

### Synergies
- **Drought**: Boosts converted Fire moves by additional 50%
- **Flash Fire**: If activated by opponent, boosts all Fire moves including converted ones
- **Choice Items**: All attacks become same type, maximizing Choice item effectiveness
- **Flame Orb + Guts**: Guts boost applies to converted Normal physical moves

### Version History
- Added as part of Elite Redux's expanded ability system
- Part of the "-ate" family alongside Refrigerate, Pixilate, Aerilate, and others
- Follows standard -ate ability mechanics with Fire-type conversion
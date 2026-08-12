---
id: 800
name: Deviate
status: reviewed
character_count: 106
---

# Deviate - Ability ID 800

## In-Game Description
"Normal-type moves become Dark and Dark gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves to Dark-type and grants STAB for Dark moves, regardless of the user's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Type Conversion**: All Normal-type moves become Dark-type
- **STAB Grant**: Provides STAB (Same Type Attack Bonus) for Dark-type moves, regardless of the user's typing
- **ATE Boost**: Sets the ateBoost flag when converting moves, which may provide a damage multiplier

### Activation Conditions
- Automatically active when the Pokemon has this ability
- Applies to all Normal-type moves used by the Pokemon
- STAB applies to all Dark-type moves (both converted and naturally Dark-type)

### Technical Implementation
```cpp
constexpr Ability Deviate = {
    ATE_ABILITY(TYPE_DARK),
};

#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Complete List of Affected Moves
**Common Normal-type moves that become Dark-type:**
- Tackle to Dark-type
- Body Slam to Dark-type  
- Hyper Beam to Dark-type
- Swift to Dark-type
- Double-Edge to Dark-type
- Slash to Dark-type
- Tri Attack to Dark-type
- Return/Frustration to Dark-type
- Facade to Dark-type
- Giga Impact to Dark-type

**All other Normal-type moves are similarly converted**

### Interactions with Other Abilities/Mechanics
- **Type-changing abilities**: Deviate takes precedence over most other type-changing effects
- **Ion Deluge/Electrify**: These field effects override Deviate for Normal-type moves
- **Plasma Fists status**: Overrides Deviate conversion
- **STAB calculation**: Provides 1.5x damage multiplier for Dark-type moves
- **Type effectiveness**: Converted moves use Dark-type effectiveness chart

### Strategic Implications
- **Offensive utility**: Turns weak Normal moves into potentially super-effective Dark moves
- **Coverage expansion**: Provides Dark-type coverage to Pokemon that lack it naturally
- **STAB abuse**: Non-Dark types can benefit from Dark-type STAB
- **Movepool synergy**: Best on Pokemon with diverse Normal-type movepools

### Example Damage Calculations
**Scenario**: Level 50 Pokemon with 100 Attack using Body Slam (85 BP)
- **Without Deviate**: 85 BP Normal-type (no STAB if not Normal-type)
- **With Deviate**: 85 BP Dark-type + STAB (127.5 effective BP) + potential ATE boost

### Common Users
This is a custom Elite Redux ability (ID 800), so users would be specific Pokemon in this ROM hack's roster.

### Competitive Usage Notes
- **Priority**: High utility for Pokemon lacking Dark-type moves
- **Synergy**: Excellent with Pokemon that have strong Normal-type movepools
- **Coverage**: Provides neutral-to-super-effective coverage against Psychic and Ghost types
- **Flexibility**: Maintains movepool diversity while gaining type consistency

### Counters
- **Dark-type resists**: Steel, Fighting, Dark, and Fairy types resist converted moves
- **Wonder Guard**: Still blocks moves that wouldn't be super-effective
- **Ability suppression**: Gastro Acid, Worry Seed nullify the conversion
- **Type-changing moves**: Moves like Soak can remove Dark typing benefit

### Synergies
- **Choice items**: Benefit from consistent Dark-type STAB across movepool
- **Life Orb**: Amplifies the boosted Dark-type moves
- **Dark-type Z-moves**: Can upgrade converted Normal moves to powerful Dark Z-moves
- **Adaptability**: Would double the STAB bonus if combined (theoretical)

### Version History
- Introduced in Elite Redux as ability ID 800
- Uses the standard ATE_ABILITY macro system
- Functions similarly to Pixilate, Refrigerate, and Aerilate from official games
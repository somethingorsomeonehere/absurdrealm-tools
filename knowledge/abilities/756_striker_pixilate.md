---
id: 756
name: Striker Pixilate
status: reviewed
character_count: 160
---

# Striker Pixilate - Ability ID 756

## In-Game Description
"Boosts the power of kicking moves by 1.3x + Pixilate."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the power of all kicking moves by 30%. Includes Pyro Ball. Normal-type moves become Fairy-type and they receive STAB regardless of the Pokemon's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Striker Pixilate is a combination ability that merges two existing abilities:
1. **Striker Effect**: Boosts power of moves with the `FLAG_STRIKER_BOOST` flag by 1.3x (30% increase)
2. **Pixilate Effect**: Converts Normal-type moves to Fairy-type and provides STAB for Fairy-type moves

### Technical Implementation
```cpp
constexpr Ability StrikerPixilate = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            Striker.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            Pixilate.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        },
    .onMoveType = Pixilate.onMoveType,
};
```

The ability delegates to both Striker and Pixilate abilities for damage calculation and uses Pixilate's type conversion system.

### Striker Boost Conditions
```c
int IsStrikerBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_STRIKER_BOOST) return TRUE;
    if (gBattleMoves[move].flags & FLAG_IRON_FIST_BOOST && 
        BattlerHasAbility(battler, ABILITY_JUNSHI_SANDA, FALSE)) return TRUE;
    return FALSE;
}
```

### Pixilate (ATE_ABILITY) Implementation
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Affected Moves (Striker Component)
Moves with `FLAG_STRIKER_BOOST` include:
- **Kicking Moves**: Double Kick, Mega Kick, Jump Kick, Rolling Kick
- **New Elite Redux Moves**: Rider Kick, Fire Glaive, Dual Wingbeat
- **And others**: Various moves flagged as benefiting from striking/kicking power

### Type Conversion (Pixilate Component)
- All Normal-type moves become Fairy-type
- Converted moves receive the "ate boost" (typically 1.2x multiplier)
- Pokemon gains STAB on all Fairy-type moves (including converted ones)

### Damage Calculation Examples
1. **Normal Kicking Move (e.g., if Mega Kick was Normal-type)**:
   - Base Power: 120
   - Striker boost: 120 x 1.3 = 156
   - Pixilate conversion: Normal to Fairy
   - Pixilate boost: 156 x 1.2 = 187.2
   - STAB (if applicable): 187.2 x 1.5 = 280.8

2. **Fairy Kicking Move**:
   - Base Power: 120  
   - Striker boost: 120 x 1.3 = 156
   - STAB: 156 x 1.5 = 234

3. **Normal Non-Kicking Move**:
   - Base Power: 80
   - Pixilate conversion: Normal to Fairy
   - Pixilate boost: 80 x 1.2 = 96
   - STAB: 96 x 1.5 = 144

### Interactions and Synergies
- **Life Orb**: Stacks multiplicatively with both effects
- **Choice Items**: Work normally with converted moves
- **Adaptability**: Would boost STAB from 1.5x to 2.0x on Fairy moves
- **Sheer Force**: Would prevent Pixilate conversion if moves have secondary effects
- **Normalize**: Would conflict with Pixilate conversion

### Strategic Applications
- **Mixed Attacker**: Can use both physical kicking moves and special NormaltoFairy moves
- **Type Coverage**: Fairy typing provides good neutral coverage
- **STAB Abuse**: Every Normal move becomes a STAB Fairy move
- **Power Stacking**: Dual boosts make both move categories very powerful

### Common Users
This ability would be ideal for Pokemon that:
- Have access to both kicking moves and Normal-type moves
- Can utilize mixed offensive stats
- Benefit from Fairy typing (counters Dark, Fighting, Dragon)

### Competitive Considerations
**Strengths**:
- Massive power boost to two different move categories
- Type conversion provides unexpected coverage
- STAB on converted moves increases consistency

**Weaknesses**:
- Steel and Poison types resist Fairy moves
- Fire types resist Fairy attacks
- Limited move pool dependency (needs kicking moves for full benefit)

**Counters**:
- Steel-type Pokemon (resist Fairy)
- Poison-type Pokemon (resist Fairy)  
- Heatran (Steel/Fire resists Fairy)
- Abilities like Flash Fire, Motor Drive (if Fairy moves become other types through items)

### Version History
- Added in Elite Redux as a combination ability
- Part of the expanded ability system designed to create unique playstyles
- Represents the hybrid ability concept where two existing abilities are merged
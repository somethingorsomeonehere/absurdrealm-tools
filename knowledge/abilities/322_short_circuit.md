---
id: 322
name: Short Circuit
status: reviewed
character_count: 77
---

# Short Circuit - Ability ID 322

## In-Game Description
"Boosts Elec.-type moves by 1.2x, or 1.5x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Electric-type moves by 20%, or by 50% at 1/3 HP or lower.

## Implementation Details

### Code Location
- **Primary Implementation**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Ability Definition**: Uses `SWARM_MULTIPLIER(TYPE_ELECTRIC)` macro
- **Ability Constant**: `ABILITY_SHORT_CIRCUIT = 322`

### Technical Implementation
```cpp
constexpr Ability ShortCircuit = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_ELECTRIC),
};
```

The ability uses the `SWARM_MULTIPLIER` macro which implements:
```cpp
#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
            else                                                             \
                MUL(1.2);                                                    \
        }                                                                    \
    }
```

## Mechanics Analysis

### Power Boost Conditions
1. **Above 1/3 HP**: Electric-type moves receive 1.2x power multiplier
2. **At or below 1/3 HP**: Electric-type moves receive 1.5x power multiplier

### Key Mechanics
- **Move Type Restriction**: Only affects Electric-type moves
- **HP Threshold**: Activates stronger boost when HP <= maxHP/3
- **Multiplicative Scaling**: Applies as a damage multiplier, not base power modification
- **Real-time Calculation**: Boost level recalculated each turn based on current HP

### Comparison to Standard Swarm Abilities
Short Circuit follows the same pattern as other swarm-type abilities in Elite Redux:
- **Overgrow**: 1.2x/1.5x for Grass moves
- **Blaze**: 1.2x/1.5x for Fire moves  
- **Torrent**: 1.2x/1.5x for Water moves
- **Swarm**: 1.2x/1.5x for Bug moves

## Strategic Applications

### Optimal Usage
- **Low HP Sweeping**: Maximum effectiveness when Pokemon is weakened
- **Electric-type Spam**: Best on Pokemon with multiple Electric moves
- **Late-game Power**: Provides comeback potential when HP is low

### Pokemon Synergy
- **Electric-type Attackers**: Maximizes STAB bonus combination
- **Mixed Attackers**: Benefits both physical and special Electric moves
- **Frail Sweepers**: Natural synergy with glass cannon builds

### Battle Scenarios
- **Revenge Killing**: Enhanced power when switching in at low HP
- **Endgame Situations**: Critical power boost in desperate situations
- **Choice Item Users**: Locks into boosted Electric moves

## Competitive Considerations

### Strengths
- **Consistent Base Boost**: 1.2x boost even at full health
- **Significant Low HP Boost**: 1.5x multiplier provides substantial power
- **Type-Specific**: Doesn't interfere with other move types
- **No Drawbacks**: Pure offensive benefit with no penalties

### Limitations
- **Electric-type Only**: Limited to one move type
- **HP Dependency**: Requires damage to reach maximum potential
- **No Utility**: Purely offensive with no defensive benefits

### Interaction Notes
- **Stacks with STAB**: Combines multiplicatively with same-type attack bonus
- **Stacks with Items**: Works with Choice items, Life Orb, etc.
- **Type Effectiveness**: Applied before type effectiveness calculations

## Related Abilities
- **Swarm**: Bug-type equivalent 
- **Overgrow**: Grass-type equivalent
- **Blaze**: Fire-type equivalent
- **Torrent**: Water-type equivalent
- **Technician**: Different power boost mechanic
- **Sheer Force**: Alternative offensive boost ability

## Version History
- **Current**: Implemented using SWARM_MULTIPLIER macro
- **Design**: Follows established swarm ability pattern
- **Balance**: Standard 1.2x/1.5x scaling consistent with other type swarm abilities
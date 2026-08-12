---
id: 68
name: Swarm
status: reviewed
character_count: 72
---

# Swarm - Ability ID 68

## In-Game Description
"Boosts Bug-type moves by 1.2x, or 1.5x when under 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Bug-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

**SWARM** is a type-boosting ability that provides variable power increases to Bug-type moves based on the user's remaining HP.

### Activation Mechanics:
- **Trigger**: Automatically active on all Bug-type moves
- **HP Threshold**: 1/3 of maximum HP or less for enhanced boost
- **Calculation**: Checks current HP against maxHP / 3
- **Type Requirement**: Only affects Bug-type moves

### Power Multipliers:
1. **Normal State** (HP > 1/3 max):
   - Bug-type moves: 1.2x power
   
2. **Low HP State** (HP <= 1/3 max):
   - Bug-type moves: 1.5x power

### Interaction Rules:
- **Multi-hit Moves**: Each hit receives the multiplier
- **STAB Interaction**: Stacks multiplicatively with STAB (1.5x)
  - Normal: 1.2 x 1.5 = 1.8x total
  - Low HP: 1.5 x 1.5 = 2.25x total
- **Other Abilities**: Stacks with abilities like Technician, Tinted Lens, etc.
- **Items**: Stacks with type-boosting items (Silver Powder, etc.)

### Technical Implementation:
```c
#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
            else                                                             \
                MUL(1.2);                                                    \
        }                                                                    \
    }

constexpr Ability Swarm = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_BUG),
};
```

### Strategic Applications:
- **Late-Game Sweeping**: Powerful comeback potential when HP is low
- **Risk/Reward**: Encourages aggressive play to reach low HP threshold
- **Focus Sash Synergy**: Guarantees survival to 1 HP for maximum boost
- **Substitute Strategy**: Use Substitute to reach low HP safely

### Common Pokemon with Swarm:
- Various Bug-type Pokemon as innate or regular ability
- Often paired with other Bug-type enhancing abilities
- Frequently found on Pokemon with high Attack stats

### Competitive Notes:
- **Damage Calculations**: At low HP, Bug moves become incredibly powerful
- **Prediction Tool**: Opponents must respect the potential damage spike
- **Entry Hazard Synergy**: Stealth Rock damage can help reach the threshold
- **Healing Moves**: Must be careful not to heal above the threshold accidentally

### Related Abilities:
- **Overgrow**: Grass-type equivalent (ID 65)
- **Blaze**: Fire-type equivalent (ID 66) 
- **Torrent**: Water-type equivalent (ID 67)
- **BOOSTED_SWARM_MULTIPLIER**: Enhanced version used by some custom abilities

### Version History:
- Original games: 1.5x boost when HP <= 1/3
- Elite Redux: Added 1.2x base boost + 1.5x low HP boost for more consistent value
---
id: 66
name: Blaze
status: reviewed
character_count: 73
---

# Blaze - Ability ID 66

## In-Game Description
"Boosts Fire-type moves by 1.2x, or 1.5x when under 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Fire-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

**BLAZE** is one of the classic starter abilities, providing conditional offensive boosts to Fire-type moves based on the user's current HP.

### Activation Mechanics:
- **Trigger**: Every Fire-type move used by the Pokemon
- **HP Threshold**: Checks current HP vs maximum HP
- **Boost Type**: Offensive multiplier applied to move damage
- **Move Restriction**: Only affects Fire-type moves

### Damage Multipliers:
1. **Healthy State** (HP > 1/3 max):
   - Fire-type moves: 1.2x power
   - All other moves: No effect
   
2. **Critical State** (HP <= 1/3 max):
   - Fire-type moves: 1.5x power
   - All other moves: No effect

### Interaction Rules:
- **Stacking**: Multiplies with other damage modifiers (STAB, type effectiveness, items, etc.)
- **Priority**: Calculated after base power but before type effectiveness
- **Move Types**: Only affects moves that are Fire-type when used (not moves that become Fire-type)
- **Ability Changes**: If Pokemon loses Blaze mid-battle, boost is immediately removed

### Technical Implementation:
```c
constexpr Ability Blaze = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_FIRE),
};

#define SWARM_MULTIPLIER(type)
    +[](ON_OFFENSIVE_MULTIPLIER) {
        if (moveType == type) {
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3))
                MUL(1.5);
            else
                MUL(1.2);
        }
    }
```

### Competitive Applications:
- **Setup Sweeping**: Pokemon can become more dangerous as they take chip damage
- **Revenge Killing**: Critical HP state makes Fire moves extremely threatening
- **Life Orb Synergy**: Life Orb recoil can help trigger the 1.5x boost
- **Substitutes**: Sub + Blaze can create dangerous offensive pressure

### Pokemon with Blaze:
- Primary starter ability for most Fire-type starters
- Classic examples: Charizard, Blaziken, Infernape
- Works particularly well on mixed attackers and wallbreakers

### Strategic Considerations:
- **Risk vs Reward**: Taking damage to activate stronger boost
- **Prediction**: Opponents may try to knock out before critical threshold
- **Priority Moves**: Enhanced Fire priority moves become extremely dangerous
- **Coverage**: Still need non-Fire moves for type coverage

### Version History:
- Gen 3: Introduced as 1.5x boost at 1/3 HP or less
- Elite Redux: Enhanced to provide 1.2x boost at all HP levels, 1.5x at low HP
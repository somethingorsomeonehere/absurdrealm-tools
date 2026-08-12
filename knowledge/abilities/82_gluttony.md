---
id: 82
name: Gluttony
status: reviewed
character_count: 201
---

# Gluttony - Ability ID 82

## In-Game Description
"Eats berries early. Berries also restore 1/3 of max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Berries that normally activate at 1/4 HP trigger at 1/2 HP instead. Additionally, after consuming any berry, the user recovers 1/3 of max HP. Does not include berries consumed through moves like Pluck.

## Detailed Mechanical Explanation
*For Discord/reference use*

**GLUTTONY** is a dual-purpose ability that modifies berry consumption timing and provides additional healing.

### Core Mechanics:
1. **Early Berry Activation**: Berries that normally activate at 1/4 HP (25%) now activate at 1/2 HP (50%)
2. **Berry Healing**: After consuming any berry, restore 1/3 of max HP (minimum 1 HP)

### Activation Conditions:
- **Early Consumption**: Only applies to berries with hpFraction <= 4 (1/4 HP berries)
- **Bonus Healing**: Triggers after ANY berry consumption, regardless of activation threshold
- **Berry Sources**: Works with held berries, berries from Pluck, Bug Bite, and Natural Gift

### Technical Implementation:
```c
// Early berry activation check in HasEnoughHpToEatBerry()
if (hpFraction <= 4 && BattlerHasAbility(battlerId, ABILITY_GLUTTONY, FALSE) && 
    isBerry && gBattleMons[battlerId].hp <= gBattleMons[battlerId].maxHP / 2) {
    return TRUE;
}

// Bonus healing in TryCheekPouch()
if (ItemId_GetPocket(itemId) == POCKET_BERRIES && 
    BattlerHasAbility(battlerId, ABILITY_GLUTTONY, FALSE)) {
    gBattleMoveDamage = gBattleMons[battlerId].maxHP / 3;
    if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
    gBattleMoveDamage *= -1; // Negative = healing
}
```

### Affected Berries (Early Activation):
- **Healing Berries**: Sitrus Berry, Figy Berry, Wiki Berry, Mago Berry, Aguav Berry, Iapapa Berry
- **Stat Berries**: Liechi Berry, Ganlon Berry, Salac Berry, Petaya Berry, Apicot Berry, Lansat Berry, Starf Berry
- **Micle Berry**: Boosts accuracy of next move
- **Custap Berry**: Grants priority to next move

### Berry Healing Calculation:
- **Base Healing**: max HP / 3
- **Minimum**: 1 HP if calculation results in 0
- **Stacks With**: Original berry effects (e.g., Sitrus Berry heals for its normal amount PLUS 1/3 max HP)

### Interactions with Other Abilities:
- **Ripen**: Works independently - Ripen doubles berry effects, Gluttony adds separate healing
- **Harvest**: Can repeatedly trigger Gluttony's healing effect
- **Unnerve**: Prevents opponent berries from being consumed early or providing healing
- **Magic Bounce**: Does not affect Gluttony since it's not a status move

### Strategic Implications:
- **Bulk Enhancement**: Effectively increases survivability by providing emergency healing
- **Berry Synergy**: Pairs excellently with stat-boosting berries for early setup
- **Harvest Combo**: Creates sustainable healing loop with Harvest ability
- **Sitrus Stacking**: Sitrus Berry + Gluttony healing = massive HP recovery

### Example Damage Calculations:
**Scenario**: 300 HP Pokemon with Sitrus Berry at 149/300 HP
- Without Gluttony: Berry doesn't activate (needs <=75 HP)
- With Gluttony: Berry activates, heals 25% (75 HP) + 33% (100 HP) = 175 HP total

### Common Users:
- **Munchlax/Snorlax**: Natural fit for bulk-focused playstyle
- **Hariyama**: Combines with high HP for substantial healing
- **Gurdurr/Conkeldurr**: Enhances physical bulk and longevity
- **Many Custom Elite Redux Pokemon**: Various species across different types

### Competitive Usage Notes:
- **Berry Selection**: Prioritize berries with 1/4 HP activation threshold
- **Timing**: Can enable aggressive play knowing healing safety net exists
- **Team Support**: Pairs well with Pokemon that can set up entry hazards or screens

### Counters:
- **Unnerve**: Completely shuts down berry consumption
- **Magic Guard**: Prevents indirect damage but doesn't affect Gluttony
- **Knock Off**: Removes held berry before it can be consumed
- **Embargo**: Prevents item usage including berries

### Synergies:
- **Harvest**: Renewable berry consumption for repeated healing
- **Ripen**: Doubles original berry effects (healing stacks separately)
- **Recycle**: Can recover consumed berries for re-use
- **Natural Gift**: Consumes berry for attack while still triggering healing

### Version History:
- **Original Games**: Only provided early berry consumption
- **Elite Redux**: Added bonus 1/3 HP healing after berry consumption, making it significantly more valuable

### Competitive Tier Assessment:
**Utility Rating**: B+ to A-
- Excellent for bulky Pokemon and stall strategies
- Provides both offensive setup potential and defensive recovery
- Synergizes well with many team compositions
- Requires specific berry selection to maximize effectiveness
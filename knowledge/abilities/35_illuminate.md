---
id: 35
name: Illuminate
status: reviewed
character_count: 90
---

# Illuminate - Ability ID 35

## In-Game Description
"Grants a 1.2x accuracy boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's accuracy by 1.2x. Removes Ghost-typing on target when landing an attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

**ILLUMINATE** is a utility ability that provides both battle accuracy enhancement and overworld encounter rate modification.

### Battle Mechanics:
- **Trigger**: Every move used by the Pokemon with Illuminate
- **Effect**: Multiplies move accuracy by 1.2 (20% increase)
- **Calculation**: Applied as a multiplicative modifier to the move's base accuracy
- **Priority**: ACCURACY_MULTIPLICATIVE priority in the accuracy calculation chain

### Overworld Effects:
1. **Wild Encounter Rate**: 
   - Doubles the base encounter rate when the Pokemon is in the lead party slot
   - Effect: `encounterRate *= 2`
   - Applies to: Tall grass, cave encounters, surfing encounters
   - Does not stack with other encounter rate modifiers

### Accuracy Calculation Details:
- Base move accuracy is multiplied by 1.2 before other modifiers
- Examples:
  - 80% accuracy move becomes 96% accuracy (80 x 1.2)
  - 85% accuracy move becomes 102% accuracy (capped at 100%)
  - 70% accuracy move becomes 84% accuracy (70 x 1.2)
  - 90% accuracy move becomes 108% accuracy (capped at 100%)

### Interaction Rules:
- **vs Accuracy Stages**: Applied before accuracy stage multipliers
- **vs Evasion**: Applied before evasion calculations
- **vs Other Accuracy Abilities**: Stacks with other accuracy-modifying abilities
- **vs Weather**: Works independently of weather-based accuracy changes (Sand-Attack, etc.)

### Technical Implementation:
```c
constexpr Ability Illuminate = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        *accuracy *= 1.2;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

### Wild Encounter Implementation:
```c
// In wild_encounter.c
else if (ability == ABILITY_ILLUMINATE)
    encounterRate *= 2;
```

### Competitive Analysis:
- **AI Rating**: 0/10 (considered worthless by battle AI)
- **Battle Value**: Very low - minimal accuracy boost rarely decisive
- **Utility Value**: High for exploration and Pokemon hunting
- **Common Users**: Early-game Pokemon, utility Pokemon for catching

### Related Abilities:
- **Compound Eyes**: Also boosts accuracy (1.3x vs 1.2x) but no encounter rate effect
- **No Guard**: Guarantees 100% accuracy for both user and opponent
- **Keen Eye**: Prevents accuracy reduction but doesn't boost base accuracy

### Pokemon That Learn This Ability:
- Often found on Electric-type Pokemon (Lanturn line, Ampharos line)
- Some Psychic-types and light-themed Pokemon
- Typically as a hidden or secondary ability

### Practical Applications:
1. **Exploration**: Lead party member for increased wild encounters
2. **Catching**: Slight accuracy boost helpful for status moves
3. **Niche Strategies**: Minor benefit for low-accuracy high-power moves
4. **Competitive**: Generally replaced by more impactful abilities

### Version History:
- Gen 3-4: Wild encounter rate boost only
- Gen 5+: Added accuracy boost in battle
- Elite Redux: Maintains both effects with 1.2x accuracy multiplier
---
id: 182
name: Pixilate
status: reviewed
character_count: 91
---

# Pixilate - Ability ID 182

## In-Game Description
"Normal-type moves become Fairy and Fairy gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Normal-type moves become Fairy-type and they receive STAB regardless of the Pokemon's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

Pixilate is an "ate" ability that fundamentally changes how Normal-type moves function:

### Core Mechanics:
1. **Type Conversion**: All Normal-type attacking moves become Fairy-type moves
2. **Damage Boost**: Converted moves receive a 1.2x (20%) power boost
3. **STAB Interaction**: If the user is part Fairy-type, converted moves gain Same Type Attack Bonus (STAB) for an additional 1.5x multiplier

### Implementation Details:
- Uses the ATE_ABILITY macro with TYPE_FAIRY parameter
- Sets the ateBoost flag when converting moves
- Grants STAB for Fairy-type moves specifically
- Only affects damaging moves (status moves remain Normal-type)

### Calculation:
For a Fairy-type Pokemon using a converted Normal move:
- Base damage x 1.2 (Pixilate boost) x 1.5 (STAB) = 1.8x total multiplier

### Strategic Applications:
- Transforms Normal-type moves like Hyper Beam, Return, Body Slam into powerful Fairy attacks
- Excellent for Pokemon with diverse Normal-type movepools
- Particularly effective on mixed attackers that can utilize both physical and special Normal moves
- Synergizes well with high Base Power Normal moves

### Notable Interactions:
- Does not affect status moves like Thunder Wave or Sleep Powder
- Works with all Normal-type attacking moves regardless of category
- The power boost applies before STAB calculation
- Can make typically weak Normal moves viable offensive options

This ability is most commonly found on Fairy-type Pokemon like Sylveon and Mega Gardevoir, where it significantly enhances their offensive capabilities by converting their Normal-type coverage moves into STAB Fairy attacks.
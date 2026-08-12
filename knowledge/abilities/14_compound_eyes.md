---
id: 14
name: Compound Eyes
status: reviewed
character_count: 35
---

# Compound Eyes - Ability ID 14

## In-Game Description
"Grants a 1.3x accuracy boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's accuracy by 1.3x.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Compound Eyes increases the accuracy of all moves used by the Pokemon with this ability by 30% (multiplies accuracy by 1.3). This is implemented in `abilities.cc`:

```c
constexpr Ability CompoundEyes = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        *accuracy *= 1.3;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

### Battle Effects
The 30% accuracy boost makes inaccurate but powerful moves much more viable:
- **Sleep Powder**: 75% to 97.5% accuracy
- **Hurricane**: 70% to 91% accuracy  
- **Stone Edge**: 80% to 104% accuracy (capped at 100%)
- **Blizzard**: 70% to 91% accuracy
- **Thunder**: 70% to 91% accuracy
- **Focus Blast**: 70% to 91% accuracy
- **Fire Blast**: 85% to 110.5% accuracy (capped at 100%)

### Overworld Effect
When the lead Pokemon in your party has Compound Eyes:
- The chance for wild Pokemon to hold their **common item** increases from 45% to 20%
- The chance for wild Pokemon to hold their **rare item** increases from 5% to 20%

Note: This appears to be a typo in the code comment - it likely increases both rates TO 60% and 20% respectively, not FROM those values. This is a significant boost to finding held items on wild Pokemon!

### Pokemon with Compound Eyes

#### As a Changeable Ability:
1. **Weedle (Redux form)** - Ice/Poison type variant
   - Has Compound Eyes as one of three ability choices
   - Other choices: Web Spinner, Run Away

#### As an Innate Ability:
1. **Butterfree** - Bug/Psychic
   - Innates: Compound Eyes, Majestic Moth, Levitate

2. **Mega Butterfree** - Bug/Psychic
   - Innates: Compound Eyes, Shield Dust, Huge Wings

3. **Venonat** - Bug/Poison
   - Innates: Compound Eyes, Nocturnal, Magical Dust

4. **Venomoth** - Bug/Poison
   - Innates: Compound Eyes, Nocturnal, Poison Mastery

5. **Yanma** - Bug/Flying
   - Innates: Compound Eyes, Infiltrator, Buzzing Fly

6. **Yanmega** - Bug/Flying
   - Innates: Compound Eyes, Infiltrator, Buzzing Fly

7. **Dustox** - Bug/Poison
   - Innates: Compound Eyes, Nocturnal, Magical Dust

### Strategic Implications
- **Move Selection**: Enables powerful but inaccurate moves as reliable options
- **Status Moves**: Makes Sleep Powder and other status moves nearly guaranteed
- **Coverage Options**: Can run moves like Stone Edge or Focus Blast without accuracy concerns
- **Item Farming**: Excellent lead for hunting specific held items on wild Pokemon

### Common Users
Bug-type Pokemon that often have access to status moves with imperfect accuracy, turning them into much more reliable options. Butterfree with Compound Eyes + Sleep Powder is a classic combination.

### Competitive Usage Notes
- Particularly valuable on Pokemon with access to powerful but inaccurate moves
- Synergizes well with status-inducing strategies
- Can enable mixed attackers to run coverage moves they'd normally avoid
- The overworld effect makes it valuable for item collection runs

### Counters
- Abilities that prevent status (Insomnia, Vital Spirit for sleep)
- Substitute blocks status moves even with high accuracy
- Magic Bounce reflects status moves back
- Safety Goggles blocks powder moves entirely

### Synergies
- Status moves become reliable setup enablers
- Powerful coverage moves become consistent
- Sleep Powder + setup sweeper cores
- Quiver Dance after landing Sleep Powder

### Version History
The ability has maintained its 30% accuracy boost throughout generations. The overworld effect for increased held item rates was added in Generation 5 and continues in Elite Redux.
---
id: 136
name: Multiscale
status: reviewed
character_count: 120
---

# Multiscale - Ability ID 136

## In-Game Description
"At full HP, halves damage taken from attacks"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces all incoming damage by 50% when the Pokemon is at max HP. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

Multiscale is a defensive ability that provides substantial damage reduction under specific conditions:

### Core Mechanics
- **Activation Condition**: Only active when the Pokemon is at exactly 100% HP
- **Damage Reduction**: Reduces all incoming damage by 50% (multiplier of 0.5)
- **Universal Coverage**: Works against all damage types:
  - Physical moves
  - Special moves
  - Fixed damage moves
  - Multi-hit moves (only the first hit gets reduced if it brings HP below max)

### Technical Implementation
From the code in `abilities.cc`:
```cpp
.onDefensiveMultiplier =
    +[](ON_DEFENSIVE_MULTIPLIER) {
        if (BATTLER_MAX_HP(battler)) MUL(.5);
    },
.breakable = TRUE,
```

The `BATTLER_MAX_HP` check ensures the ability only triggers at full HP, and the `MUL(.5)` applies the 50% damage reduction.

### Important Properties
- **Breakable**: The ability can be suppressed by moves like Gastro Acid or abilities like Mold Breaker
- **Single-Use Per Full Heal**: Once damaged, the ability won't reactivate until the Pokemon is healed back to 100% HP
- **No Type Restrictions**: Unlike type-resist berries or other defensive abilities, Multiscale works on all move types
- **Stacks with Other Modifiers**: The 50% reduction is applied alongside other damage modifiers like type resistances, screens, or weather effects

### Strategic Considerations
- Pairs excellently with recovery moves or Leftovers/Black Sludge
- Vulnerable to chip damage from entry hazards, weather, or status conditions
- Multi-hit moves only get the reduction on the first hit
- Mold Breaker and similar abilities bypass this protection entirely

### Common Pokemon with Multiscale
While the ability distribution may vary in Elite Redux, Multiscale is typically associated with bulky Pokemon that can leverage the initial damage reduction to set up or strike back.
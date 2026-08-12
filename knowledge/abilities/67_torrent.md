---
id: 67
name: Torrent
status: reviewed
character_count: 74
---

# Torrent - Ability ID 67

## In-Game Description
"Boosts Water-type moves by 1.2x, or 1.5x when under 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Water-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

**TORRENT** is a type-boosting ability that provides conditional damage increases for Water-type moves based on the user's remaining HP.

### Activation Mechanics:
- **Trigger**: Automatic check during damage calculation for any Water-type move
- **Threshold Check**: Compares current HP to maxHP / 3 (33.33% or less)
- **Type Restriction**: Only affects Water-type moves
- **Implementation**: Uses SWARM_MULTIPLIER(TYPE_WATER) macro

### Damage Multipliers:
1. **High HP (>33% HP)**: 1.2x power to Water-type moves
2. **Low HP (<=33% HP)**: 1.5x power to Water-type moves
3. **Non-Water moves**: No effect

### Move Interactions:
- **All Water-type moves**: Subject to Torrent boost (Surf, Hydro Pump, Water Gun, etc.)
- **Hidden Power Water**: Receives boost if Hidden Power resolves to Water-type
- **Weather Ball in rain**: Gets boost since it becomes Water-type
- **Multi-type moves**: Only boosted if the move's type is Water
- **Z-moves/Max moves**: Base power is boosted before other calculations

### Ability Interactions:
- **Stacks with**: STAB (Same Type Attack Bonus), items like Mystic Water, weather effects
- **Overridden by**: Abilities that change move type (Normalize, Pixilate, etc.)
- **Works with**: Abilities that don't interfere with type or power calculation
- **Rain synergy**: Combines with rain's 1.5x Water boost for massive damage when low on HP

### Strategic Applications:
1. **Emergency sweeper**: Provides comeback potential when near defeat
2. **Consistent pressure**: 1.2x boost provides reliable damage even at high HP
3. **Starter signature**: Most Water starter lines have this as their primary ability
4. **Calculations**: At low HP with STAB in rain: 1.5 (STAB) x 1.5 (Torrent) x 1.5 (Rain) = 3.375x base power

### Technical Implementation:
```c
constexpr Ability Torrent = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_WATER),
};

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

### Notable Users:
- **Starter lines**: Squirtle, Wartortle, Blastoise, Totodile, Croconaw, Feraligatr, Mudkip, Marshtomp, Swampert, Piplup, Prinplup, Empoleon, Oshawott, Dewott, Samurott, Froakie, Frogadier, Greninja, Popplio, Brionne, Primarina, Sobble, Drizzile, Inteleon
- **Other Water-types**: Various other Water-type Pokemon as innate abilities

### Competitive Notes:
- Core ability for many Water-type sweepers and tanks
- Provides both consistency and clutch factor
- Pairs exceptionally well with rain teams
- Consider HP management to optimize between survival and damage output
- Bluff potential - opponents may be reluctant to leave Torrent users at low HP

### Version History:
- Gen 3: Introduced with 1.5x boost only when below 33% HP
- Gen 4+: Maintained same mechanics
- Elite Redux: Enhanced to provide 1.2x boost at all HP levels, 1.5x when low HP
- Elite Redux unique: Part of the "Swarm family" of abilities that provide consistent type boosts
---
id: 96
name: Normalize
status: reviewed
character_count: 130
---

# Normalize - Ability ID 96

## In-Game Description
Its moves become Normal-type, get 1.1x boost, ignore resists.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all damaging moves to Normal-type and grants a 10% power boost. Normal-type moves bypass resistances, but not immunities.

## Detailed Mechanical Explanation

### Basic Information
- **Ability ID**: 96 (ABILITY_NORMALIZE)
- **Name**: Normalize
- **Description**: Its moves become Normal-type, get 1.1x boost, ignore resists.

### Technical Details
The ability modifies three key aspects of moves:
1. **Type Change**: All damaging moves become Normal-type via `onMoveType`
2. **Power Boost**: 10% damage multiplier when `ateBoost` is active
3. **Resistance Bypass**: Normal-type moves ignore resistances (mod set to 1.0)

## Code Implementation
From `src/abilities.cc`:
```cpp
constexpr Ability Normalize = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_NORMAL && gBattleStruct->ateBoost[battler]) MUL(1.1);
        },
    .onMoveType = +[](ON_MOVE_TYPE) -> int { return TYPE_NORMAL + 1; },
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        CHECK(moveType == TYPE_NORMAL) CHECK(*mod) CHECK(*mod < UQ_4_12(1.0)) *mod = UQ_4_12(1.0);
        return TRUE;
    },
};
```

## Pokemon with Normalize
Several Pokemon have access to Normalize as a changeable ability:
- **Spearow/Fearow**: Combined with Hustle and Guts for high-risk, high-reward gameplay
- **Arceus**: Part of its versatile ability pool alongside Adaptability
- **Zygarde (10%/50%)**: Paired with Mighty Horn for physical sweeping potential
- **Flittle**: As its primary ability option
- **Magearna**: Complements its Pretty Princess ability set

## Battle Strategy
### Advantages:
- Ignores Rock and Steel resistances for consistent neutral damage
- 10% power boost on all moves provides general offensive enhancement
- Simplifies damage calculations with predictable type matchups
- Works well with high base power moves of any original type

### Disadvantages:
- Loses super effective coverage against all types
- Cannot exploit type weaknesses for bonus damage
- Vulnerable to Ghost-type immunity (no effect)
- Fighting-type moves lose their Rock/Steel breaking utility

### Synergies:
- **High Base Power Moves**: Earthquake, Close Combat become boosted Normal attacks
- **STAB Items**: Silk Scarf provides additional 20% boost to all moves
- **Scrappy**: On Arceus, allows hitting Ghost-types with Normal moves
- **Multi-hit Moves**: Each hit gets the 10% boost

## Competitive Notes
Normalize creates a unique offensive profile where consistency trumps coverage. Best suited for Pokemon with naturally high Attack stats and access to powerful moves that benefit from the guaranteed neutral damage. The ability shines against defensive cores relying on type resistances but struggles against Ghost-types and teams built around exploiting type weaknesses.

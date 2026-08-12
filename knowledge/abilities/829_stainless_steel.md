---
id: 829
name: Stainless Steel
status: reviewed
character_count: 262
---

# Stainless Steel - Ability ID 829

## In-Game Description
Steelworker + Wonder Skin.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts Normal-type moves to Steel-type and grants STAB for Steel moves regardless of typing. Additionally takes half damage from Dark and Ghost-type moves. Immune to all damage boosting ability effects from opponents, other than Parental Bond and Multi Headed.

## Detailed Mechanical Explanation

### Fort Knox Protection
- Prevents multi-hit abilities (Parental Bond, Multi-Headed, etc.) from activating when attacking this Pokemon
- Only abilities with `resistsFortKnox = TRUE` can bypass this protection
- Currently only Parental Bond and Multi-Headed can resist Fort Knox

### Steel-type Conversion (-ate ability)
- Converts all Normal-type moves to Steel-type
- Converted moves receive a 20% power boost (`ateBoost`)
- Works on all Normal-type moves including status moves (though status moves don't benefit from the power boost)
- The type change happens before damage calculation, so Steel-type effectiveness and STAB apply

### Implementation Details
From `src/abilities.cc`:
```cpp
constexpr Ability StainlessSteel = {
    ATE_ABILITY(TYPE_STEEL),
    .fortKnox = TRUE,
};
```

The `ATE_ABILITY` macro handles the type conversion:
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },
```

### Strategic Uses
- Excellent on Steel-types for STAB on converted Normal moves
- Strong defensive ability against common multi-hit strategies
- Pairs well with high-powered Normal moves like Return, Extreme Speed, or Boomburst
- The Fort Knox effect makes it valuable against teams relying on Parental Bond sweepers

### Notes
- Despite the description mentioning "Wonder Skin", this ability only inherits Wonder Skin's Fort Knox property, not any accuracy-related effects
- The Fort Knox protection is checked before applying multi-hit effects in battle calculations
- This is one of the few abilities that combines both defensive utility and offensive type conversion
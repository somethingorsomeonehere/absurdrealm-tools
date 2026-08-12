---
id: 297
name: Amphibious
status: reviewed
character_count: 106
---

# Amphibious - Ability ID 297

## In-Game Description
"Water moves gain STAB. Can't become drenched."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants STAB to Water-type moves regardless of the user's typing. Also provides immunity to being drenched.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **STAB Grant**: All Water-type moves used by this Pokemon receive Same Type Attack Bonus (STAB), multiplying their power by 1.5x regardless of the user's actual typing
- **Drench Immunity**: Complete immunity to the "drenched" status condition inflicted by Venom Drench

### Technical Implementation
```cpp
constexpr Ability Amphibious = {
    .onStab = +[](ON_STAB) -> int { return moveType == TYPE_WATER; },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_DRENCH)
        return TRUE;
    },
};
```

### STAB Mechanics
- Applies the standard 1.5x power multiplier to Water moves
- Functions identically to natural STAB from Pokemon's actual typing
- Stacks additively with other damage bonuses (items, weather, etc.)
- Does not interfere with the Pokemon's natural STAB from their actual types

### Drench Immunity Details
- **Venom Drench**: A Poison-type status move that targets both foes, requiring the target to be poisoned
- **Drench Effect**: Reduces Attack, Special Attack, and Speed by 1 stage each when successfully applied
- **Immunity Scope**: Complete immunity to the stat reductions; the move will fail against Amphibious users

### Activation Conditions
- **STAB**: Automatically applies to any Water-type move used by the Pokemon
- **Immunity**: Automatically prevents drench status when targeted by Venom Drench

### Common Users
- **Eiscue (No Ice Face form)**: Ice-type Pokemon that gains Water STAB
- **Various Water/Poison types**: Natural synergy with Water moves and poison immunity themes
- **Mixed-type Pokemon**: Non-Water types that benefit from Water move coverage

### Strategic Applications
- **Coverage Expansion**: Allows non-Water types to use Water moves effectively
- **Offensive Versatility**: 1.5x boost makes Water moves viable attacking options
- **Status Immunity**: Protection against specific stat reduction strategies
- **Team Role Flexibility**: Enables Pokemon to fill Water-type offensive roles regardless of typing

### Competitive Analysis
**Strengths:**
- Immediate power boost to all Water moves
- Expands movepool viability for non-Water types  
- Specific but valuable status immunity
- No activation requirements or conditions

**Limitations:**
- Only affects Water-type moves
- Drench immunity is highly situational
- Doesn't provide defensive benefits beyond one status
- Requires good Water move coverage to be effective

### Damage Calculations
```
Base Water Move Power x 1.5 (STAB) x Other Modifiers = Final Power

Example: Hydro Pump (110 BP)
- Without Amphibious: 110 BP
- With Amphibious: 110 x 1.5 = 165 BP effective power
```

### Interactions
- **Other STAB**: Stacks with natural STAB if Pokemon is already Water-type (1.5x x 1.5x = 2.25x total)
- **Abilities**: Works with other damage-boosting abilities (Tough Claws, Sheer Force, etc.)
- **Items**: Stacks with type-boosting items like Mystic Water
- **Weather**: Combines with Rain's Water move boost for massive damage

### Counters
- **Type Resistances**: Steel, Water, Grass, and Dragon types resist Water moves
- **Abilities**: Water Absorb, Storm Drain, Dry Skin negate Water attacks entirely
- **Non-Water Movesets**: Ability provides no benefit if Pokemon lacks Water moves

### Synergies
- **Rain Teams**: Excellent synergy with Rain Dance for 1.5x + 1.5x = 2.25x Water move power
- **Mixed Attackers**: Allows physical or special Water moves to hit hard
- **Coverage Moves**: Surf, Scald, Hydro Pump become viable on any Pokemon
- **Poison Types**: Natural thematic fit with drench immunity

### Version History
- Added as part of Elite Redux's expanded ability system
- Designed to provide Water-type offensive capability to non-Water Pokemon
- Drench immunity added as a thematic bonus fitting the "amphibious" concept
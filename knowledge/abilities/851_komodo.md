---
id: 851
name: Komodo
status: reviewed
character_count: 271
---

# Komodo - Ability ID 851

## In-Game Description
"Adds Dragon-type + moves have 30% Bad Poison chance."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Dragon to the user's current typing. Retains Dragon typing even upon losing the ability, going away only when switching out. The user has a 30% to badly poison the target after landing any move. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation

### Component Abilities
Komodo combines two existing ability effects:
- **HalfDrake.onEntry**: Adds Dragon type to the Pokemon
- **ToxicChain.onAttacker**: 30% chance to inflict bad poison on hit

### Code Analysis
```cpp
constexpr Ability Komodo = {
    .onEntry = HalfDrake.onEntry,
    .onAttacker = ToxicChain.onAttacker,
};
```

### HalfDrake Component
- **Function**: `AddBattlerType(battler, TYPE_DRAGON)`
- **Effect**: Adds Dragon as an additional type
- **Timing**: On switch-in (onEntry)
- **Permanent**: Lasts until the Pokemon switches out

### ToxicChain Component  
- **Function**: 30% chance to apply `MOVE_EFFECT_TOXIC`
- **Conditions**: 
  - Move must hit and deal damage (`ShouldApplyOnHitAffect`)
  - Target must be able to be poisoned (`CanBePoisoned`)
  - 30% random chance succeeds
- **Status Applied**: `STATUS1_TOXIC_POISON` (bad poison)
- **Timing**: After successful offensive moves (onAttacker)

## Bad Poison Mechanics
- **Turn 1**: 1/16 max HP damage
- **Turn 2**: 2/16 max HP damage  
- **Turn 3**: 3/16 max HP damage
- **Turn N**: N/16 max HP damage
- **Maximum**: Caps at 15/16 max HP damage per turn
- **Differs from regular poison**: Regular poison deals constant 1/8 max HP each turn

## Interactions
- **Type Addition**: Dragon type stacks with existing types (dual becomes triple, etc.)
- **STAB Bonus**: Dragon-type moves gain Same Type Attack Bonus if Pokemon uses them
- **Type Effectiveness**: Pokemon gains Dragon type weaknesses (Ice, Dragon, Fairy) and resistances
- **Poison Immunity**: Steel and Poison types cannot be badly poisoned
- **Ability Immunity**: Pokemon with poison-immunity abilities are unaffected
- **Contact Requirement**: Works with all offensive moves, not just contact moves

## Strategic Applications
- **Offensive Utility**: Reliable status infliction on any offensive moveset
- **Type Coverage**: Dragon typing provides offensive and defensive benefits
- **Stall Potential**: Bad poison creates significant pressure over time
- **Multi-Type Synergy**: Works well with Pokemon that can utilize Dragon STAB
---
id: 298
name: Grounded
status: reviewed
character_count: 140
---

# Grounded - Ability ID 298

## In-Game Description
"Adds Ground type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grounded adds Ground type to the Pokemon upon entry. Retains Ground typing even upon losing the ability, going away only when switching out. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Grounded is a type-addition ability that triggers upon the Pokemon entering battle. It adds Ground type to the battler's type combination using the game's third type slot (`type3`).

### Activation Conditions
- Triggers automatically when the Pokemon enters battle
- Only activates if the Pokemon doesn't already have Ground typing
- Cannot be suppressed or negated by most ability-suppressing effects

### Technical Implementation
```cpp
constexpr Ability Grounded = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_GROUND); },
};

static int AddBattlerType(int battler, int type) {
    CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))
    
    gBattleMons[battler].type3 = type;
    PREPARE_TYPE_BUFFER(gBattleTextBuff2, gBattleMons[battler].type3);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAddedTheType);
    return TRUE;
}
```

The ability uses the game's third type slot (`type3`) to add Ground typing. The type effectiveness system recognizes this additional typing using the `IS_BATTLER_OF_TYPE` macro, which checks all three type slots.

### Type Effectiveness Changes
**Gained Immunities:**
- Electric-type moves (0x damage)

**Gained Resistances:**
- Poison-type moves (0.5x damage)
- Rock-type moves (0.5x damage)

**Gained Weaknesses:**
- Water-type moves (2x damage)
- Grass-type moves (2x damage)
- Ice-type moves (2x damage)

### STAB Bonus
Grounded Pokemon gain Same Type Attack Bonus (STAB) on Ground-type moves:
- Ground moves receive 1.5x damage multiplier
- Applies to both physical and special Ground moves

### Battle Message
When activated, displays: "[Pokemon] added the [Ground] type!"

### Affected Pokemon
**Primary Users (Main Ability):**
- Turtwig line (Turtwig, Grotle) - Grass to Grass/Ground
- Skorupi - Poison/Bug to Poison/Bug/Ground

**Secondary Users (Innate Ability):**
- Dodrio line - Normal/Flying to Normal/Flying/Ground
- Archeops - Rock/Flying to Rock/Flying/Ground
- Various Steel-types in legendary forms

### Strategic Implications

**Synergy with Other Abilities:**
- **Earthbound**: Provides 1.2x boost to Ground moves (1.5x under 1/3 HP), stacking with STAB
- **Tectonize**: Converts Normal moves to Ground type, gaining STAB from Grounded
- **Sand abilities**: Ground types are immune to sandstorm damage

**Optimal Usage:**
1. **Flying-type Coverage**: Eliminates Electric weakness while maintaining Flying advantages
2. **Grass Synergy**: Turtwig line gains defensive utility against Electric attacks
3. **Offensive Potential**: Enables Ground move STAB for coverage moves

**Competitive Applications:**
- **Dodrio**: Transforms from Normal/Flying to Normal/Flying/Ground, eliminating Electric weakness
- **Turtwig line**: Provides early-game Electric immunity and Ground STAB
- **Steel types**: Adds utility typing without major defensive drawbacks

### Interactions with Other Mechanics

**Ability Interactions:**
- **Levitate**: Grounded Pokemon with Levitate maintain Ground immunity despite being Ground-type
- **Air Balloon**: Can still be held to provide Ground immunity
- **Magnet Rise**: Can still be used to gain temporary Ground immunity

**Move Interactions:**
- **Earthquake/Magnitude**: Grounded Pokemon take damage from these moves unless they have Levitate or are airborne
- **Spikes**: Grounded Pokemon are affected by entry hazards on the ground
- **Arena Trap**: Can trap Grounded Pokemon that don't have Flying type or Levitate

### Counters and Limitations

**Ability Counters:**
- **Mold Breaker**: Cannot suppress Grounded as it's not a defensive ability
- **Role Play/Skill Swap**: Can remove Grounded, but the added typing remains
- **Gastro Acid**: Can suppress Grounded but doesn't remove already-added typing

**Strategic Counters:**
- Water-type moves for super effective damage
- Grass-type moves for coverage
- Ice-type moves for neutral/super effective damage

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Functions similarly to other type-adding abilities like Turboblaze (Fire) and Teravolt (Electric)
- Part of the broader type-manipulation ability family

### Competitive Usage Notes
**Tier Rankings:**
- Most effective on Flying-types that lose Electric weakness
- Moderate effectiveness on single-typed Pokemon gaining coverage
- Situational on dual-types that may gain unwanted weaknesses

**Common Team Roles:**
- **Dodrio**: Offensive pivot with Electric immunity
- **Turtwig**: Defensive wall with Ground STAB
- **Archeops**: Mixed attacker with Ground coverage

**Usage Statistics:**
- Popular on teams requiring Electric immunity
- Commonly paired with Earthbound for Ground offense
- Effective in formats with prevalent Electric attacks
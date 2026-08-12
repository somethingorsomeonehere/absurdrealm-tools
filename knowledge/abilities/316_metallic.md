---
id: 316
name: Metallic
status: reviewed
character_count: 149
---

# Metallic - Ability ID 316

## In-Game Description
"Adds Steel type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Steel to the user's current typing. Retains Steel typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation

### Overview
Metallic is a defensive utility ability that grants the holder an additional Steel typing upon switching into battle. This creates a triple-type Pokemon, combining the defensive benefits of Steel typing with the offensive capabilities of the Pokemon's original dual typing.

### Basic Information
- **ID**: 316 (ABILITY_METALLIC)
- **Name**: Metallic
- **Category**: Type Addition Ability
- **Breakable**: No
- **Trigger**: On Entry (when Pokemon switches in)

### Mechanics

### Core Functionality
```cpp
constexpr Ability Metallic = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_STEEL); },
};
```

### How It Works
1. **Activation**: Triggers automatically when the Pokemon enters battle (switching in)
2. **Type Addition**: Uses the `AddBattlerType(battler, TYPE_STEEL)` function
3. **Storage**: The Steel type is stored in `gBattleMons[battler].type3`
4. **Check**: Only activates if the Pokemon doesn't already have Steel typing (`CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))`)
5. **Message**: Displays battle message about gaining the Steel type

### Type System Integration
- **Triple Typing**: Creates a Pokemon with three types (original two + Steel)
- **Preservation**: Original typing remains unchanged (type1 and type2 intact)
- **STAB**: Retains Same Type Attack Bonus for original moves
- **Resistances**: Gains all Steel-type resistances and immunities
- **Weaknesses**: Gains Steel-type weaknesses (Fire, Fighting, Ground)

## Steel Type Benefits

### Resistances (0.5x damage)
- Normal
- Flying  
- Rock
- Bug
- Steel
- Grass
- Psychic
- Ice
- Dragon
- Fairy

### Immunity (0x damage)
- Poison (both damage and status)

### Weaknesses (2x damage)
- Fire
- Fighting  
- Ground

## Strategic Applications

### Defensive Utility
- **Frail Attackers**: Provides defensive bulk to glass cannon Pokemon
- **Status Immunity**: Complete immunity to poison damage and poisoning
- **Resistances**: Significant damage reduction from 10 common types
- **Typing Coverage**: Shores up defensive weaknesses without losing offensive options

### Offensive Preservation  
- **STAB Retention**: Maintains 1.5x damage bonus for original typing moves
- **Coverage Moves**: Original typing determines move effectiveness calculations
- **Versatility**: Triple typing provides unique resistance profile

### Team Building
- **Role Flexibility**: Allows offensive Pokemon to pivot into defensive roles
- **Matchup Coverage**: Improves neutral matchups into favorable ones
- **Synergy**: Pairs well with moves that benefit from type diversity

## Comparison to Similar Abilities

### Type Addition Abilities
- **Turboblaze**: Adds Fire type (ID varies)
- **Teravolt**: Adds Electric type (ID varies)  
- **Grounded**: Adds Ground type (ID varies)
- **IceAge**: Adds Ice type (ID varies)
- **HalfDrake**: Adds Dragon type (ID varies)
- **Aquatic**: Adds Water type (ID varies) 
- **Phantom**: Adds Ghost type (ID varies)
- **FairyTale**: Adds Fairy type (ID varies)
- **Hover**: Adds Psychic type (ID varies)
- **LightningBorn**: Adds Electric type (ID varies)

### Unique Features
- **Steel Focus**: Only ability that adds Steel typing specifically
- **Defensive Emphasis**: Steel provides more resistances than most other types
- **Poison Immunity**: Unique among type-addition abilities for complete poison immunity

## Implementation Details

### Function Call Chain
1. `onEntry` trigger fires when Pokemon switches in
2. `AddBattlerType(battler, TYPE_STEEL)` called
3. `IS_BATTLER_OF_TYPE` check prevents duplicate typing
4. `gBattleMons[battler].type3 = TYPE_STEEL` stores the new type
5. `BattleScript_BattlerAddedTheType` displays message

### Battle Script Integration
- Uses `BattleScript_BattlerAddedTheType` for message display
- Text buffer prepared with `PREPARE_TYPE_BUFFER`
- Integrates with standard battle message system

### Type Checking System
- `IS_BATTLER_OF_TYPE(battler, type)` macro checks all three type slots
- `type3` serves as the additional typing slot
- Standard type effectiveness calculations include all three types

## Code References

### Primary Implementation
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: Search for "constexpr Ability Metallic"
- **Function**: Uses `AddBattlerType` helper function

### Related Files
- **Constants**: `/Users/joel/Github/eliteredux/eliteredux-source/include/generated/constants/abilities.h`
- **Protobuf**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityList.textproto`

### Battle Scripts
- **Message Script**: `BattleScript_BattlerAddedTheType`
- **Text Preparation**: `PREPARE_TYPE_BUFFER` macro

## Related Abilities

### Metallic Jaws (ID: 792)
```cpp
constexpr Ability MetallicJaws = {
    .onEntry = Metallic.onEntry,
    .onParentalBond = PrimalMaw.onParentalBond,
};
```
Combination ability that includes Metallic's type addition plus Primal Maw's multi-hit effect.

## Conclusion
Metallic is a straightforward but powerful defensive utility ability that transforms any Pokemon into a Steel-type hybrid. Its value lies in providing significant defensive improvements while preserving all offensive capabilities, making it particularly valuable for fragile offensive Pokemon that need survivability without sacrificing their role as attackers.
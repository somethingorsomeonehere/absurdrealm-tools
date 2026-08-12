---
id: 324
name: Phantom
status: reviewed
character_count: 145
---

# Phantom - Ability ID 324

## In-Game Description
"Adds Ghost type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Ghost to user's current typing. Retains Ghost typing even upon losing the ability, going away only when switching out.

## Mechanics

### Core Functionality
- **Trigger**: On entry into battle (`onEntry`)
- **Effect**: Adds Ghost-type as the Pokemon's third type using `AddBattlerType(battler, TYPE_GHOST)`
- **Type Storage**: Uses the `type3` field in the battler's data structure
- **Battle Message**: Displays "{Pokemon} added the Ghost-type!" when activated

### Technical Implementation
```cpp
constexpr Ability Phantom = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_GHOST); },
};
```

### Key Mechanics
1. **Type Addition**: Adds Ghost as a third type without replacing existing types
2. **Immunity Check**: Before adding the type, checks if the Pokemon already has Ghost-type
3. **Battle Display**: Shows a message when the type is successfully added
4. **Permanent Effect**: The Ghost-type remains for the duration of the battle

## Battle Effects

### Defensive Benefits
- **Normal-type Immunity**: Immune to all Normal-type attacks
- **Fighting-type Immunity**: Immune to all Fighting-type attacks
- **Status Move Interactions**: Can be affected by moves that specifically target Ghost-types

### Offensive Benefits
- **STAB Retention**: Keeps STAB (Same Type Attack Bonus) for original types
- **Ghost STAB**: Gains STAB for Ghost-type moves if the Pokemon learns any
- **Triple Coverage**: Can potentially have STAB on three different types

### Strategic Considerations
- **Weakness Addition**: May gain new weaknesses (Ghost is weak to Ghost and Dark)
- **Resistance Changes**: Ghost resists Poison and Bug attacks
- **Move Interactions**: Affects how certain moves interact with the Pokemon

## Similar Abilities
Phantom is part of a family of type-adding abilities that all use the same `AddBattlerType` function:

- **Turboblaze**: Adds Fire-type
- **Teravolt**: Adds Electric-type  
- **Grounded**: Adds Ground-type
- **Ice Age**: Adds Ice-type
- **Half Drake**: Adds Dragon-type
- **Aquatic**: Adds Water-type
- **Metallic**: Adds Steel-type
- **Fairy Tale**: Adds Fairy-type
- **Hover**: Adds Psychic-type
- **Lightning Born**: Adds Electric-type

## Usage Examples

### Effective Combinations
1. **Fire/Flying + Ghost**: Gains immunity to Normal/Fighting while keeping Fire/Flying benefits
2. **Psychic + Ghost**: Creates a powerful special attacker with multiple immunities
3. **Steel + Ghost**: Combines Steel's resistances with Ghost's immunities

### Strategic Applications
- **Wall Breaking**: Ghost typing can help bypass Normal-type walls
- **Pivot Pokemon**: Immunity to common priority moves (like Extreme Speed)
- **Coverage Options**: Opens up Ghost-type move pools for additional coverage

## Code References
- **Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` lines 3447-3449
- **Registry**: Line 9169 in the ability mapping table
- **Helper Function**: `AddBattlerType` function at line 218
- **Battle Message**: `sText_BattlerAddedTheType` in `battle_message.c`
- **Data Entry**: `proto/AbilityList.textproto` lines 1624-1628

## Notes
- The ability only activates once per battle entry
- Does not work if the Pokemon already has Ghost-type
- The type addition is permanent for the duration of the battle
- Can create unique triple-type combinations not found naturally in the game
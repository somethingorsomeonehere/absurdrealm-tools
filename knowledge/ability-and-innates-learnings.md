# Ability and Innates System Knowledge

This file documents general learnings about how the ability and innate system works in Elite Redux.

## Core System Architecture

### 4-Ability System Overview
- **1 Changeable Ability**: Stored in regular ability slot, can be changed among up to 3 choices
- **3 Fixed Innate Abilities**: Always active, stored separately from changeable ability
- Implementation primarily in `src/abilities.cc` and battle engine files

### Key Implementation Files
- `src/abilities.cc` - Main ability implementation and logic
- `proto/AbilityList.textproto` - Ability data, names, descriptions
- `src/battle_util.c` - Battle mechanics integration
- `src/battle_script_commands.c` - Battle effects and triggers
- `include/battle.h` - Battle constants and enums

## System Mechanics Patterns

### Common Ability Triggers
- **onParentalBond**: Used for multi-hit abilities
- **Weather-based triggers**: Check weather conditions using `IsBattlerWeatherAffected()`
- **Type-based triggers**: Check move types with `moveType == TYPE_X`

### Battle Integration Points
- **Multi-hit handling**: `GetParentalBondCount()` in `battle_script_commands.c` determines hit counts
- **Damage multipliers**: `GetParentalBondMultiplier()` in `battle_util.c` sets damage for each hit
- **Weather immunity**: Properties like `.hailImmune = TRUE` grant weather damage immunity
- **Ability hooks**: Various hooks in the Ability struct (onParentalBond, onModifyDamage, etc.)

### Parental Bond Damage Multipliers (from GetParentalBondMultiplier)
- **Default/Unlisted**: 100% damage on all hits
- **HYPER_AGGRESSIVE**: 25% on second hit
- **THREE_HEADED**: 20% on second hit, 15% on third hit
- **MINION_CONTROL**: 10% on second hit
- **PRIMAL_MAW**: 40% on second hit
- **DUAL_WIELD**: 70% on both hits

### Data Storage Structure
- **Ability definitions**: Defined as `constexpr Ability` structs in `src/abilities.cc`
- **Ability IDs**: Auto-generated from `proto/AbilityList.textproto` during compilation
- **Ability registration**: Abilities array at the end of `abilities.cc` maps IDs to implementations
- **MultihitType enum**: Used for categorizing different multi-hit behaviors
- **Generated enums**: The ability enum is NOT manually maintained - it's generated from proto files

## Analysis Methodology

When analyzing abilities with `/project:analyze-ability`:
1. Always verify through actual code implementation, never trust descriptions alone
2. Track exact numerical values (percentages, multipliers, calculations)
3. Document trigger conditions and battle state interactions
4. Note any special cases or conditional behavior
5. Individual ability documentation goes in `knowledge/abilities/{ability_id}_{ability_name}.md`

## Critical Verification Requirements

### Elite Redux Data Verification
- **Never assume vanilla Pokemon facts** - Elite Redux has extensive changes
- **Typing**: Check `proto/SpeciesList.textproto` for actual types
- **Abilities**: Verify from species data, not vanilla assumptions  
- **Stats**: Elite Redux has modified base stats for many Pokemon
- **Examples in documentation**: Must use Elite Redux data, not vanilla Pokemon
- Common changes include type modifications, ability distributions, stats/BSTs

## General Insights

### Ability Implementation Patterns
- Abilities use a struct-based system with various function pointers for different battle events
- The `onParentalBond` hook is commonly used for multi-hit abilities, not just Parental Bond itself
- Weather-based abilities often include immunity to that weather's damage as a bonus effect

### Code Organization
- **Ability IDs**: Defined in `proto/AbilityList.textproto` with format `ABILITY_NAME = number`
- **Enum Generation**: Ability enum is auto-generated from proto files during compilation (not manually maintained)
- **Implementation**: All ability logic is in `src/abilities.cc` using constexpr structs
- **Registration**: End of `abilities.cc` contains the master abilities array mapping IDs to implementations
- **Battle Integration**: `src/battle_script_commands.c` handles multi-hit counts and special cases

### Analysis Best Practices
- Always check both the ability struct AND any referenced functions (like GetParentalBondCount)
- For multi-hit abilities, ALSO check `GetParentalBondMultiplier()` in `battle_util.c` for damage modifiers
- Look for enum definitions in header files when abilities reference special types
- Weather and type checks are common patterns - verify the exact conditions
- Multi-hit abilities often use the Parental Bond framework even if not related to Parental Bond
- Different Parental Bond variants have different damage multipliers (not all are 25% like regular Parental Bond)

## Weather System Learnings

### Weather Duration Constants
- **WEATHER_DURATION**: 8 turns (standard weather duration in Elite Redux)
- **WEATHER_DURATION_EXTENDED**: 12 turns (with weather-extending rocks)
- Defined in `include/battle_util.h`

### Weather Implementation Pattern
Weather abilities follow a consistent pattern:
```c
constexpr Ability WeatherAbility = {
    .onEntry = +[](ON_ENTRY) -> int {
        if (TryChangeBattleWeather(battler, ENUM_WEATHER_X, TRUE)) {
            BattleScriptPushCursorAndCallback(BattleScript_WeatherActivates);
            return TRUE;
        } else if (gBattleWeather & WEATHER_PRIMAL_ANY && WEATHER_HAS_EFFECT) {
            BattleScriptPushCursorAndCallback(BattleScript_BlockedByPrimalWeatherEnd3);
            return NO_ANNOUNCE;
        }
        return FALSE;
    },
};
```

### Weather Mechanics
- **TryChangeBattleWeather()**: Core function in `src/battle_util.c` that handles weather changes
- **Parameters**: (battler, weatherEnumId, viaAbility)
  - viaAbility = TRUE for abilities, FALSE for moves
- **Weather rocks**: Checked via `GetBattlerHoldEffect()` for extending duration
- **Primal weather**: Cannot be overridden by normal weather abilities/moves
- **NO_ANNOUNCE**: Special return value that prevents ability announcement when blocked

### Weather Flags Structure
- Weather info stored in `sWeatherFlagsInfo` array with format:
  - [0]: Temporary weather flag
  - [1]: Permanent weather flag  
  - [2]: Associated hold effect for extension (e.g., HOLD_EFFECT_DAMP_ROCK)

### Script Execution
- Weather abilities push specific battle scripts (e.g., `BattleScript_DrizzleActivates`)
- Scripts handle the message display and animation
- Primal weather block has its own script for failure messages

## GBA UI Constraints for Extended Descriptions

### Physical Display Limits (Confirmed June 2025)
- **Total visible lines**: 14 (including blank lines)
- **Recommended blank lines**: 3 (for readability on longer texts)
- **Usable text lines**: 11 (14 - 3 blank)
- **Max characters per line**: 30 (safe limit to avoid word-wrap issues)
- **Absolute character ceiling**: 330 (11 × 30)
- **Practical target**: 280-300 characters total

### Writing Guidelines
- Keep descriptions between 280-300 characters
- Prioritize essential mechanics over flavor text
- Use abbreviations where clear (e.g., "dmg" for damage)
- Avoid complex punctuation that wastes characters
- Test mentally: ~30 chars per line × 11 lines
- Remember: codegen handles line wrapping automatically

## Type-Based Ability Patterns

### Pokémon Type vs Move Type Abilities
Some abilities check the Pokémon's type rather than move types:
- Uses `IS_BATTLER_OF_TYPE(battler, TYPE_X)` macro
- Affects all moves from/to that Pokémon type, not specific move types
- This pattern is distinct from move-type-based abilities like Filter

### Type Checking Macros
- `IS_BATTLER_OF_TYPE(battlerId, type)`: Checks if a Pokémon has a specific type
  - Checks all three type slots (type1, type2, type3)
  - Returns true if ANY type matches
- Located in `include/battle.h`

## Primal Weather System

### Primal Weather Types
- **WEATHER_RAIN_PRIMAL** (Heavy Rain - Primordial Sea)
- **WEATHER_SUN_PRIMAL** (Extremely Harsh Sunlight - Desolate Land)  
- **WEATHER_STRONG_WINDS** (Strong Winds - Delta Stream)

### Primal Weather Properties
- **Duration**: Permanent until ability user switches out or faints
- **Priority**: Cannot be overridden by regular weather moves/abilities
- **Override Rules**: Only other primal weather can replace active primal weather
- **Weather Items**: No effect on primal weather duration
- **Suppression**: Cloud Nine/Air Lock cannot suppress primal weather

### Type Move Nullification
- **Primordial Sea**: Nullifies ALL damaging Fire-type moves (PP consumed, then fails)
- **Desolate Land**: Nullifies ALL damaging Water-type moves (PP consumed, then fails)
- **Delta Stream**: Blocks weather-based moves via `onImmune` hook (FLAG_WEATHER_BASED)

## Terrain System

### Terrain Duration
- **Base Duration**: 8 turns in Elite Redux (not 5 like vanilla)
- **Extended Duration**: 12 turns with Terrain Extender item
- **Override**: Only one terrain can be active at a time

### Terrain Power Boosts
- **Electric Terrain**: Electric moves get 1.5x (50%) boost
- **Grassy Terrain**: Grass moves get 1.5x (50%) boost
- **Psychic Terrain**: Psychic moves get 1.3x (30%) boost
- All boosts only apply to grounded Pokémon

### Elite Redux Specific Changes
- **Grassy Terrain**: Does NOT reduce Earthquake/Bulldoze damage (modifier is 1.0)
- **Weather Durations**: All weather lasts 8 turns base (not 5)
- **Terrain Durations**: All terrains last 8 turns base (not 5)

### Grounded Pokémon Definition
Affected by terrain if ALL are true:
- Not Flying-type (unless using Roost)
- Not having Levitate ability
- Not using Magnet Rise or Telekinesis
- Not holding Air Balloon
- OR under effect of Gravity/Smack Down

## Fort Knox System

### Fort Knox Mechanics
Fort Knox is a defensive ability that blocks offensive ability multipliers:
- **Blocks**: All abilities using `onOffensiveMultiplier` hook (~158 abilities)
- **Blocks**: All abilities using `onParentalBond` hook (multi-hit abilities)
- **Exception**: Parental Bond bypasses Fort Knox via `resistsFortKnox = TRUE`

### Implementation Pattern
```cpp
// Simple ability definition
constexpr Ability FortKnox = {
    .fortKnox = TRUE,
};

// Bypass mechanism
constexpr Ability ParentalBond = {
    .onParentalBond = /*...*/,
    .resistsFortKnox = TRUE,  // Allows bypassing Fort Knox
};
```

### Blocking Points
1. **CalculateAbilityMultipliers()**: Checks `HasFortKnox(battlerDef)` before applying offensive multipliers
2. **GetParentalBondType()**: Checks Fort Knox and resistsFortKnox flag for multi-hits

### Categories Blocked
- Type-based boosts (Overgrow, Blaze, -ate abilities)
- Stat multipliers (Huge Power, Hustle, Guts)
- Move-type boosts (Iron Fist, Strong Jaw, Technician)
- Weather/terrain boosts (Sand Force, etc.)
- Multi-hit abilities (except Parental Bond)

## Weather-Based Moves (FLAG_WEATHER_BASED)

### Definition
"Weather-based moves" refers to a specific set of 18 moves flagged with `FLAG_WEATHER_BASED`:
- **Not** moves that benefit from weather (e.g., Water moves in rain)
- **Not** moves that set weather (Rain Dance, Sunny Day)
- **Specifically** 18 hardcoded moves: Bleakwind Storm, Blizzard, Depletion Beam, Eerie Spell, Fire/Water/Grass Pledge, Hurricane, Ominous Wind, Revival Blessing, Sandsear Storm, Sheer Cold, Solar Beam/Blade, Springtide Storm, Thunder, Weather Ball, Wildbolt Storm

### Immunity Abilities
- **Weather Control**: Blocks all 18 weather-based moves from opponents via `onImmune` hook
- **Delta Stream**: Same immunity PLUS sets Strong Winds weather
- Shows "It doesn't affect..." message when blocked
- Can be bypassed by Mold Breaker (if ability has `.breakable = TRUE`)

## Form Change Abilities

### Form Change Pattern
Abilities that change a Pokémon's form (e.g., Gulp Missile, Stance Change):
- Use `UpdateAbilityStateIndicesForNewSpecies()` to properly update ability tracking
- Directly modify `gBattleMons[battler].species` for the form change
- Often use `BattleScriptCall(BattleScript_AttackerFormChange)` for visual update
- Can have different triggers (onAttacker for offensive, onDefender for defensive)

### Implementation Elements
- Check for transformed status (prevent Ditto usage)
- Verify specific species before form change
- Use `UpdateAbilityStateIndicesForNewSpecies()` for proper tracking
- Modify `gBattleMons[battler].species` directly
- Call appropriate battle script for visual update

### Ability Properties
- **unsuppressable**: Cannot be suppressed by Neutralizing Gas or similar effects
- **randomizerBanned**: Not available in randomizer modes (used for extremely complex/powerful abilities)
- **acceleratedTwoTurn**: Special handling for two-turn moves like Dive
- Species checks prevent transformed Pokémon (e.g., Ditto) from using form changes

## Complex Ability Patterns

### Multi-Effect Abilities
- Often use `randomizerBanned = TRUE` to prevent random assignment
- Type-based abilities check `moveType` for move's type, not Pokémon's type
- Use extensive CHECK() validation for each effect branch
- `AbilityStatusEffect()` function handles most status inflictions uniformly
- Terrain effects use `TryChangeBattleTerrain()` for consistent implementation
- Switch statements on `moveType` for type-based branching logic
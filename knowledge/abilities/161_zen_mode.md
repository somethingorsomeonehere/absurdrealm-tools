---
id: 161
name: Zen Mode
status: reviewed
character_count: 39
---

# Zen Mode - Ability ID 161

## In-Game Description
"Transforms into Zen Mode on entry until end of battle."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Triggers form change upon battle entry. 

## Detailed Mechanical Explanation

### Core Mechanics
```cpp
constexpr Ability ZenMode = {
    .onEntry = Forecast.onEntry,
    .onEndTurn = Forecast.onEndTurn,
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

### Key Features
1. **Uses Forecast Implementation**: Shares the same transformation logic as Forecast ability
2. **Unsuppressable**: Cannot be disabled by abilities like Mold Breaker
3. **Randomizer Banned**: Excluded from randomization due to form-specific nature
4. **Battle Entry Trigger**: Activates immediately when entering battle

### Transformation Logic
Located in `src/battle_util.c` in `ShouldChangeFormHpBased()`:

```cpp
// Darmanitan
if (species == SPECIES_DARMANITAN && (BattlerHasAbility(battler, ABILITY_ZEN_MODE, FALSE)) && gBattleMons[battler].hp != 0) {
    gBattleScripting.abilityPopupOverwrite = ABILITY_ZEN_MODE;
    gBattlerAttacker = battler;
    UpdateAbilityStateIndicesForNewSpecies(gActiveBattler, SPECIES_DARMANITAN_ZEN_MODE);
    gBattleMons[battler].species = SPECIES_DARMANITAN_ZEN_MODE;
    return TRUE;
}

// Darmanitan Galarian
if (species == SPECIES_DARMANITAN_GALARIAN && (BattlerHasAbility(battler, ABILITY_ZEN_MODE, FALSE)) && gBattleMons[battler].hp != 0) {
    gBattleScripting.abilityPopupOverwrite = ABILITY_ZEN_MODE;
    gBattlerAttacker = battler;
    UpdateAbilityStateIndicesForNewSpecies(gActiveBattler, SPECIES_DARMANITAN_ZEN_MODE_GALARIAN);
    gBattleMons[battler].species = SPECIES_DARMANITAN_ZEN_MODE_GALARIAN;
    return TRUE;
}
```

### Supported Transformations
1. **SPECIES_DARMANITAN** to **SPECIES_DARMANITAN_ZEN_MODE**
   - Type: Fire to Fire/Psychic
   - Stats: Physical attacker to Special attacker
   - Attack: 140 to 35, Special Attack: 50 to 140
   - Different ability set and movepool

2. **SPECIES_DARMANITAN_GALARIAN** to **SPECIES_DARMANITAN_ZEN_MODE_GALARIAN**
   - Type: Ice to Ice/Fire  
   - Stats: Balanced to Speed-focused
   - Speed: 95 to 140, Attack: 140 to 120
   - Different ability set and movepool

## Usage Patterns

### Current Implementation Status
- **Fully Implemented**: Complete transformation logic exists
- **Currently Unused**: No Pokemon in the game actually has this ability assigned
- **Form Species Exist**: Zen Mode forms are defined but not accessible

### Activation Conditions
1. Pokemon must have Zen Mode ability
2. Pokemon must be alive (HP > 0)
3. Must be specific supported species (Darmanitan/Galarian Darmanitan)
4. Triggers on battle entry only

### Battle Behavior
- **Permanent Duration**: Lasts entire battle, no reversal possible
- **Entry Activation**: Happens immediately when sent into battle
- **Ability Display**: Shows ability popup when transforming
- **Stat Changes**: Complete stat redistribution based on new form
- **Type Changes**: Gains secondary typing (Psychic or Fire)

## Technical Details

### Function Calls
- Uses `TryTransformAttacker()` for transformation handling
- Calls `UpdateAbilityStateIndicesForNewSpecies()` for ability updates
- Updates `gBattleMons[battler].species` directly
- Sets `gBattleScripting.abilityPopupOverwrite` for display

### Comparison with Similar Abilities
- **vs Forecast**: Same implementation, but different species and conditions
- **vs Stance Change**: Zen Mode is permanent, Stance Change is move-based
- **vs Shields Down**: Zen Mode isn't HP-based, triggers unconditionally

### Form Differences
**Regular Darmanitan to Zen Mode:**
- HP: 105 to 105 (unchanged)
- Attack: 140 to 35 (-105)
- Defense: 65 to 95 (+30)
- Sp. Attack: 50 to 140 (+90)
- Sp. Defense: 65 to 95 (+30)
- Speed: 95 to 50 (-45)
- Typing: Fire to Fire/Psychic

**Galarian Darmanitan to Zen Mode:**
- HP: 105 to 105 (unchanged)
- Attack: 140 to 120 (-20)
- Defense: 65 to 60 (-5)
- Sp. Attack: 50 to 35 (-15)
- Sp. Defense: 65 to 60 (-5)
- Speed: 95 to 140 (+45)
- Typing: Ice to Ice/Fire

## Integration Notes

### Battle System Integration
- Fully integrated with form change system
- Works with ability suppression checks
- Handles species updates correctly
- Manages ability state transitions

### Randomizer Considerations
- Marked as `randomizerBanned = TRUE`
- Prevents assignment to incompatible Pokemon
- Avoids breaking form change logic

### Potential Use Cases
If enabled on appropriate Pokemon:
- Creates powerful late-game sweepers with form change strategy
- Provides type coverage changes mid-battle
- Offers stat redistribution for different battle roles
- Adds tactical depth to team building

The ability is complete and functional but currently serves as unused infrastructure, ready for activation on appropriate Pokemon species.
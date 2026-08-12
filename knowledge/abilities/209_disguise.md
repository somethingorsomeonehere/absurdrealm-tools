---
id: 209
name: Disguise
status: reviewed
character_count: 215
---

# Disguise - Ability ID 209

## In-Game Description
"Protects once against an attack. Restores protection in fog."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Disguise blocks the first damaging move that hits the Pokemon and changes its form after. Only non-status moves are blocked. In fog, the disguise is restored immediately once per switch in, or when fog is set again.

## Detailed Mechanical Explanation
*For Discord/reference use*

Disguise is a unique defensive ability exclusive to Mimikyu that provides a one-time damage nullification similar to a free Focus Sash, but with additional form-changing mechanics and weather interactions.

### Core Mechanics
- **Damage Nullification**: Completely blocks the first damaging move that would hit the Pokemon
- **Form Change**: When disguise is broken, triggers a form change (e.g., Mimikyu to Mimikyu Busted)
- **One-Time Use**: Only blocks one attack per battle entry
- **Weather Restoration**: Disguise is restored in fog weather conditions

### Activation Conditions
```cpp
// From DoesDisguiseBlockMove function
ON_ABILITY(battlerDef, TRUE, gAbilities[ability].onDisguise, 
    FILTER(gAbilities[ability].onDisguise(battlerDef, TRUE));
    FILTER_NOT(gBattleMons[battlerDef].status2 & STATUS2_TRANSFORMED);
    FILTER_NOT(IS_MOVE_STATUS(move));
    FILTER_NOT(gHitMarker & HITMARKER_IGNORE_DISGUISE && move != MOVE_SUCKER_PUNCH);
    return TRUE;)
```

### Form Changes Supported
```cpp
// From onDisguise callback
switch (gBattleMons[battler].species) {
    case SPECIES_MIMIKYU:
        return SPECIES_MIMIKYU_BUSTED;
    case SPECIES_MIMIKYU_RAYQUAZA:
        return SPECIES_MIMIKYU_RAYQUAZA_BUSTED;
    default:
        return SPECIES_NONE;
}
```

### Moves That DON'T Trigger Disguise
- **Status moves**: Moves that don't deal damage (Thunder Wave, Toxic, etc.)
- **Moves with HITMARKER_IGNORE_DISGUISE**: Certain moves specifically bypass disguise
- **Exception**: Sucker Punch can trigger disguise even with the ignore flag

### Weather Interaction - Fog Restoration
```cpp
// DisguiseReformHandler restores original form in fog
static int DisguiseReformHandler(AbilityEnum ability, int battler, AbilityCallType callType) {
    SpeciesEnum newSpecies;
    switch (gBattleMons[battler].species) {
        case SPECIES_MIMIKYU_BUSTED:
            newSpecies = SPECIES_MIMIKYU;
            break;
        case SPECIES_MIMIKYU_RAYQUAZA_BUSTED:
            newSpecies = SPECIES_MIMIKYU_RAYQUAZA;
            break;
        default:
            return FALSE;
    }
    CHECK(IsBattlerWeatherAffected(battler, WEATHER_FOG_ANY))
    CHECK_NOT(gBattleMons[battler].status2 & STATUS2_TRANSFORMED)
    // Restores original form and resets disguise protection
}
```

### Technical Implementation
- **Ability Properties**: `breakable = TRUE`, `unsuppressable = TRUE`, `randomizerBanned = TRUE`
- **Entry Effect**: Automatically restores disguise form if in fog weather upon entry
- **Form Change Mechanics**: Updates species data and battle state when disguise breaks
- **Battle Script Integration**: Uses `BattleScript_TargetFormChange` for visual form changes

### Interactions with Other Mechanics
- **Substitute**: Disguise works independently of Substitute
- **Transform**: Cannot activate if the Pokemon is transformed
- **Magic Guard**: Does not interact with Magic Guard (different protection types)
- **Multi-hit Moves**: Only blocks the first hit of multi-hit moves
- **Critical Hits**: Critical hits are still blocked by disguise

### Strategic Implications
- **Guaranteed Setup**: Provides one free turn for setup moves or positioning
- **Weather Dependency**: Most effective in fog-heavy team compositions
- **Form Change Stats**: Busted forms typically have different stat distributions
- **Mind Games**: Opponents must account for the guaranteed protection

### Common Users
- **Mimikyu**: Primary user, changes to Mimikyu-Busted form
- **Mimikyu-Rayquaza**: Elite Redux variant with unique form change

### Competitive Usage Notes
- **Entry Hazards**: Stealth Rock and other hazards trigger after disguise breaks
- **Status Move Immunity**: Vulnerable to status moves like Will-O-Wisp or Thunder Wave
- **One-Time Protection**: Once broken, requires fog weather or switching out/in to restore
- **Priority Moves**: Still blocks priority moves like Extreme Speed or Bullet Punch

### Counters
- **Status Moves**: Thunder Wave, Toxic, Will-O-Wisp bypass disguise entirely
- **Passive Damage**: Poison, burn, and weather damage bypass disguise
- **Multi-turn Moves**: Only first hit blocked, subsequent hits deal full damage
- **Mold Breaker**: May bypass disguise protection (implementation dependent)

### Synergies
- **Fog Weather**: Essential for disguise restoration and repeated protection
- **Setup Moves**: Swords Dance, Nasty Plot, or defensive setup moves
- **Shadow Sneak**: Priority move that works well after disguise breaks
- **Substitute**: Can be used after disguise breaks for additional protection

### Version History
Elite Redux implementation includes the unique fog weather restoration mechanic, differentiating it from standard Pokemon games where disguise is permanently broken until switching out.
---
id: 739
name: Teraform Zero
status: reviewed
character_count: 229
---

# Teraform Zero - Ability ID 739

## In-Game Description
"Tera Shell + clears weather and terrain on first entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

At full HP, all attacks towards the user deal "not very effective" damage regardless of type effectiveness. Activates on each hit of a multihit attack unlike other similar abilities. On entry, clears normal weathers and terrains.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Teraform Zero is a hybrid defensive/utility ability that combines two distinct effects:
1. **Tera Shell component**: Damage reduction when at full HP
2. **Field clearing component**: Removes weather and terrain on first entry

### Tera Shell Component
- **Damage reduction**: Reduces super effective moves to 50% damage when at full HP
- **HP requirement**: Only works when the Pokemon is at maximum HP
- **Type coverage**: Affects all super effective attacks regardless of type
- **Breakable**: Can be suppressed by Mold Breaker and similar abilities

### Field Clearing Component
- **Activation**: Triggers only on first entry per battle
- **Single use**: Uses the single-use ability counter system
- **Weather clearing**: Removes all active weather conditions:
  - Sun, Rain, Sandstorm, Hail
  - Harsh sunlight, Heavy rain
  - Desolate Land, Primordial Sea effects
- **Terrain clearing**: Removes all active terrain effects:
  - Electric Terrain, Grassy Terrain
  - Misty Terrain, Psychic Terrain
  - Any custom terrains

### Technical Implementation
```c
constexpr Ability TeraformZero = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(!GetSingleUseAbilityCounter(battler, ability));
        SetSingleUseAbilityCounter(battler, ability, TRUE);
        CHECK(IsWeatherActive(WEATHER_ANY) || IsTerrainActive(STATUS_FIELD_TERRAIN_ANY))
        BattleScriptPushCursorAndCallback(BattleScript_TeraformZero);
        return TRUE;
    },
    .onAfterTypeEffectiveness = TeraShell.onAfterTypeEffectiveness,
    .onAfterTypeEffectivenessFor = TeraShell.onAfterTypeEffectivenessFor,
    .breakable = TRUE,
};
```

### Battle Script Behavior
The `BattleScript_TeraformZero` script:
1. First attempts to remove weather using `removeweather`
2. If weather was cleared, displays appropriate weather ending message
3. Then attempts to remove terrain using `removeterrain`
4. If terrain was cleared, displays appropriate terrain ending message

### Activation Conditions
- **Entry requirement**: Must be switching in or entering battle
- **Single use**: Only works on first entry per battle
- **Field check**: Only activates if weather or terrain is actually present
- **Priority**: Activates before other entry abilities that depend on weather/terrain

### Important Interactions
- **Multi-entry limitation**: Won't activate on subsequent entries in same battle
- **U-turn/Volt Switch**: Won't reactivate if switching back in
- **Revive/Healing**: Won't reactivate after fainting and revival
- **Form changes**: Single-use counter persists through form changes
- **Tera Shell inheritance**: Full HP requirement applies to damage reduction

### Weather/Terrain Priority
- **Override ability**: Takes priority over weather/terrain setting abilities
- **Immediate clearing**: Removes fields before other entry abilities can benefit
- **Message display**: Shows clearing messages before ability activation message
- **Permanent removal**: Fields stay cleared until manually reset

### Strategic Implications

#### Offensive Applications
- **Field control**: Disrupts weather/terrain-based strategies
- **Revenge killing**: Can switch in safely with damage reduction at full HP
- **Counter-setup**: Removes opponent's field advantages
- **Utility switching**: Provides safe entry against super effective coverage

#### Defensive Applications  
- **Tank role**: Survives super effective hits at full HP
- **Pivot utility**: Can switch in and clear problematic fields
- **Anti-setup**: Disrupts weather/terrain sweepers
- **One-time protection**: Gives free switch-in opportunity

#### Team Synergy
- **Weather teams**: Can reset opponent's weather for your own setter
- **Terrain teams**: Clears opposing terrain for your own terrain
- **Bulky pivots**: Excellent on defensive pivots and tanks
- **Lead potential**: Can lead to disrupt opposing setup strategies

### Counters and Limitations

#### Direct Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable both components
- **Multi-hit moves**: Can break through Tera Shell component
- **Status moves**: Tera Shell doesn't protect against status effects
- **Entry hazards**: Damage from hazards can break full HP requirement

#### Strategic Limitations
- **One-time use**: Field clearing only works once per battle
- **HP dependency**: Tera Shell component requires full HP
- **Priority moves**: High priority moves still deal full damage
- **Residual damage**: Poison, burn, etc. disable Tera Shell component

#### Situational Weaknesses
- **No weather/terrain**: Entry component does nothing if no fields active
- **Late game**: Less valuable once single use is expended
- **Chip damage**: Any prior damage negates Tera Shell protection
- **Prediction reliance**: Requires good prediction for optimal switching

### Common Users and Archetypes
- **Bulky pivots**: Pokemon that frequently switch in
- **Defensive walls**: Tanks that need protection from super effective hits
- **Field controllers**: Pokemon focused on disrupting opponent strategies
- **Revenge killers**: Fast attackers that need safe entry opportunities

### Competitive Viability
- **High utility**: Combination of defense and field control is unique
- **Meta dependent**: Value depends on prevalence of weather/terrain teams
- **Switch advantage**: Provides immediate board control on entry
- **Resource management**: Single-use nature requires strategic timing

### Synergistic Abilities (for multi-ability Pokemon)
- **Weather/terrain setters**: Can clear opponent's field then set your own
- **Speed control**: Abilities that help capitalize on safe entry
- **Recovery abilities**: Help maintain full HP for Tera Shell component
- **Status immunity**: Prevents status from breaking HP requirement

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Modern implementation**: Uses single-use counter system
- **Tera Shell integration**: Inherits exact mechanics from base Tera Shell
- **Field clearing**: Uses standard weather/terrain removal scripts
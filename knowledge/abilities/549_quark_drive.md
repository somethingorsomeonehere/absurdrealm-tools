---
id: 549
name: Quark Drive
status: reviewed
character_count: 285
---

# Quark Drive - Ability ID 549

## In-Game Description
"Boosts highest stat in Electric Terrain or with Booster Energy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's highest stat by 50% for Speed or 30% for other stats during electric terrain. When terrain ends, Booster Energy activates if held. This is considered a raw stat boost and not a stat raise. Cannot be copied, suppressed, or replaced unless by Simple Beam or Worry Seed.

## Detailed Mechanical Explanation
*For Discord/reference use*

Quark Drive is a paradox ability that provides stat boosts under specific conditions, making it the Electric-type counterpart to Protosynthesis.

### Core Mechanics
- **Highest Stat Detection**: Uses `GetHighestStatId(battler, TRUE)` to determine the highest stat including current stat stages
- **Boost Values**: 
  - Speed: 50% increase (1.5x multiplier)
  - Other stats: 30% increase (1.3x multiplier)
- **Priority**: Electric Terrain > Booster Energy consumption

### Activation Conditions

#### Electric Terrain Activation
```cpp
if (state.source == PARADOX_BOOST_NOT_ACTIVE && IsTerrainActive(STATUS_FIELD_ELECTRIC_TERRAIN)) {
    ParadoxBoost boost = {.source = PARADOX_WEATHER_ACTIVE, .statId = GetHighestStatId(battler, TRUE)};
    // Immediate activation when terrain becomes active
}
```

#### Booster Energy Activation
```cpp
if (state.source == PARADOX_BOOST_NOT_ACTIVE && GetBattlerHoldEffect(battler, TRUE) == HOLD_EFFECT_BOOSTER_ENERGY) {
    ParadoxBoost boost = {.source = PARADOX_BOOSTER_ENERGY, .statId = GetHighestStatId(battler, TRUE)};
    RemoveItem(battler); // Consumes the item
}
```

### Stat Calculation Process
1. **Base Stat Retrieval**: Gets base stats from `(&gBattleMons[battlerId].attack)[i - 1]`
2. **Stat Stage Application**: Applies current stat stage modifiers using `gStatStageRatios`
3. **Highest Stat Selection**: Compares all stats (ATK, DEF, SPA, SPD, SPE) to find maximum
4. **Boost Application**: Applies 1.5x for Speed or 1.3x for other stats during stat calculations

### Technical Implementation
- **Ability Handler**: `QuarkDriveHandler()` manages state transitions
- **State Management**: Uses `ParadoxBoost` struct to track boost source and target stat
- **Trigger Events**: 
  - `onEntry`: Activates on switch-in if conditions met
  - `onTerrain`: Responds to terrain changes
  - `onStat`: Applies the actual stat multiplier

### Interactions with Other Mechanics

#### Terrain Interactions
- Electric Terrain must be active (not blocked by abilities like Clueless)
- Works with natural Electric Terrain, Electric Surge ability, or moves like Electric Terrain
- Boost ends immediately when Electric Terrain ends (unless Booster Energy activates)

#### Item Interactions
- **Booster Energy Priority**: If Electric Terrain ends while holding Booster Energy, automatically consumes item to maintain boost
- **Permanent Effect**: Booster Energy consumption provides permanent boost until switching out
- **One-Time Use**: Each Booster Energy can only activate the ability once

#### Stat Stage Interactions
- Recalculates highest stat when stat stages change
- Benefits from positive stat stages in highest stat determination
- Ignores stat stage changes if battler doesn't benefit from stat buffs

### Strategic Implications

#### Competitive Usage
- **Electric Terrain Teams**: Synergizes with Electric Surge Pokemon and Electric Terrain setters
- **Booster Energy Sets**: Provides immediate power spike with guaranteed activation
- **Speed Control**: Often boosts Speed stat due to many Quark Drive users having high Speed
- **Wallbreaking**: Significant boost to offensive stats enables breaking through defensive cores

#### Common Users in Elite Redux
Based on the codebase analysis, Quark Drive appears on numerous Future Paradox Pokemon:
- High-speed attackers (often Speed becomes highest stat)
- Balanced statted Pokemon where boost varies by stat stages
- Genderless robotic/mechanical themed Pokemon

### Example Damage Calculations
Assuming a Pokemon with 120 base Attack as highest stat:
- **Without Quark Drive**: 120 base Attack
- **With Quark Drive**: 120 x 1.3 = 156 effective Attack
- **Damage Increase**: ~30% more damage output

For Speed users (130 base Speed):
- **Without Quark Drive**: 130 base Speed  
- **With Quark Drive**: 130 x 1.5 = 195 effective Speed
- **Speed Advantage**: Significant outspeeding potential

### Counters
- **Terrain Control**: Remove Electric Terrain with opposing terrains or weather
- **Ability Suppression**: Gastro Acid, Neutralizing Gas shut down the ability
- **Priority Moves**: Bypass Speed boosts entirely
- **Status Conditions**: Paralysis negates Speed advantages
- **Stat Drops**: Lower the boosted stat to reduce effectiveness

### Synergies
- **Electric Terrain Setters**: Tapu Koko, Pincurchin, Electric Surge users
- **Terrain Extenders**: Terrain Extender item prolongs Electric Terrain
- **Speed Control**: Thunder Wave support to handle faster threats
- **Entry Hazards**: Stealth Rock support for KO ranges with boosted attacks

### Version History
- Introduced in Generation 9 as signature ability of Future Paradox Pokemon
- Elite Redux implementation follows official mechanics with custom stat detection
- Works with Elite Redux's 4-ability system as innate ability on many species
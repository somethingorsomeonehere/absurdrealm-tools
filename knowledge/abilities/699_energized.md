---
id: 699
name: Energized
status: reviewed
character_count: 300
---

# Energized - Ability ID 699

## In-Game Description
"Generator + charges up on KO with an Electric-type move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Charges up the user once upon switching in, doubling Electric-type move power for the next Electric attack. Recharge when Electric Terrain becomes active during battle. Charged state is lost upon switching out or after using an Electric move. Recharges when scoring a direct KO with an Electric move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Energized is a hybrid ability that combines the functionality of Generator with an additional trigger for the charged up status. It provides multiple ways to activate the charged up condition, which doubles Electric-type move power.

### Activation Conditions
**Generator Component:**
- **On entry**: Charges up when switching in if Electric Terrain is active OR if this is the first time the ability activates per battle
- **Electric Terrain**: Automatically charges up when Electric Terrain becomes active
- **Single use**: The entry effect only works once per battle (unless terrain is active)

**Energized Component:**
- **KO with Electric move**: Charges up when knocking out an opponent with an Electric-type move
- **Multiple triggers**: Unlike Generator, this KO trigger can activate multiple times per battle

### Technical Implementation
```c
// Energized inherits Generator's onEntry and onTerrain
.onEntry = Generator.onEntry,
.onTerrain = Generator.onTerrain,

// Additional KO trigger for Electric moves
.onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
    CHECK(moveType == TYPE_ELECTRIC);
    SetOncePerTurnAbilityCounter(battler, ability, TRUE);
    BattleScriptCall(BattleScript_GeneratorActivatesRet);
    return TRUE;
},
```

### Charged Up Status Effects
- **Electric move boost**: Doubles the power of all Electric-type moves (2.0x multiplier)
- **Consumption**: Status is consumed after using any Electric-type move
- **Visual indicator**: "Pokemon is charging power!" message appears
- **Status3 flag**: Uses STATUS3_CHARGED_UP internal flag

### Important Interactions
- **Terrain synergy**: Works excellently with Electric Terrain setters
- **Move priority**: Charged status applies before move damage calculation
- **Status removal**: Charged status is removed after any Electric move, regardless of success
- **Ability suppression**: Doesn't work if ability is suppressed by Mold Breaker effects
- **Switch out**: Charged status is maintained when switching out (persistent ability)

### Strategic Implications
- **Enhanced Generator**: More reliable than base Generator due to multiple activation methods
- **Momentum building**: KO trigger allows for potential sweeping chains
- **Electric terrain synergy**: Becomes extremely potent on Electric Terrain teams
- **First turn power**: Can charge up immediately on entry in many situations
- **Revenge KO potential**: Can chain KOs with boosted Electric moves

### Optimal Usage
- **Electric Terrain teams**: Pairs excellently with Surge abilities
- **Mixed attackers**: Benefits both physical and special Electric moves equally
- **Late-game cleaners**: KO trigger makes it excellent for end-game scenarios
- **Pivot users**: Can switch in for guaranteed charge, then pivot out while maintaining status

### Counters
- **Priority moves**: Can be revenge killed before using charged moves
- **Non-Electric coverage**: Pokemon may be forced to use non-Electric moves
- **Status moves**: Sleep/paralysis can waste charged turns
- **Terrain override**: Changing terrain prevents terrain-based charging
- **Mold Breaker**: Suppresses the ability entirely

### Synergies
- **Electric Surge**: Guaranteed charging on entry with terrain
- **U-turn/Volt Switch**: Can charge up and maintain status while pivoting
- **Thunder Wave**: Paralyze opponents to ensure charged move connects
- **Magnet Rise**: Avoid Ground moves while setting up charged attacks
- **Choice items**: Maximize damage output of charged moves

### Notable Users
Pokemon with Energized typically have:
- Strong Electric-type movepools
- Mixed offensive capabilities
- Good Speed stats for sweeping
- Ability to switch in safely

### Competitive Viability
- **Tier**: High utility ability for Electric-type specialists
- **Reliability**: More consistent than base Generator
- **Versatility**: Multiple activation methods increase flexibility
- **Power level**: Significant damage boost when active
- **Team support**: Works well in Electric-focused team compositions

### Version History
- Elite Redux exclusive ability
- Based on Generator with additional KO trigger
- Designed to reward aggressive Electric-type play
- Part of the extended ability system (ID 699)
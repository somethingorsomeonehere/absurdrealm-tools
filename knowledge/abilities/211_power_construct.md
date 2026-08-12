---
id: 211
name: Power Construct
status: reviewed
character_count: 285
---

# Power Construct - Ability ID 211

## In-Game Description
"At 1/2 of max HP or below, transforms into Complete form."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Power Construct transforms Zygarde 50% or 10% forms into Complete form when HP drops to 50% or below at the end of any turn. Complete form has massive 216 HP (doubled from 108), making it an extremely bulky tank. The transformation is permanent for the battle and cannot be suppressed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Power Construct is Zygarde's signature ability that allows form transformation during battle based on HP thresholds. It functions as a powerful survival mechanism that activates automatically.

### Activation Conditions
- Must be Zygarde 50% Form (SPECIES_ZYGARDE) or Zygarde 10% Form (SPECIES_ZYGARDE_10)
- HP must be at 50% or below of maximum HP
- Triggers at the end of any turn (onEndTurn callback)
- Cannot be suppressed (unsuppressable = TRUE)
- Does not work if already transformed (STATUS2_TRANSFORMED check)

### Technical Implementation
```cpp
constexpr Ability PowerConstruct = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK(gBattleMons[battler].species == SPECIES_ZYGARDE || gBattleMons[battler].species == SPECIES_ZYGARDE_10)
        CHECK(gBattleMons[battler].hp <= gBattleMons[battler].maxHP / 2)
        CHECK_NOT(gBattleMons[battler].status2 & STATUS2_TRANSFORMED)

        gBattleStruct->changedSpecies[gBattlerPartyIndexes[battler]] = gBattleMons[battler].species;
        UpdateAbilityStateIndicesForNewSpecies(battler, SPECIES_ZYGARDE_COMPLETE);
        gBattleMons[battler].species = SPECIES_ZYGARDE_COMPLETE;
        BattleScriptPushCursorAndCallback(BattleScript_AttackerFormChangeEnd3);
        return TRUE;
    },
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

### Stat Changes Upon Transformation
**Base Zygarde 50% Form:**
- HP: 108 to **216** (+108, exactly doubled)
- Attack: 100 (unchanged)
- Defense: 121 (unchanged)
- Sp. Attack: 81 to **91** (+10)
- Sp. Defense: 95 (unchanged)
- Speed: 95 to **85** (-10)

**Zygarde 10% Form:**
- HP: Unknown base to **216** 
- Gains massive bulk upon transformation

### Numerical Values
- Activation threshold: 50% of maximum HP
- HP increase: 108 to 216 (100% increase)
- Sp. Attack boost: +10 points
- Speed reduction: -10 points
- Timing: End of turn

### Interactions with Other Abilities/Mechanics
- **Unsuppressable**: Cannot be disabled by Gastro Acid, Skill Swap, etc.
- **Permanent**: Transformation lasts for the entire battle
- **One-time**: Cannot transform back to original form
- **Status immunity**: Blocked if already transformed by other means
- **Ability updates**: Updates ability state indices for new form's abilities

### Strategic Implications
- **Defensive pivot**: Transforms a moderate tank into an extreme wall
- **HP preservation**: Doubling HP effectively heals the Pokemon
- **Speed trade-off**: Loses 10 Speed points, becoming slower but bulkier
- **Late-game power**: Most effective when activated strategically
- **Setup opportunities**: Extra bulk allows for more setup moves

### Example Calculations
If Zygarde starts with 108 HP and takes 54+ damage (50% threshold):
- At end of turn: Transforms to Complete form
- New HP: 216 total, current HP becomes proportionally higher
- Effective healing: Gains massive survivability

### Common Users
- **Zygarde 50% Form**: Primary user, most common form
- **Zygarde 10% Form**: Alternative user, faster but frailer initially
- **Zygarde Complete**: Final form, cannot use Power Construct

### Competitive Usage Notes
- **Tier placement**: Legendary tier Pokemon
- **Role compression**: Acts as both offensive threat and defensive wall
- **Prediction factor**: Opponents must account for potential transformation
- **Resource management**: Best used when opponent cannot immediately KO
- **Team synergy**: Benefits from entry hazard removal and support

### Counters
- **High damage output**: Try to KO before transformation
- **Status conditions**: Toxic, burns can pressure through bulk
- **Taunt**: Prevents setup moves after transformation
- **Critical hits**: Can bypass the increased defensive bulk
- **Multi-hit moves**: Can potentially KO before end-of-turn trigger

### Synergies
- **Leftovers/Recovery moves**: Maximizes HP benefit
- **Substitute**: Can protect while at low HP
- **Rest**: Synergizes with doubled HP pool
- **Primal Armor**: Innate ability provides additional bulk
- **Earthbound**: Innate ground immunity
- **Power Core**: Innate ability synergy

### Version History
- Elite Redux implementation: Full mechanical faithfulness to original concept
- Randomizer banned due to legendary status and power level
- Unsuppressable flag prevents common ability-removal strategies
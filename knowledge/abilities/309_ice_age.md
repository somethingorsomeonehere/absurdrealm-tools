---
id: 309
name: Ice Age
status: reviewed
character_count: 145
---

# Ice Age - Ability ID 309

## In-Game Description
"Adds Ice type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Ice to the user's current typing. Retains Ice typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Ice Age is a type-adding ability that permanently grants the Ice type to the Pokemon upon entering battle. This creates a triple-typed Pokemon by adding Ice as the third type (stored in `type3`), which affects:

- **STAB Calculation**: Ice-type moves receive 1.5x damage multiplier
- **Type Effectiveness**: The Pokemon gains Ice-type resistances and vulnerabilities
- **Move Learning**: Access to Ice-type moves that require Ice typing
- **Battle Interactions**: Affected by abilities and moves that target Ice types

### Activation Conditions
- Triggers automatically when the Pokemon enters battle
- Only activates if the Pokemon doesn't already have Ice typing
- Permanent for the duration of the battle (cannot be removed by most effects)
- Shows battle message: "{Pokemon} added the Ice-type!"

### Technical Implementation
```cpp
constexpr Ability IceAge = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_ICE); },
};

static int AddBattlerType(int battler, int type) {
    CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))
    
    gBattleMons[battler].type3 = type;
    PREPARE_TYPE_BUFFER(gBattleTextBuff2, gBattleMons[battler].type3);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAddedTheType);
    return TRUE;
}
```

### Ice Type Effectiveness Chart
**Ice is Super Effective Against:**
- Grass (2x damage)
- Ground (2x damage) 
- Flying (2x damage)
- Dragon (2x damage)

**Ice is Not Very Effective Against:**
- Fire (0.5x damage)
- Water (0.5x damage)
- Ice (0.5x damage)
- Steel (0.5x damage)

**Ice Resists:**
- Ice (0.5x damage taken)

**Ice is Weak To:**
- Fire (2x damage taken)
- Fighting (2x damage taken)
- Rock (2x damage taken)
- Steel (2x damage taken)

### Strategic Implications

#### Offensive Benefits
- **STAB Ice Moves**: Ice-type attacks receive 1.5x damage multiplier
- **Coverage Expansion**: Provides super-effective hits against Grass, Ground, Flying, and Dragon
- **Dragon Counter**: Particularly valuable against Dragon-types in competitive play
- **Utility Moves**: Access to Ice-type status moves like Haze, Aurora Veil

#### Defensive Considerations
- **Ice Resistance**: Takes 0.5x damage from Ice-type attacks
- **New Vulnerabilities**: Gains weaknesses to Fire, Fighting, Rock, and Steel
- **Type Stacking**: Combined with original types, can create unique resistance profiles

### Example: Clawtificer (Fire/Electric + Ice)
Original typing: Fire/Electric
With Ice Age: Fire/Electric/Ice

**Resistances:**
- Electric (0.5x) - from Electric type
- Fire (0.5x) - from Fire type
- Flying (0.5x) - from Electric type
- Steel (0.5x) - from Fire type
- Ice (0.5x) - from Ice type (Ice Age)
- Grass (0.25x) - Fire resists, Ice super effective (net 0.5x)

**Weaknesses:**
- Ground (2x) - Fire resists but Electric weak (net 2x)
- Water (2x) - Fire weak, Electric resists (net 2x)
- Rock (4x) - Fire weak, Ice weak (net 4x)
- Fighting (2x) - from Ice type (Ice Age)

### Common Users
- **Clawtificer (Fire/Electric)**: Currently the only known user
- Potential candidates: Any non-Ice Pokemon that would benefit from Ice coverage

### Competitive Usage Notes
- **STAB Diversity**: Provides three different STAB types for maximum coverage
- **Dragon Check**: Excellent for checking Dragon-type threats
- **Wall Breaking**: Ice moves help break through Grass and Ground defensive walls
- **Speed Control**: Access to Ice-type priority moves and field effects

### Counters
- **Fire-types**: Resist Ice moves and can exploit the new Fire weakness
- **Steel-types**: Resist Ice moves and can exploit the new Steel weakness
- **Rock-types**: Can exploit the new Rock weakness
- **Multi-hit Moves**: Can overwhelm the typically frail Ice typing

### Synergies
- **Weather Teams**: Pairs well with Hail teams for additional synergy
- **Coverage Moves**: Works with Pokemon that lack natural Ice coverage
- **Mixed Attackers**: Benefits both physical and special Ice moves
- **Entry Hazards**: Ice typing helps against Ground-type hazard setters

### Version History
- Introduced in Elite Redux as part of the extended ability system
- Currently assigned to Clawtificer as an innate ability
- Part of the type-adding ability family (similar to Half Drake, Aquatic, etc.)

### Battle Message
When Ice Age activates:
> "{Pokemon} added the Ice-type!"

### Notes
- The ability only checks that the Pokemon doesn't already have Ice typing before activating
- Cannot be suppressed by typical ability-negating effects during entry
- Persists through switching (when the Pokemon re-enters battle)
- Does not affect the Pokemon's base typing permanently outside of battle
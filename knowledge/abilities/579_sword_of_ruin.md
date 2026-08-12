---
id: 579
name: Sword Of Ruin
status: reviewed
character_count: 179
---

# Sword Of Ruin - Ability ID 579

## In-Game Description
"Lowers the Defense of other Pokemon by 25%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces the Defense stat of every other Pokemon by 25% while the user is out. Multiples of the same Ruin ability do not stack together. Stacks multiplicatively with Defense drops.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Passive Aura Effect**: Reduces Defense stat of all other Pokemon by 25% (multiplies Defense by 0.75)
- **Targets**: Affects all Pokemon on the field except the user (both allies and enemies)
- **Duration**: Permanent effect that lasts as long as the Pokemon with Sword Of Ruin is on the field
- **Activation**: Automatic upon entering battle, no user input required

### Activation Conditions
- Pokemon with Sword Of Ruin must be on the battlefield
- Effect applies immediately upon switch-in
- Persists until the Pokemon with Sword Of Ruin faints or switches out

### Technical Implementation
```cpp
constexpr Ability SwordOfRuin = {
    .onStat = +[](ON_STAT) { RuinEffect(STAT_DEF, battler, statId, stat, flags); },
    .onStatFor = APPLY_ON_OTHER,
    .ruinStat = STAT_DEF,
};

static void RuinEffect(int ruinStat, int battler, int statId, u32 *stat, NonStackingState *flags) {
    if (statId != ruinStat) return;
    if (*flags & NON_STACKING_RUIN) return;
    ON_ABILITY(battler, FALSE, gAbilities[ability].ruinStat == statId, return) *stat *= .75;
    *flags = static_cast<NonStackingState>(static_cast<int>(*flags) | static_cast<int>(NON_STACKING_RUIN));
}
```

### Numerical Values
- **Defense Reduction**: 25% (stat multiplied by 0.75)
- **Affected Stat**: Defense (STAT_DEF = 2)
- **Calculation**: Final Defense = Base Defense x 0.75

### Non-Stacking Behavior
- Multiple Ruin abilities of the same type do not stack
- Uses `NON_STACKING_RUIN` flag to prevent multiple Defense reductions
- Only the first Sword Of Ruin effect applies if multiple Pokemon have this ability

### Damage Calculation Impact
With Sword Of Ruin active, physical damage calculations are modified:
```
Physical Damage = ((2 x Level + 10) � 250) x (Attack � (Defense x 0.75)) x Base Power x Modifiers
```

This effectively increases physical damage by approximately 33.33% against affected Pokemon.

### Complete List of Affected Interactions
- **Physical Moves**: All physical attacks deal increased damage to affected Pokemon
- **Defense-based Moves**: Moves that use Defense stat (like Body Press) are weakened on affected Pokemon
- **Stat Stages**: Defense stat stage changes still apply normally, but to the reduced base Defense
- **Other Abilities**: Interacts with abilities that modify Defense (e.g., Marvel Scale, Fur Coat)

### Interactions with Other Abilities/Mechanics
- **Does NOT stack** with other Sword Of Ruin users
- **Works alongside** other Ruin abilities (Tablets Of Ruin, Vessel Of Ruin, Beads Of Ruin)
- **Bypassed by** Unaware (which ignores stat changes, but this is a base stat modification)
- **Affected by** Mold Breaker variants (which can ignore defensive abilities)
- **Compatible with** stat-boosting abilities like Huge Power on the same Pokemon

### Strategic Implications
- **Offensive Support**: Significantly boosts physical attackers on your team
- **Double-Edged**: Also weakens your own Pokemon's Defense
- **Team Synergy**: Excellent support for physical sweepers and wallbreakers
- **Defensive Liability**: Makes switch-ins more risky due to reduced Defense across the board

### Example Damage Calculations
**Scenario**: Chien-Pao with Sword Of Ruin vs. 252 HP / 252 Def Corviknight
- **Without Sword Of Ruin**: Sacred Sword deals ~45-53% damage
- **With Sword Of Ruin**: Sacred Sword deals ~60-71% damage (33% increase)

**Scenario**: Ally Garchomp Earthquake on 252 HP / 0 Def Landorus-T
- **Without Sword Of Ruin**: ~35-42% damage
- **With Sword Of Ruin**: ~47-56% damage

### Common Users
- **Chien-Pao**: Primary user in Elite Redux, legendary Dark/Ice Pokemon
- **Ruinous Quartet**: Part of the "Treasures of Ruin" legendary group
- **Competitive Builds**: Often used as offensive support or mixed attacker

### Competitive Usage Notes
- **VGC/Doubles**: Extremely powerful in doubles format where it affects multiple targets
- **Singles**: Strong support ability but requires careful team building
- **Entry Hazard Synergy**: Combines well with Stealth Rock to pressure switches
- **Pivot Role**: Often used on Pokemon that can pivot out after providing support

### Counters
- **Special Attackers**: Unaffected by the Defense reduction
- **Unaware Users**: Some interactions may be mitigated (though this is a base stat mod)
- **Rapid Removal**: Forcing the Sword Of Ruin user out removes the effect
- **Status Moves**: Sleep, paralysis, or other status to limit the user's effectiveness

### Synergies
- **Physical Attackers**: Any physical sweeper benefits enormously
- **Choice Band/Scarf Users**: Amplifies already powerful physical attacks
- **Entry Hazards**: Stealth Rock + reduced Defense creates massive pressure
- **Other Ruin Abilities**: Can be combined with Tablets/Vessel/Beads Of Ruin for comprehensive stat reduction

### Version History
- **Generation 9**: Introduced as signature ability of Chien-Pao
- **Elite Redux**: Implemented as part of the Ruinous abilities system
- **Current Status**: Fully functional with proper non-stacking mechanics
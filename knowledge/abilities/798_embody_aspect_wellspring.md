---
id: 798
name: Embody Aspect (Wellspring)
status: reviewed
character_count: 82
---

# Embody Aspect (Wellspring) - Ability ID 798

## In-Game Description
"+1 Spdef on Entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the Pokemon's Special Defense stat by one stage when switching into battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Effect**: Raises Special Defense by +1 stage (50% increase) when switching into battle
- **Trigger**: Activates immediately upon switching in, before any other battle actions
- **Type**: Entry-based stat boost ability
- **Frequency**: Once per switch-in (resets when Pokemon switches out and back in)

### Activation Conditions
- Must successfully switch into battle (not when battle starts with this Pokemon already out)
- Special Defense must be capable of being raised (not already at +6 or blocked by effects)
- Works regardless of HP, status conditions, or opponent's abilities

### Technical Implementation
```cpp
constexpr Ability EmbodyAspectWellspring = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_SPDEF))

        SetStatChanger(STAT_SPDEF, 1);
        BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
        return TRUE;
    },
};
```

### Stat Boost Details
- **+1 Special Defense**: Multiplies Special Defense by 1.5x (equivalent to 50% increase)
- **Stacking**: Combines multiplicatively with other stat modifiers
- **Duration**: Lasts until the Pokemon switches out or faints
- **Maximum**: Cannot exceed +6 Special Defense stages

### Interactions with Other Abilities/Mechanics
- **Clear Body/White Smoke**: Protects the stat boost from being lowered by opponents
- **Simple**: Doubles the stat boost to +2 Special Defense
- **Contrary**: Would lower Special Defense by 1 stage instead (theoretical interaction)
- **Intimidate**: Ability activates after Intimidate, so both effects apply
- **Competitive/Defiant**: Does not trigger these abilities as it's a self-boost

### Strategic Implications
- **Defensive Pivot**: Excellent for switch-in utility, making Ogerpon immediately bulkier
- **Setup Potential**: Provides immediate defensive presence for setting up or tanking hits
- **Type Synergy**: Complements Water-type's natural special bulk in the Wellspring form
- **Form Specialization**: Each Embody Aspect variant boosts different stats (Speed/Attack/Defense/Special Defense)

### Example Damage Calculations
With base 156 Special Defense at level 100:
- **No boost**: 364 Special Defense
- **+1 boost**: 546 Special Defense (50% increase)
- **Against 100 power special move**: ~33% damage reduction compared to unboosted

### Common Users
- **Ogerpon (Wellspring Mask)**: Only Pokemon with this specific ability variant
- **Form Requirements**: Must be holding Wellspring Mask to have this ability
- **Mega Evolution**: Ogerpon Wellspring Mask Mega retains this ability

### Competitive Usage Notes
- **Entry Hazard Synergy**: Allows safer switches into Stealth Rock/Spikes damage
- **Pivot Role**: Enables hit-and-run tactics with improved special bulk
- **Coverage**: Wellspring form typically runs Water/Grass moves with special attack focus
- **Team Support**: Can switch in on special attackers more safely

### Counters
- **Physical Attacks**: Does not boost Defense, vulnerable to physical moves
- **Stat Reset**: Haze, Clear Smog, or switching out removes the boost
- **Infiltrator**: Bypasses stat boosts when using moves through substitutes
- **Critical Hits**: Ignore positive stat modifications

### Synergies
- **Assault Vest**: Stacks with the Special Defense boost for extreme special bulk
- **Leftovers**: Provides sustain to take advantage of the improved bulk
- **U-turn/Volt Switch**: Allows repeated use of the ability through frequent switching
- **Rapid Spin/Defog**: Support to enable safer switching

### Version History
- **Generation 9**: Introduced with Ogerpon and its mask forms
- **Elite Redux**: Implemented as part of the Embody Aspect ability family
- **Current Status**: Fully functional with proper stat boost mechanics
---
id: 803
name: Headstrong
status: reviewed
character_count: 82
---

# Headstrong - Ability ID 803

## In-Game Description
"+1 Spdef on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the Pokemon's Special Defense stat by one stage when switching into battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

Headstrong is a straightforward entry ability that provides an immediate defensive boost upon switching in.

### Core Mechanics
- **Trigger**: Activates when the Pokemon switches into battle
- **Effect**: Raises Special Defense by 1 stage (+50% Special Defense)
- **Implementation**: Uses the `onEntry` hook with `CanRaiseStat(battler, STAT_SPDEF)` check

### Activation Conditions
- Must switch into battle (not at battle start)
- Special Defense must not already be at maximum (+6 stages)
- Cannot be suppressed by abilities that prevent stat changes

### Technical Implementation
```cpp
constexpr Ability Headstrong = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_SPDEF))

        SetStatChanger(STAT_SPDEF, 1);
        BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
        return TRUE;
    },
    .breakable = TRUE,
};
```

### Numerical Values
- **Stat Boost**: +1 stage to Special Defense
- **Percentage Increase**: 50% increase to Special Defense stat
- **Maximum Stages**: Cannot activate if Special Defense is already at +6

### Interactions with Other Abilities/Mechanics
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze
- **Mold Breaker Effect**: These abilities ignore Headstrong entirely
- **Clear Body/White Smoke**: Does not prevent Headstrong from activating (it's a self-boost)
- **Contrary**: Would lower Special Defense instead of raising it
- **Simple**: Would raise Special Defense by 2 stages instead of 1

### Strategic Implications
- **Defensive Setup**: Provides immediate bulk against special attacks
- **Switch-In Value**: Makes the Pokemon a reliable special wall from turn 1
- **Momentum**: Allows aggressive switching without losing defensive presence
- **Synergy**: Works well with other defensive abilities and moves

### Example Damage Calculations
With base 100 Special Defense at level 50:
- **No boost**: 120 Special Defense
- **+1 Headstrong**: 180 Special Defense (50% increase)
- **Damage reduction**: Approximately 33% less damage from special attacks

### Common Users
This ability is typically found on:
- Defensive Pokemon designed for special walling
- Pokemon with already high Special Defense stats
- Bulky support Pokemon that benefit from immediate defensive presence

### Competitive Usage Notes
- **Entry Hazard Synergy**: Helps mitigate damage from special attacks while setting up
- **Pivot Potential**: Makes switching safer against special attackers
- **Late Game**: Can be crucial for surviving powerful special attacks in endgame scenarios

### Counters
- **Mold Breaker variants**: Completely bypass the ability
- **Physical attacks**: Doesn't boost Defense, vulnerable to physical moves
- **Stat-lowering moves**: Can be neutralized by moves like Psychic Noise or abilities like Intimidate (though that affects Attack)
- **Haze/Clear Smog**: Removes the stat boost after activation

### Synergies
- **Assault Vest**: Stacks with the Special Defense boost for extreme special bulk
- **Calm Mind**: Can further boost Special Defense and Special Attack
- **Recover/Roost**: Healing moves work well with the improved bulk
- **Leftovers**: Passive recovery complements the defensive nature

### Version History
- **Elite Redux**: Introduced as a new ability providing reliable entry-based Special Defense boosts
- **Current Status**: Active ability in the current build
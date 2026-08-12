---
id: 797
name: Embody Aspect (Cornerstone)
status: reviewed
character_count: 74
---

# Embody Aspect (Cornerstone) - Ability ID 797

## In-Game Description
"+1 Defense on Entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the Pokemon's Defense stat by one stage when switching into battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Primary Effect**: Raises Defense by +1 stage upon entry
- **Timing**: Activates immediately when the Pokemon switches into battle
- **Implementation**: Uses the same code as Dauntless Shield (`DauntlessShield.onEntry`)

### Activation Conditions
- Triggers when the Pokemon switches into battle through any means:
  - Normal switching
  - Forced switching (e.g., from Roar, Whirlwind)
  - Entry after fainting of previous Pokemon
  - Entry from moves like U-turn, Volt Switch

### Technical Implementation
```cpp
constexpr Ability EmbodyAspectCornerstone = {
    .onEntry = DauntlessShield.onEntry,
};

// DauntlessShield implementation:
constexpr Ability DauntlessShield = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_DEF))
        
        SetStatChanger(STAT_DEF, 1);
        BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
        return TRUE;
    },
};
```

### Numerical Values
- **Stat Boost**: +1 stage to Defense (increases Defense by 50%)
- **Maximum Applications**: Can only boost Defense if it's not already at maximum (+6 stages)

### Interactions with Other Abilities/Mechanics
- **Blocked by**: Clear Body, White Smoke, Full Metal Body prevent the stat boost
- **Overwritten by**: Abilities like Simple double the stat boost to +2 Defense
- **Stacks with**: Other Defense-boosting abilities and moves
- **Fails if**: Defense is already at maximum (+6 stages)

### Strategic Implications
- **Defensive Setup**: Provides immediate bulk upon switching in
- **Pivot Potential**: Makes switching safer by gaining defensive presence
- **Synergy**: Works well with defensive movesets and stall strategies
- **Counterplay**: Can be reset by stat-resetting moves like Haze, Clear Smog

### Common Users
- **Ogerpon (Cornerstone Mask Mega)**: The primary user of this ability
  - Type: Grass/Rock
  - Base Defense: 156 (after Mega Evolution)
  - Complements its defensive role with immediate Defense boost

### Competitive Usage Notes
- **Format Viability**: Strong in defensive teams and balance cores
- **Entry Hazard Synergy**: Helps offset damage from Stealth Rock and Spikes
- **Momentum Control**: Allows safer switching and defensive plays
- **Multi-Battle Value**: Activates every time the Pokemon switches in

### Counters
- **Stat Reset**: Haze, Clear Smog remove the Defense boost
- **Bypassing**: Critical hits ignore the Defense boost
- **Special Attacks**: Only boosts physical Defense, not Special Defense
- **Stat Prevention**: Clear Body variants prevent the boost entirely

### Synergies
- **Assault Vest**: Complements special bulk with physical bulk
- **Rocky Helmet**: Enhanced damage reflection with higher Defense
- **Leftovers**: Sustainable recovery for defensive roles
- **Protective Moves**: Works well with Protect, Substitute strategies

### Version History
- **Elite Redux**: Part of the Embody Aspect ability series for Ogerpon forms
- **Original Inspiration**: Based on Dauntless Shield from official Pokemon games
- **Implementation**: Uses shared code with Dauntless Shield for consistency
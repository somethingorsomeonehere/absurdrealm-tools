---
id: 738
name: Rude Awakening
status: reviewed
character_count: 119
---

# Rude Awakening - Ability ID 738

## In-Game Description
"Raises all stats becomes immune to sleep after waking up."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon awakening, the user permanently gains immunity to sleep status and boosts all stats by one stage. Once per battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rude Awakening is a triggered ability that provides both defensive immunity and offensive stat boosts after experiencing sleep. The ability has two distinct phases: dormant (before waking up) and active (after first wake-up).

### Activation Conditions
- **Trigger requirement**: Pokemon must wake up from sleep status
  - Natural wake-up (sleep turns expire)
  - Forced wake-up (hit by physical move while sleeping)
  - Cure from items or moves (Awakening, Chesto Berry, Heal Bell, etc.)
- **One-time activation**: Only triggers once per battle on first wake-up
- **Persistent effect**: Once activated, effects remain for entire battle

### Phase 1: Dormant State
- **Sleep vulnerability**: Can be put to sleep normally
- **No stat boosts**: Functions as normal Pokemon
- **State tracking**: Ability monitors for sleep status removal

### Phase 2: Active State (Post-Awakening)
- **Sleep immunity**: Cannot be put to sleep by any means
- **Status cleansing**: Sleep status is immediately removed if applied
- **Stat enhancement**: All stats receive permanent boost (likely +1 stage each)

### Technical Implementation
```c
// Current implementation in abilities.cc
constexpr Ability RudeAwakening = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_SLEEP)
        CHECK(GetAbilityState(battler, ability))  // Only immune after awakening
        return TRUE;
    },
    .removesStatusOnImmunity = TRUE,
};
```

### Ability State Mechanics
- **GetAbilityState(battler, ability)**: Returns TRUE if Pokemon has awakened once
- **State persistence**: Ability state remains set for entire battle
- **Immunity activation**: Sleep immunity only works when state is active

### Important Interactions
- **Sleep Talk**: Can still use while initially sleeping
- **Rest**: Using Rest will activate the ability upon waking
- **Comatose**: Doesn't interact as Comatose prevents all status
- **Mold Breaker**: Can potentially bypass immunity if ability is suppressed
- **Status cure items**: Awakening items will trigger the ability

### Strategic Implications
- **Risk/reward design**: Must accept sleep vulnerability to gain benefits
- **One-time activation**: Strategic timing of when to first sleep matters
- **Permanent benefits**: Strong late-game scaling once activated
- **Sleep punishment**: Turns sleep moves against the user into a benefit
- **Counterplay options**: Opponents may avoid using sleep moves

### Optimal Usage
- **Early sleep**: Deliberately get slept early to activate benefits
- **Rest strategy**: Use Rest for recovery and ability activation
- **Sleep absorber**: Switch into predicted sleep moves
- **Late-game setup**: Become immune to sleep disruption for sweeps

### Competitive Considerations
- **Meta impact**: Reduces effectiveness of sleep-based strategies
- **Team synergy**: Pairs well with setup sweepers
- **Timing windows**: Opponents have limited time to use sleep moves
- **Baiting potential**: Can bait sleep moves to gain advantage

### Counters
- **Non-status disruption**: Use other status effects or disruption
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Early pressure**: Apply pressure before ability activation
- **Sleep avoidance**: Don't use sleep moves against this ability
- **Stat reduction**: Lower stats after boost with moves like Charm

### Synergies
- **Setup moves**: Combine with Swords Dance, Nasty Plot, etc.
- **Status Orb**: Hold Flame/Toxic Orb to avoid accidental sleep
- **Speed control**: Priority moves to capitalize on stat boosts
- **Coverage moves**: Benefit from attack/special attack boosts
- **Bulk increases**: Defensive stat boosts improve survivability

### Design Philosophy
Rude Awakening represents a unique "punishment reversal" ability that turns a negative status condition into a permanent advantage. The design encourages strategic sleep timing while providing counterplay through the initial vulnerability window.

### Version History
- Custom Elite Redux ability
- Designed to provide sleep counterplay while maintaining strategic depth
- Part of the expanded ability roster in Elite Redux's comprehensive battle system

### Notes on Implementation Status
The current code implementation shows only the sleep immunity portion. The stat boost component mentioned in the description may be implemented through additional callbacks not visible in the current ability definition, or may be handled by battle script commands triggered when the ability state is first set.
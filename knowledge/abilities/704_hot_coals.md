---
id: 704
name: Hot Coals
status: reviewed
character_count: 223
---

# Hot Coals - Ability ID 704

## In-Game Description
"Sets a trap that burns the next foe that switches in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets a burning trap on the opponent's side when the user switches in. The next opposing Pokemon that switches in will be burned if they are grounded and can be burned. Consumed when triggered. Does not stack multiple traps.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Hot Coals is an entry hazard ability that creates a one-time burning trap on the opponent's side of the field. Unlike traditional entry hazards, it only affects the next Pokemon that switches in and is immediately consumed upon activation.

### Activation Conditions
- **Entry trigger**: Activates when the Pokemon with Hot Coals switches into battle
- **Target side**: Sets trap on the opposing team's side (opposite side from the user)
- **Single use**: The trap only affects the next switch-in and is then removed
- **No stacking**: Multiple Hot Coals users don't stack additional traps

### Trap Mechanics
The Hot Coals trap triggers when an opposing Pokemon switches in and meets these conditions:
- **Grounded requirement**: The switching Pokemon must be grounded (not Flying-type or with Levitate)
- **Burn susceptibility**: The target must be able to be burned (not Fire-type, not already statused with burn immunity)
- **Hazard susceptibility**: Normal hazard immunity doesn't apply, but Magic Guard prevents activation

### Technical Implementation
```c
// Hot Coals sets trap on entry
constexpr Ability HotCoals = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gSideTimers[BATTLE_OPPOSITE(battler)].hotCoals)
        gSideTimers[BATTLE_OPPOSITE(battler)].hotCoals = TRUE;
        return SwitchInAnnounce(B_MSG_SWITCHIN_HOT_COALS);
    },
};

// Trap triggers when opponent switches in (HAZARD_MODE_FIRE_TRAP)
// Burns the switching Pokemon if conditions are met
// Trap is consumed regardless of whether burn is applied
```

### Burn Application
When the trap triggers:
1. **Trap check**: Verifies the trap exists and target is affected by hazards
2. **Grounding check**: Target must be grounded (touching the ground)
3. **Trap consumption**: The hotCoals timer is set to FALSE, removing the trap
4. **Burn attempt**: If the target can be burned, burn status is applied
5. **Battle script**: Displays appropriate messages for trap activation

### Important Interactions
- **One-time use**: Unlike Spikes or Stealth Rock, only affects one switch-in
- **Immediate consumption**: Trap is removed even if the burn fails to apply
- **Grounding requirement**: Flying-types and Levitate users are immune
- **Fire-type immunity**: Fire-types cannot be burned by the trap
- **Existing status**: Pokemon with existing status conditions cannot be burned
- **Magic Guard**: Prevents the burning effect but still consumes the trap

### Trap Removal
The Hot Coals trap can be removed by:
- **Natural consumption**: Triggering on a switch-in (whether burn applies or not)
- **Rapid Spin**: Clears the trap along with other hazards
- **Defog**: Removes the trap from the targeted side
- **Court Change**: Swaps trap to the other side
- **Pickup ability**: Clears all hazards including Hot Coals
- **Certain Fighting-type moves**: Some abilities can clear hazards when hit by Fighting moves

### Strategic Implications
- **Entry hazard role**: Functions as a deterrent to switching
- **Burn pressure**: Forces opponents to consider burn status when switching
- **Limited duration**: Unlike traditional hazards, only gets one use
- **Momentum tool**: Can punish aggressive switching strategies
- **Setup support**: Burns can support physical walls or damage dealers

### Comparison to Other Hazards
- **Stealth Rock**: Hot Coals affects all types equally but only once
- **Spikes**: Hot Coals causes status instead of direct damage
- **Toxic Spikes**: Both apply status, but Hot Coals is single-use
- **Sticky Web**: Hot Coals applies burn instead of Speed reduction

### Common Users
Hot Coals is typically found on:
- Fire-type Pokemon with trapping themes
- Support Pokemon that can switch in frequently
- Lead Pokemon designed to set early pressure
- Pivoting Pokemon that can reset the trap

### Competitive Usage Notes
- **Early game pressure**: Best used early to punish opponent's initial switches
- **Pivot synergy**: Works well with U-turn/Volt Switch users who can reset it
- **Burn support**: Helps physical walls by weakening physical attackers
- **Mind games**: Forces opponents to consider which Pokemon to switch in
- **Limited impact**: Less valuable in late game when switching is reduced

### Counters
- **Fire-types**: Immune to burn status from the trap
- **Flying/Levitate**: Immune due to not being grounded
- **Status immunity**: Pokemon that cannot be statused
- **Rapid Spin/Defog**: Can clear the trap before it triggers
- **Magic Guard**: Immune to indirect status effects
- **Substitute**: May protect from the burning effect

### Synergies
- **Burn punish**: Pairs with moves that benefit from burned opponents
- **Physical walls**: Supports defensive strategies against physical attackers
- **Pivot moves**: U-turn/Volt Switch can reset the trap multiple times
- **Status orb**: Can be combined with Flame Orb strategies for team control
- **Pressure builds**: Works with stall teams that force frequent switching

### Version History
- New ability introduced in Elite Redux
- Functions as a unique single-use entry hazard
- Provides Fire-types with an interesting support option
- Part of the expanded trapping and hazard mechanics in Elite Redux
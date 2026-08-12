---
id: 496
name: Wishmaker
status: reviewed
character_count: 147
---

# Wishmaker - Ability ID 496

## In-Game Description
"Uses Wish on entry 3 times per battle."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Wish on entry, setting up delayed healing that restores half of the current ally's max HP on the following turn. Activates 3 times per battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Wishmaker provides automatic access to the Wish move upon entry, creating delayed healing without requiring turn investment or move slot dedication. The ability has a battle-long usage limit for balance.

### Activation Conditions
- **Trigger**: Automatically activates when switching into battle
- **Usage limit**: Maximum 3 activations per battle
- **Move used**: Wish (restores 50% max HP after 1 turn delay)
- **Persistence**: Usage counter persists across switches and status
- **Reset**: Counter resets only when the battle ends

### Technical Implementation
```c
constexpr Ability Wishmaker = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(GetSingleUseAbilityCounter(battler, ability) < 3)
        SetSingleUseAbilityCounter(battler, ability, 
            GetSingleUseAbilityCounter(battler, ability) + 1);
        return UseEntryMove(battler, ability, MOVE_WISH, 0);
    },
    .persistent = TRUE,  // Counter persists across switches
};
```

### Wish Move Mechanics
- **Type**: Normal
- **Category**: Status
- **Effect**: Heals 50% of user's maximum HP
- **Delay**: Takes effect at the end of the next turn
- **Self-targeting**: Always heals the user, not allies
- **Reliability**: Cannot miss or fail once activated

### Usage Counter System
- **Initial state**: 0 uses remaining at battle start
- **Increment**: +1 each time ability activates
- **Limit check**: Ability fails if counter ≥ 3
- **Persistence**: Counter maintained across switches, status, fainting
- **Reset**: Only resets when leaving battle entirely

### Strategic Applications
- **Entry healing**: Guarantees healing without turn investment
- **Switch-in safety**: Provides recovery for risky switches
- **Stall support**: Enhances defensive strategies
- **HP management**: Helps maintain crucial HP thresholds
- **Pivot utility**: Safe switching with healing benefit

### Timing Considerations
**Turn 1 (switch-in):**
- Wishmaker activates Wish
- Counter increments to 1
- No immediate healing

**Turn 2:**
- Wish healing takes effect (50% max HP restored)
- Can act normally while receiving healing

### Usage Strategy
**First activation (early game):**
- Safe switch-in healing
- Establishes presence without risk

**Second activation (mid-game):**
- Emergency healing during pressure
- Maintains crucial HP for abilities/items

**Third activation (late game):**
- Final emergency healing
- Must be used strategically

### Competitive Applications
- **Defensive walls**: Enhanced staying power
- **Pivot Pokemon**: Safe switching with recovery
- **Status absorbers**: Can afford status with healing
- **Setup sweepers**: Healing support during setup
- **Stall teams**: Additional recovery layer

### Synergies
**Item combinations:**
- Leftovers: Stack passive healing effects
- Rocky Helmet: Tank hits while healing
- Choice items: Healing compensates for lock-in risk

**Ability combinations (in 4-ability system):**
- Regenerator: Multiple forms of switching recovery
- Natural Cure: Status removal + healing
- Magic Guard: Prevents indirect damage while healing

### Limitations
- **Usage cap**: Only 3 uses per battle total
- **Delayed healing**: No immediate HP recovery
- **Turn investment**: Requires switching to activate
- **Predictable**: Opponent knows healing is coming
- **Battle-long limit**: Cannot exceed 3 uses regardless of duration

### Counters
- **Heal Block**: Prevents Wish healing entirely
- **Fast offense**: Overwhelm before healing matters
- **Taunt**: Doesn't affect entry activation but limits options
- **Pressure**: Force frequent switching to waste uses
- **Status moves**: Poison/burn can offset healing

### Optimal Usage Patterns
**Conservative play:**
- Save uses for critical moments
- Use only when below 50% HP
- Preserve for late-game scenarios

**Aggressive play:**
- Use early for safe switches
- Enable riskier plays with healing backup
- Trade uses for battlefield advantage

### Team Building Considerations
- **Switching games**: Excellent for pivot-heavy teams
- **Defensive cores**: Provides additional recovery layer
- **Stall teams**: Enhances passive defensive strategies
- **Balanced teams**: Safety net for key Pokemon

### Version History
- Elite Redux custom ability for enhanced recovery options
- Limited usage prevents infinite healing loops
- Designed to reward strategic switch timing
- Part of expanded utility ability system
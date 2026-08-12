---
id: 443
name: Gravity Well
status: reviewed
character_count: 243
---

# Gravity Well - Ability ID 443

## In-Game Description
"Sets Gravity on entry for 5 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets Gravity upon entering battle for 5 turns. Gravity prevents levitating moves like Fly; grounds all Pokemon making them vulnerable to Ground moves, Arena Trap, and hazards; boosts Grav Apple's damage by 50%; and boosts move accuracy by 66%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Gravity Well is a field-setting ability that automatically establishes the Gravity field condition when the Pokemon enters battle. The ability creates a 5-turn field effect that fundamentally alters the battle environment.

### Activation Conditions
- **Entry trigger**: Activates immediately when the Pokemon enters battle
- **Field check**: Only activates if Gravity is not already active
- **Duration**: Sets Gravity for exactly 5 turns (GRAVITY_DURATION)
- **Priority**: Triggers before other entry abilities

### Gravity Field Effects
The Gravity field established by this ability has multiple mechanics:

1. **Move Prevention**: Completely prevents the use of specific moves:
   - Bounce
   - Fly
   - Flying Press
   - High Jump Kick
   - Jump Kick
   - Magnet Rise
   - Sky Drop
   - Splash
   - Telekinesis
   - Floaty Fall
   - Seismic Toss

2. **Grounding Effects**: Forces all airborne Pokemon to become grounded:
   - Removes Levitate ability immunity to Ground moves
   - Grounds Flying-type Pokemon
   - Affects Pokemon with Air Balloon
   - Grounds Pokemon affected by Magnet Rise or Telekinesis

3. **Accuracy Boost**: Increases accuracy of all moves (traditional Gravity effect)

4. **Type Effectiveness**: Allows Ground-type moves to hit Flying-type Pokemon

### Technical Implementation
```c
constexpr Ability GravityWell = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gFieldStatuses & STATUS_FIELD_GRAVITY)
        
        gFieldTimers.started.gravity = TRUE;
        gFieldTimers.gravityTimer = GRAVITY_DURATION;  // 5 turns
        gFieldStatuses |= STATUS_FIELD_GRAVITY;
        BattleScriptPushCursorAndCallback(BattleScript_GravityStarts);
        return TRUE;
    },
};
```

### Field Duration and Management
- **Timer**: Uses GRAVITY_DURATION constant (5 turns)
- **Field status**: Sets STATUS_FIELD_GRAVITY flag
- **Timer management**: Handled by gFieldTimers.gravityTimer
- **End message**: Triggers BattleScript_GravityEnds when expired

### Important Interactions
- **Ability blocking**: Clueless ability on field prevents Gravity effects
- **Move validation**: Affected moves show "prevented by Gravity" message
- **Turn counting**: Gravity countdown occurs during end-of-turn processing
- **Stacking**: Cannot stack with existing Gravity (ability only triggers if no Gravity active)

### Strategic Applications
- **Type coverage**: Enables Ground moves to hit Flying types
- **Move restriction**: Shuts down key Flying moves and evasion strategies
- **Accuracy boost**: Improves reliability of all moves on field
- **Field control**: Establishes battlefield advantage for 5 turns
- **Switch punishment**: Activates on every switch-in if Gravity expires

### Synergies
- **Ground-type moves**: Earthquake, Earth Power now hit Flying types
- **High-accuracy moves**: Benefit from additional accuracy boost
- **Heavy Pokemon**: Synergizes with Weight-based moves
- **Trapping moves**: Prevents Fly/Bounce escape options

### Counters
- **Field replacement**: Setting other room effects (Trick Room, Wonder Room)
- **Clueless ability**: Completely negates Gravity effects
- **Duration waiting**: Gravity only lasts 5 turns
- **Gravity immunity**: Some abilities or items may provide immunity

### Competitive Usage
- **Lead potential**: Excellent on lead Pokemon for immediate field control
- **Support role**: Enables Ground-type teammates
- **Anti-meta**: Counters Flying-type dominant strategies
- **Pivot control**: Limits opponent's mobility options
- **Setup enabler**: Creates favorable conditions for Ground-type sweepers

### Common Users
- Pokemon with strong Ground-type moves
- Bulky support Pokemon that can utilize the field
- Pokemon designed for field control strategies
- Tanks that benefit from limiting opponent options

### Version History
- Custom Elite Redux ability (ID 443)
- Provides automatic Gravity field setting
- Balances powerful field control with limited 5-turn duration
- Designed for strategic team building around field effects
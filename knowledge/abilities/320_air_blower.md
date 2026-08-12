---
id: 320
name: Air Blower
status: reviewed
character_count: 153
---

# Air Blower - Ability ID 320

## In-Game Description
"Casts a 3-turn Tailwind on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Air Blower automatically sets up a 3-turn Tailwind upon entering battle, doubling the Speed of all Pokemon on the user's side. Also activates Wind Rider.

## Detailed Mechanical Explanation

### Overview
Air Blower is a team support ability that automatically establishes favorable speed control upon entering battle. By casting a 3-turn Tailwind effect, it provides immediate strategic advantage to the entire team.

### Mechanical Details

### Core Functionality
- **Trigger**: Activates automatically when the Pokemon enters battle
- **Duration**: Creates a 3-turn Tailwind effect
- **Speed Boost**: Doubles the Speed stat of all Pokemon on the user's side
- **Stacking**: Cannot activate if Tailwind is already in effect

### Implementation Details
- **Constant**: `ABILITY_AIR_BLOWER` (ID: 320)
- **Timer**: Uses `TAILWIND_DURATION_SHORT` (3 turns)
- **Side Effect**: Sets `SIDE_STATUS_TAILWIND` flag
- **Battle Script**: `BattleScript_AirBlowerActivated`

### Speed Calculation Integration
The Tailwind effect integrates into the core speed calculation system:
```c
if (gSideStatuses[GET_BATTLER_SIDE(battlerId)] & SIDE_STATUS_TAILWIND)
    speed *= 2;
```

## Synergies and Interactions

### Wind Rider Synergy
- **Ability Interaction**: Wind Rider Pokemon on the same side receive an Attack boost when Tailwind activates
- **Strategic Value**: Enables dual setup (Speed + Attack) for team sweeping potential
- **Implementation**: `DisableSwitchInAbility(battler, ABILITY_WIND_RIDER)` prevents activation conflicts

### Wind Power Synergy  
- **Similar Effect**: Wind Power also benefits from Tailwind activation
- **Team Composition**: Enables multiple Wind-based ability users to benefit simultaneously

## Strategic Applications

### Speed Control Teams
- **Entry Hazard Support**: Ensures faster Stealth Rock/Spikes setup
- **Revenge Killing**: Enables slower Pokemon to outspeed threats
- **Sweeper Support**: Provides speed boost for offensive Pokemon

### Double Battles
- **Immediate Impact**: Both team members benefit from turn 1 speed doubling  
- **Synergy Potential**: Enables Wind Rider partner to gain Attack boost simultaneously
- **Field Control**: Establishes early battle momentum

## Limitations and Counterplay

### Activation Restrictions
- **No Stacking**: Cannot activate if Tailwind is already present on the field
- **One-Time Use**: Only activates on initial entry, not on subsequent switches
- **Turn Dependency**: Effect diminishes over 3 turns with standard turn progression

### Counterplay Options
- **Switch-Based**: Forcing switches can waste Tailwind turns
- **Priority Moves**: High-priority moves can still threaten despite speed advantage  
- **Trick Room**: Speed reversal negates the benefit entirely

## Pokemon Distribution

Air Blower appears on numerous Pokemon throughout the Elite Redux roster, including:
- Flying-type Pokemon (thematic fit)
- Speed-oriented Pokemon requiring setup support
- Team support Pokemon designed for enabling strategies
- Some Pokemon as innate abilities for balanced team composition

## Competitive Viability

### Strengths
- **Immediate Impact**: No setup turns required
- **Team Benefit**: Supports entire team strategy
- **Synergy Potential**: Enables multi-ability combinations
- **Momentum Building**: Creates favorable positioning from turn 1

### Weaknesses  
- **Limited Duration**: Only 3 turns of effect
- **Situational Value**: Less useful when already ahead in speed
- **Switch Vulnerability**: Switching out wastes remaining turns

## Technical Implementation

### Code Structure
```c
constexpr Ability AirBlower = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gSideStatuses[GetBattlerSide(battler)] & SIDE_STATUS_TAILWIND) 
        int side = GetBattlerSide(battler);
        gSideTimers[side].started.tailwind = TRUE;
        gSideStatuses[side] |= SIDE_STATUS_TAILWIND;
        gSideTimers[side].tailwindBattlerId = battler;
        gSideTimers[side].tailwindTimer = TAILWIND_DURATION_SHORT;

        DisableSwitchInAbility(battler, ABILITY_WIND_RIDER);
        DisableSwitchInAbility(BATTLE_PARTNER(battler), ABILITY_WIND_RIDER);

        BattleScriptPushCursorAndCallback(BattleScript_AirBlowerActivated);
        return TRUE;
    },
};
```

### Battle Message
The ability displays "AIRBLOWERACTIVATED" string when triggered, followed by the standard Tailwind setup message.

## Design Philosophy

Air Blower represents Elite Redux's approach to immediate team support abilities. Rather than requiring setup turns or specific conditions, it provides instant strategic value while maintaining clear limitations to prevent overpowered scenarios. The synergy with Wind-based abilities creates interesting team building opportunities without being mandatory for effectiveness.
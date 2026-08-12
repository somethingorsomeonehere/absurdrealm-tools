---
id: 737
name: Life Steal
status: reviewed
character_count: 127
---

# Life Steal - Ability ID 737

## In-Game Description
"Steals 1/10 HP from foes each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Drains 1/10 of each active opponent's max HP at the end of every turn and restores that amount to the user. Ignores Substitute.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Life Steal is an aggressive end-of-turn ability that drains HP from all opposing Pokemon and heals the user. It provides both offensive pressure and defensive recovery, making it valuable for both offensive and defensive builds.

### Activation Conditions
- **Timing**: Activates at the end of each turn
- **Targets**: All living opponents on the opposing side
- **HP calculation**: Drains exactly 1/10 (10%) of each target's maximum HP
- **Recovery**: User gains HP equal to the total amount drained from all targets

### Technical Implementation
```c
// Life Steal implementation from abilities.cc
constexpr Ability LifeSteal = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        int any = FALSE;
        for (int target = GetOppositeSide(battler); target < gBattlersCount; target += 2) {
            FILTER(IsBattlerAlive(target))
            FILTER_NOT(IsMagicGuardProtected(target))
            
            gStackBattler1 = battler;
            gStackBattler2 = target;
            gHitMarker |= HITMARKER_IGNORE_SUBSTITUTE | HITMARKER_PASSIVE_DAMAGE | HITMARKER_IGNORE_DISGUISE;
            BattleScriptExecute(BattleScript_AbilityDrainsHp);
            any = TRUE;
        }
        return any;
    },
};
```

### Battle Script Details
The ability uses `BattleScript_AbilityDrainsHp` which:
- Calculates damage as `hpfractiontodamage BS_STACK_2, 10` (1/10 max HP)
- Displays message: "{B_ATK_NAME_WITH_PREFIX} drains {B_DEF_NAME_WITH_PREFIX}'s health!"
- Updates HP bars and damage values
- Calls `BattleScript_AbsorbLeech` for the healing effect

### Important Interactions
- **Magic Guard protection**: Cannot drain HP from Pokemon with Magic Guard
- **Substitute bypass**: Ignores substitute protection (HITMARKER_IGNORE_SUBSTITUTE)
- **Disguise bypass**: Ignores Disguise protection (HITMARKER_IGNORE_DISGUISE)
- **Passive damage**: Marked as passive damage, affecting certain interactions
- **Multi-target**: Hits all living opponents, potentially draining massive HP in doubles
- **Type immunity**: Ignores type-based immunities

### Damage Calculations
- **Single opponent**: Drains 10% of opponent's max HP, heals user for same amount
- **Double battle**: Can drain from both opponents (up to 20% combined healing)
- **Maximum HP based**: Always drains based on target's max HP, not current HP
- **Minimum damage**: No minimum damage requirement - always drains exactly 10%

### Strategic Implications
- **Offensive pressure**: Continuous damage every turn without user action
- **Defensive recovery**: Provides consistent healing for longevity
- **Multi-target advantage**: Extremely powerful in double battles
- **Setup synergy**: Allows setup while still applying pressure
- **Anti-stall**: Counters defensive strategies with guaranteed damage
- **HP management**: Helps maintain high HP for abilities that require it

### Counters and Limitations
- **Magic Guard**: Completely blocks the HP drain
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Fainting**: No effect if all opponents are fainted
- **Heal Block**: May prevent the user from recovering HP (needs verification)
- **Weather**: Unaffected by weather conditions

### Synergies
- **Leftovers/Black Sludge**: Stacks with item-based recovery
- **Substitute**: Can hide behind substitute while draining
- **Status moves**: Free turns to set up while still dealing damage
- **Bulky builds**: Maximizes the healing received each turn
- **Double battles**: Potentially drain from multiple targets

### Competitive Usage Notes
- **Doubles powerhouse**: Incredibly strong in double battle formats
- **Stall breaker**: Forces progress in defensive matchups
- **Setup enabler**: Allows free setup turns with guaranteed value
- **HP threshold maintenance**: Helps stay above percentage-based thresholds
- **Late game pressure**: Becomes more impactful as battles progress

### Version History
- Elite Redux exclusive ability
- Part of the extended ability roster
- Designed for consistent end-of-turn value
- Balanced around Magic Guard counterplay

### Common Users
- Bulky Pokemon that benefit from consistent recovery
- Setup sweepers that need time to boost
- Pokemon with other abilities that synergize with HP management
- Doubles-focused Pokemon for maximum impact
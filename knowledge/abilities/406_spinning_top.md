---
id: 406
name: Spinning Top
status: reviewed
character_count: 111
---

# Spinning Top - Ability ID 406

## In-Game Description
"Fighting moves up speed +1 and clear hazards."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Spinning Top grants +1 Speed and removes all entry hazards from the user's side when using Fighting-type moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Spinning Top is an offensive ability that provides dual benefits when using Fighting-type moves: speed boosting and hazard removal. Both effects trigger after successfully landing a Fighting-type attack.

### Activation Conditions
- **Move type requirement**: Must use a Fighting-type move
- **Hit requirement**: The move must successfully connect (ShouldApplyOnHitAffect)
- **Once per turn**: Can only activate once per turn per Pokemon
- **Timing**: Activates after the Fighting move deals damage

### Effects Applied
1. **Speed Boost**: +1 stage increase to Speed stat
2. **Hazard Removal**: Clears all entry hazards from user's side:
   - Stealth Rock
   - Spikes (all layers)
   - Toxic Spikes (all layers)
   - Sticky Web
   - Hot Coals
   - Caltrops

### Technical Implementation
```c
constexpr Ability SpinningTop = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(moveType == TYPE_FIGHTING)
        CHECK(CheckAndSetOncePerTurnAbility(battler, ability))

        int any = FALSE;
        // Clear hazards if any exist
        if (gSideStatuses[GetBattlerSide(battler)] & SIDE_STATUS_HAZARDS_ANY || 
            gSideTimers[GetBattlerSide(battler)].hotCoals ||
            gSideTimers[GetBattlerSide(battler)].caltrops) {
            
            // Remove all hazard flags
            gSideStatuses[GetBattlerSide(battler)] &=
                ~(SIDE_STATUS_STEALTH_ROCK | SIDE_STATUS_TOXIC_SPIKES | 
                  SIDE_STATUS_SPIKES_DAMAGED | SIDE_STATUS_STICKY_WEB);
            gSideTimers[GetBattlerSide(battler)].hotCoals = FALSE;
            gSideTimers[GetBattlerSide(battler)].caltrops = FALSE;
            
            BattleScriptCall(BattleScript_AnnounceRemovedHazards);
            gBattleScripting.battler = battler;
            any = TRUE;
        }

        // Apply speed boost
        if (ChangeStatBuffs(battler, 1, STAT_SPEED, MOVE_EFFECT_AFFECTS_USER, NULL)) {
            gBattleScripting.battler = battler;
            BattleScriptCall(BattleScript_AttackBoostActivates);
            any = TRUE;
        }

        return any;
    },
};
```

### Important Interactions
- **Multi-hit moves**: Each hit can potentially trigger the ability, but once-per-turn limit applies
- **Status moves**: Fighting-type status moves also trigger the ability
- **STAB bonus**: Fighting-type users get additional damage from STAB
- **Contact requirement**: No contact requirement - works with all Fighting moves
- **Priority moves**: Works with priority Fighting moves like Mach Punch
- **Substitute**: Works even when attacking through Substitute

### Hazard Removal Details
- **Complete clearing**: Removes all layers of multi-layer hazards (Spikes, Toxic Spikes)
- **Immediate effect**: Hazards are cleared before the user can be affected by them
- **Side-specific**: Only clears hazards from the user's side, not the opponent's
- **Visual feedback**: Displays "The hazards were blown away!" message

### Speed Boost Mechanics
- **Stat stage**: Standard +1 Speed boost (50% increase)
- **Cumulative**: Can stack with other speed boosts
- **Battle-specific**: Boost is lost when switching out
- **Cap limit**: Cannot boost beyond +6 Speed stages

### Strategic Implications
- **Hazard immunity**: Essentially immune to entry hazards while using Fighting moves
- **Speed control**: Can outspeed threats after one Fighting move
- **Setup potential**: Combines well with other stat-boosting moves
- **Lead breaking**: Excellent for breaking through hazard-setting leads
- **Late-game sweeping**: Speed boosts accumulate for powerful late-game sweeps

### Common Users
- **Fighting-type attackers**: Natural STAB users benefit most
- **Physical sweepers**: Often learn Fighting moves for coverage
- **Anti-lead Pokemon**: Excel at breaking hazard-setting leads
- **Mixed attackers**: Can use both physical and special Fighting moves

### Competitive Usage Notes
- **Hazard meta counter**: Directly counters hazard-heavy teams
- **Speed tier jumping**: Allows outspeeding specific threats after one boost
- **Multi-role ability**: Provides both utility and offensive presence
- **Fighting move dependency**: Requires running Fighting-type moves to activate
- **Once per turn limit**: Cannot spam the effect with multi-hit moves

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas prevent activation
- **Non-Fighting moves**: Ability doesn't activate without Fighting moves
- **Speed control**: Thunder Wave, Trick Room can counter speed boosts
- **Phasing moves**: Roar, Whirlwind remove speed boosts
- **Priority moves**: Can still be outsped by priority even with boosts

### Synergies
- **Fighting-type STAB**: Natural synergy with Fighting-type Pokemon
- **Close Combat**: High-power move that triggers ability despite stat drops
- **Mach Punch**: Priority Fighting move for immediate benefit
- **Rapid Spin**: Similar hazard removal concept (though different type)
- **Speed boosting items**: Choice Scarf can stack with ability boosts

### Elite Redux Specific Notes
- **Extended hazard types**: Includes Hot Coals and Caltrops beyond standard hazards
- **Battle message**: Uses pickup activation string for hazard removal announcement
- **Implementation**: Part of the modern ability system with lambda functions
- **Balance consideration**: Powerful utility ability that shapes the hazard metagame

### Version History
- **Elite Redux original**: Custom ability created for the Elite Redux romhack
- **Modern implementation**: Uses constexpr lambda-based ability system
- **Unique mechanics**: Combines speed boosting with hazard removal in one ability
- **Meta impact**: Significantly affects hazard usage in Elite Redux competitive play
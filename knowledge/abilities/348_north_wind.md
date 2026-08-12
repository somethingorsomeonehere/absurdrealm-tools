---
id: 348
name: North Wind
status: reviewed
character_count: 266
---

# North Wind - Ability ID 348

## In-Game Description
"Automatically sets up Aurora Veil upon entry and immune to Hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets up Aurora Veil upon entering battle, cutting physical and special damage recieved by half for your entire team. Aurora Veil lasts 3 turns, or 5 turns with Light Clay. The user is also immune to Hail damage. Cannot trigger again if Aurora Veil is already active.

## Detailed Mechanical Explanation

### Overview

North Wind is an extremely powerful defensive ability that automatically sets up Aurora Veil upon entering battle. This ability provides immediate team support by reducing damage from both physical and special attacks by 50% for the user's entire team. Additionally, the user gains complete immunity to Hail damage, making it synergistic with Hail-based strategies.

## Mechanics

### Aurora Veil Setup
- **Duration**: 3 turns (base) or 5 turns if holding Light Clay
- **Effect**: Reduces damage from both physical and special attacks by 50%
- **Scope**: Affects the entire team on the user's side
- **Stacking**: Cannot be activated if Aurora Veil is already active

### Hail Immunity
- Complete immunity to Hail damage (1/16 HP per turn normally)
- Does not prevent other Hail effects or abilities from activating
- Allows safe switching in Hail weather conditions

## Code Implementation

### Primary Implementation
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
**Lines**: 3678-3694

```cpp
constexpr Ability NorthWind = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gSideStatuses[GetBattlerSide(battler)] & SIDE_STATUS_AURORA_VEIL)

        int side = GetBattlerSide(battler);
        gSideTimers[side].started.auroraVeil = TRUE;
        gSideStatuses[side] |= SIDE_STATUS_AURORA_VEIL;
        if (GetBattlerHoldEffect(battler, TRUE) == HOLD_EFFECT_LIGHT_CLAY)
            gSideTimers[side].auroraVeilTimer = SCREEN_DURATION;
        else
            gSideTimers[side].auroraVeilTimer = SCREEN_DURATION_SHORT;
        BattleScriptPushCursorAndCallback(BattleScript_NorthWindActivated);

        return TRUE;
    },
    .hailImmune = TRUE,
};
```

### Constants
- `SCREEN_DURATION_SHORT = 3` (base Aurora Veil duration)
- `SCREEN_DURATION = 5` (Light Clay extended duration)

### Battle Message
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_message.c`
**Message**: "{B_ACTIVE_NAME_WITH_PREFIX}'s North Wind set up Aurora Veil!"

## Strategic Applications

### Team Support
- **Immediate Protection**: Provides instant damage reduction for the entire team
- **Safe Switches**: Allows teammates to switch in more safely under Aurora Veil protection
- **Setup Opportunities**: Creates safer conditions for setting up stat boosts or hazards

### Weather Synergy
- **Hail Teams**: Perfect fit for Hail-based strategies, immune to self-damage
- **Weather Wars**: Can safely enter against opposing Hail setters
- **Mixed Weather**: Provides consistent defensive utility regardless of weather

### Light Clay Synergy
- Extends Aurora Veil from 3 to 5 turns
- Maximizes the defensive utility window
- Allows for longer-term strategic plays

## Competitive Analysis

### Strengths
- **Immediate Impact**: Activates automatically on switch-in
- **Team Wide**: Affects all teammates, not just the user
- **Versatile Defense**: Protects against both physical and special attacks
- **Weather Immunity**: Additional utility against Hail strategies
- **No Setup Required**: Unlike the Aurora Veil move, requires no turn investment

### Limitations
- **One-Time Use**: Only activates once per battle entry
- **Non-Stacking**: Cannot reactivate if Aurora Veil is already up
- **Status Moves**: Does not protect against status conditions or effects
- **Breakthrough**: Some abilities and moves can bypass damage reduction

### Comparison to Aurora Veil Move
- **Advantages**: Automatic activation, no turn cost, can't be Taunted
- **Disadvantages**: Cannot be used multiple times, no timing control

## Pokemon with North Wind

### Primary Ability Holders
- **Articuno**: Legendary Ice/Flying type, natural weather control synergy
- **Suicune**: Legendary Water type, excellent bulk to utilize Aurora Veil
- **Abomasnow**: Ice/Grass type with natural Hail synergy
- **Cryogonal**: Ice type specialist with defensive utility
- **Mr. Rime**: Ice/Psychic type with support capabilities

### Innate Ability Holders
- **Dewgong**: Ice/Water type with multiple defensive abilities
- Various other Ice-type specialists

### Strategic Considerations by Pokemon
- **Articuno**: Combines with Pressure for stall strategies
- **Suicune**: Excellent for Calm Mind setup sets
- **Abomasnow**: Natural Hail setter with immediate protection
- **Cryogonal**: Rapid Spin support with team protection

## Related Abilities and Interactions

### Similar Defensive Abilities
- **Intimidate**: Attack reduction on entry
- **Download**: Stat boost based on opponent's defenses
- **Trace**: Copies opponent's ability

### Weather-Related Abilities
- **Snow Warning**: Sets up Hail (synergizes well)
- **Sand Stream**: Sets up Sandstorm (neutral interaction)
- **Drought/Drizzle**: Overwrites beneficial Hail conditions

### Screen-Setting Abilities
- **Light Screen/Reflect**: Single-type damage reduction
- **Aurora Veil Move**: Requires Hail weather to use

## Counters and Responses

### Direct Counters
- **Brick Break**: Removes Aurora Veil completely
- **Psychic Fangs**: Also removes Aurora Veil
- **Infiltrator**: Bypasses Aurora Veil protection
- **Screen Cleaner**: Removes all screens including Aurora Veil

### Strategic Responses
- **Status Moves**: Aurora Veil doesn't prevent status conditions
- **Entry Hazards**: Damage occurs before Aurora Veil setup
- **Priority Moves**: Still hit at full power but with reduced damage
- **Multi-Hit Moves**: Each hit is reduced but can add up

## Competitive Viability

### Usage Scenarios
- **Lead Position**: Immediate team protection from the start
- **Pivot Role**: Safe switching and team support
- **Defensive Core**: Anchor for defensive team strategies
- **Weather Support**: Essential for Hail-based team compositions

### Team Building Considerations
- **Light Clay Carrier**: Maximize Aurora Veil duration
- **Setup Sweepers**: Take advantage of protected setup turns
- **Entry Hazard Setters**: Safer hazard placement under Aurora Veil
- **Status Spreaders**: Protected status move usage


## Conclusion

North Wind stands as one of the most powerful defensive abilities in Elite Redux, providing immediate and significant team-wide protection. Its combination of automatic Aurora Veil setup and Hail immunity makes it exceptionally valuable for both defensive and weather-based strategies. The ability's reliability and immediate impact make it a top-tier choice for competitive play, particularly on teams that can capitalize on the protective turns it provides.
---
id: 112
name: Slow Start
status: reviewed
character_count: 142
---

# Slow Start - Ability ID 112

## In-Game Description
"Halves Offenses and Speed during the first 5 turns out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves Attack, Special Attack, and Speed for the first 5 turns after switching in. The turn counter resets each time the Pokemon switches out. 

## Detailed Mechanical Explanation
Slow Start is a hindering ability that significantly reduces a Pokemon's offensive capabilities and speed during the initial turns of battle:

### Core Mechanics
- **Affected Stats**: Attack, Special Attack, and Speed are all halved (multiplied by 0.5)
- **Duration**: Exactly 5 turns after the Pokemon enters battle
- **Timer**: Uses `gVolatileStructs[battler].slowStartTimer` which starts at 5 and decrements each turn
- **Activation**: Triggers immediately upon switching in with an announcement message

### Implementation Details
1. **On Entry**: Sets a 5-turn timer and displays the switch-in announcement
2. **Stat Modification**: The `onStat` callback checks if the requested stat is ATK, SPATK, or SPEED, and halves it if the timer is active
3. **Turn Processing**: Each turn during `ENDTURN_SLOW_START`, the timer decrements by 1
4. **End Condition**: When the timer reaches 0, a script (`BattleScript_SlowStartEnds`) executes to notify the player

### Strategic Implications
- Requires careful timing when switching in Slow Start Pokemon
- The halved offenses make the Pokemon vulnerable during early turns
- Speed reduction can cause the Pokemon to be outsped by threats it would normally outspeed
- Works best on bulky Pokemon that can survive the initial disadvantaged turns
- Switching out resets the timer, so staying in is often preferable once switched in

### Interactions
- The timer persists through status conditions, weather, and other battle effects
- Does not affect defensive stats (Defense, Special Defense, HP)
- The stat reduction is applied at the calculation level, not as a stat stage change
- Cannot be suppressed by Mold Breaker or similar abilities since it affects the user
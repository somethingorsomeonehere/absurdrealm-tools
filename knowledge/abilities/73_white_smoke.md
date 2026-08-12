---
id: 73
name: White Smoke
status: reviewed
character_count: 103
---

# White Smoke - Ability ID 73

## In-Game Description
"Sets Smokescreen for 3 turns on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sets Smokescreen on entry, lasting 3 turns. Smokescreen increases the evasiveness of your party by 25%.

## Detailed Mechanical Explanation
*For Discord/reference use*

**WHITE SMOKE** is a defensive ability that has been completely redesigned in Elite Redux from its original stat-protection function to a smokescreen-based evasion ability.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle (onEntry hook)
- **Duration**: 3 turns standard, 5 turns with Light Clay held
- **Side Effect**: Sets SIDE_STATUS_SMOKESCREEN on the user's side
- **Script**: Displays switch-in message with smokescreen activation

### Smokescreen Effects:
1. **Evasiveness Boost**:
   - Increases evasiveness by 25% for all Pokemon on the user's side
   - Functions as a side-wide accuracy reduction for opposing moves
   - Stacks with individual evasion stat boosts

2. **Move Interactions**:
   - Affects all moves that target Pokemon on the protected side
   - Never-miss moves (like Swift) are unaffected
   - Status moves are affected by the accuracy reduction
   - Self-targeting moves are unaffected

### Interaction Rules:
- **Screen Removal**: Can be removed by Brick Break, Rapid Spin, Defog, and similar screen-clearing moves
- **Light Clay**: Extends duration from 3 to 5 turns when held by the user
- **Multiple Activations**: If multiple Pokemon with White Smoke switch in, only refreshes the timer rather than stacking
- **Court Change**: Can be swapped to the opponent's side via Court Change

### Technical Implementation:
```c
constexpr Ability WhiteSmoke = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gSideTimers[GET_BATTLER_SIDE(battler)].smokescreenTimer)

        int side = GET_BATTLER_SIDE(battler);
        gSideTimers[side].smokescreenTimer = GetBattlerHoldEffect(battler, TRUE) == ITEM_LIGHT_CLAY ? SCREEN_DURATION : SCREEN_DURATION_SHORT;
        gSideTimers[side].started.smokescreen = TRUE;
        gSideTimers[side].smokescreenBattler = battler;
        return SwitchInAnnounce(B_MSG_SWITCHIN_WHITE_SMOKE);
    },
};
```

### Competitive Analysis:
**Strengths:**
- Provides immediate defensive utility on switch-in
- Affects the entire team side, not just the user
- Can be extended with Light Clay for longer protection
- Useful for setting up or buying time for frail Pokemon

**Weaknesses:**
- Temporary effect that can be removed or expire
- Vulnerable to screen-clearing moves
- Provides no benefit against never-miss moves
- 25% accuracy reduction may not be enough against high-accuracy moves

### Comparison to Original White Smoke:
- **Original**: Prevented stat reduction from opponent's moves and abilities
- **Elite Redux**: Creates temporary evasion boost for entire team side
- **Power Level**: Similar defensive utility but more situational and temporary
- **Usage**: Better for team support, worse for individual stat protection

### Synergies:
- **Light Clay holders**: Maximize smokescreen duration
- **Evasion boosters**: Stacks with Double Team, Minimize effects
- **Setup sweepers**: Provides cover for stat-boosting moves
- **Fragile supporters**: Helps survive long enough to provide utility

### Version History:
- **Original Games**: Prevents stat reduction (Clear Body clone)
- **Elite Redux**: Complete rework to smokescreen-based evasion ability
- **Duration**: 3 turns base, extendable to 5 with Light Clay
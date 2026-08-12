---
id: 536
name: Blood Price
status: reviewed
character_count: 109
---

# Blood Price - Ability ID 536

## In-Game Description
"Does 30% more damage but lose 10% HP when attacking."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Blood Price boosts all attacking moves by 30%, but the user loses 10% of their max hp when landing an attack. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Damage Boost**: All offensive moves deal 30% more damage (1.3x multiplier)
- **HP Cost**: At the end of each turn, lose 10% of max HP (minimum 1 HP damage)
- **Activation Timing**: Damage boost applies immediately to attacks; HP loss occurs at end of turn

### Activation Conditions
- **For Damage Boost**: Applied to all offensive moves automatically
- **For HP Loss**: Only triggers if:
  - The last move used was an attacking move (not a status move)
  - The Pokemon is still alive at end of turn
  - The Pokemon is not protected by Magic Guard

### Technical Implementation
```cpp
// Damage multiplier applied to offensive moves
.onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) { MUL(1.3); },

// HP loss at end of turn
.onEndTurn = +[](ON_END_TURN) -> int {
    CHECK_NOT(IS_MOVE_STATUS(gLastResultingMoves[battler]))
    CHECK_NOT(IsMagicGuardProtected(battler))
    CHECK(IsBattlerAlive(battler))

    gBattleMoveDamage = gBattleMons[battler].maxHP / 10;
    if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
    BattleScriptPushCursorAndCallback(BattleScript_AbilitySelfDamage);
    return TRUE;
},
```

### Numerical Values
- **Damage Multiplier**: 1.3x (30% increase)
- **HP Cost**: 10% of max HP per turn (minimum 1 HP)
- **Example**: A Pokemon with 300 max HP loses 30 HP per turn after attacking

### Affected Moves
- **Boosted**: All physical, special, and multi-hit attacking moves
- **Not Affected**: Status moves (no damage boost or HP cost)
- **Multi-Hit Moves**: Get the damage boost on each hit, but HP cost only applies once per turn

### Interactions with Other Abilities/Mechanics
- **Magic Guard**: Prevents HP loss but keeps damage boost - essentially makes Blood Price a pure damage boost
- **Life Orb**: Stacks with Blood Price for 1.69x damage but double HP costs (Life Orb + Blood Price)
- **Reckless**: Stacks multiplicatively with recoil moves for extreme damage
- **Healing Moves**: Can offset the HP cost, creating interesting risk/reward gameplay

### Strategic Implications
- **Glass Cannon Strategy**: Maximizes damage output at the cost of longevity
- **Sweep Potential**: The 30% damage boost can secure KOs that would otherwise fail
- **Risk Management**: Requires careful HP management and healing support
- **Late-Game Power**: Can be devastating when you need immediate damage but don't need to survive long

### Example Damage Calculations
```
Base Move Power: 100
With Blood Price: 100 x 1.3 = 130 effective power

Pokemon with 250 Max HP:
- Turn 1: Attack deals 130 power, lose 25 HP at end of turn
- Turn 2: Attack deals 130 power, lose 25 HP at end of turn
- After 10 turns of attacking: Would have lost 250 HP (full health)
```

### Common Users
Based on species analysis, Blood Price appears on:
- Ghost-type attackers with high offensive stats
- Pokemon with innate abilities that support aggressive playstyles
- Mixed attackers that can utilize both physical and special damage boosts
- Pokemon with access to healing moves or support to offset HP costs

### Competitive Usage Notes
- **Best With**: Healing moves, Magic Guard partners, priority moves
- **Timing**: Most effective in short battles or late-game situations
- **Team Support**: Benefits from Wish support or healing items
- **Risk Assessment**: Calculate if the extra damage is worth the HP cost in each situation

### Counters
- **Residual Damage**: Pokemon already taking chip damage become extremely vulnerable
- **Status Moves**: Forcing status moves removes both benefit and cost
- **Stall Tactics**: Drawing out battles makes the HP cost unsustainable
- **Priority Moves**: Can revenge kill weakened Blood Price users

### Synergies
- **Magic Guard**: Perfect synergy - keeps damage boost, removes downside
- **Healing Moves**: Roost, Recover, Synthesis offset HP costs
- **Choice Items**: Maximize the damage boost since you're locked into attacking
- **Life Orb**: Risk/reward stacking for maximum immediate damage

### Version History
- Elite Redux custom ability
- Designed as a high-risk, high-reward damage amplifier
- Balances significant offensive power with meaningful drawback
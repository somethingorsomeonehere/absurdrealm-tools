---
id: 220
name: Soul-Heart
status: reviewed
character_count: 119
---

# Soul-Heart - Ability ID 220

## In-Game Description
"KOs dealt anywhere on the field raise Sp. Atk by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Soul-Heart raises Special Attack by one stage when any Pokemon faints on the battlefield, including allies and enemies.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Soul-Heart is a powerful stat-boosting ability that activates whenever any Pokemon faints during battle, regardless of the cause or perpetrator of the KO.

**Key Implementation Details:**
```cpp
constexpr Ability SoulHeart = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK(ChangeStatBuffs(battler, 1, STAT_SPATK, MOVE_EFFECT_AFFECTS_USER | STAT_BUFF_DONT_SET_BUFFERS, NULL))
        BattleScriptCall(BattleScript_RaiseStatOnFaintingTarget);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ANY,
};
```

### Activation Conditions
- **Trigger**: Any Pokemon fainting on the battlefield
- **Scope**: Applies to ANY battler fainting (`APPLY_ON_ANY`)
  - Allied Pokemon fainting
  - Enemy Pokemon fainting
  - The Soul-Heart user itself fainting (though this is rarely relevant)
- **Cause Independence**: Doesn't matter how the KO occurred:
  - Direct damage from moves
  - Status condition damage (poison, burn, etc.)
  - Recoil damage
  - Entry hazard damage
  - Weather damage
  - Self-KO moves like Explosion

### Numerical Values
- **Stat Boost**: +1 stage to Special Attack per activation
- **Stage Multiplier**: Each +1 stage = 1.5x Special Attack
- **Maximum**: Can stack up to +6 stages (4x Special Attack total)
- **Persistence**: Boosts remain through switches and do not reset

### Technical Implementation
The ability uses the `onBattlerFaints` hook with `APPLY_ON_ANY` scope, meaning it triggers for any battler that faints. The stat boost is applied using `ChangeStatBuffs` with a +1 modifier to `STAT_SPATK`.

### Strategic Implications
**Offensive Potential:**
- Excellent for late-game scenarios where multiple KOs have occurred
- Synergizes well with sacrifice strategies using allies
- Can quickly reach maximum Special Attack boosts in chaotic battles

**Defensive Considerations:**
- Opponents may avoid KOing allies to deny Soul-Heart boosts
- Can turn unfavorable trades into advantageous stat gains
- Particularly dangerous in multi-battle formats or long battles

### Example Scenarios
**Scenario 1 - Allied Sacrifice:**
Turn 1: Ally uses Explosion, faints to Soul-Heart user gains +1 Sp. Atk
Turn 2: Soul-Heart user sweeps with boosted attacks

**Scenario 2 - Chain KOs:**
Multiple Pokemon faint in succession due to status/hazards to Multiple Sp. Atk boosts stack

### Common Users
Notable Pokemon with Soul-Heart in Elite Redux:
- **Magearna** (primary/innate ability)
- **Wigglytuff Apex** (innate ability)
- **Gardevoir Mega** (innate ability)  
- **Xerneas/Xerneas Active** (innate ability)
- **Various Psychic/Fairy-type specialists** (changeable ability)

### Competitive Usage Notes
**Strengths:**
- Passive stat boosting requiring no setup moves
- Triggers off opponent's actions as well as allies
- Stacks indefinitely up to +6 stages
- Cannot be prevented by Taunt or similar effects

**Weaknesses:**
- Relies on KOs occurring to activate
- Useless if no Pokemon faint during battle
- Stat boosts can be reset by moves like Haze or Clear Smog
- Doesn't provide immediate benefit upon switching in

### Counters
- **Haze/Clear Smog**: Reset all stat changes
- **Roar/Whirlwind**: Force switches to waste accumulated boosts
- **Critical hits**: Ignore stat boosts when calculating damage
- **Unaware**: Ignore stat boosts when taking damage

### Synergies
**Complementary Abilities:**
- **Magic Guard** (innate): Prevents indirect damage, ensuring survival to use boosts
- **Serene Grace** (innate): Doubles secondary effect chances on boosted attacks
- **Pixilate**: Converts Normal moves to Fairy with power boost

**Team Strategies:**
- Pairs well with Explosion/Self-Destruct users
- Benefits from entry hazard stacking to cause more faints
- Effective with status spreaders causing gradual KOs

### Version History
Soul-Heart was introduced in Generation VII as Magearna's signature ability. In Elite Redux, it has been distributed to various Pokemon as both a changeable and innate ability, making it more accessible for strategic team building while maintaining its powerful late-game potential.
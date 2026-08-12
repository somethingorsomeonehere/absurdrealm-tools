---
id: 3
name: Speed Boost
status: reviewed
character_count: 140
---

# Speed Boost - Ability ID 3

## In-Game Description
"Raises own Speed by one stage after every turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

User's Speed increases by one stage at end of each full turn they remain on the field. Doesn't activate on the turn the user is switched in.

## Detailed Mechanical Explanation
*For Discord/reference use*

**SPEED BOOST** is a passive turn-based ability that provides incremental Speed boosts over time.

### Activation Mechanics:
- **Trigger**: End of turn (onEndTurn hook)
- **Timing**: After all actions, damage, and other end-of-turn effects
- **Switch-in Rule**: Does NOT activate on the turn the Pokemon enters battle (isFirstTurn != 2 check)
- **Requirement**: The Pokemon must remain active for the entire turn
- **Script**: Uses BattleScript_AttackerAbilityStatRaiseEnd3 for the "+1 Speed!" message

### Speed Stage Mechanics:
1. **Boost Amount**: Always +1 stage per turn
2. **Maximum Cap**: Stops at +6 Speed stages (MAX_STAT_STAGE = 12, default = 6)
3. **Stage Effects**: Each stage = 50% Speed increase (1.5x, 2x, 2.5x, 3x, 3.5x, 4x total)
4. **Persistence**: Boosts remain through Baton Pass but reset on switch-out

### Turn-by-Turn Progression:
- **Turn 1**: Entry - No boost (isFirstTurn = 2, decrements to 1)
- **Turn 2**: Active - No boost (isFirstTurn = 1, decrements to 0) 
- **Turn 3**: Active - First +1 Speed boost (isFirstTurn = 0)
- **Turn 4+**: +1 Speed per turn until +6 maximum

### Interaction Rules:
- **vs Clear Body/White Smoke**: Speed Boost bypasses stat reduction immunity
- **vs Contrary**: Boosts become Speed drops instead
- **vs Simple**: Each boost becomes +2 stages instead of +1
- **vs Unaware**: Speed Boost still affects turn order despite Unaware ignoring stat changes for damage
- **Baton Pass**: Speed stages transfer to the next Pokemon
- **Haze/Clear Smog**: Resets accumulated Speed boosts to 0

### Special Interactions:
- **Quick Claw/Speed Items**: Still trigger normally with boosted Speed
- **Trick Room**: Higher Speed becomes a disadvantage, making Speed Boost counterproductive
- **Tailwind**: Stacks multiplicatively with Speed Boost stages (both affect final Speed)
- **Choice Scarf**: Stacks multiplicatively (1.5x item x stage multiplier)

### Technical Implementation:
```c
constexpr Ability SpeedBoost = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK(gVolatileStructs[battler].isFirstTurn != 2)
        CHECK(ChangeStatBuffs(battler, 1, STAT_SPEED, MOVE_EFFECT_AFFECTS_USER, NULL))

        BattleScriptPushCursorAndCallback(BattleScript_AttackerAbilityStatRaiseEnd3);
        gBattleScripting.battler = battler;
        return TRUE;
    },
};
```

### Competitive Notes:
- **Setup Sweeper**: Excellent for Pokemon with strong offensive moves but mediocre initial Speed
- **Late Game Power**: Becomes increasingly threatening as battle duration extends
- **Priority Weakness**: Fast setup vulnerable to priority moves early on
- **Switch Prediction**: Opponents often force switches to reset Speed accumulation
- **Meta Impact**: Shapes team building around either supporting Speed Boost users or countering them

### Notable Users in Elite Redux:
- **Blaziken Line**: Mixed attacker that becomes progressively faster
- **Yanmega**: Special attacker with Tinted Lens + Speed Boost combination
- **Ninjask**: Pure Speed Boost + Baton Pass support
- **Sharpedo**: Hyper Offensive sweeper with Speed Boost momentum
- **Mega Blaziken**: Retains Speed Boost with enhanced offensive stats

### Version History:
- Gen 3: Introduction with Ninjask and Blaziken lines
- Gen 4+: Became highly valued in competitive play
- Elite Redux: Unchanged mechanics, but many new Pokemon gain access
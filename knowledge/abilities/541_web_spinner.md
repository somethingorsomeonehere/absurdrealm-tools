---
id: 541
name: Web Spinner
status: reviewed
character_count: 87
---

# Web Spinner - Ability ID 541

## In-Game Description
"Uses String Shot on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses String Shot on switch in, harshly lowering the Speed of all opponents by 2 stages. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Web Spinner is a switch-in ability that automatically executes String Shot when the Pokemon enters battle.

### Core Mechanics
- **Trigger**: Activates immediately upon switching into battle
- **Move Used**: String Shot (Bug-type status move)
- **Effect**: Harshly lowers Speed by 2 stages (-2 Speed)
- **Accuracy**: 100% (cannot miss)
- **PP**: Uses String Shot's base PP (20), but doesn't consume PP when triggered by ability
- **Target**: Both opposing Pokemon in double battles, single opponent in singles

### Implementation Details
```cpp
constexpr Ability WebSpinner = {
    .onEntry = +[](ON_ENTRY) -> int { return UseEntryMove(battler, ability, MOVE_STRING_SHOT, 0); },
};
```

### String Shot Move Data
- **Type**: Bug
- **Category**: Status
- **Base PP**: 20
- **Accuracy**: 100%
- **Effect**: EFFECT_SPEED_DOWN_2 (harshly lowers Speed)
- **Target**: BOTH (all opposing Pokemon)
- **Affected by**: Magic Coat, Mirror Move

### Activation Conditions
- Pokemon must successfully switch into battle
- Works on initial deployment and when switching in mid-battle
- Triggers before any other switch-in abilities or effects
- Cannot be suppressed by most ability-nullifying effects since it activates immediately

### Strategic Implications
**Offensive Usage:**
- Cripples faster sweepers and revenge killers
- Sets up for slower, powerful teammates
- Excellent for gaining speed control in battles
- Particularly effective against speed-based strategies

**Team Support:**
- Provides immediate speed control for the entire team
- Enables slower but powerful Pokemon to outspeed opponents
- Creates setup opportunities for stat-boosting moves
- Supports Trick Room strategies by lowering opponent speeds

**Counters and Limitations:**
- Taunt prevents the String Shot if used before Web Spinner activates
- Magic Coat reflects the speed drop back to the user
- Pokemon with speed-boosting abilities can potentially overcome the debuff
- Clear Body, White Smoke, and similar abilities prevent the speed reduction
- Substitute blocks the speed reduction if up before switch-in

### Competitive Viability
**Strengths:**
- Guaranteed speed control on switch-in
- No accuracy concerns (100% accurate)
- Affects multiple targets in doubles
- Cannot be prevented by most defensive measures

**Weaknesses:**
- Predictable effect allows opponents to prepare
- Doesn't deal damage, purely utility-based
- Can be turned against the user with Magic Coat
- Limited to speed control only

### Common Users
Based on the codebase analysis, Web Spinner appears on:
- **Caterpie line** (Caterpie, Metapod variants)
- **Weedle line** (Weedle, Kakuna variants) 
- **Sewaddle line** (Sewaddle, Swadloon)
- **Tarountula line** (Tarountula, Spidops)
- **Silvally** (as one of multiple ability options)
- **Joltik line** (as innate ability on some variants)

### Synergies
- **Trick Room teams**: Helps ensure Trick Room setters are slower
- **Slow sweepers**: Enables powerful but slow Pokemon to outspeed
- **Priority users**: Guarantees speed tiers for priority move effectiveness
- **Setup sweepers**: Creates safer setup opportunities

### Version History
Introduced in Elite Redux as part of the expanded ability system, providing Bug-type Pokemon with immediate battlefield control through speed manipulation.
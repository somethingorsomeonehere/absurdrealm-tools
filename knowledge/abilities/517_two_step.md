---
id: 517
name: Two Step
status: reviewed
character_count: 133
---

# Two Step - Ability ID 517

## In-Game Description
"After using a dance move, uses Revelation Dance at 50% power."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After using a dance move, automatically follows up with a 50 BP Revelation Dance. The follow-up move matches the user's primary type.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Two Step is an offensive ability that creates combo potential by automatically following up dance moves with a damaging attack. When the user successfully executes any dance move, the ability triggers a follow-up Revelation Dance at reduced power.

### Activation Conditions
- **Move requirement**: Must successfully use a dance move (moves with FLAG_DANCE or affected by Taekkyeon ability)
- **Target availability**: Valid target must exist for the follow-up attack
- **Power reduction**: Follow-up Revelation Dance deals 50% of its normal power (50 instead of 100)
- **Type matching**: Revelation Dance's type matches the user's primary type

### Technical Implementation
```c
constexpr Ability TwoStep = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(IsDance(battler, move))
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_ALLOW_SELF))
        
        return UseAttackerFollowUpMove(battler, target, ability, MOVE_REVELATION_DANCE, 50);
    },
};
```

### Dance Move Classification
The ability works with moves that have the `dance: true` flag or are affected by the Taekkyeon ability:
- **Status dance moves**: Swords Dance, Quiver Dance, Dragon Dance, etc.
- **Attacking dance moves**: Petal Dance, Fiery Dance, Revelation Dance, etc.
- **Custom dance moves**: Zap Jive, Hex Trot, Esper Waltz, etc.
- **Taekkyeon interaction**: Non-status moves become dance moves with Taekkyeon ability

### Follow-up Move Details
**Revelation Dance Properties:**
- Base power: 100 (50 with Two Step)
- Type: Matches user's primary type
- Category: Special
- Accuracy: 100%
- PP: Not consumed (ability-generated)
- Effects: Standard type effectiveness applies

### Important Interactions
- **Double dance combo**: Using Revelation Dance triggers another Revelation Dance at 25% power
- **Type advantage**: Follow-up can hit for super effective damage based on user's type
- **Multi-target**: Can target different opponent than original dance move
- **Self-targeting**: Some dance moves can redirect follow-up to self with FOLLOWUP_ALLOW_SELF
- **Ability suppression**: Doesn't work if ability is suppressed (Mold Breaker, etc.)

### Strategic Applications
- **Setup sweeping**: Use stat-boosting dances then immediately pressure with damage
- **Type coverage**: Provides additional type coverage based on user's primary type
- **Momentum building**: Combines setup and offense in a single turn
- **Surprise factor**: Unexpected damage from seemingly defensive moves
- **Action economy**: Effectively gets two moves per turn when using dance moves

### Optimal Users
- **Oricorio forms**: Natural dance move users with different primary types
- **Multi-type Pokemon**: Benefit from type-matching Revelation Dance
- **Setup sweepers**: Pokemon that use stat-boosting dance moves
- **Special attackers**: Revelation Dance is a special move
- **Speed control users**: Can use dance moves for speed control then attack

### Competitive Synergies
- **Quiver Dance**: Boosts Special Attack then immediately uses special move
- **Dragon Dance**: Physical setup with special follow-up creates mixed threat
- **Swords Dance**: Unexpected special damage from physical setup
- **Custom dances**: Elite Redux dance moves provide unique combo opportunities
- **Weather/terrain**: Can benefit from field effects on follow-up move

### Counters and Limitations
- **Power reduction**: Follow-up move is significantly weaker than full power
- **Prediction**: Opponents can predict follow-up and switch accordingly  
- **Type resistance**: Follow-up damage reduced by type matchups
- **Priority moves**: Can interrupt before follow-up triggers
- **Ability suppression**: Neutralizing Gas, Mold Breaker disable the effect
- **Taunt**: Prevents using many dance moves that trigger the ability

### Comparison to Similar Abilities
- **Dancer**: Copies dance moves used by others vs. following up own dances
- **Blade Dance**: Similar concept but uses Leaf Blade instead of Revelation Dance
- **Follow-up abilities**: Part of Elite Redux's expansion of combo-based abilities

### Team Building Considerations
- **Type synergy**: User's primary type determines follow-up move effectiveness
- **Coverage holes**: Can help cover weaknesses with surprise type matchups
- **Speed tiers**: Important for ensuring follow-up move connects
- **Item support**: Life Orb, type gems can boost follow-up damage
- **Move selection**: Balance between useful dance moves and overall coverage

### Version History
- New ability introduced in Elite Redux
- Part of the expanded ability system focusing on move combinations
- Unique to Elite Redux, not present in official Pokemon games
- Represents the "combo" archetype of abilities in the expanded roster
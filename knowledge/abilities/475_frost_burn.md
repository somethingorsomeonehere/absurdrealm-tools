---
id: 475
name: Frost Burn
status: reviewed
character_count: 69
---

# Frost Burn - Ability ID 475

## In-Game Description
"Triggers 40BP Ice Beam after using a Fire-type move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Triggers a 40 BP Ice Beam immediately after using any Fire-type move. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Frost Burn is an offensive ability that provides automatic followup attacks after using Fire-type moves. When the Pokemon uses any Fire-type move, it immediately follows up with a 40 BP Ice Beam against the same target.

### Activation Conditions
- **Move type requirement**: Must use a Fire-type move to trigger
- **Target adjustment**: Uses FOLLOWUP_STANDARD targeting rules
- **Success independence**: Triggers regardless of whether the Fire move hit or missed
- **Power independence**: Works with any Fire move regardless of its base power
- **Timing**: Activates immediately after the Fire move resolves

### Followup Attack Details
- **Move used**: Ice Beam (MOVE_ICE_BEAM)
- **Base power**: 40 BP (reduced from Ice Beam's normal 90 BP)
- **Type**: Ice-type
- **Accuracy**: 100% (followup moves typically have perfect accuracy)
- **Target**: Same target as the original Fire move
- **Additional effects**: 10% chance to cause frostbite (Ice Beam's natural effect)

### Technical Implementation
```c
constexpr Ability FrostBurn = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(moveType == TYPE_FIRE)  // Only triggers on Fire moves
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_STANDARD))
        
        return UseAttackerFollowUpMove(battler, target, ability, MOVE_ICE_BEAM, 40);
    },
};
```

### Important Interactions
- **Type effectiveness**: Ice Beam followup subject to normal type effectiveness
- **STAB bonus**: Ice Beam gets STAB if the Pokemon is Ice-type
- **Abilities interaction**: Ice Beam can trigger other abilities (Flash Fire immunity, etc.)
- **Status effects**: Can potentially inflict frostbite (10% chance)
- **Multi-hit moves**: Triggers only once per Fire move, not per hit
- **Failed moves**: Still triggers even if Fire move misses or fails

### Strategic Applications
- **Coverage enhancement**: Provides Ice coverage for Fire-type Pokemon
- **Damage amplification**: Effectively increases damage output after Fire moves
- **Type synergy**: Fire + Ice hits many types for neutral or super effective damage
- **Surprise factor**: Opponents may not expect Ice attacks from Fire-type Pokemon
- **Status utility**: Additional chance to inflict frostbite status

### Move Synergies
- **High-power Fire moves**: Flamethrower, Fire Blast, Overheat for maximum initial damage
- **Multi-target Fire moves**: Heat Wave hits multiple foes, followup hits one
- **Status Fire moves**: Will-O-Wisp, Flame Wheel still trigger the followup
- **Priority Fire moves**: Flame Charge allows priority + followup combo
- **Setup moves**: Works with Fire moves used after stat boosts

### Counters and Limitations
- **Ice immunity**: Steel, Fire, Ice, and Water types resist the followup
- **Ability suppression**: Mold Breaker family bypasses the ability
- **No Fire moves**: Useless if Pokemon lacks Fire-type moves
- **Predictability**: Opponents can predict Ice followup after Fire moves
- **PP consumption**: Only the Fire move consumes PP, not the followup

### Competitive Viability
- **Mixed attackers**: Great for Pokemon with both physical and special Fire moves
- **Fire/non-Ice types**: Provides unexpected Ice coverage
- **Wallbreaking**: Helps break through bulky Water, Ground, Dragon types
- **Speed control**: Can potentially slow opponents with frostbite
- **Team support**: Provides Ice coverage without dedicating a move slot

### Common Users
This ability would be excellent on:
- Fire-type Pokemon lacking Ice coverage
- Mixed attackers with Fire moves in their movepool
- Pokemon that want to surprise Water, Ground, Grass, Dragon types
- Fast Fire attackers that can leverage the surprise factor

### Optimal Movesets
- **Physical**: Fire Punch/Flame Wheel + other coverage moves
- **Special**: Flamethrower/Fire Blast + other special attacks
- **Mixed**: Both physical and special Fire moves for versatility
- **Status**: Will-O-Wisp for burn + guaranteed Ice Beam followup

### Version History
- Custom Elite Redux ability (ID 475)
- Part of the 500+ ability expansion project
- Designed to provide unique Fire-Ice type coverage synergy
- Balanced with reduced 40 BP instead of full Ice Beam power

### Comparison to Similar Abilities
- **More reliable than** abilities requiring specific conditions
- **More versatile than** single-type boosting abilities  
- **More surprising than** predictable type-boosting abilities
- **More consistent than** weather or terrain dependent abilities
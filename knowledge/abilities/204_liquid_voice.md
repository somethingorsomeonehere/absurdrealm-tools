---
id: 204
name: Liquid Voice
status: reviewed
character_count: 83
---

# Liquid Voice - Ability ID 204

## In-Game Description
"Sound moves get a 1.2x boost and become Water if Normal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Liquid Voice converts Normal-type sound moves to Water-type and boosts them by 20%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Liquid Voice is a unique ability that combines type conversion with power boosting for sound-based moves. It specifically targets Normal-type sound moves, converting them to Water-type while providing a 1.2x damage multiplier to all sound moves regardless of their original type.

### Activation Conditions
- **Sound move requirement**: Move must have the FLAG_SOUND property
- **Type conversion**: Only Normal-type sound moves become Water-type
- **Power boost**: All sound moves get 1.2x damage multiplier
- **Timing**: Type change occurs before damage calculation, power boost applies during damage calculation

### Technical Implementation
```c
// Type conversion component
.onMoveType = +[](ON_MOVE_TYPE) -> int {
    CHECK(moveType == TYPE_NORMAL)
    CHECK(gBattleMoves[move].flags & FLAG_SOUND)
    return TYPE_WATER + 1;
},

// Power boost component  
.onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
    if (IsSoundMove(battler, move)) MUL(1.2);
},
```

### Affected Moves
**Offensive Sound Moves** (Normal to Water + 1.2x boost):
- Hyper Voice (95 to 114 BP)
- Boomburst (140 to 168 BP) 
- Round (60 to 72 BP)
- Uproar (90 to 108 BP)
- Echoed Voice (40 to 48 BP base)

**Status Sound Moves** (Normal to Water, no damage boost):
- Growl (becomes Water-type)
- Roar (becomes Water-type)
- Sing (becomes Water-type)
- Supersonic (becomes Water-type)

**Non-Normal Sound Moves** (power boost only):
- Bug Buzz (remains Bug-type, gets 1.2x boost)
- Disarming Voice (remains Fairy-type, gets 1.2x boost)
- Chatter (remains Flying-type, gets 1.2x boost)

### Important Interactions
- **STAB calculation**: Water-type converted moves can receive STAB from Water-type users
- **Type effectiveness**: Converted moves use Water-type effectiveness chart
- **Ability precedence**: Type conversion happens before other type-changing effects
- **Sound immunity**: Soundproof still blocks all sound moves regardless of type change
- **Throat Spray**: Still activates on sound moves despite type change
- **Pixilate interactions**: Cannot stack with other -ate abilities

### Strategic Implications
- **Coverage expansion**: Provides Water-type attacks to non-Water Pokemon
- **STAB synergy**: Excellent on Water-types for boosted STAB sound moves
- **Utility retention**: Status sound moves maintain utility while gaining Water typing
- **Sound immunity**: Vulnerable to Soundproof ability
- **Type prediction**: Opponents may not expect Water-type moves from non-Water Pokemon

### Common Users
Based on codebase analysis, Liquid Voice appears on:
- Pokemon with natural sound-based movesets
- Water-type Pokemon seeking sound move utility
- Pokemon requiring additional Water-type coverage
- Mixed attackers using both offensive and utility sound moves

### Competitive Usage Notes
- **Priority targeting**: Hyper Voice becomes powerful spread Water move
- **Sound spam**: Boomburst becomes extremely powerful Water nuke
- **Utility coverage**: Sing becomes Water-type sleep move
- **Team support**: Can use sound moves for team utility while dealing Water damage
- **AI rating**: Rated 5/10 by battle AI (moderate utility)

### Counters
- **Soundproof**: Complete immunity to all sound moves
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Water resistance**: Steel, Water, Dragon, and Grass types resist converted moves
- **Substitute**: Blocks most sound moves despite type change
- **Wide Guard**: Protects teammates from spread sound moves

### Synergies
- **Water-type STAB**: Maximizes damage on Water-type users
- **Sound move coverage**: Access to varied sound utility moves
- **Rain teams**: Boosted Water-type damage in rain
- **Throat Spray**: Item activation for Special Attack boost
- **Specs/Band**: Choice items boost converted sound moves
- **Life Orb**: Recoil damage for significant power increase

### Similar Abilities
Liquid Voice is part of the "-ate" ability family that includes:
- **Sand Song**: Normal sound to Ground + 1.2x boost
- **Banshee**: Normal sound to Ghost + 1.2x boost  
- **Snow Song**: Normal sound to Ice + 1.2x boost
- **Power Metal**: Normal sound to Steel + 1.2x boost

These abilities share identical code structure with only type conversion differences.

### Version History
- Introduced in Generation VII (Sun/Moon)
- In Elite Redux, maintains standard mechanics with 1.2x multiplier
- Classified as an "ATE_ABILITY" variant in codebase
- Enhanced by Elite Redux's expanded sound move roster

### Advanced Mechanics
- **Multi-hit interactions**: Each hit of multi-hit sound moves gets full conversion and boost
- **Z-move compatibility**: Z-moves retain type conversion properties
- **Priority interactions**: Quick Claw and other priority don't affect type conversion
- **Weather independence**: Unlike some abilities, not affected by weather conditions
- **Substitute piercing**: Most sound moves bypass Substitute regardless of type
---
id: 523
name: Grappler
status: reviewed
character_count: 122
---

# Grappler - Ability ID 523

## In-Game Description
"Trapping moves last 6 turns. Trapping deals 1/6 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Trapping moves last 6 turns instead of 4-5 turns and increases their damage at the end of the turn to 1/6 max HP per turn. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Grappler is an offensive ability that enhances trapping move effectiveness by extending their duration and increasing their damage output. This ability transforms traditionally weak binding moves into serious threats.

### Activation Conditions  
- **Move requirement**: Must use a trapping/binding move
- **Affected moves**: 
  - Bind
  - Wrap
  - Fire Spin
  - Whirlpool
  - Sand Tomb
  - Clamp
  - Infestation
  - Magma Storm
  - Thunder Cage (if implemented)
- **Duration extension**: Trapping lasts exactly 6 turns (increased from normal 4-5 turns)
- **Damage boost**: Trapping damage increased to 1/6 max HP per turn (from normal 1/8)

### Technical Implementation
```c
// Grappler extends trapping duration and damage
if (ability == ABILITY_GRAPPLER && IsMoveTrapping(move)) {
    // Set trapping turns to 6
    gBattleMons[target].status2 |= STATUS2_WRAPPED;
    gBattleStruct->wrappedTurns[target] = 6;
    
    // Increase damage to 1/6 max HP
    damage = GetBattlerMaxHP(target) / 6;
}
```

### Important Interactions
- **Turn counting**: Trapping duration is fixed at 6 turns, not random
- **Damage timing**: Trapping damage occurs at the end of each turn
- **Stacking**: Cannot stack multiple trapping effects
- **Switching**: Trapped Pokemon cannot switch out
- **Ghost types**: Still affected by trapping moves (unlike traditional mechanics)
- **Partial trapping immunity**: Flying types and Levitate still affected by most moves

### Damage Calculation
- **Base damage**: 1/6 of target's maximum HP per turn
- **Minimum damage**: At least 1 HP per turn
- **Not affected by**: Type effectiveness, stats, or other damage modifiers
- **Cumulative effect**: Can deal significant damage over 6 turns (total of 100% max HP if uninterrupted)

### Strategic Implications
- **Pressure tool**: Forces switches or significant damage accumulation
- **Stall breaker**: Excellent against defensive strategies
- **Setup time**: 6-turn duration provides ample setup opportunities
- **Revenge killer**: Can finish off weakened opponents over time
- **Entry hazard synergy**: Works well with Stealth Rock and Spikes

### Enhanced Trapping Moves
When used with Grappler:
- **Fire Spin**: 6 turns of 1/6 HP fire damage
- **Bind**: 6 turns of 1/6 HP normal damage  
- **Sand Tomb**: 6 turns of 1/6 HP ground damage + accuracy reduction
- **Whirlpool**: 6 turns of 1/6 HP water damage
- **Infestation**: 6 turns of 1/6 HP bug damage
- **Magma Storm**: 6 turns of 1/6 HP fire damage (if already high damage, enhanced further)

### Common Users
- **Dugtrio**: Arena Trap + Grappler combination
- **Cradily**: Bulky trapper with Storm Drain synergy
- **Tentacruel**: Fast trapper with wide movepool
- **Octillery**: Diverse trapping move access
- **Diglett**: Early game trapping specialist

### Competitive Usage Notes
- **Guaranteed duration**: 6-turn fixed duration removes RNG from trapping
- **Significant chip damage**: 100% max HP over full duration
- **Forces responses**: Opponents must act quickly or lose Pokemon
- **Entry hazard combos**: Pairs excellently with hazard setters
- **Late game closer**: Can secure KOs on weakened teams

### Counters
- **Magic Guard**: Negates trapping damage entirely
- **Shed Shell**: Allows switching out of trapping moves
- **Rapid Spin**: Removes trapping effects (if the user can act)
- **U-turn/Volt Switch**: Pivot moves before getting trapped (timing dependent)
- **Ghost types**: Immunity to some trapping moves like Bind and Wrap
- **Substitute**: Can block initial trapping move

### Synergies
- **Arena Trap**: Prevents escape, guaranteeing full trapping duration
- **Shadow Tag**: Similar escape prevention synergy
- **Entry hazards**: Maximize damage while opponent is trapped
- **Speed control**: Trick Room or Thunder Wave to ensure trapping move hits
- **Recovery moves**: Heal while opponent takes trapping damage
- **Setup moves**: Use trapping turns for stat boosts

### Move Compatibility
**Excellent trapping moves for Grappler users:**
- **Fire Spin**: Widely distributed, decent power
- **Infestation**: Bug typing, good distribution
- **Sand Tomb**: Ground typing, accuracy reduction bonus
- **Whirlpool**: Water typing, decent availability
- **Bind**: Normal typing, neutral effectiveness

### Version History
- **Elite Redux original**: New ability created for Elite Redux
- **Implementation status**: Defined in protobuf, implementation may be pending
- **Design intent**: Enhance viability of traditionally weak trapping strategies
- **Balancing considerations**: High damage output balanced by move accuracy and setup requirements
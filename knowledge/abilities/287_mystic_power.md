---
id: 287
name: Mystic Power
status: reviewed
character_count: 144
---

# Mystic Power - Ability ID 287

## In-Game Description
"All moves gain the 1.5x power boost from STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mystic Power grants the 1.5x STAB damage bonus to all moves regardless of type matching. Does not boost moves that already receive a STAB bonus.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Universal STAB**: All moves receive the 1.5x Same Type Attack Bonus, regardless of type matching
- **No Type Requirement**: Moves don't need to match the Pokemon's type(s) to gain STAB
- **Damage Multiplier**: Every damaging move gains a flat 1.5x power multiplier
- **Stacks with Other Bonuses**: Combines multiplicatively with other damage modifiers

### Activation Conditions
- Applies to all damaging moves used by the Pokemon with this ability
- Works on both physical and special moves
- Functions on multi-hit moves (each hit gets the bonus)
- Affects variable power moves and status moves that deal damage

### Technical Implementation
```cpp
constexpr Ability MysticPower = {
    .onStab = +[](ON_STAB) -> int { return TRUE; },
};
```

The ability simply returns `TRUE` for all STAB checks, making the battle engine treat every move as if it has STAB regardless of type matching.

### Complete Move Coverage
**All moves are affected**, including but not limited to:
- **Physical Moves**: Earthquake, Close Combat, Stone Edge, U-turn, etc.
- **Special Moves**: Thunderbolt, Ice Beam, Flamethrower, Shadow Ball, etc.
- **Status Moves with Damage**: Seismic Toss, Night Shade, Dragon Rage, etc.
- **Multi-Hit Moves**: Bullet Seed, Rock Blast, Bone Rush (each hit boosted)
- **Priority Moves**: Quick Attack, Extreme Speed, Sucker Punch, etc.
- **Recoil Moves**: Double-Edge, Flare Blitz, Head Smash, etc.

### Interactions with Other Abilities/Mechanics

#### Positive Synergies
- **Life Orb**: 1.5x (Mystic Power) x 1.3x (Life Orb) = 1.95x total multiplier
- **Choice Items**: Enhanced damage on locked moves
- **Weather Abilities**: Rain/Sun boosted moves get both weather and Mystic Power bonuses
- **Type-boosting Items**: Expert Belt, type gems, etc. stack multiplicatively
- **Adaptability**: If a Pokemon somehow had both, normal STAB moves would get 2x x 1.5x = 3x total

#### Neutral Interactions
- **Protean/Libero**: User changes type but all moves still get STAB from Mystic Power
- **Normalize**: Normal-type moves still get the Mystic Power bonus
- **Type-changing moves**: Moves like Hidden Power get the bonus regardless of their type

#### No Negative Interactions
- Unlike other abilities, Mystic Power has no drawbacks or situational limitations
- Cannot be negated by abilities like Mold Breaker (it's not an immunity)
- Weather and terrain don't affect its functionality

### Strategic Implications

#### Offensive Applications
- **Perfect Coverage**: No need to worry about type matchups for raw damage
- **Move Flexibility**: Can use any move for respectable damage output
- **Mixed Attackers**: Both physical and special moves become viable damage options
- **Utility Moves**: Even utility moves with damage components hit harder

#### Team Building Considerations
- **Move Selection**: Priority shifts from type coverage to other factors (accuracy, effects, PP)
- **Item Choice**: Damage-boosting items become more valuable
- **Stat Distribution**: Both Attack and Special Attack become more valuable
- **Coverage Strategy**: Can focus on secondary effects rather than type coverage

### Example Damage Calculations

**Base 80 Power Move** (e.g., Thunderbolt without type matching):
- Without Mystic Power: 80 BP
- With Mystic Power: 80 x 1.5 = 120 effective BP

**Base 100 Power Move** (e.g., Earthquake):
- Without Mystic Power: 100 BP  
- With Mystic Power: 100 x 1.5 = 150 effective BP

**Comparison to Normal STAB**:
- Normal STAB move: 80 BP x 1.5 = 120 BP
- Mystic Power non-STAB: 80 BP x 1.5 = 120 BP
- **Result**: Every move hits as hard as a STAB move would normally

### Common Users in Elite Redux
Based on the species data, Mystic Power appears on:
- **Psychic-types**: Abra line, Ralts line, and other psychic Pokemon
- **Legendary/Mythical Pokemon**: Various legendary species as regular or innate ability
- **Mixed Attackers**: Pokemon with balanced offensive stats
- **Utility Pokemon**: Species that benefit from universal damage enhancement
- **Unown variants**: All 28 forms have access to this ability

### Competitive Usage Notes

#### Strengths
- **Consistent Damage**: All moves deal respectable damage regardless of type
- **Simplified Move Selection**: Don't need to worry about STAB when choosing moves
- **Enhanced Coverage**: Off-type moves become genuinely threatening
- **No Downsides**: Pure benefit with no negative effects or conditions

#### Optimal Strategies
- **Mixed Attacker Sets**: Use both physical and special moves effectively
- **Coverage Priority**: Focus on moves with useful secondary effects
- **Item Synergy**: Life Orb, Choice items, and type-boosting items all work well
- **Movepool Exploitation**: Makes use of the entire available movepool

#### Potential Weaknesses
- **No Additional Effects**: Only provides damage boost, no utility
- **Predictable**: Opponents know all moves will hit hard
- **Stat Requirements**: Still need good offensive stats to maximize effectiveness
- **Move Selection**: May struggle to choose optimal moves when all are viable

### Counters and Responses

#### Direct Counters
- **High Defensive Stats**: Pokemon with excellent bulk can still tank enhanced moves
- **Type Resistances**: Still take reduced damage from resisted moves
- **Defensive Abilities**: Abilities like Multiscale, Solid Rock still reduce damage

#### Indirect Responses
- **Status Moves**: Sleep, paralysis still shut down the offensive threat
- **Priority Moves**: Fast offensive pressure before they can attack
- **Defensive Positioning**: Switching to appropriate resistances still works

### Version History and Design Intent
- **Elite Redux Original**: Created as a pure offensive ability for mixed attackers
- **Design Philosophy**: Removes the type-matching requirement from STAB
- **Balance Consideration**: 1.5x multiplier matches normal STAB rather than creating overpowered scaling
- **Niche**: Allows Pokemon to use their entire movepool effectively

### Related Abilities
- **Adaptability**: Enhances STAB from 1.5x to 2x (but only for matching types)
- **Libero/Protean**: Changes type to match moves (gives STAB + type advantages)
- **Normalize**: Makes all moves Normal-type (can synergize with Mystic Power)
- **Type-boosting abilities**: Iron Fist, Strong Jaw, etc. (stack with Mystic Power)

### Technical Notes
- **Implementation**: Simple boolean return in STAB calculation
- **Performance**: No computational overhead beyond normal STAB checking
- **Compatibility**: Works with all existing move mechanics and calculations
- **Future-Proof**: Will automatically work with any new moves added to the game
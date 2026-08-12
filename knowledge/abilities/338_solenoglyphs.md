---
id: 338
name: Solenoglyphs
status: reviewed
character_count: 89
---

# Solenoglyphs - Ability ID 338

## In-Game Description
"Biting moves have 50% chance to badly poison the target."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Solenoglyphs gives all biting moves a 50% chance to badly poison the target when landing. 

## Detailed Mechanical Explanation

### Overview

Solenoglyphs is an offensive ability that adds a powerful status effect to biting moves. When a Pokemon with this ability uses any move flagged as a biting move, there's a 50% chance to inflict the badly poisoned status condition on the target, making it an excellent ability for both offensive pressure and long-term damage accumulation.

### Mechanics

### Core Implementation
- **Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc:3575-3584`
- **Trigger**: On successful hit with biting moves
- **Effect**: 50% chance to badly poison the target
- **Status Applied**: Toxic (badly poisoned)

### Code Analysis
```cpp
constexpr Ability Solenoglyphs = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBePoisoned(battler, target, MOVE_NONE))
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        CHECK(Random() % 2)

        return AbilityStatusEffect(MOVE_EFFECT_TOXIC);
    },
};
```

### Trigger Conditions
1. **Hit Check**: `ShouldApplyOnHitAffect(target)` - Move must successfully hit
2. **Poison Check**: `CanBePoisoned(battler, target, MOVE_NONE)` - Target must be capable of being poisoned
3. **Biting Move Check**: `gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST` - Move must have the Strong Jaw flag
4. **Random Check**: `Random() % 2` - 50% chance activation

## Affected Moves

Solenoglyphs affects all moves with the `FLAG_STRONG_JAW_BOOST` flag. These include:

### Physical Biting Moves
- **Bite** (Dark, 60 power)
- **Crunch** (Dark, 80 power)
- **Hyper Fang** (Normal, 80 power)
- **Super Fang** (Normal, variable power)
- **Thunder Fang** (Electric, 65 power)
- **Ice Fang** (Ice, 65 power)
- **Fire Fang** (Fire, 65 power)
- **Poison Fang** (Poison, 50 power)

### Special Biting Moves
- **Leech Life** (Bug, 80 power)
- **Pluck** (Flying, 60 power)

## Pokemon with Solenoglyphs

Based on the codebase analysis, Solenoglyphs appears as an innate ability on 6 different Pokemon:

### Confirmed Pokemon
1. **Ekans** (Lines 4153 in SpeciesList.textproto)
   - Innate ability alongside Shed Skin and Coil Up
   - Fits thematically as a venomous snake Pokemon

*Note: Additional Pokemon with this ability can be found at lines 4308, 18320, 18426, 45076, and 108063 in the species data.*

## Strategic Applications

### Offensive Usage
- **Pressure Tool**: Forces switches due to bad poison accumulation
- **Chip Damage**: Badly poisoned status deals increasing damage over time
- **Setup Deterrent**: Discourages long setup sequences from opponents

### Defensive Considerations
- **Type Coverage**: Works well on Pokemon that can learn diverse biting moves
- **Synergy**: Excellent with Merciless ability users on the same team
- **Stall Breaking**: Helps break through defensive cores

## Competitive Analysis

### Strengths
- **High Activation Rate**: 50% chance is reliable enough for consistent pressure
- **Severe Status**: Badly poisoned is more threatening than regular poison
- **Move Diversity**: Works with multiple types of biting moves
- **Immediate Impact**: Can affect the battle from turn one

### Weaknesses
- **Type Restrictions**: Limited to Pokemon that learn biting moves
- **Poison Immunity**: Completely blocked by Poison-types and Steel-types
- **Ability Counters**: Poison Heal and Guts can turn the effect beneficial
- **Random Factor**: 50% chance means inconsistent activation

### Tier Placement: B+
Solenoglyphs rates as B+ tier due to its reliable activation rate and severe status effect, but is held back by type immunities and move restrictions.

## Synergies and Counters

### Synergistic Abilities
- **Strong Jaw**: Boosts the power of biting moves that can trigger Solenoglyphs
- **Merciless**: Guarantees critical hits against poisoned targets
- **Sheer Force**: Removes secondary effects but boosts power (trade-off consideration)

### Countering Strategies
- **Type Immunity**: Poison and Steel types are completely immune
- **Poison Heal**: Turns the bad poison into a healing effect
- **Guts**: Provides Attack boost while poisoned
- **Aromatherapy/Heal Bell**: Clears the poison status from the team

## Interactions and Edge Cases

### Status Interactions
- Cannot poison Poison-type or Steel-type Pokemon
- Blocked by Poison immunity abilities (Immunity, Poison Heal)
- Overrides existing poison with badly poisoned status
- Affects through Substitute (unlike some other abilities)

### Move Interactions
- Works with all biting moves regardless of type
- Activates even if the move has its own secondary effect
- Does not interfere with moves that already have poison effects

## Conclusion

Solenoglyphs is a powerful offensive ability that transforms any biting move user into a potent status spreader. Its 50% activation rate provides consistent pressure, and the badly poisoned status can quickly accumulate significant damage. While limited by type immunities and move restrictions, it remains a valuable ability for Pokemon that can effectively utilize biting moves in their movesets.

The ability's design encourages aggressive play while providing long-term damage accumulation, making it particularly effective against bulky defensive Pokemon that would otherwise wall physical attackers. Its presence in the Elite Redux roster adds another layer of strategic depth to team building and battle dynamics.


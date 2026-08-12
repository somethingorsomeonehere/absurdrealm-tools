---
id: 359
name: Flock
status: reviewed
character_count: 75
---

# Flock - Ability ID 359

## In-Game Description
"Boosts Flying-type moves when HP is low."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Flying-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation

### Overview

**Flock** is a swarm-style ability introduced in Elite Redux that provides conditional power boosts to Flying-type moves. This ability follows the same mechanical framework as classic abilities like Overgrow, Blaze, Torrent, and Swarm, but applies specifically to Flying-type attacks.

## Mechanics

### Core Implementation
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Line 3778-3780)
- **Macro**: Uses `SWARM_MULTIPLIER(TYPE_FLYING)` (Lines 293-301)

```cpp
constexpr Ability Flock = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_FLYING),
};
```

### Damage Calculation
The ability applies multiplicative damage boosts based on HP percentage:

1. **Above 1/3 HP**: 1.2x boost to Flying-type moves
2. **At or below 1/3 HP**: 1.5x boost to Flying-type moves

The HP threshold is calculated as: `gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)`

### STAB Interaction
Flock stacks multiplicatively with STAB (Same Type Attack Bonus):
- **Non-Flying Pokemon** with Flock: Flying moves deal 1.2x/1.5x damage
- **Flying-type Pokemon** with Flock: Flying moves deal 1.8x/2.25x damage (1.5 x 1.2/1.5)

## Strategic Applications

### Early Game Power
- Provides consistent 1.2x boost to Flying-type moves throughout most battles
- Particularly valuable for non-Flying types that learn Flying moves
- Makes typically weaker Flying moves more viable options

### Pinch Activation
- The 1.5x boost at low HP can turn the tide in desperate situations
- Creates risk/reward scenarios where staying at low HP provides maximum power
- Synergizes well with Focus Sash, Sturdy, or other survival strategies

### Move Compatibility
Works with all Flying-type attacks, including:
- **Physical**: Wing Attack, Aerial Ace, Brave Bird, Fly
- **Special**: Air Slash, Hurricane, Air Cutter
- **Status**: Moves like Roost (though boost only applies to damaging moves)

## Competitive Analysis

### Strengths
- **Consistent Power**: Unlike many conditional abilities, provides boost throughout most of the battle
- **Type Coverage**: Flying is an excellent offensive type with few resistances
- **Pinch Power**: Low HP boost can secure crucial KOs
- **Versatility**: Useful on both Flying and non-Flying type Pokemon

### Weaknesses
- **Type Limitation**: Only boosts one move type
- **HP Dependency**: Maximum power requires being at low HP
- **Weather Independence**: Unlike some abilities, provides no additional utility

### Tier Ranking
- **Competitive Viability**: B+ tier offensive ability
- **Niche Usage**: Excellent for Flying-type specialists or mixed attackers
- **Synergy Rating**: High with offensive Flying-type movesets

## Pokemon Distribution

### Primary Users
Based on proto analysis, Flock appears on numerous Flying-type Pokemon, including:
- **Pidgey line** (Pidgey confirmed as innate ability holder)
- **Various bird Pokemon** throughout the Elite Redux roster
- **Mixed with other abilities**: Often appears as an innate ability alongside other traits

### Notable Combinations
- **With Aerilate**: Converts Normal moves to Flying, then boosts them
- **With Aerialist**: Combined ability that includes both Levitate and Flock effects
- **With STAB**: Flying-types get maximum benefit from the combination

## Related Abilities

### Swarm Family
Flock is part of the swarm-style ability family:
- **Overgrow** (#65): Grass-type version (1.2x/1.5x)
- **Blaze** (#66): Fire-type version (1.2x/1.5x)  
- **Torrent** (#67): Water-type version (1.2x/1.5x)
- **Swarm** (#68): Bug-type version (1.2x/1.5x)

### Enhanced Variants
Elite Redux includes boosted versions with higher multipliers:
- **Hellblaze**: Enhanced Fire version (1.3x/1.8x)
- **Riptide**: Enhanced Water version (1.3x/1.8x)
- **Forest Rage**: Enhanced Grass version (1.3x/1.8x)

### Combination Abilities
- **Aerialist**: Combines Levitate + Flock for comprehensive Flying-type support

## Code Implementation Details

### Macro Definition
```cpp
#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
            else                                                             \
                MUL(1.2);                                                    \
        }                                                                    \
    }
```

### Integration Points
- **Line 6389**: Called in offensive multiplier chain
- **Line 9204**: Registered in ability lookup table as `{ABILITY_FLOCK, Flock}`

## Battle Interactions

### Weather Effects
- **Tailwind**: Stacks with Flock for enhanced Flying-type offense
- **Strong Winds**: Delta Stream weather removes Flying weaknesses while maintaining Flock boosts
- **Rain/Sun**: No direct interaction, but affects accuracy of moves like Hurricane

### Item Synergy
- **Life Orb**: Stacks multiplicatively for 1.44x/1.8x total boost (before recoil)
- **Choice Items**: Excellent synergy for specialized Flying attackers
- **Focus Sash**: Enables safe activation of the 1.5x boost threshold

### Terrain Effects
- **Electric Terrain**: No direct effect on Flock
- **Other Terrains**: Generally neutral interaction

## Version History

- **Elite Redux**: Introduced as part of expanded ability roster
- **Current Version**: Stable implementation using established swarm mechanics
- **Future Considerations**: May receive enhanced variants in later updates

## Trivia

- Flock represents the first Flying-type entry in the classic starter ability family
- The name references the collective behavior of birds, fitting the conditional nature
- Uses the same exact multipliers as the original Generation 3 starter abilities
- Part of Elite Redux's philosophy of extending classic mechanics to new types

## Summary

Flock is a well-designed offensive ability that brings Flying-type attacks into the established swarm ability framework. Its consistent 1.2x boost makes it valuable throughout battles, while the 1.5x pinch activation provides clutch potential. The ability particularly shines on Pokemon with strong Flying-type movepools and works excellently in both casual and competitive contexts.

For trainers seeking reliable Flying-type offense with built-in comeback potential, Flock offers exactly what's needed--consistent power with the possibility of explosive damage when it matters most.


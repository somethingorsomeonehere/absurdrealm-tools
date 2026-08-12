---
id: 203
name: Long Reach
status: reviewed
character_count: 235
---

# Long Reach - Ability ID 203

## In-Game Description
"Doesn't make contact. Boosts Phys. non-contact moves by 1.2x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Long Reach prevents the user from making contact with targets when using contact moves. Additionally, physical non-contact moves receive a 1.2x damage boost. Only applies damage boost to physical moves that were originally non-contact.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Long Reach is a dual-purpose ability that both prevents contact and boosts specific moves. It fundamentally changes how the Pokemon interacts with opponents by eliminating direct contact while enhancing ranged physical attacks.

### Primary Effects
1. **Contact Prevention**: All moves used by the Pokemon are treated as non-contact moves
2. **Damage Boost**: Physical non-contact moves receive a 1.2x damage multiplier

### Activation Conditions
- **Contact prevention**: Always active for all moves
- **Damage boost**: Only applies to moves that are:
  - Physical split (not special or status)
  - Naturally non-contact moves

### Technical Implementation
```c
constexpr Ability LongReach = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_MOVE_PHYSICAL(move) && !gBattleMoves[move].contact) MUL(1.2);
        },
};

// Contact prevention in battle_util.c
bool32 IsMoveMakingContact(MoveEnum move, u8 battlerAtk) {
    if (!gBattleMoves[move].contact) {
        return FALSE;
    } else if (BattlerHasAbility(battlerAtk, ABILITY_LONG_REACH, TRUE)) {
        return FALSE;  // Long Reach prevents contact
    }
    // ... other contact checks
}
```

### Contact-Based Abilities Avoided
Long Reach prevents triggering of contact-based abilities:
- **Static**: No paralysis on contact
- **Flame Body**: No burn on contact
- **Poison Point**: No poison on contact
- **Rough Skin**: No damage on contact
- **Iron Barbs**: No damage on contact
- **Cute Charm**: No infatuation on contact
- **Effect Spore**: No status on contact

### Boosted Move Categories
Physical non-contact moves that receive the 1.2x boost include:
- **Earthquake**: Ground-type spread move
- **Rock Slide**: Rock-type spread move with flinch chance
- **Magnitude**: Variable power Ground-type move
- **Bulldoze**: Ground-type speed-lowering move
- **Razor Leaf**: Grass-type high-crit move
- **Rock Throw**: Basic Rock-type throwing move
- **Bone Club/Bonemerang**: Ground-type bone-based moves
- **Pin Missile**: Multi-hit Bug-type move

### Moves NOT Boosted
- **Contact moves**: Even with Long Reach, these don't get the boost (e.g., Punch moves)
- **Special moves**: Only physical moves qualify for the boost
- **Status moves**: No damage to boost

### Strategic Implications

#### Offensive Benefits
- **Safe attacking**: Can use moves without fear of contact abilities
- **Damage boost**: Enhanced physical ranged attacks
- **Multi-hit safety**: Multi-hit moves won't trigger contact abilities repeatedly
- **Hazard immunity**: Avoids Rocky Helmet and similar items

#### Defensive Considerations
- **No contact abilities**: Can't trigger own contact-based abilities
- **Item interactions**: Doesn't trigger items that require contact
- **Ability synergy**: Pairs well with abilities that enhance physical attacks

### Common Users
Based on the SpeciesList analysis, Long Reach appears on:
- **Fighting-types**: Timburr line (Timburr, Gurdurr, Conkeldurr)
- **Grass-types**: Various Grass starters and their evolutions
- **Water-types**: Greninja line and other Water starters
- **Steel-types**: Tinkaton line
- **Poison-types**: Various Poison specialists
- **Mixed typings**: Many Pokemon as innate ability

### Competitive Usage Notes
- **Wall-breaking**: Enhanced physical non-contact moves help break through defensive Pokemon
- **Safety**: Allows aggressive play without contact punishment
- **Team support**: Can safely use Earthquake in doubles without contact issues
- **Item synergy**: Works well with Choice Band for massive damage boosts
- **Speed control**: Bulldoze becomes a safer speed control option

### Synergistic Abilities
When used as innate alongside other abilities:
- **Iron Fist**: For contact punching moves (though Long Reach prevents contact)
- **Technician**: Boosts weaker moves that Long Reach also enhances
- **Sheer Force**: Additional damage boost for moves with secondary effects
- **Skill Link**: Ensures multi-hit moves hit maximum times safely

### Counters and Limitations
- **Special attackers**: Long Reach provides no benefit against special moves
- **Status moves**: No protection against non-contact status moves
- **Terrain effects**: Doesn't prevent terrain-based effects
- **Weather damage**: No protection from weather damage
- **Entry hazards**: Doesn't prevent hazard damage

### Item Interactions
- **Choice Band**: Stacks with Long Reach's boost for massive damage
- **Life Orb**: Additional damage boost at HP cost
- **Rocky Helmet**: Long Reach prevents triggering opponent's Rocky Helmet
- **Protective Pads**: Redundant with Long Reach's contact prevention

### Notable Interactions
- **Shell Side Arm**: Special case that can still make contact under certain conditions
- **Demolitionist**: Other abilities can also prevent contact
- **Protective Pads**: Item effect is redundant with Long Reach

### Version History
- Introduced in Generation VII as Decidueye's signature ability
- In Elite Redux, enhanced with damage boost component
- Available as both regular and innate ability on many Pokemon
- Integrated into the 4-ability system as a versatile combat ability

### Comparison to Similar Abilities
- **Protective Pads (item)**: Similar contact prevention but no damage boost
- **Magic Guard**: Broader protection but no offensive benefit
- **Iron Fist**: Boosts contact moves, opposite of Long Reach's focus
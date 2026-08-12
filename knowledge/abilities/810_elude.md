---
id: 810
name: Elude
status: reviewed
character_count: 168
---

# Elude - Ability ID 810

## In-Game Description
"Uses Speed as defense stat when hit by non-contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by non-contact moves, the Pokemon uses its Speed stat instead of Defense or Special Defense for damage calculations. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Defensive Stat Substitution**: When the Pokemon with Elude is hit by a non-contact move, the game uses its Speed stat instead of Defense or Special Defense for damage calculation
- **Non-Contact Move Detection**: Uses the `IsMoveMakingContact()` function with `CHECK_NOT()` logic - only activates when `gBattleMoves[move].contact = FALSE`
- **Stat Application**: Returns `STAT_SPEED` from the `onChooseDefensiveStat` callback when conditions are met

### Activation Conditions
- Must be hit by a move that does NOT make contact
- Applies to both physical and special non-contact moves
- Works regardless of move type or damage category

### Implementation Details
```cpp
constexpr Ability Elude = {
    .onChooseDefensiveStat = +[](ON_CHOOSE_DEFENSIVE_STAT) -> int {
        CHECK_NOT(IsMoveMakingContact(move, gBattlerAttacker))
        return STAT_SPEED;
    },
    .onChooseDefensiveStatFor = APPLY_ON_TARGET,
};
```

### Non-Contact Moves (Examples)
**Special Attacks:**
- Water Gun, Hydro Pump
- Psychic, Psybeam
- Thunderbolt, Thunder
- Flamethrower, Fire Blast
- Ice Beam, Blizzard

**Physical Projectiles:**
- Rock Slide, Stone Edge
- Pin Missile, Spike Cannon
- Bullet Seed, Seed Bomb

**Status/Other:**
- Toxic Spikes (when set)
- Stealth Rock damage
- Weather damage (if applicable)

### Moves That DON'T Trigger Elude
- All contact moves (Tackle, Punch moves, Bite, etc.)
- Moves affected by Long Reach ability
- Moves used by Pokemon with Protective Pads item
- Punching moves used by Pokemon with Punching Glove item

### Interactions with Other Abilities/Mechanics
- **Blur Ability (ID 809)**: Perfect complement - Blur uses Speed for contact moves, Elude for non-contact
- **Long Reach**: Prevents contact moves from making contact, potentially allowing both abilities to work together
- **Protective Pads**: Converts contact moves to non-contact for the attacker, making them trigger Elude instead of Blur
- **Shell Side Arm**: Special case - treated as contact when swapped to physical category
- **Stat Modifications**: Uses current Speed stat including all modifications (boosts, items, etc.)

### Strategic Implications
- **Defensive Versatility**: Allows fast Pokemon to tank both contact and non-contact moves effectively
- **Speed Investment**: Makes Speed EV investment serve dual purpose (offense and defense)
- **Synergy Potential**: Can be paired with Blur for complete defensive coverage
- **Setup Sweeper Support**: Protects fragile but fast setup sweepers from special attacks

### Damage Calculation Examples
**Example Pokemon with Elude:**
- Speed: 120
- Defense: 70  
- Special Defense: 80

**Against Psychic (Special, non-contact):**
- Normal calculation: Uses Special Defense (80)
- With Elude: Uses Speed (120) - 50% more bulk

**Against Tackle (Physical, contact):**
- Uses normal Defense (70) - Elude doesn't activate

### Common Users
Based on the codebase, Elude appears on several Pokemon as both regular and innate abilities, typically on fast but fragile Pokemon that benefit from using their high Speed for defense.

### Competitive Usage Notes
- **Role Compression**: Allows offensive Pokemon to be surprisingly bulky
- **Prediction Dependent**: Opponent must choose between contact and non-contact moves carefully
- **Item Synergy**: Works well with Choice items, Focus Sash, or Life Orb on fast attackers
- **Team Building**: Pairs excellently with Pokemon that have complementary defensive abilities

### Counters
- **Mixed Attackers**: Use both contact and non-contact moves to exploit whichever defensive stat is lower
- **Status Moves**: Many status moves are non-contact and don't care about defensive stats
- **Ability Suppression**: Gastro Acid, Neutralizing Gas shut down the defensive boost
- **Critical Hits**: Ignore defensive stat boosts (though Speed substitution isn't technically a boost)

### Synergies
- **Speed Boost**: Gradually increases defensive capability over time
- **Tailwind/Trick Room**: Team support affects both offensive and defensive capabilities
- **Choice Scarf**: Provides both speed control and defensive bulk
- **Weakness Policy**: Survives special hits better, potentially triggering the boost

### Version History
- **Elite Redux**: Custom ability unique to this ROM hack
- **Complement to Blur**: Designed as the non-contact counterpart to Blur's contact move specialization
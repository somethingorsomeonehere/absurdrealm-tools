---
id: 809
name: Blur
status: reviewed
character_count: 164
---

# Blur - Ability ID 809

## In-Game Description
"Uses Speed as defense stat when hit by contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by contact moves, the Pokemon uses its Speed stat instead of Defense or Special Defense for damage calculations. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Blur replaces the defender's Defense or Special Defense stat with their Speed stat when calculating damage from contact moves. This stat substitution occurs during the defensive stat calculation phase of damage calculation.

### Activation Conditions
- **Trigger**: When the Pokemon with Blur is hit by a contact move
- **Contact Move Definition**: Moves with the `contact = TRUE` flag in their move data
- **Target Application**: Applied to the Pokemon with Blur when defending

### Technical Implementation
```cpp
constexpr Ability Blur = {
    .onChooseDefensiveStat = +[](ON_CHOOSE_DEFENSIVE_STAT) -> int {
        CHECK(IsMoveMakingContact(move, gBattlerAttacker))
        return STAT_SPEED;
    },
    .onChooseDefensiveStatFor = APPLY_ON_TARGET,
};
```

The ability hooks into the `onChooseDefensiveStat` callback which is called during damage calculation in `CalcDefenseStat()`. When a contact move hits, it returns `STAT_SPEED` instead of the default `STAT_DEF` or `STAT_SPDEF`.

### Contact Moves (Examples)
**Physical Contact Moves**:
- Tackle, Scratch, Pound
- Punch moves (Mach Punch, Thunder Punch, etc.)
- Bite, Crunch
- Earthquake, Rock Slide
- Slash, Cut
- Most physical melee attacks

**Special Contact Moves**:
- Petal Dance
- Grass Knot
- Some signature special moves

### Non-Contact Moves (Not Affected)
- Flamethrower, Ice Beam, Thunderbolt
- Hyper Beam, Solar Beam
- Psychic, Shadow Ball
- Most projectile-based moves
- Most special attacks

### Damage Calculation Formula
When hit by contact moves:
- **Normal**: `Damage = (Attack x Move Power) / Defense`
- **With Blur**: `Damage = (Attack x Move Power) / Speed`

### Numerical Impact
For a Pokemon with:
- Defense: 70
- Special Defense: 70  
- Speed: 140

Against a contact move, effective bulk is **doubled** (140 vs 70).

### Interactions with Other Mechanics
- **Stat Boosts**: Speed boosts increase defensive effectiveness
- **Stat Drops**: Speed drops reduce defensive effectiveness
- **Items**: 
  - Choice Scarf boosts Speed to increased bulk
  - Iron Ball reduces Speed to decreased bulk
  - Assault Vest has no effect on Blur
- **Abilities**:
  - Speed Boost indirectly increases bulk over time
  - Paralysis status condition reduces effective Defense
  - Unaware ignores opponent's Speed boosts when calculating damage

### Bypassing Effects
- **Long Reach**: Prevents moves from making contact, so Blur won't activate
- **Protective Pads**: Held by attacker prevents contact, so Blur won't activate
- **Punching Glove**: For punch moves, prevents contact

### Strategic Implications
**Strengths**:
- Excellent against physical sweepers
- Synergizes with Speed-boosting moves/abilities
- Makes fast, frail Pokemon surprisingly bulky against contact moves
- Effective against priority contact moves

**Weaknesses**:
- Completely ineffective against special projectiles
- Vulnerable to status moves
- Speed drops severely impact bulk
- Paralysis cripples both offense and defense

### Example Damage Calculations
**Scenario**: Opponent's 252 Atk Garchomp Earthquake vs Blur Pokemon
- Base Stats: 70 HP / 70 Def / 140 Spe
- **Without Blur**: 85-100% damage (likely OHKO)
- **With Blur**: 42-50% damage (easy 2HKO)

### Common Users
Based on the codebase, Pokemon with Blur ability include:
- High-speed Pokemon as regular or innate ability
- Pokemon with 125+ Speed stats
- Often paired with other speed-based abilities like Unburden or Speed Boost

### Competitive Usage Notes
- **Role**: Defensive pivot against physical attackers
- **Synergy**: Works well with speed control and priority moves
- **Counters**: Special attackers, status moves, Trick Room
- **Team Support**: Provides unique defensive profile

### Counters
- **Special Attackers**: Completely bypass the ability
- **Status Moves**: Sleep, paralysis, toxic
- **Speed Control**: Trick Room, Thunder Wave
- **Non-Contact Physical**: Moves like Rock Slide, Earthquake (if non-contact)

### Synergies
- **Speed Boost**: Gradually increases bulk
- **Choice Scarf**: Immediate Speed boost
- **Tailwind**: Team speed support
- **U-turn/Volt Switch**: Maintains momentum while using bulk

### Version History
- **Elite Redux**: Introduced as part of the expanded ability system
- **ID 809**: Part of the 800+ custom ability range
- **Counterpart**: Pairs with Elude (ABILITY_ELUDE) which uses Speed for non-contact moves
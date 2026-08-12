---
id: 742
name: Magical Fists
status: reviewed
character_count: 119
---

# Magical Fists - Ability ID 742

## In-Game Description
"Punching moves use Special Attack and get a 1.3x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Punching moves use the Special Attack (still targets enemy's Defense unless stated otherwise) and deal 30% more damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MAGICAL FISTS** is a move conversion ability that transforms physical punching moves into special attacks while maintaining a significant damage boost.

### Core Mechanics:
- **Damage Multiplier**: 1.3x (30% boost) to all Iron Fist-boosted moves
- **Stat Conversion**: Forces punching moves to use Special Attack instead of Attack
- **Move Category**: Changes the attacking stat but keeps the move's original category for other interactions
- **Defensive Calculation**: Moves still target Defense or Special Defense based on their original category

### Technical Implementation:
```c
constexpr Ability MagicalFists = {
    .onOffensiveMultiplier = IronFist.onOffensiveMultiplier,  // 1.3x multiplier
    .onChooseOffensiveStat = +[](ON_CHOOSE_OFFENSIVE_STAT) -> int {
        CHECK(IsIronFistBoosted(move));
        return STAT_SPATK;
    },
};
```

### Affected Moves:
All moves with the FLAG_IRON_FIST_BOOST flag are affected:
- **Elemental Punches**: Fire Punch (75 BP to 97.5 BP), Ice Punch, Thunder Punch
- **Fighting Moves**: Focus Punch (150 BP to 195 BP), Dynamic Punch (100 BP to 130 BP), Mach Punch
- **Priority Moves**: Bullet Punch, Mach Punch, Vacuum Wave (already special)
- **Coverage Moves**: Shadow Punch, Meteor Mash, Dizzy Punch, Drain Punch
- **Heavy Hits**: Hammer Arm, Sky Uppercut, Close Combat

### Notable Pokemon with Access:
- **Grumpig**: Psychic-type with naturally high Special Attack (110 base)
  - Can utilize Focus Punch as a 195 BP special nuke
  - Access to elemental punches for coverage
- **Darmanitan Redux Aura Form**: Rock/Fighting with 140 Special Attack
  - Has Magical Fists as an innate ability
  - Devastating with STAB Fighting punches using Special Attack

### Strategic Implications:
1. **Stat Investment Freedom**: No need to split EVs between Attack and Special Attack
2. **Unexpected Coverage**: Special attackers gain access to traditionally physical coverage
3. **Wall Breaking**: Physical walls expecting punching moves face special damage instead
4. **Item Synergy**: Works with Choice Specs, Life Orb, and other special boosting items

### Damage Comparisons:
**Grumpig Example** (110 base Special Attack):
- Regular Ice Punch: 75 BP physical (uses 65 Attack)
- Magical Fists Ice Punch: 97.5 BP special (uses 110 Special Attack)
- Nearly triple damage output due to stat difference and multiplier

### Interactions:
- **With Other Abilities**: 
  - Brawling Wyvern: Dragon moves also use Special Attack if user has both
  - Junshi Sanda: Striker moves become special if user has both
- **Move Mechanics**: 
  - Contact status still applies (Iron Barbs, Rough Skin damage)
  - Can still trigger King's Rock flinch
  - Affected by Psychic Terrain's priority immunity

### Competitive Usage:
- **Lead Sets**: Grumpig with Focus Punch prediction
- **Coverage**: Special attackers breaking through Chansey/Blissey with physical Fighting coverage
- **Mixed Attackers**: Pokemon that can bluff physical or special sets
- **Terrain Teams**: Psychic Terrain doesn't block Mach Punch since it becomes special

### Common Sets:
**Grumpig @ Choice Specs**
- Focus Punch (195 BP STAB after boost)
- Fire Punch (coverage)
- Thunder Punch (coverage)
- Psychic (secondary STAB)

### Counters:
- High Special Defense walls that resist Fighting
- Ghost-types immune to Fighting moves
- Psychic Terrain blocking priority punches
- Fort Knox ability negating the damage boost

### Version History:
- Elite Redux exclusive ability
- Created to give special attackers unique coverage options
- One of several "stat swap" abilities in Elite Redux
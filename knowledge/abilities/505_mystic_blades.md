---
id: 505
name: Mystic Blades
status: reviewed
character_count: 110
---

# Mystic Blades - Ability ID 505

## In-Game Description
"Keen edge moves become special and deal 30% more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Keen Edge moves become Special (deal Special damage and use the Special Attack stat) and deal 30% more damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**MYSTIC BLADES** is a move conversion ability that transforms physical slashing and cutting moves into special attacks while providing significant damage amplification.

### Core Mechanics:
- **Damage Multiplier**: 1.3x (30% boost) to all keen edge moves
- **Move Conversion**: Changes physical keen edge moves to special split
- **Stat Usage**: Converted moves use Special Attack and target Special Defense
- **Move Count**: Affects over 50 moves with the FLAG_KEEN_EDGE_BOOST flag

### Technical Implementation:
```c
constexpr Ability MysticBlades = {
    .onOffensiveMultiplier = KeenEdge.onOffensiveMultiplier,  // 1.3x damage boost
    .onSwapSplit = +[](ON_SWAP_SPLIT) -> int {
        CHECK(gBattleMoves[move].split == SPLIT_PHYSICAL)
        CHECK(gBattleMoves[move].flags & FLAG_KEEN_EDGE_BOOST);
        return TRUE;  // Converts physical keen edge moves to special
    },
};
```

### Complete List of Affected Moves:
**Basic Slashes:**
- Cut, Slash, Fury Swipes, Scratch

**Elemental Slashes:**
- Razor Leaf (Grass), Air Cutter (Flying), Air Slash (Flying), Psycho Cut (Psychic)

**High-Power Slashes:**
- Leaf Blade (90 BP), Night Slash (70 BP), Cross Chop (100 BP), Sacred Sword (90 BP)

**Multi-Hit/Effect Slashes:**
- Fury Cutter (40 BP, power doubles), X-Scissor (80 BP), Dual Chop (40 BP x2)

**Claw Attacks:**
- Dragon Claw (80 BP), Shadow Claw (70 BP), Metal Claw (50 BP), Crush Claw (75 BP)

**Specialized Cuts:**
- Guillotine (OHKO), False Swipe (40 BP, leaves 1 HP), Razor Wind (80 BP, 2-turn)

**Priority Moves:**
- Aerial Ace (60 BP, never misses), Aqua Jet (40 BP, +1 priority when slashing)

**Signature Moves:**
- Secret Sword (85 BP), Solar Blade (125 BP), Behemoth Blade (100 BP)

### Strategic Implications:
1. **Type Coverage Expansion**: Special attackers gain access to diverse physical coverage
2. **Wall Breaking**: Bypasses physical walls expecting slashing moves
3. **Critical Hit Synergy**: Many keen edge moves have high crit ratios
4. **Weather Teams**: Solar Blade becomes a special sun nuke

### Notable Interactions:
- **Solar Blade**: Becomes a 125 BP special Grass move in sun (162.5 BP after boost)
- **Sacred Sword**: Ignores defense boosts as a special move
- **Night Slash**: High crit special Dark move
- **Leaf Blade**: 90 BP to 117 BP special Grass with high crit

### Damage Comparisons:
**Example: Alakazam with Mystic Blades** (135 Special Attack):
- Regular Psycho Cut: 70 BP physical (uses 50 Attack)
- Mystic Blades Psycho Cut: 91 BP special (uses 135 Special Attack)
- Over 4x damage increase from stat difference and multiplier

### Competitive Usage:
- **Coverage Monster**: Special attackers with unexpected slashing coverage
- **Sun Teams**: Solar Blade becomes terrifying special nuke
- **Crit Builds**: High crit moves + special damage
- **Speed Control**: Aerial Ace for priority special Flying damage

### Synergies:
- **Sharpness**: Would stack if Pokemon had both abilities
- **Critical Hit Boosts**: Scope Lens, Super Luck for crit slashes
- **Weather**: Solar Blade in sun, no charge needed
- **Terrain**: Grassy Terrain boosts Leaf Blade further

### Common Users:
While any Pokemon with access to Mystic Blades benefits, ideal users have:
- High Special Attack
- Access to multiple slashing moves
- Need for physical coverage as special attackers

### Example Set:
**Theoretical Special Attacker @ Life Orb**
- Leaf Blade (Grass coverage)
- Night Slash (Dark coverage)
- Psycho Cut (Psychic STAB)
- Air Slash (Flying coverage)

### Counters:
- High Special Defense walls
- Pokemon resistant to common slash types
- Priority users before conversion attacks land
- Fort Knox negates the damage boost

### Related Abilities:
- **Keen Edge**: Same boost but keeps moves physical
- **Sharpness**: Different boost amount, affects similar moves
- **Pony Power**: Combines both Keen Edge and Mystic Blades effects

### Version History:
- Elite Redux exclusive ability
- Part of the "move conversion" ability family
- Designed to create unique special attacking archetypes
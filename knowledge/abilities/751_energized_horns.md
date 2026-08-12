---
id: 751
name: Energized Horns
status: reviewed
character_count: 105
---

# Energized Horns - Ability ID 751

## In-Game Description
"Horn moves become special and deal 30% more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Horn moves become Special (deal Special damage and use the Special Attack stat) and deal 30% more damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**ENERGIZED HORNS** (displayed as "Energy Horns" in-game) is a move conversion ability that transforms physical horn-based moves into special attacks while providing substantial damage amplification.

### Core Mechanics:
- **Damage Multiplier**: 1.3x (30% boost) to all horn-based moves
- **Move Conversion**: Changes physical horn moves to special category
- **Stat Usage**: Converted moves use Special Attack and target Special Defense
- **Move Detection**: Checks for `hornBased` flag on moves

### Technical Implementation:
```c
constexpr Ability EnergizedHorns = {
    .onOffensiveMultiplier = MightyHorn.onOffensiveMultiplier,  // 30% damage boost
    .onSwapSplit = +[](ON_SWAP_SPLIT) -> int {
        CHECK(gBattleMoves[move].split == SPLIT_PHYSICAL)
        CHECK(gBattleMoves[move].hornBased);
        return TRUE;  // Makes the move special
    },
};
```

### Horn-Based Moves in Elite Redux:
**Standard Horn Moves:**
- **Horn Attack** - Normal, 65 BP
- **Megahorn** - Bug, 120 BP, 85% accuracy
- **Horn Drill** - Normal, OHKO move
- **Smart Strike** - Steel, 70 BP, never misses
- **Horn Leech** - Grass, 75 BP, heals 50% damage dealt

**Potential Custom Horn Moves:**
Elite Redux may include additional horn-based moves marked with the `hornBased` flag

### Strategic Implications:
1. **Mixed Attacker Creation**: Physical horn users become special threats
2. **Wall Breaking**: Bypasses high Defense Pokemon like Skarmory, Forretress
3. **Type Coverage**: Horn moves span Normal, Bug, Steel, and Grass types
4. **STAB Synergy**: Bug-types with Megahorn get special Bug STAB

### Damage Calculations:
**Example: Heracross with Energized Horns** (40 Special Attack normally):
- Regular Megahorn: 120 BP physical (uses 125 Attack)
- Energized Megahorn: 156 BP special (uses 40 Special Attack)

While base SpA is lower, the ability opens new EV spread options and catches opponents off-guard.

### Notable Interactions:
- **Megahorn**: Becomes a 156 BP special Bug nuke
- **Smart Strike**: Never-miss special Steel coverage
- **Horn Leech**: Special Grass move that heals
- **Horn Drill**: OHKO that targets Special Defense (if it connects)

### Ideal Users:
Pokemon that benefit most from Energized Horns:
- Horn users with decent Special Attack
- Mixed attackers wanting to diversify damage types
- Pokemon facing physically defensive metagames
- Bug-types seeking special STAB options

### EV Spread Considerations:
With Energized Horns, horn users can run:
- **Special Attack Investment**: Maximize horn move damage
- **Mixed Spreads**: Both physical and special coverage
- **Bulky Special**: Use defensive investment with special horn attacks

### Example Set:
**Theoretical Horn User @ Life Orb**
- Megahorn (Bug STAB, 156 BP special)
- Smart Strike (Steel coverage, never misses)
- Horn Leech (Grass coverage, recovery)
- [Non-horn coverage move]

### Competitive Usage:
- **Lead Breaker**: Surprise special damage on typical physical walls
- **Stallbreaker**: Horn Leech provides recovery while dealing special damage
- **Weather Teams**: No weather dependency, consistent damage
- **Anti-Meta**: Counters Defense-stacking strategies

### Counters:
- High Special Defense walls (Blissey, Chansey)
- Resist-heavy typings against horn moves
- Faster special attackers
- Fort Knox ability blocks the damage boost

### Synergies:
- **Mighty Horn**: Would stack if Pokemon had both abilities
- **Special Attack Boosts**: Nasty Plot, Work Up enhance horn damage
- **Screens Support**: Light Screen more valuable than Reflect
- **Trick Room**: Slower horn users become special threats

### Comparison to Similar Abilities:
- **Mighty Horn**: Same boost but keeps moves physical
- **Magical Fists**: Converts punches to special
- **Mythical Arrows**: Converts arrows to special
- **Mystic Blades**: Converts slashes to special

### Version History:
- Elite Redux exclusive ability
- Part of the "physical-to-special" ability family
- Designed to create unique offensive dynamics with horn moves
- Name displays as "Energy Horns" in-game but coded as "EnergizedHorns"
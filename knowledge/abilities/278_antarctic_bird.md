---
id: 278
name: Antarctic Bird
status: reviewed
character_count: 115
---

# Antarctic Bird - Ability ID 278

## In-Game Description
"Ice-type and Flying-type moves get a 1.3x power boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Antarctic Bird grants a 1.3x power boost to both Ice-type and Flying-type moves. Additive with other damage boosts.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Antarctic Bird provides a **30% damage boost (1.3x multiplier)** to all Ice-type and Flying-type moves used by the Pokemon with this ability.

### Activation Conditions
- Triggers on any offensive move of Ice or Flying type
- Works on both physical and special attacks
- Affects multi-hit moves (each hit gets the boost)
- Applies to status moves that deal direct damage

### Technical Implementation
```cpp
constexpr Ability AntarcticBird = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FLYING || moveType == TYPE_ICE) MUL(1.3);
        },
};
```

### Move Compatibility
**Ice-type moves affected:**
- Ice Beam, Blizzard, Ice Punch, Icicle Crash
- Freeze-Dry, Ice Shard, Avalanche, Sheer Cold
- All other Ice-type offensive moves

**Flying-type moves affected:**
- Hurricane, Air Slash, Brave Bird, Acrobatics  
- Aerial Ace, Sky Attack, Drill Peck, Fly
- All other Flying-type offensive moves

### Damage Calculation
**Base calculation:** Base Power x 1.3 x other multipliers
**With STAB:** Base Power x 1.3 x 1.5 = 1.95x total boost
**Example:** Ice Beam (90 BP) to 90 x 1.3 = 117 effective power

### Interactions with Other Abilities/Mechanics
- **Stacks multiplicatively** with STAB (1.3 x 1.5 = 1.95x total)
- **Stacks with items** like Choice Band/Specs, Life Orb
- **Works with weather boosts** (e.g., Blizzard in Hail gets both boosts)
- **Compatible with critical hits** and other damage modifiers
- **Does not affect** type-changing abilities like Normalize or Pixilate

### Strategic Implications
- Exceptional on dual Ice/Flying types like Articuno variants
- Makes mixed attackers viable with both physical and special coverage
- Provides consistent power boost without drawbacks
- Excellent for breaking walls with boosted STAB moves

### Common Users
**Primary users in Elite Redux:**
- **Articuno variants** (Articuno EX, Mega Articuno) - Natural dual-type synergy
- **Empoleon line** (Prinplup, Empoleon, Empoleon Redux) - Steel/Water types with innate boost
- **Eiscue forms** - Ice/Water penguin with perfect synergy
- **Various legendary birds** with ice movesets

### Competitive Usage Notes
- **Tier placement:** High-value ability on appropriate Pokemon
- **Team synergy:** Pairs well with weather setters (Hail for Blizzard accuracy)
- **Coverage options:** Provides reliable STAB alternative for mixed sets
- **Wall-breaking potential:** 1.95x STAB moves destroy defensive cores

### Counters
- **Fire-types** resist Ice moves and are immune to burns from Ice moves
- **Electric and Rock types** resist Flying moves  
- **Steel-types** resist both Ice and Flying attacks
- **Thick Fat** halves Ice-type damage
- **Filter/Solid Rock** reduce super-effective damage

### Synergies  
- **Snow Warning** - Boosts Blizzard accuracy to 100%
- **Slush Rush** - Speed boost in hail complements power boost
- **Ice Scales** - Defensive synergy for bulky attackers
- **Choice items** - Stack damage multipliers for massive power
- **Life Orb** - Additional 1.3x boost (with recoil)

### Version History
- Added in Elite Redux as custom ability #278
- Designed specifically for ice/flying themed Pokemon
- Part of the expanded ability roster for enhanced gameplay diversity
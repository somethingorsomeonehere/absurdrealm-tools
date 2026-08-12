---
id: 271
name: Keen Edge
status: reviewed
character_count: 45
---

# Keen Edge - Ability ID 271

## In-Game Description
"Boosts the power of slashing moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Keen Edge boosts all slashing attacks by 30%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Keen Edge provides a flat 1.3x (30%) damage multiplier to any move that has the `FLAG_KEEN_EDGE_BOOST` flag set. This multiplier is applied during the offensive damage calculation phase.

### Technical Implementation
```cpp
constexpr Ability KeenEdge = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].flags & FLAG_KEEN_EDGE_BOOST) MUL(1.3);
        },
};
```

### Activation Conditions
- Move must have the `keen_edge: true` flag in its definition
- Works on both physical and special slashing moves
- No additional requirements - always active when using eligible moves

### Complete List of Affected Moves
**Classic Slashing Moves:**
- Slash - Always crits, Keen Edge boost
- Night Slash - High crit ratio, Keen Edge boost  
- Leaf Blade - High crit ratio, Keen Edge boost
- Razor Leaf - Always crits, hits both foes, Keen Edge boost
- Fury Cutter - Multi-hit with increasing power, Keen Edge boost
- False Swipe - Can't KO, 50% bleed chance, Keen Edge boost

**Specialized Cutting Moves:**
- Air Slash - 30% flinch chance, air-based, Keen Edge boost
- Psycho Cut - Psychic blades, high crit ratio, Keen Edge boost
- Cross Poison - Hits twice, high crit, 10% poison, Keen Edge boost
- Sacred Sword - Ignores stat changes, Keen Edge boost
- Razor Shell - 50% Defense drop chance, Keen Edge boost

**Elemental Blade Moves:**
- Cryo Blade - Ice slashing, 10% frostbite chance
- Shock Blade - Electric slashing, 10% paralysis chance  
- Flame Blade - Fire slashing, 10% burn chance
- Stone Axe - Rock slashing, sets Stealth Rock
- Steel Blade - Steel slashing, 10% Stealth Rock chance

**Wind-Based Cutting:**
- Razor Wind - Super effective vs Rock, +1 priority in Tailwind
- Air Cutter - Sharp wind strikes, high crit ratio, air-based

**Multi-Hit Slashing:**
- Fury Swipes - 2-5 hits with claws/scythes, high crit rate
- Dual Chop - Hits twice with brutal strikes, high crit ratio

### Interactions with Other Abilities
**Synergistic Abilities:**
- **Mystic Blades**: Also uses Keen Edge's damage boost, plus converts physical slashing moves to special
- **Pony Power (Blade's Essence)**: Combines Keen Edge + Mystic Blades effects
- **Sweeping Edge Plus (Blademaster)**: Combines Keen Edge + Sweeping Edge (makes moves hit both foes and never miss)
- **Molten Blades**: Keen Edge boost + 20% burn chance on slashing moves
- **Power Edge**: Keen Edge moves target Special Defense and get additional 1.3x boost
- **Best Offense**: Keen Edge boost + makes slashing moves swap Attack/Special Attack splits
- **Magus Blades**: Keen Edge boost + dual wielding + stat swapping effects

### Strategic Implications
- **Offensive Powerhouse**: 30% damage boost is substantial, making slashing moves hit significantly harder
- **Wide Move Pool**: Many common attacking moves benefit from this ability
- **Crit Synergy**: Most slashing moves have high crit ratios, creating powerful offensive combinations  
- **Type Coverage**: Slashing moves span multiple types (Normal, Grass, Dark, Flying, Steel, etc.)
- **Physical/Special Flexibility**: Works with both physical moves (Slash, Night Slash) and special moves (Air Slash, Psycho Cut)

### Example Damage Calculations
**Base Slash (70 BP):**
- Without Keen Edge: 70 BP
- With Keen Edge: 91 BP effective (70 x 1.3)

**Leaf Blade (90 BP):**
- Without Keen Edge: 90 BP  
- With Keen Edge: 117 BP effective (90 x 1.3)

**Air Slash (75 BP Special):**
- Without Keen Edge: 75 BP
- With Keen Edge: 97.5 BP effective (75 x 1.3)

### Common Users
- **Grass-types**: Utilize Leaf Blade, Razor Leaf, and other plant-based cutting moves
- **Dark-types**: Benefit from Night Slash and shadow-based slashing attacks
- **Flying-types**: Use Air Slash and Razor Wind effectively
- **Steel-types**: Access various blade-based moves with type synergy
- **Normal-types**: Classic slashing moves like Slash and Fury Swipes
- **Bug-types**: Fury Cutter and similar multi-hit slashing moves

### Competitive Usage Notes
- **Offensive Pressure**: Provides consistent damage boost without setup requirements
- **Move Diversity**: Encourages diverse movesets with different slashing attacks
- **Crit Fishing**: Pairs excellently with the high crit rates of many slashing moves
- **Type Coverage**: Allows for broad offensive coverage with boosted moves
- **Immediate Impact**: No setup required - boost applies immediately

### Counters
- **Physical Walls**: High Defense stats can mitigate boosted physical slashing moves
- **Special Walls**: High Special Defense for special slashing moves like Air Slash
- **Intimidate**: Reduces Attack stat, partially offsetting the Keen Edge boost for physical moves
- **Burn**: Halves physical Attack, significantly reducing physical slashing damage
- **Abilities that Reduce Damage**: Abilities like Multiscale, Filter, or Solid Rock
- **Defensive Typing**: Resisting the slashing move's type still provides defensive advantage

### Synergies
- **High Critical Hit Moves**: Most slashing moves have high crit ratios, multiplying the effective damage boost
- **STAB**: Same-type attack bonus stacks multiplicatively with Keen Edge
- **Choice Items**: Choice Band/Specs further amplify the already-boosted slashing moves  
- **Weather Effects**: Rain boosts for Water-type slashing moves, Sun for Fire-type blade moves
- **Terrain Effects**: Various terrains can provide additional boosts to certain slashing moves
- **Life Orb**: Stacks multiplicatively for even higher damage output

### Version History
- Introduced as part of Elite Redux's expanded ability system
- Consistently provides 1.3x multiplier since implementation
- Works with both existing and newly-added slashing moves
- Flag system allows for easy expansion of compatible moves
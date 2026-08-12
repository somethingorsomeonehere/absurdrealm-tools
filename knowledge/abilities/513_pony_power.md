---
id: 513
name: Pony Power
status: reviewed
character_count: 153
---

# Pony Power (Blade's Essence) - Ability ID 513

## In-Game Description
"Keen Edge + Mystic Blades."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Keen Edge moves become Special (deal Special damage and use the Special Attack stat) and deal 30% more damage. Also gives another 30% to Keen Edge moves. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Pony Power (internally named "Blade's Essence") is a hybrid offensive ability that combines two distinct blade-focused abilities: Keen Edge and Mystic Blades. This creates a powerful synergy for Pokemon that rely on slicing attacks.

### Component Abilities Breakdown

#### Keen Edge Component
- **Damage boost**: Increases power of slicing moves by 30% (1.3x multiplier)
- **Target moves**: All moves with FLAG_KEEN_EDGE_BOOST flag
- **Activation**: Triggers on offensive multiplier calculation

#### Mystic Blades Component  
- **Stat swapping**: Physical slicing moves can use Special Attack if it's higher
- **Split conversion**: Allows physical slicing moves to benefit from higher special attack stat
- **Flexibility**: Enables mixed attackers to optimize damage output

### Activation Conditions
- **Move requirement**: Only affects moves flagged with FLAG_KEEN_EDGE_BOOST
- **Move types**: Includes approximately 50 different slicing/cutting moves
- **No weather/status requirements**: Always active when using qualifying moves

### Technical Implementation
```c
// Pony Power combines both abilities
constexpr Ability PonyPower = {
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
        // Apply Keen Edge 30% boost
        KeenEdge.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        // Apply Mystic Blades 30% boost (same as Keen Edge)
        MysticBlades.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
    },
    // Enable stat swapping for physical slicing moves
    .onSwapSplit = MysticBlades.onSwapSplit,
};
```

### Eligible Moves (Examples)
**Common Slicing Moves:**
- Slash, Night Slash, Psycho Cut
- Leaf Blade, Air Slash, Stone Edge
- Fury Cutter, Shadow Claw, X-Scissor
- Sacred Sword, Secret Sword, Razor Shell
- And approximately 40+ other slicing moves

### Stat Optimization Logic
1. **Physical slicing move used**
2. **Check**: Is Special Attack > Attack?
3. **Yes**: Use Special Attack for damage calculation + 30% boost
4. **No**: Use Attack for damage calculation + 30% boost
5. **Result**: Always uses the better offensive stat with power boost

### Exclusive User: Keldeo Resolute Form
- **Species**: Keldeo (Resolute Form only)
- **Base stats**: 91/117/70/129/70/123
- **Optimal usage**: Special Attack (129) > Attack (117), so physical slicing moves use SpA
- **Innate abilities**: Fighter, Arcane Force, Riptide
- **Typing**: Water/Fighting

### Strategic Implications
- **Mixed attacker optimization**: Perfect for Pokemon with high Special Attack using physical moves
- **Move variety**: Can run both physical and special slicing moves effectively
- **Unpredictability**: Physical moves might use special attack, confusing opponents
- **Coverage expansion**: Enables access to physical slicing moves without stat penalty

### Important Interactions
- **Physical moves only**: Stat swapping only affects physical slicing moves, not special ones
- **Multiplier stacking**: 30% boost applies regardless of which stat is used
- **Critical hits**: Higher stat usage applies to critical hit calculations too
- **Ability suppression**: Both components disabled if ability is suppressed

### Competitive Usage Notes
- **Keldeo Resolute exclusive**: Only available on one form of one Pokemon
- **Sacred Sword synergy**: Keldeo's signature move benefits greatly from this ability
- **Mixed sets**: Enables effective mixed attacking sets with slicing moves
- **Stat distribution**: Keldeo's 129 SpA vs 117 Atk makes physical slicing moves hit harder

### Damage Calculation Example
```
Base Scenario: Sacred Sword (Physical, 90 BP)
- Normal: 90 BP x Attack stat
- With Pony Power: 90 BP x 1.3 x Special Attack (if SpA > Atk)
- Keldeo Resolute: Uses 129 SpA instead of 117 Atk, plus 30% boost
```

### Synergies
- **High Special Attack**: Maximizes the stat-swapping benefit
- **Physical slicing moves**: Sacred Sword, Leaf Blade, Stone Edge
- **Mixed movesets**: Can run both physical and special attacks effectively
- **Coverage moves**: Physical slicing moves for coverage become viable

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Non-slicing moves**: Ability provides no benefit to other move types
- **Physical walls**: Still need to deal with physical defensive stats
- **Burns**: Attack drops still affect damage if Attack stat is used

### Version History
- **Elite Redux exclusive**: Custom ability not found in official games
- **Hybrid design**: Combines mechanics from two separate abilities
- **Keldeo signature**: Designed specifically for Keldeo's Resolute form
- **Mixed attacker support**: Part of Elite Redux's expanded battle mechanics

### Comparison to Component Abilities
- **Keen Edge alone**: Only provides 30% boost, no stat flexibility
- **Mystic Blades alone**: Only provides stat swapping, no damage boost  
- **Pony Power**: Best of both worlds - damage boost AND stat optimization
- **Unique value**: Only ability that combines offensive boost with stat swapping
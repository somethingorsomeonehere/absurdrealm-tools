---
id: 588
name: Iron Serpent
status: reviewed
character_count: 43
---

# Iron Serpent - Ability ID 588

## In-Game Description
"Ups 'supereffective' by 33%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Super effective attacks are boosted by 33%.

## Detailed Mechanical Explanation

Iron Serpent is a powerful offensive ability that amplifies super-effective damage, turning type advantages into overwhelming assaults. By boosting already effective moves by an additional 33%, it creates devastating offensive pressure against teams with common type weaknesses.

### Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Implementation**: Shares logic with Winged King ability

### Core Mechanics
```cpp
constexpr Ability IronSerpent = {
    .onOffensiveMultiplier = WingedKing.onOffensiveMultiplier,
};

// WingedKing implementation:
.onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
    if (typeEffectivenessMultiplier >= UQ_4_12(2.0)) MUL(1.33);
}
```

### Damage Calculation
- **Trigger**: Type effectiveness ≥ 2.0x
- **Boost**: 1.33x multiplier (33% increase)
- **Final Damage**: 2.0x x 1.33x = 2.66x (or 4.0x x 1.33x = 5.32x for 4x weakness)
- **Stacking**: Multiplies with other damage modifiers

### Strategic Applications

### Offensive Powerhouse
- Transforms 2x effectiveness into 2.66x damage
- Makes 4x effectiveness deal 5.32x damage
- Punishes common type weaknesses severely
- Excellent for breaking through defensive cores

### Coverage Optimization
- Rewards diverse movepools with good coverage
- Makes coverage moves significantly more threatening
- Reduces need for STAB moves in some cases
- Enables OHKOs that normally wouldn't be possible

### Team Building Considerations
- Best on Pokemon with wide move coverage
- Synergizes with Pokemon having multiple attacking types
- Valuable on mixed attackers who can exploit various weaknesses
- Complements teams that scout opponent weaknesses

### Mechanics Details

### Type Effectiveness Thresholds
- **Not Triggered**: 0.25x, 0.5x, 1x effectiveness
- **Triggered**: 2x, 4x effectiveness
- **Edge Case**: Abilities that modify type effectiveness can affect triggering

### Interaction with Other Abilities
- Stacks with STAB (1.5x)
- Stacks with items (Choice Specs/Band, Life Orb, etc.)
- Works with Adaptability's enhanced STAB
- Unaffected by opponent's resistance abilities on trigger condition

### Notable Users

### Primary Users
1. **Miraidon** (Legendary)
   - Electric/Dragon typing provides excellent coverage
   - Innate abilities: Iron Serpent, Hadron Engine, Dragon's Maw
   - Exceptional special attack stat
   - Signature moves benefit from the boost

### Synergistic Pokemon Types
- Electric-types: Hit Water/Flying for boosted damage
- Dragon-types: Wide neutral coverage becomes threatening
- Fighting-types: Exploit common Rock/Steel/Dark weaknesses
- Ground-types: Devastating against Electric/Fire/Rock/Steel

### Competitive Analysis

### Tier: High
Iron Serpent earns a high tier due to its consistent damage amplification against common team compositions.

### Strengths
1. **Massive Damage**: 2.66x or 5.32x multipliers are game-changing
2. **No Setup Required**: Immediate pressure from turn one
3. **Coverage Reward**: Makes coverage moves into primary threats
4. **Psychological Pressure**: Opponents must respect all coverage options

### Weaknesses
1. **Type Dependent**: Useless against teams without weaknesses
2. **Predictable**: Opponents know which moves will be boosted
3. **No Defensive Utility**: Pure offensive ability
4. **Coverage Requirement**: Needs diverse movepool to maximize

### Usage Strategies

### Lead Breaker
- Open with coverage moves to immediately pressure
- Force switches to gain momentum
- Scout team for weaknesses to exploit

### Late Game Cleaner
- Save for when resistances are removed
- Clean up weakened teams with boosted coverage
- Exploit revealed weaknesses

### Wallbreaker
- Even defensive Pokemon struggle with 2.66x+ damage
- Break through would-be safe switches
- Force unfavorable trades

### Counter Strategies

### Team Building
- Minimize common weaknesses
- Use Pokemon with unique type combinations
- Include Pokemon that resist common coverage

### In-Battle
- Switch to Pokemon that resist expected coverage
- Use Protect to scout moves
- Prioritize removing Iron Serpent user
- Terrain/weather to boost your own moves

### Conclusion

Iron Serpent represents Elite Redux's philosophy of rewarding smart type matchups with tangible benefits. Its straightforward yet powerful effect makes it a premier offensive ability that shapes both team building and battle strategy. While it lacks defensive utility or setup potential, the raw damage output against the right targets makes it a fearsome ability in capable hands.

The ability shines brightest on Pokemon like Miraidon who combine excellent stats, diverse coverage options, and complementary abilities to create an offensive powerhouse that can threaten entire teams with properly chosen moves.
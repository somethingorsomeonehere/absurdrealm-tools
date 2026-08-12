---
id: 520
name: Devourer
status: reviewed
character_count: 191
---

# Devourer - Ability ID 520

## In-Game Description
"Strong Jaw + Primal Maw."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts biting moves by 30%. All biting moves to hit twice. The first hit deals 100% damage while the second hit deals 40% damage. Independently rolls secondary effects of attacks on each hit.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Devourer is a combination ability that merges two distinct effects: Strong Jaw's damage boost and Primal Maw's multi-hit enhancement. It specifically targets moves with biting, jaw, or fang-based attacks.

### Strong Jaw Component
- **Damage boost**: 30% (1.3x multiplier) increase to all moves with the FLAG_STRONG_JAW_BOOST flag
- **Calculation**: Applied as an offensive multiplier in damage calculation
- **Stacking**: Stacks multiplicatively with other damage boosts

### Primal Maw Component
- **Multi-hit enhancement**: Changes second hit damage from 25% to 40% of first hit
- **Activation condition**: Only applies to biting/jaw moves that would trigger multi-hit effects
- **Parental Bond type**: Uses PARENTAL_BOND_PRIMAL_MAW multiplier (0.4 instead of 0.25)

### Technical Implementation
```c
// Devourer ability definition
constexpr Ability Devourer = {
    .onParentalBond = PrimalMaw.onParentalBond,
    .onOffensiveMultiplier = StrongJaw.onOffensiveMultiplier,
};

// Strong Jaw damage boost
if (gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST) MUL(1.3);

// Primal Maw multi-hit enhancement
if (gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST) 
    return PARENTAL_BOND_PRIMAL_MAW; // 40% second hit instead of 25%
```

### Affected Moves
All moves with the FLAG_STRONG_JAW_BOOST flag receive both benefits:
- **Bite**: Dark-type physical move, 30% flinch chance
- **Crunch**: Dark-type physical move, lowers Defense
- **Fire Fang**: Fire-type physical move, burn/flinch chance
- **Ice Fang**: Ice-type physical move, freeze/flinch chance  
- **Thunder Fang**: Electric-type physical move, paralysis/flinch chance
- **Hyper Fang**: Normal-type physical move, 10% flinch chance
- **Super Fang**: Normal-type physical move, halves HP
- **Poison Fang**: Poison-type physical move, badly poison chance
- **Pluck**: Flying-type physical move, consumes berry
- **Leech Life**: Bug-type physical move, drains HP

### Important Interactions
- **Multi-hit abilities**: When combined with abilities like Parental Bond, Skill Link, or Multi-Hit moves, the enhanced second hit multiplier provides significant damage increases
- **Type coverage**: Affects moves across multiple types (Dark, Fire, Ice, Electric, Normal, Poison, Flying, Bug)
- **Status effects**: Many affected moves have secondary effects that aren't enhanced by Devourer
- **Critical hits**: Both damage boost and enhanced second hit can benefit from critical hits

### Strategic Implications
- **Physical attacker synergy**: Best on physical attackers with access to multiple biting moves
- **Multi-type coverage**: Provides consistent boost across diverse move types
- **Late-game scaling**: Becomes more powerful with multi-hit enhancements
- **Versatile offense**: Combines immediate damage boost with multi-hit potential

### Damage Calculations
- **Single hit**: Base damage x 1.3 (Strong Jaw boost)
- **Multi-hit first**: Base damage x 1.3 (Strong Jaw boost)  
- **Multi-hit second**: (Base damage x 1.3) x 0.4 = Base damage x 0.52
- **Total multi-hit**: Base damage x 1.82 (vs normal 1.55)

### Common Users
- Physical attackers with diverse jaw-based movesets
- Pokemon with natural multi-hit abilities
- Mixed attackers who can utilize type coverage
- Bulky physical attackers who benefit from sustained damage

### Competitive Usage Notes
- **Setup sweeper potential**: Strong consistent damage boost across move types
- **Wall breaking**: Enhanced damage helps break through defensive Pokemon
- **Type coverage**: Multiple move types prevent easy switching
- **Multi-hit synergy**: Exceptional with abilities that enable multi-hit attacks

### Counters
- **Physical walls**: High Defense still reduces effectiveness
- **Ghost types**: Immune to Normal-type jaw moves (Hyper/Super Fang)
- **Intimidate**: Reduces physical attack before damage calculation
- **Burn status**: Halves physical attack power
- **Rocky Helmet**: Punishes contact moves (most jaw moves make contact)

### Synergies
- **Parental Bond**: Maximizes the Primal Maw component
- **Choice Band/Life Orb**: Stacks with Strong Jaw damage boost
- **Type-enhancing items**: Further boosts specific jaw move types
- **Speed control**: Allows consistent use of diverse jaw moves
- **Setup moves**: Swords Dance amplifies the damage boost effect

### Version History
- Custom Elite Redux ability combining Strong Jaw and Primal Maw
- Provides unique multi-hit enhancement not found in standard games
- Part of Elite Redux's expanded ability system for enhanced strategic depth
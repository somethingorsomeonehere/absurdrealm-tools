---
id: 753
name: Crust Coat
status: reviewed
character_count: 215
---

# Crust Coat - Ability ID 753

## In-Game Description
"Immune to critical hits. Takes 20% less damage from attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Incoming damage is reduced by 20% (x0.8), multiplicative with other damage reduction. Additionally, critical hits are blocked, functioning as regular hits and not activating on-crit effects like To The Bone's bleed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Crust Coat is a powerful defensive ability that combines two distinct protective effects:

1. **Critical Hit Immunity**: Complete immunity to critical hits from all sources
2. **Damage Reduction**: Reduces all incoming damage by 20% (multiplies damage by 0.8)

### Activation Conditions
- **Always Active**: Both effects are passive and apply automatically
- **All Damage Types**: The 20% reduction applies to physical, special, and fixed damage moves
- **All Critical Sources**: Immunity applies to natural crits, high crit ratio moves, and guaranteed crit effects

### Technical Implementation
```cpp
constexpr Ability CrustCoat = {
    .onDefensiveMultiplier = BattleArmor.onDefensiveMultiplier,  // MUL(.8) - 20% damage reduction
    .onCrit = BattleArmor.onCrit,                              // return NEVER_CRIT
    .onCritFor = BattleArmor.onCritFor,                        // APPLY_ON_TARGET
    .breakable = TRUE,
};
```

### Damage Calculation Example
- **Base Damage**: 100 HP
- **With Crust Coat**: 100 x 0.8 = 80 HP (20% reduction)
- **Potential Critical Hit**: Blocked entirely, no additional damage

### Interactions with Other Mechanics

#### What It Blocks
- Natural critical hits (1/24 or 1/16 chance depending on generation mechanics)
- High critical hit ratio moves (Slash, Psycho Cut, etc.)
- Guaranteed critical hit moves (Frost Breath, Storm Throw)
- Critical hit boosts from items (Razor Claw, Scope Lens)
- Critical hit boosts from abilities (Super Luck, Sniper's crit rate boost)

#### What It Doesn't Block
- Status effects and conditions
- Entry hazards damage (though reduces it by 20%)
- Recoil damage to the opponent
- Fixed damage moves (still reduced by 20%)

#### Ability Interactions
- **Mold Breaker**: Can bypass Crust Coat's effects
- **Turboblaze/Teravolt**: Can ignore the ability entirely
- **Sniper**: No interaction since critical hits are blocked
- **Super Luck**: Rendered ineffective against Crust Coat users

### Strategic Implications

#### Defensive Applications
- **Tank Builds**: Excellent for bulky Pokemon focused on stalling and support
- **Critical Hit Meta Counter**: Directly counters teams relying on critical hit strategies
- **Consistent Damage Calculation**: Eliminates critical hit variance for reliable HP calculations
- **Entry Hazard Resistance**: Reduces Stealth Rock and spike damage by 20%

#### Competitive Usage
- **Tier Placement**: High-value defensive ability in competitive formats
- **Team Synergy**: Pairs well with recovery moves and defensive team cores
- **Anti-Sweep Protection**: Makes it harder for setup sweepers to break through

### Common Users
Based on the codebase analysis, Crust Coat appears as an innate ability on certain Pokemon, suggesting it's used on defensive-oriented species that benefit from both critical hit immunity and damage reduction.

### Counters and Limitations

#### Direct Counters
- **Mold Breaker variants**: Excadrill, Haxorus with Mold Breaker
- **Turboblaze/Teravolt**: Zekrom, Reshiram, and their variants
- **Multi-hit moves**: While each hit is reduced, multiple hits can accumulate
- **Status conditions**: Crust Coat doesn't prevent burns, poison, or other status ailments

#### Strategic Limitations
- **Doesn't prevent OHKO moves**: Still vulnerable to moves like Fissure (though damage reduced)
- **No offensive presence**: Purely defensive, doesn't boost offensive capabilities
- **Breakable**: Can be removed by abilities like Mold Breaker

### Synergies

#### Ability Combinations (for innate slots)
- **Natural Recovery**: Pairs excellently for sustained tanking
- **Well-Baked Body**: Additional defensive typing benefits
- **Regenerator**: Enhanced longevity through passive healing

#### Move Synergies
- **Recovery Moves**: Rest, Recover, Roost for sustained presence
- **Status Moves**: Will-O-Wisp, Toxic for additional defensive pressure  
- **Defensive Sets**: Protect, Substitute for additional stalling potential

### Version History
- **Implementation**: Part of Elite Redux's extensive ability roster
- **Design Intent**: Combines Battle Armor's critical immunity with consistent damage reduction
- **Balance**: Breakable nature prevents it from being overpowered while maintaining strong defensive utility

### Competitive Analysis
Crust Coat represents one of the stronger defensive abilities in Elite Redux, providing reliable damage mitigation that's particularly valuable in formats where critical hits can determine match outcomes. Its combination of effects makes it especially valuable for defensive team cores and as a counter to offensive strategies that rely on critical hit fishing or high-damage output.

The 20% damage reduction is mathematically equivalent to having approximately 25% more effective HP against all attacks, making it a substantial defensive boost that scales with the user's existing bulk stats.
---
id: 592
name: Minion Control
status: reviewed
character_count: 271
---

# Minion Control - Ability ID 592

## In-Game Description
"Multi-hit attacks scale with healthy party members."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Moves hit an additional time for every healthy party member (max 6 hits). Members that are knocked out or have a status effect will not be counted. The first hit deals full damage while each additional hit deals 10% damage. Each hit rolls secondary effects independently.

## Detailed Mechanical Explanation

Minion Control is a unique multi-hit ability that scales with the health of your party. It transforms single-target moves into multi-hit attacks, with the number of hits determined by how many healthy party members you have. This creates an interesting dynamic where maintaining a healthy team directly translates to increased offensive power.

### Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Type**: Uses modified Parental Bond mechanics

### Core Mechanics
```cpp
constexpr Ability MinionControl = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { 
        return PARENTAL_BOND_MINION_CONTROL; 
    },
};
```

### Hit Calculation
- **Base**: 1 hit (the original move)
- **Additional Hits**: +1 for each healthy party member
- **Maximum**: 6 hits (with 5 healthy party members)
- **Damage Per Hit**: 
  - First hit: 100% damage
  - Additional hits: 10% damage each

### Health Requirements
A party member is considered "healthy" if:
- HP > 0 (not fainted)
- Not afflicted by any status condition
- Not an egg

### Damage Breakdown

### Hit Distribution
- **1 Healthy Party Member**: 2 hits (100% + 10% = 110% total)
- **2 Healthy Party Members**: 3 hits (100% + 10% + 10% = 120% total)
- **3 Healthy Party Members**: 4 hits (100% + 10% + 10% + 10% = 130% total)
- **4 Healthy Party Members**: 5 hits (100% + 10% + 10% + 10% + 10% = 140% total)
- **5 Healthy Party Members**: 6 hits (100% + 10% + 10% + 10% + 10% + 10% = 150% total)

### Effective Damage Multiplier
- Minimum: 1.1x (with only the user healthy)
- Maximum: 1.5x (with full healthy party)

### Strategic Applications

### Team Preservation Focus
- Rewards keeping party members healthy
- Encourages defensive team building
- Makes status healing more valuable
- Creates tension between switching and preserving health

### Early Game Advantage
- Strongest at battle start with full healthy team
- Provides immediate offensive pressure
- Discourages early sacrificial plays
- Rewards good team preservation

### Multi-Hit Synergies
- Each hit can trigger secondary effects
- Breaks through Focus Sash/Sturdy multiple times
- Builds up damage through Fury Cutter-like moves
- Effective against Substitute users

### Synergies and Interactions

### Ability Synergies
- **Skill Link**: Would guarantee maximum hits if it worked with Minion Control
- **Technician**: Low-power moves benefit from multiple hits
- **Sheer Force**: Each hit benefits from the power boost

### Move Synergies
- **King's Rock/Razor Fang**: Multiple flinch chances
- **Contact Moves**: Multiple chances to trigger contact effects
- **High Critical Hit Moves**: Multiple chances for critical hits
- **Status-Inducing Moves**: Multiple chances to inflict status

### Item Synergies
- **Life Orb**: Damage boost applies to all hits
- **Choice Items**: Locked move becomes multi-hit
- **Rocky Helmet Counter**: Opponents take multiple instances of damage

### Competitive Analysis

### Tier: Medium-High
Minion Control sits between Medium and High tier due to its unique scaling mechanic and team-dependent nature.

### Strengths
1. **Scaling Power**: Up to 50% damage increase with healthy team
2. **Multi-Hit Benefits**: Breaks sashes, substitutes, and sturdy
3. **No Setup Required**: Immediate power from turn one
4. **Team Synergy**: Rewards good team preservation

### Weaknesses
1. **Degrading Power**: Weakens as party members faint
2. **Status Vulnerability**: Any status removes a party member from count
3. **Predictable**: Opponents know your power level based on team health
4. **Team Building Constraint**: Requires focus on team preservation

### Usage Strategies

### Lead Strategy
- Start with maximum power
- Apply early pressure
- Force unfavorable trades
- Establish momentum

### Preservation Focus
- Prioritize keeping party healthy
- Use healing items strategically
- Avoid unnecessary switches into damage
- Clear status conditions quickly

### Endgame Considerations
- Power diminishes in longer battles
- May need alternative win conditions
- Consider preserving key party members
- Plan for reduced effectiveness

### Counter Strategies

### Status Spreading
- Toxic Spikes reduce healthy member count
- Will-O-Wisp/Thunder Wave key members
- Poison/Burn chip damage
- Status moves become high priority

### Priority Targeting
- Focus on reducing party members
- Use entry hazards for chip damage
- Pursuit trap key members
- Force difficult switches

### Defensive Play
- Stall out to reduce party health
- Use passive damage (weather, status)
- Protect/Detect to scout hits
- Resist-based switching

### Conclusion

Minion Control introduces a unique risk-reward dynamic to Elite Redux, where team preservation directly translates to offensive power. Unlike traditional multi-hit abilities, it creates strategic depth by linking battle performance to overall team health. This encourages players to think beyond individual Pokemon matchups and consider the battle as a whole.

The ability excels in the early game when teams are fresh but requires careful play to maintain effectiveness. Its scaling nature makes it neither overpowered nor underwhelming, instead creating interesting decisions about when to preserve team members versus making sacrificial plays. This design philosophy makes Minion Control a fascinating addition to the competitive landscape.
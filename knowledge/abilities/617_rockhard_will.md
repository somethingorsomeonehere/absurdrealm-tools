---
id: 617
name: Rockhard Will
status: reviewed
character_count: 73
---

# Rockhard Will - Ability ID 617

## In-Game Description
"Rock-type moves get 1.2x damage boost, 1.5x when HP is below 1/3."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Rock-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation

**Type:** Offensive Multiplier  
**Implementation:** SWARM_MULTIPLIER(TYPE_ROCK)

### Core Mechanics

Rockhard Will enhances Rock-type moves with a damage multiplier that varies based on the user's current HP:

- **Above 1/3 HP:** 1.2x damage multiplier for Rock-type moves
- **At or below 1/3 HP:** 1.5x damage multiplier for Rock-type moves

### Technical Implementation

```cpp
constexpr Ability RockhardWill = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_ROCK),
};
```

The ability uses the same SWARM_MULTIPLIER macro pattern as classic starter abilities like Overgrow, Blaze, Torrent, and Swarm, but applies to Rock-type moves instead.

### Strategic Applications

### Early Game Benefits
- Provides consistent 1.2x boost to Rock-type moves from full health
- Superior to many other damage-boosting abilities that require specific conditions

### Late Game Power Spike
- 1.5x multiplier activates when HP drops to 33% or below
- Creates dangerous comeback potential when combined with powerful Rock-type moves
- Synergizes well with strategies that intentionally reduce HP (Life Orb, Substitute, etc.)

### Move Synergies
Rock-type moves that benefit most from Rockhard Will:
- **Stone Edge:** High critical hit ratio + boosted damage
- **Rock Slide:** Spread damage with flinch chance
- **Head Smash:** Massive base power with recoil (helps trigger low HP threshold)
- **Stealth Rock:** Entry hazard with increased chip damage
- **Power Gem:** Special Rock move for mixed attackers

### Competitive Viability

### Strengths
- Unconditional damage boost at high HP unlike situational abilities
- Significant power spike when low on health creates unpredictable threat levels
- Works with both physical and special Rock-type moves
- No drawbacks or negative side effects

### Weaknesses
- Limited to Rock-type moves only
- Maximum benefit requires taking substantial damage
- Less impactful on Pokemon with poor Rock-type move pools
- Predictable activation threshold can be played around


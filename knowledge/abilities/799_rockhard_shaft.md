---
id: 799
name: Rockhard Shaft
status: reviewed
character_count: 73
---

# Rockhard Shaft - Ability ID 799

## In-Game Description
"Boosts Rock-type moves by 1.3x, or 1.8x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Rock-type moves by 30%, or by 80% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rockhard Shaft is a type-boosting ability that provides conditional damage multipliers specifically for Rock-type moves. It functions similarly to abilities like Swarm, Blaze, and Torrent, but for Rock-type moves.

### Activation Conditions
- **Normal State**: Pokemon has more than 1/3 of its maximum HP remaining
- **Boosted State**: Pokemon has 1/3 or less of its maximum HP remaining

### Numerical Values
- **Normal Boost**: 1.3x damage multiplier (30% increase)
- **Pinch Boost**: 1.8x damage multiplier (80% increase)

### Technical Implementation
The ability is implemented using the `BOOSTED_SWARM_MULTIPLIER(TYPE_ROCK)` macro in `src/abilities.cc`:

```cpp
constexpr Ability RockhardShaft = {
    .onOffensiveMultiplier = BOOSTED_SWARM_MULTIPLIER(TYPE_ROCK),
};

#define BOOSTED_SWARM_MULTIPLIER(type)                                       \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.8);                                                    \
            else                                                             \
                MUL(1.3);                                                    \
        }                                                                    \
    }
```

### Affected Moves
All Rock-type moves benefit from this ability, including but not limited to:
- Stone Edge
- Rock Slide
- Stealth Rock
- Head Smash
- Power Gem
- Ancient Power
- Rock Blast
- Accelerock
- Diamond Storm
- Stone Axe

### Interactions with Other Mechanics
- **STAB**: Stacks multiplicatively with Same Type Attack Bonus (1.5x)
- **Type Effectiveness**: Stacks multiplicatively with super effective damage (2x)
- **Critical Hits**: Stacks multiplicatively with critical hit damage (1.5x or 2.25x)
- **Weather**: No direct interaction with weather effects
- **Choice Items**: Stacks multiplicatively with Choice Band/Specs boosts
- **Life Orb**: Stacks multiplicatively with Life Orb's 1.3x boost

### Strategic Implications
- **Early Game**: Provides consistent 30% damage boost to Rock moves
- **Late Game**: Becomes a powerful 80% boost when at low HP
- **Risk vs Reward**: Players must balance staying at low HP for maximum damage
- **Synergy with Sturdy**: Works well with Sturdy to guarantee survival at 1 HP for maximum boost

### Example Damage Calculations
**Stone Edge (Base Power 100) vs neutral target:**
- Normal HP: 100 x 1.3 = 130 effective base power
- Below 1/3 HP: 100 x 1.8 = 180 effective base power

**With STAB (Rock-type user):**
- Normal HP: 100 x 1.5 x 1.3 = 195 effective base power
- Below 1/3 HP: 100 x 1.5 x 1.8 = 270 effective base power

### Common Users
- **Ogerpon Cornerstone Mega**: The primary user as an innate ability
  - Type: Grass/Rock
  - Stats: 80/120/156/80/96/118
  - Strategy: Uses defensive bulk to reach low HP safely, then unleashes powerful Rock moves

### Competitive Usage Notes
- **Tier Placement**: Highly situational but potentially game-changing
- **Team Synergy**: Pairs well with entry hazard setters for chip damage
- **Prediction**: Opponents may try to finish off low-HP users before they can abuse the boost
- **Setup Opportunity**: Can be used to bluff weakness while setting up for a powerful revenge kill

### Counters
- **Priority Moves**: Can finish off low-HP users before they attack
- **Multi-hit Moves**: Can break through Sturdy + Rockhard Shaft combos
- **Status Moves**: Toxic or burn can prevent the user from staying at low HP safely
- **Healing Moves**: Recovery moves can inadvertently weaken the ability's effectiveness

### Synergies
- **Sturdy**: Guarantees survival at 1 HP for maximum boost
- **Focus Sash**: Similar to Sturdy for guaranteed survival
- **Endure**: Can be used to safely reach 1 HP
- **Belly Drum**: Reduces HP to 50% while boosting Attack, potentially triggering the enhanced boost
- **Substitute**: Can help preserve HP while setting up opportunities

### Version History
- **Elite Redux**: Introduced as a signature ability for Ogerpon Cornerstone Mega
- **Design Philosophy**: Meant to reward aggressive play while providing comeback potential
- **Balance Considerations**: The 1.3x base boost prevents it from being completely useless at full HP

### Trivia
- The ability name "Rockhard Shaft" appears to be a play on mining/geology terminology
- The display name "We Will Rock You" is a reference to the famous Queen song
- This ability represents the "berserker" archetype in Pokemon, becoming more dangerous when wounded
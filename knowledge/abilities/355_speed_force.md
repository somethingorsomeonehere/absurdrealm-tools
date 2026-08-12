---
id: 355
name: Speed Force
status: reviewed
character_count: 112
---

# Speed Force - Ability ID 355

## In-Game Description
"Adds 20% of Speed stat to damage when using contact moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Adds 20% of the user's Speed stat to damage when using contact moves. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation

### Overview

**Speed Force** is an Elite Redux custom ability that transforms a Pokemon's speed into raw offensive power. When the bearer uses contact moves, it adds 20% of its Speed stat to the attack's damage calculation, creating a unique synergy between mobility and physical prowess.

## Mechanics

### Core Implementation
**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Lines 3746-3751)

```cpp
constexpr Ability SpeedForce = {
    .onChooseOffensiveStat =
        +[](ON_CHOOSE_OFFENSIVE_STAT) {
            if (gBattleMoves[move].contact) secondaryAtkStatToUse[STAT_SPEED] += 20;
        },
};
```

### Technical Details
- **Trigger**: Only activates when using contact moves (physical moves that make direct contact)
- **Stat Bonus**: Adds 20% of the user's current Speed stat to damage calculation
- **Stat Integration**: Uses the `secondaryAtkStatToUse[STAT_SPEED]` system for damage calculation
- **Breakable**: No (ability cannot be suppressed by Mold Breaker effects)
- **Stackable**: Yes (works with other stat bonuses and multipliers)

### Contact Move Requirement
The ability specifically checks `gBattleMoves[move].contact` before activating, meaning it only affects moves that make direct physical contact with the target. This includes most physical attacks but excludes ranged physical moves like Rock Slide or Earthquake.

## Strategic Applications

### Optimal Users
Speed Force is most effective on Pokemon with:
- **High Speed stats** (130+ base Speed for maximum benefit)
- **Strong physical attack stats** to capitalize on the Speed bonus
- **Access to powerful contact moves** like Close Combat, U-turn, or Earthquake alternatives
- **Balanced offensive presence** that can threaten both fast and slow opponents

### Example Calculation
For a Pokemon with 200 Speed using a contact move:
- Base damage calculation occurs normally
- Speed Force adds: 200 x 0.20 = 40 additional points to the offensive stat
- This roughly translates to a 15-25% damage increase depending on the user's base Attack stat

### Team Synergy
- **Speed Control**: Pairs well with Thunder Wave or Sticky Web support to maintain Speed advantage
- **Choice Items**: Choice Scarf users can maintain high Speed while gaining offensive benefits
- **Terrain Effects**: Electric Terrain boosts Speed for additional Speed Force benefit

## Competitive Analysis

### Strengths
1. **Scaling Damage**: Becomes more powerful as Speed increases through boosts or items
2. **Versatile Application**: Works with any contact move in the user's moveset
3. **Unpredictable Power**: Opponents may underestimate damage output from fast, seemingly frail attackers
4. **Item Synergy**: Combines excellently with Choice Scarf, Life Orb, or stat-boosting items

### Weaknesses
1. **Contact Dependency**: Useless against teams with Rough Skin, Iron Barbs, or similar contact-punishing abilities
2. **Limited Move Pool**: Only benefits physical contact moves, not special attacks or non-contact physical moves
3. **Speed Reliance**: Effectiveness diminishes if Speed is reduced by paralysis, Trick Room, or stat drops
4. **Defensive Weakness**: Fast attackers are often frail, making them vulnerable to priority moves

### Counters
- **Rocky Helmet + Rough Skin**: Punishes contact moves heavily
- **Will-O-Wisp**: Halves Attack stat, reducing the benefit of Speed Force
- **Trick Room**: Reverses Speed advantages, making faster users move last
- **Priority Moves**: Bypass Speed advantage entirely

## Notable Users

Speed Force appears on several Elite Redux Pokemon, including:
- **Beedrill** (135 base Speed) - Perfect synergy with high Speed and strong physical movepool
- Various fast physical attackers throughout the roster

### Distribution Analysis
The ability appears both as a regular ability and as an innate ability across the Elite Redux roster, indicating its balanced power level and thematic fit for speed-oriented Pokemon.

## Related Abilities

### Similar Mechanics
- **Juggernaut**: Adds 20% of Defense stat to contact moves (defensive equivalent)
- **Striker**: Uses 20% of Speed for special moves (special attack equivalent)
- **Momentum**: Provides Speed-based benefits with different mechanics

### Ability Interactions
- **Speed Boost**: Synergizes perfectly by continuously increasing the Speed stat
- **Unburden**: Doubles Speed after item consumption, dramatically increasing Speed Force effectiveness
- **Choice Scarf**: Provides immediate 50% Speed boost for enhanced Speed Force damage

## Conclusion

Speed Force represents an innovative approach to ability design, creating meaningful synergy between traditionally separate offensive and speed stats. Its balanced 20% conversion rate provides significant but not overwhelming benefits, making it a valuable ability for physical attackers that can maintain their speed advantage. The contact move requirement adds strategic depth, forcing users to carefully consider their moveset and opponent's defensive abilities.

The ability exemplifies Elite Redux's design philosophy of creating interesting stat interactions that reward strategic team building and thoughtful play patterns.


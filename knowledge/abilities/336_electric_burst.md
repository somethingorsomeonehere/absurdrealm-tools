---
id: 336
name: Electric Burst
status: reviewed
character_count: 169
---

# Electric Burst - Ability ID 336

## In-Game Description
"Boosts Electric-type moves by 35% but causes 10% recoil damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Electric Burst boosts Electric-type moves by 35% but causes 10% recoil damage based on damage dealt (minimum 1 HP). The recoil damage will be able to knock out the user.

## Detailed Mechanical Explanation

### Overview

Electric Burst is a high-risk, high-reward ability that significantly enhances Electric-type offensive capabilities at the cost of self-inflicted damage. This ability embodies the volatile nature of electricity, providing substantial power at the expense of safety.

### Mechanics

### Power Boost
- **Multiplier**: 1.35x damage for all Electric-type moves
- **Activation**: Triggers on any Electric-type move used by the ability holder
- **Stack Compatibility**: Multiplicative with other damage modifiers

### Recoil Calculation
- **Recoil Amount**: 10% of damage dealt (minimum 1 HP)
- **Calculation**: `max(damage / 20, 1)` HP lost
- **Timing**: Applied after damage calculation and delivery

## Code Implementation

**Location**: `src/abilities.cc` lines 3551-3561

```cpp
constexpr Ability ElectricBurst = {
    .onRecoil = +[](ON_RECOIL) -> int {
        CHECK(moveType == TYPE_ELECTRIC);
        gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_RECOIL_NORMAL;
        return max(damage / 20, 1);
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_ELECTRIC) MUL(1.35);
        },
};
```

**Ability Registration**: Line 9181 in ability lookup table

## Strategic Applications

### Offensive Strategies
- **Glass Cannon Builds**: Maximize damage output before fainting
- **Choice Item Synergy**: Lock into powerful Electric moves for consistent damage
- **Life Orb Considerations**: Stacks with Life Orb for extreme power but increased recoil
- **Priority Moves**: Electric-type priority moves benefit from the boost with minimal recoil exposure

### Defensive Considerations
- **HP Management**: Careful HP monitoring required to avoid KO from recoil
- **Recovery Moves**: Non-Electric recovery moves essential for longevity
- **Substitute Strategies**: Substitute can block recoil damage in certain scenarios

### Movepool Synergy
- **Thunderbolt/Thunder**: High base power moves benefit most from the multiplier
- **Volt Tackle**: Already has recoil, making the additional 10% manageable
- **Thunder Wave**: Status moves don't trigger recoil (no damage dealt)
- **Discharge**: Moderate power spread move with manageable recoil

## Competitive Analysis

### Strengths
- **Massive Damage Output**: 35% boost makes Electric attacks extremely threatening
- **Versatile Application**: Works with all Electric-type moves
- **Intimidation Factor**: Forces opponents to respect Electric-type threats
- **STAB Interaction**: Combines with STAB for 2.025x total multiplier

### Weaknesses
- **Self-Damage**: Continuous use leads to self-KO
- **Predictable Pattern**: Opponents can exploit the recoil mechanic
- **Limited Sustainability**: Requires support or careful play to maintain effectiveness
- **Ground-type Immunity**: Electric moves have no effect on Ground-types

### Tier Assessment: B+
- **Pros**: Exceptional damage potential, consistent activation
- **Cons**: Sustainability issues, risk of self-KO
- **Niche**: Best on fast, frail attackers or as a finishing move specialist

## Pokemon with Electric Burst

Based on SpeciesList.textproto analysis, 21 Pokemon have access to Electric Burst:

### Confirmed Species
- **Jolteon** - Natural fit with high Special Attack and Speed
- **Pikachu/Raichu** - Iconic Electric-types with diverse movepools
- **Pichu** - Glass cannon potential despite low stats
- **Manectric** - Fast special attacker with good Electric movepool
- **Shinx/Luxio/Luxray** - Physical Electric attackers with mixed potential
- **Morpeko** - Unique dual-type with situational use
- **Regieleki** - Legendary with extreme Speed and Electric specialization

### Regional Variants
- Multiple Pikachu regional forms (Kanto, Hoenn, Sinnoh, Unova, Kalos, Alola, World)
- Pichu Spiky-eared variant

## Related Abilities

### Similar Risk/Reward Abilities
- **Reckless**: Boosts recoil moves but affects all types
- **Solar Power**: Trades HP for Special Attack in sun
- **Life Orb**: Item equivalent with universal type coverage

### Electric-type Synergies
- **Motor Drive**: Immunity to Electric moves (defensive counterpart)
- **Lightning Rod**: Redirects Electric moves to boost Special Attack
- **Volt Absorb**: Heals from Electric moves instead of taking damage

## Interactions and Edge Cases

### Battle Weather
- **Rain**: Doesn't affect Electric moves directly
- **Sun**: No interaction with Electric-type moves
- **Sand/Hail**: Additional residual damage stacks with recoil

### Item Interactions
- **Leftovers**: Partial recoil recovery each turn
- **Choice Items**: Lock-in effect works well with consistent power boost
- **Focus Sash**: Prevents recoil KO from full HP
- **Rock Head**: Does NOT prevent this recoil (ability-based, not move-based)

### Move Interactions
- **Protect/Detect**: Prevents recoil when move is blocked
- **Thunder Wave**: No recoil (status move, no damage)
- **Charge**: Doesn't boost the ability's multiplier further

## Conclusion

Electric Burst exemplifies the high-risk, high-reward philosophy of Elite Redux's ability design. While the 35% damage increase is substantial, the 10% recoil creates meaningful decision-making moments and prevents the ability from being overpowered. Success with Electric Burst requires careful HP management, strategic move selection, and often short-term thinking rather than long-term sustainability.

The ability is best suited for fast, frail attackers that can maximize damage before fainting, or as a late-game finishing tool when recoil damage is less of a concern. Its presence in the metagame forces respect for Electric-type attacks and creates interesting counterplay dynamics around Ground-type immunities and HP management strategies.


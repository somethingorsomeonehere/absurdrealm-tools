---
id: 432
name: Infernal Rage
status: reviewed
character_count: 212
---

# Infernal Rage - Ability ID 432

## In-Game Description
"Fire-type moves are boosted by 35% with 5% recoil."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Infernal Rage boosts Fire-type moves by 35% but inflicts 5% recoil damage after using them. Recoil is calculated from damage dealt with minimum of 1 HP lost. This recoil damage will be able to knock the user out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Infernal Rage is an offensive ability that significantly boosts Fire-type moves while imposing a recoil penalty. It provides a substantial 35% damage boost to all Fire-type attacks but causes the user to take recoil damage equal to 5% of the damage dealt.

### Activation Conditions
- **Move type requirement**: Only Fire-type moves trigger the ability
- **Damage boost**: All Fire moves receive a 1.35x multiplier
- **Recoil calculation**: 5% of damage dealt (minimum 1 HP)
- **Timing**: Boost applies during damage calculation, recoil occurs after attack

### Technical Implementation
```c
constexpr Ability InfernalRage = {
    .onRecoil = +[](ON_RECOIL) -> int {
        CHECK(moveType == TYPE_FIRE);
        gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_RECOIL_NORMAL;
        return max(damage / 20, 1);  // 5% recoil with minimum 1 HP
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE) MUL(1.35);  // 35% boost
        },
};
```

### Recoil Mechanics
- **Calculation**: Recoil = max(damage_dealt / 20, 1)
- **Minimum damage**: Always takes at least 1 HP recoil
- **Type restriction**: Only Fire moves cause recoil
- **Self-KO**: Can cause the user to faint from recoil damage
- **Rock Head interaction**: Rock Head prevents recoil from this ability

### Important Interactions
- **Multi-hit moves**: Each hit triggers separate recoil calculation
- **Critical hits**: Recoil based on actual damage dealt (including crit bonus)
- **Substitute**: User still takes recoil even when behind Substitute
- **Magic Guard**: Prevents recoil damage completely
- **Rock Head**: Negates all recoil from this ability
- **Reckless**: Does NOT boost recoil moves from this ability (only affects specific recoil moves)

### Move Compatibility
**Boosted Fire Moves:**
- All Fire-type attacks (Flamethrower, Fire Blast, Overheat, etc.)
- Physical Fire moves (Flare Blitz, Fire Punch, Sacred Fire)
- Multi-hit Fire moves (each hit gets boost and recoil)
- Special Fire moves with secondary effects

**Non-Boosted Moves:**
- Non-Fire type moves receive no boost or recoil
- Status moves that don't deal damage

### Strategic Implications
- **Glass cannon playstyle**: High reward but self-damaging
- **Life Orb synergy**: Stacks with Life Orb for massive damage output
- **Choice item compatibility**: Works with Choice Band/Specs for extreme damage
- **Sweeper potential**: Excellent for revenge killing and cleaning up
- **Risk vs reward**: Must balance damage output with survivability

### Damage Calculations
**Example scenarios:**
- Deal 200 damage to Take 10 recoil (200/20)
- Deal 50 damage to Take 3 recoil (50/20 rounded up)
- Deal 10 damage to Take 1 recoil (minimum)
- Deal 400 damage to Take 20 recoil (400/20)

### Common Users
- Fire-type attackers with high offensive stats
- Pokemon with access to powerful Fire moves
- Glass cannon sweepers
- Revenge killers needing extra damage
- Pokemon with Rock Head (negates recoil)

### Competitive Usage Notes
- **Life Orb alternative**: Provides similar damage boost without item slot
- **Choice item synergy**: Stacks multiplicatively with Choice items
- **Late-game cleaner**: Excellent for finishing weakened teams
- **STAB stacking**: Fire types get 1.5x STAB + 1.35x ability = 2.025x total
- **Recoil management**: Requires careful HP management

### Synergies
- **Rock Head**: Completely negates recoil drawback
- **Magic Guard**: Prevents recoil while keeping damage boost
- **Life Orb**: Stacks for 1.35 x 1.3 = 1.755x damage (with double recoil)
- **Choice items**: Multiplicative stacking for extreme damage
- **Sun teams**: Fire moves already boosted in harsh sunlight
- **Drought**: Pairs well with sun-boosted Fire moves

### Counters
- **Water/Rock/Dragon types**: Resist Fire moves
- **Flash Fire**: Immune to Fire moves entirely
- **Thick Fat**: Resists Fire moves
- **Intimidate**: Reduces physical Fire move damage
- **Burn**: Halves physical Fire move damage
- **Pressure**: Forces more recoil through PP usage

### Risk Management
- **HP thresholds**: Monitor HP to avoid recoil KO
- **Priority moves**: Vulnerable to revenge killing after recoil
- **Entry hazards**: Compound the self-damage problem
- **Status conditions**: Burn particularly problematic for physical attackers
- **Weather**: Rain reduces Fire move effectiveness

### Team Building Considerations
- **Rapid Spin/Defog support**: Clear hazards to reduce cumulative damage
- **Wish/Heal Bell support**: Provide recovery and status cure
- **Trick Room teams**: Slow, powerful attackers benefit most
- **Sun teams**: Natural synergy with Fire-type focus
- **Late-game cleaner**: Position as endgame sweeper

### Comparison to Similar Abilities
- **Reckless**: Boosts specific recoil moves by 20% (different move pool)
- **Sheer Force**: Removes secondary effects for 30% boost (no recoil)
- **Life Orb**: 30% boost with 10% recoil (item-based)
- **Tough Claws**: 30% boost to contact moves (no recoil)

### Version History
- Elite Redux custom ability
- Designed for high-risk, high-reward Fire-type gameplay
- Part of the expanded ability system for more strategic depth
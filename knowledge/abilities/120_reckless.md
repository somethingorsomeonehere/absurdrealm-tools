---
id: 120
name: Reckless
status: reviewed
character_count: 285
---

# Reckless - Ability ID 120

## In-Game Description
"Moves causing recoil damage deal 1.2x more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the damage of moves that cause recoil by 20%. While enraged, this boost applies to all moves. Also grants Mold Breaker effects to these moves, allowing them to ignore abilities and innates that block effects or reduce damage. Does not bypass abilities that modify base stats. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- **Damage Boost**: 1.2x multiplier (20% increase) applied to moves with recoil damage
- **Activation**: Only affects moves that have the `FLAG_RECKLESS_BOOST` flag
- **Recoil Unchanged**: The ability boosts the damage dealt but does not increase or decrease the recoil damage taken

**Technical Implementation:**
```cpp
constexpr Ability Reckless = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].flags & FLAG_RECKLESS_BOOST) MUL(1.2);
        },
};
```

**Affected Moves:**
Reckless affects all moves that cause recoil damage to the user, including but not limited to:
- **Double-Edge**: 33% recoil damage
- **Brave Bird**: 33% recoil damage
- **Flare Blitz**: 33% recoil damage, 10% burn chance
- **Wood Hammer**: 33% recoil damage
- **Volt Tackle**: 25% recoil damage, 10% paralyze chance
- **Dragon Rush**: 33% recoil damage, 20% flinch chance
- **Submission**: 33% recoil damage
- **Head Smash**: Rock-type recoil move
- **Wild Charge**: Electric-type recoil move
- **Take Down**: Normal-type recoil move

**Damage Calculation Example:**
- Base Brave Bird power: 120
- With Reckless: 120 x 1.2 = 144 effective power
- Recoil damage: Still 33% of damage dealt (not increased)

**Strategic Applications:**
1. **Offensive Powerhouse**: Turns already powerful recoil moves into devastating attacks
2. **Risk-Reward**: Balances increased damage output with life-risking recoil
3. **Synergies**: Works exceptionally well with:
   - Rock Head (negates recoil entirely)
   - Recovery moves or items (Roost, Leftovers)
   - High HP Pokemon that can handle recoil better

**Common Users:**
- Physical attackers with access to multiple recoil moves
- Pokemon that can learn both Reckless and recovery options
- Fast sweepers that aim to KO before recoil becomes problematic

**Competitive Notes:**
- The 20% damage boost makes recoil moves extremely threatening
- Requires careful HP management due to accumulated recoil damage
- Often paired with priority moves to secure KOs when at low HP
- Can break through bulky walls that would normally survive unboosted attacks

**Interaction Notes:**
- Does not stack with other damage-boosting abilities
- The boost applies before other damage modifiers in the calculation
- Works with all recoil moves regardless of type or category (physical/special)
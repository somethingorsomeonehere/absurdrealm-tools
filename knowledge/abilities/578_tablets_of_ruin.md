---
id: 578
name: Tablets Of Ruin
status: reviewed
character_count: 177
---

# Tablets Of Ruin - Ability ID 578

## In-Game Description
"Lowers the Attack of other Pokemon by 25%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces the Attack stat of every other Pokemon by 25% while the user is out. Multiples of the same Ruin ability do not stack together. Stacks multiplicatively with Attack drops. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Passive field effect that applies to all Pokemon except the user
- Reduces Attack stat of affected Pokemon by 25% (multiplies by 0.75)
- Activates immediately when the Pokemon with Tablets of Ruin enters battle
- Remains active as long as the user is on the field

**Activation Conditions:**
- Always active when the Pokemon is on the battlefield
- Does not require any specific action or turn to activate
- Applies to both opposing Pokemon and ally Pokemon in double battles

**Technical Implementation:**
```cpp
constexpr Ability TabletsOfRuin = {
    .onStat = +[](ON_STAT) { RuinEffect(STAT_ATK, battler, statId, stat, flags); },
    .onStatFor = APPLY_ON_OTHER,
    .ruinStat = STAT_ATK,
};

static void RuinEffect(int ruinStat, int battler, int statId, u32 *stat, NonStackingState *flags) {
    if (statId != ruinStat) return;
    if (*flags & NON_STACKING_RUIN) return;
    ON_ABILITY(battler, FALSE, gAbilities[ability].ruinStat == statId, return) *stat *= .75;
    *flags = static_cast<NonStackingState>(static_cast<int>(*flags) | static_cast<int>(NON_STACKING_RUIN));
}
```

**Numerical Values:**
- Attack reduction: Exactly 25% (0.75 multiplier)
- Applies to base Attack stat calculations during damage formulas
- Affects both physical moves and moves that use Attack for damage calculation

**Interactions with Other Abilities/Mechanics:**
- **Non-Stacking Rule**: Multiple Ruin abilities (Tablets of Ruin, Sword of Ruin, Vessel of Ruin, Beads of Ruin) do not stack their effects on the same stat
- **Ability Suppression**: Neutralized by abilities like Neutralizing Gas while active
- **Stat Modifications**: Applied before stat stage modifications (not affected by Attack boosts/drops)
- **Mold Breaker Effects**: Cannot be bypassed by Mold Breaker or similar abilities
- **Switch Effects**: Immediately applies when switched in, immediately stops when switched out

**Strategic Implications:**
- Primarily defensive utility, weakening opposing physical attackers
- Excellent for supporting physically frail teammates
- Creates immediate battlefield control upon entry
- Forces opponents to rely more on special attacks or status moves
- Particularly effective against physical setup sweepers

**Example Damage Calculations:**
```
Normal Attack calculation: Base Attack x Stage Multiplier x Other Modifiers
With Tablets of Ruin: (Base Attack x 0.75) x Stage Multiplier x Other Modifiers

Example: 
- Opposing Pokemon with 150 base Attack
- Without Tablets of Ruin: 150 Attack used in damage formula
- With Tablets of Ruin: 112.5 effective Attack used in damage formula
```

**Common Users:**
- **Wo-Chien** (National Dex #1001): Dark/Grass legendary Pokemon
- Primary signature ability of this Treasure of Ruin Pokemon
- Often paired with other innate abilities in Elite Redux's multi-ability system

**Competitive Usage Notes:**
- Best used on defensive or support-oriented Pokemon
- Synergizes well with teammates that can capitalize on weakened physical attackers
- Creates immediate value without requiring setup
- Particularly strong in formats with common physical threats
- Can shift team building toward special attackers

**Counters:**
- Special attackers are completely unaffected
- Abilities that boost Attack (like Huge Power) still apply after the reduction
- Pokemon with Neutralizing Gas can temporarily suppress the effect
- Priority moves and status moves bypass the Attack reduction entirely

**Synergies:**
- **Intimidate**: Stacks with Intimidate for even greater Attack reduction
- **Physical walls**: Enhances the survivability of defensive Pokemon
- **Special attackers**: Creates opportunities for special sweepers to shine
- **Status moves**: Encourages more strategic, non-damage focused gameplay

**Version History:**
- Introduced as part of the Treasures of Ruin mechanic from Generation 9
- Implemented in Elite Redux as part of the signature ability set for legendary Pokemon
- Functions identically to official Pokemon games with passive field effect mechanics
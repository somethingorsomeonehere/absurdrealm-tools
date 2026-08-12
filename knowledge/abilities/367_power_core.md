---
id: 367
name: Power Core
status: reviewed
character_count: 120
---

# Power Core - Ability ID 367

## In-Game Description
"The Pokemon uses +20% of its Defense or SpDef during moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Adds 20% of Defense stat to physical attacks and 20% of Special Defense stat to special attacks when calculating damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**POWER CORE** is a unique offensive ability that converts defensive stats into offensive power by adding a percentage of defensive stats to the attacker's offensive stats during damage calculation.

### Core Mechanics:
- **Physical Moves**: Adds 20% of the user's Defense stat to the Attack calculation
- **Special Moves**: Adds 20% of the user's Special Defense stat to the Special Attack calculation
- **Stat Selection**: Automatically determines which defensive stat to use based on move type (physical vs special)
- **Application**: The bonus is added to the `secondaryAtkStatToUse` array during stat calculation

### Technical Implementation:
```c
constexpr Ability PowerCore = {
    .onChooseOffensiveStat = +[](ON_CHOOSE_OFFENSIVE_STAT) { 
        secondaryAtkStatToUse[IS_MOVE_PHYSICAL(move) ? STAT_DEF : STAT_SPDEF] += 20; 
    },
};
```

**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 3822-3824)

### Calculation Breakdown:
1. **Move Type Check**: `IS_MOVE_PHYSICAL(move)` determines if the move is physical or special
2. **Stat Selection**: Physical moves use `STAT_DEF`, special moves use `STAT_SPDEF`
3. **Bonus Application**: Adds 20 points to the secondary attack stat array
4. **Final Calculation**: The game combines the user's base offensive stat with 20% of the corresponding defensive stat

### Related Abilities:
Power Core shares its implementation pattern with several other abilities:
- **Slipstream** (ID 356): Adds 20% of Speed to offensive calculations
- **Best Offense** (ID 421): Adds 20% of Special Defense to offensive calculations
- **Magus Blades** (ID 423): Adds 20% of Special Defense to offensive calculations

### Strategic Implications:
1. **Bulk + Power Synergy**: Rewards investment in defensive stats with offensive returns
2. **Stat Distribution**: Encourages mixed defensive/offensive builds rather than pure glass cannon
3. **Defensive Walls**: Transforms defensive Pokemon into surprisingly potent threats
4. **Item Synergy**: Defensive items like Leftovers or Assault Vest provide indirect offensive benefits

### Example Damage Scenarios:
**Scenario 1**: A Pokemon with 100 Attack and 150 Defense using a physical move
- **Normal**: Uses 100 Attack for damage calculation
- **With Power Core**: Uses 100 Attack + (150 x 0.20) = 130 effective Attack

**Scenario 2**: Same Pokemon using a special move with 80 Special Attack and 120 Special Defense
- **Normal**: Uses 80 Special Attack for damage calculation
- **With Power Core**: Uses 80 Special Attack + (120 x 0.20) = 104 effective Special Attack

### Pokemon Distribution:
Power Core appears on numerous powerful Pokemon in Elite Redux:

**Legendary/Mythical Users (Innate):**
- **Dialga** (both forms) - Primal Armor/Impenetrable/Power Core
- **Palkia** (both forms) - Prism Scales or Sea Guardian/Overwhelm or Sea Guardian/Power Core
- **Arceus** (all forms) - Multitype/Pressure/Power Core and Levitate
- **Zygarde** (all forms) - Power Construct/Primal Armor/Earthbound/Power Core
- **Necrozma forms** - Vengeance or Power Fists/various/Power Core
- **Magearna** (both forms) - Clear Body/Mirror Armor/Soul Heart/Power Core

**Defensive Specialists:**
- **Shuckle line** - Simple/Power Core/Loose Rocks with Shell Armor/Natural Cure/Impenetrable
- **Tyranitar** - Sand Stream/Juggernaut/Battle Armor/Power Core
- **Registeel variants** - Fortitude/various/Power Core/Impenetrable/Self Sufficient

**Mixed Attackers:**
- **Machamp Redux** - Dragonslayer/Brawling Wyvern/Stamina/Power Core
- **Melmetal** - Clear Body/Mirror Armor/Soul Heart/Power Core
- **Various Rock/Steel types** - Often paired with Impenetrable and other defensive abilities

### Competitive Analysis:
**Strengths:**
- Rewards defensive investment with offensive returns
- Works with all offensive moves, no restrictions
- Scales with stat boosts and defensive items
- Excellent on bulky offensive Pokemon

**Weaknesses:**
- Requires significant defensive stats to be impactful
- No benefit to status moves or non-damaging moves
- Competes with other offensive abilities for value
- Diminishing returns on glass cannon builds

**Ideal Users:**
- Bulky attackers with balanced offensive/defensive stats
- Pokemon with naturally high defensive stats
- Mixed attackers that can leverage both bonuses
- Defensive Pokemon that want some offensive presence

### Competitive Tier Justification:
**Medium Tier** - Power Core provides meaningful but not overwhelming offensive benefits. It's most effective on Pokemon that already invest in defensive stats, making it a solid choice for bulky offensive builds but not game-changing enough for top tier.

**Comparison to Similar Abilities:**
- **Huge Power/Pure Power**: Direct 2x multiplier vs situational 20% boost
- **Adaptability**: Guaranteed 2x STAB vs conditional 20% boost
- **Life Orb effect**: 30% boost with recoil vs 20% boost with no downside

### Team Building Considerations:
1. **Stat Investment**: Prioritize defensive stats alongside offensive ones
2. **Item Choices**: Defensive items provide indirect offensive benefits
3. **Role Compression**: Allows defensive Pokemon to threaten offensively
4. **Movepool**: Benefits from diverse offensive movepools to utilize both bonuses

### Counters and Answers:
- **Stat Reduction**: Abilities like Intimidate reduce the base stat before Power Core applies
- **Defensive Answers**: Power Core doesn't overcome type disadvantages or resistances
- **Status Moves**: Burns, paralysis, and other status conditions still affect performance
- **Mold Breaker effects**: Cannot be bypassed as this is a stat calculation ability

### Version History:
- **Elite Redux**: Original implementation as ability #367
- **Design Intent**: Create synergy between defensive and offensive investment
- **Balance Philosophy**: Reward defensive building without making defensive Pokemon overpowered

### Usage Tips:
1. **Maximize defensive stats** through EVs, nature, and items
2. **Use mixed movesets** to leverage both Defense and Special Defense bonuses
3. **Pair with defensive items** for sustained offensive pressure
4. **Consider entry hazard support** to maximize offensive opportunities
5. **Use on Pokemon with naturally high defensive stats** for maximum impact

### Notable Interactions:
- **Assault Vest**: Boosts Special Defense, indirectly boosting special moves
- **Eviolite**: Provides massive defensive boosts, greatly enhancing Power Core's effectiveness
- **Defensive natures**: Become offensive investments with Power Core
- **Stat-boosting moves**: Defensive boosts (Iron Defense, Cosmic Power) increase offensive power
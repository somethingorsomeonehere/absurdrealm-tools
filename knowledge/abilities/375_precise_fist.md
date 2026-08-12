---
id: 375
name: Precise Fist
status: reviewed
character_count: 86
---

# Precise Fist - Ability ID 375

## In-Game Description
"Punching moves get +1 crit and 5x effect chance."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Punching moves gain +1 critical hit stage and 5x their normal secondary effect chance. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**PRECISE FIST** is a specialized enhancement ability that transforms punching moves into highly reliable, devastating attacks with both guaranteed critical hits and amplified secondary effects.

### Activation Mechanics:
- **Critical Hit Trigger**: onCrit callback (line 3896-3899)
- **Effect Amplification**: onModifyEffectChance callback (line 3900-3903)
- **Condition**: Move must have FLAG_IRON_FIST_BOOST flag (same as Iron Fist)
- **Type**: Universal - works with all move types that have punching flag

### Core Effects:
1. **Guaranteed Critical Hits**: All punching moves automatically score critical hits
2. **5x Secondary Effect Chance**: Status effect chances are multiplied by 5 (e.g., 10% becomes 50%)

### Affected Moves:
Precise Fist affects all moves with the FLAG_IRON_FIST_BOOST flag, including:

1. **Elemental Punches**: Fire Punch (10% burn to 50%), Ice Punch (10% freeze to 50%), Thunder Punch (10% paralysis to 50%)
2. **Fighting Punches**: Dynamic Punch (100% confusion - already guaranteed), Drain Punch, Focus Punch
3. **Priority Punches**: Bullet Punch, Mach Punch
4. **Other Punching Moves**: Comet Punch, Mega Punch, Dizzy Punch (20% confusion to 100%), Shadow Punch
5. **Special Cases**: Hammer Arm, Meteor Mash, Sky Uppercut, Power-Up Punch

### Technical Implementation:
```cpp
constexpr Ability PreciseFist = {
    .onCrit = +[](ON_CRIT) -> int {
        CHECK(IsIronFistBoosted(battler, move))
        return 1;  // Guaranteed critical hit
    },
    .onModifyEffectChance =
        +[](ON_MODIFY_EFFECT_CHANCE) {
            if (IsIronFistBoosted(battler, move)) *effectChance *= 5;
        },
};
```

### Secondary Effect Examples:
- **Fire Punch**: 10% burn chance to 50% burn chance + guaranteed crit
- **Ice Punch**: 10% freeze chance to 50% freeze chance + guaranteed crit  
- **Thunder Punch**: 10% paralysis to 50% paralysis + guaranteed crit
- **Dizzy Punch**: 20% confusion to 100% confusion + guaranteed crit
- **Meteor Mash**: 20% Attack boost to 100% Attack boost + guaranteed crit

### Critical Hit Calculation:
The guaranteed critical hit multiplies damage by:
- **Physical moves**: 1.5x base damage (2.25x in Gen 6+)
- **Stacks with**: Sniper (3x crit damage), critical hit items
- **Base Example**: 100 BP Fire Punch to 150 BP with crit to 225 BP with Sniper

### Strategic Applications:
1. **Status Spreader**: Elemental punches become highly reliable status moves
2. **Sweeping Power**: Guaranteed crits break through defensive investment
3. **Setup Synergy**: Meteor Mash becomes 100% reliable Attack boost
4. **Priority Pressure**: Bullet Punch becomes a guaranteed crit priority move

### Pokemon Distribution:
Found on various fighting specialists and versatile attackers:
- **Regular Ability**: Crabominable, Pangoro, and other fighting types
- **Innate Ability**: Appears alongside Fatal Precision, Raging Boxer on specialized Pokemon
- **Compound Users**: Often paired with Iron Fist, Power Fists, or other punch-enhancing abilities

### Synergistic Abilities:
- **Iron Fist**: Stacks multiplicatively (1.3x damage + guaranteed crit)
- **Power Fists**: Combined punch boost + Special Defense targeting + guaranteed crit
- **Raging Boxer**: Hits twice with guaranteed crits on both hits
- **Fatal Precision**: Super-effective moves get both abilities' benefits
- **Sniper**: Multiplies critical hit damage to 3x instead of 1.5x

### Synergistic Items:
- **Punching Glove**: Additional 1.1x boost + contact protection
- **Scope Lens/Razor Claw**: Redundant crit boost, but useful on non-punching moves
- **Life Orb**: 1.3x damage boost stacks with guaranteed crits
- **Choice Band**: Massive Attack boost with guaranteed crit punches

### Competitive Applications:
1. **Mixed Attacker**: Elemental punches provide special coverage with status reliability
2. **Priority Sweeper**: Bullet Punch becomes a guaranteed crit revenge tool
3. **Status Control**: 50% status chances make punches excellent utility moves
4. **Wall Breaking**: Guaranteed crits help break through defensive Pokemon
5. **Setup Integration**: Meteor Mash becomes 100% reliable for Attack boosts

### Advanced Interactions:
1. **Multi-hit Moves**: Each hit of Comet Punch crits independently
2. **Weather Synergy**: Fire Punch in sun + guaranteed crit + 50% burn
3. **Terrain Effects**: Electric punches in Electric Terrain + guaranteed crit + 50% paralysis
4. **Contact Abilities**: Punching moves trigger contact abilities while dealing massive crit damage

### Related Abilities:
- **Way of Precision** (ID varies): Shares exact same implementation (lines 7082-7083)
- **Iron Fist**: Base punching move enhancement
- **Power Fists**: Punching moves target Special Defense
- **Magical Fists**: Punching moves use Special Attack
- **Blitz Boxer**: Priority to punching moves at full HP
- **Raging Boxer**: Punching moves hit twice
- **Fatal Precision**: Guaranteed crits on super-effective moves

### Counterplay:
- **Burn**: Reduces physical punch damage despite crits
- **Intimidate**: Lowers Attack before guaranteed crits land
- **Rocky Helmet**: Punishes contact punching moves
- **Ghost-types**: Immune to Normal/Fighting punches
- **Abilities**: Flame Body, Static can punish contact punches

### Competitive Notes:
- **Tier**: High competitive viability due to reliability and power
- **Team Role**: Excellent on mixed attackers, priority users, and status spreaders
- **Meta Impact**: Forces opponents to respect punch-based coverage
- **Versatility**: Works on both physical and special punch variants

### Version History:
- **Elite Redux**: Introduced as specialized punch enhancement ability
- **Current**: Stable implementation with 5x effect multiplier and guaranteed crits
- **Shared Implementation**: Used by Way of Precision ability

### Technical Notes:
- **Function Reference**: Lines 3895-3904 in src/abilities.cc
- **Registration**: Line 9220 in ability mapping
- **Shared Usage**: Also used by Way of Precision (lines 7082-7083)
- **Move Detection**: Uses IsIronFistBoosted() function from battle_util.c:9183
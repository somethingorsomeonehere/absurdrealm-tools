---
id: 347
name: Multi Headed
status: reviewed
character_count: 287
---

# Multi Headed - Ability ID 347

## In-Game Description
"Pokemon with multiple heads attack 2-3 times per move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Attack 2-3 times per move based on number of heads. Two-headed Pokemon strike twice (1st hit does 100%, 2nd does 25%), three-headed hit thrice (1st hit does 100%, 2nd does 20%, 3rd does 15%). Each hit rolls secondary effects independently (except flinch). Bypasses Fort Knox/Wonder Skin.

## Detailed Mechanical Explanation

### Overview

Multi Headed is an Elite Redux exclusive ability that grants Pokemon the power to attack multiple times based on their anatomical structure. This ability transforms any attacking move into a multi-hit assault, with the number of strikes determined by the Pokemon's head count.

## Core Mechanics

### Hit Calculation
- **Two-Headed Pokemon**: All attacks hit twice (similar to Parental Bond Hyper Aggressive)
- **Three-Headed Pokemon**: All attacks hit three times (unique mechanic)
- **Damage**: Each hit deals full damage (no reduction like standard Parental Bond)

### Technical Implementation
```cpp
// From src/abilities.cc lines 3669-3676
constexpr Ability MultiHeaded = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType {
        if (gBaseStats[gBattleMons[battler].species].flags & F_TWO_HEADED) 
            return PARENTAL_BOND_HYPER_AGGRESSIVE;
        if (gBaseStats[gBattleMons[battler].species].flags & F_THREE_HEADED) 
            return PARENTAL_BOND_THREE_HEADED;
        return MULTIHIT_SINGLE;
    },
    .resistsFortKnox = TRUE,
};
```

### Head Count Determination
Pokemon head counts are defined in their species data through flags:
- `F_TWO_HEADED` flag: Enables 2-hit attacks
- `F_THREE_HEADED` flag: Enables 3-hit attacks
- `heads: X` field: Species data specifying exact head count

## Strategic Applications

### Offensive Power
- **Substitute Breaking**: Multi-hits easily destroy Substitutes in 1-2 strikes
- **Focus Sash Bypass**: Multiple hits bypass Focus Sash/Sturdy completely
- **Damage Stacking**: Full damage on each hit creates overwhelming offensive pressure
- **Status Spreading**: Contact moves can trigger multiple status effects

### Defensive Considerations
- **Recoil Amplification**: Pokemon with recoil moves take damage for each hit
- **Contact Punishment**: Abilities like Rough Skin, Static, or Flame Body trigger multiple times
- **Rocky Helmet**: Each hit triggers Rocky Helmet damage
- **King's Rock/Razor Fang**: Multiple flinch chances per attack

## Competitive Analysis

### Strengths
1. **Unmatched Damage Output**: Full damage multi-hits surpass most other abilities
2. **Fort Knox Resistance**: One of only two abilities that bypasses Fort Knox protection
3. **Versatile Application**: Works with any attacking move type
4. **Meta Disruption**: Forces opponents to reconsider defensive strategies

### Weaknesses
1. **Contact Move Risks**: Significantly more dangerous against contact-punishing abilities
2. **PP Consumption**: Still uses only 1 PP despite multiple hits
3. **Accuracy Dependence**: Miss chance applies to entire attack sequence
4. **Priority Moves**: Each hit is still subject to priority calculations

### Tier Placement: S-Tier
Multi Headed ranks among the most powerful abilities in Elite Redux due to its:
- Unconditional activation on all attacks
- Full damage scaling per hit
- Fort Knox bypass capability
- Universal move compatibility

## Notable Pokemon

### Three-Headed (3 Hits Per Attack)
- **Dugtrio**: Ground-type with exceptional Speed and Attack
- **Magneton**: Electric/Steel with powerful special attacks
- **Dodrio**: Normal/Flying with high Speed and diverse movepool

### Two-Headed (2 Hits Per Attack)
- **Doduo**: Early-game powerhouse with Multi Headed access
- **Weezing**: Defensive tank that becomes offensive threat
- **Girafarig**: Psychic/Normal with balanced offensive stats
- **Deino/Zweilous**: Dark/Dragon types with significant power
- **Binacle**: Rock/Water with Strong Jaw synergy
- **Klink**: Steel type with defensive utility

## Ability Interactions

### Fort Knox Bypass
Multi Headed is explicitly coded to resist Fort Knox (line 3675), making it one of only two abilities that can bypass this defensive fortress:
```cpp
.resistsFortKnox = TRUE,
```

### Parental Bond System Integration
The ability leverages the existing Parental Bond mechanics:
- `PARENTAL_BOND_HYPER_AGGRESSIVE`: 2-hit implementation
- `PARENTAL_BOND_THREE_HEADED`: 3-hit implementation (unique to Multi Headed)

### Contact Move Synergies
- **Strong Jaw**: Each hit benefits from jaw move damage boost
- **Tough Claws**: Contact moves get boosted per hit
- **Iron Fist**: Punching moves receive multiple damage boosts

## Move Compatibility

### Optimal Moves
- **High Base Power**: Maximizes the multi-hit advantage
- **Contact Moves**: Synergizes with contact-boosting abilities (with risk consideration)
- **Status Moves**: Can trigger multiple status chances
- **Priority Moves**: Maintains priority across all hits

### Problematic Moves
- **Recoil Moves**: Multiplies self-damage significantly
- **Multi-Hit Moves**: May interact unpredictably with native multi-hit mechanics
- **Moves with Secondary Effects**: Each hit can trigger effects independently

## Code References

### Primary Implementation
- **File**: `src/abilities.cc`
- **Lines**: 3669-3676
- **Ability Map**: Line 9192

### Related Systems
- **Flag Definitions**: `include/pokemon.h` (F_TWO_HEADED, F_THREE_HEADED)
- **Hit Count Logic**: `src/battle_script_commands.c` lines 986-999
- **Species Data**: `proto/SpeciesList.textproto` (heads field)

### Battle Integration
- **Parental Bond System**: `src/battle_util.c` lines 7330-7334
- **Hit Count Calculation**: `GetParentalBondCount` function


## Conclusion

Multi Headed represents the pinnacle of offensive abilities in Elite Redux, offering unparalleled damage potential through anatomically-justified multi-hit mechanics. Its Fort Knox bypass capability and full damage scaling make it a cornerstone ability for competitive play, though careful consideration of contact move risks and opponent team composition remains essential for optimal utilization.

The ability's thematic integration with Pokemon anatomy (actual head counts) combined with its devastating mechanical impact creates a unique and memorable gameplay experience that exemplifies Elite Redux's innovative approach to ability design.
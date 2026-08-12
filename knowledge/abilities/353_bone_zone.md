---
id: 353
name: Bone Zone
status: reviewed
character_count: 138
---

# Bone Zone - Ability ID 353

## In-Game Description
"Bone moves bypass immunities and flip resistances into weaknesses."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Bone moves bypass immunities and hit for normal damage, while resisted moves do 2x damage. Neutral/super effective moves remain unchanged.

## Detailed Mechanical Explanation

### Overview

**Bone Zone** is a specialized offensive ability that dramatically enhances the effectiveness of bone-based moves. This ability allows Pokemon to use their bone attacks to bypass traditional type matchups, making them incredibly versatile in battle by turning defensive resistances into offensive advantages.

## Mechanics

### Core Functionality

Bone Zone modifies type effectiveness calculations for bone moves through the `onAfterTypeEffectiveness` callback:

1. **Immunity Bypass**: Any move that would normally deal 0 damage (immune) instead deals normal (1x) damage
2. **Resistance Reversal**: Any move that would deal reduced damage (<1x effectiveness) gets doubled to 2x damage
3. **Neutral/Super Effective Unchanged**: Moves that would deal 1x or greater damage remain unmodified

### Technical Implementation

Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` at line 3727:

```cpp
constexpr Ability BoneZone = {
    .onAfterTypeEffectiveness =
        +[](ON_AFTER_TYPE_EFFECTIVENESS) {
            if (*mod >= UQ_4_12(1.0)) return;
            if (*mod == 0) {
                *mod = UQ_4_12(1.0);
                if (mod1) MulModifier(mod, mod1);
                if (mod2) MulModifier(mod, mod2);
                if (mod3) MulModifier(mod, mod3);
            }
            if (*mod < UQ_4_12(1.0)) MulModifier(mod, UQ_4_12(2.0));
        },
};
```

### Damage Calculation Examples

- **Normal Effectiveness (1x)**: Remains 1x damage
- **Super Effective (2x)**: Remains 2x damage  
- **Not Very Effective (0.5x)**: Becomes 1x damage (doubled)
- **Double Resistance (0.25x)**: Becomes 0.5x damage (doubled)
- **Immunity (0x)**: Becomes 1x damage (bypassed)

## Bone Moves Affected

The following moves have the `bone: true` flag and are enhanced by Bone Zone:

### Core Bone Moves
1. **Bone Club** (Ground-type, 80 BP)
   - 30% flinch chance
   - Single-target physical attack

2. **Bonemerang** (Ground-type, 45 BP)
   - Hits twice per use
   - Ignores levitation effects

3. **Bone Rush** (Ground-type, 15 BP)
   - Hits 2-5 times with +1 priority
   - Multi-hit move with priority

4. **Shadow Bone** (Ghost-type, 90 BP)
   - 20% chance to lower Defense
   - Ghost-type bone attack

5. **Blazing Bone** (Fire-type, 15 BP)
   - Hits 2-5 times with +1 priority
   - Fire-type variant of Bone Rush

## Pokemon with Bone Zone

This ability appears as an **innate ability** on the following Pokemon:

### Cubone Line
- **Cubone** (Species #104)
  - Innate abilities: Bone Zone, Battle Armor, Rock Head
  - Regular abilities: Technician, Stamina, Earthbound

- **Marowak** (Species #105)  
  - Innate abilities: Bone Zone, Battle Armor, Rock Head
  - Regular abilities: Technician, Stamina, Skill Link

- **Alolan Marowak** (Fire/Ghost)
  - Innate abilities: Bone Zone, Early Grave, Rock Head
  - Regular abilities: Ill Will, Greater Spirit, Skill Link

## Strategic Applications

### Offensive Utility
- **Coverage**: Bone moves can hit any type for at least neutral damage
- **Immunity Breaking**: Bypasses Ghost immunity to Normal/Fighting moves (if bone moves existed in those types)
- **Resistance Punishment**: Turns opponent's resistances into vulnerabilities

### Type Synergy
- **Ground-type bones**: Excellent coverage against Electric, Fire, Poison, Rock, Steel types
- **Ghost-type bones**: Shadow Bone becomes incredibly versatile
- **Fire-type bones**: Blazing Bone gains priority and type coverage

### Competitive Viability
- **Tier 3+ Threat**: All Bone Zone carriers are competitively viable
- **Priority Access**: Both Bone Rush and Blazing Bone have +1 priority
- **Multi-hit Potential**: Several bone moves hit multiple times, synergizing with Skill Link

## Interactions and Synergies

### Ability Synergies
- **Skill Link**: Guarantees maximum hits from Bone Rush/Blazing Bone (5 hits each)
- **Technician**: Boosts lower power bone moves by 50%
- **Rock Head**: Prevents recoil damage from potential bone moves with recoil

### Item Synergies
- **Thick Club**: Doubles Attack when held by Cubone/Marowak for physical bone moves
- **Expert Belt**: Additional 20% damage when bone moves are super effective

### Strategic Counters
- **Abilities**: Wonder Guard still blocks if the original type effectiveness wasn't super effective
- **Speed Control**: Priority bone moves can be countered by faster priority moves
- **Physical Walls**: High Defense stats can still mitigate damage despite type advantage

## Competitive Analysis

**Strengths:**
- Unprecedented type coverage and immunity bypassing
- Strong priority options with Bone Rush/Blazing Bone
- Natural synergy with the Cubone evolutionary line's stat distribution
- Excellent for breaking through defensive cores

**Weaknesses:**
- Limited to bone-type moves only
- Relatively small movepool compared to other type-enhancing abilities
- Doesn't enhance already super effective matchups
- Physical-based, vulnerable to Intimidate and physical walls

**Overall Rating:** **A-Tier** - Highly specialized but extremely effective within its niche, providing unique utility that few other abilities can match.

## Related Abilities

- **Scrappy**: Allows Normal/Fighting moves to hit Ghost types
- **Mold Breaker**: Ignores ability-based immunities
- **Tinted Lens**: Doubles damage of not very effective moves (all types)
- **Wonder Guard**: Opposite effect - only allows super effective damage

## Notes

- This ability showcases Elite Redux's philosophy of giving specialized Pokemon unique mechanical niches
- The implementation suggests the ability may apply to all moves rather than just bone moves (potential bug or intentional design choice)
- Bone Zone is exclusively an innate ability, meaning it's always active alongside the Pokemon's regular ability
- The ability name is a play on "bone zone" slang while maintaining the bone theme of the Cubone evolutionary line


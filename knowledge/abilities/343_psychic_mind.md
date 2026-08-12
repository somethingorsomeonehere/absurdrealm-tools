---
id: 343
name: Psychic Mind
status: reviewed
character_count: 76
---

# Psychic Mind - Ability ID 343

## In-Game Description
"Boosts Psychic-type moves by 1.2x, or 1.5x when HP is low."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Psychic-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation

### Basic Information
- **Ability ID:** 343  
- **Type:** Offensive Multiplier  
- **Activation:** HP-based threshold

### Overview

Psychic Mind is a signature ability that enhances the power of Psychic-type moves based on the user's remaining HP. This ability follows the classic "pinch ability" pattern, providing moderate enhancement at full health that dramatically increases when the user becomes desperate.

## Mechanics

### Damage Calculation
- **Normal state (HP > 1/3):** Psychic-type moves deal **1.2x damage** (20% increase)
- **Pinch state (HP <= 1/3):** Psychic-type moves deal **1.5x damage** (50% increase)

### Technical Implementation
**File:** `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`  
**Line:** 3627-3629

```cpp
constexpr Ability PsychicMind = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_PSYCHIC),
};
```

The ability uses the `SWARM_MULTIPLIER` macro with `TYPE_PSYCHIC`, defined at lines 293-301:

```cpp
#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
            else                                                             \
                MUL(1.2);                                                    \
        }                                                                    \
    }
```

### Key Mechanics
- Only affects **outgoing damage** from Psychic-type moves
- HP threshold check: `current HP <= (max HP / 3)`
- Stacks multiplicatively with other damage modifiers
- Active on both physical and special Psychic-type moves

## Strategic Applications

### Offensive Strategy
- **Early game:** Provides consistent 20% damage boost to Psychic moves
- **Late game/Pinch situations:** Transforms into a powerful 50% damage boost
- **Sweeping potential:** Combines well with high Special Attack Psychic-types
- **Revenge killing:** Low HP trigger makes weakened Pokemon dangerous

### Defensive Considerations
- Opponents may avoid bringing the user to low HP to prevent the boost
- Creates mindgames around healing vs. maintaining pinch state
- Works well with strategies that intentionally lower HP (Substitute, Life Orb)

### Synergistic Items
- **Life Orb:** Accelerates reaching pinch state while boosting damage further
- **Focus Sash:** Guarantees survival to trigger maximum boost
- **Sitrus Berry:** Can heal out of pinch range when strategic
- **Choice items:** Maximize the boosted damage output

## Competitive Analysis

### Strengths
- **Consistent boost:** Always provides at least 20% damage increase
- **Pinch power:** 50% boost in desperate situations is significant
- **Wide coverage:** Affects all Psychic-type moves
- **Mind games:** Creates prediction layers in battle

### Limitations
- **Type-specific:** Only affects one type of move
- **HP dependent:** Requires taking damage for maximum benefit
- **No defensive utility:** Purely offensive ability
- **Predictable:** Opponents know when boost is active

### Usage Tiers
**Tier 4 (Standard):** Solid ability for Psychic-type attackers  
**Tier 3 (Competitive):** Strong on Pokemon with diverse Psychic movesets  
**Tier 2 (High-level):** Excellent on specialized Psychic sweepers

## Pokemon with Psychic Mind

### As Changeable Ability
- **Alolan Raichu** (Electric/Psychic) - Line 35861
- **Jynx** (Ice/Psychic) - Line 26073
- **Mewtwo variants** - Lines 67276, 76972

### As Innate Ability
- **Psyduck** (Water) - Line 10386
- **Golduck** (Water) - Line 10651
- **Abra line** - Multiple entries
- **Psychic-type specialists** - Various lines throughout SpeciesList.textproto

*Note: Over 35 Pokemon have this ability, making it one of the more widely distributed type-boosting abilities.*

## Related Abilities

### Same Pattern (SWARM_MULTIPLIER)
- **Swarm** (Bug-type) - 1.2x/1.5x for Bug moves
- **Blaze** (Fire-type) - 1.2x/1.5x for Fire moves  
- **Torrent** (Water-type) - 1.2x/1.5x for Water moves
- **Overgrow** (Grass-type) - 1.2x/1.5x for Grass moves

### Enhanced Variants (BOOSTED_SWARM_MULTIPLIER)
Some abilities use the boosted version with 1.3x/1.8x multipliers instead.

## Interactions

### Battle Mechanics
- **Critical hits:** Boost applies before critical hit calculation
- **Type immunity:** No effect if Psychic move doesn't affect target
- **Multi-hit moves:** Each hit gets the boost
- **STAB:** Stacks multiplicatively with Same Type Attack Bonus

### Status Conditions
- **Burn:** Physical Psychic moves still get boosted damage
- **Paralysis/Sleep:** Ability remains active while incapacitated
- **Confusion:** Boost applies to confusion self-damage if Psychic-type

## Trivia
- Part of the "pinch ability" family that originated in Generation III
- The 1/3 HP threshold is consistent across all similar abilities
- Despite the name, affects both physical and special Psychic moves
- One of the most common innate abilities in Elite Redux
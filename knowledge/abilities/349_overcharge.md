---
id: 349
name: Overcharge
status: reviewed
character_count: 162
---

# Overcharge - Ability ID 349

## In-Game Description
"Electric moves are super effective vs Electric-types and can paralyze them."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user's Electric-type moves become effective against Electric-type Pokemon, dealing 2x damage instead of 0.5x. Also allows the user to paralyze Electric-types.

## Detailed Mechanical Explanation

### Overview

Overcharge is a unique Elite Redux ability that fundamentally changes how Electric-type interactions work in battle. This ability makes Electric-type moves super effective (2x damage) against Electric-type Pokemon and allows Electric-type Pokemon to be paralyzed, completely bypassing their natural immunity.

## Code Implementation

**Location:** `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Lines 3696-3707)

```cpp
constexpr Ability Overcharge = {
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        CHECK(moveType == TYPE_ELECTRIC)
        CHECK(defType == TYPE_ELECTRIC)
        *mod = UQ_4_12(2.0);
        return TRUE;
    },
    .onCanStatusType = +[](ABILITY_ON_CAN_STATUS_TYPE) -> int {
        CHECK(status & CHECK_PARALYSIS)
        return TRUE;
    },
};
```

### Technical Mechanics

1. **Type Effectiveness Modification:**
   - When an Electric-type move targets an Electric-type defender
   - Sets the type effectiveness modifier to 2.0 (super effective)
   - Overrides the default 0.5x (not very effective) modifier

2. **Status Immunity Bypass:**
   - Allows paralysis status to affect Electric-type Pokemon
   - Bypasses the natural paralysis immunity of Electric-types
   - Works with any source of paralysis (moves, abilities, items)

## Strategic Applications

### Offensive Usage
- **Electric vs Electric matchups:** Transform defensive scenarios into offensive opportunities
- **Paralysis support:** Enable Thunder Wave and other paralysis moves against Electric-types
- **Coverage improvement:** Electric moves become viable against Electric-type walls

### Defensive Considerations
- **Double-edged nature:** Electric-types with Overcharge are vulnerable to Electric attacks
- **Speed control:** Can be paralyzed by opposing Electric-types
- **Risk vs reward:** Increased offensive power at the cost of defensive stability

## Pokemon with Overcharge

Based on trainer data analysis, Overcharge appears on various Electric-type Pokemon including:
- Porygon line variants
- Various Pikachu forms
- Several legendary/mythical Electric-types
- Custom Elite Redux Electric-type variants

## Competitive Analysis

### Strengths
- **Meta disruption:** Changes established Electric-type matchups
- **Versatility:** Both offensive and status support applications
- **Surprise factor:** Opponents may not expect Electric moves to be super effective

### Weaknesses
- **Self-vulnerability:** Makes the user weak to Electric attacks
- **Limited scope:** Only affects Electric-type interactions
- **Predictability:** Once revealed, opponents can exploit the weakness

### Tier Ranking: A-Tier
Overcharge is a high-impact ability that significantly alters battle dynamics. While situational, its effects are powerful enough to warrant A-tier placement in competitive play.

## Related Abilities

### Combination Abilities
- **Depravity (Ability ID: Unknown):** Combines Merciless + Overcharge
  - Always critical hits against paralyzed opponents
  - Can paralyze Electric-types for guaranteed crits
  - Extremely powerful offensive combination

### Similar Mechanics
- **Corrosion:** Bypasses Poison immunity (Steel/Poison types)
- **Normalize:** Changes move types for effectiveness modifications
- **Refrigerate/Pixilate/Aerilate:** Type conversion with power boost

## Battle Interactions

### Move Interactions
- **Thunder Wave:** Can now paralyze Electric-types
- **Electric-type attacks:** Deal super effective damage to Electric-types
- **Paralysis-inducing moves:** No longer blocked by Electric typing

### Ability Interactions
- **Lightning Rod/Volt Absorb:** Still redirect/absorb Electric moves
- **Motor Drive:** Still activates on Electric-type moves
- **Static:** Can now paralyze Electric-type attackers

## Usage Notes

1. **Team building:** Consider both offensive and defensive implications
2. **Prediction:** Use the surprise factor strategically in key matchups
3. **Coverage:** Excellent for handling Electric-type walls and setup sweepers
4. **Risk management:** Be aware of the increased vulnerability to Electric attacks


## Code References

- **Ability Definition:** `src/abilities.cc:3696-3707`
- **Ability Constant:** `include/generated/constants/abilities.h` - `ABILITY_OVERCHARGE = 349`
- **Proto Description:** `proto/AbilityList.textproto`
- **Trainer Usage:** Multiple references in `src/data/trainer_parties.h`
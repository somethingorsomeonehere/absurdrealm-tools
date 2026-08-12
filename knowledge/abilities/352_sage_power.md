---
id: 352
name: Sage Power
status: reviewed
character_count: 105
---

# Sage Power - Ability ID 352

## In-Game Description
"Boosts Special Attack by 50% but locks into first move used."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Special Attack by 50% but locks the user into using the first move selected until they switch out.

## Detailed Mechanical Explanation

### Overview

Sage Power is a powerful ability that provides a substantial 50% boost to Special Attack damage at the cost of move flexibility. This ability combines the offensive power of Choice Specs with the permanence of an ability slot, making it ideal for specialized special attackers who can afford to commit to a single powerful move.

## Mechanics

### Special Attack Boost
- **Multiplier**: 1.5x (50% increase) to Special Attack
- **Applies to**: All special moves (IS_MOVE_SPECIAL check)
- **Implementation**: Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` at lines 3720-3725

```cpp
constexpr Ability SagePower = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_MOVE_SPECIAL(move)) MUL(1.5);
        },
};
```

### Move Locking Mechanism
- **Implementation**: Located in `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_util.c` at lines 1456-1466
- **Behavior**: Uses the same choice mechanics as Gorilla Tactics and Choice items
- **Trigger**: Activates after the first move is selected in battle
- **Restriction**: Cannot use any move other than the locked move until switching out

```c
// Sage Power and Gorilla Tactics
if ((BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_SAGE_POWER) || 
     BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_GORILLA_TACTICS) ||
     BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_DISCIPLINE)) &&
    *choicedMove != 0 && *choicedMove != 0xFFFF && *choicedMove != move) {
    gCurrentMove = *choicedMove;
    // ... error handling
}
```

## Strategic Applications

### Optimal Usage Scenarios
1. **Special Wallbreakers**: Pokemon with high base Special Attack that need extra power to break through defensive walls
2. **Revenge Killers**: Fast special attackers that can clean up weakened teams with a single powerful move
3. **Terrain Abusers**: Pokemon that can set up Psychic Terrain to boost their locked psychic move further
4. **Late-Game Sweepers**: When the opponent's team is sufficiently weakened that move prediction becomes easier

### Move Selection Considerations
- **High Base Power**: Prioritize moves with 90+ base power to maximize the 50% boost
- **Reliable Accuracy**: Choose moves with 100% accuracy to avoid the risk of missing with your only option
- **Coverage Moves**: Select moves that hit a wide range of Pokemon for maximum utility
- **Setup Moves**: Consider locking into setup moves if the Pokemon has time to boost safely

## Competitive Analysis

### Advantages
- **Immediate Power**: No setup required, instant 50% Special Attack boost
- **Ability Slot Efficiency**: Combines the power of Choice Specs without using an item slot
- **Prediction Pressure**: Forces opponents to play around your locked move
- **Team Synergy**: Pairs well with Psychic Terrain, Helping Hand, and other support

### Disadvantages
- **Move Restriction**: Complete loss of move flexibility once locked in
- **Predictability**: Opponents can easily predict your next move after the first use
- **Setup Vulnerability**: Cannot switch to status moves or different coverage options
- **Entry Hazards**: Switching to reset the lock risks Stealth Rock and other hazard damage

### Comparison to Related Abilities
- **Gorilla Tactics**: Physical equivalent with identical mechanics
- **Choice Specs**: Item-based version allows for item flexibility but takes up item slot
- **Sheer Force**: 30% boost without move restriction but only affects moves with secondary effects

## Pokemon with Sage Power

Based on the base stats data, the following Pokemon can have Sage Power as one of their abilities:

1. **Golduck** (Water/Psychic) - Cloud Nine/Sage Power/Drizzle
2. **Magearna** (Psychic) - Soul Heart/Sage Power/Psychic Surge
3. **Lunatone** (Rock/Psychic) - Scare/Sage Power/Dreamcatcher
4. **Froakie** (Water) - Prankster/Sage Power/Friend Guard
5. **Frogadier** (Water) - Prankster/Sage Power/Friend Guard
6. **Terrakion-Elite** (Rock/Fighting) - Sage Power/Sheer Force/Battle Aura
7. **Lunala-Elite** (Psychic/Ghost) - Low Visibility/Dreamcatcher/Sage Power
8. **Pheromosa-Elite** (Normal/Psychic) - Queenly Majesty/Competitive/Sage Power
9. **Abra-Elite** (Psychic) - Psychic Surge/Prankster/Sage Power
10. **Kadabra-Elite** (Psychic) - Sheer Force/Psychic Surge/Sage Power

## Related Mechanics

### Choice Interactions
- **Move Selection**: Uses the same `choicedMove` system as Choice items
- **Battle Structure**: Stored in `gBattleStruct->choicedMove[battler]`
- **Reset Conditions**: Switching out or fainting resets the choice lock

### Status and Effect Interactions
- **Mental Herb**: Does not remove the choice lock (unlike Taunt or Disable)
- **Encore**: Can still be Encored into the locked move
- **Disable**: Can be disabled, forcing the user to Struggle

## Code References

- **Main Implementation**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` lines 3720-3725
- **Choice Logic**: `/Users/joel/Github/eliteredux/eliteredx-source/src/battle_util.c` lines 1456-1466, 1530-1531
- **Ability Text**: `/Users/joel/Github/eliteredux/eliteredux-source/include/generated/data/abilities/ability_text.hh` line 357
- **Constant Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/include/generated/constants/abilities.h` line 358

## Notes

- Sage Power is mechanically identical to Gorilla Tactics but affects Special Attack instead of Attack
- The ability provides more immediate power than most other special attack boosting abilities
- Careful team building is essential to support the move restriction limitation
- Consider pairing with Pokemon that can remove or weaken the Pokemon's counters before bringing in the Sage Power user


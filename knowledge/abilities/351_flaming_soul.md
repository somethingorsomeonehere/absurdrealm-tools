---
id: 351
name: Flaming Soul
status: reviewed
character_count: 54
---

# Flaming Soul - Ability ID 351

## In-Game Description
"Grants +1 priority to Fire-type moves when at full HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to Fire-type moves when at full HP.

## Detailed Mechanical Explanation

### Overview
Flaming Soul is a priority-granting ability that gives Fire-type moves +1 priority when the user is at maximum HP. It is functionally identical to Gale Wings but for Fire-type moves instead of Flying-type moves, making it a powerful tool for Fire-type attackers who can maintain their health.

## Code Implementation

### Source Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: 3716-3718
- **Definition**: `constexpr Ability FlamingSoul = { .onPriority = GALE_WINGS_CLONE(TYPE_FIRE), };`

### Macro Definition
The ability uses the `GALE_WINGS_CLONE` macro (lines 128-133):
```cpp
#define GALE_WINGS_CLONE(type)                               \
    +[](ON_PRIORITY) -> int {                                \
        CHECK(GetTypeBeforeUsingMove(move, battler) == type) \
        CHECK(BATTLER_MAX_HP(battler))                       \
        return 1;                                            \
    }
```

### Key Technical Details
- **HP Check**: Uses `BATTLER_MAX_HP(battler)` macro defined in `/Users/joel/Github/eliteredux/eliteredux-source/include/battle.h:781`
  - Formula: `(gBattleMons[battlerId].hp == gBattleMons[battlerId].maxHP)`
- **Type Check**: Verifies move type before usage via `GetTypeBeforeUsingMove()`
- **Priority Boost**: Returns `1` for +1 priority boost
- **Ability Registration**: Listed in ability table at line 9196

## Mechanics

### Activation Requirements
1. **Maximum HP**: The Pokemon must have full HP (current HP = max HP)
2. **Fire-type Move**: The move being used must be Fire-type
3. **Move Usage**: Only applies when the Pokemon is using a move

### Priority System
- Normal moves have priority 0
- With Flaming Soul active, Fire moves get priority +1
- This allows Fire moves to outspeed most other moves
- Does not stack with other priority effects

### Limitations
- **HP Dependent**: Any damage taken disables the ability until HP is restored to maximum
- **Type Specific**: Only affects Fire-type moves
- **No Status Moves**: Only affects damaging and non-damaging Fire-type moves

## Strategic Applications

### Offensive Strategies
1. **Lead Sweeping**: Perfect for fast Fire-type leads with powerful moves
2. **Revenge Killing**: Guaranteed first strike when at full HP
3. **Priority Control**: Dominates priority wars with Fire moves
4. **Setup Protection**: Can interrupt setup attempts with priority Fire moves

### Synergistic Moves
- **Flamethrower**: Reliable priority special attack
- **Fire Blast**: High-power priority special move
- **Flare Blitz**: Devastating priority physical attack (but causes recoil)
- **Heat Wave**: Priority spread move in doubles
- **Will-O-Wisp**: Priority status infliction

### Team Building Considerations
- Pairs well with healing support (Wish, Heal Bell)
- Benefits from Leftovers or other passive recovery
- Strong with Life Orb for maximum damage output
- Excellent with Choice items for hit-and-run tactics

## Competitive Analysis

### Strengths
1. **Immediate Threat**: Forces opponents to respect priority Fire moves
2. **Speed Control**: Bypasses speed tiers entirely when active
3. **Versatile**: Works with both physical and special Fire moves
4. **Psychological Pressure**: Opponents must play around potential priority

### Weaknesses
1. **HP Dependency**: Easily disabled by any damage
2. **Type Limitation**: No priority on non-Fire moves
3. **Predictable**: Opponents know to damage first to disable
4. **Recoil Vulnerability**: Strong Fire moves often have recoil

### Comparison to Similar Abilities
- **Gale Wings**: Same mechanics but for Flying-type moves
- **Triage**: +3 priority but only for healing moves
- **Prankster**: +1 priority for status moves only
- **Quick Draw**: 30% chance for +1 priority on any move

## Pokemon with Flaming Soul

Based on proto file analysis, the following Pokemon have access to Flaming Soul:

### Primary Ability Holders
- **Ogerpon Hearthflame**: Fire/Fairy type with strong offensive stats
- **Magmar**: Classic Fire-type with solid special attack
- **Magby**: Pre-evolution with potential for growth
- **Entei**: Legendary Fire-type with excellent physical attack

### Usage Patterns
- Most common on offensive Fire-type Pokemon
- Often paired with other Fire-boosting abilities as innates
- Frequently combined with Flash Fire or other Fire immunities

## Related Abilities

### Direct Variants
- **Gale Wings** (Ability #177): Flying-type version
- **Ice-type Gale Wings variants**: Similar priority mechanics for Ice moves
- **Electric-type variants**: Priority Electric moves under certain conditions

### Complementary Abilities
- **Flash Fire**: Immunity to Fire moves and attack boost
- **Drought**: Weather support for Fire moves
- **Solar Power**: Special attack boost in sun

## Counters and Interactions

### Effective Counters
1. **Residual Damage**: Stealth Rock, Spikes, burn, poison
2. **Multi-hit Moves**: Breaks through and disables ability
3. **Priority Moves**: Can still be outsped by higher priority
4. **Flash Fire Users**: Immune to priority Fire moves

### Notable Interactions
- **Choice Items**: Lock into one move but maintain priority
- **Life Orb**: Extra damage without HP dependency issues
- **Recoil Moves**: Self-disables after one use (Flare Blitz)
- **Weather**: Sun boosts Fire power, hail/sandstorm chips HP

## Conclusion

Flaming Soul is a high-impact ability that transforms Fire-type Pokemon into immediate threats when at full HP. Its strategic value lies in the constant pressure it applies to opponents, forcing them to prioritize dealing damage to disable the ability. While HP-dependent, skilled players can leverage healing support and careful positioning to maintain the advantage throughout battle.

The ability rewards aggressive play while punishing passive strategies, making it excellent for fast-paced offensive teams that can protect their Flaming Soul user's HP while applying constant pressure with priority Fire moves.


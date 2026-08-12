---
id: 735
name: Know Your Place
status: reviewed
character_count: 183
---

# Know Your Place - Ability ID 735

## In-Game Description
"Contact attacks make foes move last for 5 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Landing contact moves causes the target to always move last regardless of priority, speed, or other effects for 5 turns. Effect does not stack or refresh on already afflicted targets.

## Detailed Mechanical Explanation
**Know Your Place** is a powerful speed control ability that completely overrides the normal priority system through the "dazed" status effect.

### Core Mechanics

#### Dazed Status Infliction
When a Pokemon with Know Your Place lands a contact move on an opponent:
1. **Contact Requirement**: Only contact moves trigger the effect
2. **Duration**: Inflicts dazed status for exactly 5 turns
3. **No Stacking**: Already dazed Pokemon cannot be dazed again
4. **Message**: "{B_DEF_NAME_WITH_PREFIX} is dazed by the blow!"

#### Dazed Status Effect
The dazed status forces the affected Pokemon to move **absolutely last overall**, not just within their priority bracket.

### Speed System Override

#### Technical Implementation
The dazed status affects the `dazedNegation` field in the speed calculation system:

```cpp
// Speed Value Bit Layout (higher bits = higher precedence)
u16 dazedNegation:1;    // 0 if dazed, 1 if not dazed
u16 afterYou:1;
u16 priority:4;         // Move priority (-7 to +8 range)  
u16 goesFirst:2;
u16 goesLastNegation:2;
u16 effectiveSpeed;     // Actual speed stat
```

#### Priority Override Logic
- **Dazed Pokemon**: `dazedNegation = 0` (false)
- **Non-dazed Pokemon**: `dazedNegation = 1` (true)
- **Result**: Dazed Pokemon ALWAYS move after non-dazed Pokemon

### Practical Examples

#### Priority Override
- A dazed Pokemon using **Quick Attack (+1 priority)** will still move after a non-dazed Pokemon using a **normal priority move**
- **Multiple dazed Pokemon** compete among themselves using normal priority and speed rules
- **Only exception**: Quash effect overrides all speed mechanics

#### Speed Comparison
When determining turn order:
1. **Non-dazed Pokemon** are processed first (regardless of priority/speed)
2. **Dazed Pokemon** are processed last (using normal priority/speed among themselves)
3. **Priority moves** on dazed Pokemon are still slower than normal moves on non-dazed Pokemon

### Implementation Details

```cpp
constexpr Ability KnowYourPlace = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK_NOT(gVolatileStructs[target].dazed)  // Doesn't stack
        CHECK(IsMoveMakingContact(move, battler))

        gVolatileStructs[target].dazed = 5;  // 5 turns
        BattleScriptCall(BattleScript_TargetDazed);
        return TRUE;
    },
};
```

### Status Management
- **Duration**: Counts down at end of each turn
- **Display**: Shows "Dazed" with turns remaining in battle UI
- **Clearing**: Automatically removes when counter reaches 0
- **Switching**: Status persists when switching out and back in

### Pokemon with This Ability

#### Current Users
- **Mega Slaking** (Normal/Ice type)
- **Mega Slaking (Ape Shift form)** (Normal/Ice type)

Both forms have Know Your Place as one of their regular abilities alongside Unseen Fist and Contempt.

### Strategic Applications

#### Speed Control
- **Shuts down fast sweepers** by forcing them to move last
- **Counters priority moves** completely (Quick Attack, Bullet Punch, etc.)
- **Controls tempo** by manipulating turn order

#### Defensive Utility
- **Punishes physical attackers** who make contact
- **Creates safe setup opportunities** when opponent is forced to move last
- **Disrupts offensive momentum** through speed manipulation

#### Team Synergy
- **Benefits slower teammates** who can now outspeed dazed opponents
- **Enables setup strategies** with guaranteed first moves
- **Supports defensive cores** through speed control

### Limitations
- **Contact requirement**: Only triggers on contact moves
- **No stacking**: Cannot extend duration or intensify effect
- **Self-inflicted contact**: May affect the user if opponent has contact-based retaliation

### Unique Position
Know Your Place is one of the most powerful speed control abilities in Elite Redux, providing absolute priority override that cannot be circumvented by normal priority mechanics. It creates a complete role reversal where even the fastest Pokemon become the slowest when dazed.
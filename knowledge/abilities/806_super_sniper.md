---
id: 806
name: Super Sniper
status: reviewed
character_count: 185
---

# Super Sniper - Ability ID 806

## In-Game Description
"Sniper + Attacks hit switching foes with 1/2 Power."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts critical hit damage from 1.5x to 2.25x by applying an additional 50% multiplier. Attacks strike foes before they finish switching out for 50% power, damaging them before leaving. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Super Sniper is a combination ability that merges two distinct effects:

1. **Sniper Component**: Increases critical hit damage multiplier from the standard 1.5x to 2.25x (1.5 x 1.5)
2. **Pursuit Component**: Automatically attacks switching opponents with reduced power

### Implementation Details

```cpp
constexpr Ability SuperSniper = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            // Inherit Sniper's crit damage boost
            Sniper.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            // Apply 0.5x damage for pursuit attacks
            if (gProcessingExtraAttacks && gQueuedExtraAttackData[0].ability == ability) {
                MUL(0.5);
            }
        },
    .onPreemptAction = +[](ON_PREEMPT_ACTION) -> int {
        // Trigger on opponent switch attempts
        CHECK(gCurrentActionFuncId == B_ACTION_SWITCH)
        CHECK(gActionsByTurnOrder[GetBattlerTurnOrderNum(battler)] == B_ACTION_USE_MOVE)
        // Queue extra attack with selected move
        // ...
    },
};
```

### Activation Conditions

**Sniper Component:**
- Activates whenever the Pokemon lands a critical hit
- Works with all damaging moves that can critically hit
- Damage calculation: Base damage x Critical modifier (1.5x) x Super Sniper bonus (1.5x) = 2.25x total

**Pursuit Component:**
- Triggers when an opponent attempts to switch out
- Only works if the Super Sniper user has selected a damaging move that can target the switching Pokemon
- Move targeting must be compatible (Selected, Both, Foes and Ally targets work; Random targets do not)
- The selected move is executed immediately at 0.5x power before the switch completes

### Affected Moves
- **All damaging moves** for the critical hit component
- **Most direct-targeting moves** for the pursuit component
- **Excluded from pursuit**: Moves with random targeting, self-targeting moves

### Strategic Implications

**Offensive Usage:**
- Excellent for eliminating weakened opponents trying to escape
- High critical hit rate moves become extremely threatening (2.25x damage on crits)
- Pairs well with moves like Slash, Razor Leaf, or Stone Edge
- Forces opponents to stay in battle rather than switch freely

**Defensive Considerations:**
- Users become priority targets due to their switching punishment
- Vulnerable to status moves and non-damaging strategies
- Can be played around with U-turn/Volt Switch strategies

### Example Damage Calculations

Base scenario: 100 Base Power move, no other modifiers
- Normal hit: 100 damage
- Critical hit with Super Sniper: 225 damage (100 x 1.5 crit x 1.5 Super Sniper)
- Pursuit attack on switch: 50 damage (100 x 0.5 pursuit penalty)
- Critical pursuit attack: 112.5 damage (100 x 1.5 crit x 1.5 Super Sniper x 0.5 pursuit)

### Common Users
- **Decidueye** (Mega form): Primary known user with ABILITY_SUPER_SNIPER as an innate ability
- Often paired with high critical hit ratio moves and coverage moves

### Competitive Usage Notes
- Creates a "damned if you do, damned if you don't" scenario for opponents
- Staying in risks massive critical hit damage
- Switching out guarantees chip damage and potential KO on weakened Pokemon
- Excellent for late-game cleanup and pressure

### Counters
**Direct Counters:**
- Ghost-types (immune to Normal/Fighting pursuit attacks)
- Priority moves to KO before Super Sniper can act
- U-turn/Volt Switch users can switch and potentially revenge kill

**Indirect Counters:**
- Status moves (Sleep, Paralysis) to disable the threat
- Defensive pivots that can tank both hits and crits
- Stealth Rock + pursuit damage can overwhelm the user

### Synergies
**Items:**
- Scope Lens, Razor Claw: Increase critical hit rates to maximize Sniper component
- Life Orb: Amplifies both normal hits and critical hits
- Choice items: Lock into powerful moves for consistent threat

**Abilities:**
- Often appears as innate ability alongside other offensive abilities
- Pairs well with speed-boosting abilities to outpace switch attempts

**Moves:**
- High crit-rate moves: Slash, Stone Edge, Razor Leaf
- Wide coverage moves: Ensures pursuit hits are meaningful
- Entry hazard support: Maximizes pursuit damage effectiveness

### Version History
- Introduced in Elite Redux as a combination ability
- Part of the expanded ability system (ID 806)
- Designed to create aggressive, anti-switching gameplay dynamics

### Technical Notes
- Uses the extra attack system (`gQueuedExtraAttackData`) for pursuit mechanics
- Inherits Sniper's critical hit calculation through delegation
- Pursuit attacks bypass normal turn order and execute immediately
- Compatible with the majority of offensive moves in the game
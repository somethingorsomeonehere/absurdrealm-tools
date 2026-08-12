---
id: 100
name: Stall
status: reviewed
character_count: 146
---

# Stall - Ability ID 100

## In-Game Description
"Takes 30% less damage if it hasn't moved yet."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage by 30% if the user has not moved yet. Multiplicative with other damage reduction sources. Works when the user switches in mid-turn.

## Detailed Mechanical Explanation

### Core Functionality
- **Damage Reduction**: 30% (0.7x multiplier)
- **Activation Condition**: When `gCurrentTurnActionNumber < GetBattlerTurnOrderNum(battler)`
- **Damage Types Affected**: All incoming damage (physical, special, fixed)
- **Breakable**: Yes (can be suppressed by Mold Breaker, etc.)

### Technical Implementation
```c
constexpr Ability Stall = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (gCurrentTurnActionNumber < GetBattlerTurnOrderNum(battler)) MUL(.7);
        },
    .breakable = TRUE,
};
```

The ability checks if the current turn action number is less than the defender's turn order position, meaning the defender hasn't acted yet.

### Turn Order Mechanics
1. Turn order is determined at the start of each turn based on:
   - Priority brackets
   - Speed stats (or Attack/Defense in Trick Room)
   - Speed ties resolved randomly
2. Stall activates when attacked before the user's turn
3. Does not activate if the user has already moved

### Strategic Implications
- **Trick Room Synergy**: Naturally slow Pokemon benefit most
- **Priority Move Protection**: Reduces damage from priority attacks
- **Switch-In Safety**: Provides protection on the turn switched in
- **Late-Game Advantage**: More likely to activate when slower than opponents

## Interactions

### Synergistic Abilities
- **Analytic**: Combined in Haste Makes Waste ability
- **Swift Swim**: Combined in Breakwater ability (defensive rain sweeper)
- **Iron Barbs/Rough Skin**: Punishes physical attackers while taking reduced damage

### Synergistic Moves
- **Gyro Ball**: Benefits from low speed that triggers Stall
- **Payback**: Double damage when moving second
- **Avalanche/Revenge**: Increased power after taking damage
- **Counter/Mirror Coat**: Reduced damage taken means safer counterattacks

### Counters and Limitations
- **Mold Breaker**: Ignores Stall's damage reduction
- **Faster Pokemon**: No benefit when moving first
- **Status Moves**: Doesn't reduce status move effects
- **Hazard Damage**: Doesn't affect entry hazards or weather

## Competitive Analysis

### Strengths
- Consistent damage reduction for slow Pokemon
- No setup required
- Works on all damage types
- Excellent for defensive pivots

### Weaknesses
- No benefit when moving first
- Breakable by Mold Breaker variants
- Less useful on fast Pokemon
- Doesn't help with status conditions

### Optimal Users
Stall is most effective on:
- Naturally slow, bulky Pokemon
- Trick Room sweepers
- Defensive walls and pivots
- Pokemon with negative priority moves

## Dual Ability Combinations

### Breakwater (Swift Swim + Stall)
- Defensive rain sweeper concept
- Speed boost in rain while maintaining bulk
- Unique defensive-offensive balance

### Haste Makes Waste (Stall + Analytic)
- 30% damage reduction when moving last
- 30% damage boost when moving last
- Perfect for slow, bulky attackers

## Usage Tips

1. **Team Building**: Pair with Trick Room setters for maximum effectiveness
2. **EV Spreads**: Invest in bulk over speed to ensure Stall activates
3. **Move Selection**: Use moves that benefit from moving last
4. **Switch Timing**: Safe switches into predicted attacks
5. **Speed Control**: Consider moves/items that lower speed

## Conclusion

Stall is a reliable defensive ability that rewards patient, defensive play. While simple in concept, it provides consistent value for slow Pokemon and creates unique strategic opportunities when combined with moves and abilities that benefit from moving last. Its inclusion in dual abilities like Breakwater and Haste Makes Waste demonstrates its versatility in creating balanced offensive-defensive combinations.

---
id: 705
name: Terastal Treasure
status: reviewed
character_count: 128
---

# Terastal Treasure - Ability ID 705

## In-Game Description
"Reduces damage taken by 40%, but lowers speed by 20%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces incoming damage by 40% while lowering the Pokemon's Speed by 20%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Terastal Treasure is a defensive ability that provides significant damage reduction at the cost of reduced Speed. The ability creates a powerful tank-oriented trade-off between survivability and priority.

### Implementation Details
```c
constexpr Ability TerastalTreasure = {
    .onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) { MUL(.6); },
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED) *stat *= .8;
        },
    .breakable = TRUE,
};
```

### Damage Reduction Mechanics
- **Incoming damage multiplier**: 0.6x (reduces damage by 40%)
- **Applies to**: All forms of incoming damage
  - Physical attacks
  - Special attacks
  - Status-based damage (likely most forms)
- **Calculation**: Applied as a defensive multiplier in damage calculation

### Speed Reduction Mechanics
- **Speed stat multiplier**: 0.8x (reduces Speed by 20%)
- **Applies to**: Base Speed stat calculation
- **Timing**: Calculated during stat determination phase
- **Permanent effect**: Active as long as ability is present

### Important Interactions
- **Breakable ability**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze, and Neutralizing Gas
- **Damage calculation order**: Applied during defensive multiplier phase
- **Speed priority**: Affects move order and priority bracket determination
- **Choice items**: Speed reduction affects which moves go first with choice items
- **Trick Room**: Makes the Pokemon faster in Trick Room due to lower effective Speed

### Technical Implementation Notes
- Uses `onDefensiveMultiplier` callback for damage reduction
- Uses `onStat` callback for Speed modification
- Marked as `breakable = TRUE` meaning it can be suppressed
- Speed modification applies during stat calculation, not as a temporary boost/drop

### Strategic Implications
- **Tank role enhancement**: Perfect for bulky defensive Pokemon
- **Priority trade-off**: Sacrifices speed for survivability
- **Wall potential**: Allows frail Pokemon to function as walls
- **Trick Room synergy**: Lower speed becomes an advantage
- **Setup opportunity**: Surviving hits allows more setup chances

### Optimal Users
- Naturally bulky Pokemon who can afford the Speed drop
- Pokemon with low Speed that benefit from the defense boost
- Trick Room team members
- Setup sweepers who need time to boost
- Wall Pokemon looking for extra bulk

### Counters and Weaknesses
- **Ability suppression**: Mold Breaker variants remove both benefits
- **Status conditions**: Still vulnerable to burn, poison, etc.
- **Priority moves**: Speed reduction makes priority moves more threatening
- **Speed control**: Becomes more vulnerable to faster opponents
- **Multi-hit moves**: Each hit is reduced, but still adds up

### Synergies
- **Trick Room**: Lower speed becomes advantageous
- **Recovery moves**: More opportunities to heal due to survivability
- **Setup moves**: Can survive hits while boosting stats
- **Assault Vest**: Stacks with special defensive items
- **Eviolite**: Combines with defensive items for extreme bulk

### Competitive Usage Notes
- **Meta impact**: Potentially shifts damage calculations significantly
- **Team building**: Requires team support for speed control or Trick Room
- **Move selection**: Favors powerful, low-priority moves
- **Item synergy**: Works well with defensive items and Trick Room support
- **Hazard weakness**: Still vulnerable to entry hazards

### Version History
- **Elite Redux exclusive**: Custom ability for the romhack
- **Design philosophy**: High-risk, high-reward defensive ability
- **Balance consideration**: 40% damage reduction is substantial but Speed penalty is significant

### Common Matchups
- **Offensive threats**: Can tank hits that would normally OHKO
- **Priority users**: Becomes more vulnerable to priority moves
- **Status spreaders**: Still needs to worry about status conditions
- **Setup sweepers**: Can potentially wall setup attempts
- **Choice users**: Speed reduction affects choice item effectiveness
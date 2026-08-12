---
id: 419
name: Forest Rage
status: reviewed
character_count: 74
---

# Forest Rage - Ability ID 419

## In-Game Description
"Boosts Grass-type moves by 1.3x, or 1.8x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Grass-type moves by 30%, or by 80% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Forest Rage is an offensive ability that boosts Grass-type moves with conditional scaling based on HP thresholds. It uses the BOOSTED_SWARM_MULTIPLIER system to provide enhanced damage output for Grass-type attacks.

### Activation Conditions
- **Move type requirement**: Move must be Grass-type
- **HP threshold (healthy)**: Above 1/3 maximum HP = 1.3x multiplier
- **HP threshold (low)**: Below or equal to 1/3 maximum HP = 1.8x multiplier
- **Universal typing**: Works regardless of user's type

### Technical Implementation
```c
// Forest Rage uses BOOSTED_SWARM_MULTIPLIER macro for TYPE_GRASS
constexpr Ability ForestRage = {
    .onOffensiveMultiplier = BOOSTED_SWARM_MULTIPLIER(TYPE_GRASS),
};

// Macro expands to:
+[](ON_OFFENSIVE_MULTIPLIER) {
    if (moveType == TYPE_GRASS) {
        if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3))
            MUL(1.8);  // 80% boost when low HP
        else
            MUL(1.3);  // 30% boost when healthy
    }
}
```

### HP Calculation Details
- **Threshold**: 1/3 of maximum HP (rounded down)
- **Example**: 300 HP Pokemon activates strong boost at 100 HP or below
- **Persistent**: Effect remains active until HP rises above threshold
- **Real-time**: Updates immediately when HP changes

### Important Interactions
- **Type immunity**: Doesn't boost non-Grass moves
- **Stacking multipliers**: Combines with other damage boosts
- **STAB interaction**: Multiplies with Same Type Attack Bonus
- **Choice items**: Stacks with Choice Band/Specs
- **Weather effects**: Combines with sun boosts to Grass moves
- **Ability suppression**: Disabled by Mold Breaker effects

### Damage Calculation
**Healthy (>1/3 HP)**: Base damage x 1.3 x other modifiers
**Low HP (<=1/3 HP)**: Base damage x 1.8 x other modifiers

Example with 100 BP Grass move:
- Healthy: 100 x 1.3 = 130 effective power
- Low HP: 100 x 1.8 = 180 effective power

### Strategic Implications
- **Late-game sweeper**: Becomes extremely dangerous at low HP
- **Grass STAB synergy**: Incredible on Grass-type attackers
- **Off-type coverage**: Useful for non-Grass types using Grass moves
- **Risk/reward**: Need to manage HP carefully for maximum benefit
- **Priority moves**: Grass-type priority moves get massive boost when low

### Compatible Moves
Forest Rage boosts all Grass-type moves including:
- **Physical**: Wood Hammer, Power Whip, Seed Bomb, Leaf Blade
- **Special**: Leaf Storm, Energy Ball, Giga Drain, Solar Beam
- **Status**: No boost to non-damaging moves
- **Z-moves**: Boosts Grass-type Z-moves when applicable
- **Multi-hit**: Boosts each hit of Bullet Seed, etc.

### Common Users
- **Grass-type sweepers**: Maximum synergy with STAB
- **Mixed attackers**: Using both physical and special Grass moves
- **Coverage users**: Non-Grass types with strong Grass coverage
- **Pivot Pokemon**: Can use Grass moves for utility and damage

### Competitive Applications
- **Endgame closer**: Devastating in late-game scenarios
- **Wallbreaker**: Punches through defensive cores when low
- **Revenge killer**: Can revenge kill with priority Grass moves
- **Setup sweeper**: Combines well with stat-boosting moves
- **Weather abuse**: Excellent in sun teams for Solar Beam

### Counters and Limitations
- **Type immunity**: Useless against non-Grass moves
- **HP management**: Need to reach low HP for maximum power
- **Grass resistances**: Steel, Fire, Flying, Bug, Dragon, Grass resist
- **Priority moves**: Vulnerable to faster priority when low
- **Healing**: Healing above threshold reduces power

### Synergies
- **Sun teams**: Solar Beam becomes incredibly powerful
- **Life Orb**: Helps reach low HP threshold while boosting damage
- **Substitute**: Can help manage HP while maintaining offensive threat
- **Growth**: Stat boosts stack with ability's damage boost
- **Chlorophyll**: Speed boost in sun pairs with damage boost

### Related Abilities
- **Overgrow** (Standard 1.5x boost at low HP for Grass moves)
- **Hellblaze** (Fire-type equivalent: 1.3x/1.8x multipliers)
- **Riptide** (Water-type equivalent: 1.3x/1.8x multipliers)
- **Gladiator** (Fighting-type equivalent: same system)
- **Purgatory** (Ghost-type equivalent: same multiplier system)

### Version History
- Elite Redux exclusive ability
- Uses enhanced BOOSTED_SWARM_MULTIPLIER system
- More powerful than standard type-boosting abilities
- Part of the escalating damage ability family
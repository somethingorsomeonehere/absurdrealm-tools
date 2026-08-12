---
id: 276
name: Vengeance
status: reviewed
character_count: 74
---

# Vengeance - Ability ID 276

## In-Game Description
"Boosts Ghost-type moves by 1.2x, or 1.5x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Ghost-type moves by 20%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Type-Specific Boost**: Only affects Ghost-type moves
- **Dual Power Levels**: 
  - Normal: 1.2x damage multiplier (20% boost)
  - Low HP: 1.5x damage multiplier (50% boost)
- **HP Threshold**: Enhanced boost activates when HP <= 33% of maximum HP
- **Calculation**: HP threshold is calculated as `gBattleMons[battler].maxHP / 3`

### Technical Implementation
```c
constexpr Ability Vengeance = {
    .onOffensiveMultiplier = SWARM_MULTIPLIER(TYPE_GHOST),
};

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

### Activation Conditions
- Must use a Ghost-type move
- Works on both physical and special Ghost-type moves
- Activates on direct damage moves and status moves that deal damage
- Does not affect non-damaging Ghost-type moves

### Affected Moves (Ghost-type)
All Ghost-type moves that deal damage, including but not limited to:
- Shadow Ball, Shadow Claw, Phantom Force
- Hex, Shadow Punch, Poltergeist
- Astral Barrage, Spectral Thief, Moongeist Beam
- And all other offensive Ghost-type moves

### Interactions with Other Mechanics
- **STAB**: Stacks multiplicatively with Same Type Attack Bonus (1.5x)
- **Type Effectiveness**: Stacks with super effective damage
- **Items**: Stacks with damage-boosting items like Spell Tag (+20% Ghost moves)
- **Weather/Terrain**: No direct interactions
- **Critical Hits**: Boost applies before critical hit calculation

### Strategic Implications
- **Risk vs Reward**: Higher damage potential at low HP encourages aggressive play
- **HP Management**: Players may intentionally take damage to reach the threshold
- **Late-Game Power**: Becomes more threatening as the battle progresses
- **Synergy Potential**: Works well with recovery moves and defensive strategies

### Example Damage Calculations
**Scenario**: Level 50 Pokemon with 120 Attack using Shadow Claw (70 BP) against neutral target
- **Full HP**: 70 x 1.2 x 1.5 (STAB) = 126 effective BP
- **Low HP**: 70 x 1.5 x 1.5 (STAB) = 157.5 effective BP
- **Damage Increase**: ~25% more damage when threshold is reached

### Common Users
Notable Pokemon with Vengeance ability:
- Ghost-type evolution lines (primary ability)
- Several Pokemon as innate ability (always active)
- Mixed offensive/defensive Ghost-types
- Pokemon with access to recovery moves for HP management

### Competitive Usage Notes
- **Tier Placement**: Common on mid-tier Ghost-types
- **Team Role**: Offensive Ghost-type attackers and revenge killers
- **Timing**: Most effective in mid-to-late game scenarios
- **Prediction**: Opponents may avoid bringing user to low HP threshold

### Counters
- **Type Resistances**: Dark-types resist Ghost moves
- **Immunities**: Normal and Fighting types are immune to Ghost moves
- **Abilities**: Wonder Guard, Flash Fire (doesn't apply but similar concept)
- **Priority**: Fast priority moves can KO before threshold benefit
- **Status**: Sleep, paralysis, and other status conditions limit effectiveness

### Synergies
- **Recovery Moves**: Roost, Recover for HP threshold manipulation
- **Substitute**: Protects while reaching optimal HP range
- **Focus Sash/Sturdy**: Guarantees survival to reach low HP threshold
- **Spell Tag**: Additional Ghost-type move boost
- **Life Orb**: More damage but also helps reach HP threshold faster

### Version History
- **Elite Redux**: Introduced as ability ID 276
- **Implementation**: Uses standard SWARM_MULTIPLIER template for consistency
- **Balance**: Same power levels as other type-specific Swarm abilities
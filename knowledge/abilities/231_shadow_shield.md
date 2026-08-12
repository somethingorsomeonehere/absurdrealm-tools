---
id: 231
name: Shadow Shield
status: reviewed
character_count: 113
---

# Shadow Shield - Ability ID 231

## In-Game Description
"At full HP, halves damage taken from attacks"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Shadow Shield halves damage from all attacks when at full HP. Multiplicative with other damage reduction sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shadow Shield is a defensive ability that provides a 50% damage reduction when the Pokemon is at full HP. It shares the same implementation as Multiscale from the official games.

### Activation Conditions
- **HP Requirement**: Must be at exactly 100% HP (full HP)
- **Damage Type**: Applies to all direct damaging moves
- **Automatic**: No manual activation required

### Technical Implementation
```cpp
constexpr Ability ShadowShield = {
    .onDefensiveMultiplier = Multiscale.onDefensiveMultiplier,
};

// From Multiscale implementation:
.onDefensiveMultiplier =
    +[](ON_DEFENSIVE_MULTIPLIER) {
        if (BATTLER_MAX_HP(battler)) MUL(.5);
    },
```

### Numerical Values
- **Damage Reduction**: 50% (multiplies incoming damage by 0.5)
- **HP Threshold**: Must be at maximum HP (100%)
- **No Partial Scaling**: Either full protection (50% reduction) or no protection

### Complete List of Affected Moves
- **All Physical Moves**: Any move that deals physical damage
- **All Special Moves**: Any move that deals special damage
- **Multi-Hit Moves**: Each hit is reduced by 50% while at full HP
- **Fixed Damage Moves**: Even moves like Dragon Rage and Sonic Boom are reduced
- **Critical Hits**: Still reduced by 50% when at full HP

### Interactions with Other Abilities/Mechanics
- **Breakable**: Can be suppressed by Mold Breaker, Turboblaze, and Teravolt
- **Stacks Multiplicatively**: Works with other damage reduction (Reflect, etc.)
- **Type Resistances**: Combines with type effectiveness multipliers
- **Items**: Stacks with damage-reducing items and berries
- **Does Not Affect**: Status damage, weather damage, entry hazards, recoil

### Strategic Implications
- **Exceptional Lead Ability**: Provides immediate bulk for setting up or pivoting
- **Healing Synergy**: Pairs excellently with recovery moves like Roost, Recover
- **Pivot Potential**: Allows safe switching and momentum control
- **Setup Opportunity**: Grants extra turns for stat boosts or field effects

### Example Damage Calculations
```
Base Scenario: 252 Atk Garchomp Earthquake vs 252 HP Lugia
- Without Shadow Shield: 204-240 (48.8 - 57.4%) 
- With Shadow Shield: 102-120 (24.4 - 28.7%)

Critical Hit Scenario: 252 Atk Garchomp Earthquake (Crit) vs 252 HP Lugia  
- Without Shadow Shield: 306-360 (73.2 - 86.1%)
- With Shadow Shield: 153-180 (36.6 - 43.1%)
```

### Common Users
Based on the protobuf data, Shadow Shield appears as an innate ability on several Elite Redux Pokemon, typically high-tier legendary or pseudo-legendary Pokemon that benefit from the defensive utility.

### Competitive Usage Notes
- **Priority Target**: Opponents will prioritize chip damage to break the shield
- **Entry Hazard Weakness**: Stealth Rock and other hazards immediately disable the ability
- **Weather Vulnerability**: Sandstorm and hail damage removes protection
- **Status Immunity**: Does not prevent status conditions, only damage reduction

### Counters
- **Entry Hazards**: Stealth Rock, Spikes, Toxic Spikes disable on entry
- **Weather Damage**: Sandstorm, hail, and other passive damage
- **Multi-Hit Moves**: While each hit is reduced, they can break the shield quickly
- **Ability Suppression**: Mold Breaker variants ignore the protection
- **Chip Damage**: Any source of gradual damage removal

### Synergies
- **Recovery Moves**: Roost, Recover, Moonlight for shield restoration
- **Leftovers/Healing Items**: Passive healing to maintain full HP
- **Substitute**: Can be used after taking damage to potentially heal back
- **Heavy-Duty Boots**: Prevents entry hazard damage that would break shield
- **Magic Guard**: Prevents passive damage that would break the shield

### Version History
Shadow Shield is implemented in Elite Redux as an enhanced version of the official Multiscale ability, maintaining the same core 50% damage reduction mechanic when at full HP. The ability serves as a powerful defensive tool in the expanded ability system.
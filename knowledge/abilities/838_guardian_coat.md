---
id: 838
name: Guardian Coat
status: reviewed
character_count: 298
---

# Guardian Coat - Ability ID 838

## In-Game Description
Blocks weather dmg and powders. Takes -20% physical damage.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Provides immunity to weather damage from Sandstorm and Hail, and blocks all powder moves including Sleep Powder, Stun Spore, Poison Powder, Spore, Cotton Spore, Rage Powder, Powder, and Magic Powder. Also reduces incoming physical  damage by 20%. Multiplicative with other damage reduction sources.

## Detailed Mechanical Explanation

### Implementation Details

### Source Code Location
- **Definition**: `src/abilities.cc` (line ~9666)

### Key Properties
```cpp
constexpr Ability GuardianCoat = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_PHYSICAL(move)) MUL(.8);
        },
    .breakable = TRUE,
    .powderImmune = TRUE,
    .sandImmune = TRUE,
    .hailImmune = TRUE,
};
```

### Mechanics Breakdown

1. **Physical Damage Reduction**
   - Applies a 0.8x multiplier to all incoming physical moves
   - Calculated during damage calculation phase
   - Stacks multiplicatively with other damage modifiers

2. **Weather Immunity**
   - `sandImmune = TRUE`: Prevents sandstorm damage at end of turn
   - `hailImmune = TRUE`: Prevents hail damage at end of turn
   - Does NOT affect weather-boosted moves (e.g., Solar Beam in sun)

3. **Powder Move Immunity**
   - `powderImmune = TRUE`: Blocks all powder-based moves
   - Affected moves include: Sleep Powder, Stun Spore, Poison Powder, Rage Powder, Spore, Cotton Spore
   - Powder moves fail completely against this ability

4. **Breakable Property**
   - `breakable = TRUE`: Can be ignored by Mold Breaker and similar abilities
   - When broken, all protections are removed

### Interaction Notes
- Does not protect against special moves (only physical damage reduction)
- Weather immunity only applies to residual damage, not weather-boosted attacks
- Powder immunity provides complete protection, not just status immunity
- Physical damage reduction applies after type effectiveness calculation

### Competitive Usage
Guardian Coat is excellent for defensive Pokemon that need protection from multiple threats. The combination of weather immunity and powder immunity makes it valuable in various metagames, while the physical damage reduction provides consistent defensive utility. Best suited for Pokemon that can handle special attackers through other means.
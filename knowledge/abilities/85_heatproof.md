---
id: 85
name: Heatproof
status: reviewed
character_count: 92
---

# Heatproof - Ability ID 85

## In-Game Description
Halves damage taken from Fire-type moves. Takes no burn damage.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Halves damage from Fire-type moves. Immune to burn damage and Attack drops from burn status. 

## Detailed Mechanical Explanation
**Heatproof** provides comprehensive protection against Fire-type attacks and burn effects, but with a crucial distinction regarding burn status.

### Core Mechanics

#### Fire Damage Resistance
- Halves damage taken from Fire-type moves via `.onDefensiveMultiplier` with `RESISTANCE(.5)`
- Applies to all Fire-type attacks regardless of category (physical/special/status)

#### Burn Protection (Critical Distinction)
1. **Burn Damage Immunity**: Prevents end-of-turn burn damage (explicit check in `ENDTURN_BURN` case)
2. **Attack Drop Negation**: Prevents the Attack stat drop from burn status (`.negatesBurnAtkDrop = TRUE`)
3. **Status vs Effects**: **CAN still receive burn status condition** but suffers no consequences

### Burn Status vs Burn Effects
**Key Finding**: Unlike true burn-immune abilities, Heatproof does NOT prevent burn status itself.

#### Comparison with True Burn-Immune Abilities
Abilities that actually prevent burn status:
- **Water Veil**: Has `onStatusImmune` with `CHECK(status & CHECK_BURN)`
- **Water Bubble**: Has `onStatusImmune` with `CHECK(status & CHECK_BURN)`
- **Thermal Exchange**: Has `onStatusImmune` with `CHECK(status & CHECK_BURN)`

#### Heatproof Implementation
```cpp
// Does NOT have onStatusImmune for burn
constexpr Ability Heatproof = {
    .onDefensiveMultiplier = RESISTANCE(.5), // vs Fire moves
    .negatesBurnAtkDrop = TRUE,              // no Attack drop
    // Missing: onStatusImmune for burn status
};
```

### Practical Implications
1. **Status moves** like Will-O-Wisp can still inflict burn on Heatproof Pokemon
2. **Flame Orb** can still activate and give burn status
3. **Guts ability** can still activate from the burn status
4. **Facade** would still get its power boost from burn status
5. **Status cures** like Pecha Berry would still work to remove the burn

### Strategic Applications
- Excellent against Fire-type attackers (50% damage reduction)
- Can safely absorb Will-O-Wisp without suffering consequences
- Synergizes well with status-dependent abilities that benefit from burn
- Provides defensive utility without completely negating status-based strategies

The ability is unique among burn-related abilities - it provides comprehensive protection against burn's harmful effects while still allowing the status condition itself, making it particularly interesting for strategies involving status-dependent moves and abilities.

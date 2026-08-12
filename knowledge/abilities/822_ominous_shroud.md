---
id: 822
name: Ominous Shroud
status: reviewed
character_count: 245
---

# Ominous Shroud - Ability ID 822

## In-Game Description
Phantom + Shadow Shield.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Ghost to user's current typing. Retains Ghost typing even upon losing the ability, going away only when switching out. Halves damage from all attacks when at full HP. Multiplicative with other damage reduction sources.

## Detailed Mechanical Explanation

### Mechanical Implementation

Ominous Shroud is a combination ability that merges two distinct effects:

### Phantom Component (onEntry)
- **Function:** Adds Ghost type to the Pokemon upon entering battle
- **Implementation:** `AddBattlerType(battler, TYPE_GHOST)`
- **Effect:** The Pokemon gains Ghost typing as a third type (stored in `type3` slot)
- **Persistence:** Remains active throughout the entire battle
- **Interaction:** Only adds Ghost type if the Pokemon doesn't already have it

### Shadow Shield Component (onDefensiveMultiplier)
- **Function:** Reduces incoming damage by 50% when at full HP
- **Implementation:** `if (BATTLER_MAX_HP(battler)) MUL(.5)`
- **Condition:** Only active when the Pokemon is at maximum HP
- **Breakable:** Yes - this defensive bonus can be negated by Mold Breaker-like abilities

## Battle Interactions

### Type Addition Mechanics
1. **Ghost Type Addition:** Immediately upon entering battle, the Pokemon gains Ghost typing
2. **Type Immunities:** Gains immunity to Normal and Fighting moves (standard Ghost-type immunity)
3. **Type Weaknesses:** Becomes weak to Ghost and Dark moves
4. **STAB Bonus:** Can now receive STAB on Ghost-type moves if learned

### Damage Reduction Mechanics
1. **Full HP Requirement:** Must be at exactly maximum HP for damage reduction
2. **All Move Types:** Affects physical, special, and status moves that deal damage
3. **Multiplicative Reduction:** 50% damage reduction applies after type effectiveness calculations
4. **Loss Condition:** Any HP loss removes the defensive bonus until HP is restored to maximum

## Strategic Applications

### Offensive Benefits
- **STAB Ghost Moves:** Enhanced Ghost-type move damage if the Pokemon learns them
- **Type Coverage:** Access to Ghost-type immunities and resistances

### Defensive Benefits
- **Initial Bulk:** Extreme durability on the first hit received
- **Switch-In Safety:** Safer entry against predicted attacks
- **Setup Opportunities:** Can survive strong attacks while setting up

### Counterplay
- **Multi-Hit Moves:** First hit removes damage reduction, subsequent hits deal full damage
- **Residual Damage:** Entry hazards, weather, or status conditions remove the damage reduction
- **Mold Breaker:** Abilities that ignore opponent abilities negate the damage reduction component
- **Ghost/Dark Coverage:** The added Ghost typing creates new weaknesses to exploit

## Related Abilities

- **Phantom:** Provides only the Ghost-type addition component
- **Shadow Shield:** Provides only the damage reduction at full HP component
- **Multiscale:** Similar damage reduction mechanic (Shadow Shield is based on Multiscale)
- **Disguise:** Another defensive ability that prevents damage, but works differently

## Pokemon Distribution

This ability is designed for Pokemon that benefit from both defensive bulk and Ghost-type properties, typically used on bulky setup sweepers or defensive pivots that can leverage the temporary damage reduction.
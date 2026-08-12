---
id: 116
name: Solid Rock
status: reviewed
character_count: 106
---

# Solid Rock - Ability ID 116

## In-Game Description
"Takes 35% less damage from Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Reduces damage from super-effective moves by 35% (applies a 0.65 multiplier)
- Only affects moves with type effectiveness of 2.0x or higher
- The ability is "breakable" - can be negated by moves like Moldbreaker, Turboblaze, or Teravolt
- Does not affect moves that are already reduced by other factors

**Technical Implementation:**
- Uses the same defensive multiplier system as Filter ability
- Applied during damage calculation after type effectiveness is determined
- Stacks multiplicatively with other damage reduction effects
- Activation occurs automatically when hit by super-effective moves

**Strategic Applications:**
- Essential for defensive Pokemon weak to common offensive types
- Particularly valuable on Pokemon with multiple type weaknesses
- Helps tanks survive powerful super-effective attacks
- Synergizes well with recovery moves and defensive stat investments
- Can turn 2HKOs into 3HKOs against super-effective attacks

**Breakable Nature:**
- Abilities like Moldbreaker, Turboblaze, and Teravolt ignore Solid Rock
- Moves that ignore abilities will bypass this protection
- Can be role-played, skill-swapped, or otherwise manipulated
- Suppressed by Gastro Acid or similar ability-suppressing effects

**Pokemon Commonly Associated:**
- Typically found on Rock, Ground, and Steel-type defensive Pokemon
- Rhyperior, Aggron, and similar bulky defenders benefit greatly
- Complements high HP and Defense stats for maximum survivability
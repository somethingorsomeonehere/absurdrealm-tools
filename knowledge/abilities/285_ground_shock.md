---
id: 285
name: Ground Shock
status: reviewed
character_count: 78
---

# Ground Shock - Ability ID 285

## In-Game Description
"Target Grounds aren't immune to Electric but resist it instead."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ground Shock allows Electric moves to hit Ground-type Pokemon for 0.5x damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

Ground Shock fundamentally alters the type effectiveness system for Electric vs Ground matchups. Normally, Electric-type moves have 0x effectiveness against Ground-type Pokemon (complete immunity). This ability modifies that interaction to 0.5x effectiveness (resistance).

**Technical Implementation:**
- Triggers on `onTypeEffectiveness` hook
- Checks if moveType == TYPE_ELECTRIC and defType == TYPE_GROUND
- Sets damage modifier to 0.5x (UQ_4_12(.5) in the code)
- Only activates when no other modifier is already present

**Practical Effects:**
- Electric moves can now damage Ground-type Pokemon
- Damage is reduced to 50% of normal effectiveness
- Applies to all Electric-type attacks (Thunder, Thunderbolt, Discharge, etc.)
- Does not affect other type interactions
- Ground types retain all other resistances and immunities

**Strategic Implications:**
- Makes Ground-type Pokemon vulnerable to Electric attacks for the first time
- Provides counterplay against traditionally safe Ground-type switch-ins
- Electric-type Pokemon gain coverage against Ground types
- Ground types are no longer perfect Electric counters but maintain some defensive utility

**Interaction Notes:**
- Does not stack with other type effectiveness modifiers
- The ability must be present on the attacking Pokemon to take effect
- Works in all battle formats and scenarios
- Compatible with moves that have secondary effects (paralysis chance remains normal)
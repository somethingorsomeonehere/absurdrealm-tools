---
id: 760
name: Acidic Slime
status: reviewed
character_count: 172
---

# Acidic Slime - Ability ID 760

## In-Game Description
"Corrosion + Poison STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Poison-type moves become super effective against Steel-type Pokemon. Additionally, this Pokemon can inflict poison status on any type. Also gives STAB to Poison-type moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

Acidic Slime is a hybrid ability that combines the effects of Corrosion with additional Water-type STAB functionality.

### Core Mechanics

**Water-type STAB:**
- All Water-type moves receive STAB (Same Type Attack Bonus)
- Damage multiplier: 1.5x for Water moves
- Applied regardless of the user's actual typing

**Corrosion Effects:**
- Poison-type moves hit Steel-type Pokemon for 2x damage instead of immunity
- Can inflict poison status on any type, including Steel and Poison types
- Bypasses normal type-based status immunities for poison

### Technical Implementation

```cpp
constexpr Ability AcidicSlime = {
    .onStab = +[](ON_STAB) -> int { return moveType == TYPE_WATER; },
    .onTypeEffectiveness = Corrosion.onTypeEffectiveness,
    .onCanStatusType = Corrosion.onCanStatusType,
};
```

The implementation references the existing Corrosion ability for type effectiveness and status mechanics while adding Water STAB.

### Type Effectiveness Changes

**Against Steel Types:**
- Poison moves: 0x to 2x damage
- All other type interactions remain unchanged

### Status Infliction

**Poison Status:**
- Can poison Steel types (normally immune)
- Can poison Poison types (normally immune)
- Works with moves like Toxic, Poison Gas, Sludge Bomb, etc.

### Affected Moves

**Water Moves (STAB):**
- Surf, Hydro Pump, Water Pulse, Scald, etc.
- All Water-type moves receive 1.5x damage boost

**Poison Moves (vs Steel):**
- Sludge Bomb, Toxic, Poison Jab, Gunk Shot, etc.
- Hit Steel types for 2x damage instead of immunity
- Can inflict poison status on Steel types

### Strategic Implications

**Offensive Utility:**
- Provides dual-type offensive coverage
- Water moves gain consistent power boost
- Poison moves become viable against Steel walls

**Status Utility:**
- Poison stall strategies work against all types
- Toxic becomes universally applicable
- Breaks traditional type-based immunities

### Example Damage Calculations

**Surf (90 BP) with Acidic Slime:**
- Base: 90 BP
- With STAB: 90 x 1.5 = 135 effective BP

**Sludge Bomb (90 BP) vs Steel type:**
- Normal: 0 damage (immune)
- With Acidic Slime: 90 x 2 = 180 effective BP

### Common Users

This ability is typically found on:
- Poison/Water dual types
- Pokemon with access to both Water and Poison move pools
- Bulky offensive Pokemon that benefit from status spreading

### Competitive Usage

**Strengths:**
- Excellent mixed offensive typing
- Breaks Steel-type defensive cores
- Universal poison spreading capability
- Strong against defensive teams

**Weaknesses:**
- No defensive benefits
- Doesn't boost non-Water/Poison moves
- Still vulnerable to Poison immunity from other sources

### Counters

**Direct Counters:**
- Magic Bounce (reflects status moves)
- Poison Heal (benefits from poison status)
- Natural Cure (removes poison on switch)
- Guts (benefits from status conditions)

**Indirect Counters:**
- Fast offensive Pokemon (bypass slow poison damage)
- Special walls with Poison immunity
- Taunt (prevents status moves)

### Synergies

**Item Synergies:**
- Black Sludge (HP recovery for Poison types)
- Choice items (boost either Water or Poison moves)
- Life Orb (boost both offensive types)

**Move Synergies:**
- Toxic + Water moves for stall
- Scald (Water + burn chance)
- Recovery moves to complement status spreading

**Team Synergies:**
- Toxic Spikes setters
- Pokemon that benefit from weakened Steel types
- Water/Poison offensive core partners

### Version History

Acidic Slime is a custom Elite Redux ability that combines established mechanics in a unique way, providing both offensive and utility benefits to create a versatile ability for specific archetypes.
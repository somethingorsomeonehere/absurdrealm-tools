---
id: 856
name: Molten Coat
status: reviewed
character_count: 232
---

# Molten Coat - Ability ID 856

## In-Game Description
Mineralize + Rock moves have 50% burn chance.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Rock-type moves and grants STAB for Rock-type moves, regardless of the user's typing. Rock-type moves have a 50% chance to burn when landing them. Multihits roll the activation chance on each hit.

## Detailed Mechanical Explanation

### Mechanical Analysis

### Core Components

**Mineralize Component (ATE_ABILITY):**
- Converts all Normal-type moves to Rock-type moves
- Grants STAB (Same Type Attack Bonus) for Rock-type moves
- Functions identically to abilities like Pixilate, Refrigerate, Aerilate

**Burn Chance Component:**
- Triggers on any Rock-type move that hits an opponent
- 50% chance (Random() % 2) to inflict burn status
- Only affects targets that can be burned (not Fire-types or already burned Pokemon)
- Uses `AbilityStatusEffectSafe` to apply the burn effect

### Implementation Details

```cpp
constexpr Ability MoltenCoat = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(moveType == TYPE_ROCK)
        CHECK(CanBeBurned(target))
        CHECK(Random() % 2)

        AbilityStatusEffectSafe(MOVE_EFFECT_BURN, battler, target);
        return TRUE;
    },
    ATE_ABILITY(TYPE_ROCK),
};
```

### Battle Interactions

**Move Conversion:**
- Normal-type moves become Rock-type and gain STAB
- Examples: Tackle to Rock-type Tackle, Body Slam to Rock-type Body Slam
- Converted moves maintain their original power and effects

**Burn Application:**
- Triggers after damage calculation if the move hits
- Respects burn immunity (Fire-types, already burned targets)
- Can be prevented by abilities like Water Veil or Magma Armor

**Strategic Implications:**
- Transforms utility Normal moves into offensive Rock moves
- Makes contact moves particularly dangerous due to burn chance
- Provides both immediate damage boost and long-term pressure
- Particularly effective against physical attackers due to Attack reduction from burn

### Counterplay

**Type Resistances:**
- Steel-types resist Rock moves (½x damage)
- Fire-types resist Rock moves and are immune to burn
- Flying-types are weak to Rock moves (2x damage)

**Status Immunity:**
- Fire-types cannot be burned
- Pokemon with Water Veil, Magma Armor prevent burns
- Safeguard protects team from status conditions

**Strategic Counters:**
- Special attackers are less affected by burn's Attack reduction
- Pokemon with Natural Cure can remove burn on switching
- Rapid Spin or Aromatherapy can cure burns

This ability is particularly effective on Pokemon with diverse movesets, as it converts utility Normal moves into powerful Rock attacks while adding the threat of burn status, making every successful hit potentially game-changing.
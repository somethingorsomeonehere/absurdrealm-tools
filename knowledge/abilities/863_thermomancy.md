---
id: 863
name: Thermomancy
status: reviewed
character_count: 126
---

# Thermomancy - Ability ID 863

## In-Game Description
"Pyromancy + Cryomancy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Multiplies the chance of inflicting burn or frostbite by 5x on all moves. Does not interact with Flame Body or Freezing Point.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Thermomancy is a combination ability that grants both Pyromancy and Cryomancy effects simultaneously. When a Pokemon with Thermomancy uses a move that can inflict burn or frostbite, the respective status chance is multiplied by 5.

### Implementation Details
```cpp
constexpr Ability Thermomancy = {
    .onModifyEffectChance =
        +[](ON_MODIFY_EFFECT_CHANCE) {
            Cryomancy.onModifyEffectChance(DELEGATE_MODIFY_EFFECT_CHANCE);
            Pyromancy.onModifyEffectChance(DELEGATE_MODIFY_EFFECT_CHANCE);
        },
};
```

The ability directly delegates to both Cryomancy and Pyromancy's `onModifyEffectChance` functions, providing both effects in a single ability.

### Effects Breakdown

**Burn Enhancement (Pyromancy component):**
- Multiplies burn chance by 5x for all moves with `MOVE_EFFECT_BURN`
- 10% burn chance to 50% burn chance
- 20% burn chance to 100% burn chance (guaranteed)
- Affects physical attack power (halves it when burned)

**Frostbite Enhancement (Cryomancy component):**
- Multiplies frostbite chance by 5x for all moves with `MOVE_EFFECT_FROSTBITE`
- 10% frostbite chance to 50% frostbite chance  
- 30% frostbite chance to 100% frostbite chance (guaranteed)
- Affects special attack power (halves it when frostbitten)

### Status Condition Details

**Burn:**
- Deals 1/16 max HP damage per turn
- Halves physical attack power
- Prevented by Fire-types and burn immunity
- Cured by various moves and items

**Frostbite:**
- Deals 1/16 max HP damage per turn
- Halves special attack power  
- Similar to freeze but allows action
- Cured by thaw moves, fire moves, and specific items

### Strategic Applications

**Offensive Utility:**
- Reliable dual status infliction across different move types
- Cripples both physical and special attackers
- Consistent chip damage from both status conditions
- Creates multiple win conditions in a single ability

**Defensive Benefits:**
- Reduces incoming physical damage (burn)
- Reduces incoming special damage (frostbite)
- Forces opponent to invest in status cures
- Provides multiple forms of passive damage

**Move Coverage:**
- Works with any burn-inducing move (Fire Fang, Lava Plume, etc.)
- Works with frostbite moves (Ice Fang, Bitter Malice)
- Can potentially affect both status types in the same battle

### Competitive Considerations

**Strengths:**
- Combines two powerful status abilities into one
- Provides incredible status pressure
- Effective against both physical and special attackers
- High versatility in team compositions

**Limitations:**
- Still subject to status immunity abilities
- Cannot burn Fire-types or frostbite certain immunities
- Requires moves that can inflict the respective status conditions
- Vulnerable to Substitute and Magic Guard

**Counterplay:**
- Status immunity abilities (Natural Cure, Guts, etc.)
- Type immunities (Fire-types for burn)
- Status cure moves (Heal Bell, Aromatherapy)
- Status cure items (Lum Berry, Pecha Berry)
- Magic Guard prevents damage portion

### Team Building Synergies

**Ideal Move Coverage:**
- Fire-type moves with burn chances
- Ice-type moves with frostbite chances
- Mixed attackers benefit most from dual status options
- Entry hazard support amplifies pressure

**Strategic Partners:**
- Pokemon that can cure ally status conditions
- Pressure/status spreading teammates
- Pokemon that benefit from opponent stat reductions

### Rarity and Balance
Thermomancy represents one of the most powerful combination abilities in Elite Redux, effectively granting two separate abilities in one slot. This makes it highly valuable for Pokemon that can learn moves with both burn and frostbite chances, creating unprecedented status control on the battlefield.
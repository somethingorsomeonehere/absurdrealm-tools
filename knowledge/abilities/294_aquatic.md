---
id: 294
name: Aquatic
status: reviewed
character_count: 149
---

# Aquatic - Ability ID 294

## In-Game Description
"Adds Water type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Water to the user's current typing. Retains Water typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Aquatic adds Water as a third type to the Pokemon when it enters battle, implemented through the `AddBattlerType()` function which assigns the type to the `type3` slot.

```cpp
constexpr Ability Aquatic = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_WATER); },
};

static int AddBattlerType(int battler, int type) {
    CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))
    
    gBattleMons[battler].type3 = type;
    PREPARE_TYPE_BUFFER(gBattleTextBuff2, gBattleMons[battler].type3);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAddedTheType);
    return TRUE;
}
```

### Activation Conditions
- Triggers automatically upon entering battle
- Only activates if the Pokemon doesn't already have Water type
- No activation requirements or conditions beyond entry

### Type Interactions Gained
**Resistances (0.5x damage taken):**
- Fire-type moves
- Steel-type moves  
- Ice-type moves
- Water-type moves

**Weaknesses (2x damage taken):**
- Electric-type moves
- Grass-type moves

**STAB (Same Type Attack Bonus):**
- All Water-type moves gain 1.5x power multiplier

**Status Immunities:**
- Burn status (Water types cannot be burned)

### Common Users
**Optional Ability:**
- **Tynamo** (#602) - Electric type fish Pokemon
- **Eelektrik** (#603) - Electric type eel evolution  
- **Stunfisk** (#618) - Ground/Electric type flatfish

**Innate Ability:**
- **Dragalge** (#691) - Poison/Dragon type with natural aquatic nature

### Strategic Implications
**Advantages:**
- Provides immediate type coverage expansion
- Grants Fire resistance to non-Water types
- Enables Water-type STAB for diverse movesets
- Burns become impossible

**Disadvantages:**  
- Adds Electric and Grass weaknesses
- Can make Electric types weak to Grass attacks
- Permanent type change cannot be removed

### Interactions with Other Abilities/Moves
- **Forest's Curse/Trick-or-Treat**: Can stack with other type-adding effects
- **Soak**: Will override this ability's Water type addition
- **Burn Heal/Aromatherapy**: Burn immunity makes these moves less necessary
- **Lightning Rod/Storm Drain**: Synergizes well by redirecting Electric/Water attacks

### Competitive Usage Notes
**Synergies:**
- Electric types gain Fire resistance while keeping Electric STAB
- Poison types can use Water moves for coverage
- Ground types can hit Fire types super effectively with Water moves

**Counters:**
- Grass-type attackers gain advantage
- Electric attacks become more threatening for Ground types
- Freeze-Dry ignores Water resistance

### Example Damage Calculations
**Stunfisk (Ground/Electric + Water via Aquatic):**
- Fire Blast: 0.5x damage (Water resistance)
- Grass Knot: 2x damage (new Grass weakness)  
- Surf with STAB: 1.5x power output

**Dragalge (Poison/Dragon + Water via innate Aquatic):**
- Flamethrower: 0.5x damage (Water resistance)
- Thunder: 2x damage (new Electric weakness)
- Hydro Pump with STAB: 1.5x power output

### Version History
- Introduced in Elite Redux as part of type-adding ability system
- Functions identically to other type-adding abilities like Half Drake (Dragon), Metallic (Steel), and Phantom (Ghost)
- Part of the expanded type system allowing Pokemon to have up to 3 types simultaneously
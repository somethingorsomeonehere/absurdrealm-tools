---
id: 310
name: Half Drake
status: reviewed
character_count: 151
---

# Half Drake - Ability ID 310

## In-Game Description
"Adds Dragon type to itself."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Dragon to the user's current typing. Retains Dragon typing even upon losing the ability, going away only when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Half Drake is a type-adding ability that grants the Pokemon an additional Dragon typing upon entering battle. This is implemented through the `AddBattlerType` function, which assigns Dragon-type to the Pokemon's `type3` slot.

### Activation Conditions
- Triggers automatically when the Pokemon enters battle
- Only activates if the Pokemon doesn't already have Dragon typing
- Cannot be suppressed by abilities like Mold Breaker
- Persists for the entire duration the Pokemon remains in battle

### Technical Implementation
```c
constexpr Ability HalfDrake = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_DRAGON); },
};

static int AddBattlerType(int battler, int type) {
    CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))
    
    gBattleMons[battler].type3 = type;
    PREPARE_TYPE_BUFFER(gBattleTextBuff2, gBattleMons[battler].type3);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAddedTheType);
    return TRUE;
}
```

The ability uses the `IS_BATTLER_OF_TYPE` macro which checks all three type slots:
```c
#define IS_BATTLER_OF_TYPE(battlerId, type) \
    ((gBattleMons[battlerId].type1 == type || \
      gBattleMons[battlerId].type2 == type || \
      gBattleMons[battlerId].type3 == type))
```

### Type Effectiveness Changes
**New Weaknesses (2x damage taken):**
- Ice-type moves
- Dragon-type moves  
- Fairy-type moves

**New Resistances (0.5x damage taken):**
- Fire-type moves
- Water-type moves
- Electric-type moves
- Grass-type moves

### STAB Benefits
- All Dragon-type moves gain 1.5x power multiplier
- Stacks with other offensive boosts
- Works with moves learned naturally or through TMs/breeding

### Strategic Implications
**Offensive Benefits:**
- Powerful Dragon-type STAB for coverage
- Access to moves like Dragon Pulse, Draco Meteor, Dragon Claw
- Enhanced wallbreaking potential against neutral targets

**Defensive Considerations:**
- Vulnerable to common Ice-type priority moves (Ice Shard)
- Weak to Fairy-type moves, reducing effectiveness against Fairy teams
- Dragon vs Dragon neutral damage creates prediction battles
- Gains valuable resistances to common attacking types

### Example Damage Calculations
**STAB Dragon Move:**
- Base 90 Dragon Pulse: 90 x 1.5 = 135 effective power
- Base 130 Draco Meteor: 130 x 1.5 = 195 effective power

**Defensive Multipliers:**
- Fire-type move dealing 100 damage to 50 damage taken
- Ice-type move dealing 100 damage to 200 damage taken

### Common Users
Notable Pokemon with Half Drake ability:
- **Charizard line** (changeable ability)
- **Hydreigon line** (innate ability)
- **Aurorus** (innate ability)
- **Tyrantrum** (innate ability) 
- **Absol line** (changeable ability)
- Various other Dragon and non-Dragon Pokemon

### Competitive Usage Notes
**Team Synergy:**
- Excellent on mixed offensive teams needing Dragon coverage
- Pairs well with Fire/Water/Electric/Grass moves for coverage
- Benefits from entry hazard support to pressure switchins

**Positioning:**
- Strong lead ability for immediate type advantage
- Good revenge killer with added Dragon STAB
- Effective wallbreaker against balanced teams

### Counters
**Direct Counters:**
- Steel-type Pokemon (resist Dragon moves)
- Fairy-type Pokemon (immune to Dragon, super effective back)
- Ice-type priority moves (exploit new weakness)
- Dedicated Dragon-type walls

**Strategic Counters:**
- Speed control to prevent setup
- Entry hazards to punish switching
- Status moves to cripple offensive potential

### Synergies
**Ability Combinations:**
- Dragon's Maw (Dragon move power boost)
- Adaptability (double STAB bonus)
- Sheer Force (boosted secondary effect moves)

**Move Synergies:**
- Dragon Dance (setup sweeping)
- Dragon-type coverage moves
- Fire/Water/Electric/Grass moves (utilize resistances)

**Item Synergies:**
- Dragonium Z (powerful Z-moves)
- Life Orb (raw power boost)
- Choice items (speed/power emphasis)

### Version History
- Added in Elite Redux as part of type-manipulation ability system
- Functions identically to other type-adding abilities (Ice Age, Aquatic, Metallic)
- Consistent with core type-addition mechanics across the game

### Related Abilities
- **Ice Age** (adds Ice typing)
- **Aquatic** (adds Water typing) 
- **Metallic** (adds Steel typing)
- **Phantom** (adds Ghost typing)
- **Dragonfly** (adds Dragon typing + Levitate)
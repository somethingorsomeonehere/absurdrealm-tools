---
id: 118
name: Honey Gather
status: reviewed
character_count: 169
---

# Honey Gather - Ability ID 118

## In-Game Description
"Has a 50% chance to find Honey each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gives a 50% chance to find Honey at the end of each turn if the Pokemon is not already holding an item. Honey acts as a Sitrus and Lum Berry for Pokemon related to bees.

## Detailed Mechanical Explanation
*For Discord/reference use*

**HONEY GATHER** is a utility ability that provides consistent item generation for resource management and emergency healing.

### Core Mechanics:
- **Trigger**: End of each turn
- **Activation Rate**: 50% chance per turn
- **Requirement**: Pokemon must not be holding an item
- **Item Generated**: Honey (ITEM_HONEY)
- **Honey Properties**: Restores 20 HP when consumed, sells for 100 Poké Dollars

### Activation Conditions:
1. **Turn End Trigger**: Activates during the end-of-turn phase
2. **No Item Requirement**: Pokemon must have an empty item slot
3. **Random Check**: 50% probability using the game's random number generator
4. **Success**: Pokemon receives a Honey item that can be used immediately

### Item Details - Honey:
- **Healing**: Restores 20 HP when consumed
- **Monetary Value**: Can be sold for 100 Poké Dollars
- **Usage**: Can be consumed during battle for emergency healing
- **Inventory**: Transfers to bag if gained outside battle

### Strategic Applications:
**Resource Generation**:
- Consistent income source through Honey sales
- Emergency healing item for extended battles
- Useful for Pokemon without reliable recovery moves

**Synergies**:
- Pairs well with item-consuming moves or abilities
- Benefits Pokemon that frequently use their held items
- Good on defensive Pokemon that can survive to generate multiple items

**Limitations**:
- Requires empty item slot to activate
- 50% chance means inconsistent activation
- Honey provides modest healing compared to other items
- No benefit if Pokemon already holds a better item

### Technical Implementation:
```c
constexpr Ability HoneyGather = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK_NOT(gBattleMons[battler].item)  // Must not hold item
        CHECK(Random() % 2)                   // 50% chance
        
        gBattleMons[battler].item = gLastUsedItem = ITEM_HONEY;
        BattleScriptPushCursorAndCallback(BattleScript_HoneyGatherActivates);
        return TRUE;
    },
};
```

### Competitive Viability:
**Pros**:
- Passive resource generation
- No setup required
- Works consistently throughout battle
- Provides both healing and monetary value

**Cons**:
- Requires giving up held item slot
- 50% activation rate can be unreliable
- Modest healing amount (20 HP)
- Competes with more powerful abilities

### Optimal Users:
- Defensive Pokemon that can survive multiple turns
- Pokemon without access to reliable recovery moves
- Team members used primarily for utility rather than combat
- Pokemon in casual play where resource management matters

### Comparison to Similar Abilities:
- **Pickup**: Activates after battle, can find various items
- **Harvest**: Restores consumed Berries, more reliable for healing
- **Frisk**: Reveals opponent items but doesn't generate resources

### Historical Context:
Honey Gather originated as a primarily overworld ability in the main series games, with different mechanics for in-battle vs. out-of-battle activation. In Elite Redux, it's been adapted as a consistent in-battle utility ability focused on resource generation and emergency healing.
---
id: 180
name: Symbiosis
status: reviewed
character_count: 103
---

# Symbiosis - Ability ID 180

## In-Game Description
"Passes own item to its ally if said ally consumes its item."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transfers the holder's item to an ally immediately after that ally consumes or uses up their held item. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**Symbiosis** is a support ability that activates in Double and Multi battles when specific conditions are met:

**Activation Conditions:**
- Must be in a Double, Triple, or Multi battle format (requires allies)
- An ally Pokemon on the same side must consume/use their held item
- The Symbiosis user must be holding an item to transfer
- Both Pokemon must be active on the field

**Mechanics:**
- Triggers immediately after ally's item is consumed, before any other effects
- Transfers the Symbiosis user's held item to the ally who just used their item
- Works with consumable items like Berries, Focus Sash, Air Balloon, etc.
- Does not activate if the ally's item is removed by moves like Knock Off or abilities like Magician
- The item must be "consumed" naturally (used up) rather than lost/stolen

**Items That Trigger Symbiosis:**
- All consumable Berries (Sitrus, Lum, type-resist berries, etc.)
- One-time use items (Focus Sash, Focus Band when activated, Choice items when switching moves)
- Air Balloon when popped
- Weakness Policy when activated
- Most held items that get "used up" during battle

**Items That Do NOT Trigger Symbiosis:**
- Items removed by Knock Off, Trick, Switcheroo
- Items stolen by Magician, Pickpocket, Covet, Thief
- Items destroyed by Incinerate
- Items that are permanently held (Mega Stones, Z-Crystals)

**Strategic Applications:**
- Support builds where one Pokemon holds recovery items for the team
- Passing Choice items to enable powerful sweepers
- Emergency item sharing (passing Sitrus Berry to low HP ally)
- Synergy with Unburden users (they consume item, get speed boost + new item)

**Battle Message:**
"{Pokemon name} passed its {item name} to {ally name} through {ability name}!"

**Implementation Status:**
Currently appears to be partially implemented in Elite Redux with message strings present but may need full mechanical implementation in the abilities system.
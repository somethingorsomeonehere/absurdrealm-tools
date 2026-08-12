---
id: 515
name: Retriever
status: reviewed
character_count: 104
---

# Retriever - Ability ID 515

## In-Game Description
"Automatically restores original held item when switching out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Retrieves original held item when switching out if not holding one. Must not be knocked out to activate.

## Detailed Mechanical Explanation

Retriever automatically restores a Pokemon's original held item when switching out, providing a unique form of item recovery that counters item removal and allows reuse of consumables.

### Mechanics
- **Trigger**: When the Pokemon switches out (must be alive)
- **Effect**: Restores the original held item if currently not holding one
- **Conditions**:
  - Pokemon must be alive when switching
  - Pokemon must have no current item
  - Pokemon must have had an item at battle start
- **Message**: "{POKEMON} retrieved its {ITEM}!"

### Code Implementation
Located in `src/abilities.cc` at line 5430:
- Uses onExit callback for switch-out trigger
- Retrieves original item from battle storage:
  - Player team: `gBattleStruct->itemStolen[index].originalItem`
  - Opponent team: `gBattleStruct->opposingOriginalItems[index]`
- Updates Pokemon's held item to the original

### Item Tracking System
The game maintains records of all Pokemon's original items throughout the battle, enabling restoration even after consumption, Knock Off, Trick, or Thief.

### Strategic Applications
- **Consumable Reuse**: Berries, Focus Sash, etc. can be used multiple times
- **Anti-Item Removal**: Counters Knock Off, Trick, and Thief strategies
- **Switching Synergy**: Encourages strategic switching to refresh items
- **Double Battle Value**: Can retrieve items for multiple team members

### Limitations
- Only activates on voluntary switches (not when fainting)
- Cannot retrieve if already holding an item
- Cannot generate new items - only restores battle start items


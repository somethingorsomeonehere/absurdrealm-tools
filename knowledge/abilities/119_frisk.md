---
id: 119
name: Frisk
status: reviewed
character_count: 161
---

# Frisk - Ability ID 119

## In-Game Description
"Checks foes' item and disables their items for two turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, reveals the opponents' items and prevents them from working for 2 turns. Does not prevent Mega Stones and other similar items from working.

## Detailed Mechanical Explanation
*For Discord/reference use*

Frisk is significantly enhanced in Elite Redux compared to vanilla Pokemon games:

**On Entry Effect:**
- Automatically activates when the Pokemon enters battle
- Scans all opposing Pokemon for held items
- If any opponent has an item, displays messages revealing what items they possess
- Simultaneously applies STATUS3_EMBARGO to all opposing Pokemon

**Embargo Effect:**
- Prevents affected Pokemon from using their held items for exactly 2 turns
- Items that normally activate automatically (like Leftovers) are also disabled
- Does not affect items that were already consumed before Frisk activated
- Timer decrements each turn until embargo expires

**Tactical Applications:**
- Ideal for disrupting item-dependent strategies (Choice items, healing items, etc.)
- Provides information advantage by revealing opponent's item choices
- Particularly effective against defensive Pokemon relying on Leftovers/recovery items
- Can shut down setup sweepers using Choice items or status orbs

**Technical Details:**
- Only affects opposing Pokemon (different sides in battle)
- Does not stack - multiple Frisk activations don't extend embargo duration
- Works in both single and double battles
- Embargo timer is stored in gVolatileStructs[battler].embargoTimer
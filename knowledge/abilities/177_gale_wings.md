---
id: 177
name: Gale Wings
status: reviewed
character_count: 56
---

# Gale Wings - Ability ID 177

## In-Game Description
"Flying-type moves get +1 priority at full HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to Flying-type moves when at full HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

Gale Wings is implemented using the GALE_WINGS_CLONE macro with TYPE_FLYING. The ability works through the onPriority callback, which triggers during move priority calculation.

**Conditions for activation:**
1. The move being used must be Flying-type (checked via GetTypeBeforeUsingMove)
2. The Pokemon must be at exactly full HP (checked via BATTLER_MAX_HP macro)

**Technical details:**
- GetTypeBeforeUsingMove accounts for type changes from abilities like Aerilate, Pixilate, etc.
- BATTLER_MAX_HP checks: gBattleMons[battlerId].hp == gBattleMons[battlerId].maxHP
- Returns +1 priority boost when both conditions are met
- Priority boost is additive with natural move priority (e.g., Quick Attack becomes +2)

**Important interactions:**
- Works with moves that become Flying-type through abilities
- Does not work if HP is reduced by even 1 point
- Stacks with other priority-modifying effects
- Can make normally negative priority moves (like Focus Punch) become neutral or positive

**Variants:**
Elite Redux includes several type-specific variants using the same macro:
- Dark Gale Wings (Dark-type moves)
- Water Gale Wings (Water-type moves) 
- Flaming Soul (Fire-type moves)
- Frozen Soul (Ice-type moves)
- Volt Rush (Electric-type moves)
- Early Grave (Ghost-type moves)
- Cute Antecedence (Fairy-type moves)

The macro design allows easy creation of priority-boosting abilities for different types while maintaining consistent behavior and HP requirements.
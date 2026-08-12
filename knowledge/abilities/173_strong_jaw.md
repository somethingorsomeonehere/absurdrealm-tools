---
id: 173
name: Strong Jaw
status: reviewed
character_count: 49
---

# Strong Jaw - Ability ID 173

## In-Game Description
"Boosts the power of bite/fang moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of biting and fang moves by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

Strong Jaw provides a 1.3x (30%) damage multiplier to all moves that have the FLAG_STRONG_JAW_BOOST flag set. The ability is implemented as an onOffensiveMultiplier callback that checks if the move being used has this flag and applies the multiplier if so.

### Affected Moves:
**Standard Moves:**
- Bite (60 BP Dark Physical)
- Crunch (80 BP Dark Physical) 
- Hyper Fang (80 BP Normal Physical)
- Super Fang (Variable BP Normal Physical)
- Fire Fang (65 BP Fire Physical)
- Ice Fang (65 BP Ice Physical)
- Thunder Fang (65 BP Electric Physical)
- Poison Fang (50 BP Poison Physical)
- Psychic Fangs (85 BP Psychic Physical)
- Jaw Lock (80 BP Dark Physical)
- Bug Bite (60 BP Bug Physical)
- Pluck (60 BP Flying Physical)
- Leech Life (80 BP Bug Physical)

**Elite Redux Custom Moves:**
- Iron Fangs (80 BP Steel Physical)
- Shadow Fangs (80 BP Ghost Physical)
- Lovely Bite (80 BP Fairy Physical)
- Jagged Fangs (80 BP Rock Physical)
- Draconic Fangs (80 BP Dragon Physical)
- Fertile Fangs (80 BP Grass Physical)
- Tectonic Fangs (80 BP Ground Physical)
- Kilobite (120 BP Electric Physical)
- Rip and Tear (120 BP Dark Physical)
- Terror Charge (120 BP Dark Physical)

### Mechanics:
- The multiplier is applied during damage calculation
- Stacks multiplicatively with other damage boosts (items, field effects, etc.)
- Does not affect status moves or moves without the flag
- Works with all damage-dealing moves that have the biting/fang theme
- The ability is not affected by Mold Breaker or similar abilities since it's a self-buff

### Competitive Impact:
Strong Jaw transforms Pokemon with access to biting moves into potent physical attackers. The 30% boost is significant enough to make formerly weak moves like Bite viable, while making already strong moves like Crunch and Psychic Fangs extremely powerful. Elite Redux's expanded movepool with custom fang moves gives Strong Jaw users excellent type coverage.

### Strategic Considerations:
- Best utilized on Pokemon with high Attack stats and good Speed
- Provides excellent type coverage through the variety of elemental fang moves
- Crunch is particularly valuable for its 100% accuracy and Defense drop chance
- Psychic Fangs removes screens while dealing boosted damage
- Custom moves like Kilobite and Rip and Tear provide devastating 120 BP options
---
id: 286
name: Ancient Idol
status: reviewed
character_count: 165
---

# Ancient Idol - Ability ID 286

## In-Game Description
"Uses Def and Sp. Def instead of Atk and Sp. Atk when attacking."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Physical moves use the Defense stat of the user instead of Attack for damage, while special moves use the Special Defense stat of the user instead of Special Attack. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Ancient Idol is a unique ability that fundamentally alters how a Pokemon calculates damage output. Instead of using the traditional Attack and Special Attack stats for damage calculations, Ancient Idol redirects the game to use the Pokemon's defensive stats instead. Damage modifiers still apply normally.

**Implementation Details:**
- **Physical Moves**: Uses Defense stat instead of Attack stat for all damage calculations
- **Special Moves**: Uses Special Defense stat instead of Special Attack stat for all damage calculations
- **Code Location**: `src/abilities.cc` - Uses `onChooseOffensiveStat` callback
- **Technical Implementation**: `*atkStatToUse = IS_MOVE_PHYSICAL(move) ? STAT_DEF : STAT_SPDEF;`

**Strategic Applications:**
- Transforms defensive tanks into powerful offensive threats
- Particularly effective on Pokemon with high defensive stats but low offensive stats
- Creates unique team building opportunities for defensive-oriented Pokemon
- Allows for dual-role Pokemon that can both tank hits and dish out damage

**Notable Pokemon with Ancient Idol:**
- **Runerigus**: High Defense (105) and Special Defense (105) make it a formidable attacker
- **Claydol**: Balanced defensive stats (105 Def, 120 SpDef) for mixed attacking
- **Bronzong**: Extremely high defensive stats (131 Def/SpDef) create massive damage potential
- **Various other defensive Pokemon**: Shuckle line, Steelix line, etc.

**Damage Calculation Impact:**
- A Pokemon with 150 Defense would calculate physical move damage as if it had 150 Attack
- A Pokemon with 120 Special Defense would calculate special move damage as if it had 120 Special Attack
- All other damage modifiers (items, abilities, type effectiveness, etc.) apply normally
- Does not affect defensive calculations - the Pokemon still uses its actual defensive stats for taking damage

**Synergy Considerations:**
- Works excellently with moves like Body Press (which already uses Defense for damage)
- Pairs well with defensive items like Leftovers, Assault Vest
- Benefits from defensive EV spreads and nature choices
- Can make unexpected threats out of typically defensive Pokemon
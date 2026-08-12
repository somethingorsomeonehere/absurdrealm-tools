---
id: 237
name: Ball Fetch
status: reviewed
character_count: 20
---

# Ball Fetch - Ability ID 237

## In-Game Description
"No effect in battle."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

No effect in battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

Ball Fetch is a unique out-of-battle utility ability that was introduced in Generation VIII. The ability serves as a resource conservation tool for players attempting to catch wild Pokemon.

### Mechanics:
- **Battle Effect**: None - the ability has no impact during actual battles
- **AI Rating**: 0 (confirmed in battle_ai_util.c)
- **Overworld Effect**: Retrieves the first Poké Ball used in a failed wild encounter
- **Activation Requirements**: 
  - Must be in the player's party (not necessarily in battle)
  - Only works in wild Pokemon encounters
  - Only retrieves the first Poké Ball used in the encounter
  - Ball must have failed to catch the Pokemon

### Implementation in Elite Redux:
In the Elite Redux codebase, Ball Fetch is defined in the ability list (proto/AbilityList.textproto) but appears to have no implemented functionality beyond its definition. The ability exists as ID 237 in the ability enum but lacks any actual mechanics implementation in the abilities.cc file.

### Current Status:
- Defined in ability enums and lists
- Has AI utility rating of 0
- No battle mechanics implemented
- No overworld mechanics detected in the codebase
- Appears to be a placeholder ability that exists for completeness but lacks functionality

This suggests that Ball Fetch may be intended for future implementation or exists as a legacy ability definition from the original game data but without the accompanying overworld mechanics that would make it functional.

### Notable Pokemon:
Ball Fetch is typically associated with Yamper and Boltund in the main series games, though the specific Pokemon that have this ability in Elite Redux would need to be confirmed by checking the SpeciesList.textproto file.
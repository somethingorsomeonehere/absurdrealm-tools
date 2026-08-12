---
id: 238
name: Cotton Down
status: reviewed
character_count: 156
---

# Cotton Down - Ability ID 238

## In-Game Description
"Lowers the Speed of all foes by one stage when hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Cotton Down triggers when the Pokemon is hit by any attack, lowering the Speed of ALL Pokemon by one stage. Activates multiple times against multihit moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

Cotton Down is a defensive ability that activates when the Pokemon takes damage from any move that hits. When triggered, it lowers the Speed stat of ALL opposing Pokemon by one stage (-1 stage = 50% Speed reduction).

### Key Mechanics:
- **Trigger Condition**: Must be hit by a damaging move (contact or non-contact)
- **Target Selection**: Affects ALL Pokemon on the opposing side(s)
- **Stat Change**: -1 Speed stage to each target
- **Doubles/Multi Effect**: Hits both opposing Pokemon simultaneously
- **Failure Cases**: 
  - Targets with already minimum Speed stats (-6) are unaffected
  - Does not trigger if the user faints from the hit
  - Targets that are absent/fainted are skipped

### Battle Implementation:
The ability uses the `onDefender` hook and calls `BattleScript_CottonDownActivates`, which:
1. Loops through all opposing battlers
2. Attempts to lower each one's Speed by 1 stage
3. Shows appropriate messages for successful stat drops or immunity
4. Respects stat drop immunities (Clear Body, etc.)

### AI Considerations:
The battle AI rates Cotton Down with a score of 3 and properly evaluates the Speed drop effects when deciding whether to attack the Pokemon with this ability.

### Pokemon with Cotton Down:
Several Pokemon have Cotton Down as either a regular ability or innate ability, including various fluffy/cotton-themed Pokemon like Mareep line, Swablu line, and others. It's often paired with Fluffy as an innate ability for thematic consistency.
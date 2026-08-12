---
id: 774
name: Corrupted Mind
status: reviewed
character_count: 229
---

# Corrupted Mind - Ability ID 774

## In-Game Description
"Psychic moves ignore resists and get 1.4x effect chance."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Psychic-type moves bypass type resistances and immunities, hitting for at least neutral damage regardless of the target's typing. Additionally, all secondary effects of Psychic moves have their activation chance increased by 40%.

## Detailed Mechanical Explanation
*For Discord/reference use*

Corrupted Mind is a dual-effect ability that enhances Psychic-type moves in two distinct ways:

**Type Effectiveness Override:**
- Uses `onTypeEffectiveness` hook to modify damage calculations
- Checks if the move type is Psychic (`TYPE_PSYCHIC`)
- If the effectiveness modifier is less than 1.0 (resistant or immune), it forces the modifier to exactly 1.0 (neutral damage)
- This allows Psychic moves to bypass type resistances from Steel, Psychic, and Dark types
- Importantly, it does NOT boost super-effective damage - it only prevents resisted damage

**Effect Chance Enhancement:**
- Uses `onModifyEffectChance` hook to boost secondary effect probabilities
- Multiplies the effect chance by 1.4 (40% increase) for all Psychic-type moves
- This affects any secondary effects like confusion, stat drops, or status conditions
- For example, Psychic's 10% chance to lower Sp. Def becomes 14%

**Technical Implementation:**
- Uses `UQ_4_12(1.0)` fixed-point arithmetic for precise damage calculations
- The ability is marked as `randomizerBanned = TRUE`, preventing it from appearing in randomizer modes
- Currently only found on Mega Slowking (Galarian) as an innate ability

**Strategic Impact:**
This ability makes Psychic-type attackers significantly more reliable against traditionally resistant targets, while also improving their utility through enhanced secondary effects. It's particularly powerful on Pokemon with strong Psychic movesets and diverse secondary effects.
---
id: 853
name: Purple Haze
status: reviewed
character_count: 127
---

# Purple Haze - Ability ID 853

## In-Game Description
Follow up with weakened Poison Gas after any move.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After using a move, follow up with a 20 BP Poison Gas (Poison, Special, 20% chance to poison, super effective on Flying-types). 

## Detailed Mechanical Explanation

Purple Haze (ID: 853) is a follow-up move ability that triggers after the user successfully uses any move. The ability automatically uses Poison Gas with 20 base power against the same target immediately after the original move resolves.

### Technical Mechanics

**Trigger Condition**: After any move is used by the Pokemon with Purple Haze
**Follow-up Move**: Poison Gas (normally 65 base power, reduced to 20 for this ability)
**Target**: Same as the original move (uses FOLLOWUP_STANDARD targeting)
**Activation**: Uses `UseAttackerFollowUpMove` function with the onAttacker callback

### Poison Gas Properties (When Triggered by Purple Haze)

- **Base Power**: 20 (reduced from normal 65)
- **Type**: Poison
- **Accuracy**: 100%
- **Effect**: 20% chance to poison (this is the effect_chance from Poison Gas, not modified by Purple Haze)
- **Target**: Varies based on original move target
- **Category**: Special
- **Additional**: Super effective against Flying-type Pokemon, hits both opponents in doubles

### Strategic Implications

Purple Haze provides consistent chip damage and poison pressure after every move. The 20% poison chance on the follow-up Poison Gas can accumulate significant passive damage over time. The ability is particularly strong on Pokemon that use non-damaging moves frequently, as it provides offensive presence regardless of the original move's damage output.


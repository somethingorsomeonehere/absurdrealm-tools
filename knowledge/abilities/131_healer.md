---
id: 131
name: Healer
status: reviewed
character_count: 179
---

# Healer - Ability ID 131

## In-Game Description
"30% chance to heal user or ally's status at the end of each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gives a 30% chance to cure status conditions at the end of each turn for both the user and their ally if they are out in a double battle. Makes 2 separate checks for each Pokemon.

## Detailed Mechanical Explanation
Healer is a supportive ability that provides passive status condition removal at the end of each turn. Here's how it works in detail:

### Activation Mechanics
- Triggers at the end of each turn during the end-turn ability phase
- Has a 30% chance to activate (rolled independently each turn)
- In single battles: Only attempts to cure the user's status
- In double battles: Can cure either the user OR the ally (not both with one activation)

### Battle Script Implementation
According to `BattleScript_HealerActivates` in the battle scripts:
1. The ability attempts to cure the partner's status first (`BS_ABILITY_PARTNER`)
2. Then attempts to cure the user's status (`BS_ABILITY_BATTLER`)
3. Updates status icons for any cured Pokemon
4. Displays the healing message

### Status Conditions Affected
Healer can cure all standard status conditions:
- Paralysis
- Burn
- Poison/Badly Poisoned
- Sleep
- Freeze

### Important Notes
- The 30% chance is rolled once per turn, not per affected Pokemon
- In doubles, both the user and ally could potentially be cured in the same turn if both have status conditions
- Does not prevent status conditions, only cures existing ones
- Activates even if the Pokemon with Healer is not statused itself
- Works through Substitute

### Strategic Considerations
- Particularly valuable in double battles where it can support allies
- Synergizes well with bulky Pokemon that can survive multiple turns
- Can help teammates that use Rest by potentially waking them early
- Less reliable than active status healing moves but provides passive support
- Combines well with the Caretaker ability (Healer + Friend Guard fusion)
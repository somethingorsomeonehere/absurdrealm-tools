---
id: 261
name: Curious Medicine
status: reviewed
character_count: 90
---

# Curious Medicine - Ability ID 261

## In-Game Description
"Resets its ally's stat changes on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Curious Medicine removes an ally's positive and negative stat changes on the user's entry.

## Detailed Mechanical Explanation
*For Discord/reference use*

Curious Medicine is a unique support ability that activates when the Pokemon enters battle in double battles only. Here's how it works:

**Activation Conditions:**
- Only works in double battles (2v2 format)
- The ally partner must be alive on the field
- The ally must have at least one stat change (positive or negative)

**Mechanics:**
- Uses `TryResetBattlerStatChanges(BATTLE_PARTNER(battler), RESET_ALL_STATS)`
- `RESET_ALL_STATS` = 0, which resets all stat modifications regardless of direction
- This affects all seven stats: Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, and Evasion
- Clears both positive boosts (like from Swords Dance) and negative drops (like from Intimidate)
- Returns the ally to neutral stat stages (0 for all stats)

**Strategic Uses:**
1. **Debuff Removal**: Clear Intimidate, Sticky Web, or other stat-lowering effects from your ally
2. **Reset Setup**: Remove your ally's setup moves if they're about to be KO'd and you want to pivot
3. **Cleanse Status**: Remove stat changes caused by moves like Overheat or Close Combat
4. **Double Battle Support**: Provides utility in doubles format where stat management is crucial

**Important Notes:**
- Only works in double battles - has no effect in singles
- Does not activate if the ally is already at neutral stats
- The ability user must successfully enter the field for activation
- Cannot be suppressed by abilities like Neutralizing Gas (though the reset effect still occurs)
- Triggers battle message: "Curious Medicine reset [ally's] stat changes!"

**Comparison to Similar Abilities:**
- Unlike White Smoke/Clear Body which prevent stat drops, this actively resets existing changes
- More targeted than Haze (which affects all Pokemon), only affecting the ally
- Provides more control than Natural Cure (which only affects the user and only removes status conditions)

The ability is particularly valuable in competitive double battles where stat control and positioning are key strategic elements.
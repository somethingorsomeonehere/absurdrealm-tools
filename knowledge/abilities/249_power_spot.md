---
id: 249
name: Power Spot
status: reviewed
character_count: 99
---

# Power Spot - Ability ID 249

## In-Game Description
"Grants a 1.3x boost to ally's attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Power Spot boosts allies' attack power by 30% in double battles. The user itself receives no boost. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Power Spot is a double battle support ability that provides a 1.3x damage multiplier to all attacks made by the user's ally. Key mechanics:

- **Ally-Only Boost**: The ability only affects allies, not the user itself (uses `APPLY_ON_ALLY_ONLY` flag)
- **30% Damage Increase**: Provides a 1.3x multiplier to all offensive moves used by allies
- **Universal Coverage**: Affects all move types - physical, special, and status moves that deal damage
- **Double Battle Exclusive**: Only functions in double battles where there are allies present
- **Persistent Effect**: The boost is always active as long as the Power Spot user is on the field
- **Stacks with Other Boosts**: Can combine with other damage multipliers like STAB, type effectiveness, etc.
- **Bypasses Protective Moves**: The boost applies even if the ally is behind Substitute or Light Screen/Reflect

Similar to Battery (which only boosts special moves), Power Spot provides comprehensive offensive support but works on all move types. The ability is particularly valuable for supporting powerful but slow attackers or enabling otherwise moderate attackers to reach important damage thresholds.

Implementation details:
- Uses the `onOffensiveMultiplier` callback with `MUL(1.3)`
- Applied via the `APPLY_ON_ALLY_ONLY` flag system
- Activates during damage calculation phase
- No activation message or popup
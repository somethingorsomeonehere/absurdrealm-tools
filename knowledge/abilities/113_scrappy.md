---
id: 113
name: Scrappy
status: reviewed
character_count: 124
---

# Scrappy - Ability ID 113

## In-Game Description
"Normal/Fighting can hit Ghosts. Immune to Intimidate/Scare."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user can land Normal and Fighting-type moves on Ghost-types for neutral damage. Grants immunity to Intimidate and Scare.

## Detailed Mechanical Explanation

Scrappy provides two distinct benefits:

1. **Type Effectiveness Override**: Normal and Fighting-type moves can hit Ghost-type Pokemon for neutral damage (1x effectiveness). This completely bypasses the normal immunity that Ghost types have to these move types.

2. **Taunt Immunity**: The Pokemon with Scrappy cannot be affected by Taunt or similar intimidation-based effects. This is implemented through the `tauntImmune = TRUE` flag.

The ability's type effectiveness modification is implemented as an `onTypeEffectiveness` handler that:
- Checks if the move type is Normal or Fighting
- Checks if the defending type is Ghost
- If both conditions are met and the modifier is currently 0 (immunity), it changes it to 1.0 (neutral damage)

This ability is particularly valuable for physical attackers who rely on Normal or Fighting-type coverage moves, as it removes one of the most common immunities in the game. The additional Taunt immunity provides extra utility in competitive battles where status moves are commonly used.

Note: The ability Mind's Eye uses the same type effectiveness handler as Scrappy, indicating they share this Ghost-hitting mechanic.
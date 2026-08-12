---
id: 598
name: Malicious
status: reviewed
character_count: 166
---

# Malicious - Ability ID 598

## In-Game Description
"Lowers the foe's highest Attack and Defense stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On switch-in, lowers all opposing Pokemon's highest offensive stat (Attack or Special Attack) and highest defensive stat (Defense or Special Defense) by 1 stage each. 

## Detailed Mechanical Explanation

The MALICIOUS ability triggers **on entry** (when the Pokemon switches into battle) using the `UseIntimidateClone` function system. It lowers **two specific stats** of all opposing Pokemon:

1. **Highest Attacking Stat** (either Attack or Special Attack, whichever is higher)
2. **Highest Defending Stat** (either Defense or Special Defense, whichever is higher)

The ability uses sophisticated stat calculation functions:
- **For Offensive Stats**: `GetHighestAttackingStatId()` compares only Attack vs Special Attack
- **For Defensive Stats**: `GetHighestDefendingStatId()` compares only Defense vs Special Defense
- **Stat Boosts Included**: The calculation includes current stat stage modifications due to the `STAT_USE_STAT_BOOSTS_IN_CALC` flag

## Trigger Conditions

- **On Entry**: Activates when the Pokemon switches into battle
- **Affects**: All opposing Pokemon (both in double battles)
- **No Immunity**: Standard Intimidate immunities don't apply since this targets different stats

## Numerical Effects

- **Stat Reduction**: 1 stage reduction for each targeted stat
- **Number of Stats**: Exactly 2 stats per opponent
- **Target Selection**: Dynamic based on opponent's current highest offensive and defensive stats

## Interactions

- **Stat Stage Modifications**: Takes into account current buffs/debuffs when determining "highest" stats
- **Double Battles**: Affects both opposing Pokemon simultaneously
- **Standard Intimidate**: Can stack with regular Intimidate effects
- **Clear Body/White Smoke**: These abilities would prevent the stat reduction

## Special Cases

- **Example 1**: Against a Pokemon with 120 Attack and 80 Special Attack, it would lower Attack (highest offensive stat)
- **Example 2**: Against a Pokemon with +2 Special Attack boost, the boosted Special Attack might become the "highest" and be targeted instead
- **Tied Stats**: Implementation uses consistent tie-breaking logic in the stat comparison functions

## Notes

- More versatile than standard Intimidate by adapting to each opponent's stat distribution
- Provides powerful entry control by weakening opponents' strongest capabilities
- Strategic value increases against mixed attackers and defensive walls
- Cannot be suppressed by abilities that block Intimidate specifically
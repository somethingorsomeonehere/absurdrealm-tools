# Individual Ability Documentation

This directory contains detailed mechanical explanations for individual abilities and innates.

## Filename Convention
All files follow the pattern: `{ability_id}_{ability_name_kebab_case}.md`

Examples:
- `123_ice_cold_hunter.md`
- `25_multiscale.md` 
- `23_shadow_tag.md`

## File Structure Template

Each ability file should contain:

```markdown
# {Ability Name}

**Ability ID**: {number}
**Type**: {Regular Ability | Innate}

**In-Game Description**: "{Exact description from the game}"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

{Extended description for in-game use. Write as continuous text without line breaks. Target 280-300 characters total. Keep concise due to GBA UI limits: 11 usable lines x 30 chars/line. Should explain core mechanics clearly for players.}

## Detailed Mechanical Explanation (Discord/Reference)

{Comprehensive explanation that can be copy-pasted to answer player questions on Discord. Can be much longer and more detailed than the in-game version. Include comparisons to similar abilities when relevant.}

## Trigger Conditions

{When exactly the ability activates - be very specific}

## Numerical Effects

{Exact percentages, multipliers, damage calculations. Be explicit about things like "100% damage on both hits" vs "25% on second hit"}

## Interactions

{How it works with other abilities, moves, items, weather, etc.}

## Special Cases

{Any conditional behavior or exceptions}

## Notes

{Any additional observations, synergies, or strategic considerations}
```

## Purpose

These files provide human-readable mechanical documentation without code snippets. They serve as the definitive reference for how each ability actually works in-game, verified through deep code analysis.
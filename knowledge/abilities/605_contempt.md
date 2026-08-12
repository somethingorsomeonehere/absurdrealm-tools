---
id: 605
name: Contempt
status: reviewed
character_count: 163
---

# Contempt - Ability ID 605

## In-Game Description
"Ignores stat stage changes when calculating damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ignores all the foes' stat stage changes during damage calculations. When the user has their stats lowered by another Pokemon, they raise their Attack by 2 stages.

## Detailed Mechanical Explanation

Contempt is an ability that ignores stat stage modifications during damage calculations, functioning identically to Unaware. Despite any descriptions suggesting additional effects, the current implementation only provides the stat-ignoring mechanic.

### Core Mechanics
- **Stat Ignore**: Completely ignores all stat stage changes during damage calculations
- **Universal Application**: Affects both offensive and defensive calculations
- **Pure Unaware**: Functions exactly like the standard Unaware ability
- **No Additional Effects**: Despite descriptions mentioning other properties, only Unaware is implemented

### Strategic Applications
- **Setup Counter**: Nullifies opponent setup strategies
- **Defensive Utility**: Ignores opponent's Attack boosts when taking damage
- **Offensive Consistency**: Damage output remains consistent regardless of opponent's defensive boosts
- **Meta Disruption**: Forces opponents to rely on base stats rather than setup

### Notable Interactions
- **Setup Moves**: Makes Swords Dance, Dragon Dance, etc. irrelevant for damage calculation
- **Item Boosts**: Still affected by items like Choice Band (not stat stages)
- **Ability Boosts**: Other ability multipliers still apply
- **STAB and Type Effectiveness**: These multipliers are unaffected
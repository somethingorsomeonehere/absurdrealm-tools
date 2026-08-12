---
id: 186
name: Dark Aura
status: reviewed
character_count: 116
---

# Dark Aura - Ability ID 186

## In-Game Description
"Boosts Dark moves by 1.33x for all while this Pokemon is out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All Dark-type moves for the user, their allies, and the opponent get a 1.33x boost. Boost is reversed by Aura Break. 

## Detailed Mechanical Explanation

**Basic Information:**
- **Ability ID**: 186
- **Name**: Dark Aura
- **Category**: Aura
- **Generation**: VI (Kalos)

### Core Functionality
Dark Aura is a field-affecting ability that provides a 1.33x (33%) damage multiplier to all Dark-type moves used by any Pokemon on the battlefield, similar to how weather conditions affect certain move types.

### Implementation Details
- **Trigger**: Active while the Pokemon with Dark Aura is on the field
- **Effect**: 1.33x damage multiplier for Dark-type moves from all Pokemon
- **Scope**: Affects both the user and opponents
- **Switch-in Message**: "{Pokemon} is radiating a dark aura!"

### Interactions
- **Aura Break**: When Aura Break is present on the field, Dark Aura's effect is reversed, reducing Dark-type move power to 0.75x instead of boosting it
- **Stacking**: Multiple Dark Aura abilities do not stack - the effect remains 1.33x regardless of how many Pokemon have the ability
- **Field Coverage**: The effect applies to all Pokemon on the battlefield, including opponents

### Code Implementation
```cpp
constexpr Ability DarkAura = {
    .onEntry = +[](ON_ENTRY) -> int { return SwitchInAnnounce(B_MSG_SWITCHIN_DARKAURA); },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType != TYPE_DARK) return;
            if (IsAbilityOnField(ABILITY_AURA_BREAK))
                MUL(.75);
            else
                MUL(1.33);
        },
    .onOffensiveMultiplierFor = APPLY_ON_ANY,
};
```

## Pokemon with Dark Aura

### Primary Users
- **Mega Absol**: Has Dark Aura as a regular ability choice
- **Mega Yveltal**: Has Dark Aura as a regular ability choice

### Innate Users
Several Pokemon have Dark Aura as an innate ability, meaning it's always active alongside their regular abilities:
- Various legendary and mythical Pokemon
- Certain custom/modified Pokemon in the Elite Redux hack

## Strategic Applications

### Offensive Strategies
- **Dark Spam Teams**: Build teams around powerful Dark-type moves like Knock Off, Sucker Punch, and Dark Pulse
- **Mixed Coverage**: Use Dark Aura to boost Dark-type coverage moves on non-Dark Pokemon
- **Priority Abuse**: Boost priority Dark moves like Sucker Punch for enhanced revenge killing

### Defensive Considerations
- **Double-Edged**: Remember that Dark Aura boosts opponent Dark moves too
- **Aura Break Counter**: Be aware that Aura Break can completely reverse the benefit
- **Team Synergy**: Consider how boosted Dark moves from opponents might affect your team

### Competitive Viability
- **High Impact**: 33% damage boost is substantial and affects all Dark moves
- **Field Control**: Changes the battle dynamic by making Dark moves universally stronger
- **Risk/Reward**: Provides benefits to both sides, requiring careful team construction

## Related Abilities
- **Fairy Aura**: Identical mechanics but for Fairy-type moves
- **Aura Break**: Directly counters both Dark Aura and Fairy Aura
- **Pixilate/Refrigerate/Aerilate**: Similar damage boosting concepts but for specific move conversions

## Notes
- Dark Aura is one of the signature abilities that defined Generation VI's introduction of "Aura" mechanics
- The ability creates a unique battlefield state where Dark-type moves become significantly more threatening
- In Elite Redux, the ability appears on various Pokemon beyond its original Yveltal exclusive status
- The 1.33x multiplier is applied after all other damage calculations, making it a pure 33% increase to final damage
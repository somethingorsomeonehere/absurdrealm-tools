---
id: 843
name: Fey Flight
status: reviewed
character_count: 290
---

# Fey Flight - Ability ID 843

## In-Game Description
Adds Fairy-type and levitates.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, adds Fairy to the user's current typing. Retains Fairy typing even upon losing the ability, going away only when switching out. The user is immune to Ground-type moves and other ground effects such as Spikes and terrains. Boosts the damage of Flying-type moves by 25%.

## Detailed Mechanical Explanation

### Mechanics Details
- **Type Addition**: Adds Fairy as type3 slot (does not replace existing types)
- **Levitation**: Provides complete Ground immunity and hazard avoidance
- **Breakable**: Can be suppressed by Mold Breaker-like abilities
- **Trigger**: Activates immediately upon entering battle

## Interactions
- Works with other type-changing abilities/moves
- Levitation can be negated by Gravity, Ingrain, or Iron Ball
- Mold Breaker bypasses both the type addition and levitation
- Does not stack with existing Fairy typing (no effect if already Fairy-type)

## Competitive Analysis
Fey Flight is an exceptional defensive ability that transforms a Pokemon's defensive profile. The Fairy typing alone is valuable for resisting common offensive types like Fighting and Dark, while the Ground immunity removes one of the most common offensive types entirely. This ability is particularly strong on Pokemon that appreciate both aspects - those weak to Ground benefit from the immunity, while those weak to Fighting or Dark appreciate the Fairy resistances. The combination can turn several 4x weaknesses into manageable 2x weaknesses or even resistances.

## Pokemon with This Ability
- **Merrykarp**: Has Fey Flight as an innate ability alongside Two Step and Festivities

## Code Implementation
```c
constexpr Ability FeyFlight = {
    .onEntry = FairyTale.onEntry,  // Adds Fairy type
    .breakable = TRUE,
    .levitate = TRUE,
};
```

The ability reuses FairyTale's onEntry function which calls AddBattlerType to add TYPE_FAIRY as the Pokemon's third type. The levitate flag provides all standard levitation benefits.
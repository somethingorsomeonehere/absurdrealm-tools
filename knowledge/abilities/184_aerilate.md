---
id: 184
name: Aerilate
status: reviewed
character_count: 92
---

# Aerilate - Ability ID 184

## In-Game Description
"Normal-type moves become Flying and Flying gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Normal-type moves become Flying-type and they receive STAB regardless of the Pokemon's type.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Type Conversion**: Converts all Normal-type moves to Flying-type
- **STAB Granting**: Grants STAB (Same Type Attack Bonus) on all Flying-type moves
- **Damage Boost**: Converted moves receive a 1.2x damage multiplier in addition to STAB

### Activation Conditions
- Only affects Normal-type moves when used by the Pokemon with this ability
- Must be the Pokemon's own moves (doesn't affect moves used via Metronome, etc.)
- Works on both physical and special Normal-type moves

### Technical Implementation
```cpp
constexpr Ability Aerilate = {
    ATE_ABILITY(TYPE_FLYING),
};

#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Complete List of Affected Moves
All Normal-type moves become Flying-type, including but not limited to:
- **Physical**: Body Slam, Double-Edge, Extreme Speed, Facade, Return, Frustration, Quick Attack, Tackle, Take Down
- **Special**: Hyper Voice, Boomburst, Swift, Hidden Power (when Normal), Weather Ball (when Normal)
- **Status moves**: Moves like Growl, Leer become Flying-type but don't benefit from damage boost

### Interactions with Other Abilities/Mechanics

#### Positive Synergies
- **Tough Claws**: Contact Normal moves converted to Flying still get 1.3x boost
- **Choice Items**: Flying-type moves now locked in benefit from conversion
- **Life Orb**: Flying moves get Life Orb boost
- **Flying Gem**: Can activate on converted Normal moves

#### Interactions with Opposing Abilities
- **Normalize**: Normalize would override Aerilate (moves become Normal, not Flying)
- **Protean/Libero**: User changes to Flying-type when using converted moves
- **Lightning Rod/Storm Drain**: Don't interact since Flying ≠ Electric/Water

#### Type Effectiveness Changes
- Normal moves that hit Rock/Steel/Electric neutrally now hit for super effective damage against Fighting/Bug/Grass
- Normal moves lose their inability to hit Ghost-types
- Normal moves become resisted by Rock/Steel/Electric types

### Strategic Implications

#### Offensive Applications
- **Hyper Voice**: Becomes a powerful 90 BP Flying-type spread move with 1.2x boost + STAB
- **Boomburst**: 140 BP Flying-type spread move becomes incredibly powerful
- **Return**: 102 BP physical Flying move with maximum happiness
- **Double-Edge**: High-power recoil move becomes Flying-type

#### Defensive Considerations
- Makes the user more predictable (Normal moves telegraphed as Flying)
- Can be walled by Steel/Rock/Electric types more easily
- Provides better coverage against Fighting/Bug/Grass types

### Example Damage Calculations
**Hyper Voice** (90 BP Normal to Flying):
- Base: 90 BP
- Type conversion: Still 90 BP Flying-type
- Aerilate boost: 90 x 1.2 = 108 BP
- STAB (if user is Flying-type): 108 x 1.5 = 162 effective BP
- **Total effective power: 162 BP**

**Return** (102 BP at max happiness):
- Base: 102 BP
- Aerilate boost: 102 x 1.2 = 122.4 BP
- STAB: 122.4 x 1.5 = 183.6 effective BP
- **Total effective power: ~184 BP**

### Common Users in Elite Redux
- **Mega Pinsir**: Flying/Bug type with strong physical moves
- **Salamence variants**: Dragon/Flying with mixed offensive capabilities  
- **Rayquaza forms**: Legendary with diverse movepool
- **Various Flying-types**: As innate ability on multiple species

### Competitive Usage Notes

#### Strengths
- Transforms Normal-type coverage moves into STAB moves
- 1.2x damage boost makes all Normal moves significantly stronger
- Excellent with sound moves like Hyper Voice and Boomburst
- Synergizes well with high-power Normal moves

#### Weaknesses
- Removes Normal-type neutrality, making moves resisted by Rock/Steel/Electric
- Predictable type conversion can be exploited
- Doesn't affect already-typed moves
- Steel-types become problematic walls

#### Optimal Movesets
- **Hyper Voice/Boomburst**: Spread damage with conversion
- **Return/Body Slam**: Reliable physical options
- **Quick Attack**: Priority move becomes Flying-type
- **Coverage moves**: Non-Normal moves for Steel/Rock/Electric types

### Counters and Responses

#### Direct Counters
- **Steel-types**: Resist Flying moves, often have high Defense
- **Rock-types**: Resist Flying moves, can threaten back with Rock moves
- **Electric-types**: Resist Flying moves, often faster

#### Indirect Counters
- **Sturdy + Berry**: Survive boosted Normal moves
- **Rocky Helmet**: Punish contact moves like Body Slam
- **Static/Flame Body**: Status on contact moves

### Version History
- Introduced in Generation VI as one of the "-ate" abilities
- Maintained standard 1.2x damage boost in Elite Redux
- Functions identically to Pixilate/Refrigerate/Galvanize but for Flying-type

### Related Abilities
- **Pixilate**: Normal to Fairy conversion
- **Refrigerate**: Normal to Ice conversion  
- **Galvanize**: Normal to Electric conversion
- **Normalize**: All moves to Normal (opposite effect)
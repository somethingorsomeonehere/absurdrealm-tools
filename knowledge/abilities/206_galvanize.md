---
id: 206
name: Galvanize
status: reviewed
character_count: 89
---

# Galvanize - Ability ID 206

## In-Game Description
"Normal-type moves become Electric and Electric gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Galvanize converts all Normal-type moves into Electric-type and Electric moves gain STAB.

## Detailed Mechanical Explanation
*For Discord/reference use*

Galvanize is an ATE-type ability that fundamentally alters how Normal-type moves function for the user.

### Core Mechanics
- **Type Conversion**: All Normal-type moves used by the Pokemon become Electric-type
- **Power Boost**: Converted moves receive a 20% damage increase (1.2x multiplier)
- **STAB Application**: The Pokemon gains Same Type Attack Bonus on converted Electric moves
- **Move Coverage**: Affects both damaging moves and status moves

### Technical Implementation
```cpp
constexpr Ability Galvanize = {
    ATE_ABILITY(TYPE_ELECTRIC),
};

#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Affected Moves Examples
**Damaging Moves:**
- Quick Attack to Electric Quick Attack (boosted)
- Body Slam to Electric Body Slam (boosted)
- Hyper Beam to Electric Hyper Beam (boosted)
- Return/Frustration to Electric Return/Frustration (boosted)

**Status Moves:**
- Thunder Wave (already Electric - no change)
- Growl to Electric Growl (type changed, still status)
- Tail Whip to Electric Tail Whip (type changed, still status)

### Damage Calculation
For a Normal move converted by Galvanize:
1. Base move becomes Electric-type
2. Power increased by 20% (x1.2)
3. STAB applied if user is Electric-type (x1.5)
4. Type effectiveness calculated against Electric

**Example**: Quick Attack (40 BP) becomes:
- Base: 40 x 1.2 (Galvanize) = 48 BP
- With STAB (if Electric-type): 48 x 1.5 = 72 effective BP

### Common Users in Elite Redux
- **Alolan Geodude line**: Geodude-A, Graveler-A, Golem-A (regular or innate ability)
- **Dragonite variants**: Multiple Dragonite forms (innate ability)
- **Whismur line**: Whismur-Redux, Loudred-Redux, Exploud-Redux (innate ability)
- **Flygon variants**: Flygon-Redux-B forms (innate ability)
- **Magearna variants**: Various Magearna forms (regular ability)
- **Magnezone variants**: Some specialized forms (regular ability)

### Strategic Implications
**Advantages:**
- Converts weak Normal moves into powerful Electric attacks
- Provides excellent neutral coverage with Electric typing
- Synergizes well with Electric terrain and Electric-type STAB
- Makes common moves like Quick Attack and Body Slam more threatening

**Considerations:**
- Normal moves lose their universal neutral typing
- Electric moves are resisted by Ground, Grass, Electric, and Dragon types
- Ground types become completely immune to converted moves
- Status moves like Growl may become less useful when Electric-typed

### Interactions with Other Mechanics
- **Ion Deluge**: If Ion Deluge is active, it would normally convert Normal moves to Electric, but Galvanize takes precedence
- **Electrify**: If the target is Electrified, Galvanize's conversion still applies
- **Normalize**: Cannot stack with Normalize (different abilities)
- **Plasma Fists**: If Plasma Fists effect is active, it may interact with Galvanize

### Competitive Usage Notes
- Excellent for physical attackers with access to powerful Normal moves
- Pairs well with Electric Terrain for additional power boost
- Consider coverage moves to handle Ground types
- Status moves become more niche when converted to Electric type

### Counters
- **Ground types**: Completely immune to converted Electric moves
- **Electric types**: Resist converted moves
- **Grass types**: Resist converted moves  
- **Lightning Rod/Volt Absorb**: Abilities that redirect or absorb Electric moves

### Synergies
- **Electric Terrain**: Boosts converted Electric moves further
- **Choice Band/Specs**: Amplifies the power boost from conversion
- **Life Orb**: Stacks with Galvanize's damage boost
- **Electric Gem**: Would activate on converted moves (if not consumed)

### Version History
Galvanize was introduced in Generation VI as part of the ATE ability family (Aerilate, Pixilate, Refrigerate). In Elite Redux, it maintains the standard 20% power boost while providing type conversion and STAB benefits.

### Notable Interactions
- Works with multi-hit Normal moves (each hit is converted and boosted)
- Affects Sketch-copied Normal moves
- Converts Normal-type Z-moves to Electric Z-moves (in applicable mechanics)
- Does not affect moves that are already Electric-type
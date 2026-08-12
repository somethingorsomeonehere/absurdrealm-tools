---
id: 465
name: Pixie Power
status: reviewed
character_count: 145
---

# Pixie Power - Ability ID 465

## In-Game Description
"1.2x accuracy. Boosts Fairy moves by 1.33x for all."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All Fairy-type moves for the user, their allies, and the opponent get a 1.33x boost. Boost is reversed by Aura Break. 1.2x accuracy on all moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Pixie Power is a hybrid ability that combines the field-wide Fairy-type boosting effects of Fairy Aura with a personal accuracy enhancement. This makes it both a team support ability and a personal reliability boost.

### Activation Conditions
- **Fairy Aura Effect**: Automatically boosts all Fairy-type moves used by any Pokemon on the field
- **Accuracy Boost**: Applies to all moves used by the Pokemon with this ability
- **Field-wide application**: The Fairy boost applies to opponents' Fairy moves as well
- **Always active**: Both effects are passive and don't require activation

### Power Boost Mechanics
- **Base multiplier**: 1.33x power to all Fairy-type moves field-wide
- **Aura Break interaction**: If Aura Break is present, the multiplier becomes 0.75x instead
- **Affects all users**: Both allies and opponents benefit/suffer from the Fairy boost
- **Move type requirement**: Only affects moves that are Fairy-type when used

### Accuracy Enhancement
- **Personal benefit**: Only applies to the Pokemon with Pixie Power
- **Universal application**: Affects all moves regardless of type
- **Multiplier**: 1.2x accuracy (20% increase)
- **Stacks with other accuracy modifiers**: Combines multiplicatively with items, moves, etc.

### Technical Implementation
```c
// Pixie Power combines Fairy Aura effects with accuracy boost
constexpr Ability PixiePower = {
    .onEntry = FairyAura.onEntry,                    // Fairy aura switch-in message
    .onOffensiveMultiplier = FairyAura.onOffensiveMultiplier,  // Field-wide Fairy boost
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        *accuracy *= 1.2;                           // Personal accuracy boost
        return ACCURACY_MULTIPLICATIVE;
    },
    .onOffensiveMultiplierFor = APPLY_ON_ANY,       // Affects all Pokemon's Fairy moves
};
```

### Important Interactions
- **Fairy Aura equivalence**: The power boost portion works identically to Fairy Aura
- **Aura Break reversal**: Aura Break turns the 1.33x boost into 0.75x reduction
- **Switch-in announcement**: Displays the same message as Fairy Aura on entry
- **Accuracy stacking**: The 1.2x accuracy stacks with other accuracy modifiers
- **Type effectiveness**: Fairy boost applies after type effectiveness calculations
- **Multi-hit moves**: Each hit gets both the power boost (if Fairy) and accuracy boost

### Strategic Applications
- **Fairy team support**: Excellent on Fairy-type focused teams
- **Mixed offense**: Benefits both Fairy and non-Fairy moves differently
- **Reliability improvement**: The accuracy boost makes all moves more consistent
- **Double-edged support**: Also boosts opponent Fairy moves unless Aura Break is present
- **Switch utility**: Can be brought in to immediately boost team's Fairy moves

### Team Synergies
- **Fairy-type attackers**: Directly benefits from the power boost
- **Aura Break users**: Can negate the opponent benefit while keeping accuracy boost
- **Mixed attackers**: Pokemon using both Fairy and non-Fairy moves benefit fully
- **Support movesets**: Improved accuracy on status moves and utility moves
- **Terrain setters**: Misty Terrain synergizes with Fairy-type focus

### Counters and Limitations
- **Aura Break**: Completely reverses the Fairy power boost
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable both effects
- **Non-Fairy teams**: Less valuable on teams with few Fairy-type moves
- **Opponent benefit**: Boosts enemy Fairy moves unless countered
- **Accuracy caps**: Cannot boost accuracy above 100% if move normally has perfect accuracy

### Competitive Usage
- **Team support role**: Functions as a pseudo-weather effect for Fairy moves
- **Swiss army knife**: Provides both offensive support and personal reliability
- **Entry timing**: Best switched in when Fairy moves are about to be used
- **Aura Break synergy**: Can be paired with Aura Break users for one-way benefit
- **Mixed sets**: Allows reliable use of lower-accuracy moves

### Unique Characteristics
- **Dual functionality**: Only ability combining field-wide power boost with personal accuracy
- **Fairy Aura clone**: Power boost mechanics identical to existing Fairy Aura
- **Universal accuracy**: Accuracy boost applies to all move types
- **Field manipulation**: Changes the battle dynamics for all Fairy move users
- **Announcement effect**: Provides battlefield awareness of the aura effect

### Version History
- Custom ability created for Elite Redux
- Based on Fairy Aura foundation with added accuracy component
- Part of the expanded ability roster for enhanced strategic depth
- Designed to provide both team support and individual reliability improvements
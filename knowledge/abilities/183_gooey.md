---
id: 183
name: Gooey
status: reviewed
character_count: 135
---

# Gooey - Ability ID 183

## In-Game Description
"Lowers Speed of enemies that make contact with this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user is hit by a contact move, the attacker reduces their Speed by one stage. Activates multiple times against multihit moves.


## Detailed Mechanical Explanation

### Activation Conditions
- Triggered when the Pokemon with Gooey is hit by a contact move
- Only activates if the attacking Pokemon's Speed can be lowered (not at -6)
- Checks for immunity effects like Mirror Armor before applying

### Effects
- Reduces the attacker's Speed stat by 1 stage (-1)
- Bypasses Safeguard protection when applying the Speed reduction
- Does not affect the damage calculation of the triggering move

### Implementation Details
```cpp
// From abilities.cc
constexpr Ability Gooey = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(StatLowerableOrMirrorArmor(attacker, STAT_SPEED))
        CHECK(IsMoveMakingContact(move, attacker))

        BattleScriptCall(BattleScript_GooeyActivates);
        gHitMarker |= HITMARKER_IGNORE_SAFEGUARD;
        return TRUE;
    },
};
```

### Battle Script Mechanics
- Uses `BattleScript_GooeyActivates` to handle the Speed reduction
- Swaps attacker/target context for proper stat lowering application
- Sets `MOVE_EFFECT_SPD_MINUS_1` as the secondary effect

## Strategic Applications

### Defensive Utility
- **Physical Wall Support**: Punishes contact-based physical attackers by reducing their Speed
- **Speed Control**: Gradually slows down threatening physical sweepers
- **Momentum Shift**: Can turn aggressive physical attacks into disadvantageous trades

### Competitive Considerations
- **Contact Move Deterrent**: Makes opponents think twice about using physical contact moves
- **Setup Disruption**: Interferes with physical setup sweepers' Speed control
- **Team Support**: Provides passive Speed control for slower teammates

### Counters and Limitations
- **Non-Contact Moves**: Physical moves like Earthquake, Rock Slide, etc. don't trigger Gooey
- **Special Attackers**: Completely bypassed by special moves
- **Stat Immunity**: Mirror Armor, Clear Body, and similar abilities prevent the Speed drop
- **Substitute**: Attacking through Substitute doesn't trigger contact abilities

## Thematic Design

### Pokemon Association
Gooey is commonly found on:
- **Goodra Line**: The classic gooey dragon Pokemon
- **Sticky/Slimy Types**: Various Pokemon with viscous or adhesive properties
- **Defensive Builds**: Often paired with other defensive abilities as innates

### Flavor Connection
The ability perfectly captures the concept of sticky substances that trap and slow down anything that touches them, translating the real-world physics of viscous materials into a battle mechanic.

## Synergies and Combinations

### Ability Combinations
- **With Regenerator**: Creates a defensive wall that heals and slows attackers
- **With Sticky Hold**: Thematic pairing for maximum stickiness
- **With Liquid Ooze**: Punishes both contact and draining moves

### Move Synergies
- **Infestation/Wrap**: Combines with trapping moves for enhanced control
- **Thunder Wave**: Stacks with paralysis for maximum Speed control
- **Toxic Spikes**: Sets up while slowing physical threats

### Team Role
- **Defensive Pivot**: Switches into physical attackers and slows them down
- **Speed Control Support**: Provides passive Speed manipulation for team setup
- **Physical Check**: Helps check fast physical sweepers through Speed reduction
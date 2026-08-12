---
id: 221
name: Tangling Hair
status: reviewed
character_count: 135
---

# Tangling Hair - Ability ID 221

## In-Game Description
"Lowers Speed of enemies that make contact with this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user is hit by a contact move, the attacker reduces their Speed by one stage. Activates multiple times against multihit moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

**TANGLING HAIR** is a contact-punishment ability identical to Gooey in mechanics, providing defensive utility by slowing down physical attackers.

### Core Mechanics
- **Trigger**: When the Pokemon with Tangling Hair is hit by a contact move
- **Effect**: Reduces attacker's Speed by 1 stage (-1)
- **Activation Conditions**: Only if attacker's Speed can be lowered (not already at -6 stages)
- **Safeguard Bypass**: Ignores Safeguard protection on the attacker

### Activation Conditions
1. **Contact Move Required**: Only contact moves trigger the ability
2. **Stat Lowerable Check**: Attacker must be able to have Speed lowered
3. **Mirror Armor Immunity**: Respects stat lowering immunities like Mirror Armor
4. **On-Hit Application**: Must successfully hit the Tangling Hair user

### Technical Implementation
```cpp
// From abilities.cc - Tangling Hair uses Gooey's implementation
constexpr Ability TanglingHair = {
    .onDefender = Gooey.onDefender,
};

// The actual Gooey implementation that Tangling Hair inherits:
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
The ability uses `BattleScript_GooeyActivates` which:
- Swaps attacker/target context for proper stat application
- Sets `MOVE_EFFECT_SPD_MINUS_1` as the secondary effect
- Applies Speed reduction immediately after damage calculation

### Complete List of Contact Moves (Examples)
**Physical Contact Moves** that trigger Tangling Hair:
- Tackle, Body Slam, Take Down
- Punch moves: Fire Punch, Ice Punch, Thunder Punch
- Scratch, Slash, Fury Swipes
- Bite, Crunch, Jaw moves
- Close Combat, Mach Punch, Drain Punch
- Earthquake does NOT trigger (non-contact)
- Rock Slide does NOT trigger (non-contact)

### Interactions with Other Abilities/Mechanics
- **Mirror Armor**: Reflects the Speed drop back to the Tangling Hair user
- **Clear Body/White Smoke**: Prevents the Speed reduction entirely  
- **Defiant/Competitive**: Triggers +2 Attack/Sp.Attack when Speed is lowered
- **Substitute**: Contact moves hitting Substitute do NOT trigger Tangling Hair
- **Long Reach**: Moves become non-contact, preventing activation

### Strategic Implications
**Defensive Applications:**
- Punishes physical contact attackers by reducing their Speed
- Creates speed control for slower defensive teams
- Deters setup sweepers using contact moves
- Provides passive team support through opponent speed reduction

**Offensive Considerations:**
- Forces opponents to consider non-contact alternatives
- Can ruin opponent's speed tier calculations mid-battle
- Synergizes with Thunder Wave and other speed control

### Example Damage Calculations
Tangling Hair doesn't affect damage calculation - it's a post-damage effect:
- Opponent uses Close Combat to Deals full damage to Speed drops by 1 stage
- Opponent at +1 Speed to After contact move to Now at base Speed (0 stages)
- Multiple contact hits in one turn to Only one Speed drop per turn

### Common Users
In Elite Redux, Pokemon commonly associated with Tangling Hair:
- **Dugtrio line**: Hair-like ground spikes
- **Tangela/Tangrowth**: Vine hair that tangles
- **Various grass types**: With hair-like appendages
- **Custom distributions**: As innate abilities on defensive builds

### Competitive Usage Notes
- **Physical Wall Support**: Excellent on bulky Pokemon that can tank contact moves
- **Speed Control Teams**: Fits well in teams needing passive speed manipulation  
- **Setup Disruption**: Interferes with physical setup sweepers' momentum
- **Contact Move Deterrent**: Makes opponents reconsider their move choices

### Counters and Limitations
**Direct Counters:**
- **Non-Contact Physical Moves**: Earthquake, Rock Slide, Bulldoze, U-turn
- **Special Attackers**: Completely bypass the ability
- **Stat Immunity**: Clear Body, White Smoke prevent the Speed drop
- **Remote Contact**: Long Reach makes contact moves non-contact

**Situational Limitations:**
- **Already Slow Opponents**: -1 Speed may not matter for slow tanks
- **Choice Item Users**: May not care about Speed drop if locked into one move
- **Priority Users**: Speed reduction less relevant for priority move spam

### Synergies and Combinations
**Ability Combinations:**
- **With Regenerator**: Creates excellent defensive pivot that heals and slows
- **With Rocky Helmet**: Punishes contact moves with damage AND speed drop
- **With Rough Skin/Iron Barbs**: Triple punishment for contact moves

**Move Synergies:**
- **Thunder Wave**: Stacks paralysis with Speed drops for maximum control
- **Infestation/Bind**: Trapping moves become more effective with slower opponents
- **Payback**: Benefits from slower opponents due to Speed reduction

**Team Role:**
- **Defensive Pivot**: Switches into physical threats and cripples their speed
- **Speed Control Support**: Provides team-wide speed advantage
- **Physical Check**: Helps handle fast physical sweepers through accumulated speed drops

### Counters
**Hard Counters:**
- Special attackers (completely avoid contact)
- Non-contact physical moves
- Stat immunity abilities

**Soft Counters:**
- Pokemon that don't rely on Speed
- Choice item users
- Priority move users

### Version History
- **Generation VII**: Introduced as signature ability of Alolan Dugtrio
- **Elite Redux**: Maintains original mechanics, distributed to various Pokemon
- **Implementation**: Shares exact code with Gooey for consistency
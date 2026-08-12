---
id: 149
name: Illusion
status: reviewed
character_count: 115
---

# Illusion - Ability ID 149

## In-Game Description
"Appears as last party slot and boosts power by 1.3x until hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Makes the Pokemon appear as the last alive party member. Boosts the user's damage by 30% until the illusion breaks.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Illusion is a unique ability that combines visual deception with offensive power enhancement:

**Disguise System:**
- When entering battle, automatically assumes the appearance of the last alive, non-egg Pokemon in the party
- Excludes the Illusion user itself and any active partner in double battles
- Shows the target Pokemon's species, sprite, and typing information
- Does not copy stats, moves, or other abilities - only visual appearance

**Power Enhancement:**
- Provides a 1.3x (30%) damage multiplier to all offensive moves while the illusion is active
- Applied through the `onOffensiveMultiplier` callback in battle calculations
- Stacks multiplicatively with other damage modifiers

**Breaking Conditions:**
- Illusion breaks immediately when the user takes damage from any move that successfully hits
- Triggered by the `onDefender` callback when `DidMoveHit()` returns true
- Status moves that don't deal damage will not break the illusion
- Missing moves will not break the illusion

### Technical Implementation

```cpp
constexpr Ability Illusion = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(DidMoveHit())
        CHECK(gBattleStruct->illusion[battler].on)
        CHECK_NOT(gBattleStruct->illusion[battler].broken)

        BattleScriptCall(BattleScript_IllusionOff);
        return TRUE;
    },
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleStruct->illusion[battler].on && !gBattleStruct->illusion[battler].broken) MUL(1.3);
        },
};
```

**Illusion State Structure:**
```cpp
struct Illusion {
    u8 on;       // Whether illusion is active
    u8 set;      // Whether illusion has been initialized
    u8 broken;   // Whether illusion has been broken
    u8 partyId;  // ID of the party member being mimicked
    struct Pokemon *mon; // Pointer to the mimicked Pokemon
}
```

### Setup Process
1. `SetIllusionMon()` is called when the Pokemon enters battle
2. Searches party from last slot (index 5) to first slot (index 0)
3. Selects the first viable candidate:
   - Must have a valid species
   - Must have HP > 0 (alive)
   - Must not be an egg
   - Must not be the Illusion user itself
   - Must not be the active partner in doubles
4. Sets up the illusion state with the selected party member

### Breaking Animation
When illusion breaks:
- Plays `B_ANIM_ILLUSION_OFF` animation
- Updates the sprite to show the true form
- Displays message: "{Pokemon}'s Illusion wore off!"
- Permanently disables the illusion for the remainder of battle

### Strategic Applications

**Offensive Usage:**
- 1.3x damage boost makes setup moves and powerful attacks more threatening
- Disguise can mislead opponents about typing and potential movesets
- Particularly effective on frail but powerful attackers

**Team Synergy:**
- Works best with diverse party members to maximize deception potential
- Consider party positioning to control which Pokemon is mimicked
- Strong offensive presence in the last party slot enhances the deception

**Timing Considerations:**
- Most effective early in battle before taking damage
- Prioritize dealing damage quickly to maximize the power boost
- Switch out before taking damage to preserve the illusion

### Common Users
- **Zoroark line**: Primary users with high Attack/Sp. Attack stats
- Various Pokemon with Illusion as an innate ability in Elite Redux

### Damage Calculation Example
Base damage: 100
With Illusion active: 100 x 1.3 = 130 damage
After illusion breaks: 100 damage (normal)

### Interactions with Other Abilities
- **Fort Knox**: Does not block Illusion's damage boost (non-offensive ability)
- **Trace/Role Play**: Can copy Illusion but won't set up a new disguise mid-battle
- **Skill Swap**: Removes Illusion ability and breaks any active illusion

### Limitations
- Illusion breaks on any damage taken, making it fragile
- No effect if no suitable party members are available for mimicking
- Visual deception only - doesn't change actual stats or capabilities
- One-time use per battle entry (cannot be reactivated once broken)
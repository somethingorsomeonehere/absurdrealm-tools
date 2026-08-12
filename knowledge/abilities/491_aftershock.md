---
id: 491
name: Aftershock
status: reviewed
character_count: 120
---

# Aftershock - Ability ID 491

## In-Game Description
"Follows up damaging moves with Magnitude."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

After landing a damaging move, the user follows up with Magnitude at 10, 30, 50, or 70 power. Hits all adjacent Pokemon.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Aftershock automatically triggers a secondary Magnitude attack after any successful damaging move, creating seismic follow-up damage that affects all adjacent Pokemon on the battlefield.

### Activation Conditions
- **Trigger**: After using any damaging move with power > 0
- **Success requirement**: Original move must not result in MOVE_RESULT_NO_EFFECT
- **Target validation**: Must successfully target an opponent
- **Power**: Fixed at 65 base power for Magnitude
- **Type**: Ground-type attack with all Ground-type interactions

### Technical Implementation
```c
constexpr Ability Aftershock = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(gBattleMoves[move].power) // Must be damaging move
        u8 target = AdjustFollowupMoveTarget(battler, FOLLOWUP_STANDARD);
        return UseAttackerFollowUpMove(battler, target, MOVE_MAGNITUDE, 65);
    },
};
```

### Magnitude Move Properties
- **Base power**: 65 (fixed for this ability)
- **Type**: Ground
- **Category**: Physical
- **Target**: All adjacent Pokemon (FOES_AND_ALLY)
- **Accuracy**: 100%
- **Effects**: Standard Ground-type interactions

### Strategic Applications
- **Area damage**: Hits multiple targets for additional damage output
- **Ground coverage**: Provides Ground-type attacks regardless of user's type
- **Combo potential**: Works with any damaging move for consistent follow-up
- **Pressure tool**: Forces opponents to consider seismic follow-ups
- **Multi-target utility**: Excellent in double battles for field control

### Double Battle Considerations
- **Ally damage**: Can harm partner Pokemon, requiring careful positioning
- **Flying immunity**: Flying-types and Levitate users avoid the follow-up
- **Wide spread**: Affects all adjacent positions simultaneously
- **Positioning strategy**: Requires tactical awareness of battlefield layout

### Move Synergies
**Excellent triggers:**
- High-power moves: Follow devastating attacks with seismic damage
- Multi-hit moves: Each successful hit can potentially trigger Aftershock
- Status moves with damage: Moves like Knock Off gain seismic follow-up

**Considerations:**
- Contact moves: Original move makes contact, follow-up doesn't
- Priority moves: Fast attacks followed by immediate Ground damage
- Special attacks: Special moves followed by physical Ground attack

### Type Interactions
- **Super effective against**: Fire, Electric, Poison, Rock, Steel
- **Not very effective against**: Bug, Grass
- **No effect on**: Flying-types and Levitate users
- **STAB potential**: Ground-types get STAB on the follow-up attack

### Limitations
- **Flying immunity**: Flying-types completely avoid the follow-up
- **Ally damage**: Can harm partners in double battles
- **One follow-up**: Only triggers once per successful attack
- **Ground typing**: Limited by Ground-type coverage and immunities
- **Fixed power**: Always 65 base power regardless of original move

### Counters
- **Flying-types**: Immune to the Magnitude follow-up
- **Levitate**: Ability grants immunity to Ground moves
- **Protect variants**: Can protect against the follow-up attack
- **Air Balloon**: Item provides temporary Ground immunity
- **Telepathy**: Ally ability prevents friendly fire damage

### Competitive Usage
- **Physical attackers**: Excellent on physical sweepers for extra damage
- **Mixed coverage**: Provides Ground attacks for non-Ground types
- **Field control**: Controls battlefield positioning in doubles
- **Anti-switch**: Discourages switching with follow-up pressure
- **Breaking focus**: Sash/Sturdy breaking potential with dual hits

### Team Building Considerations
- **Flying allies**: Partner with Flying-types to avoid friendly fire
- **Magnet Rise**: Temporary immunity for Ground-weak allies
- **Air Balloon**: Protect important allies from seismic damage
- **Earthquake synergy**: Stack with Earthquake for massive Ground damage

### Version History
- Elite Redux custom ability for seismic battle mechanics
- Designed to create unique follow-up attack patterns
- Fixed power ensures balanced damage output
- Part of expanded ability system for enhanced combat dynamics
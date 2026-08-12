---
id: 531
name: Clap Trap
status: reviewed
character_count: 155
---

# Clap Trap - Ability ID 531

## In-Game Description
"Counters contact with 50BP Snap Trap."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user receives a contact move, counters with a 50 BP Snap Trap. This Steel-type move traps opponents for 4-5 turns while dealing 1/8 max HP damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger Condition**: Only activates when the user is hit by a contact move
- **Retaliation Move**: Uses Snap Trap (MOVE_SNAP_TRAP) with fixed 50 base power
- **Type**: Steel-type move (inherits from Snap Trap)
- **Accuracy**: 85% (inherits from Snap Trap base accuracy)
- **Target**: The attacking Pokemon that made contact

### Technical Implementation
```cpp
constexpr Ability SnapTrapWhenHit = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))

        UseOutOfTurnAttack(battler, attacker, ability, MOVE_SNAP_TRAP, 50);
        return FALSE;
    },
};
```

### Snap Trap Move Details
- **Base Power**: 100 (but Clap Trap uses fixed 50 power)
- **Type**: Steel
- **Effect**: EFFECT_TRAP - traps target for 4-5 turns
- **PP**: 10
- **Accuracy**: 85%
- **Contact**: No
- **Category**: Physical

### Activation Conditions
- **Required**: User must be hit by a contact move
- **Blocked by**: 
  - Non-contact moves (special attacks, status moves, etc.)
  - Magic Guard protecting the attacker
  - Moves that don't make contact (Earthquake, Surf, etc.)

### Contact Moves (Examples)
- **Physical attacks**: Tackle, Punch moves, Bite moves, most physical attacks
- **Special contact moves**: Grass Knot, Draining Kiss
- **Multi-hit contact**: Fury Swipes, Pin Missile (triggers on each hit)

### Trapping Effect
- Target cannot switch out for 4-5 turns (random duration)
- Takes 1/8 of target's max HP damage each turn while trapped
- Trapping ends early if the user switches out or faints
- Trapped Pokemon can still attack normally

### Strategic Implications
- **Defensive Utility**: Punishes physical attackers while providing board control
- **Damage Over Time**: Combines immediate retaliation with ongoing trap damage
- **Switch Prevention**: Forces opponents to commit to battle or use specific escape moves
- **Steel Typing**: Benefits from Steel-type STAB users and resists common types

### Damage Calculation
- Uses the user's Attack stat vs target's Defense stat
- Fixed 50 base power regardless of Snap Trap's normal 100 power
- Can receive STAB bonus if user is Steel-type
- Affected by type effectiveness (Steel vs target's typing)

### Common Users
Based on proto analysis:
- **Stunfisk (Galarian)**: Has Clap Trap as an ability option
- **Various Steel-types**: Likely distributed to defensive Steel-type Pokemon

### Competitive Usage Notes
- **Tank Role**: Excellent on defensive Pokemon that expect to take contact moves
- **Pivot Punishment**: Deters U-turn, Volt Switch, and other contact pivot moves
- **Physical Wall**: Enhances the role of defensive Pokemon against physical attackers
- **Setup Counter**: Punishes setup sweepers that rely on contact moves

### Counters
- **Special Attackers**: Completely avoid triggering the ability
- **Non-contact Physical**: Earthquake, Rock Slide, etc. don't trigger
- **Ghost-types**: Immune to Steel-type Snap Trap damage
- **Magic Guard**: Prevents the user from taking trap damage
- **Rapid Spin/Defog**: Can remove trap effects

### Synergies
- **Steel-types**: Gain STAB on the Snap Trap retaliation
- **Defensive Items**: Leftovers, Rocky Helmet stack with trap damage
- **Entry Hazards**: Combine with Spikes/Stealth Rock for additional pressure
- **Status Moves**: Sleep/Paralyze trapped opponents for maximum value

### Version History
- **Elite Redux Custom**: Introduced as ABILITY_SNAP_TRAP_WHEN_HIT (ID 531)
- **Elite Redux Implementation**: Uses UseOutOfTurnAttack system with fixed 50 power
- **Current Status**: Active ability in Elite Redux v2024+
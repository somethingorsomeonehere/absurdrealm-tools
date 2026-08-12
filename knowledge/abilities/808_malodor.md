---
id: 808
name: Malodor
status: reviewed
character_count: 105
---

# Malodor - Ability ID 808

## In-Game Description
"Suppresses attacker's abilities on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by a contact move, the user suppresses the attacker's ability and innates until they switch out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger**: Activates when the Malodor user is hit by any contact move
- **Effect**: Applies the STATUS3_GASTRO_ACID status to the attacking Pokemon
- **Duration**: Suppression lasts until the attacker switches out or the battle ends
- **Contact Detection**: Uses the same contact detection as other contact-based abilities

### Activation Conditions
```cpp
CHECK(ShouldApplyOnHitAffect(attacker))          // Standard on-hit ability check
CHECK(IsMoveMakingContact(move, attacker))       // Move must make contact
CHECK_NOT(gStatuses3[attacker] & STATUS3_GASTRO_ACID)  // Attacker not already suppressed
```

### Technical Implementation
The ability works through the `onDefender` hook in the abilities system:

```cpp
constexpr Ability Malodor = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(gStatuses3[attacker] & STATUS3_GASTRO_ACID)

        gStatuses3[attacker] |= STATUS3_GASTRO_ACID;
        BattleScriptCall(BattleScript_StackAbilitySuppressedMessage);
        return TRUE;
    },
};
```

### Suppression Mechanics
- Uses the same suppression system as Gastro Acid (STATUS3_GASTRO_ACID flag)
- Suppressed abilities are checked via `IsSuppressed()` function in battle_util.c
- Does not affect abilities with the "unsuppressable" flag
- Blocked by Ability Shield (if the attacker has one)

### Contact Move Detection
Contact moves are determined by:
1. Move has the `contact` flag in battle data
2. Special case: Shell Side Arm when physical
3. Bypassed by Long Reach ability
4. Bypassed by Protective Pads item
5. Bypassed by Punching Glove for punch moves

### Affected Moves (Examples)
**Contact moves that trigger Malodor:**
- Physical attacks: Tackle, Body Slam, Earthquake, etc.
- Special contact moves: Petal Dance, Grass Knot
- Multi-hit moves: Fury Attack, Pin Missile
- Priority moves: Quick Attack, Mach Punch

**Non-contact moves that don't trigger:**
- Projectile moves: Thunderbolt, Flamethrower
- Sound moves: Boomburst, Hyper Voice
- Long-range moves: Rock Slide, Surf

### Strategic Implications
**Offensive Use:**
- Excellent counter to contact-based setup sweepers
- Shuts down abilities like Guts, Flame Orb combos via contact
- Forces switches on Pokemon relying on their abilities

**Defensive Use:**
- Protects team from status-inducing contact abilities
- Disrupts opposing strategies dependent on specific abilities
- Creates long-term advantage through ability suppression

### Common Users
- **Mega Garbodor**: Primary user in Elite Redux, fits thematically with toxic/foul odor concept
- Type combination: Poison/Steel with defensive stats

### Competitive Applications
**Team Roles:**
- Physical wall that punishes contact attackers
- Anti-setup utility Pokemon
- Switch-in for contact-based threats

**Synergies:**
- Works well with entry hazards to punish forced switches
- Combines with status moves to cripple suppressed opponents
- Effective on bulky Pokemon that can tank multiple contact hits

### Counters and Limitations
**Counters:**
- Special attackers using non-contact moves
- Pokemon with Long Reach ability
- Protective Pads item users
- Magic Bounce (reflects suppression effects)

**Limitations:**
- Only triggers on contact moves hitting the user
- Cannot suppress already suppressed Pokemon
- No effect on Pokemon with Ability Shield
- Requires taking damage to activate

**Unsuppressable Abilities:**
- Core abilities that cannot be suppressed include certain forme-maintaining abilities
- Battle Bond, Power Construct, and similar form-based abilities

### Battle Message
When activated, displays: "[Pokemon]'s ability was suppressed!"

### Version History
- Introduced in Elite Redux as ID 808
- Part of the expanded ability roster for enhanced strategic depth
- Themed around the concept of foul odors disrupting opponents' natural abilities
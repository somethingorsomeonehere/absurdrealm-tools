---
id: 304
name: Magical Dust
status: reviewed
character_count: 211
---

# Magical Dust - Ability ID 304

## In-Game Description
"If hit by a contact move, gives Psychic type to the attacker."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user is hit by a contact move, adds Psychic-type to the attacker's existing typing. Triggers immediately after the attack lands, including the first hit of a mutiihit attack. Removed when switching out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger**: Activates when the Pokemon with this ability is hit by a contact move
- **Effect**: Adds Psychic typing to the attacking Pokemon by setting their `type3` field
- **Duration**: Permanent for the battle (until the attacker switches out)
- **Type System**: Uses Elite Redux's enhanced typing system where Pokemon can have up to 3 types

### Activation Conditions
1. The Pokemon with Magical Dust must be hit by a move
2. The move must make contact (`IsMoveMakingContact(move, attacker)` returns true)
3. The move must successfully hit and deal damage (`ShouldApplyOnHitAffect(attacker)` returns true)
4. The attacker must not already be Psychic-type (`IS_BATTLER_OF_TYPE(attacker, TYPE_PSYCHIC)` returns false)

### Technical Implementation
```c
constexpr Ability MagicalDust = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK_NOT(IS_BATTLER_OF_TYPE(attacker, TYPE_PSYCHIC))

        gBattleMons[attacker].type3 = TYPE_PSYCHIC;
        PREPARE_TYPE_BUFFER(gBattleTextBuff1, gBattleMons[attacker].type3);
        BattleScriptCall(BattleScript_AttackerBecameTheType);
        return TRUE;
    },
};
```

### Contact Moves Affected
All contact moves can trigger this ability, including but not limited to:
- Physical attacks like Tackle, Quick Attack, Body Slam
- Multi-hit moves like Fury Attack, Double Kick
- Priority moves like Mach Punch, Bullet Punch
- Most Fighting-type moves (Brick Break, Close Combat, etc.)
- Biting moves (Bite, Crunch, Fire Fang, etc.)

### Type Interactions After Activation
When an attacker gains Psychic typing:
- **Weak to**: Dark (2x), Bug (2x), Ghost (2x)
- **Resistant to**: Fighting (0.5x), Psychic (0.5x)
- **Immune to**: None

### Strategic Implications
**Defensive Usage**:
- Punishes physical attackers by making them vulnerable to Dark-type moves
- Particularly effective against Fighting-type Pokemon, making them resist their own moves
- Can disrupt opponent's strategy by changing their type matchups mid-battle

**Offensive Implications for Opponent**:
- Gained Psychic typing may help against Fighting-types
- New weaknesses to Dark, Bug, and Ghost types
- Must be considered when switching in teammates

### Common Users
Based on the proto data, Pokemon with Magical Dust include:
- Various moth and butterfly Pokemon (as innate ability)
- Psychic/Fairy-type Pokemon with mystical themes
- Generally appears on Pokemon with magical or dust-related themes

### Competitive Usage Notes
- **Utility**: Strong defensive ability that can change type matchups
- **Timing**: Best used against physical attackers early in battle
- **Team Synergy**: Pairs well with Dark-type teammates who can exploit the new weakness
- **Counter-Strategy**: Opponents should prioritize special moves or already-Psychic attackers

### Counters
- **Special Moves**: Non-contact moves bypass the ability entirely
- **Psychic-types**: Already Psychic-type attackers are unaffected
- **Long-range Moves**: Moves like Earthquake, Surf, Flamethrower don't make contact
- **Status Moves**: Most status moves don't trigger the ability

### Synergies
- **Dark-type Teammates**: Can immediately exploit the new Psychic typing
- **Ghost-type Moves**: Become super effective against converted attackers  
- **Bug-type Coverage**: Gains effectiveness against converted Pokemon
- **Intimidate/Burn Support**: Helps reduce physical damage before conversion

### Version History
- Added in Elite Redux as part of the expanded ability roster
- ID 304 in the ability list
- Uses the enhanced typing system allowing for 3 simultaneous types

### Example Battle Scenario
1. Opponent's Machamp uses Close Combat on Magical Dust user
2. Machamp gains Psychic typing (becomes Fighting/Psychic)
3. Machamp is now weak to Dark moves (2x damage)
4. Machamp's own Fighting moves are now resisted by its Psychic typing
5. Partner Dark-type can switch in and exploit the new weakness

This ability represents a unique defensive mechanism that can significantly alter battle dynamics by permanently changing an opponent's typing and creating new strategic opportunities.
---
id: 518
name: Spiteful
status: reviewed
character_count: 182
---

# Spiteful - Ability ID 518

## In-Game Description
"Reduces attacker's PP on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Spiteful reduces the attacker's PP by 4 when hit by contact moves. Targets the last move used by the attacker. Fails if the attacker has no remaining PP or hasn't used any moves yet.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Spiteful is a defensive ability that punishes physical contact moves by reducing the attacker's PP. The ability triggers when the Pokemon with Spiteful is hit by a move that makes physical contact.

### Activation Conditions
- **Contact requirement**: Attacker must use a move that makes physical contact
- **Move exclusion**: Does not trigger on Struggle
- **PP requirement**: Attacker must have remaining PP on their last used move
- **Timing**: Activates immediately after taking damage from contact move

### PP Reduction Mechanics
- **Amount reduced**: Always reduces PP by 4 (modern generation mechanics)
- **PP limit**: Cannot reduce PP below 0
- **Move targeted**: Targets the attacker's last used move, not necessarily the contact move
- **Failure conditions**: 
  - Attacker has no PP remaining on their last move
  - Attacker hasn't used any moves yet (gLastMoves is 0 or 0xFFFF)
  - Last move was Struggle

### Technical Implementation
```c
// Spiteful ability implementation
constexpr Ability Spiteful = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(move != MOVE_STRUGGLE)
        CHECK(IsMoveMakingContact(move, attacker))
        CHECK(gBattleMons[attacker].pp[gChosenMovePos])

        BattleScriptCall(BattleScript_AbilitySpiteful);
        return TRUE;
    },
};
```

### Battle Script Process
The ability uses `tryspiteppreduce` command which:
1. Finds the attacker's last used move in their moveset
2. Checks if PP reduction is valid (move has remaining PP)
3. Reduces PP by 4 (or remaining PP if less than 4)
4. Updates the attacker's PP both in battle and permanently
5. Displays message about PP reduction
6. Cancels multi-turn moves if PP reaches 0

### Important Interactions
- **Last move targeting**: Reduces PP of the last move used, not the contact move
- **Multi-turn moves**: Cancels moves like Outrage if PP reaches 0
- **Transform/Mimic immunity**: Doesn't affect mimicked or transformed movesets
- **Ability negation**: Blocked by abilities like Mold Breaker
- **Protection**: Doesn't trigger if the attack is blocked by Protect

### Strategic Implications
- **Physical wall utility**: Excellent on defensive Pokemon that take many hits
- **PP stalling**: Can force opponents to run out of moves faster
- **Contact move deterrent**: Makes physical attackers think twice about repeated contact
- **Longevity tool**: Helps in extended battles by depleting opponent resources

### Contact Move Interactions
Common contact moves affected:
- **Physical attacks**: Tackle, Quick Attack, Body Slam, etc.
- **Priority moves**: Extreme Speed, Fake Out, Sucker Punch
- **Multi-hit moves**: Each hit can trigger Spiteful
- **Punch moves**: Fire Punch, Thunder Punch, etc.

### Non-Contact Moves (Unaffected)
- **Projectile moves**: Rock Throw, Pin Missile, Bullet Punch
- **Special attacks**: Most special moves don't make contact
- **Status moves**: Thunder Wave, Toxic, etc.
- **Environmental moves**: Earthquake, Surf, etc.

### Competitive Usage Notes
- **Defensive core**: Excellent on bulky Pokemon expected to take many hits
- **Innate ability**: Found as innate on Galarian Slowking and Runerigus
- **PP pressure**: Creates additional win condition through PP depletion
- **Contact punishment**: Deters physical attackers from repeated contact
- **Stall strategy**: Effective in longer battles and PP stall teams

### Known Users
- **Galarian Slowking**: Innate ability alongside Pressure for double PP pressure
- **Runerigus**: Innate ability providing defensive utility
- Both Pokemon can utilize the ability for stall and defensive strategies

### Counters
- **Non-contact moves**: Use special attacks or non-contact physical moves
- **Ability suppression**: Mold Breaker ignores Spiteful
- **Protection**: Protect prevents contact and ability activation
- **Long-range attacks**: Projectile and environmental moves avoid contact
- **One-shot strategies**: KO before Spiteful becomes relevant

### Synergies
- **Pressure**: Doubles PP reduction when combined as innate ability
- **Defensive stats**: High Defense/HP maximizes hits taken to trigger ability
- **Recovery moves**: Roost, Recover to stay healthy while reducing PP
- **Status moves**: Toxic, Thunder Wave to complement PP pressure strategy
- **Protective moves**: Protect to force more PP usage from opponents

### Version History
- Elite Redux exclusive ability (ID 518)
- Uses modern PP reduction mechanics (4 PP consistently)
- Implemented with specialized battle script for PP management
- Found as innate ability on select defensive Pokemon
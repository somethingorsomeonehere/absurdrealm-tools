---
id: 503
name: High Tide
status: reviewed
character_count: 129
---

# High Tide - Ability ID 503

## In-Game Description
"Triggers 50 BP Surf after using a Water-type move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Triggers a 50 BP Surf after the user lands a Water-type attack, including status moves like Soak. Surf hits all adjacent Pokemon.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
High Tide is an offensive ability that provides automatic followup attacks after using Water-type moves. The ability triggers a 50 BP Surf attack immediately after any Water-type move is used.

### Activation Conditions
- **Move type requirement**: Must use a Water-type move
- **Target adjustment**: Uses same target as the original move
- **Power**: Followup Surf always has 50 BP (regardless of original Surf power)
- **Timing**: Triggers immediately after the original move resolves

### Technical Implementation
```c
constexpr Ability HighTide = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(moveType == TYPE_WATER)
        CHECK(AdjustFollowupMoveTarget(battler, &target, move, FOLLOWUP_STANDARD))
        
        return UseAttackerFollowUpMove(battler, target, ability, MOVE_SURF, 50);
    },
};
```

### Move Interactions
- **All Water moves**: Works with any Water-type move, including status moves
- **Original move first**: Original move resolves completely before followup
- **Same target**: Followup Surf targets the same opponent as original move
- **Fixed power**: Followup Surf is always 50 BP regardless of original Surf power
- **No accuracy check**: Followup Surf cannot miss

### Status Move Synergy
High Tide works with Water-type status moves, making them offensive threats:
- **Aqua Ring**: Heals then deals 50 BP damage
- **Rain Dance**: Sets weather then attacks
- **Water Sport**: Reduces Fire damage then attacks
- Any other Water-type status moves

### Important Interactions
- **Double damage**: Effectively adds 50 BP to every Water-type move
- **Type effectiveness**: Followup Surf has normal type effectiveness
- **Contact**: Followup Surf does not make contact (like regular Surf)
- **Multi-target**: In doubles, Surf hits both opponents if applicable
- **Ability suppression**: Doesn't work if ability is suppressed

### Strategic Implications
- **Sustained pressure**: Every Water move becomes a potential 2-hit combo
- **Status move utility**: Makes Water status moves threatening
- **STAB synergy**: Water-types get STAB on both original move and followup
- **Coverage**: Provides consistent Water-type damage output
- **Energy efficiency**: Doubles damage output per turn with Water moves

### Pokemon Distribution
High Tide appears as an innate ability on several Water-type Pokemon:
- **Manaphy**: Innate alongside other abilities
- **Phione**: Innate alongside Field Explorer and Soul Heart
- **Squirtle evolution line**: Innate with Torrent and Opportunist
- **Primarina**: As a regular ability option alongside others

### Competitive Usage Notes
- **Water-type synergy**: Essential for Water-type attackers
- **Multi-hit potential**: Creates powerful combos with Water moves
- **Doubles utility**: Surf followup affects multiple targets
- **Status move viability**: Makes Water status moves more threatening
- **Consistent damage**: Guaranteed extra damage on Water attacks

### Counters
- **Type resistance**: Steel and Water types resist followup Surf
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable it
- **Contact abilities**: Don't trigger since Surf doesn't make contact
- **Substitute**: May block the followup attack
- **Protect variations**: Can potentially block followup

### Synergies
- **Torrent**: Boosts both original move and followup when at low HP
- **STAB**: Water-types get 1.5x damage on both hits
- **Rain**: Powers up both Water moves significantly
- **Choice items**: Locked into original move, not followup
- **Life Orb**: Boosts both attacks with recoil from each

### Similar Abilities
High Tide follows the same pattern as other followup abilities:
- **Volcano Rage**: Fire moves to 50 BP Eruption
- **Thundercall**: Electric moves to 20% power Smite
- **Frost Burn**: Fire moves to 40 BP Ice Beam
- **Glacial Rage**: Ice moves to 50 BP Blizzard

### Version History
- Custom Elite Redux ability (ID 503)
- Part of the enhanced ability system
- Uses the UseAttackerFollowUpMove framework
- Designed for sustained offensive pressure

### Calculation Examples
- **Hydro Pump (110 BP) + Surf (50 BP)**: Total ~160 BP per turn
- **Scald (80 BP) + Surf (50 BP)**: Total ~130 BP with burn chance
- **Aqua Ring (0 BP) + Surf (50 BP)**: Healing + 50 BP damage
- **With STAB**: Both moves get 1.5x multiplier
- **In rain**: Both moves get 1.5x power boost
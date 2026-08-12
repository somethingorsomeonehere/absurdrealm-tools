---
id: 383
name: Cold Rebound
status: reviewed
character_count: 123
---

# Cold Rebound - Ability ID 383

## In-Game Description
"When hit by contact moves, retaliates with Icy Wind."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When struck by any contact move, Cold Rebound retaliates with Icy Wind (60 BP), lowering the attacker's Speed by one stage. 

## Detailed Mechanical Explanation

### Overview
Cold Rebound is a defensive ability that triggers an immediate counter-attack when the user is hit by any contact move. Upon being struck by a contact move, the Pokemon automatically uses Icy Wind against the attacker, dealing Ice-type damage and reducing their Speed stat.

## Technical Implementation

### Source Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 3969-3977
- **Ability Definition**: `ColdRebound`

### Implementation Details
```cpp
constexpr Ability ColdRebound = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))

        UseOutOfTurnAttack(battler, attacker, ability, MOVE_ICY_WIND, 0);
        return FALSE;
    },
};
```

### Key Functions
- **`ShouldApplyOnHitAffect(attacker)`**: Ensures the ability only triggers under appropriate conditions (attacker is alive, no immunities, etc.)
- **`IsMoveMakingContact(move, attacker)`**: Verifies the triggering move makes physical contact
- **`UseOutOfTurnAttack(battler, attacker, ability, MOVE_ICY_WIND, 0)`**: Executes the counter-attack using Icy Wind

### Triggered Move: Icy Wind
- **Power**: 60 BP
- **Type**: Ice
- **Accuracy**: 100%
- **Target**: Both opponents (in doubles)
- **Effect**: EFFECT_SPEED_DOWN_HIT (lowers Speed by 1 stage)
- **Category**: Special
- **Additional Properties**: Air-based move

## Battle Mechanics

### Activation Conditions
1. **Must be hit by a contact move**: Only physical moves that make contact (punch, tackle, bite, etc.) trigger the ability
2. **Attacker must be alive**: The ability won't trigger if the contact move KO'd the attacker
3. **Standard hit requirements**: Move must actually connect and deal damage

### Counter-Attack Properties
- **Immediate activation**: Occurs directly after taking damage from the contact move
- **Automatic targeting**: Always targets the attacker
- **Special attack**: Uses the defender's Special Attack stat
- **Type effectiveness applies**: Super effective against Grass, Ground, Flying, and Dragon types
- **Can miss**: Though Icy Wind has 100% accuracy, accuracy modifiers still apply
- **Speed reduction**: Lowers attacker's Speed by 1 stage on hit

## Strategic Analysis

### Competitive Advantages
1. **Deterrent Effect**: Discourages opponents from using contact moves
2. **Speed Control**: Icy Wind's Speed reduction can cripple fast physical attackers
3. **Chip Damage**: 60 BP provides meaningful damage output
4. **Multi-Target**: In doubles, hits both opponents
5. **Type Coverage**: Ice typing provides super effective coverage against common types

### Tactical Applications
- **Physical Wall Support**: Excellent on defensive Pokemon that can tank contact moves
- **Speed Tier Management**: Speed reduction can flip speed tiers in your favor
- **Revenge Killing Setup**: Slowing down faster threats for teammates
- **Doubles Utility**: Multi-target effect provides excellent board control

### Synergistic Abilities
Cold Rebound works exceptionally well with:
- **Defensive abilities**: Pairs with damage reduction or HP recovery abilities
- **Ice-type STAB**: Maximizes the counter-attack damage
- **Speed control strategies**: Complements other speed manipulation tactics

## Competitive Tier Assessment: HIGH

### Reasons for High Tier Rating
1. **Powerful Deterrent**: Significantly impacts opponent's move choices
2. **Dual Effect**: Both damage and speed control in one trigger
3. **Reliable Activation**: Contact moves are extremely common in competitive play
4. **Strategic Depth**: Adds layers of decision-making to both players

### Potential Drawbacks
- **Contact Move Dependency**: Useless against special attackers
- **Ice Type Resistances**: Less effective against Water, Ice, Fire, and Steel types
- **No Damage Reduction**: Unlike some similar abilities, provides no defensive boost

## Related Abilities Comparison

### Similar Counter-Attack Abilities

#### Parry (Ability #335)
- **Counter Move**: Mach Punch (40 BP, Fighting-type, +1 priority)
- **Additional Effect**: 20% damage reduction
- **Comparison**: Cold Rebound deals more damage but lacks damage reduction

#### Ice Downfall (Ability #633)
- **Counter Move**: Icicle Crash (60 BP, Ice-type, 30% flinch chance)
- **Comparison**: Similar power but Icicle Crash has flinch chance instead of Speed reduction

#### Ultra Instinct (Ability #641)
- **Counter Move**: Vacuum Wave (40 BP, Fighting-type, +1 priority)
- **Additional Effect**: 20% damage reduction
- **Comparison**: Lower damage but priority and damage reduction

### Unique Positioning
Cold Rebound occupies a unique niche as the only contact counter-attack ability that provides speed control, making it particularly valuable in speed-centric metagames.

## Usage Recommendations

### Ideal Pokemon Types
- **Defensive Ice-types**: Maximize STAB damage from Icy Wind
- **Bulky pivots**: Pokemon that can tank contact moves and benefit from speed control
- **Support Pokemon**: Those that appreciate the utility of speed manipulation

### Team Role Integration
- **Defensive Core**: Excellent on walls that commonly face physical attackers
- **Speed Control Support**: Valuable on teams that need speed tier manipulation
- **Anti-Physical Tech**: Strong choice against contact-heavy metagames

### Caution Advised
- Avoid on frail Pokemon that can't survive strong contact moves
- Consider team synergy with Ice-type coverage
- Be mindful of Special Attack stat for counter-attack effectiveness

## Conclusion

Cold Rebound represents a high-tier defensive ability that combines immediate retaliation with valuable speed control. Its ability to punish contact moves while simultaneously providing team support through speed manipulation makes it an excellent choice for defensive and support-oriented Pokemon. The combination of respectable damage output and strategic utility places it among the more impactful defensive abilities in Elite Redux's extensive ability roster.


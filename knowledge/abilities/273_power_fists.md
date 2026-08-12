---
id: 273
name: Power Fists
status: reviewed
character_count: 85
---

# Power Fists - Ability ID 273

## In-Game Description
"Iron Fist moves target Special Defense and get a 1.3x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Punching moves gain a 30% damage boost and target Special Defense instead of Defense. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**POWER FISTS** is a unique offensive ability that modifies how punching moves calculate damage, forcing them to target the opponent's Special Defense stat regardless of the move's category.

### Core Mechanics:
- **Damage Multiplier**: 1.3x (30% boost) to all Iron Fist-boosted moves
- **Stat Targeting**: Forces moves to use defender's Special Defense for damage calculation
- **Move Category**: Does NOT change the move from physical to special - only changes which defensive stat is targeted
- **Attacker Stat**: Still uses the attacker's Attack or Special Attack based on the move's original category

### Technical Implementation:
```c
constexpr Ability PowerFists = {
    .onOffensiveMultiplier = IronFist.onOffensiveMultiplier,  // 1.3x multiplier
    .onChooseDefensiveStat = +[](ON_CHOOSE_DEFENSIVE_STAT) -> int {
        CHECK(IsIronFistBoosted(move));
        return STAT_SPDEF;
    },
};
```

### Affected Moves:
All moves with the FLAG_IRON_FIST_BOOST flag benefit from this ability:
- **Elemental Punches**: Fire Punch, Ice Punch, Thunder Punch, Drain Punch
- **Fighting Moves**: Mach Punch, Dynamic Punch, Focus Punch, Sky Uppercut, Close Combat
- **Other Punches**: Bullet Punch, Comet Punch, Mega Punch, Dizzy Punch, Shadow Punch
- **Special Cases**: Hammer Arm, Power-Up Punch, Meteor Mash

### Interaction with Other Abilities:
- **Brawling Wyvern**: If the user also has this ability, Dragon-type moves also receive the Power Fists treatment
- **Junshi Sanda**: If the user also has this ability, striker moves are affected as well
- **Fort Knox**: Can be blocked by Fort Knox's offensive ability nullification

### Strategic Implications:
1. **Mixed Offensive Threat**: Physical attackers can now exploit specially defensive walls
2. **Meta Disruption**: Traditional physical walls with high Defense but low Special Defense become vulnerable
3. **Type Coverage**: Access to multiple typed punches means diverse special-targeting coverage
4. **Damage Calculation**: A 100 BP punch becomes effectively 130 BP targeting Special Defense

### Example Damage Scenarios:
Against a Skarmory (140 Defense, 70 Special Defense):
- Normal Fire Punch: Targets 140 Defense
- Power Fists Fire Punch: Targets 70 Special Defense with 1.3x boost

This effectively doubles or triples damage output against physically defensive Pokemon.

### Common Users:
- Fighting-types seeking to break through physical walls
- Mixed attackers that can leverage the unpredictability
- Pokemon with wide punching move coverage

### Competitive Notes:
- Pairs excellently with Choice Band for maximum physical damage through Special Defense
- Countered by specially defensive Pokemon regardless of their physical bulk
- Creates mind games in team preview - opponents must consider different defensive benchmarks
- Particularly effective in metas dominated by physically defensive Steel-types

### Version History:
- Elite Redux exclusive ability
- Designed to create unique offensive dynamics not seen in standard Pokemon games
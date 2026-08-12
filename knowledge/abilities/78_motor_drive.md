---
id: 78
name: Motor Drive
status: reviewed
character_count: 129
---

# Motor Drive - Ability ID 78

## In-Game Description
"Boosts Speed instead of being hit by Electric-type moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to Electric-type moves, and boost Speed by 1 stage when the user is hit by them. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MOTOR DRIVE** is an absorption ability that converts Electric-type move damage into Speed boosts, providing both immunity and a stat advantage.

### Core Mechanics:
- **Trigger**: When hit by any Electric-type move
- **Effect**: Complete immunity to the move + Speed boost
- **Boost Amount**: +1 stage per hit absorbed
- **Priority**: Activates before damage calculation (onAbsorb hook)

### Activation Conditions:
1. **Direct Hits**: Any Electric-type move targeting this Pokemon
2. **Status Moves**: Thunder Wave, Electric Terrain setup, etc.
3. **Multi-Hit Moves**: Each hit of moves like Double Kick (if Electric) boosts Speed separately
4. **Indirect Damage**: Does NOT absorb Electric-type damage from abilities like Static or items

### Technical Implementation:
```c
constexpr Ability MotorDrive = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_ELECTRIC);
        *statId = STAT_SPEED;
        return ABSORB_RESULT_STAT;
    },
    .breakable = TRUE,
};
```

### Complete List of Affected Moves:
**Common Electric Moves Absorbed:**
- Thunder Bolt, Thunder, Discharge, Thunderbolt
- Thunder Wave (status), Thunder Shock, Spark
- Wild Charge, Volt Tackle, Zap Cannon
- Electro Ball, Thunder Fang, Thunder Punch
- Charge Beam, Shock Wave, Thunder Wave
- Electric Terrain (when used directly)

**NOT Affected By:**
- Static ability activation
- Electric-type Z-moves (absorbs the base move)
- Paralysis from non-Electric sources
- Electric Terrain passive damage

### Interactions with Other Abilities/Mechanics:
1. **Mold Breaker**: Can bypass Motor Drive, allowing Electric moves to hit normally
2. **Teravolt/Turboblaze**: Also bypass Motor Drive
3. **Lightning Rod**: Takes priority over Motor Drive if both are present
4. **Air Lock/Cloud Nine**: Do not affect Motor Drive (weather-independent)
5. **Trace/Skill Swap**: Can copy/transfer Motor Drive to other Pokemon

### Strategic Implications:
- **Pivoting Tool**: Safe switch-in against Electric-type attackers
- **Speed Control**: Accumulates Speed boosts throughout battle
- **Thunder Wave Immunity**: Cannot be paralyzed by the most common paralysis move
- **Team Support**: Forces opponents to avoid Electric moves or face stat penalties

### Example Damage Calculations:
- **Before Motor Drive**: 100 BP Thunderbolt deals ~25-30% to neutral target
- **With Motor Drive**: Same Thunderbolt deals 0 damage, grants +1 Speed instead
- **Multi-Hit Scenario**: Double Shock (hypothetical 2-hit Electric move) would grant +2 Speed stages total

### Common Users in Elite Redux:
Based on the species data, Motor Drive appears on:
- Various Electric/Fighting-type hybrids
- Speed-oriented Pokemon with Generator/Transistor abilities
- Rotom forme variants (Heat, Wash, Frost, Fan forms)
- Some custom Elite Redux species focusing on speed control

### Competitive Usage Notes:
- **Team Role**: Speed control and Electric-type switch-in
- **Held Items**: Focus Sash for survival, Choice items for immediate pressure after boost
- **Move Synergy**: Baton Pass to transfer accumulated Speed boosts
- **Positioning**: Use as a pivot against Electric-heavy teams

### Counters:
1. **Ability Bypass**: Mold Breaker, Teravolt, Turboblaze users
2. **Non-Electric Paralysis**: Body Slam, Glare, Stun Spore
3. **Priority Moves**: Bypass accumulated Speed advantage
4. **Status Moves**: Sleep, confusion, other non-Electric debuffs
5. **Trapping**: Prevent switching to build Speed safely

### Synergies:
- **Thunder Wave Support**: Teammates can set up paralysis while Motor Drive user is immune
- **Electric Terrain**: Team benefits from terrain while Motor Drive user is unaffected by passive damage
- **Baton Pass Chains**: Pass accumulated Speed boosts to sweepers
- **Dual Screens**: Extra setup time to accumulate multiple Speed boosts

### Version History:
- **Gen 4 Introduction**: Original implementation as Electric immunity + Speed boost
- **Elite Redux**: Maintains standard mechanics with expanded move pool interactions
- **Current Status**: Functions identically to mainline games with full Electric-type move coverage
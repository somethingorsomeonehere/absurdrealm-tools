---
id: 71
name: Arena Trap
status: reviewed
character_count: 211
---

# Arena Trap - Ability ID 71

## In-Game Description
"Enemies can't flee. Ghosts and ungrounded Pokemon are immune."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all non-levitating or Ghost-type foes from switching out. Pokemon holding Shed Shell or using a pivot move such as Flip Turn can escape. Activates during the next turn if the user switches in mid battle

## Detailed Mechanical Explanation
*For Discord/reference use*

**ARENA TRAP** is a trapping ability that prevents certain opposing Pokemon from fleeing or switching out voluntarily.

### Activation Mechanics:
- **Trigger**: Passive effect while the Pokemon is on the battlefield
- **Target**: Grounded opposing Pokemon only
- **Function**: onTrap hook that checks if the switching Pokemon is grounded

### Trapping Conditions:
Arena Trap prevents escape if ALL of the following are true:
1. **Target is grounded**: Must pass IsBattlerGrounded() check
2. **Target is opposing**: Does not affect allies in double battles
3. **Target is not Ghost-type**: Ghost-types are immune (Gen 6+ behavior)
4. **Target doesn't have Shed Shell**: Shed Shell bypasses all trapping effects

### Immunity Conditions:
The following Pokemon are **immune** to Arena Trap:
- **Flying-type Pokemon**: Always immune due to not being grounded
- **Pokemon with Levitate**: Ability makes them ungrounded
- **Pokemon affected by Magnet Rise**: Temporary levitation
- **Pokemon holding Air Balloon**: Item-based levitation
- **Pokemon affected by Telekinesis**: Move-based levitation
- **Ghost-type Pokemon**: Type-based immunity (Gen 6+ rule)
- **Pokemon with Shed Shell**: Item bypasses all trapping

### Interaction Rules:
- **vs Double Battles**: Only affects opposing Pokemon, not allies
- **vs Grounding Effects**: Iron Ball, Gravity, Ingrain, etc. can make Flying-types vulnerable
- **vs Run Away**: Shed Shell and Ghost-type immunity override Run Away ability
- **vs Wild Battles**: Prevents fleeing from wild Pokemon battles

### Technical Implementation:
```c
constexpr Ability ArenaTrap = {
    .onTrap = +[](ABILITY_ON_TRAP) -> int { 
        return IsBattlerGrounded(switchingBattler); 
    },
};
```

The ability simply checks if the Pokemon trying to switch is grounded. All other immunity checks (Ghost-type, Shed Shell, etc.) are handled by the battle system's escape logic.

### Competitive Notes:
- Extremely powerful for revenge killing and trapping setup sweepers
- Pairs well with fast attackers that can KO trapped Pokemon
- Countered by switching to Ghost-types or Flying-types
- Air Balloon is a common item specifically to counter trapping abilities
- Shed Shell is the universal counter to all trapping abilities

### Related Abilities:
- **Shadow Tag**: Traps all Pokemon except those with Shadow Tag
- **Magnet Pull**: Traps Steel-type Pokemon specifically
- **Mean Look/Block**: Move-based trapping with different rules

### Version History:
- Gen 3-5: Worked on all non-Flying, non-Levitate Pokemon
- Gen 6+: Ghost-types became immune (Elite Redux follows this rule)
- Elite Redux: Full Gen 6+ implementation with Ghost immunity
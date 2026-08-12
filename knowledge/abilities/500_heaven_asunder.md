---
id: 500
name: Heaven Asunder
status: reviewed
character_count: 117
---

# Heaven Asunder - Ability ID 500

## In-Game Description
"Spacial Rend always crits. Ups crit level by +1."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees Spacial Rend always lands critical hits and increases critical hit ratio by one stage for all other moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Heaven Asunder is Palkia's signature ability that provides two distinct critical hit bonuses. The ability has special interaction with Spacial Rend while providing general critical hit enhancement for all other moves.

### Activation Conditions
- **Spacial Rend**: Automatically lands critical hits (100% crit rate)
- **All other moves**: Critical hit ratio increased by +1 stage
- **Passive ability**: Always active when not suppressed
- **No HP requirement**: Works at any HP level

### Critical Hit Stages
In Elite Redux, critical hit stages work as follows:
- Stage 0: 6.25% (1/16) base crit rate
- Stage +1: 12.5% (2/16) crit rate - Heaven Asunder bonus
- Stage +2: 25% (4/16) crit rate
- Stage +3: 50% (8/16) crit rate
- Stage +4: 100% guaranteed crit

### Technical Implementation
```c
// Heaven Asunder implementation in abilities.cc
constexpr Ability HeavenAsunder = {
    .onCrit = +[](ON_CRIT) {
        if (move == MOVE_SPACIAL_REND) return ALWAYS_CRIT;  // Guaranteed crit
        return 1;  // +1 crit stage for other moves
    },
};
```

### Important Interactions
- **Focus Energy**: Stacks with Heaven Asunder (+1 + +2 = +3 total)
- **Super Luck**: Stacks with Heaven Asunder (+1 + +1 = +2 total)
- **Razor Claw/Scope Lens**: Stacks with Heaven Asunder (+1 + +1 = +2 total)
- **High crit moves**: Moves like Slash get +1 stage on top of their natural bonus
- **Battle Armor/Shell Armor**: Prevents crits even from guaranteed Spacial Rend
- **Lucky Chant**: Blocks crits for 5 turns, affecting all moves including Spacial Rend

### Spacial Rend Synergy
Spacial Rend (Move 460) is Palkia's signature move:
- **Base Power**: 100
- **Accuracy**: 95%
- **Type**: Dragon
- **Category**: Special
- **PP**: 5
- **Natural crit rate**: Already high (Stage +1)
- **With Heaven Asunder**: Guaranteed critical hit (Stage +4)

### Strategic Implications
- **Signature synergy**: Perfect match with Palkia's signature move
- **Consistent damage**: Spacial Rend becomes completely reliable
- **General improvement**: All moves become more threatening
- **Coverage moves**: Physical attacks benefit from crit chance
- **Wall breaking**: Critical hits ignore stat drops and some defensive abilities
- **Momentum building**: High crit rate creates pressure and KO opportunities

### Common Users
- **Palkia**: Primary user with natural Spacial Rend access
- **Origin Palkia**: Enhanced stats with same ability
- **Legendary tier**: Matches the power level of other legendary abilities

### Competitive Usage Notes
- **Wallbreaker role**: Excellent for breaking through defensive cores
- **Mixed sets**: Benefits both physical and special attacks
- **Prediction reward**: High crit rate punishes passive play
- **Pressure tool**: Forces opponents to play more aggressively
- **Signature move abuse**: Spacial Rend becomes a nuclear option

### Damage Calculations
Critical hits in Elite Redux:
- **Damage multiplier**: 1.5x damage (same as mainline)
- **Stat interaction**: Ignores target's positive stat changes
- **Ability interaction**: Ignores some defensive abilities
- **Item interaction**: Life Orb recoil still applies to crits

### Counters
- **Battle Armor/Shell Armor**: Completely negates critical hits
- **Lucky Chant**: Temporary protection from all critical hits
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Sturdy**: Survives guaranteed OHKO from full HP
- **Focus Sash**: Survives one critical hit if at full HP
- **Eviolite users**: High bulk can tank even critical hits

### Synergies
- **Focus Energy**: Stacks for even higher crit rate
- **Super Luck**: Additional crit boost for non-Spacial Rend moves
- **Razor Claw/Scope Lens**: Item support for maximum crit rate
- **High critical hit moves**: Slash, Psycho Cut, etc. become very reliable
- **Spatial moveset**: Pairs with Palkia's naturally diverse movepool

### Movepool Considerations for Palkia
Palkia's movepool benefits greatly from Heaven Asunder:
- **Spacial Rend**: Guaranteed critical hit signature move
- **Hydro Pump**: High-power special move with crit chance
- **Thunder**: Perfect accuracy in rain with crit potential
- **Earth Power**: Coverage move that benefits from crits
- **Dragon Pulse**: Reliable STAB with enhanced crit rate
- **Earthquake**: Physical option that loves critical hits

### Version History
- **Elite Redux exclusive**: Custom ability for legendary balance
- **Palkia signature**: Reflects the Pokemon's spatial manipulation theme
- **Thematic design**: Represents tearing through space-time itself
- **Power level**: Appropriate for restricted legendary tier

### Design Philosophy
Heaven Asunder embodies Palkia's role as the master of space, with the ability representing its power to tear through dimensional barriers and strike with overwhelming force. The guaranteed critical hit on Spacial Rend makes thematic sense - when Palkia rends space itself, there's no defense against such a fundamental attack.
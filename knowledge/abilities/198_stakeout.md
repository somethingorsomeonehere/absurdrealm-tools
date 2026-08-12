---
id: 198
name: Stakeout
status: reviewed
character_count: 105
---

# Stakeout - Ability ID 198

## In-Game Description
"Deals double damage to opponents being switched in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deals double damage to opponents that just switched in. Only works right after they switch in for 1 turn.


## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Stakeout doubles the damage of all moves used against a Pokemon that just switched into battle. The ability uses the `isFirstTurn` volatile battle state to determine when a Pokemon has switched in.

### Activation Conditions
- Target must have `gVolatileStructs[target].isFirstTurn == 2`
- This value is set to 2 when a Pokemon switches in or is sent out initially
- The value decrements by 1 each turn, becoming 1 after the first turn, then 0
- Only triggers on the exact turn the Pokemon switches in (isFirstTurn == 2)

### Technical Implementation
```cpp
constexpr Ability Stakeout = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gVolatileStructs[target].isFirstTurn == 2) MUL(2.0);
        },
};
```

### Numerical Values
- **Damage Multiplier**: 2.0x (doubles damage)
- **Duration**: Only the turn the target switches in
- **Move Coverage**: All offensive moves that deal damage

### Affected Moves
- All damaging moves (physical, special, and status moves that deal damage)
- Multi-hit moves (each hit gets the multiplier)
- Fixed damage moves like Seismic Toss
- Does NOT affect status moves that don't deal damage

### Interactions with Other Abilities/Mechanics
- **Overwatch**: Hybrid ability that combines On the Prowl (entry hazard detection) with Stakeout's damage multiplier
- **Payback**: Has different switch-in detection logic (`isFirstTurn != 2` check) - Stakeout and Payback have opposite conditions
- **Speed Boost**: Specifically excludes the first turn after switching (`isFirstTurn != 2` check)
- **Fort Knox**: Cannot be bypassed - Stakeout is not listed as an exception to Fort Knox's ability blocking

### Strategic Implications
- **Wallbreaker Role**: Exceptional at punishing defensive switches and pivoting
- **Momentum Control**: Discourages opponent switching, maintaining offensive pressure
- **Prediction Reward**: Rewards accurate prediction of opponent switches
- **Late Game Power**: Particularly strong in endgame scenarios with limited switch options

### Example Damage Calculations
Assuming a base 100 power move with standard conditions:
- **Normal damage**: 100 base power
- **With Stakeout**: 200 base power (2.0x multiplier)
- **Combined with STAB**: 300 base power (2.0x Stakeout x 1.5x STAB)

### Common Users in Elite Redux
- **Gumshoos line**: Yungoos and Gumshoos have Stakeout as a changeable ability
- **Golett line**: Golett and Golurk have Stakeout as an innate ability
- **Sableye line**: Sableye and Mega Sableye have Stakeout as a changeable ability
- **Pawniard line**: Pawniard and Bisharp have Stakeout as a changeable ability
- **Various others**: Including Lycanroc-Dusk, Crobat line, and several custom Elite Redux Pokemon

### Competitive Usage Notes
- **Entry Hazard Synergy**: Combines well with Stealth Rock and Spikes to limit switching
- **Choice Item Synergy**: Choice Band/Specs users become extremely threatening to switch-ins
- **U-turn/Volt Switch Counter**: Punishes common pivoting moves severely
- **Doubles/VGC**: Less effective due to targeting restrictions and protect usage

### Counters
- **Protect/Detect**: Opponent can use protection moves to waste the Stakeout turn
- **Fast Revenge Killers**: Speed control can prevent Stakeout users from capitalizing
- **Substitute**: Can block the doubled damage if set up beforehand
- **Fort Knox**: Completely negates Stakeout (and most other offensive abilities)
- **Priority Moves**: Can KO Stakeout users before they act

### Synergies
- **Choice Items**: Massive damage output against switch-ins
- **Life Orb**: Stacks with the 2x multiplier for extreme power
- **Entry Hazards**: Limits switching options, forcing opponents into Stakeout range
- **Slow Pivots**: U-turn/Volt Switch users can bring in Stakeout users safely
- **Pursuit**: (If available) Traps Pokemon trying to avoid the doubled damage

### Version History
- Introduced in Generation 7 (Sun/Moon) as Gumshoos's signature ability
- In Elite Redux: Expanded to multiple Pokemon as both changeable and innate abilities
- Maintained original 2x damage multiplier and switch-in detection mechanics
- Added to hybrid abilities like Overwatch for increased utility
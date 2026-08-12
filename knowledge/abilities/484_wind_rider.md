---
id: 484
name: Wind Rider
status: reviewed
character_count: 178
---

# Wind Rider - Ability ID 484

## In-Game Description
"Tailwind entry boost + wind move absorption."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's highest attacking stat when entering battle under Tailwind. When hit by wind-based moves, absorbs the attack and raises the highest attacking stat by one stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Wind Rider combines Tailwind synergy with wind move absorption, creating a Pokemon that thrives in aerial conditions and benefits from wind-based attacks.

### Dual Effect Components

#### Tailwind Entry Boost
- **Trigger**: Activates when entering battle while Tailwind is active on user's side
- **Effect**: Raises the Pokemon's highest attacking stat by 1 stage
- **Stat determination**: Compares Attack and Special Attack (including current modifiers)
- **Timing**: Immediate upon switch-in during Tailwind

#### Wind Move Absorption
- **Trigger**: When hit by air-based moves
- **Effect**: Completely negates damage and raises highest attacking stat by 1 stage
- **Affected moves**: Gust, Hurricane, Tailwind, and other moves with airBased flag
- **Benefit**: Turns wind attacks into stat boosts

### Technical Implementation
```c
constexpr Ability WindRider = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(gSideStatuses[GET_BATTLER_SIDE(battler)] & SIDE_STATUS_TAILWIND)
        u8 statId = GetHighestAttackingStatId(battler, TRUE);
        CHECK(CanRaiseStat(battler, statId))
        RaiseStat(battler, statId, 1, TRUE, FALSE);
        return TRUE;
    },
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(gBattleMoves[move].airBased)
        u8 statId = GetHighestAttackingStatId(battler, TRUE);
        CHECK(CanRaiseStat(battler, statId))
        RaiseStat(battler, statId, 1, TRUE, FALSE);
        return TRUE;
    },
    .breakable = TRUE,
};
```

### Wind-Based Moves
**Commonly absorbed moves:**
- Gust (Flying-type, 40 BP)
- Hurricane (Flying-type, 110 BP)
- Tailwind (Flying-type status move)
- Whirlwind (Normal-type, forces switching)
- Bleakwind Storm (Flying-type, 100 BP)

### Strategic Applications
- **Tailwind teams**: Perfect synergy with speed control strategies
- **Wind immunity**: Complete protection against wind-based attacks
- **Stat accumulation**: Multiple ways to boost attacking stats
- **Switch-in timing**: Rewards switching during Tailwind
- **Anti-Hurricane**: Hard counter to Hurricane users

### Tailwind Synergy
- **Setup reward**: Benefits immediately from team Tailwind setup
- **Doubled benefit**: Speed boost from Tailwind + stat boost from ability
- **Priority switching**: Enhanced value of switching during Tailwind turns
- **Team coordination**: Encourages Tailwind support from teammates

### Competitive Usage
- **Tailwind sweepers**: Excellent on teams built around Tailwind setup
- **Wind counters**: Reliable answer to wind-based offense
- **Mixed attackers**: Benefits regardless of physical/special preference
- **Dynamic switching**: Rewards tactical switch timing
- **Weather teams**: Synergizes with flying-type weather effects

### Wind Move Interactions
**Strategy against common winds:**
- Hurricane: Complete immunity + stat boost
- Gust: Absorbs weak early-game moves for setup
- Tailwind: Can absorb opposing team's Tailwind for benefit
- Whirlwind: Prevents forced switching while gaining stats

### Limitations
- **Ability suppression**: Breakable by Mold Breaker effects
- **Non-wind moves**: Only helps against specific move types
- **Tailwind dependency**: Entry effect requires active Tailwind
- **One boost per hit**: Each absorption only gives 1 stage
- **Stat cap**: Cannot exceed +6 stat stages

### Counters
- **Mold Breaker family**: Suppresses the entire ability
- **Non-wind attacks**: Physical/special moves that aren't air-based
- **Stat reset**: Haze, Clear Smog remove accumulated boosts
- **Taunt**: Prevents Tailwind setup for entry synergy
- **Ground moves**: Typically not air-based, bypass absorption

### Team Building
**Ideal partners:**
- Tailwind setters: Whimsicott, Suicune, Crobat
- Wind move users: Can set up Wind Rider with friendly wind moves
- Speed control: Trick Room as alternative to Tailwind
- Stat passers: Baton Pass to transfer accumulated boosts

### Item Synergies
- **Choice items**: Benefit from guaranteed stat boosts
- **Life Orb**: Amplify boosted attacking stats
- **Weakness Policy**: Additional stat boost opportunity
- **Sitrus Berry**: HP recovery while accumulating boosts

### Version History
- Elite Redux custom ability for wind-based battle strategies
- Designed to create Tailwind synergy and wind immunity
- Part of expanded weather and field effect ability system
- Encourages aerial battlefield control tactics
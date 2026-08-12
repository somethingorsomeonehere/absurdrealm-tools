---
id: 350
name: Violent Rush
status: reviewed
character_count: 93
---

# Violent Rush - Ability ID 350

## In-Game Description
"Gains 50% Speed and 20% Attack boost on first turn after switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user gains a 50% Speed boost and 20% Attack boost on their first turn after switching in. 

## Detailed Mechanical Explanation

### Overview

**Violent Rush** is a powerful first-turn ability that provides immediate offensive presence upon switch-in. The Pokemon gains a significant Speed boost of 50% and an Attack boost of 20% for their first turn on the battlefield, creating explosive opening plays that can catch opponents off-guard.

## Mechanics

### Implementation Details

The ability is implemented across multiple files in the Elite Redux codebase:

#### Switch-in Setup (`src/abilities.cc:3709-3714`)
```cpp
constexpr Ability ViolentRush = {
    .onEntry = +[](ON_ENTRY) -> int {
        gVolatileStructs[battler].violentRush = gVolatileStructs[battler].started.violentRush = TRUE;
        return SwitchInAnnounce(B_MSG_SWITCHIN_VIOLENT_RUSH);
    },
};
```

#### Attack Stat Boost (`src/battle_util.c:7010`)
```c
// Violent Rush
if (gVolatileStructs[battler].violentRush) statBase = statBase * 6 / 5;
```
- Attack multiplier: **1.2x** (6/5 = 1.2)
- Percentage increase: **+20%**

#### Speed Stat Boost (`src/battle_main.c:4067`)
```c
if (gVolatileStructs[battler].violentRush) speed = (speed * 150) / 100;
```
- Speed multiplier: **1.5x** (150/100 = 1.5)
- Percentage increase: **+50%**

#### Turn Duration (`src/battle_util.c:2822`)
```c
CLEAR_ONE_TURN(violentRush)
```
The `violentRush` flag is cleared at the end of each turn, ensuring the boost only lasts one turn.

### Switch-in Message

When a Pokemon with Violent Rush enters battle, it displays the message:
**"{Pokemon name} charges onto the battlefield!"**

## Strategic Applications

### Offensive Sweeping
- The 50% Speed boost allows normally slower Pokemon to outspeed threats on the first turn
- Combined with the 20% Attack boost, enables powerful opening attacks
- Ideal for revenge killing or breaking through defensive walls

### Lead Positioning
- Excellent for lead Pokemon that need immediate pressure
- Forces opponents to respect the threat or risk taking significant damage
- Can secure crucial KOs before opponents can react

### Hit-and-Run Tactics
- Switch in, deliver a powerful attack, then potentially switch out
- Forces opponents to make difficult predictions about staying in
- Creates momentum through immediate offensive presence

### Revenge Killing
- Perfect for revenge killing threats after a teammate faints
- The Speed boost ensures outspeeding most opponents
- Attack boost guarantees significant damage output

## Competitive Analysis

### Strengths
- **Immediate Impact**: No setup turns required
- **Speed Control**: 50% Speed boost can outpace most threats
- **Offensive Pressure**: 20% Attack boost enhances damage output
- **Unpredictability**: Opponents must respect the threat immediately
- **Tempo Control**: Creates immediate offensive momentum

### Limitations
- **One Turn Only**: Boosts disappear after the first turn
- **Timing Dependent**: Must switch in at the right moment
- **Switch-in Hazards**: Vulnerable to entry hazards reducing effectiveness
- **No Defense**: Provides no defensive benefits
- **Prediction Required**: Requires good game sense to maximize impact

### Synergies
- **Choice Items**: Choice Band/Scarf synergize well with the stat boosts
- **Priority Moves**: High Speed ensures priority moves hit hard
- **Coverage Moves**: Wide movepool coverage maximizes first-turn potential
- **U-turn/Volt Switch**: Can maintain momentum after the boosted turn

## Related Abilities

### Direct Combinations
- **Showdown Mode**: Combines Violent Rush with Ambush (guaranteed crits)
- **Champion's Entrance**: Combines Violent Rush with Intimidate

### Similar Effects
- **Rapid Response**: Also provides 50% Speed boost on first turn
- **Readied Action**: Provides Attack doubling on first turn
- **Ambush**: Provides guaranteed critical hits on first turn

### Competitive Comparison
- More balanced than Readied Action (20% vs 100% Attack boost)
- Less specialized than Ambush (stat boosts vs guaranteed crits)
- Similar to Rapid Response but includes Attack boost

## Notable Pokemon

Based on the species list, 52 Pokemon have access to Violent Rush, including:

### Primary Ability Users
- **Nidorino** (SPECIES_NIDORINO) - Line 5728
- Various other species with different roles and stat distributions

### Innate Ability Users
- Multiple Pokemon have Violent Rush as an innate ability, making it always active alongside their regular abilities

## Technical Notes

### Code References
- **Ability Definition**: `src/abilities.cc:3709-3714`
- **Attack Calculation**: `src/battle_util.c:7010`
- **Speed Calculation**: `src/battle_main.c:4067`
- **Turn Cleanup**: `src/battle_util.c:2822`
- **Message Display**: `src/battle_message.c:802, 2029`
- **Constant Definition**: `include/generated/constants/abilities.h:356`

### Message Strings
- **Switch-in Text**: `"{B_ATK_NAME_WITH_PREFIX} charges onto the battlefield!"`
- **String ID**: `STRINGID_VIOLENT_RUSH`
- **Battle Message**: `B_MSG_SWITCHIN_VIOLENT_RUSH`

### Stat Calculation Integration
The ability integrates seamlessly with the battle stat calculation system:
- Attack boost applied in `CalculateStat` function before other modifiers
- Speed boost applied in `GetSpeedFromAbilities` before paralysis checks
- Properly cleared at turn end to prevent permanent boosts


## Conclusion

Violent Rush is a high-impact ability that rewards aggressive play and smart switching. The combination of Speed and Attack boosts creates immediate offensive threats that force opponents to make difficult decisions. While limited to one turn, the ability's power lies in its unpredictability and ability to swing momentum in crucial moments. Its widespread distribution across 52 Pokemon makes it a common sight in competitive play, where timing and game sense determine its effectiveness.
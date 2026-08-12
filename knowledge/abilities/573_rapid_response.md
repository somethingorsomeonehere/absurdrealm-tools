---
id: 573
name: Rapid Response
status: reviewed
character_count: 101
---

# Rapid Response - Ability ID 573

## In-Game Description
"Boosts Speed by 50% + SpAtk by 20% on first turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user gains a 50% Speed boost and 20% Special Attack boost on their first turn after switching in.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Speed Boost**: 50% increase (1.5x multiplier) to Speed stat on first turn only
- **Special Attack Boost**: 20% increase (1.2x multiplier) to Special Attack stat on first turn only
- **Duration**: Only active on the first turn after switch-in or battle start
- **Activation**: Automatically triggers when the Pokemon enters battle

### Activation Conditions
- Triggers immediately upon switch-in to battle
- Triggers at battle start if the Pokemon is in the lead position
- Does not retrigger if the Pokemon switches out and back in during the same battle

### Technical Implementation
```c
// In abilities.cc - Entry handler
constexpr Ability RapidResponse = {
    .onEntry = +[](ON_ENTRY) -> int {
        gVolatileStructs[battler].rapidResponse = gVolatileStructs[battler].started.rapidResponse = TRUE;
        return SwitchInAnnounce(B_MSG_SWITCHIN_RAPID_RESPONSE);
    },
};

// In battle_main.c - Speed calculation
if (gVolatileStructs[battlerId].rapidResponse) speed = (speed * 150) / 100;

// In battle_util.c - Special Attack calculation
if (gVolatileStructs[battler].rapidResponse) statBase = statBase * 6 / 5;

// In battle_util.c - Turn cleanup
CLEAR_ONE_TURN(rapidResponse)
```

### Numerical Values
- **Speed Multiplier**: 1.5x (150/100 = +50%)
- **Special Attack Multiplier**: 1.2x (6/5 = +20%)
- **Duration**: 1 turn only

### Affected Calculations
- **Speed Priority**: Determines turn order for the first turn
- **Special Attack Damage**: Enhances damage of special moves on first turn
- **Move Selection**: AI considers enhanced stats when choosing moves

### Strategic Implications
- **Sweeper Setup**: Ideal for special attackers that need to outspeed and KO opponents
- **Revenge Killing**: Allows slower Pokemon to revenge kill faster threats
- **First Turn Advantage**: Provides immediate offensive pressure
- **Choice Item Synergy**: Works well with Choice Specs for massive first-turn damage

### Example Damage Calculations
```
Base 100 Special Attack with Choice Specs + Rapid Response:
- Normal: 100 x 1.5 (Choice Specs) = 150
- With Rapid Response: 100 x 1.2 x 1.5 = 180 (20% additional boost)

Speed comparison (Base 80 Speed):
- Normal: 80
- With Rapid Response: 80 x 1.5 = 120 (outspeed base 119 threats)
```

### Common Users
- Special attackers with moderate Speed stats
- Pokemon that need to outspeed specific threats
- Glass cannon Pokemon that need first-turn momentum
- Revenge killers that need guaranteed speed control

### Competitive Usage Notes
- **First Turn Impact**: Provides immediate board control
- **Switch-In Timing**: Must be timed carefully since effect only lasts one turn
- **Team Building**: Pairs well with aggressive team compositions
- **Prediction Required**: Opponent may switch to resist the boosted attack

### Counters
- **Priority Moves**: Bypass the Speed boost entirely
- **Switch-Out**: Opponent can switch to a resistant Pokemon
- **Status Moves**: Paralyze or sleep the user to waste the boost
- **Protect/Detect**: Stall out the one-turn effect

### Synergies
- **Choice Items**: Maximize the damage output on first turn
- **Life Orb**: Stack damage multipliers for massive first-turn power
- **Weather**: Pairs with weather-boosted moves for additional damage
- **Terrain**: Electric/Psychic Terrain for priority/power boosts

### Version History
- **Elite Redux**: Custom ability designed for aggressive playstyles
- **Implementation**: Uses volatile battle structure system for turn-based effects
- **Balance**: Limited to one turn to prevent being overpowered
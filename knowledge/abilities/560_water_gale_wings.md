---
id: 560
name: Water Gale Wings
status: reviewed
character_count: 55
---

# Water Gale Wings - Ability ID 560

## In-Game Description
"Water-type moves get +1 priority at max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to Water-type moves when at full HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Water Gale Wings (displayed as "Tidal Rush" in-game) is a clone of the Gale Wings ability that specifically affects Water-type moves instead of Flying-type moves. The ability implementation uses the `GALE_WINGS_CLONE(TYPE_WATER)` macro.

### Activation Conditions
- The Pokemon must be at maximum HP (`BATTLER_MAX_HP(battler)` returns true)
- The move being used must be Water-type (checked via `GetTypeBeforeUsingMove(move, battler) == TYPE_WATER`)
- When both conditions are met, the move receives +1 priority

### Technical Implementation
```cpp
constexpr Ability WaterGaleWings = {
    .onPriority = GALE_WINGS_CLONE(TYPE_WATER),
};

#define GALE_WINGS_CLONE(type)                               \
    +[](ON_PRIORITY) -> int {                                \
        CHECK(GetTypeBeforeUsingMove(move, battler) == type) \
        CHECK(BATTLER_MAX_HP(battler))                       \
        return 1;                                            \
    }
```

### Priority System Details
- Standard priority moves: +1 (Quick Attack, Aqua Jet)
- Water Gale Wings boost: +1 additional priority
- Result: Water-type moves at max HP get +1 priority over normal moves
- Still subject to speed tiebreakers within the same priority bracket

### Affected Moves
All Water-type moves benefit from the priority boost, including but not limited to:
- **Powerful STAB moves**: Hydro Pump, Surf, Scald, Water Pulse
- **Status moves**: Water Sport, Rain Dance, Aqua Ring
- **Physical moves**: Waterfall, Liquidation, Crabhammer
- **Multi-hit moves**: Water Shuriken (if user is Water-type)
- **Already priority moves**: Aqua Jet becomes +2 priority

### Pokemon That Have This Ability
Based on the Elite Redux species data, several Pokemon have access to Water Gale Wings either as a regular ability or innate ability, including various Water-type specialists and some mixed-type Pokemon. The ability appears on both offensive sweepers and more defensive Water-types.

### Competitive Applications
**Offensive Sweeping**: Allows Water-type attackers to outspeed common priority moves and revenge kill efficiently. Particularly powerful on fast, frail attackers who can maintain max HP through careful play.

**Early Game Dominance**: Provides significant early-game pressure since most Pokemon start battles at full HP, making the first few turns particularly threatening.

**Priority War Advantage**: Gives Water-types an edge in priority move exchanges, as +1 priority Water moves will outspeed most common priority moves.

### Comparison to Regular Gale Wings
- **Gale Wings**: Affects Flying-type moves (Brave Bird, Acrobatics, etc.)
- **Water Gale Wings**: Affects Water-type moves (Hydro Pump, Surf, etc.)
- **Identical mechanics**: Both require max HP for activation
- **Type coverage**: Water-type moves often have better neutral coverage than Flying-type moves

### Strategic Applications
1. **Lead Pokemon**: Excellent on lead Pokemon who start at full HP
2. **Switch-in sweepers**: Pairs well with healing moves or items to maintain max HP
3. **Glass cannon builds**: Maximizes the effectiveness of frail but powerful Water attackers
4. **Priority control**: Allows Water-types to control the pace of battle in early turns

### Counterplay
- **Chip damage**: Any damage that brings the user below max HP disables the ability
- **Multi-hit moves**: Moves like Bullet Seed can quickly break the max HP requirement
- **Entry hazards**: Stealth Rock, Spikes, etc. prevent the ability from activating on switch-in
- **Status conditions**: Poison, burn, etc. will eventually reduce HP below maximum
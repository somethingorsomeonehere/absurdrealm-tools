---
id: 585
name: Sun Basking
status: reviewed
character_count: 126
---

# Sun Basking - Ability ID 585

## In-Game Description
"Provides dual protection in harsh sunlight: priority immunity and physical damage reduction."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Blocks priority moves and reduces physical attack damage by 50% in sun. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation

Sun Basking is a powerful weather-dependent defensive ability that transforms harsh sunlight into a protective shield. It combines priority immunity with physical damage reduction, making it a cornerstone ability for sun-based defensive strategies.

### Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Implementation**: Uses QueenlyMajesty's priority immunity + custom defensive multiplier

### Core Mechanics
```cpp
constexpr Ability SunBasking = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK(IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY));
        return QueenlyMajesty.onImmune(DELEGATE_IMMUNE);
    },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY) && IS_MOVE_PHYSICAL(move)) MUL(.5);
        },
    .breakable = TRUE,
};
```

### Mechanics Breakdown

### Priority Immunity (Sun Only)
- **Effect**: Complete immunity to all priority moves from opponents
- **Condition**: Only active during Sun or Harsh Sunlight
- **Scope**: Blocks moves with positive priority (Quick Attack, Mach Punch, etc.)
- **Implementation**: Inherits from Queenly Majesty's priority blocking

### Physical Damage Reduction
- **Multiplier**: 0.5x (50% reduction)
- **Type**: Physical moves only
- **Weather Required**: Sun or Harsh Sunlight
- **Stacking**: Multiplies with other defensive modifiers

### Breakable Property
- **Status**: Can be broken by Mold Breaker-like abilities
- **Implications**: Strong abilities can bypass Sun Basking's protection

### Strategic Applications

### Defensive Wall Role
- Becomes incredibly tanky against physical attackers in sun
- Priority immunity prevents revenge kills
- Synergizes with recovery moves and defensive stats

### Sun Team Anchor
- Provides defensive backbone for offensive sun teams
- Protects setup sweepers from priority revenge
- Creates safe switching opportunities

### Anti-Priority Tech
- Completely shuts down priority-based strategies
- Forces opponents to rely on regular speed tiers
- Invaluable against teams built around priority moves

### Synergies and Interactions

### Weather Synergies
- **Drought**: Auto-sets sun for immediate activation
- **Solar Power**: Offensive sun ability for team diversity
- **Chlorophyll**: Speed boost to outpace non-priority moves

### Move Synergies
- **Morning Sun**: Enhanced recovery in sun
- **Solar Beam**: No charge turn required
- **Synthesis**: Boosted healing amount

### Type Synergies
- Fire-types benefit from sun's fire boost + Sun Basking defense
- Grass-types resist common physical Ground/Rock moves
- Water-types can use sun to reduce their weakness

### Competitive Viability

### Tier: High
Sun Basking earns a high tier due to its potent defensive capabilities when active.

### Strengths
1. **Dual Protection**: Both priority immunity and damage reduction
2. **No Setup Required**: Instant activation with sun
3. **Wide Coverage**: Affects all physical moves and all priority
4. **Team Support**: Protects entire team from priority revenge

### Weaknesses
1. **Weather Dependent**: Useless without sun
2. **Special Vulnerability**: No protection against special attacks
3. **Breakable**: Can be bypassed by Mold Breaker variants
4. **Weather Wars**: Vulnerable to weather changes

### Notable Users

### Potential Candidates
- Fire-type defensive walls
- Sun-dependent Pokemon
- Bulky setup sweepers
- Support Pokemon on sun teams

### Counter Strategies

### Direct Counters
- **Weather Override**: Change weather to disable ability
- **Special Attacks**: Bypass physical damage reduction
- **Mold Breaker**: Ignore ability effects entirely
- **Status Moves**: Not affected by damage reduction

### Indirect Counters
- **Cloud Nine**: Negates weather effects
- **Sand/Hail Teams**: Natural weather competition
- **Stall Tactics**: Wait out sun turns

### Conclusion

Sun Basking represents Elite Redux's approach to weather-dependent abilities - powerful but conditional effects that reward weather control. Its combination of priority immunity and physical damage reduction makes it exceptionally strong when active, but complete dependence on sun weather creates clear counterplay.

The ability excels on defensive Pokemon that can capitalize on both effects while supporting sun teams. Its breakable status prevents it from being oppressive while maintaining its role as a premier sun-team defensive option.
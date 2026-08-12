---
id: 374
name: Big Leaves
status: reviewed
character_count: 208
---

# Big Leaves - Ability ID 374

## In-Game Description
"Chloroplast + Chlorophyll + Leaf Guard + Harvest + Solar Power."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Activates any sun related effects for the user's moves. Boosts Speed stat by 50% in sun. Cures status in sun. 50% chance to restore berry on turn end, 100% in sun. Raises highest attacking stat by 50% in sun.

## Technical Implementation

### Core Components
Big Leaves is implemented as a combination of five separate abilities:

#### 1. Harvest Component
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 1596-1606)
- **Function**: Restores consumed berries at the end of turn
- **Mechanics**: 
  - 100% chance in sun, 50% chance otherwise
  - Only works if the Pokemon has no held item
  - Only restores berries (pocket check: `POCKET_BERRIES`)

#### 2. Leaf Guard Component
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 1252-1259)
- **Function**: Heals status conditions in sun
- **Mechanics**: Cures all status ailments when sun is active

#### 3. Solar Power Component
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 1194-1200)
- **Function**: Boosts special attack in sun
- **Mechanics**: 1.5x multiplier to highest attacking stat in sun

#### 4. Chlorophyll Component
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 663-668)
- **Function**: Boosts speed in sun
- **Mechanics**: 1.5x speed multiplier in sun

#### 5. Chloroplast Property
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (line 3892)
- **Function**: Special property that affects Weather Ball and Solar Beam
- **Mechanics**:
  - Weather Ball gets 2x power boost (line 6607 in `battle_util.c`)
  - Solar Beam ignores power reduction in bad weather (lines 6920-6921 in `battle_util.c`)

### Implementation Details

```cpp
constexpr Ability BigLeaves = {
    .onEndTurn = +[](ON_END_TURN) -> int { 
        return Harvest.onEndTurn(DELEGATE_END_TURN) | LeafGuard.onEndTurn(DELEGATE_END_TURN); 
    },
    .onStat = +[](ON_STAT) {
        SolarPower.onStat(DELEGATE_STAT);
        Chlorophyll.onStat(DELEGATE_STAT);
    },
    .chloroplast = TRUE,
};
```

**Location**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (lines 3885-3893)

### Weather Ball Enhancement
- **Function**: `battle_util.c` line 6607
- **Effect**: Weather Ball receives 2x power when used by Pokemon with chloroplast property
- **Priority**: Applied before weather-based Weather Ball effects

### Solar Beam Protection
- **Function**: `battle_util.c` lines 6920-6921
- **Effect**: Solar Beam maintains full power in hail, sandstorm, rain, and fog
- **Mechanics**: Bypasses the 0.5x power reduction normally applied in adverse weather

## Strategic Analysis

### Strengths
1. **Sun Synergy**: All effects work optimally in sunny weather
2. **Multi-layered Benefits**: Five different advantages from a single ability slot
3. **Offensive Power**: 1.5x special attack boost in sun
4. **Speed Control**: 1.5x speed boost in sun for sweeping potential
5. **Sustainability**: Berry restoration and status healing
6. **Move Enhancement**: Weather Ball becomes a 100 base power move, Solar Beam ignores weather penalties

### Weaknesses
1. **Weather Dependency**: Most benefits require sun to activate
2. **Sun Vulnerability**: No protection against Fire-type attacks (unlike Solar Power alone)
3. **Berry Limitation**: Harvest only affects berries, not other consumables
4. **Competitive Weather**: Struggles when opposing weather abilities are present

### Optimal Conditions
- **Best Weather**: Harsh Sunlight (activates all benefits)
- **Recommended Moves**: Solar Beam, Weather Ball, any special attacks
- **Synergy Items**: Berries (Harvest compatibility), Heat Rock (sun extension)
- **Team Support**: Drought setters, sun team members

## Competitive Applications

### Set Recommendations
1. **Sun Sweeper**: Focus on high special attack moves with speed investment
2. **Weather Ball Abuser**: Capitalize on doubled Weather Ball power
3. **Solar Beam Tank**: Use Solar Beam's immunity to weather reduction
4. **Berry Cycling**: Utilize Harvest for repeated berry activation

### Damage Calculations
- **Weather Ball**: 50 base power to 100 base power (2x from chloroplast) to 150 base power in sun
- **Solar Beam**: 120 base power maintained in all weather conditions
- **Special Attacks**: 1.5x damage boost in sun from Solar Power component

### Counters and Checks
- **Weather Control**: Rain Dance, Sandstorm setters to remove sun
- **Priority Moves**: Bypass speed boost advantage
- **Physical Attackers**: Solar Power only boosts special attack
- **Fire Types**: Can threaten with sun-boosted attacks

## Related Abilities

### Component Abilities
- **Harvest** (#139): Berry restoration mechanic
- **Leaf Guard** (#102): Status immunity in sun
- **Solar Power** (#94): Special attack boost in sun
- **Chlorophyll** (#34): Speed boost in sun

### Similar Multi-Ability Fusions
- **Solar Flare** (#366): Fire-type fusion with chloroplast property
- **Chloroplast** (#268): Pure chloroplast ability

### Competitive Comparisons
- **Versus Chlorophyll**: Adds offensive power and utility
- **Versus Solar Power**: Adds speed, healing, and berry restoration
- **Versus Harvest**: Adds combat effectiveness and speed

## Version History
- **Elite Redux**: Introduced as ability #374
- **Current Status**: Active and competitively viable

## Notes
- One of the most comprehensive multi-ability fusions in Elite Redux
- The chloroplast property makes it unique among sun-based abilities
- Weather Ball interaction makes it a powerful offensive tool
- Requires sun support to reach full potential but offers incredible value when conditions are met
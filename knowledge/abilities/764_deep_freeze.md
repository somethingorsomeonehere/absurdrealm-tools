---
id: 764
name: Deep Freeze
status: reviewed
character_count: 150
---

# Deep Freeze - Ability ID 764

## In-Game Description
"Boosts Water and Ice by 1.25x. Halves Fire damage taken."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the damage of Water and Ice-type moves by 25%. Halves damage received from Fire-type moves. Multiplicative with other damage reduction sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Deep Freeze is a dual-purpose ability that provides both offensive and defensive benefits:

**Offensive Component:**
- Boosts Water-type and Ice-type moves by 25% (1.25x multiplier)
- Applied to moves used by the ability holder
- Functions as a type-specific damage boost similar to abilities like Sheer Force

**Defensive Component:**
- Reduces Fire-type damage taken by 50% (0.5x multiplier)
- Applied to Fire-type moves targeting the ability holder
- Functions as a type resistance modifier

### Technical Implementation
```cpp
constexpr Ability DeepFreeze = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_WATER || moveType == TYPE_ICE) MUL(1.25);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE) RESISTANCE(.5);
        },
    .breakable = TRUE,
};
```

### Numerical Values
- **Offensive Boost:** 1.25x (25% increase) for Water and Ice moves
- **Defensive Resistance:** 0.5x (50% reduction) for Fire damage
- **Breakable:** Yes (can be suppressed by Mold Breaker, etc.)

### Affected Moves
**Boosted Moves (Water-type):**
- Surf, Hydro Pump, Scald, Water Pulse, Aqua Jet, Waterfall, etc.
- All Water-type moves regardless of physical/special split

**Boosted Moves (Ice-type):**
- Ice Beam, Blizzard, Ice Punch, Icicle Crash, Freeze-Dry, etc.
- All Ice-type moves regardless of physical/special split

**Resisted Moves (Fire-type):**
- Flamethrower, Fire Blast, Overheat, Fire Punch, Flame Wheel, etc.
- All Fire-type moves regardless of physical/special split

### Interactions with Other Abilities/Mechanics

**Stacking with Other Modifiers:**
- Stacks multiplicatively with STAB (1.5x), items (Life Orb 1.3x), weather boosts, etc.
- Example: Water move with STAB + Deep Freeze + Life Orb = 1.5 x 1.25 x 1.3 = 2.4375x total

**Type Effectiveness Interactions:**
- Fire resistance stacks with natural type resistances
- Example: Water/Ice Pokemon takes Fire moves at 0.5x (Deep Freeze) x 0.5x (Water resistance) = 0.25x total

**Ability Interactions:**
- Can be suppressed by Mold Breaker, Teravolt, Turboblaze
- Cannot be copied by Trace (complex ability)
- Cannot be skill swapped
- Not affected by Simple or Unaware

### Strategic Implications

**Offensive Usage:**
- Provides significant power boost to dual STAB coverage
- Excellent for mixed attackers using both Water and Ice moves
- Makes weaker Water/Ice moves more viable due to consistent boost

**Defensive Usage:**
- Crucial Fire resistance for Ice-types (typically weak to Fire)
- Helps Water-types better handle Fire coverage moves
- Particularly valuable in formats with prevalent Fire-type threats

**Team Synergy:**
- Pairs well with Rain teams (Water moves already boosted by weather)
- Excellent in Hail teams (Ice moves get additional power)
- Good pivot ability for balanced teams needing Fire resistance

### Example Damage Calculations

**Offensive Example:**
- Frostula's Ice Beam (90 BP) with STAB + Deep Freeze:
- Base damage x 1.5 (STAB) x 1.25 (Deep Freeze) = 168.75 effective BP

**Defensive Example:**
- Fire Blast (110 BP) against Water-type with Deep Freeze:
- 110 x 0.5 (Water resistance) x 0.5 (Deep Freeze) = 27.5 effective BP

### Common Users
Based on the Elite Redux roster:
- **Pikachu Belle:** Electric-type forme with unique typing synergy
- **Dewpider Redux:** Water/Bug-type with enhanced Water STAB
- **Araquanid Redux:** Water/Bug evolution with powerful Water moves
- **Frostula:** Ice-type specialist utilizing both offensive and defensive benefits

### Competitive Usage Notes

**Advantages:**
- Dual utility (offense + defense) maximizes ability slot efficiency
- Strong synergy with Water/Ice dual-type Pokemon
- Consistent damage boost without drawbacks
- Excellent Fire-type matchup coverage

**Situational Benefits:**
- Strong in metas with prominent Fire-types
- Valuable for slow, bulky Water/Ice types
- Good for mixed attackers with diverse movesets

### Counters and Weaknesses

**Direct Counters:**
- Mold Breaker variants ignore the ability entirely
- Grass and Electric moves aren't affected by either component
- Strong physical attackers can overwhelm despite Fire resistance

**Strategic Counters:**
- Status moves bypass the offensive boost
- Entry hazards reduce effectiveness of switching
- Priority moves can revenge kill despite defensive boost

### Synergies

**Item Synergies:**
- Life Orb: Stacks with offensive boost for maximum damage
- Choice items: Consistent power boost with locked moves
- Leftovers/Sitrus Berry: Complements defensive Fire resistance

**Move Synergies:**
- Ice Beam + Surf: Dual STAB coverage with consistent boost
- Freeze-Dry: Super effective against Water-types with boost
- Priority moves like Aqua Jet: Boosted priority for revenge kills

**Team Synergies:**
- Rain teams: Double Water boost (weather + ability)
- Hail teams: Ice move synergy with weather
- Fire-weak teammates: Provides team Fire resistance

### Version History
- Introduced in Elite Redux as ID 764
- Designed as a balanced dual-utility ability
- Currently assigned to 4 Pokemon species as innate abilities
- Part of the extended ability system with hybrid offensive/defensive mechanics
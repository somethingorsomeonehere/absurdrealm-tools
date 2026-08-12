---
id: 804
name: Firefighter
status: reviewed
character_count: 213
---

# Firefighter - Ability ID 804

## In-Game Description
"Deals 1.5x damage to Fire. Takes 0.5x damage from Fire."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Deals 1.5x damage to Fire-type Pokemon and takes 0.5x damage when attacked by Fire-type Pokemon. Based on attacker/defender Pokemon types, not move types. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Firefighter is a dual-purpose ability that modifies damage calculations both offensively and defensively when Fire-type interactions occur.

**Offensive Multiplier:**
- When the user attacks a Fire-type Pokemon, damage is multiplied by 1.5x (50% increase)
- Applies to any move used against Fire-type targets, regardless of the move's type
- Calculated after type effectiveness but before other damage modifiers

**Defensive Multiplier:**
- When taking damage from Fire-type moves, incoming damage is multiplied by 0.5x (50% reduction)
- Applies regardless of the attacker's type - only the move type matters
- Calculated in the damage reduction phase

### Technical Implementation
```cpp
constexpr Ability Firefighter = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(target, TYPE_FIRE)) RESISTANCE(1.5);
        },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_BATTLER_OF_TYPE(attacker, TYPE_FIRE)) MUL(.5);
        },
    .breakable = TRUE,
};
```

### Activation Conditions
- **Offensive:** Target must be Fire-type (checked via `IS_BATTLER_OF_TYPE`)
- **Defensive:** Attacker must be Fire-type (move type determines this)
- Both effects are passive and automatic
- Ability can be suppressed by Mold Breaker effects (breakable = TRUE)

### Numerical Values
- Offensive boost: 1.5x damage multiplier (50% increase)
- Defensive reduction: 0.5x damage multiplier (50% reduction)
- These are direct multipliers applied to the final damage calculation

### Affected Moves
**Offensive Enhancement:** Any move used against Fire-type Pokemon
- Physical moves (Tackle, Earthquake, etc.)
- Special moves (Surf, Ice Beam, etc.)  
- Status moves that deal damage
- Multi-hit moves (each hit gets the boost)

**Defensive Reduction:** Any Fire-type move received
- Flamethrower, Fire Blast, Overheat
- Physical Fire moves like Fire Punch, Flare Blitz
- Multi-hit Fire moves (each hit is reduced)

### Interactions with Other Mechanics
- **Type Effectiveness:** Applied after type effectiveness calculations
- **STAB:** Stacks multiplicatively with Same Type Attack Bonus
- **Items:** Stacks with damage-boosting items like Life Orb
- **Weather:** Interacts normally with Sun/Rain damage modifiers
- **Critical Hits:** Applied to critical hit damage as well
- **Abilities:** Can be suppressed by Mold Breaker, Teravolt, Turboblaze

### Example Damage Calculations
**Offensive Example:**
- Base damage vs Fire-type: 100
- With Firefighter: 100 x 1.5 = 150 damage
- Net effect: +50 damage

**Defensive Example:**
- Incoming Fire-type damage: 100
- With Firefighter: 100 x 0.5 = 50 damage
- Net effect: -50 damage

**Combined Scenario:**
- Firefighter user uses Surf on Fire-type opponent
- Normal: Water vs Fire = 2x effectiveness
- With Firefighter: 2x x 1.5 = 3x total damage multiplier

### Strategic Implications
- **Role:** Fire-type counter and check
- **Best Users:** Water-types that naturally resist Fire moves
- **Timing:** Most effective in metas with prominent Fire-type threats
- **Coverage:** Provides both offensive pressure and defensive utility

### Common Users
Currently available to the Squirtle evolutionary line:
- **Squirtle** - Early game Fire counter
- **Wartortle** - Mid-game Fire resistance  
- **Blastoise** - Late game Fire specialist

These Water-types gain significant advantage against Fire opponents, making them premier Fire-type counters in the metagame.

### Competitive Usage Notes
- **Tier Impact:** Elevates Water-types in Fire-heavy metagames
- **Team Role:** Dedicated Fire-type check and counter
- **Switch-in Value:** High against Fire-type attackers
- **Offensive Presence:** Strong against Fire-type walls and tanks

### Counters and Limitations
**Counters:**
- Mold Breaker users bypass the ability entirely
- Non-Fire attackers ignore the defensive benefit
- Taunt prevents setup opportunities

**Limitations:**
- Only affects Fire-type interactions
- Provides no benefit against other types
- Can be suppressed by ability-suppressing moves
- Vulnerable to mixed attackers using non-Fire moves

### Synergies
**Item Synergies:**
- Life Orb: Stacks with offensive multiplier for massive Fire-type damage
- Leftovers: Provides longevity for repeated Fire-type encounters
- Choice items: Amplifies the already boosted Fire-type attacks

**Move Synergies:**
- Water-type STAB moves become extremely powerful vs Fire-types
- Coverage moves maintain their enhanced effectiveness
- Status moves benefit from the defensive Fire resistance

**Team Synergies:**
- Fire-weak teammates appreciate the dedicated Fire check
- Sun teams struggle against Firefighter users
- Pairs well with Ground-types for Fire/Electric coverage

### Version History
- Introduced in Elite Redux as ability ID 804
- Currently exclusive to Squirtle evolutionary line
- Part of the expanded 4-ability system implementation
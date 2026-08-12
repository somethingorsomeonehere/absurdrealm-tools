---
id: 399
name: Parry
status: reviewed
character_count: 153
---

# Parry - Ability ID 399

## In-Game Description
"Reduces damage by 20% and counters contact moves with Mach Punch."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces all damage by 20%. Multiplicative with other damage reduction sources. Counters contact moves with Mach Punch (40 BP Fighting-type, +1 priority).

## Detailed Mechanical Explanation

### Overview
Parry is an exceptional defensive ability that embodies the concept of turning defense into offense. This ability combines damage reduction with an immediate counter-attack, making it one of the most comprehensive defensive abilities in Elite Redux.

## Technical Implementation

### Source Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Lines**: 4118-4127
- **Function Reference**: Line 9243

### Core Mechanics
```cpp
constexpr Ability Parry = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK(IsMoveMakingContact(move, attacker))

        UseOutOfTurnAttack(battler, attacker, ability, MOVE_MACH_PUNCH, 0);
        return FALSE;
    },
    .onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) { MUL(.8); },
};
```

### Activation Conditions
1. **Contact Check**: The attacking move must make physical contact
2. **Hit Confirmation**: The attack must successfully hit the defender
3. **Battler Status**: The defending Pokemon must be able to act

### Damage Calculation
- **Defensive Multiplier**: 0.8x (20% damage reduction)
- **Applied To**: All incoming damage, regardless of move type
- **Stacks With**: Other defensive multipliers and abilities

## Strategic Analysis

### Offensive Component
- **Counter Move**: Mach Punch (40 BP, +1 Priority Fighting-type)
- **Timing**: Executes immediately after taking damage
- **Target**: Always targets the original attacker
- **Accuracy**: Uses Mach Punch's base accuracy (100%)

### Defensive Component
- **Damage Reduction**: 20% reduction on all attacks
- **Universal**: Works against all damage types
- **Consistent**: Always active, no turn limits or conditions

## Competitive Applications

### Tier Rating: High
Parry earns a High competitive tier rating due to its dual-purpose nature and consistent effectiveness.

### Strengths
1. **Dual Utility**: Provides both damage reduction and counter-attack capability
2. **Priority Revenge**: Mach Punch's +1 priority often allows revenge KOs
3. **Contact Punishment**: Heavily discourages physical contact moves
4. **Consistent Defense**: 20% damage reduction applies to all attacks
5. **No Resource Cost**: Requires no PP, items, or setup

### Weaknesses
1. **Contact Dependency**: Counter-attack only triggers on contact moves
2. **Fighting-Type Limitation**: Mach Punch can be resisted or ineffective
3. **Low Base Power**: 40 BP counter may not always be threatening
4. **No Special Coverage**: Only affects physical contact moves for counter

### Pokemon Synergy
**Ideal Candidates:**
- Bulky Fighting-types (maximizes Mach Punch STAB)
- Defensive pivots (benefits from consistent damage reduction)
- Pokemon with high Attack stats (maximizes counter damage)
- Tanks requiring offensive presence

**Stat Priorities:**
1. **HP/Defense**: Maximize survivability to trigger counter-attacks
2. **Attack**: Increase Mach Punch damage output
3. **Speed**: Less critical due to Mach Punch priority

## Competitive Interactions

### Ability Synergies
- **Iron Fist**: Boosts Mach Punch damage by 20%
- **Technician**: Increases Mach Punch power to 60 BP
- **Sheer Force**: Would affect Mach Punch if it had secondary effects

### Counter-Strategies
- **Non-Contact Moves**: Avoid triggering the counter-attack
- **Special Attacks**: Bypass the contact requirement entirely
- **Status Moves**: Can't trigger counter-attacks
- **Substitute**: Blocks direct contact with the Pokemon

### Related Abilities Comparison

#### Similar Counter Abilities
1. **Rough Skin**: Damages on contact but no damage reduction
2. **Iron Barbs**: Similar to Rough Skin but Steel-type focused
3. **Rocky Payload**: Contact-based counter with different move

#### Defensive Multiplier Abilities
1. **Battle Armor**: Same 20% reduction but includes crit immunity
2. **Filter/Solid Rock**: Reduces super-effective damage specifically
3. **Multiscale**: Reduces damage only at full HP

## Battle Scenarios

### Scenario 1: Physical Sweeper Counter
```
Opponent uses Close Combat (contact, physical)
to Parry reduces damage by 20%
to Immediately counters with Mach Punch
to Priority often secures revenge KO
```

### Scenario 2: Mixed Attacker
```
Opponent uses Flamethrower (non-contact, special)
to Parry reduces damage by 20%
to No counter-attack triggered
to Still provides defensive value
```

### Scenario 3: Setup Counter
```
Opponent uses Swords Dance (non-contact, status)
to No damage taken, no counter triggered
to Must rely on other defensive options
```

## Advanced Mechanics

### Interaction with Other Effects
- **Substitute**: Parry's counter bypasses Substitute to hit the real target
- **Wonder Guard**: Mach Punch must be super-effective to damage Wonder Guard users
- **Sturdy/Focus Sash**: Counter-attack can potentially break these effects

### Turn Order Implications
- Mach Punch's +1 priority often allows immediate revenge
- In same-priority scenarios, speed still determines order
- Can potentially KO before opponent can act again

## Historical Context

### Design Philosophy
Parry represents Elite Redux's approach to making defensive abilities more interactive and engaging. Rather than passive damage reduction, it creates dynamic battle scenarios where taking damage becomes an opportunity.

### Competitive Evolution
This ability addresses the traditional problem of purely defensive abilities being passive. By combining defense with offense, Parry creates meaningful decisions for both players.


## Conclusion

Parry stands out as one of Elite Redux's most well-designed abilities, successfully combining defensive utility with offensive pressure. Its consistent 20% damage reduction provides tangible bulk improvements, while the Mach Punch counter creates immediate threats against contact move users.

The ability's High tier rating reflects its versatility and consistent effectiveness across various battle scenarios. While it has specific weaknesses to non-contact attacks, its universal damage reduction ensures it provides value even when the counter-attack doesn't trigger.

As ability #399 - the final ability in our comprehensive analysis range - Parry serves as an excellent example of Elite Redux's innovative approach to ability design, creating dynamic, interactive gameplay mechanics that enhance competitive depth.

**Key Takeaway**: Parry transforms defensive positioning into offensive opportunity, making it an elite choice for Pokemon that need both survivability and revenge capabilities.
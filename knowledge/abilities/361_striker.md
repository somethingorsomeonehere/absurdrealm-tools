---
id: 361
name: Striker
status: reviewed
character_count: 76
---

# Striker - Ability ID 361

## In-Game Description
"Boosts the power of kicking moves by 30%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Striker increases the power of all kicking moves by 30%. Includes Pyro Ball.

## Detailed Mechanical Explanation

### Overview
Striker is an offensive ability that provides a 30% power boost to all kicking moves. This ability identifies kicking moves through the `FLAG_STRIKER_BOOST` flag system, covering both traditional kicks and modern kicking attacks.

## Mechanics

### Power Boost
- **Multiplier**: 1.3x (30% increase)
- **Trigger**: Any move with the `FLAG_STRIKER_BOOST` flag
- **Implementation**: Called during offensive multiplier calculation phase

```cpp
// From src/abilities.cc:3789-3794
constexpr Ability Striker = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IsStrikerBoosted(battler, move)) MUL(1.3);
        },
};
```

### Move Recognition System
The ability uses the `IsStrikerBoosted` function from `src/battle_util.c:9190-9194`:

```cpp
int IsStrikerBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_STRIKER_BOOST) return TRUE;
    if (gBattleMoves[move].flags & FLAG_IRON_FIST_BOOST && BattlerHasAbility(battler, ABILITY_JUNSHI_SANDA, FALSE)) return TRUE;
    return FALSE;
}
```

## Affected Moves

### Classic Kicking Moves
- **Double Kick** - Fighting-type, hits twice
- **Mega Kick** - Normal-type, high power single hit
- **Jump Kick** - Fighting-type, recoil if missed
- **High Jump Kick** - Fighting-type, high power with recoil risk
- **Rolling Kick** - Fighting-type, may cause flinching
- **Low Kick** - Fighting-type, variable power based on target weight
- **Stomp** - Normal-type, may cause flinching
- **Triple Kick** - Fighting-type, hits three times with increasing power

### Modern Kicking Moves
- **Blaze Kick** - Fire-type, high critical hit ratio
- **High Horsepower** - Ground-type, high power
- **Trop Kick** - Grass-type, lowers Attack
- **Pyro Ball** - Fire-type, may burn
- **Triple Axel** - Ice-type, hits three times
- **Thunderous Kick** - Fighting-type, lowers Defense
- **Whirling Strikes** - Custom move
- **Triple Arrows** - Fighting/Flying-type
- **Rider Kick** - Custom move
- **Axe Kick** - Fighting-type, may cause paralysis
- **Triple Tremor** - Custom move

## Strategic Applications

### Team Building
1. **Physical Sweeper Role** - Focus on high Attack stats to maximize damage output
2. **Coverage Options** - Kicking moves span multiple types (Fighting, Fire, Ground, Ice, etc.)
3. **Speed Control** - Many kicking moves benefit from priority or speed investment
4. **Mixed Attackers** - Some kicking moves are special (like Pyro Ball)

### Competitive Advantages
- **Consistent Damage Boost** - Unlike conditional abilities, works on all qualifying moves
- **Type Diversity** - Kicking moves cover multiple types for coverage
- **Multi-Hit Synergy** - Boosts each hit of multi-hit kicks like Triple Kick
- **Priority Integration** - Works with priority kicking moves like Rolling Kick

### Common Strategies
1. **All-Out Attacker** - Maximum Attack investment with Choice Band/Life Orb
2. **Speed Control** - Use faster kicks to outspeed and KO threats
3. **Coverage Fighter** - Utilize different-typed kicks for neutral coverage
4. **Support Utility** - Use stat-lowering kicks while dealing boosted damage

## Pokemon with Striker

### As Regular Ability
- **Rapidash** (Kantonian) - Fire/Striker/Deadly Precision
- **Rapidash** (Galarian) - Reckless/Striker/Deadly Precision  
- **Hitmonlee** - Combat Specialist/Roundhouse with Striker innate
- **Blaziken line** (Torchic/Combusken/Blaziken) - All have Striker as innate
- **Mega Blaziken** - Striker innate with Hellblaze/Roundhouse
- **Lucario** - Emanate with Striker innate
- **Buneary line** (Buneary/Lopunny) - All have Striker innate
- **Mega Lopunny** - Striker innate
- **Scrafty** - Striker/Moxie/Intimidate
- **Litten** - Striker innate
- **Primarina line** - All have Striker innate
- **Scolipede line** - All have Striker innate

### Variant Abilities
- **Mega Grimmsnarl** - Has Striker Pixilate (Striker + Pixilate combined)
- **Samba** - Shares Striker's offensive multiplier with Dancer effects

## Related Abilities

### Combat Specialist (Ability #462)
Combines Iron Fist and Striker effects:
```cpp
constexpr Ability CombatSpecialist = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            IronFist.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
            Striker.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        },
};
```

### Roundhouse (Ability #403)
Enhances kicking moves with perfect accuracy and defensive stat targeting:
- Never misses when using kicking moves
- Chooses lower defensive stat (Defense vs Special Defense)
- Synergizes perfectly with Striker for maximum effectiveness

### Iron Fist (Ability #89)
Similar concept but for punching moves:
- Boosts FLAG_IRON_FIST_BOOST moves by 1.2x
- Many Pokemon learn both punching and kicking moves

## Competitive Analysis

### Tier Assessment
**A-Tier Offensive Ability**
- Consistent 30% boost without conditions
- Wide move pool coverage
- No drawbacks or restrictions

### Strengths
1. **Reliable Damage** - Always active when using qualifying moves
2. **Type Coverage** - Kicking moves span many types
3. **Multi-Hit Synergy** - Boosts each hit of multi-hit moves
4. **No Restrictions** - No HP thresholds, status requirements, or turn limitations

### Weaknesses
1. **Move Pool Dependent** - Requires access to good kicking moves
2. **Physical Focus** - Most kicking moves are physical (exception: Pyro Ball)
3. **Competition** - Other offensive abilities may provide similar or better boosts
4. **Prediction Required** - Opponent can switch to resist kicking move types

### Usage Statistics
- **Most Common Sets**: Choice Band physical attacker, Life Orb mixed attacker
- **Popular Moves**: High Jump Kick, Blaze Kick, Triple Kick, Low Kick
- **Team Roles**: Physical sweeper, wallbreaker, revenge killer

## Technical Implementation

### Code Structure
```cpp
// Ability definition
constexpr Ability Striker = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IsStrikerBoosted(battler, move)) MUL(1.3);
        },
};

// Move recognition
int IsStrikerBoosted(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_STRIKER_BOOST) return TRUE;
    // Special case for Junshi Sanda ability interaction
    if (gBattleMoves[move].flags & FLAG_IRON_FIST_BOOST && 
        BattlerHasAbility(battler, ABILITY_JUNSHI_SANDA, FALSE)) return TRUE;
    return FALSE;
}
```

### Flag System
Moves gain Striker boost through proto definition:
```proto
moves {
  id: MOVE_DOUBLE_KICK
  name: "Double Kick"
  description: "Kicks the foe quickly twice. Striker boost."
  striker: true  // This sets FLAG_STRIKER_BOOST
}
```

### Ability Registration
```cpp
// From abilities array at line 9206
{ABILITY_STRIKER, Striker},
```

## Version History
- **Elite Redux 2.5+**: Introduced as ability #361
- **Current**: No changes since introduction

## Notes
- Unlike Iron Fist's 1.2x multiplier, Striker provides a stronger 1.3x boost
- The FLAG_STRIKER_BOOST system allows easy addition of new kicking moves
- Combat Specialist users get both Iron Fist and Striker boosts simultaneously
- Roundhouse ability provides perfect synergy by making kicks never miss and hit weaker defensive stats


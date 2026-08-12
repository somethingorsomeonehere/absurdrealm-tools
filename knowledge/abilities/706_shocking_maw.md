---
id: 706
name: Shocking Maw
status: reviewed
character_count: 106
---

# Shocking Maw - Ability ID 706

## In-Game Description
"Strong Jaw + Bite moves have 50% paralysis chance."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of biting and fang moves by 30% and they have a 50% chance to paralyze the target on hit. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shocking Maw is a hybrid offensive ability that combines the power-boosting effects of Strong Jaw with the status-inflicting potential of paralysis on all bite moves. This creates a dual threat that increases both damage output and crowd control capabilities.

### Implementation Analysis
From the codebase analysis in `src/abilities.cc`:

```c
constexpr Ability ShockingMaw = {
    .onAttacker = ShockingJaws.onAttacker,
    .onOffensiveMultiplier = StrongJaw.onOffensiveMultiplier,
};
```

The ability inherits two separate function pointers:
1. **onOffensiveMultiplier**: From Strong Jaw - provides 1.3x damage multiplier
2. **onAttacker**: From ShockingJaws - applies paralysis chance

### Strong Jaw Component
```c
constexpr Ability StrongJaw = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST) MUL(1.3);
        },
};
```
- **Damage boost**: 1.3x multiplier (30% increase)
- **Move requirement**: Move must have FLAG_STRONG_JAW_BOOST flag
- **Always active**: No conditions beyond move type

### Paralysis Component (ShockingJaws)
```c
constexpr Ability ShockingJaws = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBeParalyzed(battler, target))
        CHECK(gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST)
        CHECK(Random() % 2)

        return AbilityStatusEffect(MOVE_EFFECT_PARALYSIS);
    },
};
```

#### Activation Requirements
1. **Hit requirement**: `ShouldApplyOnHitAffect(target)` - move must successfully hit
2. **Paralysis immunity check**: `CanBeParalyzed(battler, target)` - target must not be immune
3. **Move flag check**: Same FLAG_STRONG_JAW_BOOST requirement
4. **Random chance**: `Random() % 2` - exactly 50% chance

### Affected Moves
All moves with the FLAG_STRONG_JAW_BOOST flag, including:
- **Bite** (Dark, 60 BP)
- **Crunch** (Dark, 80 BP) 
- **Fire Fang** (Fire, 65 BP)
- **Ice Fang** (Ice, 65 BP)
- **Thunder Fang** (Electric, 65 BP)
- **Poison Fang** (Poison, 50 BP)
- **Psychic Fangs** (Psychic, 85 BP)
- **Hyper Fang** (Normal, 80 BP)
- **Super Fang** (Normal, variable)
- Other bite/jaw-based moves

### Damage Calculations
With Shocking Maw, bite moves receive:
- **Base damage**: Normal move power
- **Strong Jaw boost**: x 1.3 multiplier
- **Type effectiveness**: Normal STAB and type chart
- **Critical hits**: Can still crit normally
- **Other modifiers**: Life Orb, Choice items, etc. still apply

Example: Crunch (80 BP) becomes effectively 104 BP (80 x 1.3)

### Status Effect Mechanics
- **Paralysis chance**: Exactly 50% on each successful hit
- **Paralysis effects**: 
  - Speed reduced to 25% of original
  - 25% chance to be unable to move each turn
- **No stacking**: Cannot paralyze already paralyzed targets
- **Immunity bypassing**: Does not bypass Ground-type immunity to paralysis
- **Priority**: Paralysis application occurs after damage calculation

### Strategic Applications

#### Offensive Advantages
- **High damage output**: 30% damage boost makes bite moves significantly stronger
- **Crowd control**: 50% paralysis chance provides excellent status pressure
- **Multi-hit potential**: Each bite move hit can potentially paralyze
- **Type coverage**: Bite moves span multiple types for coverage

#### Team Synergy
- **Speed control**: Paralysis supports slower teammates
- **Setup enabling**: Paralyzed opponents struggle to interrupt setup
- **Revenge killing**: Strong Jaw boost helps secure KOs
- **Status spreading**: Can cripple multiple opponents over time

### Limitations and Counterplay

#### Inherent Limitations
- **Move dependence**: Only works with specific bite moves
- **Status immunity**: Electric types and Limber ignore paralysis
- **Accuracy dependence**: Must hit to apply both damage and status
- **Random element**: 50% chance means unreliable status application

#### Counters and Responses
- **Limber ability**: Complete immunity to paralysis
- **Electric types**: Natural paralysis immunity
- **Lum Berry**: Instant status cure
- **Substitute**: Blocks status application (but not damage boost)
- **Contact punishment**: Abilities like Static still trigger on contact moves

### Competitive Usage

#### Ideal Users
- **Physical attackers**: Pokemon with high Attack stats
- **Diverse movesets**: Pokemon that learn multiple bite moves
- **Bulky attackers**: Can tank hits while applying status pressure
- **Priority users**: Can potentially paralyze faster threats

#### Common Strategies
- **Lead pressure**: Early paralysis can cripple fast setup sweepers
- **Wallbreaking**: 30% damage boost helps break through defensive walls
- **Speed control**: Paralysis enables slower team members to outspeed
- **Status spreading**: Multiple bite moves for type coverage and status

#### Metagame Impact
- **Anti-speed**: Directly counters speed-based strategies
- **Consistent threat**: Every bite move becomes a potential game-changer
- **Team building consideration**: Forces opponents to consider paralysis immunity
- **Move selection pressure**: May influence opponent's item and ability choices

### Interactions with Other Abilities

#### Beneficial Synergies
- **Guts**: Teammate benefits from being paralyzed
- **Quick Feet**: Teammate gets speed boost from paralysis
- **Facade users**: Double damage when statused

#### Negative Interactions
- **Own team paralysis**: Cannot paralyze own teammates
- **Substitute blocking**: Subs block status but not damage boost
- **Mold Breaker**: Can bypass some immunities but not type-based ones

### Version Notes
- **Elite Redux specific**: Part of the expanded ability roster
- **ID assignment**: Ability ID 706 in the current build
- **Balance consideration**: Combines two strong effects for powerful synergy
- **Implementation**: Clean combination of existing ability components

### Technical Notes
- **Flag dependency**: Both components require FLAG_STRONG_JAW_BOOST
- **Order of operations**: Damage boost calculated before status application
- **Random generation**: Uses standard battle RNG for paralysis chance
- **Status effect timing**: Applied via standard `AbilityStatusEffect` function

This ability represents a perfect fusion of offensive power and battlefield control, making every bite move a potential game-changing attack through both enhanced damage and debilitating status effects.
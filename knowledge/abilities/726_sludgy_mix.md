---
id: 726
name: Sludgy Mix
status: reviewed
character_count: 267
---

# Sludgy Mix - Ability ID 726

## In-Game Description
"Intoxicate + Punk Rock."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Converts all Normal-type moves into Poison-type moves and grants STAB for Poison-type moves, regardless of the user's typing. Amplifies the user's sound moves by 30% and reduces incoming sound move damage by 50%. Damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sludgy Mix is a combination ability that merges the effects of two distinct abilities: Intoxicate and Punk Rock. This creates a unique offensive profile that enhances both Normal-type move conversion and sound-based move interactions.

### Ability Components

#### Intoxicate Component
- **Move Type Conversion**: All Normal-type moves become Poison-type
- **Power Boost**: Converted moves receive a 20% damage boost (1.2x multiplier)
- **STAB Interaction**: Poison-type Pokemon gain STAB on converted moves
- **Coverage**: Provides Poison-type coverage without learning Poison moves

#### Punk Rock Component
- **Offensive Boost**: Sound-based moves deal 30% more damage (1.3x multiplier)
- **Defensive Reduction**: Takes 50% less damage from opposing sound moves (0.5x multiplier)
- **Sound Move Recognition**: Affects all moves with the sound flag in the game data

### Technical Implementation
```c
// Sludgy Mix combines both abilities through delegation
constexpr Ability SludgyMix = {
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
        // Delegates to both Intoxicate and Punk Rock offensive multipliers
        Intoxicate.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
        PunkRock.onOffensiveMultiplier(DELEGATE_OFFENSIVE_MULTIPLIER);
    },
    .onMoveType = Intoxicate.onMoveType, // Normal to Poison conversion
};

// Intoxicate uses the ATE_ABILITY macro for type conversion
#define ATE_ABILITY(type)
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(moveType == TYPE_NORMAL)
        *ateBoost = TRUE; // Applies 20% power boost
        return type + 1;  // Returns POISON_TYPE + 1
    }

// Punk Rock provides sound move interactions
constexpr Ability PunkRock = {
    .onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
        if (IsSoundMove(battler, move)) MUL(1.3); // 30% boost to sound moves
    },
    .onDefensiveMultiplier = +[](ON_DEFENSIVE_MULTIPLIER) {
        if (IsSoundMove(attacker, move)) MUL(.5); // 50% less damage from sound moves
    },
};
```

### Affected Sound Moves
Common sound-based moves that benefit from Punk Rock component:
- **Boomburst**: Extremely powerful with 30% boost
- **Hyper Voice**: Reliable STAB option for Normal types
- **Bug Buzz**: Special attacking Bug move
- **Overdrive**: Electric-type sound move
- **Clangorous Soul**: Dragon-type stat booster
- **Disarming Voice**: Never-miss Fairy move
- **Echoed Voice**: Escalating power move
- **Round**: Doubles in power with ally usage

### Move Conversion Examples
Normal moves that become Poison-type with 20% boost:
- **Hyper Voice** to Poison-type, boosted by both components (1.2x from conversion, 1.3x from sound = 1.56x total)
- **Boomburst** to Poison-type, massive power with both boosts
- **Facade** to Poison-type with status boost potential
- **Body Slam** to Poison-type physical attack
- **Swift** to Poison-type never-miss move

### Damage Calculation
For a sound-based Normal move with Sludgy Mix:
1. **Base Power**: Original move power
2. **Type Conversion**: Normal to Poison (enables STAB for Poison types)
3. **Intoxicate Boost**: 1.2x multiplier from type conversion
4. **Punk Rock Boost**: 1.3x multiplier for sound moves
5. **Total Multiplier**: 1.2 x 1.3 = 1.56x damage boost
6. **STAB**: Additional 1.5x if user is Poison-type

### Strategic Applications

#### Offensive Synergies
- **Sound Move Spam**: Hyper Voice and Boomburst become devastating Poison attacks
- **Mixed Coverage**: Normal moves provide unexpected Poison coverage
- **STAB Maximization**: Poison-type users gain STAB on formerly Normal moves
- **Sound-based Sets**: Built around powerful sound moves with dual boosts

#### Defensive Benefits
- **Sound Move Resistance**: Takes half damage from opponent's sound moves
- **Noise Immunity**: Reduces effectiveness of sound-based strategies
- **Bulk Enhancement**: Effective HP doubled against sound attacks

### Pokemon Synergy
Ideal candidates for Sludgy Mix:
- **Poison-types with Sound Moves**: Gain STAB on converted moves plus sound boosts
- **Normal-types with Sound Access**: Transform their movepool while keeping sound advantages
- **Mixed Attackers**: Benefit from both physical and special sound move variety
- **Bulky Sound Users**: Appreciate the defensive sound resistance

### Team Composition
- **Sound-based Cores**: Multiple Pokemon with sound moves for team synergy
- **Anti-Meta Picks**: Counters opposing sound-based strategies
- **Coverage Fillers**: Provides unexpected Poison typing on Normal moves
- **Wallbreakers**: Combined boosts create powerful wall-breaking potential

### Competitive Considerations

#### Advantages
- **Unpredictable Coverage**: Opponents don't expect Poison-type attacks from Normal moves
- **Sound Move Mastery**: Excellent at both using and resisting sound attacks
- **Flexible Movesets**: Can run both sound and non-sound Normal moves effectively
- **Anti-Sound Meta**: Hard counters sound-based teams

#### Limitations
- **Move Pool Dependent**: Requires access to both Normal and sound moves for full benefit
- **Type Matchup Issues**: Poison typing can be resisted or ineffective
- **Soundproof Immunity**: Soundproof users are immune to sound move benefits
- **Limited Defensive Scope**: Only resists sound moves, not other common attacks

### Counters and Checks
- **Soundproof**: Completely negates the Punk Rock component
- **Steel-types**: Resist Poison-type converted moves
- **Poison-types**: Immune to Poison-type moves entirely
- **Non-Sound Attackers**: Bypass the defensive sound resistance
- **Substitute**: Blocks sound moves regardless of ability

### Notable Interactions
- **Throat Chop**: Prevents use of sound moves, negating major component
- **Telepathy**: Allies with Telepathy avoid damage from sound moves
- **Liquid Voice**: Other abilities that modify sound moves may interact uniquely  
- **Pixilate/Aerilate**: Similar -ate abilities may conflict with move conversion

### Version History
- Elite Redux custom combination ability
- Combines Generation VI+ abilities (Intoxicate concept) with Generation VIII (Punk Rock)
- Represents the fusion of type conversion and sound mastery themes
- Part of Elite Redux's expanded ability system for unique battle interactions
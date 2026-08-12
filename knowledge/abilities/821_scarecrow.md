---
id: 821
name: Scarecrow
status: reviewed
character_count: 280
---

# Scarecrow - Ability ID 821

## In-Game Description
Scare + Bad Luck.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon entering battle, the user drops the Special Attack stat of all opposing Pokemon by one stage. Foes can not land critical hits, always roll minimum damage (85% instead of 85-100%), fail to inflict secondary effects that are not guaranteed, and have a 5% chance to miss a move.

## Detailed Mechanical Explanation

### Effects

#### On Entry (Scare Component)
- Lowers opposing Pokemon's **Special Attack** by 1 stage when entering battle
- Affects both opponents in double battles
- Cannot be prevented by abilities like Substitute
- Triggers Guard Dog's Attack boost if the target has that ability

#### Battle Effects (Bad Luck Component)
- **Critical Hit Prevention**: Completely prevents opposing Pokemon from landing critical hits
- **Effect Chance Reduction**: Reduces the effect chance of opposing moves to 0% if they're normally less than 100%
- **Minimum Rolls**: Forces opposing Pokemon to roll minimum values for damage ranges and other RNG effects
- **Applies to**: All opposing Pokemon (foes only)

### Implementation Details

#### Code Location
- **Main Definition**: `src/abilities.cc` (Scarecrow ability)
- **Intimidate Data**: `src/pokemon.c` (gIntimidateCloneData array)
- **Battle Function**: `src/battle_util.c` (UseIntimidateClone function)

#### Technical Mechanics
```cpp
constexpr Ability Scarecrow = {
    .onEntry = UseIntimidateClone,           // Scare effect
    .onCrit = BadLuck.onCrit,                // Prevent crits
    .onModifyEffectChance = BadLuck.onModifyEffectChance,  // Reduce effect chances
    .onCritFor = BadLuck.onCritFor,          // Apply to foes
    .onModifyEffectChanceFor = BadLuck.onModifyEffectChanceFor,
    .breakable = TRUE,
};
```

#### Intimidate Clone Data
```cpp
{
    .ability = ABILITY_SCARECROW,
    .numStatsLowered = 1,
    .statsLowered = {STAT_SPATK, 0, 0},  // Special Attack only
    .targetBoth = TRUE,                   // Affects both opponents
}
```

### Interactions

#### Guard Dog Interaction
- If the target has Guard Dog, the Special Attack drop is converted to a +1 Attack boost
- Guard Dog's ability popup will trigger after the intimidate effect

#### Ability Interactions
- **Breakable**: Can be suppressed by Mold Breaker and similar abilities
- **Clear Body/White Smoke**: Prevents the Special Attack drop but not the Bad Luck effects
- **Competitive/Defiant**: Will trigger from the Special Attack drop

#### Move Interactions
- **Critical Hit Moves**: Completely blocked - moves like Storm Throw become regular attacks
- **Effect Chances**: Moves with <100% effect rates (like Thunderbolt's 10% paralysis) become 0%
- **Perfect Accuracy Moves**: Effect chances still reduced, but accuracy unaffected

### Strategic Usage

#### Best Used For
- **Special Wall Setup**: Crippling special attackers while setting up
- **RNG Control**: Eliminating critical hit threats and secondary effect risks
- **Double Battles**: Maximum value from intimidating both opponents
- **Status Spreaders**: Shutting down unreliable status moves

#### Situational Considerations
- Less effective against physical attackers (only affects Special Attack)
- Bad Luck effects don't stack with multiple Scarecrow users
- Guard Dog users can turn the intimidate against you
- Mold Breaker completely bypasses all effects
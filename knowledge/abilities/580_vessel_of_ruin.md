---
id: 580
name: Vessel Of Ruin
status: reviewed
character_count: 193
---

# Vessel Of Ruin - Ability ID 580

## In-Game Description
"Lowers the Special Attack of other Pokemon by 25%."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces the Special Attack stat of every other Pokemon by 25% while the user is out. Multiples of the same Ruin ability do not stack together. Stacks multiplicatively with Special Attack drops.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Vessel of Ruin is a passive aura ability that applies a permanent 25% reduction to the Special Attack stat of all Pokemon on the battlefield except the user. The ability is part of the "Ruinous Pokemon" ability family, which includes:

- **Tablets of Ruin**: Reduces Attack by 25%
- **Sword of Ruin**: Reduces Defense by 25% 
- **Vessel of Ruin**: Reduces Special Attack by 25%
- **Beads of Ruin**: Reduces Special Defense by 25%

### Technical Implementation
```cpp
constexpr Ability VesselOfRuin = {
    .onStat = +[](ON_STAT) { RuinEffect(STAT_SPATK, battler, statId, stat, flags); },
    .onStatFor = APPLY_ON_OTHER,
    .ruinStat = STAT_SPATK,
};

static void RuinEffect(int ruinStat, int battler, int statId, u32 *stat, NonStackingState *flags) {
    if (statId != ruinStat) return;
    if (*flags & NON_STACKING_RUIN) return;
    ON_ABILITY(battler, FALSE, gAbilities[ability].ruinStat == statId, return) *stat *= .75;
    *flags = static_cast<NonStackingState>(static_cast<int>(*flags) | static_cast<int>(NON_STACKING_RUIN));
}
```

### Activation Conditions
- **Automatic**: The ability is always active when the Pokemon is on the battlefield
- **No setup required**: No move usage or special conditions needed
- **Immediate effect**: Takes effect the moment the Pokemon enters battle

### Numerical Values
- **Special Attack Reduction**: 25% (multiplies by 0.75)
- **Affects**: All other Pokemon on the field (enemies and allies)
- **Does not affect**: The user of the ability

### Affected Moves
All moves that use the Special Attack stat for damage calculation are affected:
- Special attacking moves (Flamethrower, Psychic, Surf, etc.)
- Mixed damage calculation moves that use Special Attack
- Fixed damage moves are NOT affected (Seismic Toss, Night Shade, etc.)

### Interactions with Other Abilities/Mechanics
- **Stacking**: Multiple Ruin abilities DO NOT stack - only one Ruin effect per stat applies
- **Stat modifications**: Works multiplicatively with other stat changes (boosts, items, etc.)
- **Mold Breaker effects**: Cannot be bypassed by Mold Breaker or similar abilities
- **Neutralizing Gas**: The effect is temporarily suppressed when Neutralizing Gas is active
- **Magic Bounce/Guard**: Cannot be reflected or blocked as it's a passive aura, not a targeted effect

### Strategic Implications
- **Defensive utility**: Significantly reduces opponent's special attack power
- **Doubles strategy**: Must consider impact on ally Pokemon
- **Team synergy**: Works well with physically defensive Pokemon
- **Permanent effect**: Cannot be removed by moves like Haze or Clear Smog

### Example Damage Calculations
```
Base Special Attack: 100
With Vessel of Ruin: 100 x 0.75 = 75 Special Attack

Example with Flamethrower (90 BP):
Normal damage: (100 SpA / opposing defense) x 90 BP = base damage
With Vessel of Ruin: (75 SpA / opposing defense) x 90 BP = 75% of base damage
```

### Common Users
Based on the codebase analysis, Vessel of Ruin is primarily found on legendary/mythical Pokemon, particularly those themed around ancient ruins and destruction. In Elite Redux, it appears as an innate ability on certain legendary Pokemon.

### Competitive Usage Notes
- **Entry hazard synergy**: Pairs well with entry hazards to create defensive pressure
- **Stall teams**: Excellent for defensive/stall team compositions
- **Doubles considerations**: Can hinder ally special attackers - plan team accordingly
- **Speed control**: Often paired with speed control moves to maximize defensive utility

### Counters
- **Physical attackers**: Unaffected by the Special Attack reduction
- **Status moves**: Not affected by stat reductions
- **Neutralizing Gas**: Temporarily disables the ability
- **Switching**: Removing the Vessel of Ruin user stops the effect

### Synergies
- **Physical walls**: Complements Pokemon with high physical defense
- **Entry hazards**: Stealth Rock, Spikes, Toxic Spikes for additional pressure
- **Status moves**: Thunder Wave, Will-O-Wisp to further cripple opponents
- **Recovery moves**: Roost, Recover to maintain longevity

### Version History
Vessel of Ruin is one of the signature abilities of the Treasures of Ruin legendary Pokemon introduced in Generation IX. In Elite Redux, it maintains its core functionality while being integrated into the game's expanded ability system and multi-ability framework.
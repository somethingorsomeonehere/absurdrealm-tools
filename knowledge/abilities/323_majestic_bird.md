---
id: 323
name: Majestic Bird
status: reviewed
character_count: 100
---

# Majestic Bird - Ability ID 323

## In-Game Description
"Boosts own Sp. Atk by 1.5x. Boosts raw stat, not base stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Majestic Bird boosts the user's Special Attack stat by 50%. Multiplicative with other damage boosts.

## Mechanics Analysis

### Stat Boost Details
- **Stat Affected**: Special Attack (STAT_SPATK)
- **Multiplier**: 1.5x (50% increase)
- **Application**: Applied to final calculated stat, not base stat
- **Timing**: Constant effect, applied during stat calculation
- **Conditions**: None - always active

### Implementation
```cpp
constexpr Ability MajesticBird = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPATK) *stat *= 1.5;
        },
};
```

### Key Characteristics
1. **Unconditional**: No weather, terrain, or status requirements
2. **Raw Stat Boost**: Multiplies final stat after all calculations
3. **Permanent**: Active throughout battle
4. **Stackable**: Combines with other stat boosts and items
5. **Not Suppressible**: No special suppression mechanics

## Pokemon Distribution

### Primary Ability
- **Pidgey**: Can have as one of 3 choosable abilities
- **Pidgeotto**: Can have as one of 3 choosable abilities  
- **Delcatty**: Can have as one of 3 choosable abilities

### Innate Ability
- **Mega Pidgeot**: Fixed innate ability
- **Articuno-Ex**: Fixed innate ability
- **Articuno-Redux**: Fixed innate ability  
- **Noctowl**: Fixed innate ability
- **Lugia**: Fixed innate ability
- **Oricorio**: Fixed innate ability
- **Pecharunt**: Fixed innate ability
- **Cresselia**: Fixed innate ability
- **Moltres-Ex**: Fixed innate ability

## Related Abilities

### Auroras Gale (Compound Ability)
- Uses `MajesticBird.onStat` for the Special Attack boost
- Also includes `NorthWind.onEntry` and hail immunity
- Found on ice-type legendary variants

### Similar Stat Boost Abilities
- **Marvel Scale**: 1.5x Defense/Sp.Defense when statused
- **Solar Power**: 1.5x highest attacking stat in sun
- **Sand Force**: 1.5x highest attacking stat in sandstorm
- **Flare Boost**: 1.5x Special Attack when burned

## Competitive Impact

### Advantages
1. **Reliable Power**: No setup or conditions required
2. **Immediate Impact**: Active from turn 1
3. **Sweeping Potential**: Significant damage boost for special attackers
4. **Versatile**: Works with any special attacking moveset

### Strategic Considerations
1. **Choice Items**: Stacks with Choice Specs for massive damage
2. **Life Orb**: Combines with recoil items for even higher output
3. **Setup Moves**: Can be combined with Calm Mind, Nasty Plot, etc.
4. **Weather Teams**: Pairs well with weather-boosted moves

## Code References
- **Main Implementation**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (MajesticBird function)
- **Ability List**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityList.textproto`
- **Enum Definition**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityEnum.proto`
- **Species Distribution**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/SpeciesList.textproto`
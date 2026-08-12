---
id: 381
name: Pollinate
status: reviewed
character_count: 89
---

# Pollinate - Ability ID 381

## In-Game Description
"Normal-type moves become Bug and Bug gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Normal-type moves become Bug-type and they receive STAB regardless of the Pokemon's type. 

## Technical Implementation

### Source Code Location
- **File**: `src/abilities.cc`
- **Lines**: 3956-3958
- **Implementation**: Uses the `ATE_ABILITY(TYPE_BUG)` macro

### ATE_ABILITY Macro Details
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Mechanics
1. **Type Conversion**: All Normal-type moves are converted to Bug-type
2. **Power Boost**: Converted moves receive a 1.2x damage multiplier (`*ateBoost = TRUE`)
3. **STAB Application**: Bug-type moves (including converted ones) always receive STAB regardless of the Pokemon's actual typing
4. **Priority**: Applied before other type-modifying effects

## Strategic Analysis

### Competitive Applications
- **Tier Rating**: Medium - Solid offensive boost but limited by Bug-type's middling offensive coverage
- **Primary Use**: Converting Normal-type attackers into Bug-type specialists
- **Best Movesets**: Pokemon with strong Normal-type movesets benefit most

### Optimal Move Combinations
**Recommended Normal to Bug Conversions**:
- **Hyper Beam** to 120 BP Bug-type move with 1.2x boost
- **Body Slam** to 85 BP Bug-type move with paralysis chance
- **Double-Edge** to 100 BP Bug-type move with recoil
- **Return/Frustration** to Variable BP Bug moves
- **Quick Attack** to Priority Bug-type move
- **Facade** to Powerful Bug move when statused

### Coverage Considerations
**Bug-type Effectiveness**:
- **Super Effective vs**: Dark, Grass, Psychic
- **Not Very Effective vs**: Fairy, Fighting, Fire, Flying, Ghost, Poison, Steel
- **Immune**: None

### Synergies
- **Weather Teams**: Pairs well with abilities that boost Bug moves
- **Status Strategies**: Facade becomes a powerful Bug-type move when burned/poisoned
- **Priority Moves**: Quick Attack becomes a Bug-type priority move
- **Choice Items**: Fixed Bug typing allows for consistent STAB damage

## Related Abilities

### Other ATE Abilities in Elite Redux
Pollinate is part of a large family of type-conversion abilities:

**Official ATE Abilities**:
- **Refrigerate** (#174) - Normal to Ice
- **Pixilate** (#182) - Normal to Fairy  
- **Aerilate** (#184) - Normal to Flying
- **Galvanize** (#206) - Normal to Electric

**Elite Redux ATE Abilities**:
- **Steelworker** (#200) - Normal to Steel
- **Immolate** (#279) - Normal to Fire
- **Fighting Spirit** (#300) - Normal to Fighting
- **Tectonize** (#308) - Normal to Ground
- **Hydrate** (#315) - Normal to Water
- **Intoxicate** (#325) - Normal to Poison
- **Spectralize** (#???) - Normal to Ghost
- **Mineralize** (#404) - Normal to Rock
- **Draconize** (#413) - Normal to Dragon
- **Atomic Burst** (#416) - Normal to Electric (with additional effects)
- **Emanate** (#459) - Normal to Psychic
- **Fertilize** (#507) - Normal to Grass
- **Deviate** (#???) - Normal to Dark

### Comparison with Similar Abilities
**vs Refrigerate/Pixilate/Aerilate**: 
- Same 1.2x power boost mechanism
- Bug-type has worse offensive coverage than Ice/Fairy/Flying
- More situational than the mainstream ATE abilities

**vs Swarm**:
- Pollinate affects all moves, not just Bug moves
- Swarm provides conditional boost, Pollinate provides consistent conversion
- Can't stack with Swarm (both affect Bug moves)

## Counters and Weaknesses

### Direct Counters
- **Fire-types**: Resist Bug moves, often have super-effective moves
- **Flying-types**: Resist Bug moves, immune to Ground coverage
- **Steel-types**: Resist Bug moves, typically bulky
- **Poison-types**: Resist Bug moves, can absorb status

### Strategic Limitations
- **Poor Coverage**: Bug-type doesn't hit many types super-effectively
- **Common Resists**: Many types resist Bug moves
- **No Defensive Benefit**: Pure offensive ability with no defensive utility
- **Move Pool Dependent**: Effectiveness limited by Normal-type moves available

## Recommended Pokemon

### Ideal Candidates
Pokemon with large Normal-type movepools and good offensive stats:
- **Normal-types**: Natural synergy with existing movesets
- **High Attack/Sp.Attack**: Maximize the 1.2x boost
- **Speed Control**: Fast Pokemon to outspeed and convert
- **Coverage Moves**: Non-Normal moves for type coverage

### Team Roles
- **Physical Sweeper**: High Attack with converted Normal moves
- **Special Attacker**: Special Normal moves become Bug-type
- **Revenge Killer**: Quick Attack becomes priority Bug move
- **Wall Breaker**: Powerful converted moves break defensive cores

## Conclusion

Pollinate provides a solid offensive conversion that transforms Normal-type attackers into Bug-type specialists. While Bug-type doesn't offer the best offensive coverage, the guaranteed STAB and 1.2x power boost make it a respectable ability for Pokemon with strong Normal-type movesets. The ability's effectiveness is highly dependent on move pool and team composition, making it a medium-tier competitive option that requires careful planning to maximize its potential.
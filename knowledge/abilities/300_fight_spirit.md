---
id: 300
name: Fighting Spirit
status: reviewed
character_count: 113
---

# Fighting Spirit - Ability ID 300

## In-Game Description
"Normal-type moves become Fighting and Fighting gains STAB."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Fighting Spirit converts all Normal-type moves into Fighting-type moves and grants STAB on Fighting-type attacks.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fighting Spirit is an "ATE" (Normalize-type) ability that fundamentally changes how the user's moveset functions:

1. **Type Conversion**: All Normal-type moves become Fighting-type
2. **STAB Grant**: Provides STAB (Same Type Attack Bonus) for Fighting-type moves
3. **ATE Boost Flag**: Sets the internal `ateBoost` flag when converting moves

### Activation Conditions
- Triggers automatically when the Pokemon uses any Normal-type move
- No activation requirements or conditions - passive ability
- Works on all Normal-type moves regardless of category (physical/special/status)

### Technical Implementation
```cpp
constexpr Ability FightingSpirit = {
    ATE_ABILITY(TYPE_FIGHTING),
};

#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Complete List of Affected Moves
Common Normal-type moves that become Fighting-type:
- **Physical**: Body Slam, Double-Edge, Facade, Return, Frustration, Tackle, Take Down, Mega Kick, Extreme Speed
- **Special**: Hyper Voice, Boomburst, Tri Attack, Swift, Hidden Power (if Normal)
- **Status**: Not typically affected as status moves don't change type effectiveness

### Interactions with Other Abilities/Mechanics
- **Technician**: If user has Technician as another ability, converted 60 BP or lower moves get boosted
- **STAB**: Converted moves receive 1.5x damage multiplier from STAB
- **Type Effectiveness**: Moves gain Fighting-type effectiveness (super effective vs Normal, Dark, Ice, Rock, Steel; resisted by Flying, Psychic, Fairy, Bug, Poison; no effect on Ghost)
- **Wonder Guard**: Converted moves can hit Wonder Guard users if Fighting is super effective
- **Protean/Libero**: If user has these abilities, they change to Fighting-type when using converted moves

### Strategic Implications
1. **Coverage Enhancement**: Transforms Normal-type filler moves into useful Fighting STAB
2. **Mixed Attacker Support**: Both physical and special Normal moves benefit
3. **STAB Consistency**: Ensures Fighting-types always have STAB on former Normal moves
4. **Movepool Expansion**: Effectively gives access to Fighting-type versions of powerful Normal moves

### Example Damage Calculations
Assuming 100 Base Attack, 100 Base Move Power, no other modifiers:
- **Without Fighting Spirit**: Normal-type move = 100% damage (no STAB for non-Normal types)  
- **With Fighting Spirit**: Fighting-type move = 150% damage (with STAB)
- **Net Gain**: 50% damage increase for converted moves when user has Fighting typing

### Common Users
Based on the codebase analysis, Fighting Spirit appears on various Pokemon as either a regular or innate ability. Commonly found on:
- Fighting-type Pokemon that learn many Normal-type moves
- Mixed attackers that benefit from consistent STAB
- Pokemon with diverse Normal-type movepools

### Competitive Usage Notes
- **Offensive Utility**: Maximizes damage output from Normal-type moves
- **Type Synergy**: Most effective on Fighting-types or Pokemon that can become Fighting-type
- **Move Selection**: Prioritize high-power Normal moves in moveset planning
- **Team Building**: Consider Fighting-type weaknesses when building around this ability

### Counters
- **Ghost-types**: Completely immune to converted Fighting-type moves
- **Flying-types**: Resist Fighting-type damage
- **Psychic-types**: Resist Fighting-type damage  
- **Fairy-types**: Resist Fighting-type damage
- **Intimidate**: Reduces physical Fighting move damage
- **Burn**: Halves physical Fighting move damage

### Synergies
- **Iron Fist**: Boosts Fighting-type punching moves by 20%
- **Sheer Force**: Removes secondary effects but boosts power by 30%
- **Life Orb**: 30% damage boost to all moves
- **Choice Items**: Lock into powerful converted moves
- **Fighting Gem**: One-time 50% boost to Fighting moves

### Version History
- Introduced as part of Elite Redux's expanded ability roster
- Uses the standard ATE ability framework
- Provides Fighting-types with enhanced Normal move utility
- Part of the broader type-conversion ability family including Pixilate, Refrigerate, Aerilate, etc.
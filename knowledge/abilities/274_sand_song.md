---
id: 274
name: Sand Song
status: reviewed
character_count: 111
---

# Sand Song - Ability ID 274

## In-Game Description
"Sound moves get a 1.2x boost and become Ground if Normal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sand Song boosts the power of all sound-based moves by 20% and converts Normal-type sound moves to Ground-type. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sand Song is a dual-effect ability that enhances sound-based moves in two ways:
1. **Power Boost**: All moves with the FLAG_SOUND flag receive a 1.2x damage multiplier
2. **Type Conversion**: Normal-type sound moves are converted to Ground-type

### Activation Conditions
- Must use a move with the FLAG_SOUND flag
- Type conversion only applies to Normal-type sound moves
- Both effects can apply to the same move simultaneously

### Technical Implementation
```cpp
constexpr Ability SandSong = {
    .onOffensiveMultiplier = LiquidVoice.onOffensiveMultiplier,  // 1.2x for sound moves
    .onMoveType = +[](ON_MOVE_TYPE) -> int {
        CHECK(moveType == TYPE_NORMAL)
        CHECK(gBattleMoves[move].flags & FLAG_SOUND);
        return TYPE_GROUND + 1;  // Convert to Ground-type
    },
};
```

### Affected Sound Moves
**Normal-type sound moves (converted to Ground + boosted):**
- Hyper Voice (95 BP to 114 BP, becomes Ground-type)
- Boomburst (140 BP to 168 BP, becomes Ground-type)  
- Uproar (90 BP to 108 BP, becomes Ground-type)
- Howl (status move, becomes Ground-type)
- Roar (status move, becomes Ground-type)
- Sing (status move, becomes Ground-type)
- Supersonic (status move, becomes Ground-type)

**Non-Normal sound moves (only boosted):**
- Bug Buzz (Electric-type, 90 BP to 108 BP)
- Screech (Normal status to remains Normal)
- Chatter (Flying-type, 65 BP to 78 BP)
- Round (Normal-type, 60 BP to 72 BP, becomes Ground-type)

### Strategic Implications
**Offensive Applications:**
- Converts Normal-type sound moves into powerful Ground-type attacks
- Enables STAB bonus for Ground-type Pokemon using converted moves
- Super effective against Electric, Fire, Poison, Rock, and Steel types
- Immune to Flying types and Levitate ability holders

**Defensive Considerations:**
- Ground-type moves are resisted by Bug, Grass, and Flying types
- Completely ineffective against Flying-types and Levitate users
- Sound moves still bypass Substitute regardless of type

### Example Damage Calculations
**Hyper Voice with Sand Song (95 BP Normal to Ground):**
- Base: 95 BP
- Sand Song boost: 95 x 1.2 = 114 BP
- With STAB (Ground-type user): 114 x 1.5 = 171 effective BP
- Super effective: 171 x 2 = 342 effective BP

### Common Users
Sand Song is typically found on:
- Ground-type Pokemon that learn sound moves
- Pokemon with diverse movepools including both Ground and Normal moves
- Defensive Pokemon that can utilize status sound moves

### Competitive Usage Notes
**Advantages:**
- Significant power boost to sound-based movesets
- Type conversion provides better offensive coverage
- Status sound moves gain Ground typing for interactions
- Bypasses Substitute with sound moves

**Limitations:**
- Limited to sound moves only
- Ground immunity severely limits effectiveness against certain teams
- Depends on movepool containing sound moves
- No defensive benefits

### Counters
**Direct Counters:**
- Flying-type Pokemon (immune to Ground-type moves)
- Pokemon with Levitate ability
- Sound-proof ability users (immune to sound moves entirely)

**Situational Counters:**
- Bug, Grass, and Flying types (resist Ground)
- Priority moves that outspeed sound attackers
- Choice Scarf users that can revenge kill

### Synergies
**Ability Synergies:**
- Works with other offensive abilities like Adaptability for additional STAB
- Combines with stat-boosting abilities for enhanced damage
- Pairs with abilities that provide additional type coverage

**Move Synergies:**
- Sound moves that provide utility (Roar for phazing)
- Coverage moves to handle Flying-types and Levitate users
- Priority moves to compensate for sound move speeds

**Item Synergies:**
- Life Orb for additional damage boost
- Choice items for power or speed enhancement
- Throat Spray for Special Attack boost after sound moves

### Version History
- Added in Elite Redux as ability ID 274
- Based on Liquid Voice framework with Ground-type conversion
- Part of the "song" ability family including Snow Song and Power Metal
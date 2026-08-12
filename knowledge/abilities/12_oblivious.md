---
id: 12
name: Oblivious
status: reviewed
character_count: 165
---

# Oblivious - Ability ID 12

## In-Game Description
"Immune to infatuation, Scare, Intimidate and Taunt."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

This Pokemon is immune to infatuation, Scare, Intimidate and Taunt. When gaining this ability while afflicted by any of the mentioned statuses, instantly cures them.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Oblivious provides immunity to multiple mental/restriction effects:

1. **Infatuation Immunity**
   - Cannot be infatuated by any means
   - Includes Attract, Cute Charm, etc.
   - Removes existing infatuation when gained

2. **Restriction Immunity** (CHECK_RESTRICTING)
   - **Taunt**: Cannot be taunted
   - **Disable**: Cannot have moves disabled  
   - **Encore**: Cannot be locked into moves
   - **Torment**: Cannot be prevented from using same move

### Technical Implementation

**Code Structure** (`src/abilities.cc`):
```cpp
constexpr Ability Oblivious = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_INFATUATE)
        CHECK(status & CHECK_RESTRICTING)
        return TRUE;
    },
    .tauntImmune = TRUE,
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Important Note
Despite the description mentioning "Intimidate immunity," the actual implementation does NOT provide immunity to Intimidate's Attack reduction. This is a description error.

### What CHECK_RESTRICTING Includes
From battle code analysis:
- Active Taunt timer
- Active Disable timer  
- Active Encore timer
- Torment status effect

### Key Properties
- **Breakable**: Can be suppressed by Mold Breaker
- **Status Removal**: Clears restrictions when gained
- **Ability Popup**: Shows when effects are blocked

### Strategic Implications

1. **Setup Sweeper Protection**
   - Can't be Taunted out of setup moves
   - Can't be Encored into setup moves
   - Maintains move flexibility

2. **Stall Breaking**
   - Ignores Taunt on recovery moves
   - Can't be Disabled out of key moves
   - Full moveset always available

3. **Attract Immunity**
   - Gender-based strategies fail
   - Cute Charm contact safe

### Battle Scenarios

**vs Taunt Lead**: 
- Opponent uses Taunt to Fails
- Can still use Stealth Rock, Recover, etc.

**vs Encore Trap**:
- Uses Protect to Opponent uses Encore to Fails
- Not locked into Protect

**vs Disable**:
- Uses Hydro Pump to Opponent uses Disable to Fails
- Can continue using Hydro Pump

### Common Oblivious Users
- **Slowbro/Slowking**: Defensive walls
- **Swinub line**: Physical attackers
- **Wailord**: Special tank
- **Barboach/Whiscash**: Ground/Water types
- Various Pokemon as ability option

### Competitive Usage Notes
- B-tier utility ability
- Excellent on defensive Pokemon
- Valuable for setup sweepers
- Counters common disruption strategies
- AI rates it relatively low (2/10)

### What It Doesn't Block
- **Intimidate**: Attack drops still occur
- **Scare moves**: If they exist separately
- **Imprison**: Move locking via shared moves
- **Heal Block**: Recovery prevention
- **Embargo**: Item prevention

### Counters
- **Mold Breaker**: Bypasses Oblivious
- **Direct damage**: No defensive benefits
- **Status conditions**: Burn, paralysis work normally
- **Stat reduction**: Intimidate, Screech work
- **Gastro Acid**: Removes the ability

### Synergies
- **Setup moves**: Dragon Dance, Calm Mind safe from Taunt
- **Recovery moves**: Rest, Recover can't be Taunted
- **Choice items**: Less punishable with Encore immunity
- **Substitute**: Can't be Encored into it
- **Baton Pass**: Pass boosts without Taunt fear

### Similar Abilities
- **Aroma Veil**: Team-wide mental immunity
- **Inner Focus**: Flinch immunity
- **Own Tempo**: Confusion immunity
- Various abilities providing specific immunities

### Practical Applications
**Lead Pokemon**: Set hazards despite Taunt
**Defensive Walls**: Use recovery freely
**Setup Sweepers**: Boost without disruption
**Choice Users**: Switch moves despite Encore

### Version History
- **Gen IV**: Introduced with Infatuation immunity
- **Gen VI+**: Added Taunt immunity
- **Elite Redux**: Expanded to full restriction immunity
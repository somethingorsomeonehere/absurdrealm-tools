---
id: 472
name: Super Slammer
status: reviewed
character_count: 60
---

# Super Slammer - Ability ID 472

## In-Game Description
"Boosts the power of hammer and slamming moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Super Slammer boosts the power of hammer-based moves by 30%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Super Slammer is an offensive ability that provides a 1.3x damage multiplier (30% increase) to moves classified as hammer-based. This ability activates during damage calculation and applies to the move's base power.

### Activation Conditions
- **Move requirement**: The move must have the `hammerBased` flag set to true
- **Timing**: Multiplier applies during damage calculation phase
- **Boost amount**: 1.3x damage multiplier (30% increase)
- **Contact moves**: Most hammer moves are contact moves, making them subject to contact-based effects

### Technical Implementation
```c
// Super Slammer implementation in abilities.cc
constexpr Ability SuperSlammer = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (gBattleMoves[move].hammerBased) MUL(1.3);
        },
};
```

### Affected Moves
Super Slammer boosts the following hammer-based moves:

**Original Hammer Moves:**
- Hammer Arm (Fighting-type)
- Wood Hammer (Grass-type) 
- Crabhammer (Water-type)

**Elite Redux Custom Hammer Moves:**
- Dragon Hammer (Dragon-type)
- Gigaton Hammer (Steel-type)
- Megaton Hammer (Fighting-type)
- Shadow Hammer (Ghost-type)
- Molten Strike (Fire-type)
- Crackle Slam (Electric-type)
- Battering Ram (Dragon-type)
- Beetle Bash (Bug-type)
- And many other custom hammer variations

### Important Interactions
- **Iron Fist synergy**: Many hammer moves also have the `iron_fist` flag, allowing double stacking with Iron Fist ability
- **Contact effects**: Most hammer moves make contact, triggering abilities like Static, Rough Skin, etc.
- **Reckless compatibility**: Some hammer moves have recoil, making them compatible with Reckless ability
- **Sheer Force**: Does not prevent Sheer Force from removing secondary effects on applicable moves

### Multiplier Stacking
Super Slammer's 1.3x multiplier stacks multiplicatively with other damage modifiers:
- **Type effectiveness**: 1.3x x type modifier
- **STAB**: 1.3x x 1.5 for same-type moves
- **Items**: 1.3x x held item multipliers
- **Other abilities**: 1.3x x other ability multipliers
- **Weather/terrain**: 1.3x x environmental multipliers

### Strategic Implications
- **Physical attacker role**: Best used on physical attackers with access to hammer moves
- **Move variety**: Elite Redux has many custom hammer moves across different types
- **Contact considerations**: Be aware of contact punishing abilities when using hammer moves  
- **Power boost**: Significant 30% damage increase makes hammer moves much more viable
- **Movepool dependent**: Effectiveness depends on having good hammer moves available

### Common Users
Pokemon that benefit most from Super Slammer:
- Physical attackers with hammer move access
- Multi-type hammer users (can use different hammer types)
- Pokemon with Iron Fist as secondary ability for double stacking
- Custom Elite Redux Pokemon designed around hammer movesets

### Competitive Usage Notes
- **Niche but powerful**: Strong ability for Pokemon with good hammer movepools
- **Type coverage**: Hammer moves span many types in Elite Redux
- **Contact risk**: Most hammer moves make contact, creating risk/reward scenarios
- **Setup sweeper**: Pairs well with setup moves like Swords Dance
- **Choice item synergy**: Works well with Choice Band for massive damage output

### Counters
- **Contact punishment**: Abilities like Rough Skin, Static, Flame Body
- **Physical walls**: High Defense stats reduce hammer move effectiveness
- **Intimidate**: Lowers Attack stat, reducing hammer move damage
- **Burn**: Halves physical damage output
- **Protection moves**: Protect, Detect, and King's Shield block hammer moves

### Synergies
- **Iron Fist**: Double stacking on moves with both flags
- **Choice Band**: Massive damage boost for physical hammer moves
- **Life Orb**: Additional damage boost with recoil tradeoff
- **Swords Dance**: Setup sweeping with boosted hammer moves
- **Trick Room**: Slow hammer users can benefit from speed reversal

### Notable Differences from Description
The in-game description mentions "hammer and slamming moves" but the actual implementation only boosts moves with the `hammerBased` flag. There is no separate `slamBased` flag in the current implementation, so traditional "slam" moves like Body Slam are not affected unless they also have the hammer flag.

### Version History
- Elite Redux custom ability
- Designed to make hammer-based moves more viable
- Part of the expanded ability roster for diverse team building
- Implementation focuses on `hammerBased` flag rather than move names
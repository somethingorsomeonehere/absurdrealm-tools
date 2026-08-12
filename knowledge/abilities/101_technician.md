---
id: 101
name: Technician
status: reviewed
character_count: 156
---

# Technician - Ability ID 101

## In-Game Description
"Moves with 60 BP or less get a 1.5x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts moves with 60 BP or less by 1.5x. Does not boost moves with 60 BP or less if they potentially can have more than 60 BP, such as Revenge or Venoshock.  

## Detailed Mechanical Explanation

### Implementation
```cpp
constexpr Ability Technician = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (basePower <= 60) MUL(1.5);
        },
};
```

### Key Mechanics
1. **Power Threshold**: Applies to moves with 60 base power or less
2. **Damage Multiplier**: 1.5x (50% increase)
3. **Multi-hit Calculation**: For multi-hit moves, the check is done per individual hit
4. **Priority Move Synergy**: Many priority moves are low power and benefit from Technician
5. **Hidden Power**: Always benefits regardless of type (base power is 60)

### Affected Move Examples
- **Priority Moves**: Bullet Punch (40to60), Mach Punch (40to60), Quick Attack (40to60)
- **Multi-hit Moves**: Bullet Seed (25to37.5 per hit), Pin Missile (25to37.5 per hit)
- **Utility Moves**: Rapid Spin (50to75), Fake Out (40to60)
- **Coverage Moves**: Hidden Power (60to90), Aerial Ace (60to90)
- **Status Moves**: Doesn't affect status moves (0 base power)

### Notable Interactions
- Works with Skill Link for devastating multi-hit combos
- Stacks with STAB and other damage multipliers
- Does NOT affect moves that have variable power (like Low Kick)
- The 60 BP check happens before other power modifications

## Pokemon with Technician

### As Changeable Ability
- Persian-Alola (tier 3)
- Krabby (tier 1)
- Kingler-Johto (tier 3)
- Wormadour (tier 1)
- Hitmontop (tier 3)
- Minccino (tier 1)
- Ambipom (tier 3)

### As Innate Ability
- Persian (tier 3) - innate slot
- Persian-Alola (tier 3) - innate slot
- Kingler (tier 3) - innate slot
- Beedrill (tier 3) - innate slot
- Kricketune (tier 3) - innate slot
- Roserade (tier 4) - innate slot
- Scizor (tier 4) - innate slot

## Competitive Analysis

### Strengths
- Turns weak priority moves into legitimate threats
- Excellent on fast physical attackers with priority access
- Makes multi-hit moves extremely powerful with Skill Link
- Provides unique coverage options with boosted weak moves
- Great for revenge killing with boosted priority

### Weaknesses
- No effect on stronger moves (>60 BP)
- Requires specific movepool to utilize effectively
- Less useful on special attackers due to limited low-BP special moves
- Competes with potentially stronger abilities on some Pokemon

### Optimal Users
1. **Scizor**: Bullet Punch becomes a 90 BP priority STAB move
2. **Ambipom**: Fake Out + multi-hit moves with great coverage
3. **Breloom**: Mach Punch and Bullet Seed synergy
4. **Persian**: Wide movepool of low-BP coverage moves
5. **Roserade**: Benefits special moves like Hidden Power and Magical Leaf

### Team Synergy
- Pairs well with entry hazard support for chip damage
- Benefits from speed control to maximize priority abuse
- Works great with Sticky Web teams
- Synergizes with weather teams using weather-boosted low BP moves

## Moveset Examples

### Physical Technician Set
- Bullet Punch / Mach Punch (priority STAB)
- U-turn (pivot + damage)
- Pursuit (trap + boost)
- Knock Off / Thief (utility + boost)

### Special Technician Set
- Hidden Power (coverage)
- Vacuum Wave (priority)
- Magical Leaf (never miss)
- Swift (never miss + spread in doubles)

### Multi-hit Technician Set
- Bullet Seed (2-5 hits boosted)
- Rock Blast (2-5 hits boosted)
- Pin Missile (2-5 hits boosted)
- Icicle Spear (2-5 hits boosted)

## Notes
- One of the most popular abilities for physical priority users
- Elite Redux has many Pokemon with this as an innate ability
- Particularly strong in the early-game where low BP moves are common
- Calculation happens before other damage modifiers like STAB

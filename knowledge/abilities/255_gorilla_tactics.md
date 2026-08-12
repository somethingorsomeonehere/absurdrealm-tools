---
id: 255
name: Gorilla Tactics
status: reviewed
character_count: 126
---

# Gorilla Tactics - Ability ID 255

## In-Game Description
"Boosts physical moves but restricts choice like Choice Band."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gorilla Tactics boosts physical move power by 50% but locks the user into using the first move selected until they switch out.

## Detailed Mechanical Explanation
*For Discord/reference use*

**GORILLA TACTICS** is a powerful offensive ability that provides significant physical damage output at the cost of move flexibility.

### Core Mechanics:
- **Power Boost**: Multiplies physical move damage by 1.5x (50% increase)
- **Move Lock**: After using the first move, restricts the Pokemon to only that move
- **Activation Timing**: Applied during damage calculation via onOffensiveMultiplier hook
- **Physical Moves Only**: Only affects moves where IS_MOVE_PHYSICAL(move) returns true

### Choice-Like Behavior:
- **Move Restriction**: Functions identically to Choice Band's move-locking mechanism
- **Shared Code Path**: Groups with Sage Power and Discipline abilities in battle logic
- **Battle Script**: Uses BattleScript_SelectingNotAllowedMoveGorillaTactics when attempting different moves
- **Reset Condition**: Choice lock resets only when the Pokemon switches out

### Technical Implementation:
```c
constexpr Ability GorillaTactics = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IS_MOVE_PHYSICAL(move)) MUL(1.5);
        },
};
```

### Calculation Order:
1. **Base move power** (from move data)
2. **STAB** (Same Type Attack Bonus, if applicable)
3. **Gorilla Tactics multiplier** (x1.5 for physical moves)
4. **Item effects** (Life Orb, Expert Belt, etc.)
5. **Other ability effects** (Technician, Sheer Force, etc.)
6. **Critical hit multiplier** (if applicable)

### Key Interactions:
- **vs Choice Band**: Both effects stack multiplicatively (1.5 x 1.5 = 2.25x total)
- **vs Life Orb**: Stacks multiplicatively for 1.5 x 1.3 = 1.95x damage
- **vs Technician**: Stacks with Technician's 1.5x boost for weak moves
- **vs Special Moves**: No effect on special attacks (Thunder Punch, Focus Blast, etc.)
- **vs Status Moves**: No effect on non-damaging moves

### Strategic Applications:
1. **Physical Sweeper Setup**: Ideal for Pokemon with high Attack and diverse physical movepool
2. **Choice Item Synergy**: Can stack with Choice Band for massive damage output
3. **Priority Move Abuse**: Makes priority moves hit with significant power
4. **Wallbreaking**: Enables moderately powerful moves to break through defensive Pokemon

### Pokemon Distribution in Elite Redux:
- **Primary Users**: Primeape (paired with Choice Scarf in trainer teams)
- **Common on**: Physical attackers that benefit from immediate power over flexibility
- **Team Role**: Mid-game wallbreaker, late-game cleaner with proper support

### Competitive Analysis:
- **Power Level**: Very high - substantial damage increase with significant restriction
- **Risk vs Reward**: High damage output balanced by loss of move flexibility
- **Switching Importance**: Requires good team support to manage move locks effectively
- **Prediction Reliance**: Success depends heavily on correct move predictions

### Ability Relationships:
- **Sage Power (ID 352)**: Shares identical choice-locking logic in battle code
- **Discipline (ID 387)**: Also grouped in the same choice restriction system
- **Choice Band**: Provides same power boost and restriction but as held item

### Common Misconceptions:
- **NOT a stat boost**: Multiplies damage, doesn't increase Attack stat itself
- **Only physical moves**: Special moves receive no benefit whatsoever
- **Cannot be Skill Swapped**: Choice-locking state tied to individual Pokemon, not ability
- **Switching resets**: Must switch out to use different moves, no in-battle reset

### Counters and Responses:
1. **Defensive Walls**: High Defense Pokemon can still tank boosted hits
2. **Intimidate**: Reduces Attack stat, partially offsetting the damage boost
3. **Burn Status**: Halves Attack, significantly reducing effectiveness
4. **Switching**: Prediction and switching can waste the locked move
5. **Ghost-types**: Immune to Normal and Fighting moves commonly used

### Version History:
- **Generation 8**: Originally introduced in Sword/Shield
- **Elite Redux**: Implemented with modern callback system and choice-locking integration
- **Battle AI**: Recognized by AI systems for proper move selection and switching logic

### Usage Tips:
- **Lead with Coverage**: Choose moves that hit multiple common threats
- **Late-Game Cleaning**: Most effective when opponent's team is weakened
- **Team Support**: Pair with pivots and entry hazard support
- **Item Synergy**: Consider Choice Scarf for speed or Choice Band for raw power
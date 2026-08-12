---
id: 89
name: Iron Fist
status: reviewed
character_count: 42
---

# Iron Fist - Ability ID 89

## In-Game Description
"Boosts the power of punching moves by 1.3x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of punching moves by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

**IRON FIST** is a damage-boosting ability that enhances the power of punching moves.

### Activation Mechanics:
- **Trigger**: Offensive damage calculation hook (onOffensiveMultiplier)
- **Condition**: Move must have FLAG_IRON_FIST_BOOST flag
- **Multiplier**: 1.3x (30% boost) to move power
- **Type**: Universal - works with all move types

### Boosted Moves:
Iron Fist affects all moves with the punching flag, including but not limited to:
1. **Elemental Punches**: Fire Punch, Ice Punch, Thunder Punch
2. **Fighting Punches**: Mach Punch, Drain Punch, Dynamic Punch, Focus Punch
3. **Priority Punches**: Bullet Punch, Mach Punch, Sucker Punch
4. **Other Punching Moves**: Hammer Arm, Mega Punch, Comet Punch, Shadow Punch, Dizzy Punch
5. **Special Cases**: Power-Up Punch, Meteor Mash, Sky Uppercut, Ice Hammer

### Technical Implementation:
```c
constexpr Ability IronFist = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (IsIronFistBoosted(battler, move)) MUL(1.3);
        },
};
```

### Damage Calculation:
The 1.3x multiplier is applied during damage calculation and stacks multiplicatively with:
- **STAB**: 1.5x (1.95x total with Iron Fist)
- **Weather boosts**: e.g., Fire Punch in sun (1.95x total)
- **Item boosts**: Choice Band, Life Orb, etc.
- **Other abilities**: Sheer Force (if move has secondary effect)

### Calculation Examples:
- Base 100 BP Fire Punch to 130 BP with Iron Fist
- STAB Fire Punch (150 BP) to 195 BP with Iron Fist
- Fire Punch in sun with STAB and Iron Fist to 292.5 BP

### Special Interactions:
1. **Punching Glove Item**: When holding Punching Glove, Iron Fist-boosted moves get an additional 1.1x multiplier
2. **Brawling Wyvern**: Dragon-type moves also count as Iron Fist-boosted for this ability
3. **Junshi Sanda**: Striker-boosted moves count as Iron Fist-boosted for this ability

### Related Abilities:
- **Power Fists**: Iron Fist effect + forces punching moves to target Special Defense
- **Magical Fists**: Iron Fist effect + punching moves use Special Attack stat
- **Nika**: Iron Fist effect + Water moves function normally under sun
- **Blitz Boxer**: Priority to punching moves at full HP
- **Raging Boxer**: Punching moves hit twice at 70% power each
- **Precise Fist**: Punching moves always crit + 5x secondary effect chance

### Synergistic Items:
- **Punching Glove**: Additional 1.1x boost to Iron Fist moves (1.43x total)
- **Choice Band**: 1.5x Attack for physical punching moves
- **Life Orb**: 1.3x damage at cost of 10% HP

### Strategic Applications:
1. **Physical Sweeper**: High Attack Pokemon using boosted priority Bullet Punch
2. **Coverage**: Elemental punches provide excellent type coverage
3. **Fighting STAB**: Makes Fighting-types exceptional with STAB Drain Punch/Close Combat
4. **Priority Abuse**: Bullet Punch and Mach Punch become significant threats

### Competitive Notes:
- Essential for Pokemon with good Attack and access to punching moves
- Elemental punches provide special coverage on physical sets
- Priority moves like Bullet Punch become viable revenge killing tools
- Pairs excellently with Technician on low BP punching moves

### Version History:
- Gen 4: Introduced with 1.2x boost
- Gen 5+: Buffed to 1.3x boost
- Elite Redux: Maintained at 1.3x, interacts with multiple compound abilities
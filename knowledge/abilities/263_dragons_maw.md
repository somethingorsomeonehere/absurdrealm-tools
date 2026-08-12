---
id: 263
name: Dragons Maw
status: reviewed
character_count: 58
---

# Dragons Maw - Ability ID 263

## In-Game Description
"Boosts the power of Dragon-type moves by 1.5x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Dragon's Maw boosts the power of Dragon-type moves by 50%.

## Detailed Mechanical Explanation
*For Discord/reference use*

**DRAGONS MAW** is a type-specific damage-boosting ability that enhances the power of Dragon-type moves.

### Activation Mechanics:
- **Trigger**: Offensive damage calculation hook (onOffensiveMultiplier)
- **Condition**: Move must be Dragon-type
- **Multiplier**: 1.5x (50% boost) to move power
- **Category**: Universal - affects both physical and special Dragon moves

### Boosted Moves:
Dragon's Maw affects all Dragon-type moves, including but not limited to:
1. **Physical Dragon Moves**: Dragon Rush, Dragon Claw, Outrage, Dual Chop, Dragon Tail
2. **Special Dragon Moves**: Dragon Pulse, Draco Meteor, Dragon Breath, Spacial Rend, Roar of Time
3. **Priority Dragon Moves**: Dragon Darts (if applicable)
4. **Status Dragon Moves**: Dragon Dance (no damage boost, but still Dragon-type)
5. **Multi-hit Dragon Moves**: Dragon Darts, Dual Chop
6. **Z-Moves**: Devastating Drake and any Dragon-type Z-Move

### Technical Implementation:
```c
constexpr Ability DragonsMaw = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (GetMoveType(battler, move) == TYPE_DRAGON) MUL(1.5);
        },
};
```

### Damage Calculation:
The 1.5x multiplier is applied during damage calculation and stacks multiplicatively with:
- **STAB**: 1.5x (2.25x total with Dragon's Maw for Dragon-types)
- **Weather boosts**: No direct Dragon weather, but Sunny Day can boost Solar Beam coverage
- **Item boosts**: Choice Specs/Band, Life Orb, Dragon Fang, etc.
- **Other abilities**: Sheer Force (if Dragon move has secondary effect)

### Calculation Examples:
- Base 100 BP Dragon Pulse to 150 BP with Dragon's Maw
- STAB Dragon Pulse on Dragon-type (150 BP) to 225 BP with Dragon's Maw
- Dragon Claw with Choice Band, STAB, and Dragon's Maw to 337.5 BP
- Draco Meteor with Life Orb, STAB, and Dragon's Maw to 292.5 BP

### Special Interactions:
1. **Dragon Fang Item**: Additional 1.2x boost to Dragon moves (1.8x total with Dragon's Maw)
2. **Adaptability**: Dragon-types with this get 2x STAB instead of 1.5x (3x total with Dragon's Maw)
3. **Sheer Force**: If Dragon move has secondary effect, Sheer Force removes effect but adds 1.3x boost
4. **Life Orb**: 1.3x boost with 10% HP recoil, stacks multiplicatively

### Synergistic Items:
- **Dragon Fang**: Additional 1.2x boost to Dragon moves (1.8x total)
- **Choice Specs/Band**: 1.5x boost to Special/Physical Attack for Dragon moves
- **Life Orb**: 1.3x damage boost at cost of 10% HP per attack
- **Dragonium Z**: Converts Dragon move to 1-time devastating Z-Move

### Strategic Applications:
1. **Dragon Sweeper**: High Attack/Special Attack Dragon-types become overwhelming
2. **Late-game Cleaner**: Draco Meteor becomes a nuke against weakened teams
3. **STAB Abuse**: Dragon-types get 2.25x total multiplier (1.5x STAB + 1.5x Dragon's Maw)
4. **Mixed Attacker**: Both physical and special Dragon moves benefit equally

### Competitive Notes:
- Essential for mono-Dragon teams and Dragon-type specialists
- Makes weaker Dragon moves like Dragon Breath viable
- Particularly powerful on Pokemon with high base Attack/Special Attack
- Pairs excellently with Choice items for overwhelming power
- Compensates for Dragon-type's often limited move coverage

### Related Abilities:
- **Dragonslayer**: Deals extra damage TO Dragons rather than WITH Dragon moves
- **Adaptability**: Enhances STAB bonus (pairs well with Dragon's Maw on Dragon-types)
- **Sheer Force**: Can stack with Dragon's Maw if Dragon move has secondary effect

### Pokemon Synergy:
Best used on:
- **Pure Dragon-types**: Maximize STAB synergy
- **High Attack/SpA Dragons**: Salamence, Garchomp, Hydreigon-like Pokemon
- **Mixed Attackers**: Pokemon that can use both physical and special Dragon moves
- **Late-game Sweepers**: Pokemon designed to clean up with powerful Dragon attacks

### Version History:
- Gen 8: Introduced as signature ability concept
- Elite Redux: Implemented as standard type-boosting ability at 1.5x multiplier
- Functions identically to other type-boosting abilities like Iron Fist but for Dragon-type moves
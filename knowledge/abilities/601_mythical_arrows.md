---
id: 601
name: Mythical Arrows
status: reviewed
character_count: 112
---

# Mythical Arrows - Ability ID 601

## In-Game Description
"Arrow moves become special and deal 30% more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Arrow moves moves become Special (deal Special damage and use the Special Attack stat) and deal 30% more damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MYTHICAL ARROWS** is a move conversion ability that transforms physical arrow-based moves into special attacks while providing a substantial damage boost.

### Core Mechanics:
- **Damage Multiplier**: 1.3x (30% boost) to all arrow-based moves
- **Move Conversion**: Changes physical arrow moves to special category
- **Stat Usage**: Converted moves use Special Attack and target Special Defense
- **Effect Retention**: All secondary effects of arrow moves are preserved

### Technical Implementation:
```c
constexpr Ability MythicalArrows = {
    .onOffensiveMultiplier = Archer.onOffensiveMultiplier,  // 1.3x multiplier
    .onSwapSplit = +[](ON_SWAP_SPLIT) -> int {
        CHECK(gBattleMoves[move].split == SPLIT_PHYSICAL)
        CHECK(gBattleMoves[move].arrowBased);
        return TRUE;  // Converts to special
    },
};
```

### Complete List of Arrow Moves:
1. **Spirit Shackle** - Ghost, 80 BP, prevents switching
2. **Archer Shot** - Normal, 90 BP, high crit ratio
3. **Frost Bolt** - Ice, 90 BP, 10% freeze chance
4. **Supersonic Shot** - Flying, 40 BP, always flinches
5. **Lightning Strike** - Electric, 130 BP, 30% paralysis
6. **Volt Bolt** - Electric, 90 BP, 30% paralysis
7. **Bramble Blast** - Grass, 60 BP, applies Leech Seed
8. **Cupid Shot** - Fairy, 50 BP, infatuates target
9. **Clay Dart** - Ground, 55 BP, hits 2-5 times
10. **Diamond Arrow** - Rock, 100 BP, 50% defense boost
11. **Venom Bolt** - Poison, 130 BP, badly poisons
12. **Blazing Arrow** - Fire, 120 BP, 50% burn chance
13. **Web Shot** - Bug, 40 BP, sets Sticky Web
14. **Drake Missile** - Dragon, 85 BP, standard
15. **Homing Fletch** - Steel, varies BP, never misses
16. **Devious Shot** - Dark, 80 BP, lowers Special Defense
17. **Triple Arrows** - Fighting, 50 BP, +1 crit, 30% flinch, lowers defense
18. **Sparkling Barrage** - Varies type, 120 BP, matches user's type

### Notable Users:
- **Aegislash Redux (Blade Form)**:
  - 60/130/50/140/50/95 stats - exceptional Special Attack
  - Has Mythical Arrows as an innate ability
  - Access to diverse arrow coverage
- **Mega Aegislash Redux**:
  - 60/130/50/200/80/120 stats - monstrous 200 Special Attack
  - Retains Mythical Arrows innate
  - Can OHKO most Pokemon with boosted arrows

### Strategic Implications:
1. **Coverage Monster**: 18 moves across nearly every type
2. **Status Spreader**: Burns, paralysis, poison, infatuation, stat drops
3. **Hazard Setting**: Web Shot sets Sticky Web as special damage
4. **Mixed Attacker Facade**: Physical attacker appearance with special damage

### Damage Calculations:
**Mega Aegislash Redux Examples** (200 Special Attack):
- Blazing Arrow: 120 BP to 156 BP special Fire + 50% burn
- Venom Bolt: 130 BP to 169 BP special Poison + toxic
- Lightning Strike: 130 BP to 169 BP special Electric + 30% paralysis

### Unique Interactions:
- **Triple Arrows**: Becomes a special Fighting move with multiple effects
- **Spirit Shackle**: Ghost-type special trapping move
- **Sparkling Barrage**: Adapts to user's type as special damage
- **Diamond Arrow**: Special Rock move that boosts defense

### Competitive Usage:
- **Hazard Lead**: Web Shot for special-damage Sticky Web
- **Status Spreader**: Multiple high-chance status arrows
- **Wallbreaker**: Unexpected special damage from "physical" attacker
- **Trapper**: Spirit Shackle prevents switching while dealing special damage

### Example Set:
**Mega Aegislash Redux @ Life Orb**
- Blazing Arrow (Fire coverage + burn)
- Venom Bolt (Poison STAB + toxic)
- Lightning Strike (Electric coverage + paralysis)
- Spirit Shackle (Ghost STAB + trap)

### Counters:
- Special walls that resist multiple types
- Priority users (before Aegislash can attack)
- Prankster status moves
- Multi-hit moves to break King's Shield

### Synergies:
- **Sticky Web Support**: Sets hazards while dealing damage
- **Status Teams**: Spreads multiple statuses efficiently
- **VoltTurn**: Sparkling Barrage can be Electric-type U-turn

### Version History:
- Elite Redux exclusive ability
- Designed specifically for Aegislash Redux variants
- Creates unique special attacking arrow user archetype
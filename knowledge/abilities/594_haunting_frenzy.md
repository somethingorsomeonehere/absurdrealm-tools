---
id: 594
name: Haunting Frenzy
status: reviewed
character_count: 104
---

# Haunting Frenzy - Ability ID 594

## In-Game Description
"20% chance to flinch the opponent. +1 speed on kill."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Attacks have a 20% chance to flinch. Upon defeating an enemy with a direct hit, the user gains +1 Speed.

## Detailed Mechanical Explanation

**Internal Name**: ABILITY_HAUNTING_FRENZY

### Mechanics

### Flinch Component
- **Trigger**: On successful attack that damages the target
- **Probability**: 20% chance per hit
- **Requirements**: 
  - Move must have the `FLAG_KINGS_ROCK_AFFECTED` flag (same moves affected by King's Rock)
  - Target must be alive after the attack
  - Move must successfully hit and deal damage
- **Effect**: Applies flinch status (MOVE_EFFECT_FLINCH) directly to the target

### Speed Boost Component  
- **Trigger**: When the Pokemon with this ability causes an opponent to faint
- **Effect**: Raises Speed stat by +1 stage
- **Implementation**: Uses the same mechanism as Adrenaline Rush ability (MoxieClone with STAT_SPEED)
- **Applies**: Only to the attacking Pokemon with Haunting Frenzy

### Move Compatibility
Works with any damaging move that has the `FLAG_KINGS_ROCK_AFFECTED` flag, including:
- Basic attacks like Pound, Scratch, Tackle
- High critical hit moves like Karate Chop
- Multi-hit moves like Double Slap
- Most physical and special attacking moves that don't inherently cause flinch

### Strategic Applications

### Offensive Pressure
- Creates consistent flinch pressure (20% vs King's Rock's ~10%)
- Forces opponents to make risky plays or switch frequently
- Particularly effective against slower, bulky Pokemon

### Speed Control
- Speed boosts from KOs create snowball potential
- Each elimination makes subsequent sweeps more likely
- Synergizes well with choice items and momentum-based strategies

### Synergies
- **Choice Band/Specs**: Maximizes flinch chances while maintaining power
- **Fast attackers**: Natural speed advantage amplified by stat boosts
- **Multi-hit moves**: Multiple flinch chances per turn
- **Revenge killing**: Speed boosts help secure follow-up KOs

### Counters and Limitations

### Direct Counters
- **Inner Focus**: Completely immune to flinch effects
- **Own Tempo**: Prevents flinch from confusion interactions
- **Substitute**: Blocks both flinch and speed boost triggers

### Strategic Counters  
- Priority moves bypass flinch mechanics
- Status moves unaffected by flinch component
- Faster Pokemon can outspeed before speed boosts accumulate
- Bulky walls that resist being KO'd prevent speed boosts

### Code Implementation
```cpp
constexpr Ability HauntingFrenzy = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanMoveHaveExtraFlinchChance(move))
        CHECK(Random() % 100 < 20)
        
        return AbilityStatusEffectDirect(MOVE_EFFECT_FLINCH);
    },
    .onBattlerFaints = AdrenalineRush.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```


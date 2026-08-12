---
id: 1
name: Stench
status: reviewed
character_count: 285
---

# Stench - Ability ID 1

## In-Game Description
"10% chance to make the target flinch. Halves wild Pokemon encounters."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Attacks gain +10% flinch chance. Stacks additively with other flinch sources. Multihits roll the activation chance on each hit. Outside of battle, wild Pokemon appear half as often when this Pokemon leads the party. Toxic Terrain active turns do not decrease while the user is present.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Stench in Elite Redux has been enhanced from its original implementation with two distinct effects:

1. **Battle Effect - Flinch Chance (10%)**
   - Grants a 10% chance to cause flinching on ANY move that is affected by King's Rock
   - Works on both contact and non-contact moves (unlike main series where it's contact-only)
   - Stacks with existing flinch chances (e.g., a move with 30% flinch becomes 40%)
   - Does not affect moves that cannot naturally cause flinching

2. **Overworld Effect - Encounter Rate Reduction**
   - **Normal areas**: Wild encounter rate is halved (50% reduction)
   - **Battle Pyramid**: Wild encounter rate reduced by 25% (multiplied by 3/4)
   - Only works when the Pokemon with Stench is in the first party slot
   - The Pokemon must not be an egg

### Technical Implementation

**Battle Implementation** (`src/abilities.cc`):
```cpp
constexpr Ability Stench = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanMoveHaveExtraFlinchChance(move))
        CHECK(Random() % 100 < 10)
        
        return AbilityStatusEffectDirect(MOVE_EFFECT_FLINCH);
    },
};
```

**Overworld Implementation** (`src/wild_encounter.c`):
```c
if (ability == ABILITY_STENCH && gMapHeader.mapLayoutId == LAYOUT_BATTLE_FRONTIER_BATTLE_PYRAMID_FLOOR)
    encounterRate = encounterRate * 3 / 4;
else if (ability == ABILITY_STENCH)
    encounterRate /= 2;
```

### Affected Moves
All moves with the `FLAG_KINGS_ROCK_AFFECTED` flag can trigger Stench's flinch effect. This includes most damaging moves except:
- Moves that already have a 100% secondary effect
- Multi-hit moves
- Certain signature moves

### Interactions with Other Abilities/Mechanics
- **King's Rock/Razor Fang**: Effects stack multiplicatively (19% total flinch chance)
- **Serene Grace**: Would affect the base move's flinch chance but not Stench's addition
- **Inner Focus/Shield Dust**: Prevents the flinch from occurring
- **Steadfast**: Opponent gains Speed boost if they have this ability

### Strategic Implications
- Excellent on fast Pokemon that can capitalize on flinching slower opponents
- Pairs well with high-power moves that normally can't flinch
- Provides utility for exploration by reducing grinding time
- More valuable in Elite Redux due to working on all attack types

### Example Damage Calculations
Since Stench doesn't affect damage, the key calculation is flinch probability:
- Base move with no flinch: 10% flinch chance
- Iron Head (30% flinch): 40% total flinch chance
- With King's Rock on non-flinch move: 19% total flinch chance

### Common Users
- Skuntank (signature user in original games)
- Grimer/Muk lines
- Trubbish/Garbodor lines
- Various Poison-type Pokemon

### Competitive Usage Notes
- Mid-tier ability that provides decent utility
- Best on offensive Pokemon with good Speed stats
- Can create "paraflinch" strategies with Thunder Wave
- The encounter reduction is valuable for nuzlockes and speedruns

### Counters
- **Inner Focus**: Complete immunity to flinching
- **Steadfast**: Turns flinches into Speed boosts
- **Faster Pokemon**: Can't flinch if they move first
- **Shield Dust**: Prevents secondary effects

### Synergies
- **Paralysis Support**: Ensures you move first to utilize flinch chance
- **Sticky Web/Tailwind**: Speed control to enable flinching
- **King's Rock**: Stacks for higher flinch chance
- **U-turn/Volt Switch**: Hit and potentially flinch before switching

### Version History
- **Generation III-IV**: Only had overworld effect
- **Generation V+**: Added 10% flinch chance to contact moves
- **Elite Redux**: Enhanced to work on all King's Rock-affected moves
---
id: 450
name: Earth Eater
status: reviewed
character_count: 86
---

# Earth Eater - Ability ID 450

## In-Game Description
"Heals 25% of max HP when hit by a Ground move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Earth Eater heals the Pokemon for 25% of its maximum HP when hit by Ground-type moves. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Earth Eater is a defensive absorption ability that converts Ground-type damage into healing. When the Pokemon with Earth Eater is targeted by a Ground-type move, instead of taking damage, it recovers 25% of its maximum HP.

### Activation Conditions
- **Move type requirement**: The attacking move must be Ground-type
- **Damage nullification**: The move deals 0 damage regardless of power
- **Healing amount**: Restores exactly 25% of maximum HP (rounded down, minimum 1 HP)
- **HP cap**: Cannot heal above maximum HP
- **Healing restriction**: Only heals if the Pokemon can be healed (not affected by Heal Block)

### Technical Implementation
```c
constexpr Ability EarthEater = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_GROUND)
        return ABSORB_RESULT_HEAL;
    },
    .breakable = TRUE,
};

// In battle_util.c, ABSORB_RESULT_HEAL triggers:
// gBattleMoveDamage = gBattleMons[battler].maxHP / 4; // 25% healing
// gBattleMoveDamage *= -1; // Negative = healing
```

### Ground Moves That Trigger Earth Eater
- **Physical Ground moves**: Earthquake, Drill Run, Bulldoze, Stomping Tantrum
- **Special Ground moves**: Earth Power, Mud Bomb, Scorching Sands
- **Status Ground moves**: Spikes (on entry), Thousand Arrows (even hits Flying types)
- **Multi-hit Ground moves**: Each hit would trigger healing separately
- **Z-Moves and Max Moves**: Ground-type variants are absorbed

### Important Interactions
- **Flying types**: Earth Eater users who are Flying-type still absorb Ground moves
- **Levitate interaction**: If a Pokemon has both, Earth Eater takes priority
- **Ability suppression**: Doesn't work if ability is suppressed by Mold Breaker variants
- **Substitute**: Ground moves hitting Substitute don't trigger Earth Eater
- **Magic Bounce**: Reflected Ground moves don't trigger the original user's Earth Eater

### Damage Calculation Override
- **Power independence**: Healing is always 25% regardless of move power
- **Critical hits**: Don't affect healing amount
- **STAB/effectiveness**: Completely irrelevant as no damage is dealt
- **Stat stages**: Attack/Defense stats don't matter for healing calculation

### Strategic Implications
- **Ground immunity**: Provides complete immunity to the most common offensive type
- **Earthquake synergy**: Teammates can use Earthquake freely
- **Pivot potential**: Can switch into predicted Ground moves for free healing
- **Longevity**: Provides reliable recovery against Ground-type attackers
- **Sandstorm teams**: Excellent on sand teams where Ground moves are common

### Competitive Usage Notes
- **Tier placement**: Extremely valuable ability due to Ground's offensive prevalence
- **Team support**: Allows safe Earthquake usage by teammates
- **Wallbreaker check**: Can wall many Ground-type wallbreakers
- **Hazard immunity**: Doesn't protect against Spikes/Stealth Rock
- **Versatile defensive tool**: Works against both physical and special Ground attacks

### Counters and Limitations
- **Non-Ground coverage**: Vulnerable to all other attacking types
- **Mold Breaker**: Neutralizing Gas, Mold Breaker, and similar bypass the ability
- **Heal Block**: Prevents the healing aspect while still negating damage
- **Status moves**: Doesn't provide status immunity
- **Max HP users**: Less valuable healing on high HP Pokemon

### Synergies
- **Earthquake teammates**: Can use Earthquake without friendly fire
- **Sand teams**: Common Ground move usage makes ability valuable
- **Pivot strategies**: Safe switching on predicted Ground moves
- **Leftovers/recovery**: Stacks with other healing for extreme longevity
- **Assault Vest**: Can run offensive sets while maintaining defensive utility

### Pokemon That Learn Earth Eater
Earth Eater is typically found on:
- Ground-type Pokemon as a defensive option
- Bulky Pokemon that appreciate the immunity and healing
- Pokemon designed to counter Ground-type threats
- Rock/Steel types vulnerable to Ground coverage

### Version History
- Custom ability in Elite Redux
- Similar to existing absorption abilities (Water Absorb, Volt Absorb)
- Designed to provide Ground-type immunity with healing benefit
- Part of the expanded ability system in Elite Redux

### Ability Comparison
- **Water/Volt/Fire Absorb**: Same healing mechanism, different types
- **Levitate**: Provides Ground immunity but no healing
- **Flash Fire**: Boosts Fire moves instead of healing
- **Sap Sipper**: Grass absorption with Attack boost instead of healing
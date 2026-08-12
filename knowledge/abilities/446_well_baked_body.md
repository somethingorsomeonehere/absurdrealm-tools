---
id: 446
name: Well Baked Body
status: reviewed
character_count: 107
---

# Well Baked Body - Ability ID 446

## In-Game Description
"Boosts Defense sharply instead of being hit by Fire-type moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Well Baked Body grants immunity to Fire-type moves and boosts Defense by 2 stages when hit by Fire attacks. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Well Baked Body is a Fire-type absorption ability that provides complete immunity to Fire-type moves while granting a sharp Defense boost (+2 stages) when targeted by Fire attacks. This ability completely negates the Fire-type move, preventing any damage, status effects, or secondary effects.

### Activation Conditions
- **Move type requirement**: Only Fire-type moves trigger the ability
- **Attack targeting**: Must be directly targeted by the Fire-type move
- **Stat boost**: Always boosts Defense by exactly 2 stages (+50% defense)
- **Damage negation**: Completely prevents the Fire-type move from dealing damage
- **No redirection**: Unlike some absorption abilities, does not redirect Fire moves to the user

### Technical Implementation
```c
constexpr Ability WellBakedBody = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_FIRE);
        *statId = STAT_DEF;
        return ABSORB_RESULT_STAT;
    },
    .breakable = TRUE,
    .absorbUp2 = TRUE,
};
```

### Key Technical Details
- **absorbUp2 flag**: This special flag makes the ability boost stats by 2 stages instead of 1
- **STAT_DEF target**: Always boosts Defense, never other stats
- **ABSORB_RESULT_STAT**: Returns stat boost result type
- **breakable = TRUE**: Can be suppressed by Mold Breaker effects
- **No redirection**: Does not redirect Fire moves like Lightning Rod or Storm Drain

### Important Interactions
- **Complete immunity**: Fire moves deal 0 damage and have no effect
- **Status immunity**: Fire moves with status effects (like Will-O-Wisp) are completely blocked
- **Secondary effects**: Fire moves with secondary effects (like Flamethrower's burn chance) are negated
- **Multi-hit moves**: Each hit of a multi-hit Fire move is absorbed separately, but only one stat boost occurs
- **Ability suppression**: Can be bypassed by Mold Breaker, Teravolt, and Turboblaze
- **Stat cap**: Defense boosts are subject to the +6 stat stage maximum

### Strategic Applications
- **Fire immunity**: Complete protection against Fire-type attacks
- **Defensive setup**: Builds defensive bulk while being attacked
- **Pivot utility**: Safe switch-in against Fire-type moves
- **Wall building**: Allows defensive Pokemon to become increasingly bulky
- **Team support**: Can absorb Fire moves intended for teammates in doubles

### Stat Boost Mechanics
- **+2 stages**: Equivalent to a "sharp" increase, boosting Defense by 50%
- **Stack potential**: Multiple Fire attacks can stack up to +6 Defense maximum
- **Immediate effect**: Stat boost applies immediately when hit
- **Persistent**: Stat boosts remain until the Pokemon switches out or uses moves like Haze

### Common Usage Patterns
- **Defensive walls**: Pokemon that want to tank physical attacks
- **Setup sweepers**: Pokemon that can use the Defense boost to set up other moves
- **Fire-type counters**: Dedicated answers to Fire-type attackers
- **Pivot points**: Safe switching options against Fire teams

### Counters and Limitations
- **Non-Fire attacks**: Vulnerable to all other move types
- **Mold Breaker effects**: Can be bypassed by ability-ignoring effects
- **Special attacks**: Only boosts Defense, not Special Defense
- **Stat reset**: Defense boosts lost on switching out
- **Taunt**: Cannot use setup moves if taunted after absorbing Fire moves

### Synergies
- **Body Press**: Increased Defense directly boosts Body Press damage
- **Stamina**: Can stack with Stamina for massive defensive bulk
- **Curse**: Can use Curse to further boost Defense and Attack
- **Rest**: High Defense allows for safe Rest usage
- **Stored Power**: Defense boosts increase Stored Power's damage

### Comparison to Similar Abilities
- **Flash Fire**: Well Baked Body gives stat boosts instead of Fire move power
- **Water Absorb**: Provides stat boost instead of HP restoration
- **Sap Sipper**: Similar mechanic but for Grass moves and Attack boost
- **Justified**: Similar mechanic but for Dark moves and Attack boost

### Competitive Usage Notes
- **Tier placement**: Excellent ability for defensive and setup roles
- **Team synergy**: Pairs well with offensive teammates who appreciate Fire immunity
- **Meta positioning**: Strong against Fire-heavy teams and sun teams
- **Role compression**: Provides both defensive utility and setup potential

### Version History
- **Elite Redux exclusive**: Custom ability not found in mainline games
- **Unique mechanics**: One of only two abilities with absorbUp2 flag
- **Balanced design**: Provides strong defensive utility without being overpowered

### Pokemon That Learn This Ability
Well Baked Body is a custom Elite Redux ability that can be found on select Pokemon, typically those with defensive stats or thematic connections to baking/cooking. The ability is designed to provide a unique defensive option for handling Fire-type attacks while building momentum.
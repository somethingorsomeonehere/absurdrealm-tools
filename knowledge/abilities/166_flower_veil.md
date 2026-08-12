---
id: 166
name: Flower Veil
status: reviewed
character_count: 99
---

# Flower Veil - Ability ID 166

## In-Game Description
"Protects Grass-type allies from status and stat drops."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all status conditions and stat reductions for Grass-type allies. Includes self-stat drops.

## Detailed Mechanical Explanation

Flower Veil is a protective ability that shields Grass-type allies from harmful status conditions and stat reductions. This ability was introduced in Generation VI and provides comprehensive battlefield protection for Grass-type teammates.

### Status Protection
- Prevents ALL status conditions (poison, burn, paralysis, sleep, freeze, confusion) from affecting Grass-type allies
- Works against both direct status moves and secondary status effects from damaging moves
- Applies through `onStatusImmune` callback in the battle engine

### Stat Reduction Protection  
- Blocks ALL stat decreases to Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, and Evasion
- Protects against moves like Intimidate, stat-lowering moves, and ability-based stat drops
- Handled through `IsFlowerVeilProtected()` function in battle script commands
- Displays "surrounded itself with a veil of petals!" message when activated

### Application Rules
- **Target:** Only affects Grass-type Pokemon on the same side as the ability user
- **Self-Protection:** Does NOT protect the user unless they are also Grass-type
- **Breakable:** Can be bypassed by Mold Breaker and similar abilities
- **Activation:** Works passively - no turn activation required

## Implementation Details

### Code Location
- **Primary Definition:** `src/abilities.cc` lines 1840-1848 (`FlowerVeil` struct)
- **Status Immunity:** Uses `onStatusImmune` callback with `APPLY_ON_ALLY` flag
- **Stat Protection:** Handled in `src/battle_script_commands.c` via `IsFlowerVeilProtected()`
- **Battle Message:** "surrounded itself with a veil of petals!" in `battle_message.c`

### Ability Structure
```cpp
constexpr Ability FlowerVeil = {
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_STATUS1)
        CHECK(IS_BATTLER_OF_TYPE(target, TYPE_GRASS))
        return TRUE;
    },
    .onStatusImmuneFor = APPLY_ON_ALLY,
    .breakable = TRUE,
};
```

## Pokemon That Learn This Ability

### Regular Ability
- **Sunflora** - Primary ability option alongside Grassy Surge and Chlorophyll

### Innate Ability
- **Bellossom** - Has Flower Veil as one of multiple innate abilities

## Competitive Analysis

### Strengths
1. **Comprehensive Protection:** Covers both status and stat reduction immunity
2. **Team Support:** Excellent for protecting Grass-type teammates in doubles
3. **Consistent Activation:** Works passively without setup requirements
4. **Wide Coverage:** Protects against many common battle strategies

### Weaknesses
1. **Type Restriction:** Only protects Grass-type Pokemon
2. **Breakable:** Countered by Mold Breaker abilities
3. **No Self-Protection:** Doesn't help non-Grass-type users
4. **Situational:** Less valuable in singles or non-Grass teams

### Strategic Use
- **Doubles Support:** Ideal for protecting valuable Grass-type attackers
- **Status Immunity:** Counters common status strategies like Spore or Will-O-Wisp
- **Anti-Intimidate:** Protects physical Grass attackers from Attack drops
- **Team Synergy:** Works well with powerful but fragile Grass-type sweepers

## Related Abilities
- **Aroma Veil:** Protects team from move restriction (Taunt, Encore, etc.)
- **Sweet Veil:** Prevents sleep status for entire team
- **Jungle's Guard:** Custom ability that combines Flower Veil with Leaf Guard effects

## Battle Messages
- **Activation:** "{B_DEF_NAME_WITH_PREFIX} surrounded itself with a veil of petals!"
- **Context:** Displayed when stat reduction or status condition is blocked

## Version History
- **Generation VI:** Introduced as signature ability of Florges line
- **Elite Redux:** Enhanced with comprehensive stat reduction immunity
- **Current:** Functions as both status and stat protection for Grass allies

## Notes
- The ability checks for `TYPE_GRASS` using `IS_BATTLER_OF_TYPE()` macro
- Status immunity uses the standard `CHECK_STATUS1` flag system
- Stat protection integrates with the broader stat modification system
- Battle scripts handle both the immunity check and message display
- Works in both singles and doubles, but most effective in team formats
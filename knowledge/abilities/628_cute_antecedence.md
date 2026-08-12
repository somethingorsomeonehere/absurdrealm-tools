---
id: 628
name: Cute Antecedence
status: reviewed
character_count: 55
---

# Cute Antecedence - Ability ID 628

## In-Game Description
"At full HP, gives +1 priority to its Fairy-type moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Grants +1 priority to Fairy-type moves when at full HP.

## Detailed Mechanical Explanation

**Name**: Pretty Privilege (in-game display name)
**Internal Name**: ABILITY_CUTE_ANTECEDENCE
**Type**: Priority manipulation ability

## Implementation Details

### Code Implementation
```cpp
constexpr Ability CuteAntecedence = {
    .onPriority = GALE_WINGS_CLONE(TYPE_FAIRY),
};
```

The ability uses the `GALE_WINGS_CLONE` macro with `TYPE_FAIRY`, which translates to:
```cpp
+[](ON_PRIORITY) -> int {
    CHECK(GetTypeBeforeUsingMove(move, battler) == TYPE_FAIRY)
    CHECK(BATTLER_MAX_HP(battler))
    return 1;
}
```

### Mechanics
1. **HP Requirement**: Must be at full HP (100% health)
2. **Type Check**: Only affects Fairy-type moves
3. **Priority Boost**: Adds +1 to move priority
4. **Move Type Detection**: Uses `GetTypeBeforeUsingMove()` to account for type-changing effects

## Strategic Applications

### Offensive Usage
- Enables priority Moonblast, Dazzling Gleam, and other powerful Fairy moves
- Particularly potent on fast sweepers who can maintain full HP
- Synergizes with setup moves that don't cause damage

### Defensive Considerations
- HP threshold makes it vulnerable to entry hazards, residual damage
- Weather damage, status conditions, and recoil nullify the effect
- Priority Fairy moves can revenge kill or prevent setup

## Pokemon with This Ability
Based on the code analysis, this ability appears on:
- Species with multi-ability sets including this as a third option
- Likely appears on Fairy-type or Fairy-themed Pokemon

## Comparison to Similar Abilities
- **Gale Wings**: Same mechanic but for Flying-type moves
- **Flaming Soul**: Fire-type equivalent 
- **Frozen Soul**: Ice-type equivalent
- **Volt Rush**: Electric-type equivalent


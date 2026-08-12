---
id: 42
name: Magnet Pull
status: reviewed
character_count: 258
---

# Magnet Pull - Ability ID 42

## In-Game Description
"Traps opposing Steel-types. Ghosts aren't affected."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents Steel-type Pokemon from switching out while the user is present. Ghost-types are immune to this effect. Pokemon holding Shed Shell or using a pivot move such as Flip Turn can escape. Activates during the next turn if the user switches in mid battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MAGNET PULL** is a trapping ability that prevents Steel-type opposing Pokemon from switching out of battle.

### Activation Mechanics:
- **Trigger**: Passive effect while the Pokemon is on the field
- **Target**: Steel-type opponents only
- **Check Function**: `IS_BATTLER_OF_TYPE(switchingBattler, TYPE_STEEL)`
- **No Message**: Unlike Arena Trap, Magnet Pull doesn't display a message when trapping

### Trapping Rules:
1. **Steel-Type Check**: Only Steel-type Pokemon are trapped
2. **Ghost Immunity**: Ghost-type Pokemon cannot be trapped by any trapping ability
3. **Shed Shell Override**: Pokemon holding Shed Shell can always switch out
4. **Switching Prevention**: Prevents normal switching via Switch command or Run away

### Interactions and Exceptions:
- **Move-Based Switching**: Does NOT prevent U-turn, Volt Switch, Flip Turn, Teleport, or Baton Pass
- **Fainting**: Does not prevent switching when the trapped Pokemon faints
- **Dual Types**: Affects any Pokemon with Steel as one of its types (Steel/Flying, Steel/Psychic, etc.)
- **Type Changes**: If a Steel-type loses its Steel typing (via Burn Up, etc.), it can switch freely

### Ghost-Type Immunity:
The game's trap system has built-in Ghost-type immunity:
```c
if (IS_BATTLER_OF_TYPE(battlerId, TYPE_GHOST)) return 0;
```
This means Ghost-types ignore ALL trapping abilities, not just specific ones.

### Technical Implementation:
```c
constexpr Ability MagnetPull = {
    .onTrap = +[](ABILITY_ON_TRAP) -> int { 
        return IS_BATTLER_OF_TYPE(switchingBattler, TYPE_STEEL); 
    },
};
```

The trap check occurs in `IsAbilityPreventingEscape()` in battle_util.c, which:
1. First checks for Shed Shell (allows escape)
2. Then checks if the switching Pokemon is Ghost-type (allows escape)
3. Finally iterates through opponents checking their trapping abilities

### Competitive Applications:
- **Steel Trapping**: Ideal for trapping defensive Steel-types like Skarmory, Forretress, or Magnezone
- **Pursuit Trapping**: Historically paired with Pursuit to eliminate Steel-types that resist common attacks
- **Hazard Control**: Prevents Steel-type hazard removers from switching out after using Rapid Spin/Defog
- **Type Coverage**: Complements team members that struggle against Steel-types

### Counterplay:
- **Ghost Types**: Completely immune to the trapping effect
- **Shed Shell**: Any Steel-type can hold this item to escape
- **Switching Moves**: U-turn, Volt Switch, and Baton Pass still work
- **Knock Off**: Removing Choice items from trapped Steel-types can reduce their threat

### Version History:
- Gen 3: Introduced as Steel-type trapping ability
- Elite Redux: Functions identically to original implementation
- No changes from base game mechanics
---
id: 144
name: Regenerator
status: reviewed
character_count: 86
---

# Regenerator - Ability ID 144

## In-Game Description
"Heals 1/3 of max HP upon switching out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Restores 33% of maximum HP when switching out. This heal is not blocked by Heal Block.

## Detailed Mechanical Explanation
*For Discord/reference use*

**REGENERATOR** is a passive healing ability that activates upon switching out of battle.

### Activation Mechanics:
- **Trigger**: When the Pokemon exits battle (onExit hook)
- **Requirements**: Pokemon must be alive (not KO'd) and below maximum HP
- **Healing Amount**: Exactly 33% of maximum HP (1/3)
- **Script**: Uses `tryhealpercenthealth BS_ATTACKER, 33` for consistent healing calculation

### Switch Scenarios:
1. **Voluntary Switch**: Player manually switches Pokemon - healing triggers
2. **Forced Switch (Moves)**: Roar, Whirlwind, Dragon Tail, Circle Throw - healing triggers
3. **Forced Switch (Items)**: Red Card activation - healing triggers
4. **Pivot Moves**: U-turn, Volt Switch, Flip Turn, Teleport - healing triggers
5. **KO'd/Fainted**: No healing occurs (blocked by `IsBattlerAlive` check)
6. **Full HP**: No healing occurs (blocked by `BATTLER_MAX_HP` check)

### Interaction Rules:
- **Entry Hazards**: Regenerator heals first, then hazards damage on switch-in to new Pokemon
- **Status Conditions**: Healing occurs regardless of poison, burn, or other status
- **Pursuit**: If hit by Pursuit while switching, healing still occurs if Pokemon survives
- **Natural Recovery**: Some Pokemon have this combo ability (Natural Cure + Regenerator)

### Technical Implementation:
```c
constexpr Ability Regenerator = {
    .onExit = +[](ON_EXIT) -> int {
        CHECK(IsBattlerAlive(battler))
        CHECK_NOT(BATTLER_MAX_HP(battler))
        BattleScriptCall(BattleScript_RegeneratorExits);
        return FALSE;
    },
};
```

### Competitive Applications:
- **Defensive Pivoting**: Essential for bulky Pokemon that switch frequently
- **Stall Teams**: Provides consistent healing without items or moves
- **Pivot Strategies**: Combines excellently with U-turn/Volt Switch for safe switches
- **Hazard Management**: Helps offset entry hazard damage accumulation
- **Longevity**: Extends battle presence without requiring recovery moves

### Common Users:
- Slowpoke line (Natural regenerative abilities)
- Ho-Oh (Legendary phoenix regeneration)
- Various defensive Pokemon as innate abilities

### Strategic Notes:
- **AI Value**: Rated 8/10 in AI switching calculations
- **Timing**: Healing occurs immediately upon exit, before any entry effects
- **Stacking**: Cannot stack with itself, but combines with other healing sources
- **Prediction**: Forces opponents to consider immediate KO vs. allowing healing

### Version History:
- Gen 5: Introduced as 1/3 HP healing on switch-out
- Elite Redux: Maintains standard 33% healing rate, expanded to more Pokemon as innate abilities
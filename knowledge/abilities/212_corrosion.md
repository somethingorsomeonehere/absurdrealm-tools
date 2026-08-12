---
id: 212
name: Corrosion
status: reviewed
character_count: 134
---

# Corrosion - Ability ID 212

## In-Game Description
"Poison is super effective vs Steel. Can poison any type."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Poison-type moves become super effective against Steel-type Pokemon. Additionally, this Pokemon can inflict poison status on any type.

## Detailed Mechanical Explanation
*For Discord/reference use*

Corrosion provides two distinct mechanical effects that break traditional poison immunity rules:

### Type Effectiveness Modification
- **Core Mechanic**: Poison-type moves deal super effective (2x) damage to Steel-type Pokemon
- **Normal Interaction**: Steel resists Poison (0.5x damage)
- **With Corrosion**: Steel takes super effective damage from Poison (2x damage)
- **Implementation**: Uses `onTypeEffectiveness` hook to modify damage multiplier from 0.5x to 2.0x

```cpp
.onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
    CHECK(moveType == TYPE_POISON)
    CHECK(defType == TYPE_STEEL)
    *mod = UQ_4_12(2.0);
    return TRUE;
},
```

### Poison Status Bypass
- **Core Mechanic**: Can poison any Pokemon regardless of type
- **Affected Types**: Steel-type and Poison-type Pokemon (normally immune)
- **Status Types**: Works for both regular poison and bad poison
- **Implementation**: Uses `onCanStatusType` hook to override type immunity

```cpp
.onCanStatusType = +[](ABILITY_ON_CAN_STATUS_TYPE) -> int {
    CHECK(status & CHECK_POISON)
    return TRUE;
},
```

### Activation Conditions
1. **Type Effectiveness**: Activates when using Poison-type moves against Steel-type targets
2. **Status Infliction**: Activates when attempting to poison any target via moves, abilities, or items

### Affected Moves
**Poison-type offensive moves** (for type effectiveness):
- Sludge Bomb, Poison Jab, Gunk Shot, Sludge Wave, etc.
- All direct damage Poison-type moves gain super effectiveness vs Steel

**Poison-inflicting moves** (for status bypass):
- Toxic, Poison Gas, Poison Powder, Toxic Spikes
- Cross Poison, Poison Jab (secondary effect)
- Any move with poison chance secondary effects

### Strategic Implications
- **Steel Counter**: Transforms Steel-types from walls into vulnerable targets
- **Status Spreader**: Enables reliable poison status against traditional immunities
- **Stall Breaker**: Bypasses passive Steel-type walls and Poison-type tanks
- **Toxic Spikes Enhancement**: Makes entry hazard more universally threatening

### Interactions with Other Abilities
- **Overrides**: Type immunities (Steel/Poison to poison status)
- **Bypasses**: Natural Cure, Immunity, Poison Heal (for initial infliction)
- **Stacks With**: Poison Touch, Effect Spore (for additional poison chances)
- **Blocked By**: Magic Guard (prevents poison damage), Substitute (blocks status)

### Common Users
- **Salandit/Salazzle**: Primary users with fire/poison typing
- **Various Elite Redux Pokemon**: Multiple species have access as regular or innate ability
- **Grimer Line**: Some forms have access to this ability

### Competitive Usage
- **Role**: Wallbreaker and status spreader
- **Synergy**: Pairs well with Toxic Spikes setters and poison-type attackers
- **Threats**: Steel-type walls, Poison-type tanks, defensive cores
- **Teammates**: Benefits from entry hazard support and paralysis support

### Counters and Limitations
- **Magic Guard**: Prevents poison damage (but not initial status)
- **Substitute**: Blocks status moves entirely
- **Taunt**: Prevents non-damaging poison moves
- **Clerics**: Heal Bell, Aromatherapy remove poison status
- **Guts/Poison Heal**: Turn poison into advantage

### Damage Calculations
**Example vs Steel-type**:
- Base: Poison move vs Steel = 0.5x damage
- With Corrosion: Poison move vs Steel = 2.0x damage
- Net change: 4x damage increase

**Poison Status**:
- Regular poison: 1/8 max HP per turn
- Bad poison: Increasing damage (1/16, 2/16, 3/16, etc.)

### Version History
- **Elite Redux**: Enhanced implementation with comprehensive poison immunity bypass
- **Original**: Standard Corrosion from mainline games
- **Modifications**: Integrated with Elite Redux's expanded ability system and multi-ability framework
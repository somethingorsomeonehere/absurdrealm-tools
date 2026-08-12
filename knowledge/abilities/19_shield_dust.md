---
id: 19
name: Shield Dust
status: reviewed
character_count: 218
---

# Shield Dust - Ability ID 19

## In-Game Description
"Immune to added move effects, hazards, and powder moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Blocks all secondary effects from damaging moves. Grants immunity to entry hazards. Blocks all powder moves including Sleep Powder, Stun Spore, Poison Powder, Spore, Cotton Spore, Rage Powder, Powder, and Magic Powder.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shield Dust has been massively buffed in Elite Redux, providing three distinct types of protection:

```c
constexpr Ability ShieldDust = {
    .breakable = TRUE,
    .powderImmune = TRUE,
};
```

### 1. Secondary Effect Immunity

Implemented in `battle_script_commands.c` (line 2241), Shield Dust prevents ALL secondary effects from damaging moves:

**Blocked Effects Include**:
- Status conditions: Burn, paralysis, poison, freeze, sleep
- Stat drops: Attack, Defense, Speed, etc. reductions
- Flinching: From moves like Iron Head, Rock Slide
- Confusion: From moves like Water Pulse, Dynamic Punch

**Key Details**:
- Only blocks SECONDARY effects (30% burn chance on Scald)
- Does NOT block PRIMARY effects (Will-O-Wisp still burns)
- Uses `IsPreventableSecondaryEffect()` function
- Works alongside Covert Cloak item

### 2. Entry Hazard Immunity

Implemented in `battle_util.c` (`IsBattlerAffectedByHazards()` at line 8306):

**Complete Immunity To**:
- Stealth Rock
- Spikes (all layers)
- Toxic Spikes
- Sticky Web

**Mechanics**:
- Functions like built-in Heavy-Duty Boots
- Prevents all hazard damage on switch-in
- Does NOT clear hazards, just ignores them

### 3. Powder Move Immunity

Via the `powderImmune = TRUE` flag:

**Blocks All Powder Moves**:
- Sleep Powder
- Stun Spore  
- Poison Powder
- Spore
- Rage Powder
- Cotton Spore
- Magic Powder
- Any move with powder properties

**Implementation**:
- Checked by `IsPowderImmune()` in `battle_util.c` (line 3006)
- Powder moves fail completely against Shield Dust users

### Ability Properties
- **breakable = TRUE**: Can be suppressed by Mold Breaker
- All three immunities are suppressed when ability is broken

### Strategic Implications

**Defensive Profile**:
- Safe switches into hazard-heavy fields
- Immune to status powder strategies
- Protection from RNG secondary effects
- Reliable defensive consistency

**Team Value**:
- Less reliance on Defog/Rapid Spin
- Counters hazard stacking strategies
- Shuts down powder sleep leads
- Reduces battle RNG

### Key Code Locations
- **Ability Definition**: `src/abilities.cc` (line 522)
- **Secondary Effects**: `src/battle_script_commands.c` (line 2241)
- **Hazard Immunity**: `src/battle_util.c` (line 8306)
- **Powder Immunity**: `src/battle_util.c` (line 3006)

### Pokemon with Shield Dust
Typically found on Bug-type Pokemon and those with protective scales or dusty coatings. The expanded immunities make it valuable on many defensive and support Pokemon.

### Competitive Usage Notes

**Advantages**:
- Eliminates three major battle hazards in one ability slot
- Perfect for leads and pivots
- Counters RNG-heavy strategies
- Enables safer setup

**Limitations**:
- No offensive benefits
- Vulnerable to Mold Breaker
- Primary effects still work
- Doesn't prevent direct damage

### Counters
- Mold Breaker bypasses all immunities
- Direct status moves (Thunder Wave, Will-O-Wisp)
- Primary effect moves work normally
- Raw offensive pressure

### Synergies
- Pivot Pokemon benefit from hazard immunity
- Setup sweepers appreciate RNG protection
- Defensive cores value consistent switches
- Teams weak to hazards gain flexibility

### Comparison to Similar Effects
- **Heavy-Duty Boots**: Only blocks hazards
- **Covert Cloak**: Only blocks secondary effects
- **Safety Goggles**: Only blocks powder/weather
- **Shield Dust**: Combines all three protections

### Version History
Elite Redux transformed Shield Dust:
- **Original**: Only blocked secondary effects
- **Elite Redux**: Added hazard immunity + powder immunity

This makes Shield Dust one of the most comprehensive defensive abilities in the game, providing unparalleled protection against common battle mechanics.
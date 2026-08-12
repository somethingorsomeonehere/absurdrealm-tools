---
id: 516
name: Monster Mash
status: reviewed
character_count: 159
---

# Monster Mash - Ability ID 516

## In-Game Description
"Casts Trick-or-Treat on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Casts Trick-or-Treat on entry, adding Ghost type to the target. They do not benefit from the effects of fog. The effect persists until the target switches out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Monster Mash automatically casts Trick-or-Treat when the user enters battle, targeting the opposing Pokemon. This ability uses the `UseEntryMove` function with `MOVE_TRICK_OR_TREAT` and 0 power.

**Implementation:**
```c
constexpr Ability MonsterMash = {
    .onEntry = +[](ON_ENTRY) -> int { return UseEntryMove(battler, ability, MOVE_TRICK_OR_TREAT, 0); },
};
```

### How Trick-or-Treat Works
Trick-or-Treat is a Status move with the following properties:
- **Effect**: EFFECT_THIRD_TYPE
- **Type**: Ghost
- **Accuracy**: 100
- **PP**: 20
- **Target**: Selected opposing Pokemon
- **Flags**: Protect-affected, Mirror Move-affected

When successful, Trick-or-Treat:
1. Adds Ghost as a third type to the target
2. Sets the `trickOrTreat` flag in the target's volatile struct
3. The effect remains until the target switches out

### Fog Weather Interaction (Critical)
This is the most important tactical aspect of Monster Mash. In Fog weather:

**Normal Ghost-types in Fog:**
```c
// From battle_util.c
if (IS_BATTLER_OF_TYPE(battlerDef, TYPE_GHOST) && 
    IsBattlerWeatherAffected(battlerDef, WEATHER_FOG_ANY) && 
    !gVolatileStructs[battlerDef].trickOrTreat)
    MUL_MODIFIER(&modifier, .8);
```
- Ghost-types in Fog receive a 0.8x multiplier to physical damage taken (20% reduction)
- This makes them effectively immune to physical attacks

**After Trick-or-Treat:**
- The `trickOrTreat` flag is set to TRUE
- The condition `!gVolatileStructs[battlerDef].trickOrTreat` becomes FALSE
- The Ghost-type no longer receives the 0.8x damage reduction in Fog
- They take full damage from physical attacks

This creates a unique strategic niche where Monster Mash can neutralize Ghost-types' Fog weather immunity.

### Activation Conditions
- Triggers immediately upon switching in
- Does not trigger if the user is already on the field
- Can fail if:
  - The target is already Ghost-type (naturally, not from Trick-or-Treat)
  - The target is protected by Protect/Detect
  - The target has already been affected by Trick-or-Treat

### Type Interaction Changes
After Trick-or-Treat adds Ghost type:
- Target gains Ghost STAB if using Ghost moves
- Target becomes weak to Ghost and Dark moves
- Target becomes immune to Normal and Fighting moves (unless they have Scrappy or similar)
- Target becomes immune to trapping moves/abilities
- In Fog: Target LOSES Ghost-type physical damage immunity

### Strategic Implications
1. **Fog Counter**: Primary use is removing Ghost-types' physical immunity in Fog
2. **Type Manipulation**: Can give opponents unwanted Ghost weaknesses
3. **Entry Hazard**: Automatic effect on switch-in provides immediate pressure
4. **Defensive Liability**: Can make non-Ghost types vulnerable to Ghost/Dark coverage

### Example Scenarios
- **Vs Ghost in Fog**: Phanfernal switches in against Gengar in Fog. Monster Mash applies Trick-or-Treat, removing Gengar's physical damage immunity. Now physical attackers can hit Gengar for full damage.
- **Vs Non-Ghost**: Phanfernal switches in against Garchomp. Trick-or-Treat adds Ghost type, making Garchomp weak to Ghost/Dark but immune to Fighting coverage.

### Common Users
- **Phanfernal**: Fire/Grass type with Monster Mash as an innate ability
- **Crabonination**: Has Monster Mash as one of its innate abilities

### Competitive Usage Notes
- Best used in Fog-heavy teams to counter opposing Ghost-types
- Pairs well with physical attackers who struggle against Ghosts in Fog
- Can disrupt defensive Ghost-types relying on Fog immunity
- Less useful outside of Fog weather
- Consider the risk of giving opponents Ghost STAB

### Counters
- Magic Bounce reflects Trick-or-Treat back
- Switching out removes the effect
- Natural Ghost-types are unaffected
- Protect/Detect blocks the initial cast
- Taunt prevents manual Trick-or-Treat but not Monster Mash

### Synergies
- **Fog setters**: Maximize the ability's anti-Ghost utility
- **Physical attackers**: Benefit from removing Ghost immunity
- **Pursuit users**: Trap Ghost-types trying to switch out
- **Ghost/Dark coverage**: Exploit the new weakness
- **Arena Trap/Shadow Tag**: Prevent switching to maintain the effect
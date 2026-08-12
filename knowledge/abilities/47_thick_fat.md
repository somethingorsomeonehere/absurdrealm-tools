---
id: 47
name: Thick Fat
status: reviewed
character_count: 115
---

# Thick Fat - Ability ID 47

## In-Game Description
"Takes 1/2 damage from Fire-type and Ice-type attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage received from Fire and Ice-type moves by 50%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Thick Fat provides a **0.5x damage multiplier** (50% damage reduction) against all Fire-type and Ice-type attacks. This is implemented as a defensive multiplier that directly modifies incoming damage.

### Activation Conditions
- Triggers automatically against **any Fire-type move**
- Triggers automatically against **any Ice-type move**  
- Works against both physical and special attacks
- Functions regardless of the attacking Pokemon's ability or move properties

### Technical Implementation
```cpp
constexpr Ability ThickFat = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_FIRE || moveType == TYPE_ICE) RESISTANCE(.5);
        },
    .breakable = TRUE,
};
```

The `RESISTANCE(.5)` macro applies both resistance and modifier values, effectively halving damage from Fire and Ice attacks.

### Affected Move Types
**Fire-type moves** (examples):
- Flamethrower
- Fire Blast
- Heat Wave
- Eruption
- Sacred Fire

**Ice-type moves** (examples):
- Ice Beam
- Blizzard
- Ice Punch
- Icicle Crash
- Freeze-Dry

### Damage Calculation Examples
**Without Thick Fat:**
- 100 BP Fire move to 100% damage
- 120 BP Ice move to 100% damage

**With Thick Fat:**
- 100 BP Fire move to 50% damage
- 120 BP Ice move to 50% damage

### Interactions with Other Mechanics

**Can be bypassed by:**
- Mold Breaker and similar abilities (marked as `breakable = TRUE`)
- Abilities that ignore defensive abilities

**Does NOT affect:**
- Status effects from Fire/Ice moves (burn, frostbite still apply)
- Indirect damage (poison, weather, etc.)
- Multi-type moves (only reduces damage if the move is Fire or Ice type)

**Stacks with:**
- Type resistances (0.5x Fire resistance + 0.5x Thick Fat = 0.25x total)
- Other damage reduction abilities and items
- Weather effects that reduce Fire/Ice damage

### Strategic Implications

**Defensive Value:**
- Exceptional switch-in potential against Fire and Ice attackers
- Enables tanking powerful special attacks like Blizzard and Fire Blast
- Particularly valuable in formats with common Fire/Ice coverage moves

**Team Synergy:**
- Excellent partner for Pokemon weak to Fire or Ice
- Provides reliable pivot points against temperature-based attackers
- Enables aggressive positioning against common offensive types

### Common Users in Elite Redux
**Notable Pokemon with Thick Fat** (as innate ability):
- **Bulbasaur line** - Defensive Grass/Poison starter with Fire resistance
- **Swinub/Piloswine line** - Ice/Ground types that resist their own weakness
- **Azumarill line** - Water types with enhanced Fire resistance
- **Snorlax** - Defensive Normal type with broad resistances
- **Walrein line** - Water/Ice types with Fire resistance
- **Camerupt line** - Fire/Ground types with enhanced Ice resistance

### Competitive Usage Notes

**Tier Impact:**
- High value in tiers with prevalent Fire/Ice attackers
- Enables defensive builds against specific offensive cores
- Creates opportunities for prediction and switching

**Common Strategies:**
- Pivot switching against Fire/Ice special attackers
- Defensive stallbreaking against Fire/Ice-based cores
- Supporting teammates weak to these common attacking types

### Counters and Limitations

**Direct Counters:**
- Mold Breaker abilities bypass the resistance entirely
- Pokemon with non-Fire/Ice coverage moves
- Status-based strategies (unaffected by damage reduction)

**Indirect Limitations:**
- No protection against other common types (Electric, Grass, etc.)
- Status effects from Fire/Ice moves still apply at full strength
- Multi-hit moves still accumulate damage despite reduction

### Version History
- Classic implementation maintained in Elite Redux
- Enhanced with Elite Redux's expanded type chart and ability interactions
- Functions identically to traditional Pokemon games but with broader utility due to expanded movesets

### Synergistic Abilities
**Works well with:**
- **Water Veil** - Prevents burn from Fire moves while resisting damage
- **Oblivious** - Status immunity pairs with damage resistance
- **Regenerator** - Enhanced longevity with damage reduction
- **Ice Body** - Ice resistance + healing from hail creates defensive synergy

**Competitive Combinations:**
- Thick Fat + defensive typing creates exceptional bulk
- Pairs well with recovery moves for sustained tanking
- Enhances the effectiveness of defensive stat spreads
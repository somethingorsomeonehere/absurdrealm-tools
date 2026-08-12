---
id: 830
name: Temporal Rupture
status: reviewed
character_count: 212
---

# Temporal Rupture - Ability ID 830

## In-Game Description
Roar of Time is altered drastically.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Roar of Time becomes a 100 BP +0 Priority attack that changes the target's Ability to Slow Start (halves attacking stats and speed for 5 turns). It also no longer forces Pokemon out or is considered a sound move.

## Detailed Mechanical Explanation

Temporal Rupture is an innate ability possessed by legendary Dragon/Steel-type Pokemon. This ability fundamentally alters how Roar of Time functions. In Elite Redux, Roar of Time already differs from the main series by forcing switches at -6 priority instead of requiring recharge. Temporal Rupture further modifies this move's behavior, though the exact changes remain mysterious and powerful.

### Technical Details

#### Code Implementation
Located in `src/abilities.cc`:
```cpp
constexpr Ability TemporalRupture = {
    .breakable = TRUE,
};
```

#### Properties
- **Breakable**: Yes (can be bypassed by Mold Breaker)
- **Innate**: Yes (cannot be changed or suppressed normally)

#### Known Pokemon
This ability is found on legendary Dragon/Steel-type Pokemon with the following innate ability set:
- Temporal Rupture (changeable slot)
- Primal Armor (innate)
- Impenetrable (innate)  
- Power Core (innate)

### Notes
- The specific mechanical changes to Roar of Time are not explicitly defined in the code
- Roar of Time in Elite Redux already has EFFECT_HIT_SWITCH_TARGET with -6 priority
- The "drastic alteration" likely involves additional effects beyond the base switch-forcing mechanic
- This is one of the signature abilities of the most powerful legendary Pokemon in Elite Redux
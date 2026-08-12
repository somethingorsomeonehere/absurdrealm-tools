---
id: 248
name: Ice Face
status: reviewed
character_count: 220
---

# Ice Face - Ability ID 248

## In-Game Description
"Protects once against an attack. Restores protection under hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ice Face transforms Eiscue into its Noice Face form after taking an attack, negating damage once. While in Noice form, if hail is set or if the user is swapped in, revert to Ice Face form. Cannot be copied or suppressed. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Ice Face is a disguise-type ability exclusive to Eiscue that provides one-time physical damage negation with weather-based restoration:

**Core Mechanics:**
- Functions as a form-changing disguise ability similar to Mimikyu's Disguise
- When Eiscue (Ice Face form) takes a physical attack, it transforms to Eiscue Noice Face form
- The first physical attack that would hit is completely negated (0 damage)
- Special attacks bypass Ice Face entirely and deal normal damage
- Multi-hit moves only break the disguise on the first hit; subsequent hits deal full damage

**Restoration Mechanics:**
- Under any hail weather (temporary or permanent), Eiscue automatically restores its Ice Face form
- Restoration occurs during weather checks (entry, weather change, end of turn)
- Must be in Noice Face form to restore - cannot restore if already in Ice Face form
- Works with natural hail, Snow Warning, and other hail-inducing effects

**Battle Interactions:**
- Ability is breakable (can be suppressed by Mold Breaker effects)
- Unsuppressable (cannot be changed by abilities like Skill Swap)
- Provides hail immunity (takes no hail damage)
- Form changes trigger the standard form change battle script and animations
- Transformation cannot occur if the Pokemon is already transformed by other means

**Strategic Applications:**
- Guaranteed survival of one physical attack per hail cycle
- Excellent synergy with hail teams and Snow Warning setters
- Forces opponents to use special attacks or set non-hail weather
- Can be used repeatedly if hail weather is maintained
- Particularly effective against physical setup sweepers

**Technical Implementation:**
- Uses the onDisguise callback to determine form change (SPECIES_EISCUE to SPECIES_EISCUE_NOICE_FACE)
- onEntry and onWeather callbacks handle form restoration under hail
- Requires specific species check (only works on Eiscue species)
- Cannot function if Pokemon is transformed by other effects (Transform move, etc.)

This ability represents a unique defensive tool that combines one-time damage negation with weather dependency, making it a cornerstone of defensive hail strategies while requiring careful weather management for maximum effectiveness.
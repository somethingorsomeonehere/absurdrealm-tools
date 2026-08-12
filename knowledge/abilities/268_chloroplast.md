---
id: 268
name: Chloroplast
status: reviewed
character_count: 268
---

# Chloroplast - Ability ID 268

## In-Game Description
"Weather Ball, Solar Beam/Blade, Growth act as if used in sun."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Weather Ball doubles power and becomes Fire-type. Solar moves charge instantly. Growth boosts Attack and Special Attack by 2 stages. Moonlight, Morning Sun, and Synthesis recover 2/3 of your max HP. Grass and Water Pledge creates a sea of fire or rainbow respectively. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics

Chloroplast makes specific moves behave as if they were used during harsh sunlight conditions, regardless of the actual weather:

1. **Weather Ball Enhancement**
   - Base power doubles from 50 to 100
   - Type changes to Fire-type (same as during actual sun)
   - Works even in no weather, rain, hail, or sandstorm

2. **Solar Beam/Solar Blade Instant Charging**
   - Removes the charging turn requirement
   - Moves execute immediately in one turn
   - Same effect as using these moves in actual harsh sunlight

3. **Growth Double Boost**
   - Attack stat increases by +2 stages instead of +1
   - Special Attack stat increases by +2 stages instead of +1
   - Provides the enhanced sun effect without requiring actual sun weather

### Implementation Details

**Battle Script Integration:**
- Growth script checks for Chloroplast ability alongside actual sun weather
- Both Attack and Special Attack get the doubled boost when Chloroplast is present
- Solar moves skip charging phase when Chloroplast is active
- Weather Ball power calculation treats Chloroplast as sun condition

**Code References:**
- Defined in `abilities.cc` as `constexpr Ability Chloroplast = { .chloroplast = TRUE };`
- Used in battle scripts via `jumpifability BS_ATTACKER, ABILITY_CHLOROPLAST`
- Weather Ball implementation in `battle_util.c` checks `HasChloroplast(battlerAtk)`

### Strategic Applications

**Immediate Benefits:**
- Enables immediate Solar Beam/Solar Blade usage without setup
- Provides powerful Weather Ball without weather dependency
- Makes Growth significantly more valuable as a setup move

**Team Synergy:**
- Works well with Pokemon that learn Solar moves naturally
- Benefits Grass-types that commonly have Growth in their movepool
- Provides fire coverage through Weather Ball without actual Fire typing

**Weather Independence:**
- Functions regardless of current weather conditions
- Cannot be negated by opposing weather effects
- Provides consistent solar-based benefits

### Comparison to Related Abilities

**vs. Chlorophyll:** 
- Chlorophyll provides Speed boost in sun
- Chloroplast provides move effects without weather dependency

**vs. Solar Power:**
- Solar Power boosts Special Attack but causes HP loss in sun
- Chloroplast enhances specific moves without stat changes or HP costs

**vs. Drought:**
- Drought creates actual sunlight weather
- Chloroplast simulates sun effects for specific moves only

### Notable Interactions

- **Big Leaves ability:** Also provides Chloroplast effect alongside other benefits
- **Solar Flare ability:** Another ability that grants chloroplast functionality
- **Pledge moves:** Water Pledge and Grass Pledge also benefit from Chloroplast effects
- **Healing moves:** Morning Sun, Synthesis, and Moonlight get enhanced healing with Chloroplast

This ability effectively grants "selective sunlight" for specific moves, making it highly valuable for Pokemon that rely on solar-based strategies without requiring weather setup or risking weather wars with opponents.
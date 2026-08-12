---
id: 17
name: Immunity
status: reviewed
character_count: 185
---

# Immunity - Ability ID 17

## In-Game Description
"Cannot be poisoned. Halves damage taken from Poison moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents poisoning. Reduces all Poison-type damage by 50%. Multiplicative with other sources of damage reduction. If poisoned when gaining this ability, the poison is immediately cured. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Immunity provides dual protection against Poison through status immunity and damage reduction. Implementation in `src/abilities.cc`:

```cpp
constexpr Ability Immunity = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_POISON) RESISTANCE(.5);
        },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_POISON)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Key Features

1. **Poison Status Immunity**: 
   - The `onStatusImmune` callback prevents all forms of poisoning
   - Checks for `CHECK_POISON` status flag and returns TRUE to block it
   - Includes regular poison and badly poisoned (Toxic) status

2. **Poison Damage Reduction**:
   - The `onDefensiveMultiplier` callback reduces Poison-type damage by 50%
   - `RESISTANCE(.5)` multiplies incoming Poison damage by 0.5
   - Stacks with other resistances (e.g., Steel-type's natural Poison resistance)

3. **Ability Properties**:
   - **breakable = TRUE**: Can be suppressed by Mold Breaker and similar abilities
   - **removesStatusOnImmunity = TRUE**: If already poisoned when gaining Immunity, the poison status is immediately removed

### Sources of Poison Blocked
- **Status Moves**: Toxic, Poison Gas, Poison Powder
- **Secondary Effects**: Sludge Bomb's 30% poison chance, etc.
- **Abilities**: Poison Point, Effect Spore's poison chance
- **Items**: Toxic Orb, Poison Barb (status effect only)
- **Other**: Toxic Spikes hazards

### Damage Calculation Examples
Against a neutral Poison-type move:
- Normal: 1.0x damage
- With Immunity: 0.5x damage

Against a super effective Poison-type move (e.g., vs Grass):
- Normal: 2.0x damage  
- With Immunity: 1.0x damage

Stacking with Steel-type (0.5x from type + 0.5x from ability):
- Steel with Immunity: 0.25x damage from Poison moves

### Pokemon with Immunity
Some examples include:
- **Frillish** (Water/Ghost): Has Immunity as a changeable ability option
  - Other options: Low Visibility, Clear Body
- Various other Pokemon have it as either changeable or innate ability

### Strategic Implications

**Defensive Value**:
- Complete protection against Toxic stalling
- Significant bulk against Poison attackers
- Can switch into Toxic Spikes safely
- Removes existing poison when gained (e.g., via Skill Swap)

**Team Support**:
- Excellent on defensive pivots
- Valuable for stall teams vulnerable to Toxic
- Good on setup sweepers that fear poison chip damage

### Interactions

1. **With Mold Breaker**:
   - Both poison immunity and damage reduction are suppressed
   - Pokemon with Mold Breaker can poison and deal full damage

2. **With Corrosion**:
   - Corrosion does NOT bypass Immunity
   - The status immunity still applies

3. **With Type Changes**:
   - If user becomes Poison-type, still takes 0.5x from Poison moves
   - If user becomes Steel-type, stacks to 0.25x damage

### Competitive Usage Notes
- Excellent on bulky Water-types that fear Toxic
- Valuable on walls and defensive pivots
- Provides unique defensive profile against Poison coverage
- Can enable safer setup against Poison-types

### Counters
- Mold Breaker users bypass both effects
- Other status conditions work normally
- Non-Poison offensive moves unaffected
- Ability suppression (Gastro Acid, etc.)

### Synergies
- Pokemon weak to Poison appreciate the damage reduction
- Defensive cores benefit from Toxic immunity
- Setup sweepers can boost without poison chip
- Pairs well with Heal Bell/Aromatherapy support

### Version History
Elite Redux enhanced Immunity significantly:
- **Original games**: Only prevented poison status
- **Elite Redux**: Added 50% Poison-type damage reduction

This makes Immunity a comprehensive anti-Poison ability providing both offensive and defensive benefits.
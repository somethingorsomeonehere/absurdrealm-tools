---
id: 805
name: Sepia Lens
status: reviewed
character_count: 258
---

# Sepia Lens - Ability ID 805

## In-Game Description
"Tinted Lens + Sand Guard."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Combines Tinted Lens and Sand Guard. Doubles damage when attacking with not very effective moves. During sandstorm, blocks priority moves from opponents and halves damage from special attacks. Also grants immunity to sandstorm damage like other Ground-types.

## Detailed Mechanical Explanation
*For Discord/reference use*

Sepia Lens is a combination ability that merges the effects of Tinted Lens and Sand Guard into a single powerful ability.

### Core Mechanics

**Tinted Lens Component:**
- When the user attacks with a move that is "not very effective" (0.5x effectiveness or less), the damage is doubled
- This effectively makes not very effective moves deal neutral (1x) damage
- Applies to all offensive moves, both physical and special
- Calculated during the offensive multiplier phase

**Sand Guard Component:**
- **Priority Move Immunity**: During sandstorm weather, the user is immune to priority moves from opposing Pokemon
- **Special Defense Boost**: During sandstorm, incoming special attacks deal half damage (0.5x multiplier)
- **Sandstorm Immunity**: The user takes no damage from sandstorm weather

### Activation Conditions

**Tinted Lens Effect:**
- Activates when using any move with type effectiveness <= 0.5x
- Works against any target regardless of weather conditions
- No restrictions on move type or category

**Sand Guard Effects:**
- Only active during sandstorm weather (temporary or permanent)
- Priority immunity applies to moves from opposing team only
- Special defense boost affects all special moves from any attacker during sandstorm
- Sandstorm immunity is always active regardless of weather

### Technical Implementation

```cpp
constexpr Ability SepiaLens = {
    .onImmune = SandGuard.onImmune,                    // Priority move immunity in sandstorm
    .onOffensiveMultiplier = TintedLens.onOffensiveMultiplier,  // Double damage on not very effective
    .onDefensiveMultiplier = SandGuard.onDefensiveMultiplier,   // Halve special damage in sandstorm
    .breakable = TRUE,       // Can be suppressed by Mold Breaker effects
    .sandImmune = TRUE,      // Immune to sandstorm damage
};
```

**Tinted Lens Logic:**
```cpp
if (typeEffectivenessMultiplier <= UQ_4_12(.5)) RESISTANCE(2);
```
- `UQ_4_12(.5)` = 0.5x effectiveness threshold
- `RESISTANCE(2)` = Apply 2x multiplier to both resistance and damage modifier

**Sand Guard Logic:**
```cpp
// Priority move immunity (delegates to Queenly Majesty behavior)
if (IsBattlerWeatherAffected(battler, WEATHER_SANDSTORM_ANY) && 
    GetMovePriority(attacker, move, battler) > 0) {
    Block priority move;
}

// Special defense boost
if (IS_MOVE_SPECIAL(move) && IsBattlerWeatherAffected(attacker, WEATHER_SANDSTORM_ANY)) {
    MUL(.5);  // Half damage from special moves
}
```

### Affected Moves and Interactions

**Tinted Lens Component:**
- All offensive moves with <=0.5x type effectiveness
- Common scenarios: Fire moves vs Water, Electric vs Ground, Fighting vs Ghost, etc.
- Does NOT affect moves that are already super effective or neutral

**Sand Guard Priority Immunity:**
- Quick Attack, Bullet Punch, Aqua Jet, Ice Shard
- Sucker Punch, Shadow Sneak, Mach Punch
- Vacuum Wave, Water Shuriken
- Prankster-boosted status moves
- Does NOT block: Fake Out, Extreme Speed (higher priority), or same-team moves

### Strategic Implications

**Offensive Benefits:**
- Eliminates traditional type disadvantages when attacking
- Allows for surprising coverage against resistant types
- Particularly valuable on mixed attackers or Pokemon with diverse movepools

**Defensive Benefits:**
- Strong special bulk during sandstorm conditions
- Complete immunity to priority revenge killing in sandstorm
- Natural sandstorm immunity allows safe pivoting

**Team Synergy:**
- Excellent on sandstorm teams with Tyranitar, Hippowdon, or Excadrill
- Pairs well with Pokemon that can set up sandstorm reliably
- Provides both offensive pressure and defensive utility

### Common Users

**Primary User:**
- **Mega Flygon**: The signature user with 125/130/125 offensive stats
  - Flying/Ground typing benefits greatly from priority immunity
  - High speed and mixed attacking stats utilize both components well
  - Ground typing provides natural sandstorm synergy

### Competitive Usage Notes

**Strengths:**
- Versatile ability providing both offensive and defensive utility
- Eliminates common revenge killing strategies in sandstorm
- Makes traditionally bad matchups much more manageable
- No activation cost or setup required

**Limitations:**
- Sand Guard effects only active during sandstorm weather
- Breakable by Mold Breaker, Teravolt, and Turboblaze
- Tinted Lens doesn't help against already super effective moves
- Requires team support to maintain sandstorm for full effectiveness

### Counters

**Direct Counters:**
- Mold Breaker effects bypass both components entirely
- Cloud Nine/Air Lock removes weather, disabling Sand Guard
- Non-priority moves are unaffected by the immunity
- Physical attacks in sandstorm bypass the special defense boost

**Strategic Counters:**
- Hail or other weather conditions to override sandstorm
- Status moves and entry hazards for indirect damage
- Super effective moves that bypass Tinted Lens benefit
- High-power neutral moves that don't rely on type advantage

### Synergies

**Team Combinations:**
- Sand Stream setters (Tyranitar, Hippowdon)
- Other Ground-types that benefit from sandstorm
- Pokemon with powerful not very effective coverage moves
- Bulky support Pokemon that can maintain weather control

**Item Synergies:**
- Smooth Rock to extend sandstorm duration
- Life Orb to boost already-enhanced Tinted Lens damage
- Leftovers for added sustainability during extended sandstorm turns

### Version History

- **Elite Redux Implementation**: Combined ability featuring both Tinted Lens and Sand Guard effects
- **Balance Notes**: Breakable status prevents it from being completely overwhelming
- **Design Intent**: Provides Mega Flygon with unique defensive utility while maintaining offensive presence
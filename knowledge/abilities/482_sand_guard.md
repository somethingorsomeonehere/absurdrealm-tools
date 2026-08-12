---
id: 482
name: Sand Guard
status: reviewed
character_count: 148
---

# Sand Guard - Ability ID 482

## In-Game Description
"Blocks priority and reduces special damage by 1/2 in sand."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sand Guard blocks priority moves and reduces Special Attack damage by 50% during a sandstorm. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sand Guard is a dual-defensive ability that provides both priority move immunity and special damage reduction during sandstorm weather. The ability has two distinct effects that operate under different conditions.

### Priority Move Blocking
- **Weather requirement**: Sandstorm must be active to block priority moves
- **Effect**: Completely blocks all priority moves (priority > 0) from opponents
- **Range**: Protects both the user and allied Pokemon (onImmuneFor = APPLY_ON_ALLY)
- **Mechanism**: Uses the same priority blocking system as Queenly Majesty and Dazzling
- **Message**: Shows "Dazzling" protection message when blocking

### Special Damage Reduction
- **Weather requirement**: Sandstorm must be active for damage reduction
- **Attacker condition**: The attacking Pokemon must be affected by sandstorm
- **Move type**: Only applies to special attacks (IS_MOVE_SPECIAL)
- **Damage reduction**: Multiplies incoming special damage by 0.5 (50% reduction)
- **Target**: Only applies to the Sand Guard user, not allies

### Technical Implementation
```c
constexpr Ability SandGuard = {
    .onImmune = +[](ON_IMMUNE) -> int {
        CHECK(IsBattlerWeatherAffected(battler, WEATHER_SANDSTORM_ANY));
        return QueenlyMajesty.onImmune(DELEGATE_IMMUNE);
    },
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_SPECIAL(move) && IsBattlerWeatherAffected(attacker, WEATHER_SANDSTORM_ANY)) MUL(.5);
        },
    .breakable = TRUE,
    .sandImmune = TRUE,
};
```

### Weather Conditions
Sand Guard activates under any sandstorm weather:
- **Regular sandstorm** (from Sandstorm move)
- **Sand Stream** (from Tyranitar, Hippowdon, etc.)
- **Sand Spit** (triggered by contact moves)
- **WEATHER_SANDSTORM_ANY** covers all sandstorm variants

### Important Interactions
- **Sandstorm immunity**: User is immune to sandstorm damage (sandImmune = TRUE)
- **Ability suppression**: Both effects are disabled by abilities like Mold Breaker (breakable = TRUE)
- **Priority bypass**: Abilities like Triage or Prankster still have their priority moves blocked
- **Physical moves**: No damage reduction against physical attacks
- **Status moves**: Priority status moves are still blocked even if they don't deal damage

### Priority Move Examples Blocked
- Aqua Jet, Bullet Punch, Mach Punch (physical priority)
- Vacuum Wave, Water Shuriken (special priority)
- Prankster-boosted status moves
- Quick Attack, Extremespeed
- Fake Out, Sucker Punch

### Special Damage Reduction Examples
- **Blocked**: Hydro Pump from Pokemon in sandstorm (50% damage)
- **Not blocked**: Earthquake from Pokemon in sandstorm (physical move)
- **Not blocked**: Surf from Pokemon not in sandstorm (clear weather)
- **Blocked**: Thunderbolt from Garchomp with Sand Stream active

### Strategic Implications
- **Sandstorm team synergy**: Essential for sand-based teams
- **Priority immunity**: Protects against common priority revenge killers
- **Special tank**: Excellent special bulk in sandstorm conditions
- **Weather dependent**: Completely ineffective without sandstorm
- **Dual protection**: Covers both offensive pressure and priority threats

### Competitive Usage
- **Sand core**: Pairs well with Sand Stream setters like Tyranitar/Hippowdon
- **Defensive pivot**: Can switch into special attackers and priority users
- **Weather support**: Maintains sand for team while providing utility
- **Anti-priority**: Shuts down common priority-based strategies
- **Tank role**: Functions as special wall in sandstorm teams

### Common Users
Sand Guard is a custom Elite Redux ability, so usage depends on which Pokemon receive it:
- Likely Ground/Rock/Steel types that fit sandstorm teams
- Pokemon that naturally benefit from sandstorm conditions
- Defensive Pokemon that can utilize both protective effects

### Synergies
- **Sand Stream/Sand Spit**: Essential weather setters
- **Sand Rush/Sand Force**: Other sand-based abilities
- **Rock-type moves**: Boosted accuracy in sandstorm
- **Leftovers/Rocky Helmet**: Defensive item synergy
- **Sand Veil**: Evasion boost stacking with damage reduction

### Counters
- **Weather override**: Changing weather disables both effects completely
- **Cloud Nine/Air Lock**: Negates sandstorm effects
- **Physical attackers**: Bypass special damage reduction
- **Mold Breaker family**: Ignore the ability entirely
- **Weather-immune moves**: Some moves ignore weather conditions

### Comparison to Similar Abilities
- **Queenly Majesty**: Same priority blocking but no damage reduction
- **Ice Scales**: Same special damage reduction but no priority blocking
- **Fur Coat**: Physical damage reduction instead of special
- **Dazzling**: Priority blocking for ally but no personal benefits

### Elite Redux Context
In Elite Redux's 4-ability system, Sand Guard can function as either:
- **Changeable ability**: Switchable based on team needs
- **Innate ability**: Always active for consistent sand team support
- The dual nature makes it valuable in both roles
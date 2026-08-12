---
id: 744
name: Sand Bender
status: reviewed
character_count: 178
---

# Sand Bender - Ability ID 744

## In-Game Description
"Sand Stream + Sand Force."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Summons sandstorm on entry, lasting 8 turns (12 with Smooth Stone). Boosts the Pokemon's highest attacking stat by 50% during sandstorm. Also grants immunity to sandstorm damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sand Bender is a powerful combination ability that merges the effects of two complementary sand-based abilities:
1. **Sand Stream component**: Automatically summons sandstorm weather upon entry
2. **Sand Force component**: Provides 1.5x boost to highest attacking stat during sandstorm
3. **Sand immunity**: User takes no damage from sandstorm weather

### Activation Conditions
- **Entry effect**: Sandstorm is summoned immediately when the Pokemon switches in
- **Stat boost**: Active whenever sandstorm weather is present (regardless of source)
- **Duration**: Sandstorm lasts 8 turns in Elite Redux (extended from vanilla 5 turns)
- **Stat selection**: Boosts whichever attacking stat (Attack or Special Attack) is higher

### Technical Implementation
```cpp
constexpr Ability SandBender = {
    .onEntry = SandStream.onEntry,      // Summons sandstorm on entry
    .onStat = SandForce.onStat,         // 1.5x boost to highest attacking stat
    .sandImmune = TRUE,                 // Immune to sandstorm damage
};
```

The ability directly inherits the Sand Stream entry effect and Sand Force stat boost, while adding sandstorm immunity.

### Sand Stream Component Details
- **Weather change**: Sets weather to WEATHER_SANDSTORM
- **Priority**: Can override existing weather (except Primal weather)
- **Duration**: 8 turns in Elite Redux
- **Announcement**: Triggers "A sandstorm kicked up!" message
- **Primal interaction**: Blocked by Primal weather effects

### Sand Force Component Details
- **Stat boost**: 1.5x multiplier to highest attacking stat
- **Stat selection**: Compares base Attack vs Special Attack stats
- **Weather requirement**: Any sandstorm weather (natural or ability-induced)
- **Timing**: Applied during stat calculation phase
- **Stacking**: Multiplicative with other stat modifiers

### Weather Interactions
- **Compatible weather**: Only sandstorm weather activates Sand Force
- **Weather override**: Other weather abilities can replace the sandstorm
- **Primal weather**: Desolate Land/Primordial Sea block Sand Stream activation
- **Cloud Nine/Air Lock**: Suppresses both weather setting and stat boost
- **Weather Rock**: Heat Rock extends sandstorm to 13 turns when held

### Strategic Implications
- **Dual role**: Functions as both weather setter and weather abuser
- **Instant activation**: No setup required - both effects work on switch-in
- **Self-sufficient**: Creates own optimal conditions
- **Offensive focus**: Emphasizes immediate damage output over utility
- **Team synergy**: Benefits sand team while providing sand support

### Common Users
Sand Bender is typically found on:
- Ground-type offensive Pokemon
- Rock-type sweepers and wallbreakers
- Steel-type attackers immune to sandstorm
- Pokemon with high Attack or Special Attack stats
- Sand team cores that need both setting and sweeping capability

### Competitive Applications
- **Lead position**: Excellent for setting weather from battle start
- **Revenge killer**: Switch in to set sand and immediately threaten
- **Wallbreaker**: 1.5x boost helps break through defensive cores
- **Late-game cleaner**: Sand boost enables end-game sweeps
- **Pivot role**: Can set sand then switch to dedicated sweeper

### Synergies
- **Sand Rush teammates**: Speed boost complements Sand Bender's power
- **Rock/Ground/Steel types**: Team members immune to sand damage
- **Smooth Rock**: Extends sandstorm duration to 13 turns
- **Life Orb/Choice items**: Stacks with Sand Force boost for massive power
- **Entry hazards**: Sandstorm chip damage combos with hazard damage

### Counters and Weaknesses
- **Weather override**: Drought/Drizzle/Snow Warning remove sandstorm
- **Primal weather**: Completely blocks Sand Stream activation
- **Ability suppression**: Mold Breaker/Neutralizing Gas disable both effects
- **Cloud Nine/Air Lock**: Negates weather-based stat boost
- **Mixed attackers**: Only boosts one attacking stat, not both
- **Weather-immune targets**: Some Pokemon resist sandstorm effects

### Important Interactions
- **Stat boost timing**: Applied before damage calculation each turn
- **Weather immunity**: User never takes sandstorm damage
- **Ability order**: Sand Stream activates first, then Sand Force applies
- **Switch mechanics**: Both effects reset on switching out
- **Form changes**: Stat boost recalculates if stats change

### Version History
- Elite Redux exclusive combination ability
- Combines two established Generation III-V abilities
- Benefits from Elite Redux's 8-turn weather duration
- Designed for offensive sand team archetypes
- Part of the expanded ability roster for competitive diversity

### Comparison to Component Abilities
- **vs Sand Stream**: Adds immediate offensive pressure
- **vs Sand Force**: Adds weather setting reliability
- **vs Sandstorm immunity**: Provides both offense and protection
- **Power level**: Significantly stronger than either component alone
- **Versatility**: More self-sufficient than single-effect abilities
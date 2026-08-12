---
id: 93
name: Hydration
status: reviewed
character_count: 64
---

# Hydration - Ability ID 93

## In-Game Description
Cures own status at the end of every turn in rain.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

During rain, cures all status conditions at the end of the turn.

## Detailed Mechanical Explanation

### In-Game Effects

### Primary Effect
- At the end of each turn, if the Pokemon is affected by rain weather, it automatically cures any status condition
- Status conditions cured include:
  - Sleep
  - Poison (regular and toxic)
  - Burn
  - Freeze
  - Paralysis

### Activation Conditions
- Activates at the end of each turn (after all other turn-end effects)
- Requires rain weather to be active:
  - Regular Rain (from Rain Dance)
  - Heavy Rain (from Downpour move)
  - Primordial Sea (permanent rain from Primal Kyogre)
  - Primal Rain
- Does NOT activate if rain is blocked by abilities like Air Lock or Cloud Nine


## Strategic Applications

### Competitive Usage
- **Rain Team Core**: Essential ability for rain-based teams, providing status immunity
- **Status Absorber**: Can switch into status moves without fear during rain
- **Sleep Talk Synergy**: Can use Rest for recovery and wake up immediately in rain
- **Toxic Spikes Counter**: Removes poison upon switching in if rain is active at turn end

### Notable Interactions
- **Rest Synergy**: Can use Rest for full healing and wake up same turn in rain
- **Status Move Baiting**: Opponents may waste turns trying to status a Hydration user
- **Weather Wars**: Losing rain means losing status immunity, making weather control crucial
- **End Turn Timing**: Cures status after damage from poison/burn is taken

### Strengths
- Complete status immunity in rain
- No item slot needed (unlike Lum Berry)
- Reusable every turn
- Works on all major status conditions

### Weaknesses
- Completely dependent on rain weather
- Useless without rain active
- Vulnerable to weather changes
- Still takes status damage before cure

## Pokemon with This Ability
Common Hydration users include:
- Vaporeon (water-type synergy)
- Lapras (bulky water tank)
- Goodra (special tank)
- Phione (mythical water-type)
- Various other water-types

## Competitive Tips
1. **Weather Control**: Pair with reliable rain setters like Politoed or Pelipper
2. **Rest Strategy**: Use Rest as primary recovery move for instant full heals
3. **Status Bait**: Let opponents waste turns trying to status you
4. **Team Support**: Acts as team's status absorber during rain
5. **Backup Plans**: Have contingencies for when rain expires

## Developer Notes
- Implemented in `src/abilities.cc` at line 1185
- Uses `IsBattlerWeatherAffected` to check for rain conditions
- Calls `AbilityHealMonStatus` to cure all status conditions
- Simple but effective ability for weather-based strategies
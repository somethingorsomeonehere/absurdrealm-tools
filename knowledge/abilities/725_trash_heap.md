---
id: 725
name: Trash Heap
status: reviewed
character_count: 266
---

# Trash Heap - Ability ID 725

## In-Game Description
"Corrosion + Toxic Spill."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Poison-type moves become super effective against Steel-type Pokemon. Additionally, this Pokemon can inflict poison status on any type. Damages all non-Poison-type Pokemon by 1/8 HP each turn. Pokemon with Poison Heal recover instead. Disappears when the user leaves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Trash Heap is a combination ability that merges two powerful poison-based abilities: Corrosion and Toxic Spill. It provides both offensive type coverage and battlefield control through environmental hazards.

### Corrosion Component
- **Type effectiveness override**: Poison-type moves deal super effective (2x) damage to Steel-type Pokemon
- **Status bypass**: Can inflict poison status on any type, including Steel and Poison types
- **Universal poisoning**: Ignores type-based poison immunity

### Toxic Spill Component
- **Entry effect**: Upon switching in, creates toxic waste on the battlefield
- **End-of-turn damage**: All non-Poison type Pokemon take 1/8 of their max HP in damage each turn
- **Poison Heal interaction**: Pokemon with Poison Heal recover 1/8 HP instead of taking damage
- **Exit effect**: Toxic waste disappears when the ability holder switches out or faints
- **Monotype exception**: Does not activate during Poison-type monotype champion battles

### Technical Implementation
```c
constexpr Ability TrashHeap = {
    .onEntry = ToxicSpill.onEntry,           // Creates toxic waste field
    .onEndTurn = ToxicSpill.onEndTurn,       // Damages non-Poison types
    .onExit = ToxicSpill.onExit,             // Removes toxic waste
    .onTypeEffectiveness = Corrosion.onTypeEffectiveness,  // Super effective vs Steel
    .onCanStatusType = Corrosion.onCanStatusType,          // Universal poison status
};
```

### Activation Conditions
**Corrosion Effects:**
- Poison-type moves used by the ability holder
- Status moves that inflict poison

**Toxic Spill Effects:**
- Automatically activates on entry (except in Poison monotype battles)
- Damages all battlers at end of each turn
- Deactivates when ability holder leaves the field

### Important Interactions
- **Poison Heal synergy**: Turns damage into healing for Poison Heal users
- **Magic Guard protection**: Magic Guard prevents toxic waste damage
- **Type immunity**: Only affects non-Poison types with toxic waste
- **Steel-type coverage**: Makes Poison moves viable against Steel types
- **Status immunity bypass**: Can poison traditionally immune types like Steel and Poison

### Damage Calculation
- **Toxic waste damage**: 1/8 of target's maximum HP per turn
- **Poison Heal recovery**: 1/8 of maximum HP per turn (instead of damage)
- **Timing**: Occurs at end of turn along with other residual effects

### Strategic Implications
- **Field control**: Creates persistent battlefield hazard
- **Type coverage**: Expands Poison-type offensive options
- **Team synergy**: Benefits teams with Poison Heal users
- **Switching punishment**: Forces opponents to consider switch timing
- **Stall potential**: Provides passive damage for bulky strategies

### Counters
- **Type switching**: Switch to Poison-type Pokemon for immunity
- **Magic Guard**: Blocks toxic waste damage entirely
- **Rapid switching**: Minimize exposure to toxic waste
- **Poison Heal**: Turn the effect into a benefit
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable both components

### Synergies
- **Poison Heal teammates**: Benefit from toxic waste instead of taking damage
- **Poison-type moves**: Gain Steel-type coverage and universal status
- **Stall teams**: Provides passive damage for defensive strategies
- **Entry hazards**: Combines with Spikes/Toxic Spikes for multi-layered pressure
- **Status moves**: Can now poison any target regardless of type

### Common Users
- Bulky Poison-type Pokemon that can set up field control
- Mixed attackers that want both offensive and utility presence
- Pokemon on teams with multiple Poison Heal users
- Stall-oriented Poison types that benefit from passive damage

### Competitive Usage Notes
- Exceptional field control ability that pressures entire opposing teams
- The combination of offensive utility (Corrosion) and battlefield control (Toxic Spill) makes it highly versatile
- Particularly effective in longer battles where passive damage accumulates
- Requires careful team building to maximize Poison Heal synergies
- Can single-handedly change the pace and strategy of battles

### Version History
- Elite Redux exclusive combination ability
- Merges two existing abilities into a single powerful effect
- Part of the expanded ability system in Elite Redux

### Monotype Battle Behavior
- Does not activate Toxic Spill effects during Poison-type monotype champion battles
- Corrosion effects still function normally in monotype contexts
- This prevents the ability from being overpowered in specific battle formats
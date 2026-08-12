---
id: 709
name: Dream State
status: reviewed
character_count: 215
---

# Dream State - Ability ID 709

## In-Game Description
"Immune to critical hits. Takes 20% less damage from attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Incoming damage is reduced by 20% (x0.8), multiplicative with other damage reduction. Additionally, critical hits are blocked, functioning as regular hits and not activating on-crit effects like To The Bone's bleed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Dream State is a powerful defensive ability that provides two distinct protective effects: complete critical hit immunity and a flat 20% damage reduction on all incoming attacks. This dual nature makes it one of the strongest purely defensive abilities in the game.

### Implementation Details
Dream State uses the same implementation as Battle Armor with additional defensive properties:
```c
constexpr Ability DreamState = {
    .onDefensiveMultiplier = BattleArmor.onDefensiveMultiplier,  // 20% damage reduction
    .onCrit = BattleArmor.onCrit,                               // NEVER_CRIT
    .onCritFor = BattleArmor.onCritFor,                         // APPLY_ON_TARGET
    .breakable = TRUE,
};
```

### Critical Hit Immunity
- **Complete immunity**: Cannot be critically hit under any circumstances
- **All sources**: Blocks crits from moves, abilities, and held items
- **Crit rate modifiers**: Renders Focus Energy, Super Luck, Razor Claw, etc. useless
- **Stage-based crits**: Even +3 critical hit ratio moves cannot crit

### Damage Reduction
- **Flat 20% reduction**: All incoming damage is multiplied by 0.8
- **Universal application**: Works on physical, special, and typeless damage
- **Stacking**: Multiplicatively stacks with type resistances and other defensive modifiers
- **Calculation order**: Applied after type effectiveness but before other defensive modifiers

### Activation Conditions
- **Passive ability**: Always active when the Pokemon is on the field
- **No requirements**: Does not require specific weather, status, or field conditions
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze
- **Target application**: Both effects apply to the Pokemon with Dream State

### Damage Calculation Example
```
Base damage: 100
Type effectiveness: x0.5 (resisted) = 50
Dream State: x0.8 = 40 final damage
```

### Important Interactions
- **Multi-hit moves**: Each hit receives damage reduction
- **Recoil moves**: User still takes full recoil (not affected by target's Dream State)
- **Fixed damage**: Seismic Toss, Dragon Rage bypass the damage reduction
- **Status damage**: Burn, poison damage not reduced
- **Entry hazards**: Stealth Rock, Spikes damage not reduced
- **Confusion/recoil**: Self-inflicted damage not reduced

### Strategic Applications
- **Physical tank**: Excellent on bulky Pokemon that fear critical hits
- **Special tank**: Works equally well against special attackers
- **Anti-luck**: Completely nullifies critical hit luck in competitive play
- **Longevity**: 20% damage reduction significantly extends staying power
- **Setup sweeper protection**: Prevents crits from ruining setup attempts

### Synergies
- **Leftovers/Recovery**: Enhanced by improved longevity
- **Defensive items**: Stacks with Assault Vest, Eviolite, etc.
- **Type resistances**: Multiplicatively stacks for extreme damage reduction
- **Substitute**: Sub takes reduced damage, lasting longer
- **Rest**: Pairs well with recovery moves due to increased bulk

### Counters and Limitations
- **Mold Breaker family**: Completely bypasses both effects
- **Status conditions**: Doesn't prevent burn, poison, paralysis
- **Entry hazards**: Stealth Rock still does full damage
- **Fixed damage moves**: Seismic Toss, Dragon Rage, etc. ignore damage reduction
- **Indirect damage**: Weather, Leech Seed, etc. not reduced
- **Ability suppression**: Neutralizing Gas, Simple Beam disable it

### Competitive Usage
- **Tier placement**: Extremely valuable in competitive formats
- **Team role**: Defensive pivot and special wall
- **Meta impact**: Forces opponents to rely on consistent damage over luck
- **Prediction safe**: No timing or prediction required for activation
- **Versatile**: Works on any Pokemon regardless of typing or role

### Notable Users
Pokemon with Dream State as either their primary or innate ability:
- Often found on defensive/bulky Pokemon
- Particularly valuable on mixed walls
- Excellent on Pokemon with recovery moves
- Synergizes with defensive stat spreads

### Version History
- Elite Redux exclusive ability
- Part of the expanded ability roster
- Designed to provide consistent defensive utility
- Implements Battle Armor's proven mechanics with enhanced damage reduction

### Comparison to Similar Abilities
- **Battle Armor**: Same effects but typically on different Pokemon
- **Shell Armor**: Only critical hit immunity, no damage reduction
- **Filter/Solid Rock**: Only 25% reduction on super-effective moves
- **Multiscale**: Only works at full HP
- **Dream State advantage**: Combines best aspects with no conditions
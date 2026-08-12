---
id: 75
name: Shell Armor
status: reviewed
character_count: 215
---

# Shell Armor - Ability ID 75

## In-Game Description
"Immune to critical hits. Takes 20% less damage from attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Incoming damage is reduced by 20% (x0.8), multiplicative with other damage reduction. Additionally, critical hits are blocked, functioning as regular hits and not activating on-crit effects like To The Bone's bleed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shell Armor in Elite Redux is functionally identical to Battle Armor, providing two powerful defensive effects:

1. **Critical Hit Immunity**
   - Completely prevents critical hits from occurring against this Pokemon
   - This includes guaranteed critical hit moves like Frost Breath and Storm Throw
   - Also blocks critical hits from items like Scope Lens or moves like Focus Energy

2. **Damage Reduction (20%)**
   - All incoming damage is multiplied by 0.8 (80% of original damage)
   - Applies to both physical and special attacks
   - Stacks multiplicatively with other damage reduction effects
   - Applies after all other damage calculations

### Technical Implementation

Shell Armor shares the exact same mechanical implementation as Battle Armor:
- Uses the same onDefensiveMultiplier, onCrit, and onCritFor functions
- Both abilities are marked as breakable (can be suppressed by Mold Breaker)
- The only difference is the ability ID (75 vs 4)

```c
constexpr Ability ShellArmor = {
    .onDefensiveMultiplier = BattleArmor.onDefensiveMultiplier,
    .onCrit = BattleArmor.onCrit,
    .onCritFor = BattleArmor.onCritFor,
    .breakable = TRUE,
};
```

### Numerical Values/Percentages
- **Critical Hit Prevention**: 100% (absolute immunity)
- **Damage Reduction**: 20% (takes 80% of normal damage)
- **Effective HP Increase**: ~25% (1/0.8 = 1.25x effective bulk)

### Interactions with Other Abilities/Mechanics
- **Mold Breaker**: Can bypass Shell Armor since it's marked as breakable
- **Sniper**: Opponent's Sniper ability is useless against Shell Armor
- **Super Luck**: High crit-rate abilities are neutralized
- **Laser Focus**: The guaranteed critical hit is prevented
- **Other damage reduction**: Stacks multiplicatively (e.g., with Friend Guard)

### Shell Armor vs Battle Armor
These abilities are functionally identical in Elite Redux:
- **Same effects**: Critical hit immunity + 20% damage reduction
- **Same breakability**: Both can be suppressed by Mold Breaker
- **Same description**: Identical in-game text
- **Only difference**: Ability ID numbers (Shell Armor = 75, Battle Armor = 4)

### Strategic Implications
- Excellent on defensive Pokemon and tanks
- Particularly valuable on Pokemon with low Defense or Special Defense
- Removes the RNG element of critical hits in important battles
- Makes stat calculations more predictable for defensive plays

### Example Damage Calculations
For a move that would normally deal 100 damage:
- Normal hit: 100 x 0.8 = **80 damage**
- What would be a critical hit: 150 x 0.8 = **120 damage** to But crit is prevented, so still **80 damage**
- Effective bulk increase: A Pokemon with 400 HP effectively has 500 HP worth of bulk

### Common Users
Shell Armor is available on various Pokemon including:
- Water-type Pokemon with shells (Squirtle line, Shellder line)
- Defensive Rock and Steel-types
- Armored Pokemon like Shieldon, Bastiodon
- Various Pokemon as both changeable and innate abilities

### Competitive Usage Notes
- S-tier defensive ability combining two powerful effects
- Makes setup sweepers more reliable (no random crits to ruin setup)
- Excellent for stall teams and defensive pivots
- The 20% reduction is more impactful than it initially appears
- Particularly strong in Elite Redux where battles are longer

### Counters
- **Mold Breaker**: Completely bypasses Shell Armor's effects
- **Fixed damage moves**: Seismic Toss, Night Shade bypass the reduction
- **Status conditions**: Burn, Poison, etc. deal percentage-based damage
- **Stat-lowering moves**: Reduce the Pokemon's defenses
- **Super effective moves**: Still deal significant damage despite reduction
- **Knock Off**: Can remove items that further boost defense

### Synergies
- **Leftovers/Black Sludge**: Healing is more valuable with increased bulk
- **Defense/Sp.Def boosts**: Multiplicative stacking makes setup more rewarding
- **Weakness Policy**: Can survive super effective hits more reliably
- **Rest**: More turns of effective HP to heal back
- **Substitute**: Substitutes are harder to break

### Version History
- **Original Games**: Only prevented critical hits
- **Elite Redux**: Added 20% damage reduction, making it functionally identical to Battle Armor
- **Elite Redux**: Both Shell Armor and Battle Armor now share the same enhanced mechanics
---
id: 4
name: Battle Armor
status: reviewed
character_count: 215
---

# Battle Armor - Ability ID 4

## In-Game Description
"Immune to critical hits. Takes 20% less damage from attacks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Incoming damage is reduced by 20% (x0.8), multiplicative with other damage reduction. Additionally, critical hits are blocked, functioning as regular hits and not activating on-crit effects like To The Bone's bleed.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Battle Armor in Elite Redux has been significantly enhanced from its original implementation:

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

The ability is implemented with two key properties:
- Critical hit immunity (shared with Shell Armor)
- Flat 20% damage reduction modifier

The damage reduction is applied in the damage calculation formula after all other modifiers, effectively making the Pokemon take only 80% of the calculated damage.

### Numerical Values/Percentages
- **Critical Hit Prevention**: 100% (absolute immunity)
- **Damage Reduction**: 20% (takes 80% of normal damage)
- **Effective HP Increase**: ~25% (1/0.8 = 1.25x effective bulk)

### Interactions with Other Abilities/Mechanics
- **Mold Breaker**: Cannot bypass Battle Armor (it's not marked as breakable)
- **Sniper**: Opponent's Sniper ability is useless against Battle Armor
- **Super Luck**: High crit-rate abilities are neutralized
- **Laser Focus**: The guaranteed critical hit is prevented
- **Other damage reduction**: Stacks multiplicatively (e.g., with Friend Guard)

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
Battle Armor is available on various Pokemon including:
- Defensive Steel-types
- Armored Pokemon like Crustle, Escavalier
- Rock and Bug-type tanks
- Various Pokemon as either changeable or innate abilities

### Competitive Usage Notes
- S-tier defensive ability combining two powerful effects
- Makes setup sweepers more reliable (no random crits to ruin setup)
- Excellent for stall teams and defensive pivots
- The 20% reduction is more impactful than it initially appears
- Particularly strong in Elite Redux where battles are longer

### Counters
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
- **Elite Redux**: Added 20% damage reduction, making it a premier defensive ability
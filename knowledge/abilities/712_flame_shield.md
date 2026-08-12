---
id: 712
name: Flame Shield
status: reviewed
character_count: 106
---

# Flame Shield - Ability ID 712

## In-Game Description
"Takes 35% less damage from Super-effective moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Reduces damage from super-effective attacks by 35%. Multiplicative with other sources of damage reduction.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Flame Shield is a defensive ability that reduces incoming damage from super-effective moves. The ability provides significant damage reduction against type disadvantageous attacks, helping Pokemon survive otherwise lethal coverage moves.

### Activation Conditions
- **Type effectiveness requirement**: Move must have 2x or greater type effectiveness
- **Damage reduction**: Reduces damage by 35% (multiplies damage by 0.65)
- **Timing**: Applied during damage calculation phase
- **Move types affected**: All offensive moves that would be super-effective

### Technical Implementation
```c
// Flame Shield implementation in abilities.cc
constexpr Ability FlameShield = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (typeEffectivenessModifier >= UQ_4_12(2.0)) MUL(.65);
        },
    .breakable = TRUE,
};
```

### Important Interactions
- **Multiple effectiveness**: Works against 4x super-effective moves as well
- **STAB interaction**: Reduces damage from STAB super-effective moves
- **Critical hits**: Damage reduction applies after critical hit calculation
- **Multi-hit moves**: Each hit gets damage reduction if super-effective
- **Ability suppression**: Can be bypassed by Mold Breaker and similar abilities
- **Breakable**: This ability can be broken by certain effects

### Damage Calculation Order
1. Base damage calculated
2. Type effectiveness applied (2x, 4x, etc.)
3. Flame Shield reduction applied (x0.65)
4. Other defensive modifiers applied
5. Final damage dealt

### Strategic Implications
- **Coverage survival**: Helps survive super-effective coverage moves
- **Switch safety**: Provides more switching opportunities against coverage
- **Frail Pokemon support**: Especially valuable on glass cannon attackers
- **Fire-type synergy**: Helps Fire types survive Water/Rock/Ground attacks
- **Prediction reward**: Rewards staying in against expected super-effective moves

### Type-Specific Benefits
- **Fire types**: Survive Water, Ground, Rock attacks better
- **Grass types**: Better survival against Fire, Ice, Flying, Poison, Bug attacks
- **Electric types**: Survive Ground-type moves (if they somehow hit)
- **Flying types**: Better survival against Electric, Ice, Rock attacks

### Common Users
- Frail offensive Pokemon that need survival utility
- Pokemon with multiple common weaknesses
- Mixed attackers that need to stay in longer
- Pokemon in speed tiers where they need to survive one hit

### Competitive Usage Notes
- Excellent on frail sweepers that fear revenge killing
- Helps pivot Pokemon survive coverage on predicted switches
- Valuable in formats with high offensive power
- Can turn 2HKOs into 3HKOs against super-effective moves
- Pairs well with recovery moves for increased longevity

### Counters
- **Neutral effectiveness moves**: No damage reduction against neutral hits
- **Mold Breaker**: Ignores the ability entirely
- **Neutralizing Gas**: Suppresses the ability while active
- **Multi-hit moves**: Still dangerous even with reduction
- **Status moves**: Doesn't protect against status conditions
- **Entry hazards**: No protection from Stealth Rock, spikes, etc.

### Synergies
- **Recovery moves**: Extended longevity with Roost, Recover, etc.
- **Substitute**: Can set up behind reduced damage
- **Focus Sash**: Better guarantee of Sash activation survival
- **Leftovers/Life Orb**: More turns to benefit from items
- **Priority moves**: Survive to use priority revenge moves

### Similar Abilities
- **Filter**: Identical effect and implementation
- **Solid Rock**: Same damage reduction for super-effective moves
- **Prism Armor**: Similar concept but different reduction rate in some games

### Version History
- Added in Elite Redux as ID 712
- Shares implementation with Filter ability
- Part of the defensive utility ability category
- Designed to help frail Pokemon survive in high-power metagames
---
id: 296
name: Lead Coat
status: reviewed
character_count: 159
---

# Lead Coat - Ability ID 296

## In-Game Description
"Takes 40% less from Phys. moves. This Pokemon's Speed is 0.9x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Lead Coat reduces physical damage by 40% but decreases Speed by 10%. Also triples the user's weight. The damage reduction is multiplicative with other sources.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Lead Coat is a defensive ability with both benefits and drawbacks that significantly alters a Pokemon's battle performance.

**Primary Effects:**
1. **Physical Damage Reduction**: Reduces all incoming physical move damage by 40% (multiplies by 0.6)
2. **Speed Reduction**: Reduces the Pokemon's Speed stat by 10% (multiplies by 0.9)
3. **Weight Multiplication**: Triples the Pokemon's weight for all weight-based calculations

### Technical Implementation
```cpp
constexpr Ability LeadCoat = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (IS_MOVE_PHYSICAL(move)) MUL(.6);
        },
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED) *stat *= .9;
        },
    .breakable = TRUE,
};
```

**Weight Calculation:**
```cpp
if (BATTLER_HAS_ABILITY(battlerId, ABILITY_LEAD_COAT)) weight *= 3;
```

### Activation Conditions
- **Physical Damage Reduction**: Activates on any physical move targeting the Pokemon
- **Speed Reduction**: Always active, applied during stat calculation
- **Weight Multiplication**: Always active, affects all weight-dependent calculations

### Affected Moves and Mechanics
**Weight-Based Moves Affected:**
- **Low Kick**: Damage increases based on target's weight
- **Grass Knot**: Damage increases based on target's weight  
- **Heat Crash**: Damage based on user's weight vs target's weight
- **Heavy Slam**: Damage based on user's weight vs target's weight

**Weight Damage Table for Low Kick/Grass Knot:**
- Normal weight ranges: 10kg (20 BP) to 200kg+ (120 BP)
- With Lead Coat: 3x weight means reaching maximum damage (120 BP) much easier

### Interactions with Other Abilities/Items
**Stacking with Weight Modifiers:**
- **Heavy Metal**: Both abilities stack (2x from Heavy Metal, then 3x from Lead Coat = 6x total weight)
- **Light Metal**: Light Metal halves weight first, then Lead Coat triples (0.5x to 1.5x total weight)
- **Float Stone**: Item halves weight after ability calculations (3x to 1.5x total weight)

**Speed Modification Interactions:**
- Stacks multiplicatively with other speed modifiers
- Nature modifiers applied before ability
- Choice Scarf: Speed becomes (base x 0.9 x 1.5) = 1.35x base speed
- Paralysis: Speed becomes (base x 0.9 x 0.25) = 0.225x base speed

### Strategic Implications
**Advantages:**
- Excellent physical bulk, taking only 60% damage from physical attacks
- Makes weight-based attacks more powerful when used by the Pokemon
- Synergizes well with slow, bulky Pokemon that don't rely on speed

**Disadvantages:**
- 10% speed reduction can be critical in speed ties
- Triple weight makes the Pokemon extremely vulnerable to Low Kick and Grass Knot
- Mold Breaker and similar abilities can bypass the physical damage reduction

### Damage Calculations
**Physical Attack Example:**
- 100 BP physical move vs 100 Def Pokemon
- Without Lead Coat: 100% damage
- With Lead Coat: 60% damage (40% reduction)

**Low Kick Against Lead Coat User:**
- Pokemon weighing 50kg normally to 150kg with Lead Coat
- Low Kick power: 80 BP (vs 60 BP without Lead Coat)
- Effectively makes the Pokemon much more vulnerable to weight-based attacks

### Common Users
Based on trainer battle data, Lead Coat is commonly found on:
- **Togedemaru**: Sturdy/Lead Coat/Impenetrable options
- **Skarmory**: Mirror Armor/Sturdy/Lead Coat options  
- **Bronzong**: Battle Armor/Lead Coat/Twisted Dimension options
- **Aggron**: Juggernaut/Heatproof/Iron Barbs with Lead Coat as innate ability
- **Steelix**: Various abilities with Lead Coat as innate
- **Metang**: Fatal Precision/Predator/Lead Coat options

### Competitive Usage Notes
**Optimal Usage:**
- Best on slow, physically defensive Pokemon
- Excellent for Trick Room teams where the speed reduction is beneficial
- Strong on Pokemon that can use weight-based attacks effectively

**Team Synergy:**
- Pairs well with Trick Room setters
- Benefits from teammates that can handle special attackers
- Works well with entry hazard support to pressure switch-ins

### Counters
**Direct Counters:**
- **Special Attackers**: Completely bypass the physical damage reduction
- **Mold Breaker**: Ignores the ability entirely
- **Weight-based moves**: Low Kick and Grass Knot become much more effective

**Indirect Counters:**
- **Status moves**: Burn reduces physical attack but doesn't trigger the ability
- **Multi-hit moves**: Each hit is reduced individually, but multiple hits can still break through
- **Critical hits**: Still reduced by 40% but can overcome the bulk

### Version History
Lead Coat is an Elite Redux custom ability, not present in official Pokemon games. It represents a defensive ability designed for tank Pokemon that want to sacrifice some speed for significant physical bulk, with the interesting trade-off of increased vulnerability to weight-based attacks.

The ability's design creates interesting strategic decisions - the physical bulk is significant, but the weight tripling can be exploited by opponents running Low Kick or Grass Knot, making team building and prediction crucial elements of using Lead Coat effectively.
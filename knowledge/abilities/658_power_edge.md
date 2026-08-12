---
id: 658
name: Power Edge
status: reviewed
character_count: 86
---

# Power Edge - Ability ID 658

## In-Game Description
"Keen Edge moves target Special Defense and get a 1.3x boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Keen Edge moves gain a 30% damage boost and target Special Defense instead of Defense.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Power Edge provides two key benefits to moves with the `FLAG_KEEN_EDGE_BOOST` flag:
1. **Damage Boost**: 1.3x (30%) damage multiplier, identical to Keen Edge
2. **Defense Targeting**: Forces slashing moves to target Special Defense instead of Defense

### Technical Implementation
```cpp
constexpr Ability PowerEdge = {
    .onOffensiveMultiplier = KeenEdge.onOffensiveMultiplier,
};
```

The ability inherits Keen Edge's damage multiplier and adds Special Defense targeting through the battle engine's stat calculation system.

### Activation Conditions
- Move must have the `keen_edge: true` flag in its definition
- Works on both physical and special slashing moves
- No additional requirements - effects are always active when using eligible moves

### Key Differences from Keen Edge
**Power Edge vs Keen Edge:**
- **Damage Boost**: Both provide identical 1.3x multiplier
- **Stat Targeting**: Power Edge forces Special Defense targeting, Keen Edge uses normal Defense
- **Strategic Focus**: Power Edge breaks special walls, Keen Edge pressures physical walls

### Complete List of Affected Moves
All moves that work with Keen Edge also work with Power Edge, but with Special Defense targeting:

**Classic Slashing Moves:**
- Slash - Always crits, targets Special Defense, 1.3x boost
- Night Slash - High crit ratio, targets Special Defense, 1.3x boost  
- Leaf Blade - High crit ratio, targets Special Defense, 1.3x boost
- Razor Leaf - Always crits, hits both foes, targets Special Defense, 1.3x boost
- Fury Cutter - Multi-hit with increasing power, targets Special Defense, 1.3x boost
- False Swipe - Can't KO, 50% bleed chance, targets Special Defense, 1.3x boost

**Specialized Cutting Moves:**
- Air Slash - 30% flinch chance, targets Special Defense, 1.3x boost
- Psycho Cut - Psychic blades, high crit ratio, targets Special Defense, 1.3x boost
- Cross Poison - Hits twice, high crit, 10% poison, targets Special Defense, 1.3x boost
- Sacred Sword - Ignores stat changes, targets Special Defense, 1.3x boost
- Razor Shell - 50% Defense drop chance, targets Special Defense, 1.3x boost

**Elemental Blade Moves:**
- Cryo Blade - Ice slashing, 10% frostbite chance, targets Special Defense
- Shock Blade - Electric slashing, 10% paralysis chance, targets Special Defense  
- Flame Blade - Fire slashing, 10% burn chance, targets Special Defense
- Stone Axe - Rock slashing, sets Stealth Rock, targets Special Defense
- Steel Blade - Steel slashing, 10% Stealth Rock chance, targets Special Defense

### Strategic Advantages
**Wall Breaking:**
- **Physical Walls**: Power Edge completely bypasses high Defense stats
- **Mixed Attackers**: Physical slashing moves become pseudo-special attacks
- **Stat Distribution**: Exploits Pokemon with high Defense but low Special Defense
- **Defensive Typing**: Type resistances still apply, but defensive stats are circumvented

**Offensive Pressure:**
- **Immediate Impact**: No setup required, works from turn one
- **Unpredictable**: Opponents may expect Defense targeting, not Special Defense
- **Crit Synergy**: High crit rates of slashing moves amplify Special Defense targeting
- **Coverage**: Wide variety of slashing moves across multiple types

### Interactions with Other Abilities
**Related Abilities:**
- **Keen Edge**: Standard version that targets Defense normally
- **Power Fists**: Equivalent effect for punching moves instead of slashing moves
- **Exploit Weakness**: Targets the lower of Defense/Special Defense for all moves
- **Roundhouse**: Similar concept but for kicking moves with perfect accuracy

**Synergistic Abilities:**
- **Mystic Blades**: Converts physical slashing moves to special, stacks with Special Defense targeting
- **Sweeping Edge**: Makes slashing moves hit both opponents, both get Special Defense targeting
- **Molten Blades**: Adds burn chance to Special Defense-targeting slashing moves

### Common Users and Strategies
**Ideal Pokemon:**
- **Physical Attackers**: High Attack stat Pokemon that can exploit Special Defense
- **Mixed Attackers**: Pokemon with decent Attack that want to pressure special walls
- **Crit-focused Builds**: Pokemon that can take advantage of high crit rate slashing moves

**Team Roles:**
- **Wall Breaker**: Specifically targets special defensive walls
- **Physical Sweeper**: Enhanced offensive presence against defensive teams
- **Late-Game Cleaner**: Cuts through weakened special walls

### Example Damage Scenarios
**Vs Blissey (High Special Defense but still targeted):**
- Slash (70 BP): 91 effective BP targeting 10 base Defense instead of 135 base Special Defense
- Result: Massive damage increase despite high Special Defense

**Vs Skarmory (High Defense):**
- Leaf Blade (90 BP): 117 effective BP targeting 70 base Special Defense instead of 140 base Defense
- Result: Nearly double damage output

**Vs Balanced Defenders:**
- Air Slash (75 BP): 97.5 effective BP targeting Special Defense
- Still benefits from 30% boost while potentially hitting weaker defensive stat

### Counters and Limitations
**Defensive Counters:**
- **Special Walls**: Pokemon with high Special Defense can still tank boosted slashing moves
- **Type Resistances**: Resisting the slashing move's type provides significant damage reduction
- **Abilities**: Filter, Solid Rock, and similar damage-reducing abilities still apply

**Offensive Counters:**
- **Priority Moves**: Fast revenge killing before Power Edge user can sweep
- **Status Effects**: Burn still reduces physical Attack stat for slashing moves
- **Stat Drops**: Intimidate, Swagger, and similar Attack-reducing effects

**Strategic Limitations:**
- **Move Dependence**: Only works with specific slashing moves
- **Type Coverage**: Limited to types that have access to slashing moves
- **Physical Attack Reliance**: Still uses physical Attack stat for damage calculation

### Competitive Viability
**Advantages:**
- **Meta Disruption**: Forces opponents to rethink defensive strategies
- **Immediate Power**: No setup required for significant damage boost
- **Versatility**: Works with variety of slashing moves across multiple types
- **Surprise Factor**: Unexpected Special Defense targeting can win key matchups

**Considerations:**
- **Move Pool Dependency**: Requires access to good slashing moves
- **Specialized Role**: Most effective against teams with physical walls
- **Coverage Gaps**: May struggle against Pokemon that resist slashing move types

### Version History
- Introduced as part of Elite Redux's expanded ability system
- Provides same damage boost as Keen Edge with Special Defense targeting
- Works with all existing and future moves flagged for Keen Edge compatibility
- Complements the physical-to-special targeting ability theme in Elite Redux
---
id: 314
name: Mountaineer
status: reviewed
character_count: 88
---

# Mountaineer - Ability ID 314

## In-Game Description
"Immune to Rock-type attacks and Stealth Rock damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mountaineer grants immunity to all Rock-type moves and Stealth Rock entry hazard damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Mountaineer provides two distinct protective effects:
1. **Rock-type Move Immunity**: Complete immunity to all Rock-type attacks
2. **Stealth Rock Immunity**: No damage taken from Stealth Rock entry hazards

### Technical Implementation
```cpp
constexpr Ability Mountaineer = {
    .onAfterTypeEffectiveness =
        +[](ON_AFTER_TYPE_EFFECTIVENESS) {
            if (moveType == TYPE_ROCK) *mod = 0;
        },
    .onAfterTypeEffectivenessFor = APPLY_ON_TARGET,
    .breakable = TRUE,
    .stealthRockImmune = TRUE,
};
```

The ability works by:
- Setting type effectiveness modifier to 0 for Rock-type moves (`*mod = 0`)
- Using the `stealthRockImmune` flag to prevent Stealth Rock damage
- Being marked as `breakable = TRUE`, meaning it can be suppressed by abilities like Mold Breaker

### Affected Rock-Type Moves
Mountaineer provides immunity to all Rock-type moves including but not limited to:
- Stone Edge
- Rock Slide  
- Rock Blast
- Ancient Power
- Power Gem
- Head Smash
- Stone Axe
- Rock Wrecker
- Diamond Storm
- Thousand Arrows (when used by Zygarde)

### Interactions with Other Abilities/Mechanics
- **Mold Breaker Effects**: Can be bypassed by Mold Breaker, Turboblaze, Teravolt, and similar abilities
- **Multi-Hit Moves**: Completely negates multi-hit Rock moves like Rock Blast
- **Critical Hits**: Even critical Rock-type moves deal no damage
- **Status Rock Moves**: Non-damaging Rock moves (like Stealth Rock setup) are not affected
- **Combination with Other Immunities**: Stacks with other type immunities and resistances

### Stealth Rock Interaction
- Prevents all damage from Stealth Rock regardless of the Pokemon's typing
- Does not prevent other entry hazards (Spikes, Toxic Spikes, Sticky Web)
- Does not remove existing Stealth Rock from the field (unlike Molten Core)

### Strategic Implications
**Offensive Value:**
- Allows safe switching into predicted Rock-type moves
- Provides setup opportunities against Rock-type attackers
- Excellent for pivot strategies

**Defensive Value:**
- Hard counter to Rock-type sweepers
- Negates Stealth Rock chip damage for improved longevity
- Reduces opponent's coverage options

**Team Synergy:**
- Excellent on teams weak to Rock-type moves
- Pairs well with Pokemon that struggle with entry hazards
- Good insurance against common Rock-type coverage moves

### Common Users
Based on the species data, Mountaineer appears on various Pokemon including:
- Ice-type Pokemon (often as regular or innate ability)
- Fire-type Pokemon (frequently as innate ability)  
- Ground/Rock-type hybrids (providing unique defensive coverage)
- Flying-type Pokemon (complementing their typical Rock weakness)
- Various legendary and pseudo-legendary Pokemon

### Competitive Usage Notes
- **Tier Impact**: Particularly valuable in higher tiers where Stealth Rock is omnipresent
- **Meta Relevance**: Counters Rock-type coverage moves that are common in competitive play
- **Setup Potential**: Provides safe setup opportunities against Rock-type moves
- **Hazard Management**: Reduces reliance on traditional hazard removal

### Counters
- **Mold Breaker**: Completely bypasses the immunity
- **Non-Rock Coverage**: Opponents can use other coverage types
- **Status Moves**: Vulnerable to status conditions and non-damaging moves
- **Indirect Damage**: Cannot prevent damage from burns, poison, or weather

### Synergies
- **Weak Armor**: Can safely activate on contact moves without Rock-type interference
- **Sturdy**: Provides additional protection layers
- **Recovery Moves**: Longevity enhanced by reduced chip damage
- **Setup Moves**: Safe setup opportunities against Rock-type users

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Shares Stealth Rock immunity with Molten Core (ability that also absorbs Rock moves for stat boosts)
- Part of the defensive immunity ability family alongside type-specific immunities

### Example Damage Calculations
```
252+ Atk Choice Band Tyranitar Stone Edge vs. Mountaineer Pokemon:
Normal: 150-176 HP (potential KO)
With Mountaineer: 0 HP (no damage)

Stealth Rock damage on typical 4x weak Flying/Ice type:
Normal: 50% max HP
With Mountaineer: 0% max HP
```

The ability transforms Rock-weak Pokemon into reliable counters and provides significant defensive utility in hazard-heavy metagames.
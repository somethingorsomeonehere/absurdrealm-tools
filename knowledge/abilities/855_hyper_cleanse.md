---
id: 855
name: Hyper Cleanse
status: reviewed
character_count: 170
---

# Hyper Cleanse - Ability ID 855

## In-Game Description
"Immune to status. Halves poison damage taken."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to all status conditions. Additionally reduces all Poison-type damage by 50%. If afflicted with status when gaining this ability, conditions are immediately cured.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Hyper Cleanse is a powerful defensive ability that combines complete status immunity with poison-type damage reduction. This makes the Pokemon an exceptional defensive pivot and status absorber.

### Status Immunity
- **Complete immunity**: Prevents all major status conditions
  - Burn: Cannot be burned by any means
  - Freeze: Cannot be frozen
  - Paralysis: Cannot be paralyzed
  - Poison: Cannot be poisoned (regular or badly poisoned)
  - Sleep: Cannot be put to sleep
- **Mold Breaker interaction**: Unlike most abilities, Hyper Cleanse's status immunity is NOT bypassed by Mold Breaker
- **Ability flag**: `breakable = TRUE` but with special `removesStatusOnImmunity = TRUE`

### Poison Damage Reduction
- **50% reduction**: All poison-type moves deal half damage
- **Stacks multiplicatively**: With other resistances and defensive modifiers
- **Type effectiveness**: Makes neutral poison hits deal 0.5x damage
- **Resisted hits**: Makes resisted poison hits deal 0.25x damage

### Technical Implementation
```c
constexpr Ability HyperCleanse = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (moveType == TYPE_POISON) RESISTANCE(.5);
        },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_STATUS1)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Key Features
- **CHECK_STATUS1**: Checks for all primary status conditions
- **RESISTANCE(.5)**: Applies 50% damage reduction to poison moves
- **removesStatusOnImmunity**: Cures existing status when ability activates

### Important Interactions
- **Status moves**: All status-inducing moves fail (Thunder Wave, Will-O-Wisp, etc.)
- **Secondary effects**: Move secondary effects that cause status also fail
- **Toxic Spikes**: Immune to poisoning from Toxic Spikes
- **Flame Orb/Toxic Orb**: Items have no effect
- **Synchronize**: Cannot receive status from Synchronize
- **Effect Spore**: Immune to all Effect Spore triggers

### Poison Damage Calculations
Examples with 100 base power poison move:
- **Neutral target**: 100 × 0.5 = 50 power
- **Grass/Fairy target**: 100 × 2 × 0.5 = 100 power
- **Steel target**: Would be immune anyway
- **Poison/Ground target**: 100 × 0.5 × 0.5 = 25 power

### Strategic Implications
- **Ultimate status wall**: Cannot be crippled by status conditions
- **Poison immunity plus**: Better than Immunity ability due to damage reduction
- **Hazard clearer**: Can safely switch into Toxic Spikes
- **Stall breaker**: Immune to Toxic stall strategies
- **Burn immunity**: No Attack reduction from burn
- **Para immunity**: No Speed reduction from paralysis

### Common Users
- Specially defensive Pokemon who fear status
- Defensive pivots and walls
- Support Pokemon that need reliability
- Pokemon weak to poison needing extra protection

### Competitive Usage Notes
- **S-tier defensive ability**: Among the best defensive abilities
- **Role compression**: Provides both status immunity and defensive typing help
- **Team support**: Acts as team's status absorber
- **No drawback**: Unlike Comatose, has no sleep vulnerabilities
- **Always active**: Unlike Leaf Guard, doesn't need weather

### Counters
- **Direct damage**: Must rely on regular attacks
- **Stat reduction**: Can still have stats lowered
- **Entry hazards**: Still takes Stealth Rock/Spikes damage
- **Taunt**: Can still be Taunted
- **Ability suppression**: Neutralizing Gas disables it

### Synergies
- **Defensive stats**: Maximizes value on bulky Pokemon
- **Wish support**: Can reliably pass Wishes without status risk
- **Aromatherapy/Heal Bell**: Can be team's cleric without status risk
- **Poison typing**: Stacks with poison's natural poison immunity
- **Regenerator**: Would create ultimate defensive pivot

### Comparison to Similar Abilities
- **Immunity**: Only blocks poison, no damage reduction
- **Water Veil**: Only blocks burn
- **Insomnia/Vital Spirit**: Only blocks sleep
- **Limber**: Only blocks paralysis
- **Magma Armor**: Only blocks freeze
- **Leaf Guard**: Requires sun, only end of turn
- **Comatose**: Has sleep vulnerabilities

### Version History
- Elite Redux exclusive ability
- Combines multiple defensive traits into one powerful ability
- Designed as premium defensive ability for special Pokemon
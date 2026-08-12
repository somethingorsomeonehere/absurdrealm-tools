---
id: 575
name: Thermal Exchange
status: reviewed
character_count: 211
---

# Thermal Exchange - Ability ID 575

## In-Game Description
"Ups Attack when hit by Fire. Immune to burn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Attack by one stage when hit by Fire-type moves and grants immunity to burn status. The Attack boost applies immediately after taking damage from any Fire attack. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Thermal Exchange provides two distinct defensive effects against Fire-type attacks:

1. **Attack Boost on Fire Damage**: When the Pokemon is hit by a Fire-type move that would deal damage, its Attack stat is raised by +1 stage immediately after damage calculation.

2. **Complete Burn Immunity**: The Pokemon cannot be inflicted with burn status through any means, including moves like Will-O-Wisp, abilities like Flame Body, or items like Flame Orb.

### Activation Conditions
- **Attack Boost**: Triggers on `onDefender` when:
  - `ShouldApplyOnHitAffect(battler)` is true (standard on-hit ability check)
  - `moveType == TYPE_FIRE` (move must be Fire-type)
  - `CanRaiseStat(battler, STAT_ATK)` is true (Attack can still be raised)

- **Burn Immunity**: Triggers on `onStatusImmune` when:
  - `status & CHECK_BURN` is true (any burn status attempt)

### Technical Implementation
```cpp
constexpr Ability ThermalExchange = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(moveType == TYPE_FIRE)
        CHECK(CanRaiseStat(battler, STAT_ATK))

        SetStatChanger(STAT_ATK, 1);
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        return TRUE;
    },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_BURN)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

### Affected Fire-Type Moves
All moves with `TYPE_FIRE` classification trigger the Attack boost, including but not limited to:
- Flamethrower, Fire Blast, Overheat
- Fire Punch, Blaze Kick, Flame Charge
- Heat Wave, Lava Plume, Eruption
- Hidden Power Fire, Tera Blast (when Fire-type)
- Fire-type Z-moves and Max Moves

### Interactions with Other Abilities/Mechanics

**Stat Stage Mechanics**:
- Each trigger raises Attack by exactly +1 stage (50% boost at +1, 100% at +2, etc.)
- Maximum Attack boost is +6 stages (+300% total)
- Stacks with other Attack-boosting effects (items, moves, abilities)
- Can be reset by moves like Clear Smog or abilities like Clear Body opponents

**Burn Immunity Details**:
- Prevents burn from direct status moves (Will-O-Wisp, Thunder Wave variants)
- Blocks burn from secondary effects (Scald 30% chance, Lava Plume, etc.)
- Stops burn from abilities (Flame Body, Flaming Jaws, etc.)
- Negates burn from held items (Flame Orb)
- `removesStatusOnImmunity = TRUE` means existing burns are cured upon gaining this ability

### Strategic Implications

**Offensive Pressure**:
- Turns Fire-type attacks into setup opportunities
- +1 Attack significantly improves physical damage output
- Multiple Fire hits can quickly max out Attack stat
- Particularly effective against Fire-type spam teams

**Fire-Type Matchup Reversal**:
- Completely reverses the typical Fire vs Steel/Ice dynamic
- Ice-types with this ability become Fire-type checks instead of victims
- Creates psychological pressure for Fire-type users

**Team Synergy**:
- Excellent on physical attackers that fear burn status
- Pairs well with moves that benefit from Attack boosts (physical STAB, coverage)
- Good on defensive pivots that can tank Fire moves and gain offensive presence

### Example Damage Calculations
Assuming base 100 Attack Pokemon with neutral nature:
- **Base**: 100 Attack = 236 final Attack stat at level 50
- **+1 Stage**: 150% = 354 Attack (50% increase)
- **+2 Stages**: 200% = 472 Attack (100% increase)
- **+6 Stages**: 400% = 944 Attack (300% increase, maximum)

### Common Users in Elite Redux
Based on proto data analysis:
- Various Ice-type Pokemon (creating Fire/Ice type interactions)
- Steel-types that benefit from Fire resistance and Attack boosts
- Physical attackers that want burn immunity
- Defensive Pokemon that can pivot and gain offensive presence

### Competitive Usage Notes

**Strengths**:
- Excellent Fire-type deterrent
- Provides both offensive and defensive utility
- No drawbacks or negative effects
- Reliable activation conditions

**Counters**:
- Special Fire-type moves still boost Attack but don't rely on Attack stat
- Non-Fire status moves (Thunder Wave, Toxic, Sleep Powder)
- Stat-clearing moves (Clear Smog, Haze)
- Abilities that prevent stat boosts (Clear Body on opponents)

**Synergies**:
- Physical STAB moves to utilize Attack boosts
- Priority moves for immediate pressure after boost
- Protective moves to avoid other status conditions
- Entry hazard support to wear down Fire-types switching in

### Version History
- Added in Elite Redux as ability ID 575
- Breakable ability (affected by Mold Breaker, Teravolt, Turboblaze)
- Functions identically to the official Pokemon games implementation
---
id: 537
name: Spike Armor
status: reviewed
character_count: 254
---

# Spike Armor - Ability ID 537

## In-Game Description
"30% chance to bleed on contact or offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Spike Armor has a 30% chance to inflict bleeding on contact moves, both when attacking and being attacked. Bleeding causes 1/16 max HP damage per turn, prevents healing, and negates the effects of stat stages. Rock and Ghost types are immune to bleeding.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger Rate**: 30% chance to inflict bleeding
- **Activation Conditions**: 
  - Must be a contact move (checked via `IsMoveMakingContact`)
  - Triggers both when using contact moves (`onAttacker`) and when hit by contact moves (`onDefender`)
  - Target must be able to bleed (`CanBleed` check)
- **Effect**: Inflicts bleeding status condition on the target

### Bleeding Status Condition
- **Damage**: 1/16 of max HP per turn (minimum 1 HP if calculation results in 0)
- **Duration**: Until cured, switched out, or battle ends
- **Type**: Primary status condition (mutually exclusive with burn, poison, paralysis, etc.)

### Technical Implementation
```cpp
ON_EITHER(SpikeArmor) {
    CHECK(ShouldApplyOnHitAffect(opponent))
    CHECK(CanBleed(opponent))
    CHECK(IsMoveMakingContact(move, gBattlerAttacker))
    CHECK(Random() % 100 < 30)

    AbilityStatusEffectSafe(MOVE_EFFECT_BLEED, battler, opponent);
    return TRUE;
}

#define BLEED_DAMAGE(hp) (hp / 16)
```

### Bleeding Immunity
Pokemon immune to bleeding:
- **Type Immunity**: Rock-type and Ghost-type Pokemon
- **Status Immunity**: Pokemon already affected by any primary status condition
- **Ability Immunity**: Pokemon with abilities that prevent status conditions
- **Special Cases**: Mycelium Might can override some immunities

### Contact Moves That Trigger Spike Armor
Any move with the contact flag, including but not limited to:
- Physical moves like Tackle, Body Slam, Earthquake (if contact-based)
- Multi-hit moves like Fury Attack, Pin Missile
- Priority moves like Quick Attack, Mach Punch
- Does NOT trigger on non-contact moves like Psychic, Flamethrower, Surf

### Strategic Implications
**Offensive Usage:**
- Punishes physical attackers that rely on contact moves
- Creates chip damage over time to wear down opponents
- Pairs well with defensive strategies and stall tactics

**Defensive Usage:**
- Deters contact-based physical attackers
- Provides passive damage without requiring setup
- Especially effective against fast physical sweepers

### Common Users
Based on proto analysis, Spike Armor is found on several Pokemon including:
- Various defensive and bulky Pokemon
- Some offensive Pokemon as either main or innate ability
- Multiple evolution lines with different ability combinations

### Competitive Usage Notes
- **Meta Role**: Anti-physical deterrent ability
- **Team Synergy**: Works well with defensive cores and status-spreading teams
- **Timing**: Most effective early-game when opponents haven't taken other status damage
- **Prediction**: Forces opponents to consider non-contact alternatives

### Counters and Limitations
**Direct Counters:**
- Rock and Ghost types (complete immunity)
- Pokemon with status immunity abilities
- Non-contact move users (special attackers, projectile moves)
- Clerics with status healing moves

**Situational Limitations:**
- Only 30% activation rate makes it unreliable
- Blocked by existing status conditions
- Magic Guard prevents bleeding damage
- Substitute blocks the ability from triggering

### Synergies
**Ability Synergies:**
- Magic Guard (on teammates) - protects from bleeding damage
- Guts (on opponents) - can backfire by boosting Attack
- Status immunity abilities provide protection

**Move Synergies:**
- Status moves to apply conditions before bleeding can trigger
- Entry hazards to complement chip damage strategy
- Healing moves to outlast bleeding effects

**Item Synergies:**
- Leftovers/recovery items to offset bleeding damage
- Status-healing berries as safety nets
- Rocky Helmet for additional contact punishment

### Version History
- Introduced in Elite Redux as part of the expanded ability system
- Part of the bleeding status condition mechanic unique to Elite Redux
- Ability ID 537 in the ability enum system
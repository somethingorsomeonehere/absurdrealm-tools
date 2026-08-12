---
id: 875
name: Energy Tap
status: reviewed
character_count: 135
---

# Energy Tap - Ability ID 875

## In-Game Description
"Heals the user for 1/8 of the damage they deal."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Heals the user for 1/8 of all damage they deal to opponents. Healing occurs immediately after damage is dealt. Minimum healing of 1 HP.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Energy Tap is a sustain ability that provides healing based on damage output. The ability activates after successfully dealing damage to an opponent, converting a portion of that damage into healing for the user.

### Activation Conditions
- **Damage requirement**: Must deal damage to an opponent with any move
- **HP requirement**: User must not be at maximum HP
- **Healing eligibility**: User must be able to be healed (not affected by Heal Block)
- **Timing**: Activates immediately after damage calculation during the attack sequence

### Healing Calculation
```c
// Energy Tap healing formula
healing_amount = damage_dealt / 8;
if (healing_amount == 0) healing_amount = 1; // Minimum 1 HP heal
```

### Technical Implementation
```c
constexpr Ability EnergyTap = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))

        gBattleMoveDamage = -gHpDealt / 8;
        if (!gBattleMoveDamage) gBattleMoveDamage = -1;
        BattleScriptCall(BattleScript_HydroCircuitAbsorbEffectActivated);
        return TRUE;
    },
};
```

### Move Compatibility
- **Direct damage moves**: All moves that deal direct damage
- **Multi-hit moves**: Heals after each individual hit
- **Critical hits**: Healing scales with the increased damage
- **Super effective hits**: Healing scales with damage multipliers
- **STAB moves**: Healing benefits from STAB damage bonus
- **Status moves**: No healing since they don't deal damage

### Important Interactions
- **Maximum HP**: No healing occurs if already at full health
- **Minimum healing**: Always heals at least 1 HP if damage is dealt
- **Heal Block**: Ability is suppressed while Heal Block is active
- **Substitute**: Does not heal when attacking through Substitute
- **Magic Guard**: Target's Magic Guard doesn't affect Energy Tap healing
- **Rocky Helmet/Rough Skin**: Recoil damage occurs after Energy Tap healing

### Strategic Applications
- **Offensive sustainability**: Allows sweepers to maintain health during long battles
- **Life Orb synergy**: Offsets Life Orb recoil damage partially
- **Multi-hit moves**: Particularly effective with moves like Bullet Seed or Rock Blast
- **High-damage moves**: More effective on Pokemon with powerful single-target moves
- **Mixed attackers**: Benefits from both physical and special damage output

### Competitive Usage
- **Wallbreaker support**: Helps wallbreakers stay healthy during setup
- **Revenge killing**: Allows revenge killers to heal back up after trades
- **Pivot moves**: U-turn/Volt Switch provide healing while maintaining momentum
- **Choice item users**: Provides sustain for Choice Band/Specs users
- **Setup sweepers**: Helps maintain health during setup phases

### Synergies
- **Life Orb**: Partially offsets the recoil damage
- **Choice items**: Provides sustain for locked-in attackers
- **Recoil moves**: Helps offset recoil from moves like Double-Edge
- **Drain moves**: Stacks with drain moves for enhanced healing
- **High base power moves**: Maximizes healing potential

### Counters and Limitations
- **Heal Block**: Completely negates the ability
- **Max HP condition**: No benefit when already at full health
- **Status moves**: Provides no healing from non-damaging moves
- **Low damage output**: Less effective on defensive or utility Pokemon
- **Ability suppression**: Mold Breaker effects disable Energy Tap

### Optimal Users
- High-attack Pokemon that benefit from sustain
- Mixed attackers with diverse move coverage
- Pokemon that use recoil moves or hold Life Orb
- Setup sweepers that need longevity
- Pokemon with multi-hit signature moves

### Comparison to Similar Abilities
- **Drain moves**: Energy Tap works with all damaging moves, not just specific ones
- **Poison Heal**: Provides healing without status condition requirement
- **Regenerator**: Energy Tap requires dealing damage vs. switching out
- **Leftovers**: Provides burst healing vs. gradual passive healing

### Version History
- New ability introduced in Elite Redux
- Part of the expanded ability system for enhanced battle complexity
- Designed to support offensive playstyles with built-in sustainability
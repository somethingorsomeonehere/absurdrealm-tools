---
id: 423
name: Hydro Circuit
status: reviewed
character_count: 119
---

# Hydro Circuit - Ability ID 423

## In-Game Description
"Electric moves +50%; Water moves siphon 25% damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Hydro Circuit boosts Electric-type moves by 50% and heals the user for 25% of damage dealt when using Water-type moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Hydro Circuit is a dual-effect ability that provides both offensive and recovery benefits. It combines damage amplification for Electric moves with HP siphoning from Water moves, making it particularly powerful for Electric/Water dual-type Pokemon.

### Activation Conditions
**Electric Move Boost:**
- **Multiplier**: 1.5x damage (50% increase)
- **Move requirement**: Any Electric-type move
- **Timing**: Applies during damage calculation

**Water Move Healing:**
- **Healing amount**: 25% of damage dealt (gHpDealt / 4, minimum 1 HP)
- **Move requirement**: Any Water-type move that deals damage
- **Target conditions**: Target cannot be at full HP
- **User conditions**: User must be able to heal (not at full HP)
- **Timing**: Triggers after damage is dealt

### Technical Implementation
```cpp
// From abilities.cc - HydroCircuit ability
constexpr Ability HydroCircuit = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(moveType == TYPE_WATER)

        gBattleMoveDamage = -gHpDealt / 4;
        if (!gBattleMoveDamage) gBattleMoveDamage = -1;
        BattleScriptCall(BattleScript_HydroCircuitAbsorbEffectActivated);
        return TRUE;
    },
    .onOffensiveMultiplier = Transistor.onOffensiveMultiplier,
};

// Electric boost uses Transistor logic:
// if (moveType == TYPE_ELECTRIC) MUL(1.5);
```

### Dual-Type Move Interactions
**Electric/Water moves**: Both effects apply simultaneously
- Damage is boosted by 1.5x from Electric typing
- User heals for 25% of the boosted damage dealt
- Examples: No natural Electric/Water moves exist, but with abilities like Electrify

### Important Interactions
- **Healing calculation**: Based on actual damage dealt to target
- **Minimum healing**: Always heals at least 1 HP if conditions are met
- **Substitute**: Healing works against substitute (HITMARKER_IGNORE_SUBSTITUTE)
- **Multi-hit moves**: Healing triggers once per hit for Water moves
- **Status immunity**: No special status protections
- **Ability suppression**: Doesn't work if ability is suppressed

### Battle Script Behavior
```asm
BattleScript_HydroCircuitAbsorbEffectActivated::
    manipulatedamage DMG_TO_HP_FROM_ABILITY
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_ATTACKER
    datahpupdate BS_ATTACKER
    printstring STRINGID_ATTACKERREGAINEDHEALTH
```

### Strategic Implications
**Offensive benefits:**
- **STAB synergy**: Excellent on Water/Electric types with dual STAB
- **Coverage moves**: Makes Electric moves more threatening
- **Mixed attacking**: Supports both physical and special movesets

**Defensive benefits:**
- **Sustain**: Water moves provide reliable healing
- **Longevity**: Allows for extended battles with proper Water move usage
- **Health management**: Can offset recoil or entry hazard damage

### Common Users
**Confirmed Users:**
- **Mega Lanturn**: Electric/Water with perfect typing synergy
  - Has ABILITY_HYDRO_CIRCUIT as all three abilities
  - Innate abilities: Radiance, Storm Drain
  - Stats favor special attacking (126 SpA)

### Competitive Usage Notes
- **Type synergy**: Incredible on Electric/Water Pokemon
- **Move selection**: Prioritize Water moves with high damage output
- **Setup potential**: Healing enables longer setup sequences
- **Mixed coverage**: Electric boost makes coverage moves more viable
- **Sustainability**: Water moves provide consistent healing source

### Optimal Movesets
**Special Attacker (Mega Lanturn example):**
- Surf/Hydro Pump (STAB + healing)
- Thunderbolt/Thunder (STAB + boost)
- Ice Beam (coverage)
- Volt Switch (STAB + boost + pivot)

**Physical Options:**
- Waterfall/Liquidation (STAB + healing)
- Thunder Punch/Wild Charge (STAB + boost)
- U-turn (utility)

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Healing prevention**: Heal Block stops Water move healing
- **Type resistances**: Ground types resist Electric boost
- **Substitute**: Can limit healing effectiveness
- **Priority moves**: Fast KOs before healing accumulates

### Synergies
**Team support:**
- **Rain teams**: Boosts Water move power and accuracy
- **Electric Terrain**: Boosts Electric moves further (doesn't stack with ability)
- **Choice items**: Maximizes damage for better healing
- **Life Orb**: Recoil can be offset by Water move healing

**Status moves:**
- **Thunder Wave**: Benefits from Electric boost if it dealt damage
- **Toxic Spikes**: Setup support for wearing down switch-ins

### Ability Comparison
**Similar abilities:**
- **Transistor**: Electric boost only (no healing)
- **Torrent/Swarm**: Type boost when low HP (conditional)
- **Volt Absorb**: Electric immunity + healing (different activation)
- **Water Absorb**: Water immunity + healing (different activation)

**Unique aspects:**
- Only ability combining type boost with damage-based healing
- Works on different move types (Electric boost, Water heal)
- Healing scales with damage output

### Version History
- Elite Redux custom ability (ID 423)
- Dual-type synergy ability for Electric/Water combinations
- Part of the expanded ability roster for enhanced Pokemon diversity
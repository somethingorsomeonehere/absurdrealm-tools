---
id: 734
name: Ape Shift
status: reviewed
character_count: 224
---

# Ape Shift - Ability ID 734

## In-Game Description
"Transforms below 50% HP, curing status and always critting."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transforms the Pokemon when HP drops to 50% or below, automatically curing all status conditions after transformation. After transforming, all attacks become critical hits. Activates on entry, during battle, and at turn end. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Ape Shift is a unique transformation ability exclusive to Mega Slaking that fundamentally changes the Pokemon's battle capabilities when its HP threshold is reached.

### Activation Conditions
- **HP threshold**: HP must be at 50% or below (uses hpFraction = 2 in code)
- **Species requirement**: Only works on SPECIES_SLAKING_MEGA and SPECIES_SLAKING_MEGA_APE_SHIFT
- **Transform state**: Cannot activate if already transformed by another effect
- **Timing**: Can trigger on entry, at end of turn, or when taking damage

### Transformation Effects
1. **Form change**: 
   - SPECIES_SLAKING_MEGA to SPECIES_SLAKING_MEGA_APE_SHIFT (when HP drops)
   - SPECIES_SLAKING_MEGA_APE_SHIFT to SPECIES_SLAKING_MEGA (when HP rises above 50%)

2. **Status cure**: Automatically removes all status conditions during transformation:
   - Burn, freeze, paralysis, poison (including badly poisoned), sleep
   - Uses `curestatus BS_ATTACKER` battle script command

3. **Critical hit guarantee**: In Ape Shift form, all attacks become critical hits
   - Returns `ALWAYS_CRIT` when in SPECIES_SLAKING_MEGA_APE_SHIFT form

### Technical Implementation
```c
// HP-based transformation check
{ABILITY_APE_SHIFT, SPECIES_SLAKING_MEGA, SPECIES_SLAKING_MEGA_APE_SHIFT, 2}

// Critical hit guarantee in shifted form
.onCrit = +[](ON_CRIT) -> int {
    CHECK(gBattleMons[battler].species == SPECIES_SLAKING_MEGA_APE_SHIFT)
    return ALWAYS_CRIT;
}

// Transformation handler with status cure
int ApeShiftHandler(int battler, AbilityCallType callType) {
    // Various checks including ShouldChangeFormHpBased(battler)
    if (gBattleMons[battler].species == SPECIES_SLAKING_MEGA_APE_SHIFT) {
        BattleScriptCall(BattleScript_ApeShift); // Cures status
    }
    BattleScriptCall(BattleScript_StackBattlerFormChange);
}
```

### Battle Script Details
```assembly
BattleScript_ApeShift::
    saveattackertostack3
    jumpifstatus BS_ATTACKER, STATUS1_ANY, BattleScript_ApeShift_HealStatus
    # ... status cure logic with curestatus command
```

### Unique Characteristics
- **Bidirectional transformation**: Can transform both ways based on HP
- **Multiple trigger points**: Entry, end turn, and when taking damage
- **Status immunity during shift**: Provides free status cure when transforming
- **Guaranteed crits**: Every attack is a critical hit in shifted form
- **Randomizer banned**: Cannot appear on random Pokemon due to species restriction

### Strategic Implications
- **Low HP advantage**: Becomes more dangerous when weakened
- **Status immunity**: Natural counter to status-based strategies
- **Critical hit synergy**: Pairs with moves that have additional crit effects
- **Timing strategy**: Can deliberately lower HP to trigger transformation
- **Pressure build**: Opponents must either KO immediately or face guaranteed crits

### Interactions
- **Healing moves**: Can reverse transformation if HP rises above 50%
- **Multi-hit moves**: Transformation can trigger mid-sequence
- **Status immunity**: Only during transformation, not permanent
- **Ability suppression**: Mold Breaker effects prevent the ability
- **Transform status**: Cannot activate if affected by Transform move

### Counters
- **OHKO strategies**: Prevent transformation by avoiding the HP threshold
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Priority moves**: Strike before the guaranteed crits land
- **Defensive strategies**: Tank the crits with high defense/resistances
- **Status after transformation**: Can be statused again after shifting

### Synergies
- **Focus Sash/Sturdy**: Survive to trigger transformation
- **Healing moves**: Control when transformation occurs
- **High critical hit ratio moves**: Benefit from guaranteed crits
- **Life Orb**: Extra power on guaranteed critical hits
- **Type coverage**: Diverse movepool to utilize guaranteed crits

### Version History
- Elite Redux exclusive ability
- Unique to Mega Slaking evolutionary line
- One of the few abilities that provides guaranteed critical hits
- Combines transformation, status cure, and battle advantage mechanics

### Competitive Notes
- **Risk/reward design**: Must reach low HP to gain advantage
- **Momentum shift**: Can turn the tide when properly utilized
- **Prediction game**: Opponents must decide between immediate KO or defensive play
- **Team support**: Benefits from entry hazard removal and healing support
- **Versatile timing**: Multiple activation windows provide flexibility
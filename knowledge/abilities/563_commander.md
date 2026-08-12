---
id: 563
name: Commander
status: reviewed
character_count: 274
---

# Commander - Ability ID 563

## In-Game Description
"Hops inside an allied Dondozo. Boosts its ally but can't act."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows Tatsugiri to enter an allied Dondozo and become untargetable. Dondozo receives +2 to all stats, cannot switch or be forced out and Tatsugiri becomes unusable. If Dondozo faints, Tatsugiri reappears and can act normally again. Cannot be swapped, copied, or suppressed.

## Detailed Mechanical Explanation
*For Discord/reference use*

Commander is a unique symbiotic ability that creates a powerful duo mechanic between Tatsugiri and Dondozo.

### Core Mechanics
- **Species Requirement**: Only works when Tatsugiri (Commander user) is paired with Dondozo ally
- **Activation**: Automatically triggers on switch-in if both Pokemon are present and alive
- **State System**: Uses COMMANDER_ACTIVE/COMMANDER_NOT_ACTIVE states to track activation

### Battle Effects
1. **Tatsugiri Effects**:
   - Becomes semi-invulnerable (STATUS3_SEMI_INVULNERABLE)
   - Cannot be targeted by moves (ACCURACY_ALWAYS_MISSES)
   - Made invisible on battlefield
   - Cannot act while inside Dondozo

2. **Dondozo Effects**:
   - Receives +2 boost to all stats (Attack, Defense, Sp.Atk, Sp.Def, Speed)
   - Gains STATUS4_COMMANDED status
   - Can act normally while carrying Tatsugiri

### Technical Implementation
```cpp
constexpr Ability Commander = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK(GetAbilityState(battler, ability))
        SetAbilityState(battler, ability, COMMANDER_NOT_ACTIVE);
        gStatuses3[battler] &= ~STATUS3_SEMI_INVULNERABLE;
        BattleScriptCall(BattleScript_CommanderEnds);
        return TRUE;
    },
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(GetAbilityState(target, ability))
        return ACCURACY_ALWAYS_MISSES;
    },
    .onBattlerFaintsFor = APPLY_ON_ALLY,
    .onAccuracyFor = APPLY_ON_TARGET,
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
};
```

### Activation Conditions
- Tatsugiri must have Commander ability
- Ally must be Dondozo (base species check)
- Both Pokemon must be alive
- Triggers automatically on Tatsugiri switch-in

### Deactivation
- When Dondozo (the ally) faints, Commander ends
- Tatsugiri becomes visible and targetable again
- Semi-invulnerable status is removed
- Tatsugiri can act normally again

### Targeting Mechanics
- Moves that would target Commander-active Tatsugiri automatically redirect
- Multi-target moves skip the Commander-active Pokemon
- Ally-targeting moves cannot target Commander-active Tatsugiri

### Competitive Applications
- **Stat Boost Strategy**: Free +2 to all stats makes Dondozo extremely threatening
- **Protection**: Tatsugiri becomes immune to all direct attacks
- **Team Support**: Allows Tatsugiri to provide utility without taking damage
- **Risk/Reward**: If Dondozo faints, Tatsugiri is exposed and may be revenge-killed

### Strategic Usage
- **Setup Potential**: Use Commander activation to set up a powerful Dondozo sweep
- **Pivot Play**: Switch Tatsugiri in to activate Commander at key moments
- **Team Composition**: Build around protecting Dondozo while it's boosted
- **Counterplay**: Target Dondozo with status moves or strong attacks to force Commander to end

### Important Notes
- Ability is unsuppressable (cannot be disabled by Gastro Acid, etc.)
- Banned from randomizer due to species-specific requirement
- Only works in Double Battles where both species can be on field simultaneously
- Tatsugiri forms (Curly, Stretchy, Droopy) all work with Commander
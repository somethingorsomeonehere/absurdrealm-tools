---
id: 795
name: Embody Aspect
status: reviewed
character_count: 72
---

# Embody Aspect - Ability ID 795

## In-Game Description
"+1 Speed on Entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the Pokemon's Speed stat by one stage when switching into battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Embody Aspect is a form-dependent ability exclusive to Mega Ogerpon forms in Elite Redux. Each form has a different variant that boosts a specific stat upon entering battle:

- **Base Embody Aspect (ID 795)**: +1 Speed stage
- **Embody Aspect Hearthflame (ID 796)**: +1 Attack stage  
- **Embody Aspect Cornerstone (ID 797)**: +1 Defense stage
- **Embody Aspect Wellspring (ID 798)**: +1 Special Defense stage

### Activation Conditions
- Triggers automatically when the Pokemon switches into battle
- Activates on first entry, switching in from the bench, and revival from fainting
- Does not activate if the stat is already at maximum (+6 stages)
- Bypassed by abilities like Clear Body or effects that prevent stat changes

### Technical Implementation
```cpp
// Base Embody Aspect (Speed boost)
constexpr Ability EmbodyAspect = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_SPEED))
        SetStatChanger(STAT_SPEED, 1);
        BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
        return TRUE;
    },
};

// Hearthflame variant (Attack boost)
constexpr Ability EmbodyAspectHearthflame = {
    .onEntry = IntrepidSword.onEntry,  // Reuses IntrepidSword logic
};

// Cornerstone variant (Defense boost)  
constexpr Ability EmbodyAspectCornerstone = {
    .onEntry = DauntlessShield.onEntry,  // Reuses DauntlessShield logic
};

// Wellspring variant (Special Defense boost)
constexpr Ability EmbodyAspectWellspring = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(CanRaiseStat(battler, STAT_SPDEF))
        SetStatChanger(STAT_SPDEF, 1);
        BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
        return TRUE;
    },
};
```

### Statistical Impact
- **1 stage boost** = 1.5x multiplier to the affected stat
- Speed boost: Enables outspeeding threats and revenge killing
- Attack boost: Immediate offensive pressure upon entry
- Defense boost: Enhanced physical bulk for switching into attacks
- Special Defense boost: Improved special bulk and staying power

### Exclusive Users
**Mega Ogerpon Forms:**
- **Mega Ogerpon** (Grass): Base Embody Aspect (+1 Speed)
  - Stats: 80/125/104/80/106/155
  - Additional Abilities: Defiant, Forest Rage, Super Slammer (innate)
  
- **Mega Ogerpon Hearthflame** (Grass/Fire): Embody Aspect Hearthflame (+1 Attack)
  - Stats: 80/135/104/110/96/125  
  - Additional Abilities: Mold Breaker, Hellblaze, Super Slammer (innate)
  
- **Mega Ogerpon Cornerstone** (Grass/Rock): Embody Aspect Cornerstone (+1 Defense)
  - Stats: 80/120/156/80/96/118
  - Additional Abilities: Self Repair, Rockhard Shaft, Super Slammer (innate)
  
- **Mega Ogerpon Wellspring** (Grass/Water): Embody Aspect Wellspring (+1 Special Defense)
  - Stats: 80/120/94/80/156/120
  - Additional Abilities: Self Repair, Riptide, Super Slammer (innate)

### Strategic Applications
**Base Form (Speed boost):**
- Revenge killing after teammates fall
- Immediate speed control upon switching in
- Enhanced setup sweeping potential with speed advantage

**Hearthflame Form (Attack boost):**
- Immediate offensive presence
- Maximizes physical attack power with Mold Breaker support
- Synergizes with Hellblaze for Fire-type STAB boost

**Cornerstone Form (Defense boost):**
- Enhanced physical wall capabilities
- Switching into physical attacks more safely
- Prolonged staying power with Self Repair

**Wellspring Form (Special Defense boost):**
- Special tank role with immediate bulk increase
- Countering special attackers more effectively
- Sustained presence with Self Repair recovery

### Counters and Limitations
**Direct Counters:**
- **Clear Body/White Smoke**: Prevents the stat boost entirely
- **Unaware**: Ignores stat boosts for damage calculation
- **Haze/Clear Smog**: Removes accumulated stat boosts
- **Topsy-Turvy**: Inverts stat changes (though rarely seen)

**Situational Limitations:**
- Cannot boost stats already at +6 maximum
- One-time boost per switch-in (doesn't stack with multiple entries)
- Vulnerable to priority moves despite speed boosts
- Stat boosts reset upon switching out

### Synergies
**With Other Abilities:**
- **Baton Pass users**: Can pass the initial boost to other teammates
- **Defiant/Competitive**: Stack with Embody Aspect if opponents use stat-lowering moves
- **Speed Boost**: Compounds with base form's speed increase over time

**With Moves:**
- **Agility/Rock Polish**: Further speed control with base form
- **Swords Dance/Dragon Dance**: Stack offensive boosts with Hearthflame form
- **Iron Defense**: Enhance defensive prowess with Cornerstone form
- **Calm Mind**: Complement special bulk with Wellspring form

### Competitive Usage Notes
- **Entry Hazard Synergy**: Abilities provide immediate value even against hazard damage
- **Prediction Dependent**: Optimal form choice depends on predicted threats
- **Multi-Form Team Building**: Different Ogerpon forms fill distinct team roles
- **Momentum Shifts**: Each form can immediately impact battle flow upon entry

### Version History
- **Elite Redux Addition**: Introduced as signature ability for Mega Ogerpon forms
- **Form Implementation**: Each mask form received appropriate stat-boosting variant
- **Balance Consideration**: One-time per entry prevents excessive stacking
- **Code Reuse**: Hearthflame and Cornerstone variants reuse existing ability logic (IntrepidSword/DauntlessShield)
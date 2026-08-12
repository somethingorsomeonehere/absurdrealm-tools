---
id: 542
name: Showdown Mode
status: reviewed
character_count: 129
---

# Showdown Mode - Ability ID 542

## In-Game Description
"Ambush + Violent Rush."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees a critical hit while also boosting the user's Attack by 20% and their Speed by 50% after switching in. Lasts one turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Showdown Mode is a combination ability that merges two powerful first-turn abilities:

**Ambush Component:**
- Guarantees critical hits on all moves during the first turn after switching in
- Critical hits ignore defensive stat boosts and deal 1.5x damage

**Violent Rush Component:**
- Boosts Attack stat by 20% (multiplier of 6/5 = 1.2x) on the first turn
- Boosts Speed by 50% (multiplier of 150/100 = 1.5x) on the first turn

### Activation Conditions
- Triggers automatically upon switching into battle
- Effects only last for the first turn after switch-in
- Both volatile flags (`showdownMode` and `violentRush`) are set simultaneously
- The ability announces itself with a switch-in message

### Technical Implementation
```c
constexpr Ability ShowdownMode = {
    .onEntry = +[](ON_ENTRY) -> int {
        gVolatileStructs[battler].showdownMode = gVolatileStructs[battler].started.showdownMode = TRUE;
        return SwitchInAnnounce(B_MSG_SWITCHIN_SHOWDOWN_MODE);
    },
};
```

**Critical Hit Logic:**
```c
// In battle_script_commands.c - Always Critical section
if (gVolatileStructs[battlerAtk].showdownMode) {
    return ALWAYS_CRIT;
}
```

**Attack Boost:**
```c
// In battle_util.c - Attack stat calculation
if (gVolatileStructs[battler].showdownMode) statBase = statBase * 6 / 5; // +20%
```

**Speed Boost:**
```c
// In battle_main.c - Speed calculation
if (gVolatileStructs[battlerId].showdownMode) speed = (speed * 150) / 100; // +50%
```

**Turn Cleanup:**
```c
// Effects are cleared after the first turn unless battler was just switched in
CLEAR_ONE_TURN(showdownMode)
CLEAR_ONE_TURN(violentRush)
```

### Numerical Values
- **Attack Boost:** +20% (1.2x multiplier)
- **Speed Boost:** +50% (1.5x multiplier)  
- **Critical Hit Rate:** 100% (guaranteed on all moves)
- **Duration:** First turn only after switch-in

### Affected Moves
- **Critical Hits:** All offensive moves that can normally crit
- **Attack Boost:** All physical moves benefit from the Attack increase
- **Speed Boost:** Affects turn order and speed-based calculations

### Interactions with Other Abilities/Mechanics
- **Stacks with other stat boosts:** The 20% Attack boost applies before other multipliers
- **Speed boost affects turn order:** Can allow slower Pokemon to outspeed opponents
- **Critical hits bypass defensive boosts:** Ignores opponent's Defense/Special Defense stat increases
- **Works with held items:** Scope Lens, Lucky Punch, etc. are redundant for crit rate but may still provide other benefits
- **Compatible with move effects:** Works with high-crit moves, but they're already guaranteed to crit

### Strategic Implications
- **Wallbreaker Role:** Guaranteed crits ignore defensive setups like Reflect/Light Screen effects on damage calculation
- **Revenge Killer:** Speed boost allows revenge killing faster threats
- **Lead Potential:** Devastating opening turn can force immediate switches
- **Momentum Control:** Can break through defensive cores with guaranteed critical damage

### Example Damage Calculations
**Scenario:** Level 50 Pokemon with 252 Attack EVs using a 100 Base Power move

**Without Showdown Mode:**
- Base Attack: ~200
- Move Power: 100
- Damage: ~Normal damage calculation

**With Showdown Mode:**
- Base Attack: ~240 (200 x 1.2)
- Move Power: 100
- Critical Hit: 1.5x damage multiplier
- **Total effective multiplier:** 1.8x normal damage (1.2 x 1.5)

### Common Users
Pokemon that benefit most from Showdown Mode typically:
- Have high base Attack stats to maximize the boost
- Appreciate the speed control for revenge killing
- Want to break through defensive teams quickly
- Need help with immediate offensive presence

### Competitive Usage Notes
- **Priority:** Extremely high in offensive team compositions
- **Timing:** Best used as a switch-in against predicted defensive plays
- **Synergy:** Pairs well with Choice items for continued pressure after the first turn
- **Terrain/Weather:** Speed boost can help set up beneficial field conditions

### Counters
- **Ghost-types:** Immune to Normal/Fighting moves that rely on the Attack boost
- **Intimidate:** Can partially offset the Attack boost (-1 stage vs +20% base)
- **Priority Moves:** Can bypass the speed advantage entirely
- **Protect/Detect:** Forces the ability to waste its one-turn window
- **Defensive typing:** Steel/Rock types can still tank even boosted critical hits

### Synergies
- **Choice Band/Specs:** Extends offensive pressure beyond the first turn
- **Life Orb:** Stacks with the Attack boost for maximum damage
- **High base power moves:** Maximizes the critical hit damage
- **Coverage moves:** Ensures super-effective hits with guaranteed crits

### Version History
- Introduced as a combination ability merging Ambush (guaranteed first-turn crits) and Violent Rush (first-turn Attack/Speed boosts)
- Part of Elite Redux's expanded ability system
- Designed to create explosive opening turns for offensive Pokemon
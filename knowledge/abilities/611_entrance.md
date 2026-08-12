---
id: 611
name: Entrance
status: reviewed
character_count: 139
---

# Entrance - Ability ID 611

## In-Game Description
"When this Pokemon confuses an opponent, it simultaneously infatuates all eligible opposing Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user confuses an opponent, it also infatuates them (cuts their Attack and Special Attack in half) if they are the opposite gender. 

## Detailed Mechanical Explanation

**Source Code Location:** `/src/abilities.cc` line 6436-6441

**Core Mechanism:**
```cpp
constexpr Ability Entrance = {
    .onReactive = +[](ON_REACTIVE) -> int { 
        return PoisonPuppeteerClone(ability, battler, CanInfatuate, BattleScript_Entrance); 
    },
    .onBattlerFaints = PoisonPuppeteer.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_OTHER,
    .setStateOnEffect = MOVE_EFFECT_CONFUSION,
};
```

**Trigger Condition:** `MOVE_EFFECT_CONFUSION` - Activates when the user inflicts confusion on any opponent.

**Effect:** Uses `BattleScript_Entrance` which sets `MOVE_EFFECT_ATTRACT` (infatuation) via `PoisonPuppeteerClone`.

### Detailed Mechanics

### Activation Process
1. User inflicts confusion on opponent(s)
2. `PoisonPuppeteerClone` function executes
3. For each confused opponent, checks `CanInfatuate(battler, target)`
4. If infatuation is possible, applies attract effect via `BattleScript_Entrance`

### Target Validation (CanInfatuate function)
- Target must not already be infatuated
- Target must be alive
- Different battlers (cannot infatuate self)
- Gender compatibility:
  - Both Pokemon must have genders (not genderless)
  - Must be opposite genders
- Bypassed by Mycelium Might or Pure Love abilities
- Blocked by status protection abilities

### State Management
- Inherits faint tracking from PoisonPuppeteer
- Removes state flags when tracked opponents faint
- State persists across multiple confusion applications

### Strategic Applications

**Optimal Usage:**
- Multi-target confusion moves (e.g., Supersonic in doubles)
- Status-spreading team compositions
- Control-oriented battle strategies

**Synergistic Moves:**
- Confuse Ray, Supersonic, Sweet Kiss
- Multi-hit confusion moves
- Priority confusion moves

**Competitive Considerations:**
- Powerful in doubles/multi-battles
- Countered by same-gender teams
- Effectiveness reduced by Mental Herb/status immunity


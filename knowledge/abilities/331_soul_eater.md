---
id: 331
name: Soul Eater
status: reviewed
character_count: 102
---

# Soul Eater - Ability ID 331

## In-Game Description
"Dealing a KO heals 1/4 of this Pokemon's max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user knocks out an opponent with a direct hit, it immediately recovers 25% of its maximum HP.

## Detailed Mechanical Explanation

### Implementation Details
- **Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`
- **Condition**: Activates when the Pokemon with Soul Eater knocks out an opponent
- **Effect**: Heals 25% of the user's maximum HP
- **Battle Script**: `BattleScript_HandleSoulEaterEffect`

### Code Implementation
```cpp
constexpr Ability SoulEater = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler));
        CHECK(CanBattlerHeal(battler));
        BattleScriptCall(BattleScript_HandleSoulEaterEffect);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

### Battle Script
```assembly
BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return
BattleScript_HandleSoulEaterEffect_AfterHeal:
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_STACK_1
    datahpupdate BS_STACK_1
    printstring STRINGID_STACKREGAINEDHEALTH
    waitmessage B_WAIT_TIME_LONG
    return
```

## Strategic Analysis

### Strengths
- **Sustain**: Provides excellent longevity in battles through healing
- **Snowball Effect**: Each victory makes the Pokemon harder to defeat
- **Reliable Activation**: Triggers on any knockout, not just specific move types
- **Substantial Healing**: 25% HP recovery is significant

### Limitations
- **Requires Knockouts**: No benefit if the Pokemon can't secure KOs
- **No Effect at Full HP**: Cannot heal beyond maximum HP
- **Single Battle Focus**: Most effective in battles with multiple opponents

### Tactical Applications
- **Sweeper Role**: Ideal for Pokemon designed to sweep through multiple opponents
- **Late Game Power**: Becomes increasingly valuable as battles progress
- **Endurance Battles**: Excellent for longer, drawn-out fights
- **Double/Triple Battles**: More opportunities for knockouts and healing

## Related Abilities
Soul Eater's healing mechanic is shared by several other abilities in the codebase:
- **Blood Bath**: Also uses `SoulEater.onBattlerFaints` for healing
- **Jaws of Carnage**: Uses `BattleScript_HandleJawsOfCarnageEffect` (50% healing)
- **Hunter's Horn**: References the same 25% healing mechanism
- **Various Combination Abilities**: Many abilities incorporate Soul Eater's effect

## Technical Notes
- The ability uses `tryhealpercenthealth` with a 25% value
- Healing is subject to standard battle conditions (can't heal at full HP, must be able to heal)
- The effect bypasses Substitute due to `HITMARKER_IGNORE_SUBSTITUTE`
- Displays the standard "regained health" message after healing
---
id: 222
name: Receiver
status: reviewed
character_count: 90
---

# Receiver - Ability ID 222

## In-Game Description
"In Double Battles, copies its fainting partner's ability."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Receiver copies a fainted ally's ability, replacing Receiver. Persists until switched out.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Receiver is a situational ability that only functions in Double Battles, Multi Battles, and other team-based formats. When an ally Pokemon faints, Receiver triggers and attempts to copy that ally's ability.

### Activation Conditions
- **Battle Format**: Only works in Double Battles, Multi Battles, or other formats with allies
- **Trigger**: An ally Pokemon must faint while the Receiver user is still active
- **Timing**: Activates immediately when the ally faints, before any other end-of-turn effects

### Technical Implementation
```cpp
constexpr Ability Receiver = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        AbilityEnum allyAbility = GetBattlerAbility(fainted);
        CHECK_NOT(IsRolePlayBannedAbility(allyAbility))
        CHECK_NOT(HasAbilityIgnoringSuppression(battler, allyAbility))
        int index = GetAbilityIndex(battler, ability, FALSE);
        CHECK(index < TOTAL_ABILITY_COUNT)

        gBattleMons[battler].abilities[index] = allyAbility;
        gVolatileStructs[battler].switchInAbilityDone[index] = FALSE;

        gBattleScripting.abilityPopupOverwrite = allyAbility;
        BattleScriptCall(BattleScript_ReceiverActivates);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ALLY,
};
```

### Banned Abilities (Cannot Be Copied)
According to `sRolePlayBannedAbilities` array:
- **Trace**: Prevents ability copying loops
- **Wonder Guard**: Too powerful to be copyable
- **Receiver**: Prevents infinite ability copying chains
- **Any persistent/unsuppressable abilities**: Technical limitation

### Ability Replacement Mechanics
- **Elite Redux Multi-Ability System**: Receiver replaces one of the user's current abilities
- **Index Selection**: Uses `GetAbilityIndex()` to determine which ability slot to replace
- **Persistence**: The copied ability remains until the Pokemon switches out
- **Switch-In Effects**: The copied ability can trigger switch-in effects if applicable

### Strategic Implications
- **Team Synergy**: Allows strategic ability sharing between teammates
- **Risk/Reward**: Requires sacrificing an ally to gain their ability
- **Versatility**: Can adapt to different situations based on team composition
- **Doubles Meta**: Primarily useful in competitive doubles formats

### Common Users
- **Kecleon**: Natural user with Color Change synergy
- **Passimian**: Fighting-type with team-oriented movepool

### Competitive Usage Notes
- **Doubles Strategy**: Plan team composition to maximize copied ability value
- **Timing Considerations**: Can be used defensively to save a powerful ability
- **Ability Priority**: Consider which abilities are most valuable to copy
- **Format Limitations**: Useless in Singles format

### Counters
- **Singles Format**: Completely inactive in 1v1 battles
- **Ability Suppression**: Neutralizing Gas, etc. prevent activation
- **Priority Switching**: Removing the Receiver user before allies faint

### Synergies
- **Powerful Abilities**: Copying meta-defining abilities like Intimidate
- **Entry Hazards**: Copying abilities that benefit from switching
- **Weather/Terrain**: Copying setup abilities for field control

### Version History
- Introduced in Generation VII
- Elite Redux implementation allows multi-ability integration
- Enhanced with role-play banning system for balance
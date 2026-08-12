---
id: 36
name: Trace
status: reviewed
character_count: 231
---

# Trace - Ability ID 36

## In-Game Description
"Copies the foe's ability. Does not copy innates."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Copies the ability of an opposing Pokemon when entering battle, replacing itself in the current ability slot. Cannot copy Trace, Wonder Guard, and most form related abilities. In doubles, targets the first valid opponent at random. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**TRACE** is a unique copying ability that replaces itself with an opponent's ability upon switch-in.

### Activation Mechanics:
- **Trigger**: Immediately upon entering battle (onEntry hook)
- **Target Selection**: First checks direct opponent, then their partner if invalid
- **Replacement**: Overwrites the Trace ability in its current slot
- **Message**: "{Pokemon} Traced {Target}'s {Ability}!" followed by copied ability popup
- **Script**: Uses BattleScript_TraceActivatesEnd3 for display

### Target Selection Logic:
1. **Primary Target**: Direct opponent (BATTLE_OPPOSITE position)
2. **Fallback Target**: Opponent's partner if primary is invalid
3. **Validity Check**: Target must be alive and have a traceable ability
4. **Already Has Check**: Cannot copy abilities the user already possesses

### Copying Restrictions:
**Cannot Copy:**
- **Trace itself** (prevents infinite loops)
- **Wonder Guard** (too powerful)
- **Receiver** (ability copying ability)
- **Persistent Abilities** (marked as persistent in ability data)
- **Unsuppressable Abilities** (marked as unsuppressable)
- **Abilities from fainted Pokemon**

### Elite Redux Multi-Ability Integration:
- **Slot Replacement**: Replaces Trace in its current ability slot only
- **Innate Immunity**: Cannot copy innate abilities (only regular abilities)
- **Index Tracking**: Uses GetAbilityIndex to determine which slot to replace
- **State Reset**: Resets switchInAbilityDone flag for the copied ability
- **Ability Activation**: Copied ability can immediately activate if it has onEntry effects

### Interaction Rules:
- **vs Ability Shield**: Blocked by Ability Shield (cannot copy)
- **vs Neutralizing Gas**: Can copy abilities even if currently suppressed
- **vs Multiple Opponents**: In doubles, follows target priority logic
- **Copy Timing**: Occurs before other switch-in abilities activate

### Technical Implementation:
```c
constexpr Ability Trace = {
    .onEntry = +[](ON_ENTRY) -> int {
        int target = BATTLE_OPPOSITE(battler);
        auto newAbility = GetBattlerAbility(target);
        if (!IsBattlerAlive(target) || IsRolePlayBannedAbility(newAbility)) {
            target = BATTLE_PARTNER(target);
            CHECK(IsBattlerAlive(target))
            newAbility = GetBattlerAbility(target);
            CHECK_NOT(IsRolePlayBannedAbility(newAbility))
        }

        CHECK_NOT(HasAbilityIgnoringSuppression(battler, newAbility))

        int index = GetAbilityIndex(battler, ability, FALSE);
        CHECK(index < TOTAL_ABILITY_COUNT)

        gBattleMons[battler].abilities[index] = newAbility;
        gVolatileStructs[battler].switchInAbilityDone[index] = FALSE;

        gStackBattler1 = battler;
        gStackBattler2 = target;
        gBattleScripting.abilityPopupOverwrite = newAbility;
        BattleScriptPushCursorAndCallback(BattleScript_TraceActivatesEnd3);
        return TRUE;
    },
    .randomizerBanned = TRUE,
};
```

### Competitive Notes:
- **Versatility**: Provides access to opponent's key abilities
- **Scouting**: Reveals opponent's ability selection
- **Momentum**: Can gain powerful abilities like Intimidate or weather setting
- **Weakness**: Predictable targeting and slot replacement
- **Synergy**: Best with Pokemon that can utilize diverse abilities effectively

### Common Strategies:
- **Lead Usage**: Copy setup abilities like Drought or Drizzle
- **Revenge Sweeper**: Copy abilities like Moxie or Speed Boost
- **Utility Role**: Copy supportive abilities like Regenerator
- **Counter Strategy**: Copy opponent's key ability to neutralize their plan

### Important Notes:
- **Permanent Change**: Trace ability is lost for the duration of battle
- **Ability Popup**: Shows both Trace activation and copied ability
- **No Recursion**: Multiple Trace users cannot create infinite loops
- **Doubles Complexity**: Target selection follows specific priority rules
- **Version Difference**: Elite Redux's 4-ability system affects which slot gets replaced

### Pokemon with Trace:
- **Abra line** (Abra, Kadabra, Alakazam)
- **Porygon line** (Porygon, Porygon2, Porygon-Z) 
- **Ralts line** (Ralts, Kirlia)
- **Mewtwo forms** (certain variants)

### Version History:
- **Gen 3**: Introduced, permanent weather copying
- **Gen 4-5**: Expanded interaction rules
- **Gen 6+**: Weather duration limits affect copied weather abilities
- **Elite Redux**: 4-ability system integration, innate ability immunity
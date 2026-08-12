---
id: 176
name: Stance Change
status: reviewed
character_count: 268
---

# Stance Change - Ability ID 176

## In-Game Description
"Turns into Blade or Shield form depending on move used."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Changes Aegislash's form based on moves used. Shield form switches to Blade when using damaging moves. Blade switches to Shield with King's Shield. Redux forms swap between physical/special based on move type. Unsuppressable. Form changes occur before attacks execute.

## Detailed Mechanical Explanation
*For Discord/reference use*

**STANCE CHANGE** is Aegislash's signature ability that automatically changes its form based on the moves it uses, altering its stats dramatically.

### Activation Mechanics:
- **Trigger**: Before any attack is executed (onBeforeAttack hook)
- **Unsuppressable**: Cannot be suppressed by Mold Breaker or similar abilities
- **Visual**: Uses BattleScript_AttackerFormChange to show transformation
- **Timing**: Form change completes before the triggering move executes

### Form Changes:

1. **Standard Aegislash Forms**:
   - **Shield Form to Blade Form**: When using any damaging move (power > 0)
   - **Blade Form to Shield Form**: When using King's Shield
   - Shield Form: High defenses (150/150), low offenses (50/50)
   - Blade Form: High offenses (150/150), low defenses (50/50)

2. **Redux Forms (Elite Redux Exclusive)**:
   - **Blade Redux to Shield Redux**: When using physical moves (non-arrow based)
   - **Shield Redux to Blade Redux**: When using special moves or arrow-based moves
   - **Mega Forms**: Follow same pattern as regular Redux forms
   - Redux forms have different stat distributions than standard forms

### Special Mechanics:
- **Arrow Moves**: Always treated as special moves for Redux form determination
- **State Updates**: Properly updates ability state indices when changing forms (UpdateAbilityStateIndicesForNewSpecies)
- **No Change**: Returns FALSE if no valid form change is possible
- **Randomizer**: Cannot be randomly assigned to other Pokemon

### Technical Implementation:
```c
// From abilities.cc line 1899
constexpr Ability StanceChange = {
    .onBeforeAttack = +[](ON_BEFORE_ATTACK) -> int {
        u16 newSpecies = SPECIES_NONE;
        // Complex form change logic based on:
        // - Current species
        // - Move being used (King's Shield vs damaging)
        // - For Redux: Physical vs Special/Arrow moves
        if (newSpecies != SPECIES_NONE) {
            UpdateAbilityStateIndicesForNewSpecies(battler, newSpecies);
            SET_BATTLER_TYPE(battler, gSpeciesInfo[newSpecies].types[0]);
            SET_BATTLER_TYPE2(battler, gSpeciesInfo[newSpecies].types[1]);
            // ... stat recalculation ...
            BattleScriptPushCursorAndCallback(BattleScript_AttackerFormChange);
            return TRUE;
        }
        return FALSE;
    },
};
```

### AI Behavior:
- AI gives +3 score to King's Shield when Aegislash is in Blade form
- Encourages switching back to defensive form before taking hits
- Considers form changes when evaluating move damage

### Competitive Notes:
- Mind games: Opponents must predict whether you'll attack or use King's Shield
- Redux forms add complexity with physical/special split consideration
- Form changes cannot be prevented, making Aegislash uniquely consistent
- Speed tier changes dramatically between forms
- Must balance offensive pressure with defensive positioning

### Pokemon with Stance Change:
- Aegislash (all standard forms)
- Aegislash Redux (all forms)
- Aegislash Mega and Redux Mega forms
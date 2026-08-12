---
id: 16
name: Color Change
status: reviewed
character_count: 155
---

# Color Change - Ability ID 16

## In-Game Description
"Changes type to a resist or an immunity before getting hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transforms the user into the best defensive type before taking damage. Prioritizes immunities over resistances. Only changes to a pure type. Once per turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Color Change has been completely redesigned in Elite Redux. Unlike the original version that changed type AFTER being hit, this version intelligently selects the best defensive type BEFORE taking damage.

Implementation in `src/abilities.cc` (lines 470-495):

```c
constexpr Ability ColorChange = {
    .onBeforeAttack = +[](ON_BEFORE_ATTACK) -> int {
        if (!CheckAndSetOncePerTurnAbility(battler)) return FALSE;
        
        // Search for best defensive type
        u16 bestType = TYPE_NONE;
        u16 bestModifier = UQ_4_12(1.0);
        
        for (u16 type = TYPE_NORMAL; type < NUMBER_OF_MON_TYPES; type++) {
            u16 modifier = GetTypeModifier(move, type);
            if (modifier < bestModifier) {
                bestModifier = modifier;
                bestType = type;
            }
            // Stop if immunity found
            if (modifier == UQ_4_12(0.0)) break;
        }
        
        // Change to best defensive type
        if (bestType != TYPE_NONE && gBattleMons[battler].type1 != bestType) {
            gBattleMons[battler].type1 = bestType;
            gBattleMons[battler].type2 = bestType;
            gBattleMons[battler].type3 = TYPE_MYSTERY;
            BattleScriptPushCursor();
            gBattlescriptCurrInstr = BattleScript_ColorChangeActivated;
            return TRUE;
        }
        return FALSE;
    },
};
```

### Key Features

1. **Activation Timing**: Triggers BEFORE the user gets hit (`onBeforeAttack`)
2. **Once per Turn**: Can only activate once per turn via `CheckAndSetOncePerTurnAbility`
3. **Type Selection Algorithm**:
   - Searches through all possible types
   - Calculates type effectiveness modifier for each type
   - Selects the type with the lowest damage multiplier
   - Prioritizes immunities (0x damage) over resistances

4. **Type Change**: 
   - Changes to pure type (both type slots set to same type)
   - Only changes if not already the optimal type
   - Displays: "{Pokemon}'s ability made it the {Type} type!"

### Defensive Examples
- **Earthquake incoming** to Changes to Flying (immune)
- **Flamethrower incoming** to Changes to Water or Fire (0.5x damage)
- **Close Combat incoming** to Changes to Ghost (immune) or Flying/Psychic (0.5x)
- **Thunder incoming** to Changes to Ground (immune)

### Pokemon with Color Change

In Elite Redux, Color Change appears as an innate ability on:

1. **Kecleon** (the original user):
   - Changeable Abilities: Defeatist, Receiver, Klutz
   - Innate Abilities: Color Change, Protean, Cheap Tactics

2. **Cascoon's Primal Form**:
   - Has Color Change as one of its innate abilities
   - Combined with Impenetrable and Adaptability

### Strategic Implications

**Advantages**:
- **Damage Reduction**: Always takes neutral or reduced damage
- **Immunity Potential**: Can become immune to incoming attacks
- **Defensive Prediction**: Forces opponents to think carefully about move order
- **Type Synergy**: Works well with Protean for both offense and defense

**Disadvantages**:
- **Once per Turn**: Multiple attackers can exploit this limitation
- **Predictability**: Opponents know what type you'll become
- **STAB Loss**: May lose STAB on your moves after changing
- **Status Vulnerability**: Doesn't protect against status effects

### Technical Details
- Battle message defined in `src/battle_message.c`
- Battle script in `data/battle_scripts_1.s`
- AI recognizes the ability and may adjust targeting

### Competitive Usage Notes
- Excellent on bulky Pokemon that can survive multiple hits
- Pairs well with recovery moves to maintain defensive advantage
- Can enable unique defensive cores
- Requires careful team support for offensive pressure

### Counters
- Multi-hit moves (only first hit triggers change)
- Status moves (ability doesn't activate)
- Mixed attackers can hit for at least neutral after change
- Multiple attackers in doubles
- Setup sweepers (if Color Change user lacks offense)

### Synergies
- **Protean**: Offensive and defensive type manipulation
- **Recovery moves**: Maximize defensive type advantages
- **Entry hazard removal**: Maintain HP for multiple activations
- **Substitute**: Prevent ability activation to maintain offensive type

### Version History
This is a complete reimagining of Color Change for Elite Redux:
- **Original**: Changed type to match the move that hit it AFTER taking damage
- **Elite Redux**: Preemptively changes to the best defensive type BEFORE damage

This transformation makes Color Change a powerful defensive tool rather than the largely detrimental ability it was originally.
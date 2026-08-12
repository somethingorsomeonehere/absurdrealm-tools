---
id: 307
name: Self Sufficient
status: reviewed
character_count: 82
---

# Self Sufficient - Ability ID 307

## In-Game Description
"Recovers 1/16 of max HP at the end of each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Self Sufficient restores 1/16 of the Pokemon's maximum HP at the end of each turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Heals 1/16 (6.25%) of maximum HP at the end of each turn
- Minimum healing of 1 HP if calculation results in 0
- Triggers during the end turn phase after all other effects

**Activation Conditions:**
- Pokemon must not be at full HP
- Pokemon must be able to heal (not blocked by Heal Block, Bleed status, etc.)
- Does not activate on the first turn after switching in (`isFirstTurn != 2` check)
- Pokemon must be alive

**Technical Implementation:**
```cpp
constexpr Ability SelfSufficient = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(gVolatileStructs[battler].isFirstTurn != 2)

        gBattleMoveDamage = gBattleMons[battler].maxHP / 16;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        gBattleMoveDamage *= -1;
        BattleScriptPushCursorAndCallback(BattleScript_SelfSufficientActivates);
        return TRUE;
    },
};
```

**Healing Prevention:**
Self Sufficient will not activate when:
- Heal Block is active on the Pokemon
- Pokemon has Bleed status condition
- Blood Stain field effect is active
- Opposing Pokemon has Permanence ability
- Pokemon is poisoned and opponent has Hemolysis ability

**Interactions with Other Abilities/Mechanics:**
- **Big Root**: Does not affect Self Sufficient healing (only affects draining moves)
- **Poison Heal**: Overrides Self Sufficient when poisoned - Pokemon will heal from poison instead
- **Magic Guard**: Self Sufficient healing works normally with Magic Guard
- **Leftovers**: Stacks with Self Sufficient for 1/16 + 1/16 = 1/8 total healing per turn
- **Ingrain/Aqua Ring**: Can stack with Self Sufficient for multiple sources of healing

**Strategic Implications:**
- Excellent for defensive/stall Pokemon that need consistent recovery
- Pairs well with defensive moves like Protect, Substitute, and Toxic
- Valuable for Pokemon with high HP stats to maximize healing amount
- Provides sustainability without requiring specific weather or terrain
- Helps counter passive damage from status conditions, entry hazards, or recoil

**Example Damage Calculations:**
- 404 HP Pokemon: 404 ÷ 16 = 25.25 to 25 HP healed per turn
- 200 HP Pokemon: 200 ÷ 16 = 12.5 to 12 HP healed per turn
- 50 HP Pokemon: 50 ÷ 16 = 3.125 to 3 HP healed per turn
- 10 HP Pokemon: 10 ÷ 16 = 0.625 to 1 HP healed per turn (minimum)

**Common Users:**
Based on the codebase, Pokemon with Self Sufficient include:
- Various defensive Pokemon in trainer teams
- Pokemon that also have access to Shadow Tag and Soul Eater
- Poison-type Pokemon that can also have Poison Touch and Regenerator

**Competitive Usage Notes:**
- Strong on bulky Pokemon that can take hits and benefit from gradual recovery
- Synergizes with defensive movesets and stall strategies
- Less effective on frail Pokemon due to lower HP pools
- Provides consistent value throughout long battles

**Counters:**
- Heal Block (prevents all healing)
- Taunt (prevents defensive moves that synergize with healing)
- Strong offensive pressure that outdamages the healing
- Status conditions that deal percentage damage (Poison, Burn)
- Entry hazards that chip away at health

**Synergies:**
- **Defensive moves**: Protect, Substitute, Recover
- **Status moves**: Toxic, Thunder Wave, Will-O-Wisp
- **Items**: Leftovers (stacks), Rocky Helmet, Assault Vest
- **Abilities**: Can be combined with other abilities in Elite Redux's multi-ability system

**Version History:**
- Added as ability ID 307 in Elite Redux
- Used as base healing effect for combo abilities like Self Repair (Self Sufficient + Natural Cure) and Apple Pie
- Referenced by Peaceful Slumber ability for enhanced healing calculations

**Related Abilities:**
- **Self Repair**: Combines Self Sufficient healing with Natural Cure status removal
- **Apple Pie**: Uses identical healing to Self Sufficient
- **Peaceful Slumber**: Enhanced version that combines Sweet Dreams and Self Sufficient effects
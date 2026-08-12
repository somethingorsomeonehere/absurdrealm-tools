---
id: 50
name: Run Away
status: reviewed
character_count: 199
---

# Run Away - Ability ID 50

## In-Game Description
"Guarantees fleeing. Raises Speed if stats lowered by an enemy."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guarantees successful escape from wild Pokemon battles regardless of speed differences. When any of the user's stats are lowered by an opponent's move or ability, raises the user's Speed by 2 stages.

## Detailed Mechanical Explanation
*For Discord/reference use*

**RUN AWAY** is a dual-purpose utility ability that provides guaranteed escape from wild battles and defensive stat boost mechanics in trainer battles.

### Escape Mechanics:
- **Wild Battle Effect**: Guarantees 100% success when attempting to flee from wild Pokemon encounters
- **Override Speed**: Bypasses normal speed-based flee calculations entirely
- **Special Locations**: 
  - In Battle Pyramid: Still uses modified speed calculation but with additional bonuses
  - Trainer Battles: Escape mechanics don't apply (trainer battles prevent fleeing regardless)
  - Link Battles: Escape mechanics don't apply

### Stat Boost Mechanics:
- **Trigger**: When any stat is lowered by an opponent's move or ability
- **Effect**: Raises user's Speed by 2 stages (+100% speed at +2)
- **Activation Message**: Shows ability popup and "{Pokemon}'s Speed rose sharply!" message
- **Stage Limit**: Will not activate if Speed is already at maximum (+6 stages)
- **Counter Mechanics**: Similar to Defiant/Competitive but specifically for Speed

### Affected Stat Lowering Sources:
1. **Moves**: Growl, Leer, Intimidate, String Shot, etc.
2. **Abilities**: Intimidate (Attack drop), Sticky Web (Speed drop), etc.
3. **Items**: King's Rock/Razor Fang secondary effects, etc.
4. **NOT triggered by**: Self-inflicted stat drops (Close Combat, Superpower, etc.)

### Technical Implementation:
```c
// Escape functionality in TryRunFromBattle()
else if (BattlerHasAbility(battler, ABILITY_RUN_AWAY, FALSE)) {
    if (InBattlePyramid()) {
        // Special pyramid calculation with bonuses
        speedVar = (speed * multiplier) / opponentSpeed + (tries * 30);
        if (speedVar > (Random() & 0xFF)) {
            SetActiveAbilityPopupOverride(ABILITY_RUN_AWAY);
            gRoundStructs[battler].fleeFlag = 2;
            effect++;
        }
    } else {
        // Guaranteed success in normal wild battles
        SetActiveAbilityPopupOverride(ABILITY_RUN_AWAY);
        gRoundStructs[battler].fleeFlag = 2;
        effect++;
    }
}

// Stat boost functionality in TryToApplyMimicry()
if (stringId == STRINGID_DEFENDERSSTATFELL && 
    BATTLER_HAS_ABILITY(gBattlerTarget, ABILITY_RUN_AWAY)) {
    gBattleScripting.abilityPopupOverwrite = ABILITY_RUN_AWAY;
    gBattlerAbility = gBattlerTarget;
    BattleScriptCall(BattleScript_RunAwayActivates);
}

// Battle Script (BattleScript_RunAwayActivates)
jumpifstat BS_ABILITY_BATTLER, CMP_EQUAL, STAT_SPEED, MAX_STAT_STAGE, End
setstatchanger STAT_SPEED, 2, FALSE
goto BattleScript_DefiantActivates_Effect
```

### AI Considerations:
- **AI Rating**: 0 (lowest priority - considered weak competitively)
- **Stat Drop Immunity**: AI recognizes Run Away users benefit from stat drops
- **Escape Prevention**: AI knows Run Away bypasses trapping moves in wild battles

### Interaction Rules:
- **vs Trapping**: Overrides Mean Look, Block, Arena Trap in wild battles only
- **vs Ghost Types**: Works alongside Ghost-type natural flee ability
- **vs Shed Shell**: Stacks with Shed Shell's escape properties
- **Immunity Abilities**: Clear Body, White Smoke prevent the stat drop but won't trigger Run Away's boost
- **Contrary**: If user has Contrary, stat "drops" become raises and won't trigger Run Away

### Competitive Analysis:
**Strengths:**
- Punishes stat-drop strategies with speed boosts
- Provides utility in catching wild Pokemon (guaranteed escape to heal/restock)
- Unexpected momentum against Intimidate users

**Weaknesses:**
- Very situational competitive use
- Doesn't prevent the initial stat drop
- Speed boost may not be immediately useful
- AI rates it as lowest priority ability

**Common Users:**
- Furret (main ability choice in trainer teams)
- Linoone (hidden ability option)
- Ambipom (hidden ability option)
- Often used as an innate ability on Normal-type specialists

### Synergies and Counters:
**Synergies:**
- Works well with speed-based sweepers who can capitalize on the boost
- Pairs with Choice Scarf for immediate speed tier jumping
- Benefits Pokemon with strong priority moves after speed boost

**Counters:**
- Clear Body/White Smoke prevent stat drops (no trigger)
- Taunt prevents stat-dropping moves
- Priority moves bypass speed advantage
- Abilities like Unaware ignore speed boosts in damage calculation

### Version History:
- Gen 3-4: Escape-only ability
- Gen 5+: No additional effects in most games
- Elite Redux: Added defensive stat boost mechanic, making it competitively relevant

### Usage Examples:
1. **Wild Encounter**: Player wants to flee from strong wild Pokemon - Run Away guarantees success
2. **Intimidate Counter**: Opponent switches in Intimidate user to Run Away activates to Speed +2, potentially outspeeding revenge killers
3. **Sticky Web Response**: Entry hazard lowers Speed to Run Away triggers to Net result is +1 Speed instead of -1

**Note**: Run Away is currently missing from the main abilities array in `abilities.cc` but has full battle logic implementation. The ability functions properly through the battle system's ability checking mechanisms.
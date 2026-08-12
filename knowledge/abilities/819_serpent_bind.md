---
id: 819
name: Serpent Bind (N)
status: reviewed
character_count: 173
---

# Serpent Bind (N) - Ability ID 819

## In-Game Description
"50% chance to trap, then drop the their speed by -1 each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Gives attacks a 50% chance to trap the target for 4-5 turns, preventing escape or switching. Once trapped, their speed drops by one stage each turn they remain on the field. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Trigger**: On successful attack against a target
- **Activation Chance**: 50% per attack that connects
- **Trap Effect**: Applies `STATUS2_ESCAPE_PREVENTION` to the target
- **Speed Reduction**: Reduces target's speed stat stage by 1 each turn while trapped
- **Duration**: Persists until the user faints or switches out

### Implementation Status
**CURRENTLY NOT IMPLEMENTED** - The ability exists in the codebase as a placeholder:
```cpp
constexpr Ability SerpentBind = {
    .breakable = TRUE,
};
```

### Expected Implementation Pattern
Based on similar abilities in the codebase, the implementation would likely follow this pattern:

```cpp
constexpr Ability SerpentBind = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(gBattleMoves[move].power) // Only on damaging moves
        CHECK(Random() % 100 < 50) // 50% chance
        CHECK_NOT(gBattleMons[target].status2 & STATUS2_ESCAPE_PREVENTION) // Not already trapped
        
        gBattleMons[target].status2 |= STATUS2_ESCAPE_PREVENTION;
        gVolatileStructs[target].battlerPreventingEscape = battler;
        BattleScriptCall(BattleScript_AnnounceTargetTrapped);
        return TRUE;
    },
    .onEndTurn = +[](ON_END_TURN) -> int {
        // Check for trapped opponents and reduce their speed
        int any = FALSE;
        for (int target = 0; target < gBattlersCount; target++) {
            FILTER(IsBattlerAlive(target))
            FILTER(gBattleMons[target].status2 & STATUS2_ESCAPE_PREVENTION)
            FILTER(gVolatileStructs[target].battlerPreventingEscape == battler)
            FILTER(CanLowerStat(target, STAT_SPEED))
            
            gBattlerTarget = target;
            AbilityStatusEffect(MOVE_EFFECT_SPEED_MINUS_1);
            any = TRUE;
        }
        return any;
    },
    .breakable = TRUE,
};
```

### Technical Details
- **Trap Mechanism**: Uses the same system as Mean Look, Block, and Arena Trap
- **Speed Reduction**: Applied via `MOVE_EFFECT_SPEED_MINUS_1` status effect
- **Stat Stage Range**: Speed can be reduced to minimum (-6 stages)
- **Breakable**: Can be suppressed by Mold Breaker, Teravolt, Turboblaze

### Interactions with Other Mechanics

#### Escape Prevention Interactions
- **Ghost-types**: In Gen 6+, Ghost-types can escape from most trapping effects
- **Shed Shell**: Holders can switch out despite being trapped
- **Run Away**: Allows the holder to always flee from wild Pokemon
- **U-turn/Volt Switch**: May still allow switching despite trap status

#### Speed Reduction Interactions
- **Contrary**: Would reverse the speed drop into a speed boost
- **Mirror Armor**: Would reflect the speed drop back to the user
- **Clear Body/White Smoke**: Prevents the speed reduction
- **Minimum Stage**: Speed reduction stops at -6 stages

### Strategic Applications

#### Offensive Use
- **Stat Pressure**: Forces opponents into increasingly disadvantageous speed tiers
- **Setup Prevention**: Prevents opponents from switching to answers
- **Endgame Control**: Eliminates opponent switching options late in battle

#### Defensive Use
- **Revenge Killing**: Trapped, slowed opponents become easier targets
- **Entry Hazard Support**: Forces opponents to take Stealth Rock damage repeatedly
- **Status Support**: Combines well with poison/burn for gradual KOs

### Counters and Answers

#### Direct Counters
- **Shed Shell**: Complete immunity to the trapping effect
- **Ghost-types**: Natural escape ability in most generations
- **Magic Bounce**: Reflects the initial trap attempt
- **Substitute**: May block the initial trapping attempt

#### Stat Protection
- **Clear Body family**: Prevents speed reduction entirely
- **Contrary**: Turns speed drops into speed boosts
- **White Herb**: Resets negative stat changes once per battle
- **Lum Berry**: May cure some associated status conditions

### Competitive Usage Notes

#### Tier Assessment
- **Viability**: High - Combines board control with stat pressure
- **Usage Niche**: Anti-meta positioning against switch-heavy teams
- **Synergy Requirements**: Benefits from speed control and entry hazards

#### Common Users
Based on the (N) designation, this would be an innate ability, so specific Pokemon would naturally possess it rather than it being distributed widely.

#### Team Support
- **Entry Hazards**: Stealth Rock, Spikes force repeated damage
- **Status Moves**: Toxic, Will-O-Wisp for additional pressure
- **Priority Moves**: Compensate for reduced speed tiers
- **U-turn/Volt Switch**: Maintain momentum despite binding

### Version History
- **Elite Redux**: Introduced as ability ID 819
- **Current Status**: Placeholder implementation only
- **Implementation Priority**: Requires full coding of trap + stat reduction mechanics

### Related Abilities
- **Salt Circle**: Similar trapping mechanism on entry
- **Arena Trap**: Pure trapping without stat modification
- **Mean Look**: Move-based equivalent of trapping effect
- **Speed Boost**: Opposite effect (speed increases over time)

### Notes for Developers
- The description contains a typo: "drop the their speed" should be "drop their speed"
- Implementation would require both `onAttacker` and `onEndTurn` callbacks
- Should respect existing trap immunity mechanics (Ghost-types, Shed Shell)
- Speed reduction should follow standard stat stage modification rules
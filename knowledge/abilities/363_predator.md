---
id: 363
name: Predator
status: reviewed
character_count: 102
---

# Predator - Ability ID 363

## In-Game Description
"Dealing a KO heals 1/4 of this Pokemon's max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When the user knocks out an opponent with a direct hit, it immediately recovers 25% of its maximum HP.

## Detailed Mechanical Explanation

### Implementation Details
- **Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`
- **Condition**: Activates when the Pokemon with Predator knocks out an opponent
- **Effect**: Heals 25% of the user's maximum HP
- **Battle Script**: `BattleScript_HandleSoulEaterEffect`
- **Code Location**: Line 3800-3803 in `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`

### Code Implementation
```cpp
constexpr Ability Predator = {
    .onBattlerFaints = SoulEater.onBattlerFaints,
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
- **Consistent Healing**: Provides reliable HP recovery after each knockout
- **Sustain Ability**: Excellent for sweeping through multiple opponents
- **Momentum Maintenance**: Keeps the Pokemon healthy for extended battles
- **No Type Restrictions**: Works with any damaging move that secures a KO
- **Substantial Recovery**: 25% HP is a significant amount of healing

### Limitations
- **Requires Knockouts**: No benefit if the Pokemon cannot secure eliminations
- **No Effect at Full HP**: Cannot heal beyond maximum HP
- **Single Battle Limitation**: Less effective in 1v1 scenarios
- **Depends on Offensive Power**: Requires the ability to actually knock out opponents

### Tactical Applications
- **Sweeper Role**: Ideal for Pokemon designed to eliminate multiple opponents
- **Late Game Sustain**: Becomes increasingly valuable as battles progress
- **Multi-Battle Scenarios**: Excellent for Battle Tower, Elite Four, and similar formats
- **Team Support**: Allows the Pokemon to stay healthy for longer team contributions

## Pokemon Distribution

Based on the proto data analysis, Predator is distributed across **85+ Pokemon** in Elite Redux, appearing as both regular abilities and innate abilities. This wide distribution suggests it's a popular ability for creating sustainable offensive threats.

### Notable Distribution Patterns
- **Mixed Usage**: Appears as both regular and innate abilities
- **Diverse Types**: Found across various Pokemon types and roles
- **Widespread Availability**: One of the more commonly distributed abilities in the game

## Related Abilities

### Direct Relatives
- **Soul Eater (331)**: Identical effect - Predator uses Soul Eater's implementation
- **Looter (365)**: Also uses Soul Eater's healing mechanism
- **Jaws of Carnage (438)**: Similar concept but heals 50% instead of 25%

### Combination Abilities
- **Apex Predator (486)**: "Tough Claws + Predator" - combines contact move boost with healing
- **Magma Eater (467)**: "Predator + Molten Down" - combines healing with entry hazard setting

### Comparable Abilities
- **Scavenger (345)**: Heals 1/3 HP on KO but has additional effects
- **Hunter's Horn (464)**: References similar healing mechanics

## Technical Notes

### Healing Mechanics
- Uses `tryhealpercenthealth` with 25% value
- Healing is subject to standard battle conditions
- Cannot heal if already at maximum HP
- Requires the Pokemon to be able to heal (not affected by Heal Block, etc.)

### Battle System Integration
- Effect bypasses Substitute due to `HITMARKER_IGNORE_SUBSTITUTE`
- Displays standard "regained health" message
- Triggers after the knockout is confirmed
- Works with any move that deals the final damage

### Competitive Implications
- **Tier Impact**: Makes many Pokemon more viable as sweepers
- **Meta Influence**: Encourages aggressive, offensive playstyles
- **Synergy Potential**: Excellent with high-damage moves and setup sweepers
- **Counterplay**: Can be countered by preventing knockouts or using priority moves

## Conclusion

Predator is a straightforward but powerful ability that transforms many Pokemon into sustainable offensive threats. Its wide distribution and reliable healing make it a cornerstone ability for sweep-oriented strategies in Elite Redux. The ability's simplicity belies its effectiveness, providing consistent value in any battle scenario where knockouts are achievable.
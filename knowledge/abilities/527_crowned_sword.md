---
id: 527
name: Crowned Sword
status: reviewed
character_count: 165
---

# Crowned Sword - Ability ID 527

## In-Game Description
"Intrepid Sword + Anger Point."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises Attack by 1 stage upon switching in. When hit, raises the user's Attack by 1 stage or maximizes it on critical hits. Activates on each hit of a multihit move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Crowned Sword is a hybrid ability that combines two distinct attack-boosting effects: an entry boost (Intrepid Sword) and a reactive boost system (Anger Point). This creates a powerful offensive ability that gains momentum both proactively and reactively.

### Component Abilities

#### Intrepid Sword Component
- **Entry effect**: Automatically raises Attack by 1 stage when switching in
- **Timing**: Activates immediately upon entering battle
- **Conditions**: No special conditions required
- **Message**: Displays standard stat raise message

#### Anger Point Component  
- **Trigger**: Activates when the Pokemon takes damage from any attack
- **Normal hits**: Raises Attack by 1 stage
- **Critical hits**: Maximizes Attack stat (+12 stages, equivalent to +6 effective stages)
- **Timing**: Activates after damage calculation but before end of turn

### Technical Implementation
```c
constexpr Ability CrownedSword = {
    .onEntry = IntrepidSword.onEntry,     // +1 Attack on switch-in
    .onDefender = AngerPoint.onDefender,  // +1 Attack when hit, +12 on crit
};

// IntrepidSword component
.onEntry = +[](ON_ENTRY) -> int {
    CHECK(CanRaiseStat(battler, STAT_ATK))
    SetStatChanger(STAT_ATK, 1);
    BattleScriptPushCursorAndCallback(BattleScript_BattlerAbilityStatRaiseOnSwitchIn);
    return TRUE;
}

// AngerPoint component  
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(battler))
    CHECK(CanRaiseStat(battler, STAT_ATK))
    
    if (gIsCriticalHit) {
        SetStatChanger(STAT_ATK, 12);  // Max out Attack
        BattleScriptCall(BattleScript_TargetsStatWasMaxedOut);
    } else {
        SetStatChanger(STAT_ATK, 1);   // +1 stage
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
    }
    return TRUE;
}
```

### Activation Conditions
- **Entry boost**: Triggers automatically on switch-in, switch-out doesn't require damage
- **Hit response**: Requires taking damage from an opponent's attack
- **Stat check**: Must be able to raise Attack stat (not at +6 for normal hits)
- **Critical hit exception**: Can exceed +6 Attack limit when hit by critical hits

### Important Interactions
- **Substitute**: Anger Point component doesn't activate if protected by Substitute
- **Focus Sash/Sturdy**: Still triggers even if damage is reduced to 1 HP
- **Multi-hit moves**: Each hit can potentially trigger the Anger Point effect
- **Ability suppression**: Neither component works if ability is suppressed
- **Stat resets**: Entry boost reapplies if switched out and back in

### Strategic Implications
- **Immediate pressure**: Enters with +1 Attack, threatening from turn 1
- **Snowball potential**: Each hit makes the Pokemon more dangerous
- **Critical hit punishment**: Opponents risk giving massive Attack boosts
- **Switch advantage**: Gain momentum on every switch-in
- **Defensive pivot**: Can absorb hits while gaining offensive power

### Current Users
- **Zacian-Crowned-Sword**: The signature Pokemon with this ability
  - Base 170 Attack becomes 255 (effectively 340) with +1
  - Paired with innate abilities: Steelworker, Battle Armor, Keen Edge
  - Fairy/Steel typing with excellent coverage

### Competitive Usage Notes
- **Entry hazard synergy**: Can switch in multiple times for repeated boosts
- **Intimidate counter**: Neutralizes some Intimidate disadvantage
- **Risk/reward**: Taking hits becomes beneficial rather than purely negative
- **Critical hit fishing**: Opponents may avoid high-crit moves against this ability
- **Revenge killing**: Dangerous to attempt due to Attack boost on contact

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas, Gastro Acid
- **Stat reset**: Haze, Clear Smog, switching out
- **Substitute**: Blocks the Anger Point component (but not entry boost)
- **Non-damaging moves**: Status moves don't trigger the reactive boost
- **Special attacks**: Can avoid giving Attack boosts while dealing damage
- **Priority moves**: Can potentially KO before boosts become threatening

### Synergies
- **Battle Armor/Shell Armor**: Prevents critical hits that would max Attack
- **Keen Edge**: Increased critical hit ratio pairs with potential max Attack
- **Choice items**: Immediate power boost makes Choice Band/Scarf more effective
- **Steelworker**: Zacian's innate ability boosts Steel-type moves further
- **Speed control**: Paralysis, Trick Room can help utilize Attack boosts

### Comparison to Component Abilities
- **vs Intrepid Sword**: Adds reactive boosting to the entry boost
- **vs Anger Point**: Adds guaranteed entry boost to the reactive system  
- **Combined effect**: Creates consistent offensive pressure regardless of opponent's strategy
- **Unique advantage**: Only ability that guarantees Attack boost on entry AND reactive boosts

### Version History
- Elite Redux exclusive ability
- Signature ability of Zacian-Crowned-Sword form
- Represents the fusion of defensive adaptation (Anger Point) with offensive presence (Intrepid Sword)
- Part of the legendary signature ability design philosophy in Elite Redux
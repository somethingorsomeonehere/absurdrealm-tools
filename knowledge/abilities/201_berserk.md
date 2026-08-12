---
id: 201
name: Berserk
status: reviewed
character_count: 298
---

# Berserk - Ability ID 201

## In-Game Description
"Boosts highest attack by +1 when at 1/2 of max HP or lower."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Berserk activates when the Pokemon drops to half HP or below from an opposing attack, boosting its highest attacking stat by one stage. Includes stat stages to determine which gets boosted. Triggers only once per battle. Other damage sources that bring you to half HP or below will not activate it.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Berserk is an offensive ability that provides a stat boost when the Pokemon reaches critical HP levels. It activates when the Pokemon's HP drops from above half to at or below half HP, providing a one-stage boost to whichever attacking stat is higher.

### Activation Conditions
- **HP threshold**: Must drop from above 50% HP to 50% HP or below in a single turn
- **Stat selection**: Automatically chooses between Attack and Special Attack
  - Compares current Attack vs Special Attack including stat stage modifications
  - Boosts whichever stat is currently higher
- **One-time trigger**: Can only activate once per battle per Pokemon
- **Damage source**: Works with any damage that brings HP to the threshold
  - Contact moves (Tackle, Punch moves)
  - Non-contact moves (Thunderbolt, Surf)
  - Entry hazards (Stealth Rock, Spikes)
  - Weather damage (Sandstorm, Hail)
  - Status damage (Burn, Poison)

### Technical Implementation
```c
// Berserk triggers when dropping to half HP
constexpr Ability Berserk = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(CheckHalfHpAbility(battler, attacker))  // HP threshold check
        CHECK_NOT(GetAbilityState(battler, ability))  // One-time use check
        int stat = GetHighestAttackingStatId(battler, TRUE);  // Choose stat
        CHECK(CanRaiseStat(battler, stat))  // Verify boost possible
        
        SetAbilityState(battler, ability, TRUE);  // Mark as used
        SetStatChanger(stat, 1);  // +1 stage boost
        BattleScriptCall(BattleScript_TargetAbilityStatRaiseOnMoveEnd);
        return TRUE;
    },
};
```

### Stat Selection Logic
The ability uses `GetHighestAttackingStatId(battler, TRUE)` which:
- Compares current Attack and Special Attack values
- **Includes stat stage modifications** in the comparison
- Returns STAT_ATK or STAT_SPATK based on which is higher
- In case of ties, defaults to Attack

### Important Interactions
- **Multi-hit moves**: Only triggers on the hit that brings HP below threshold
- **Substitute**: Does not activate if damage is absorbed by Substitute
- **Ability suppression**: Cannot activate if ability is suppressed (Mold Breaker, etc.)
- **Stat boost prevention**: Blocked by Clear Body, White Smoke, and similar abilities
- **Taunt/Torment**: Not affected by move-restricting conditions
- **One-time nature**: State persists even through switching and fainting

### HP Threshold Mechanics
The `CheckHalfHpAbility` function requires:
- `gBattleStruct->hpBefore[battlerDef] > maxHP / 2` (was above half)
- `gBattleMons[battlerDef].hp <= maxHP / 2` (now at or below half)
- Not triggered during multi-hit move subsequent hits
- Must be a legitimate hit that affects the Pokemon

### Strategic Implications
- **Late-game sweeper**: Becomes dangerous when low on HP
- **Pivot potential**: Can be intentionally brought to low HP for setup
- **Stat stage stacking**: Boost stacks with other stat increases
- **Type coverage**: Boosts either physical or special depending on build
- **Prediction element**: Opponents must be careful about bringing it to activation range

### Synergistic Strategies
- **Focus Sash**: Guarantees survival to activate against strong attacks
- **Sitrus Berry/Berry Juice**: Can heal above threshold to potentially re-trigger
- **Belly Drum**: Self-damage to activate, though extreme
- **Pain Split**: Manipulate HP to activation range
- **Substitute**: Protect while at low HP to capitalize on boost
- **Choice items**: Maximize damage output after boost

### Pokemon Usage Context
Based on trainer data analysis, Berserk appears on:
- Physical attackers who benefit from Attack boosts
- Mixed attackers who can utilize either stat boost
- Pokemon with good bulk to survive reaching activation threshold
- Mon with access to priority moves to leverage the boost

### Competitive Analysis
**Strengths:**
- Provides significant late-game power spike
- Automatic activation requires no setup
- Chooses optimal stat intelligently
- Cannot be easily prevented once threshold is reached

**Weaknesses:**
- Requires taking significant damage to activate
- One-time use limits impact
- May activate on the "wrong" stat if opponent manipulates stages
- Vulnerable to being KO'd before capitalizing on boost

### Counters and Counterplay
- **OHKO strategies**: Prevent activation by avoiding the HP threshold
- **Stat stage manipulation**: Lower their attacking stats to influence selection
- **Ability changing**: Worry Seed, Simple Beam to replace ability
- **Haze/Clear Smog**: Remove stat boosts after activation
- **Intimidate**: Can influence which stat gets boosted

### Similar Abilities Comparison
- **Anger Point**: Requires critical hit, gives +6 Attack specifically
- **Defiant/Competitive**: Trigger on stat reduction, not HP threshold
- **Berserk DNA (ID 529)**: Entry-based boost with confusion drawback
- **Berserker Rage (ID 480)**: Combines Tipping Point + Rampage effects

### Version History
- Original Pokemon ability introduced in Generation VII
- In Elite Redux: Maintained core mechanics with stat selection intelligence
- Benefits from Elite Redux's expanded stat calculation system
- State tracking ensures proper one-time activation per battle

### Technical Notes
- Uses battle state tracking to prevent multiple activations
- Integrates with Elite Redux's enhanced stat stage system
- Compatible with all damage types and sources
- Properly handles edge cases like exact 50% HP scenarios
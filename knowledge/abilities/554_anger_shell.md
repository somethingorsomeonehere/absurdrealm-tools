---
id: 554
name: Anger Shell
status: reviewed
character_count: 265
---

# Anger Shell - Ability ID 554

## In-Game Description
"Applies Shell Smash when reduced below 1/2 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When dropping to below 50% HP, the user triggers Shell Smash effects: raising Attack, Special Attack, and Speed by 2 stages each while lowering Defense and Special Defense by 1 stage each. Only activates once per battle. Activates at the last hit of multihit moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Triggers when HP drops from above 50% to below 50% in a single hit
- Applies identical stat changes to the Shell Smash move
- Only activates once per battle encounter (ability state is set to prevent re-triggering)

**Activation Conditions:**
- Must have HP above 50% before taking damage
- Must have HP below 50% after taking damage  
- Must be hit by an attack (not passive damage)
- Must not be on the last hit of a multi-hit move
- At least one offensive stat (Attack/Special Attack/Speed) must be raiseable
- Cannot be prevented by abilities like Clear Body

**Stat Changes Applied:**
```
Attack: +2 stages
Special Attack: +2 stages  
Speed: +2 stages
Defense: -1 stage
Special Defense: -1 stage
```

**Technical Implementation:**
```c
constexpr Ability AngerShell = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(CheckHalfHpAbility(battler, attacker))
        CHECK_NOT(GetAbilityState(battler, ability))
        CHECK(CanRaiseStat(battler, STAT_ATK) || CanRaiseStat(battler, STAT_SPATK) || CanRaiseStat(battler, STAT_SPEED))

        SetAbilityState(battler, ability, TRUE);
        BattleScriptCall(BattleScript_AngerShell);
        return TRUE;
    },
};
```

**Interactions:**
- Works with substitute (checks actual HP, not substitute HP)
- Cannot be suppressed by abilities like Gastro Acid once triggered
- Stat changes can still be prevented by Clear Body, White Smoke, etc.
- Does not activate from self-inflicted damage or recoil
- Compatible with Contrary (would invert the stat changes)

**Strategic Implications:**
- Transforms defensive Pokemon into immediate offensive threats
- Risk/reward mechanic - trading bulk for power when weakened
- Excellent on Pokemon with recovery moves to repeatedly threaten the threshold
- Pairs well with Focus Sash or Sturdy to guarantee survival

**Common Users:**
- Coalossal (Fire/Rock type with defensive stats)
- Various Rock-type Pokemon with high defensive stats

**Competitive Usage:**
- Strong in formats where taking damage is inevitable
- Creates immediate pressure when Pokemon reaches low HP
- Forces opponents to either finish the Pokemon quickly or face a boosted sweeper
- Excellent comeback mechanic for bulky offensive Pokemon

**Counters:**
- Multi-hit moves (won't trigger on final hit)
- Status moves that don't deal damage
- Abilities that prevent stat changes (Clear Body, White Smoke)
- Priority moves to finish off weakened Pokemon
- Phasing moves (Roar, Whirlwind) to remove stat boosts

**Synergies:**
- Recovery moves (Recover, Roost) to repeatedly threaten the threshold
- Focus Sash/Sturdy to guarantee survival and activation
- Shell Bell/Leftovers for passive recovery
- Moves that benefit from multiple stat boosts (mixed attackers)

**Version History:**
- Introduced in Elite Redux as ability ID 554
- Based on Shell Smash move mechanics from Generation V
- Functions as a defensive ability that becomes offensive under pressure
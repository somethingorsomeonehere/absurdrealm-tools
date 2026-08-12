---
id: 599
name: Dead Power
status: reviewed
character_count: 238
---

# Dead Power - Ability ID 599

## In-Game Description
"1.5x Attack boost. 20% chance to curse on contact moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the user's Attack stat by 50% and 20% chance to inflict curse on contact moves. Curse inflicts 25% max HP damage per turn until the cursed Pokemon switches out or faints. The Attack boost is multiplicative with other damage boosts.

## Detailed Mechanical Explanation

### Implementation Details

### Core Mechanics
From `src/abilities.cc`:
```cpp
constexpr Ability DeadPower = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK_NOT(gBattleMons[target].status2 & STATUS2_CURSED)
        CHECK(IsMoveMakingContact(move, battler))
        CHECK(Random() % 100 < 20)

        return AbilityStatusEffect(MOVE_EFFECT_CURSE);
    },
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_ATK) *stat *= 1.5;
        },
};
```

### Proto Definition
From `proto/AbilityList.textproto`:
```
id: ABILITY_DEAD_POWER
name: "Dead Power"
description: "1.5x Attack boost. 20% chance to curse on contact moves."
```

### Detailed Analysis

### Attack Boost Component
- **Effect**: 1.5x multiplier to Attack stat
- **Timing**: Passive stat modification
- **Application**: Affects all physical moves, not just contact moves
- **Stacking**: Does not stack with other Attack boosts multiplicatively

### Curse Contact Component
- **Trigger**: Contact moves only (moves that make physical contact)
- **Chance**: 20% per hit (Random() % 100 < 20)
- **Condition**: Target must not already be cursed
- **Effect**: Applies curse status (STATUS2_CURSED)

### Curse Status Effect
From `src/battle_util.c`:
```c
case ENDTURN_CURSE:  // curse
    if (((gBattleMons[gActiveBattler].status2 & STATUS2_CURSED) || IsBattlerCursed(gActiveBattler)) && gBattleMons[gActiveBattler].hp != 0) {
        MAGIC_GUARD_CHECK;
        gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 4;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        BattleScriptExecute(BattleScript_CurseTurnDmg);
        effect++;
    }
```

**Curse Mechanics:**
- **Damage**: 25% of max HP per turn (maxHP / 4)
- **Timing**: End of turn
- **Minimum**: At least 1 HP damage if calculation rounds to 0
- **Interaction**: Blocked by Magic Guard ability
- **Duration**: Permanent until switched out or cured

### Strategic Applications

### Offensive Synergy
1. **Physical Sweeper Setup**: 1.5x Attack boost makes physical moves significantly stronger
2. **Contact Move Priority**: Favor contact moves to trigger curse effect
3. **Sustained Pressure**: Curse provides ongoing damage even after switching

### Contact vs Non-Contact Moves
**Contact Moves (Trigger Curse):**
- Tackle, Body Slam, Double-Edge
- Punch moves (Fire Punch, Ice Punch, etc.)
- Bite, Crunch
- Most physical moves that involve direct contact

**Non-Contact Moves (No Curse):**
- Rock Slide, Earthquake
- Projectile moves like Rock Throw
- Most ranged physical attacks

### Team Synergy
1. **Pivot Support**: Switch in to apply curse, then pivot out
2. **Wallbreaker Role**: High Attack boost breaks through defensive walls
3. **Status Spreading**: Curse multiple targets across the battle

### Comparative Analysis

### Similar Abilities
- **Poison Touch**: 30% poison chance on contact (vs 20% curse)
- **Static**: 30% paralysis chance on contact
- **Flame Body**: 30% burn chance on contact

### Unique Aspects
1. **Dual Benefit**: Both immediate (Attack boost) and delayed (curse) effects
2. **Severe Punishment**: 25% max HP per turn is extremely threatening
3. **Permanent Effect**: Curse persists until cured or switched

### Competitive Viability

### Strengths
- **Immediate Power**: 1.5x Attack makes all physical moves significantly stronger
- **Long-term Pressure**: Curse forces switches or threatens KO
- **Versatile Application**: Works with any contact move
- **Meta Pressure**: Forces opponents to carry curse cures or accept damage

### Limitations
- **Contact Dependency**: Non-contact moves don't trigger curse
- **RNG Dependent**: 20% chance means inconsistent curse application
- **Already Cursed Check**: Cannot stack curse or reapply
- **Switch Vulnerability**: Curse clears on switch out

### Ideal Pokemon Types
1. **High Attack Physical Attackers**: Maximize the Attack boost
2. **Contact Move Users**: Pokemon with strong contact movesets
3. **Bulky Attackers**: Can stay in to apply multiple curse attempts
4. **Pivot Pokemon**: Apply curse then switch for team support

### Code Integration Notes

### Implementation Pattern
- Uses standard `ON_ATTACKER` hook for contact-based effects
- Uses `ON_STAT` hook for stat modifications
- Follows established patterns from other contact abilities (Static, Poison Touch)

### Status Interaction
- Checks for existing curse status before applying
- Uses `AbilityStatusEffect(MOVE_EFFECT_CURSE)` for application
- Integrates with battle's end-turn damage calculation system

### Technical Considerations
- **Random Number Generation**: Uses standard `Random() % 100` for chance calculation
- **Status Flags**: Uses STATUS2_CURSED bit flag (1 << 28)
- **Damage Calculation**: Follows consistent end-turn damage patterns

This ability represents a powerful combination of immediate offensive pressure and long-term strategic advantage, making it highly valuable for physical attackers in competitive play.
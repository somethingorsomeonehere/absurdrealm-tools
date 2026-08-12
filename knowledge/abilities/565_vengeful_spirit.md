---
id: 565
name: Vengeful Spirit
status: reviewed
character_count: 269
---

# Vengeful Spirit - Ability ID 565

## In-Game Description
"Haunted Spirit + Vengeance."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Curses the attacker when knocked out by a direct hit. The curse inflicts 25% max HP damage per turn until the cursed Pokemon switches out or faints. Ghost-type attackers are immune to the curse. Boosts the power of Ghost-type moves by 30%, or by 50% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

Vengeful Spirit is a powerful combination ability that merges two distinct effects:

### Haunted Spirit Component (.onDefender)
- **Trigger**: When the Pokemon is KO'd by a contact move
- **Effect**: Applies Curse status to the attacker (STATUS2_CURSED)
- **Damage**: Cursed Pokemon lose 1/4 of their max HP each turn
- **Immunities**: 
  - Ghost-type attackers are immune
  - Attackers already cursed are immune
- **Contact Requirement**: Only works against moves that make contact

### Vengeance Component (.onOffensiveMultiplier)
- **Trigger**: When using Ghost-type moves at low HP
- **Condition**: Pokemon must be at 1/3 HP or less
- **Effect**: 1.5x damage multiplier for Ghost-type moves
- **Implementation**: Uses SWARM_MULTIPLIER(TYPE_GHOST) macro

### Technical Implementation
```cpp
constexpr Ability VengefulSpirit = {
    .onDefender = HauntedSpirit.onDefender,
    .onOffensiveMultiplier = Vengeance.onOffensiveMultiplier,
};
```

The HauntedSpirit.onDefender function:
```cpp
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(attacker))
    CHECK_NOT(IsBattlerAlive(battler))
    CHECK_NOT(IS_BATTLER_OF_TYPE(attacker, TYPE_GHOST))
    CHECK_NOT(gBattleMons[attacker].status2 & STATUS2_CURSED)
    CHECK(IsMoveMakingContact(move, attacker))

    gBattleMons[attacker].status2 |= STATUS2_CURSED;
    BattleScriptCall(BattleScript_HauntedSpiritActivated);
    return TRUE;
},
```

The Vengeance.onOffensiveMultiplier uses SWARM_MULTIPLIER:
```cpp
#define SWARM_MULTIPLIER(type)                                               \
    +[](ON_OFFENSIVE_MULTIPLIER) {                                           \
        if (moveType == type) {                                              \
            if (gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)) \
                MUL(1.5);                                                    \
        }                                                                    \
    }
```

### Competitive Applications
1. **Defensive Punishment**: Deters physical attackers from making contact
2. **Revenge Kills**: Low HP Ghost moves become extremely powerful
3. **Pivot Potential**: Forces opponents to choose between curse damage or switching
4. **Ghost-type Synergy**: Pairs excellently with Ghost-type movesets
5. **Anti-Physical**: Specifically counters contact-based physical attackers

### Strategic Usage
- **Setup Sweepers**: Can threaten curse while setting up
- **Revenge Killers**: Becomes dangerous when brought in at low HP
- **Pivot Pokemon**: Forces difficult decisions for opponents
- **Wall Breakers**: Low HP Ghost moves can break through defensive cores
- **End Game**: Curse damage can secure late-game victories

### Notable Interactions
- **Magic Guard**: Prevents curse damage to Magic Guard users
- **Ghost-types**: Immune to the curse effect but not the damage boost
- **Non-contact moves**: Bypass the curse effect entirely
- **Status moves**: Don't trigger the offensive multiplier
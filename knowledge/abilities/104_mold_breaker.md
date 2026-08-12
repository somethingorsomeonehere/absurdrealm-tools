---
id: 104
name: Mold Breaker
status: reviewed
character_count: 172
---

# Mold Breaker - Ability ID 104

## In-Game Description
"Moves hit through abilities. Also affects innates."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Allows moves to ignore the target's abilities and innates that interfere with effects or reduce damage. Does not bypass abilities that modify base stats such as Grass Pelt.

## Detailed Mechanical Explanation
*For Discord/reference use*

**MOLD BREAKER** is an ability-negation ability that allows the user's moves to bypass most defensive and protective abilities on the target.

### Activation Mechanics:
- **Trigger**: Automatically active when the Pokemon with Mold Breaker uses any move
- **Switch-in Message**: "{Pokemon} breaks the mold!" (B_MSG_SWITCHIN_MOLDBREAKER)
- **Scope**: Affects both regular abilities and all three innate ability slots in Elite Redux's 4-ability system
- **Flag**: Sets HITMARKER_MOLD_BREAKER for the duration of the move

### Core Mechanics:
Mold Breaker works by suppressing the target's abilities during move execution through the `IsSuppressed()` function:

```c
int IsSuppressed(int battler, AbilityEnum ability, int checkMoldBreaker) {
    if ((checkMoldBreaker && battler != gBattlerAttacker && gHitMarker & HITMARKER_MOLD_BREAKER && gAbilities[ability].breakable) ||
        ((gFieldTimers.neutralizingGas || gStatuses3[battler] & STATUS3_GASTRO_ACID) && !IsUnsuppressableAbility(ability))) {
        return !DoesBattlerHaveAbilityShield(battler);
    }
    return FALSE;
}
```

### Conditions for Mold Breaker Activation:
The `ShouldSetMoldBreaker()` function determines when abilities are ignored:

1. **Mold Breaker Family**: ABILITY_MOLD_BREAKER, ABILITY_TERAVOLT, ABILITY_TURBOBLAZE
2. **Move-Specific**: Moves with FLAG_TARGET_ABILITY_IGNORED flag
3. **Special Cases**: 
   - ABILITY_BLIND_RAGE
   - ABILITY_MYCELIUM_MIGHT (status moves only)
   - Steel-type monotype champion (vs player)

### Abilities That Can Be Ignored (breakable = TRUE):
- **Defensive**: Battle Armor, Shell Armor, Sturdy, Filter, Solid Rock, Multiscale
- **Type Immunities**: Levitate, Flash Fire, Water Absorb, Volt Absorb, Sap Sipper
- **Status Immunities**: Limber, Insomnia, Water Veil, Magma Armor, Immunity, Own Tempo
- **Stat Protection**: Clear Body, White Smoke, Keen Eye, Hyper Cutter
- **Weather/Terrain**: Thick Fat, Heatproof, Overcoat, Sand Veil, Snow Cloak
- **Accuracy/Evasion**: Tangled Feet, Compound Eyes, Wonder Skin
- **Contact Effects**: Effect Spore, Static, Flame Body, Poison Point
- **Move Effects**: Soundproof, Bulletproof, Dazzling, Queenly Majesty

### Abilities That CANNOT Be Ignored:
- **Unsuppressable**: Neutralizing Gas, Comatose, Multitype, RKS System
- **Non-breakable**: Magic Guard, Wonder Guard, Air Lock, Cloud Nine
- **Protective Items**: Ability Shield holders are immune to suppression

### Elite Redux 4-Ability System Impact:
Mold Breaker is particularly powerful in Elite Redux because it can suppress:
- **Slot 0**: Changeable ability (standard ability slot)  
- **Slot 1**: First innate ability
- **Slot 2**: Second innate ability
- **Slot 3**: Third innate ability

This means Pokemon that rely on multiple defensive abilities for bulk can be completely bypassed.

### Technical Implementation:
```c
constexpr Ability MoldBreaker = {
    .onEntry = +[](ON_ENTRY) -> int { return SwitchInAnnounce(B_MSG_SWITCHIN_MOLDBREAKER); },
};
```

The ability itself has no special functionality beyond the switch-in message. The actual effect is implemented in the battle system's ability checking functions.

### Example Interactions:
- **vs Levitate**: Ground moves hit normally
- **vs Water Absorb**: Water moves deal damage instead of healing
- **vs Filter/Solid Rock**: Super effective moves deal full damage
- **vs Sturdy**: One-hit KO moves and moves that would leave 1 HP work normally
- **vs Magic Guard**: Still blocks indirect damage (ability not breakable)

### Strategic Applications:
1. **Wall Breaking**: Bypasses defensive abilities like Filter, Multiscale
2. **Type Coverage**: Ignores type-based immunities like Levitate, Flash Fire
3. **Setup Prevention**: Bypasses abilities that trigger on contact or damage
4. **Guaranteed Effects**: Move secondary effects work through Shield Dust

### Common Users in Elite Redux:
Based on the species data, Mold Breaker appears on many powerful physical attackers and some special attackers, often as an innate ability or choice ability.

### Counters:
- **Ability Shield**: Completely prevents ability suppression
- **Non-breakable abilities**: Magic Guard, Wonder Guard still function
- **Switching**: Opponent can switch to non-ability-reliant Pokemon
- **Priority moves**: Can KO before Mold Breaker user attacks

### Synergies:
- **High Attack**: Maximizes damage when bypassing defensive abilities
- **Super effective moves**: Especially effective when ignoring Filter/Solid Rock
- **Status moves**: Can inflict status through immunity abilities
- **Contact moves**: Ignore contact-based defensive abilities

### Competitive Usage Notes:
Mold Breaker is considered one of the most valuable abilities in Elite Redux due to the prevalence of multiple defensive abilities on most Pokemon. It's particularly effective in higher difficulty tiers where opponents stack defensive abilities.

### Version History:
- **Gen 4+**: Original implementation
- **Elite Redux**: Extended to affect all four ability slots, making it significantly more powerful than in standard games
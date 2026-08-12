---
id: 559
name: Guilt Trip
status: reviewed
character_count: 149
---

# Guilt Trip - Ability ID 559

## In-Game Description
"Sharply lowers attacker's Attack and SpAtk when fainting."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The attacker that delivers the final blow on the user drops their Attack and Special Attack by 2 stages. Only works when fainting from direct damage.

## Detailed Mechanical Explanation
*For Discord/reference use*

Guilt Trip is a posthumous punishment ability that activates when the Pokemon with this ability faints from a direct attack.

### Core Mechanics
- **Trigger**: When the Pokemon with Guilt Trip faints from taking damage
- **Effect**: Lowers the attacker's Attack and Special Attack by 2 stages each
- **Target**: The battler that dealt the finishing blow
- **Timing**: Activates immediately after fainting

### Activation Conditions
1. The Pokemon with Guilt Trip must faint (HP reduced to 0)
2. The fainting must be caused by a direct attack from an opponent
3. The attacker must still be alive on the field
4. The attacker must be capable of having their stats lowered (not at minimum -6 stages)

### Technical Implementation
```cpp
constexpr Ability GuiltTrip = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(attacker))
        CHECK_NOT(IsBattlerAlive(battler))  // Ability holder faints
        CHECK(CanLowerStat(attacker, STAT_ATK) || CanLowerStat(attacker, STAT_SPATK))

        BattleScriptCall(BattleScript_GuiltTrip);
        return TRUE;
    },
};
```

The battle script performs the stat reductions:
```asm
BattleScript_GuiltTrip::
    playstatchangeanimation BS_ATTACKER, BIT_ATK | BIT_SPATK, STAT_CHANGE_NEGATIVE | STAT_CHANGE_BY_TWO | STAT_CHANGE_MULTIPLE_STATS
    setstatchanger STAT_ATK, 2, TRUE     @ Lower Attack by 2 stages
    statbuffchange STAT_BUFF_ALLOW_PTR | MOVE_EFFECT_AFFECTS_USER, BattleScript_GuiltTripTrySpAtk
    setstatchanger STAT_SPATK, 2, TRUE   @ Lower Sp. Attack by 2 stages  
    statbuffchange STAT_BUFF_ALLOW_PTR | MOVE_EFFECT_AFFECTS_USER, BattleScript_GuiltTripEnd
```

### Stat Stage Impact
- **"Sharply lowers"** = -2 stages to both Attack and Special Attack
- Attack stages: 100% to 67% to 50% to 40% to 33% to 29% to 25%
- At -2 stages: Attacker deals 50% of normal physical damage
- At -2 stages: Attacker deals 50% of normal special damage

### Interactions with Other Abilities/Items
**Blocked by:**
- Clear Body, White Smoke, Full Metal Body (prevent stat reduction)
- Hyper Cutter (prevents Attack reduction only)
- Keen Eye (doesn't prevent Attack/Sp. Attack reduction)

**Enhanced by:**
- Contrary (would boost attacker's stats instead of lowering them)

**Not affected by:**
- Substitute (ability activates even if behind Substitute)
- Magic Bounce (cannot reflect posthumous effects)

### Moves That Don't Trigger Guilt Trip
- Indirect damage (poison, burn, weather, entry hazards)
- Recoil damage to the ability holder
- Confusion self-damage
- Destiny Bond (since both Pokemon faint simultaneously)

### Strategic Applications
**Defensive Strategy:**
- Perfect for bulky support Pokemon that expect to faint
- Forces attackers to think twice about finishing off the Guilt Trip user
- Excellent on Pokemon with low offensive stats but good defensive utility

**Team Synergy:**
- Pairs well with revival moves (Revival Blessing, Wish)
- Works on switch-in revenge killers and Choice item users
- Particularly effective against physical/special sweepers

**Common Users in Elite Redux:**
- Various bulky support Pokemon across different tiers
- Often found on Pokemon with other defensive abilities
- Frequently paired with healing/utility movesets

### Competitive Usage Notes
**Pros:**
- Guaranteed activation if opponent KOs with direct damage
- Significant offensive debuff (-50% damage output)
- No opportunity cost - activates passively on fainting
- Cannot be prevented by most standard means

**Cons:**
- Requires the Pokemon to faint to activate
- No benefit if the Pokemon survives the battle
- Useless against opponents using indirect damage to finish
- Some abilities can prevent or reverse the stat drops

### Counters
**Direct Counters:**
- Stat drop immunity abilities (Clear Body, White Smoke, etc.)
- Haze, Clear Smog to reset stat changes
- Contrary ability users (though rare)

**Play Around Strategies:**
- Use indirect damage for the KO (Toxic, burn, hazards)
- Switch immediately after KOing to avoid the debuff
- Use Pokemon that don't rely heavily on Attack/Sp. Attack

### Version History
- Added in Elite Redux as a custom ability
- Designed as a defensive/support ability for tanky Pokemon
- Part of the expanded ability roster beyond Generation 9
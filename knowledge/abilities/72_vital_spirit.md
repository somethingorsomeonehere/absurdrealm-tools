---
id: 72
name: Vital Spirit
status: reviewed
character_count: 155
---

# Vital Spirit - Ability ID 72

## In-Game Description
"Can't fall asleep. Fighting-type moves heal status."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Immune to sleep. When the Pokemon uses a Fighting-type move, it heals all status conditions immediately after the move resolves. Removes sleep when gained. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**VITAL SPIRIT** is a defensive ability that provides sleep immunity and status healing through Fighting-type moves.

### Core Mechanics:
1. **Sleep Immunity**: Completely immune to sleep status
   - Prevents Sleep, Yawn-induced sleep, and Rest-induced sleep
   - Automatically removes sleep status if gained through ability changes
   - Works even if ability is gained mid-battle

2. **Fighting-Type Healing**: Using any Fighting-type move heals all status conditions
   - Triggers on: All direct damage Fighting moves, status Fighting moves, and multi-hit Fighting moves
   - Heals: Poison, Toxic Poison, Burn, Paralysis, Freeze, Frostbite, Bleed, Sleep
   - Also removes: Nightmare status
   - Shows ability popup and status cure message

3. **Taunt Immunity**: Cannot be affected by Taunt
   - Can use status moves even when opponent uses Taunt
   - Particularly valuable for support Fighting-types

### Activation Rules:
- **Sleep Prevention**: Passive, always active (onStatusImmune hook)
- **Status Healing**: Only when using Fighting-type moves (onAttacker hook)
- **Taunt Immunity**: Passive, always active (tauntImmune flag)
- **Ability Properties**: Breakable by Mold Breaker, but removesStatusOnImmunity = TRUE

### Technical Implementation:
```c
constexpr Ability VitalSpirit = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(moveType == TYPE_FIGHTING)
        CHECK(AbilityHealMonStatus(battler, ability));
        return TRUE;
    },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_SLEEP)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
    .tauntImmune = TRUE,
};
```

### Strategic Applications:

**Offensive Sets**:
- Fighting-type attackers can maintain momentum without status interruption
- Taunt immunity allows setup moves like Bulk Up or Swords Dance
- Particularly strong on mixed attackers using status moves

**Defensive Sets**:
- Sleep immunity prevents rest stalling and sleep powder strategies
- Status healing through Fighting moves creates unique defensive utility
- Taunt immunity preserves access to recovery and support moves

**Notable Users**:
- **Mankey/Primeape**: Early game sleep immunity with fighting STAB
- **Hitmonlee/Hitmonchan/Hitmontop**: All have innate Vital Spirit, can cure status reliably
- **Electabuzz/Electivire**: Innate ability, synergizes with fighting coverage moves
- **Heracross**: Mega form has innate Vital Spirit with powerful fighting moves
- **Timburr line**: Construction workers immune to sleep, fighting STAB for healing
- **Blissey Redux**: Unusual defensive user with fighting coverage for status cure

### Interaction Notes:
- **vs Sleep Moves**: Completely immune (Sleep Powder, Spore, Hypnosis, Dark Void, etc.)
- **vs Yawn**: Immune to the delayed sleep effect
- **vs Rest**: Cannot use Rest (immunity prevents the sleep component)
- **vs Status**: All major status conditions can be healed through Fighting moves
- **vs Mold Breaker**: Ability can be suppressed, losing all immunities and healing
- **vs Taunt**: Completely immune, can still use status moves freely

### Competitive Viability:
**Strengths**:
- Reliable status immunity and healing creates longevity
- Taunt immunity provides utility that many Fighting-types lack
- Works well on both offensive and defensive sets
- Cannot be bypassed by most sleep-inducing strategies

**Weaknesses**:
- Requires Fighting-type moves to access the healing benefit
- Mold Breaker completely negates the ability
- No direct combat benefits beyond status management
- Fighting-type requirement may limit moveset flexibility

### Version Notes:
- Elite Redux enhancement: Added Fighting-type move healing and Taunt immunity
- Original: Only provided sleep immunity (like Insomnia)
- The healing mechanic uses the same function as Shed Skin but triggers on Fighting moves instead of randomly
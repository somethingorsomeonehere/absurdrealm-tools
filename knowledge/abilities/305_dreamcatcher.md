---
id: 305
name: Dreamcatcher
status: reviewed
character_count: 273
---

# Dreamcatcher - Ability ID 305

## In-Game Description
"Doubles move power if anyone on the field is asleep."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Dreamcatcher doubles the power of the user's moves when any Pokemon on the field is asleep. This includes the user, allies, or opponents. Attacks hit sleeping foes who are switching out for 1x power instead, damaging them before leaving. Does not activate against Comatose.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Effect**: Doubles move power (2.0x multiplier) when any battler on the field has sleep status
- **Activation**: Checks all 4 battle positions for sleep status before each attack
- **Scope**: Global battlefield check - affects user's moves regardless of who is asleep

### Activation Conditions
- Any Pokemon on the battlefield must have `STATUS1_SLEEP` status
- Includes natural sleep from moves like Sleep Powder, Spore, Sing
- Includes self-induced sleep from Rest
- Works with Comatose ability (permanent sleep-like status)
- Checks all battlers: user, partner (doubles), and both opponents

### Technical Implementation
```cpp
constexpr Ability Dreamcatcher = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            for (int i = 0; i < gBattlersCount; i++) {
                if (IsBattlerAlive(i) && gBattleMons[i].status1 & STATUS1_SLEEP) {
                    MUL(2.0);
                    return;
                }
            }
        },
};
```

### Move Interactions
- **All Move Types**: Works with Physical, Special, and Status moves that deal damage
- **Priority Moves**: Boost applies to Quick Attack, Extreme Speed, etc.
- **Multi-Hit Moves**: Each hit receives the 2x boost
- **Fixed Damage Moves**: Does NOT boost moves like Seismic Toss, Night Shade
- **OHKO Moves**: Does NOT boost Guillotine, Fissure, etc.

### Ability Interactions
- **Comatose**: Permanent activation since Comatose counts as sleep status
- **Insomnia/Vital Spirit**: These prevent sleep but don't interfere if others are asleep
- **Early Bird**: Reduces sleep duration but ability still works while asleep
- **Bad Dreams**: Synergizes well - damages sleeping foes while boosting your attacks

### Strategic Applications
- **Self-Activation**: Use Rest to put yourself to sleep for guaranteed activation
- **Team Support**: Partner uses sleep moves to enable Dreamcatcher user
- **Revenge Killing**: Punish opponents who use Rest or get put to sleep
- **Doubles Strategy**: More opportunities for sleep status with 4 battlers

### Example Damage Calculations
Base 100 power move with Dreamcatcher active:
- Normal: 100 power
- With Dreamcatcher: 200 power
- With Dreamcatcher + Life Orb: 200 x 1.3 = 260 power
- With Dreamcatcher + STAB: 200 x 1.5 = 300 power

### Common Users
**Primary Ability Holders:**
- **Natu**: Psychic/Flying type with access to supportive moves
- **Munna**: Psychic type that can learn sleep-inducing moves
- **Sigilyph**: Fast special attacker with diverse movepool
- **Lunatone**: Rock/Psychic with good special attack
- **Shiinotic**: Grass/Fairy with access to Spore

**Innate Ability (Fixed):**
- **Darkrai**: Has Dreamcatcher as innate alongside Bad Dreams
- **Cresselia**: Powerful defensive Pokemon with reliable activation
- Various other Psychic-types as innate ability

### Competitive Usage Notes
- **Tier Placement**: Varies by user, but generally increases viability significantly
- **Usage Rate**: Moderate - situational but powerful when active
- **Synergy Rating**: High with sleep support, self-sleep strategies
- **Threat Level**: High when active - forces opponents to avoid sleep entirely

### Counters and Limitations
**Direct Counters:**
- **Insomnia/Vital Spirit**: Prevents sleep on the user but doesn't stop ability if others sleep
- **Lum Berry/Chesto Berry**: Quick sleep removal
- **Aromatherapy/Heal Bell**: Team-wide status cure
- **Magic Bounce**: Reflects sleep moves back

**Strategic Counters:**
- Avoid using Rest or sleep-inducing moves
- Priority sleep removal (Lum Berry users)
- Fast Taunt to prevent Rest setup
- Substitute to block sleep moves

**Limitations:**
- Requires sleep status to be present on field
- Only works on damage-dealing moves
- Can be unreliable without setup
- Opponent can wake up and remove the boost

### Synergistic Abilities and Items
**Abilities:**
- **Comatose**: Permanent sleep status for guaranteed activation
- **Synchronize**: Can spread sleep status when inflicted
- **Bad Dreams**: Damage sleeping opponents while boosting own attacks
- **Early Bird**: Reduces sleep time but still allows temporary activation

**Items:**
- **Lum Berry**: Self-sleep with Rest, then wake up next turn
- **Life Orb**: Stacks with Dreamcatcher for massive damage
- **Choice Items**: Locked into one move but with doubled power
- **Sleep Talk**: Use random moves while asleep (if self-sleeping)

### Version History and Development
- **Introduction**: Added in Elite Redux as custom ability #305
- **Design Philosophy**: High-risk, high-reward ability encouraging sleep-based strategies
- **Balance Notes**: 2x multiplier is significant but requires setup or luck
- **Interaction Updates**: Works properly with all sleep sources and Comatose

### Advanced Strategies
1. **Rest + Sleep Talk**: Put yourself to sleep, use random boosted moves
2. **Doubles Sleep Support**: Partner uses Spore while user attacks with doubled power
3. **Comatose Synergy**: Permanent activation on Pokemon with both abilities
4. **Revenge Sleep**: Punish opponents who Rest by immediately attacking with 2x power
5. **Status Spreading**: Use Synchronize to potentially put opponents to sleep via contact

This ability transforms sleep from a liability into a powerful offensive tool, creating unique strategic opportunities and forcing opponents to reconsider their status move usage.
---
id: 275
name: Rampage
status: reviewed
character_count: 98
---

# Rampage - Ability ID 275

## In-Game Description
"No recharge after a KO, if it usually would need to recharge."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Rampage eliminates recharge turns when the user successfully KOs an opponent with a direct attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Rampage is a powerful ability that removes the recharge limitation from moves with the `EFFECT_RECHARGE` mechanic when the user successfully KOs an opponent.

### Activation Conditions
- The Pokemon with Rampage must use a move that normally requires recharge (Hyper Beam, Giga Impact)
- The move must successfully KO the target
- When both conditions are met, the recharge requirement is completely removed

### Technical Implementation
```cpp
constexpr Ability Rampage = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        SetAbilityState(battler, ability, TRUE);
        gVolatileStructs[battler].rechargeTimer = 0;
        gBattleMons[battler].status2 &= ~(STATUS2_RECHARGE);
        return FALSE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

The ability triggers when an opponent faints and:
1. Sets the recharge timer to 0
2. Removes the `STATUS2_RECHARGE` flag
3. Allows the user to act normally on the next turn

### Affected Moves
Currently in Elite Redux, only two moves have the `EFFECT_RECHARGE` mechanic:
- **Hyper Beam** (Special, 150 BP, Normal-type)
- **Giga Impact** (Physical, 150 BP, Normal-type)

### Normal Recharge Mechanics
Without Rampage, recharge moves work as follows:
- Move hits and deals damage
- User gains `STATUS2_RECHARGE` status
- `rechargeTimer` is set to 2 turns
- User cannot act on the following turn
- Recharge status is removed after the forced rest turn

### Strategic Implications
- **Late-game sweeping**: Excellent for cleaning up weakened teams
- **Momentum preservation**: Maintains offensive pressure without vulnerability windows
- **Risk management**: Allows safe use of powerful moves when securing KOs
- **Team positioning**: Works best when opponents are already in KO range

### Example Scenarios
1. **Successful KO**: Dragonite uses Hyper Beam to KOs opponent to Can act immediately next turn
2. **Failed KO**: Dragonite uses Hyper Beam to Opponent survives to Must recharge next turn
3. **Multi-KO potential**: With proper setup, can chain multiple Hyper Beams without recharge

### Interactions with Other Mechanics
- **Choice items**: Still locked into the same move, but no recharge penalty
- **Parental Bond**: Each hit can potentially trigger Rampage if it secures a KO
- **Life Orb**: Recoil damage still applies, but no recharge if KO is secured
- **Substitute**: Does not interfere with Rampage activation

### Common Users in Elite Redux
Notable Pokemon that can have Rampage:
- **Nidoking**: Physical/Special mixed attacker with Sheer Force synergy
- **Aerodactyl**: High-speed physical sweeper with Rock Head
- **Gyarados**: Intimidate support with late-game sweep potential
- **Dragonite**: Multiple forms with Multiscale and Overwhelm support
- **Cranidos**: Early-game physical powerhouse with Sheer Force
- **Genesect**: Legendary with Neuroforce and Beast Boost synergy
- **Blissey**: Unexpected special tank with Pixilate and Magic Bounce

### Competitive Usage Notes
- **Tier placement**: Primarily found on Tier 2-3 Pokemon for balance
- **Role compression**: Allows bulky attackers to also serve as late-game cleaners
- **Meta positioning**: Counters defensive stall strategies
- **Speed requirements**: Most effective on naturally fast Pokemon or with speed control

### Counters and Counterplay
- **Residual damage**: Sandstorm, Toxic, etc. can prevent clean KOs
- **Focus Sash/Sturdy**: Prevents one-shot KOs that would trigger Rampage
- **Substitute**: Blocks the initial attack and prevents KO
- **Priority moves**: Can revenge kill before Rampage user acts again
- **Status conditions**: Sleep, paralysis can limit follow-up potential

### Synergies
- **Life Orb**: Increased damage helps secure KOs despite recoil
- **Choice Band/Specs**: Massive power increase for guaranteed KOs
- **Moxie**: Attack boosts stack with Rampage for increasing sweep potential
- **Dragon Dance/Nasty Plot**: Setup sweeping becomes more reliable
- **Multiscale/Sturdy**: Defensive abilities help survive to use powerful moves

### Version History
- Added in Elite Redux as part of the expanded ability system
- Designed to make recharge moves more viable in competitive play
- Currently paired with various legendary and pseudo-legendary Pokemon
- Balanced by limiting to specific Pokemon rather than reducing the effect
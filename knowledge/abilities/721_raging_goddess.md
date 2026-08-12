---
id: 721
name: Raging Goddess 
status: reviewed
character_count: 255
---

# Raging Goddess - Ability ID 721

## In-Game Description
"Rampage + Hyper Aggressive."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Eliminates recharge turns when the user successfully KOs an opponent with a direct attack. Makes all attacks hit twice in succession. The first hit deals 100%, while the second hit deals 25%. Each hit rolls secondary effects independently (except flinch).


## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Raging Goddess is a combination ability that merges the effects of Rampage and Hyper Aggressive, making it one of the most powerful offensive abilities in Elite Redux. It provides both multi-hit capabilities and recharge elimination.

### Component Abilities

#### Rampage Component 
- **Recharge elimination**: When this Pokemon knocks out an opponent with a move that normally requires recharge (like Hyper Beam, Blast Burn, etc.), the recharge requirement is completely eliminated
- **Timing**: Activates immediately when the opponent faints from the attack
- **Effect**: Sets `gVolatileStructs[battler].rechargeTimer = 0` and clears `STATUS2_RECHARGE`

#### Hyper Aggressive Component
- **Multi-hit mechanic**: All moves hit twice using the Parental Bond system
- **First hit**: 100% power (full damage)  
- **Second hit**: 25% power (quarter damage)
- **Hit count**: Always exactly 2 hits per move

### Technical Implementation
```cpp
// From src/abilities.cc
constexpr Ability RagingGoddess = {
    .onBattlerFaints = Rampage.onBattlerFaints,
    .onParentalBond = ParentalBond.onParentalBond,
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};

// Rampage effect - eliminates recharge on KO
.onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
    SetAbilityState(battler, ability, TRUE);
    gVolatileStructs[battler].rechargeTimer = 0;
    gBattleMons[battler].status2 &= ~(STATUS2_RECHARGE);
    return FALSE;
},

// Hyper Aggressive effect - double hit
.onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { 
    return PARENTAL_BOND_HYPER_AGGRESSIVE; 
},
```

### Multi-Hit Mechanics Details
- Uses `PARENTAL_BOND_HYPER_AGGRESSIVE` system
- **Hit count**: `GetParentalBondCount()` returns 2
- **Damage calculation**: 
  - Turn 0 (first hit): 100% damage
  - Turn 1 (second hit): `UQ_4_12(0.25)` = 25% damage
- **Total damage**: 125% of original move power per use

### Recharge Move Interactions
**Affected moves include:**
- Hyper Beam, Giga Impact
- Frenzy Plant, Blast Burn, Hydro Cannon
- Rock Wrecker, Roar of Time, Spacial Rend
- Any move with the recharge flag

**Interaction with multi-hit:**
1. Move hits twice (100% + 25% damage)
2. If either hit causes a KO, recharge is eliminated
3. Can immediately use another move next turn

### Strategic Implications
- **Ultimate sweeper ability**: Combines damage multiplication with recharge removal
- **Momentum preservation**: Never gets locked into recharge after securing KOs
- **Devastating with powerful moves**: Hyper Beam becomes a spammable 125% power move with KOs
- **Status move utility**: Even status moves hit twice, doubling success chances
- **Contact move synergy**: Each hit can trigger contact-based effects

### Move Compatibility
**Works with:**
- All damaging moves (hit twice)
- Status moves (applied twice) 
- Single-target and multi-target moves
- Priority moves
- Recharge moves (no recharge on KO)

**Doesn't work with:**
- Multi-hit moves (they don't get additional hits)
- Moves that specifically prevent multi-hit

### Common Strategies
- **Recharge move spam**: Use Hyper Beam/Giga Impact without fear of recharge
- **Sweeping builds**: Focus on high-power moves to secure KOs
- **Status spreading**: Double-chance status moves like Will-O-Wisp
- **Breaking Focus Sash**: Multi-hit breaks through Focus Sash/Sturdy

### Competitive Advantages
- **No recharge vulnerability**: Eliminates the main weakness of powerful moves
- **Effective 125% power**: Every move becomes significantly stronger
- **Momentum control**: Can chain KOs without interruption
- **Utility doubling**: Status moves become much more reliable

### Counters and Limitations
- **Ghost immunity**: Normal/Fighting moves can't hit Ghost types
- **Protection moves**: Protect blocks both hits
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable it
- **Rocky Helmet**: Takes damage from both hits if making contact
- **Static/Flame Body**: Can trigger from either hit

### Synergies
- **Life Orb**: Boosts both hits (but takes recoil twice)
- **Choice items**: Locked into powerful moves, but no recharge penalty
- **Contact effects**: Items like Expert Belt boost both hits
- **Critical hits**: Each hit can crit independently

### Notable Users
Raging Goddess is typically found on:
- Legendary or pseudo-legendary Pokemon
- Late-game boss battles
- Pokemon designed for ultimate offensive presence
- Special event or postgame encounters

### Version Notes
- Elite Redux exclusive ability
- One of the most powerful combination abilities
- Designed for endgame challenge encounters
- Resistant to Fort Knox ability suppression effects
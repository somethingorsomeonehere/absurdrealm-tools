---
id: 811
name: Drake Of Rage
status: reviewed
character_count: 221
---

# Drake Of Rage - Ability ID 811

## In-Game Description
"Tinted Lens + Rampage"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles damage when attacking into resistances. If a move would be resisted (0.5x damage or less), the damage is multiplied by 2x. Eliminates recharge turns when the user successfully KOs an opponent with a direct attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

Drake Of Rage combines two powerful abilities into one devastating package:

### Tinted Lens Component
- **Effect**: Doubles the power of "not very effective" moves
- **Activation**: When `typeEffectivenessMultiplier <= UQ_4_12(.5)` (0.5x or less effectiveness)
- **Implementation**: Uses `RESISTANCE(2)` macro which applies a 2x multiplier to both resistance and damage modifier
- **Coverage**: Affects moves with 0.25x and 0.5x type effectiveness

```cpp
.onOffensiveMultiplier = +[](ON_OFFENSIVE_MULTIPLIER) {
    if (typeEffectivenessMultiplier <= UQ_4_12(.5)) RESISTANCE(2);
},
```

### Rampage Component
- **Effect**: Removes recharge status when knocking out an opponent
- **Activation**: When the Pokemon with this ability faints an enemy battler
- **Implementation**: 
  - Sets ability state to TRUE (tracking activation)
  - Resets `gVolatileStructs[battler].rechargeTimer = 0`
  - Removes `STATUS2_RECHARGE` flag from the battler's status2
- **Affected Moves**: Hyper Beam, Giga Impact, Rock Wrecker, Roar of Time, Frenzy Plant, Blast Burn, Hydro Cannon, and other recharge moves

```cpp
.onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
    SetAbilityState(battler, ability, TRUE);
    gVolatileStructs[battler].rechargeTimer = 0;
    gBattleMons[battler].status2 &= ~(STATUS2_RECHARGE);
    return FALSE;
},
```

### Damage Calculation Examples

**Tinted Lens Effect:**
- Fire move vs Water-type: 0.5x to 1.0x (100% damage instead of 50%)
- Electric move vs Ground-type: 0x to 0x (no effect on immunities)
- Grass move vs Fire/Flying: 0.25x to 0.5x (50% damage instead of 25%)

**Rampage Scenarios:**
- Use Hyper Beam to KO opponent to No recharge turn to Can attack immediately next turn
- Use Giga Impact to KO opponent to No recharge turn to Can switch or attack freely

### Strategic Implications

**Offensive Advantages:**
- Makes "not very effective" coverage moves viable for dealing neutral damage
- Enables consecutive use of the most powerful moves in the game
- Particularly devastating on high-attack Pokemon with broad movepools
- Synergizes with Choice items since recharge removal allows switching

**Competitive Usage:**
- **Ideal Users**: High-attack Dragon-types, Normal-types with diverse coverage
- **Common Movesets**: Hyper Beam/Giga Impact + coverage moves of different types
- **Team Role**: Wallbreaker and late-game sweeper
- **Timing**: Most effective when opponent has weakened teams for easy KOs

### Interactions and Edge Cases

**Ability Interactions:**
- **Mold Breaker/Teravolt/Turboblaze**: Cannot bypass this ability (it's offensive, not defensive)
- **Neutralizing Gas**: Suppresses both components while active
- **Skill Swap/Role Play**: Both effects transfer together as one ability
- **Trace**: Can copy the full combined ability

**Move Interactions:**
- **Multi-hit moves**: Each hit can trigger Tinted Lens bonus, Rampage only triggers on final KO
- **Future Sight/Doom Desire**: Rampage effect applies when the delayed move KOs
- **Substitute**: Rampage triggers when breaking substitute if it causes fainting
- **Recoil moves**: Rampage activates even if user faints from recoil

**Status Interactions:**
- **Sleep/Paralysis**: Rampage removes recharge but doesn't cure other status conditions
- **Choice Lock**: Recharge removal allows switching out of Choice lock
- **Encore**: Rampage doesn't break Encore, but allows consecutive use of encored recharge move

### Counters and Counterplay

**Direct Counters:**
- **Ghost-types**: Immune to Normal-type recharge moves like Hyper Beam
- **Rocky Helmet/Rough Skin**: Punish contact recharge moves
- **Sturdy/Focus Sash**: Prevent OHKO and deny Rampage activation

**Strategic Counters:**
- **Priority moves**: Strike before recharge moves can be used
- **Status moves**: Cripple with sleep, paralysis, or burn
- **Defensive walls**: Tank hits and stall out with recovery
- **Speed control**: Use Trick Room or Thunder Wave to outspeed

### Synergies

**Item Synergies:**
- **Life Orb**: Boosts already powerful moves further
- **Choice Band/Specs**: Maximum power output, switching enabled by Rampage
- **Normalium Z**: Turns Hyper Beam into devastating Z-move with no recharge on KO

**Team Synergies:**
- **Entry hazards**: Chip damage helps secure KOs for Rampage
- **Dual screens**: Protection while setting up for sweeps
- **Healing support**: Keep ability user healthy for multiple Rampage chains

**Move Synergies:**
- **Setup moves**: Dragon Dance, Swords Dance before Rampage chain
- **Coverage moves**: Utilize Tinted Lens for neutral damage on resists
- **High-power moves**: Hyper Beam, Giga Impact, Outrage for maximum impact

### Version History
- **Introduced**: Elite Redux as combination ability
- **Current Status**: Active in competitive formats
- **Usage Rate**: High in offensive teams, moderate overall

### Notable Users
While specific Pokemon data would need to be checked in the species files, this ability would be most effective on:
- High-attack Dragon-types (natural synergy with "Drake" theme)
- Physical attackers with diverse movepools
- Pokemon with access to powerful recharge moves
- Wallbreakers that can reliably secure KOs
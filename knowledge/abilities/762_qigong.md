---
id: 762
name: Qigong
status: reviewed
character_count: 223
---

# Qigong - Ability ID 762

## In-Game Description
"Always hits. Fighting Spirit + Rampage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user always lands their moves. Converts all Normal-type moves into Fighting-type moves and grants STAB on Fighting-type attacks. Eliminates recharge turns when the user successfully KOs an opponent with a direct attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Qigong is a powerful hybrid ability that combines three distinct mechanical effects:

1. **Perfect Accuracy**: All moves used by the Pokemon will always hit, regardless of accuracy calculations, evasion, or weather conditions
2. **Fighting Spirit Component**: Converts all Normal-type moves to Fighting-type and grants STAB for Fighting-type moves
3. **Rampage Component**: Eliminates recharge requirements after successfully KOing opponents

### Activation Conditions

#### Always Hits Component
- **Trigger**: Every move used by the Pokemon
- **Effect**: `return ACCURACY_ALWAYS_HITS;`
- **Scope**: Applies to all moves, including those with naturally low accuracy

#### Fighting Spirit Component  
- **Move Type Conversion**: 
  - Converts Normal-type moves to Fighting-type
  - Grants the "Ate" boost (1.2x power multiplier) for converted moves
  - Code: `ATE_ABILITY(TYPE_FIGHTING)`
- **STAB Mechanics**:
  - Fighting-type moves receive STAB even if Fighting isn't the Pokemon's natural type
  - Converted Normal moves also receive STAB as they become Fighting-type

#### Rampage Component
- **Trigger**: Successfully KOing an opponent with a recharge move
- **Effect**: Removes recharge status and timer
- **Implementation**: 
  ```cpp
  .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
      SetAbilityState(battler, ability, TRUE);
      gVolatileStructs[battler].rechargeTimer = 0;
      gBattleMons[battler].status2 &= ~(STATUS2_RECHARGE);
      return FALSE;
  }
  ```

### Technical Implementation
```cpp
constexpr Ability Qigong = {
    .onBattlerFaints = Rampage.onBattlerFaints,
    .onOffensiveMultiplier = FightingSpirit.onOffensiveMultiplier,
    .onMoveType = FightingSpirit.onMoveType,
    .onAccuracy = +[](ON_ACCURACY) { return ACCURACY_ALWAYS_HITS; },
    .onBattlerFaintsFor = Rampage.onBattlerFaintsFor,
    .onStab = FightingSpirit.onStab,
};
```

### Affected Moves

#### Always Hits All Moves Including:
- Low accuracy moves (Thunder, Blizzard, Hypnosis, etc.)
- OHKO moves (Fissure, Horn Drill, etc.)
- Status moves with accuracy checks
- All damaging moves regardless of base accuracy

#### Normal to Fighting Conversion Examples:
- **Hyper Beam** to Fighting-type with no recharge after KO
- **Giga Impact** to Fighting-type with no recharge after KO  
- **Return/Frustration** to Fighting-type with STAB
- **Quick Attack** to Fighting-type priority move with STAB
- **Body Slam** to Fighting-type with STAB and paralysis chance

#### Recharge Moves Affected:
- Hyper Beam
- Giga Impact
- Blast Burn
- Hydro Cannon
- Frenzy Plant
- Rock Wrecker
- Roar of Time
- Prismatic Laser

### Interactions with Other Mechanics

#### Weather Interactions
- **Always Hits** overrides weather accuracy modifiers:
  - Thunder still hits in clear weather
  - Blizzard hits outside of hail/snow
  - Hurricane hits in any weather condition

#### Evasion/Accuracy Modifiers
- Completely ignores evasion boosts on target
- Ignores accuracy drops on user
- Overrides moves that modify accuracy (Sand Attack, Double Team effects)

#### Ability Interactions
- **Wonder Guard**: Still blocks non-super effective moves despite perfect accuracy
- **Magic Guard**: Doesn't prevent the Fighting-type conversion or accuracy boost
- **Bulletproof**: Still blocks bullet/ball moves despite perfect accuracy

### Strategic Implications

#### Offensive Advantages
- **Reliable Sweeper**: Hyper Beam becomes a reliable KO move with no drawback
- **Perfect Coverage**: Never miss key moves in crucial moments
- **STAB Boost**: Normal moves gain Fighting STAB and 1.2x Ate multiplier
- **Chain Sweeping**: Can continuously use powerful recharge moves

#### Competitive Usage Notes
- Extremely powerful on physically offensive Pokemon with good Normal move pools
- Ideal for late-game sweeping scenarios
- Pairs excellently with Choice items (no recharge means no need to switch)
- Dangerous with Z-Moves converted to Fighting-type

### Counters
- **Type Resistances**: Ghost-types immune to Fighting moves
- **Sturdy/Focus Sash**: Prevents OHKO sweeps
- **Priority Moves**: Can revenge kill before Qigong user acts
- **Will-O-Wisp/Thunder Wave**: Status can cripple physical attackers
- **Intimidate**: Reduces physical attack power

### Synergies
- **Choice Band**: Maximizes the power of converted Fighting moves
- **Life Orb**: Boosts all moves while maintaining perfect accuracy
- **Silk Scarf**: Boosts Normal moves before conversion
- **Black Belt**: Boosts Fighting-type moves after conversion
- **Normalize**: Converts all moves to Normal first, then Qigong converts to Fighting

### Example Damage Calculations
With Choice Band on a 120 Attack Pokemon using Hyper Beam (150 BP):
- **Base Power**: 150
- **Fighting Spirit Boost**: 150 x 1.2 = 180
- **STAB**: 180 x 1.5 = 270 effective BP
- **Choice Band**: 270 x 1.5 = 405 effective BP
- **Perfect accuracy** ensures this devastating attack never misses
- **No recharge** if it KOs the target

### Common Users
Qigong is typically found on:
- Physically offensive Normal-types with diverse movepools
- Late-game sweepers designed for cleaning up weakened teams  
- Pokemon with access to powerful recharge moves
- Mixed attackers that can utilize both the accuracy and type conversion

### Version History
- **Elite Redux**: Introduced as ID 762
- **Design Intent**: Create a high-risk, high-reward sweeping ability
- **Balance Considerations**: Countered by Ghost-types and priority moves

### Competitive Tier Assessment
**Power Level**: S-Tier in appropriate team compositions
**Usage Rate**: High in offensive teams, moderate overall
**Versatility**: Excellent on physical attackers, limited on special attackers
**Meta Impact**: Significant threat requiring specific counterplay preparation
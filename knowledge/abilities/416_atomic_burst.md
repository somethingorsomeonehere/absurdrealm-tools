---
id: 416
name: Atomic Burst
status: reviewed
character_count: 292
---

# Atomic Burst - Ability ID 416

## In-Game Description
"Electromorphosis + Galvanize."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by any move, the user becomes charged up, doubling the power of the next Electric-type move used. Converts all Normal-type moves into Electric-type moves and grants STAB for Electric-type moves, regardless of the user's typing. Charged status is consumed after one Electric move use.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Atomic Burst** is a hybrid defensive/offensive ability that combines two distinct mechanics from existing abilities:

### Core Mechanics

**1. Electromorphosis Component (Charge-Up Effect)**
- **Activation**: Triggers when the user is hit by any damaging move
- **Effect**: Grants STATUS3_CHARGED_UP status
- **Power Boost**: Next Electric-type move deals **2.0x damage** (100% increase)
- **Single Use**: Charged up status is consumed after using one Electric-type move
- **Restrictions**: Cannot stack - hitting a already charged Pokemon won't add additional charges

**2. Galvanize Component (Type Conversion)**
- **Conversion**: All Normal-type moves become Electric-type moves
- **Power Boost**: Converted moves receive the standard "ate" ability boost (typically ~1.2x)
- **STAB Interaction**: Electric-type users gain STAB on converted Normal moves
- **Move Pool Expansion**: Grants access to Electric-type coverage through Normal moves

### Technical Implementation

```cpp
constexpr Ability AtomicBurst = {
    .onDefender = Electromorphosis.onDefender,  // Charge when hit
    ATE_ABILITY(TYPE_ELECTRIC),                 // NormaltoElectric conversion
};
```

**Charge-Up Mechanism**:
```cpp
.onDefender = +[](ON_DEFENDER) -> int {
    CHECK(ShouldApplyOnHitAffect(battler))
    CHECK_NOT(gStatuses3[battler] & STATUS3_CHARGED_UP)
    
    gStatuses3[battler] |= STATUS3_CHARGED_UP;
    BattleScriptCall(BattleScript_ElectromorphosisActivates);
    return TRUE;
}
```

**Type Conversion Mechanism**:
```cpp
.onMoveType = +[](ON_MOVE_TYPE) -> int {
    CHECK(moveType == TYPE_NORMAL)
    *ateBoost = TRUE;                    // Grants power boost
    return TYPE_ELECTRIC + 1;            // Converts to Electric
},
.onStab = +[](ON_STAB) -> int { 
    return moveType == TYPE_ELECTRIC;    // STAB for Electric moves
}
```

### Damage Calculations

**Base Scenario**: 100 BP Normal move on neutral Electric-type user
- **Standard**: 100 BP Normal move (no STAB)
- **With Atomic Burst**: 100 BP to Electric-type to 100 x 1.2 (ate boost) x 1.5 (STAB) = **180 BP**
- **When Charged**: 180 BP x 2.0 (charged) = **360 BP effective power**

### Affected Moves

**High-Value Normal Moves That Benefit**:
- **Hyper Beam** (150 BP) to 150 x 1.2 x 1.5 x 2.0 = **540 BP when charged**
- **Giga Impact** (150 BP) to Same as Hyper Beam
- **Double-Edge** (120 BP) to 432 BP when charged
- **Body Slam** (85 BP) to 306 BP when charged
- **Quick Attack** (40 BP) to 144 BP when charged (priority maintained)
- **Extreme Speed** (80 BP) to 288 BP when charged (priority maintained)

**Utility Moves**:
- **Thunder Wave** remains unchanged (already Electric)
- **Status moves** like Toxic, Will-O-Wisp unaffected

### Interactions with Other Mechanics

**Positive Synergies**:
- **Electric Terrain**: Boosts Electric-type moves by additional 30%
- **Choice Band/Specs**: Stacks multiplicatively with charged bonus
- **Life Orb**: Stacks with all bonuses
- **Electric-type teammates**: Can set up Electric Terrain support

**Ability Interactions**:
- **Mold Breaker**: Completely negates both components
- **Lightning Rod/Volt Absorb**: Can absorb the converted Electric moves
- **Motor Drive**: Gets Speed boost from converted moves
- **Dry Skin**: Takes damage from converted moves in rain

### Strategic Applications

**Offensive Sets**:
- **Choice Band**: Hyper Beam becomes 810 BP effective power when charged
- **Life Orb**: Flexible move selection with powerful charged attacks
- **Mixed Attacker**: Utilizes both physical and special Normal moves

**Defensive Applications**:
- **Tank Build**: Use the charge-up as a deterrent against physical attackers
- **Pivot**: Get charged, then switch to maintain the boost
- **Revenge Killer**: Come in on a hit, get charged, revenge kill with priority

**Common Users**:
- **Arceus-Electric**: Massive movepool benefits from conversion
- **Regigigas**: Slow Start compensated by massive charged Normal moves
- **Porygon-Z**: Special attacker with diverse Normal movepool

### Competitive Usage Notes

**Strengths**:
- **Versatility**: Functions as both defensive and offensive tool
- **Move Pool Expansion**: Grants Electric-type coverage through Normal moves
- **Unpredictable**: Opponents must respect both uncharged and charged states
- **STAB Synergy**: Electric-types gain significant coverage expansion

**Weaknesses**:
- **Predictable Timing**: Opponents know when you're charged
- **Single Use**: Must get hit again to recharge
- **Ground Immunity**: Converted moves become ineffective against Ground-types
- **Voltage Absorption**: Vulnerable to Electric-immune abilities

**Counters**:
- **Ground-types**: Immune to all converted moves
- **Lightning Rod/Volt Absorb**: Redirect and absorb converted attacks
- **Mold Breaker users**: Completely shut down the ability
- **Special Walls**: Can tank even charged special attacks

### Synergistic Teammates

**Electric Terrain Setters**:
- **Tapu Koko**: Sets terrain for additional Electric boost
- **Pincurchin**: Provides terrain support

**Pivoting Support**:
- **U-turn/Volt Switch users**: Help maintain charged status
- **Slow pivots**: Allow safe entry after getting charged

### Version History

**Previous Implementation**: Originally designed as a counter-attack ability that triggered 50 BP Hyper Beam when hit super-effectively.

**Current Implementation**: Redesigned as a combination ability merging Electromorphosis (charge when hit) with Galvanize (NormaltoElectric conversion), creating a more versatile and strategically interesting ability.

**Design Philosophy**: The change moved from a reactive defensive ability to a proactive offensive tool that rewards both taking hits and utilizing diverse movesets.
---
id: 344
name: Poison Absorb
status: reviewed
character_count: 120
---

# Poison Absorb - Ability ID 344

## In-Game Description
"Absorbs Poison-type moves to heal 25% max HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Absorbs Poison-type moves to heal 25% max HP instead of taking damage. On Toxic Terrain, heals 1/8th of max HP per turn. 

## Detailed Mechanical Explanation

### Basic Information
- **Ability ID:** 344  
- **Type:** Absorption/Healing  
- **Breakable:** Yes

### Overview

Poison Absorb is a defensive ability that turns Poison-type moves into a healing opportunity. When the user would be hit by a Poison-type move, they instead take no damage and recover 25% of their maximum HP. This ability also provides passive healing benefits on Toxic Terrain.

## Mechanics

### Primary Effect: Poison-Type Move Absorption
- **Trigger:** When targeted by any Poison-type move
- **Effect:** Complete immunity to the move + healing for 25% of max HP
- **Healing Amount:** `gBattleMoveDamage = gBattleMons[battler].maxHP / 4`
- **Minimum Healing:** 1 HP (if calculation results in 0)

### Secondary Effect: Toxic Terrain Healing
- **Trigger:** End of turn while on Toxic Terrain
- **Effect:** Heals 12.5% of max HP per turn
- **Healing Amount:** `gBattleMoveDamage = gBattleMons[battler].maxHP / 8`
- **Conditions:** 
  - Not at full HP
  - Can heal (not blocked by Heal Block, etc.)
  - Not the first turn after switching in
  - Standing on Toxic Terrain

### Redirection in Double Battles
- **Effect:** Redirects Poison-type moves to this Pokemon
- **Type:** `TYPE_POISON`
- **Note:** Similar to Lightning Rod but for Poison-type moves

## Code Implementation

### Location: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Lines 3631-3650)

```cpp
constexpr Ability PoisonAbsorb = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_POISON)
        return ABSORB_RESULT_HEAL;
    },
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(gVolatileStructs[battler].isFirstTurn != 2)
        CHECK(IsBattlerTerrainAffected(battler, STATUS_FIELD_TOXIC_TERRAIN))

        gBattleMoveDamage = gBattleMons[battler].maxHP / 8;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        gBattleMoveDamage *= -1;
        BattleScriptPushCursorAndCallback(BattleScript_RainDishActivates);
        return TRUE;
    },
    .redirectType = TYPE_POISON,
    .breakable = TRUE,
};
```

### Healing Logic

The healing is processed in `src/battle_util.c` where `ABSORB_RESULT_HEAL` triggers:

```cpp
if (effect & ABSORB_RESULT_HEAL && !BATTLER_MAX_HP(battler) && CanBattlerHeal(battler)) {
    gBattleMoveDamage = gBattleMons[battler].maxHP / 4;  // 25% healing
    if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
    gBattleMoveDamage *= -1;  // Negative damage = healing
    BattleScriptCall(BattleScript_MoveHPDrain);
}
```

## Strategic Applications

### Offensive Strategy
- **Move Redirection:** In double battles, forces opponent's Poison-type moves to target this Pokemon
- **Toxic Terrain Synergy:** Pairs well with Toxic Terrain setters for passive healing
- **Switch-In Opportunities:** Can safely switch into predicted Poison-type moves

### Defensive Strategy
- **Healing Tank:** Provides substantial healing (25% per absorbed move)
- **Status Move Immunity:** Immune to Poison-type status moves like Toxic, Poison Powder
- **Terrain Control:** Benefits from friendly Toxic Terrain setup

## Competitive Analysis

### Strengths
- **Reliable Healing:** 25% HP recovery is significant
- **Type Immunity:** Complete immunity to an entire type
- **Terrain Synergy:** Additional healing source on Toxic Terrain
- **Doubles Utility:** Move redirection can protect partners

### Weaknesses
- **Mold Breaker:** Can be bypassed by Mold Breaker and similar abilities
- **Limited Scope:** Only works against one specific type
- **Heal Block:** Healing can be prevented by Heal Block
- **Breakable:** Can be suppressed by abilities like Gastro Acid

### Counters
- **Mold Breaker family:** Bypasses the absorption entirely
- **Heal Block:** Prevents the healing component
- **Non-Poison attackers:** Ability provides no benefit against other types
- **Gastro Acid:** Suppresses the ability entirely

## Pokemon with Poison Absorb

Based on the codebase analysis, Poison Absorb appears on various Pokemon as both a regular ability and innate ability:

### As Regular Ability
- Multiple Grass/Poison type Pokemon (including Oddish line based on code context)
- Various other species with poison resistance themes

### As Innate Ability  
- Several species have this as one of their fixed innate abilities
- Often paired with other defensive or type-based abilities

*Note: Complete list would require cross-referencing the SpeciesList.textproto file with specific species names.*

## Related Abilities

### Similar Absorption Abilities
- **Water Absorb (ID: 11):** Same mechanics but for Water-type moves
- **Volt Absorb (ID: 10):** Same mechanics but for Electric-type moves
- **Flash Fire (ID: 18):** Absorbs Fire-type moves but boosts Attack instead of healing

### Terrain-Based Healing
- **Rain Dish (ID: 44):** Heals in rain weather
- **Ice Body (ID: 115):** Heals in hail weather

## Technical Notes

- **Constant Definition:** `#define ABILITY_POISON_ABSORB 344` in `include/generated/constants/abilities.h`
- **Absorption Flag:** Uses `ABSORB_RESULT_HEAL` (value: 1 << 0) to trigger healing
- **Battle Script:** Uses `BattleScript_RainDishActivates` for the terrain healing animation
- **Minimum Healing:** Always heals at least 1 HP to prevent 0-damage issues
- **Negative Damage:** Healing is implemented as negative `gBattleMoveDamage`

## Version History

This ability is part of Elite Redux's expanded ability system, providing enhanced defensive options for Poison-type specialists and defensive team compositions.
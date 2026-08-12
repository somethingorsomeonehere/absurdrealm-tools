---
id: 591
name: Celestial Blessing
status: reviewed
character_count: 89
---

# Celestial Blessing - Ability ID 591

## In-Game Description
"Recovers 1/12 of its health each turn under Misty Terrain."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Restores 1/12 of the user's maximum HP at the end of each turn while under Misty Terrain. 

## Detailed Mechanical Explanation

### Activation Conditions
- **Turn Phase**: End of turn
- **Terrain Requirement**: Must be affected by Misty Terrain
- **Health Requirement**: Cannot be at maximum HP
- **Healing Availability**: Must be able to heal (not blocked by Heal Block, etc.)
- **Turn Restriction**: Does not activate on the turn the Pokemon switches in

### Recovery Amount
- **Base Recovery**: 1/12 of maximum HP per turn
- **Minimum Recovery**: 1 HP (if 1/12 calculation results in 0)

### Implementation Details
- **Battle Script**: Uses `BattleScript_SelfSufficientActivates` for activation message
- **Terrain Check**: Uses `IsBattlerTerrainAffected(battler, STATUS_FIELD_MISTY_TERRAIN)`
- **Healing Check**: Uses `CanBattlerHeal(battler)` to verify healing is possible

### Strategic Applications

#### Team Synergy
- **Misty Surge**: Pairs excellently with Pokemon that can set Misty Terrain
- **Fairy Types**: Provides passive healing for Fairy-type cores
- **Terrain Control**: Encourages maintaining terrain control throughout battle

#### Defensive Utility
- **Passive Recovery**: Provides consistent healing without using move slots
- **Stall Potential**: Enables defensive strategies when combined with other recovery
- **Longevity**: Extends staying power in prolonged battles

#### Counters and Limitations
- **Terrain Dependency**: Completely ineffective without Misty Terrain
- **Heal Block**: Nullified by Heal Block and similar healing prevention
- **Terrain Override**: Disabled when other terrains replace Misty Terrain
- **Switch Timing**: No recovery on switch-in turn

### Related Abilities
- **Eternal Blessing**: Combines Celestial Blessing with Regenerator for enhanced recovery
- **Self Sufficient**: Similar end-turn healing but without terrain requirement (1/16 HP)
- **Peaceful Rest**: Similar concept but requires Fog weather (1/8 HP)

### Competitive Viability
- **Niche Usage**: Highly specialized for Misty Terrain teams
- **Defensive Core**: Strong in defensive teams with terrain support
- **Setup Potential**: Enables Pokemon to set up while maintaining health
- **Resource Management**: Reduces reliance on healing items and moves

### Code Reference
```cpp
constexpr Ability CelestialBlessing = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(gVolatileStructs[battler].isFirstTurn != 2)
        CHECK(IsBattlerTerrainAffected(battler, STATUS_FIELD_MISTY_TERRAIN))

        gBattleMoveDamage = gBattleMons[battler].maxHP / 12;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        gBattleMoveDamage *= -1;
        BattleScriptPushCursorAndCallback(BattleScript_SelfSufficientActivates);
        return TRUE;
    },
};
```
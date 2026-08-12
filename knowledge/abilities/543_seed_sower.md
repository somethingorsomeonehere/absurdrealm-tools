---
id: 543
name: Seed Sower
status: reviewed
character_count: 169
---

# Seed Sower - Ability ID 543

## In-Game Description
"Sets Grassy Terrain when hit. Heals party status when it does."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Activates Grassy Terrain when the Pokemon takes damage from a direct attack, lasting 5 turns (8 with Terrain Extender). Also heals all party Pokemon's status conditions.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Seed Sower is a defensive reaction ability that triggers when the Pokemon takes damage from a direct physical or special attack (not indirect damage like weather or status conditions).

### Activation Conditions
- Must be hit by a direct damaging move
- Activates even if the Pokemon faints from the hit
- Uses the `ShouldApplyOnHitAffect()` check, so blocked by abilities like Magic Guard

### Terrain Setting Effect
When triggered, Seed Sower attempts to set Grassy Terrain on the battlefield:
- **Duration**: 5 turns normally, 8 turns if the user holds a Terrain Extender
- **Permanent**: Terrain can be made permanent by certain field effects
- **Priority**: Can override existing terrain types
- **Airborne Interaction**: The ability has `allowTerrainIfAirborne = TERRAIN_GRASSY`, meaning the user benefits from Grassy Terrain even when airborne (Flying-type, Levitate, etc.)

### Party Status Healing Effect
Simultaneously with setting terrain, Seed Sower calls `BattleScript_HealAllPartyStatus` which heals all party Pokemon of:

**Status1 Effects (Major Status Conditions)**:
- Sleep (all sleep turns)
- Poison (regular)  
- Toxic Poison (with counter reset)
- Burn
- Paralysis
- Freeze
- Frostbite
- Bleeding

**Status2 Effects (Volatile Status)**:
- Nightmare

### Technical Implementation
```cpp
constexpr Ability SeedSower = {
    .onDefender = +[](ON_DEFENDER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK(TryChangeBattleTerrain(battler, STATUS_FIELD_GRASSY_TERRAIN, &gFieldTimers.terrainTimer))

        BattleScriptCall(BattleScript_SeedSower);
        return TRUE;
    },
    .allowTerrainIfAirborne = TERRAIN_GRASSY,
};
```

The battle script sequence:
1. Prints "The battlefield became grassy!"
2. Plays terrain change animation
3. Calls terrain change effects
4. Heals all party status conditions
5. Displays appropriate healing messages

### Grassy Terrain Benefits
Once set, Grassy Terrain provides additional benefits:
- **HP Recovery**: Grounded Pokemon heal 1/16 of max HP each turn
- **Grass Move Boost**: Grass-type moves deal 50% more damage
- **Earthquake Reduction**: Earthquake, Magnitude, and Bulldoze deal 50% less damage to grounded Pokemon
- **Duration**: 5 turns (8 with Terrain Extender)

### Strategic Implications
**Defensive Utility**:
- Immediate party-wide status cleansing makes it excellent for defensive teams
- Can be used as a sacrifice play to cleanse status and set terrain for the team
- Works well on bulky Pokemon that can survive hits and gain multiple activations

**Terrain Control**:
- Provides immediate terrain control without needing to use a move slot
- Can override opponent's terrain setups
- Benefits Grass-type teammates with damage boost and healing

### Interactions with Other Abilities/Mechanics

**Soundproof Interaction**: Unlike Heal Bell, the status healing from Seed Sower is NOT blocked by Soundproof, as it uses the Aromatherapy-style healing (affects all party members regardless of sound immunity).

**Multi-Hit Moves**: Can potentially trigger multiple times if the Pokemon survives multiple hits from moves like Bullet Seed or Double Slap, though terrain won't be reset if already active.

**Magic Guard**: Blocked by Magic Guard as it uses `ShouldApplyOnHitAffect()` check.

**Substitute**: Likely blocked when behind Substitute (needs testing).

### Common Users
- **Mega Rillaboom**: Primary user, makes excellent use as a bulky Grass-type
- Other Grass-type Pokemon in Elite Redux may have this as an innate ability

### Competitive Usage Notes
**Strengths**:
- Provides immediate utility even when taking heavy damage
- Excellent for status-heavy metas
- Gives team-wide support without requiring move slots
- Can disrupt opponent's terrain strategies

**Weaknesses**:
- Requires taking damage to activate
- One-time healing per activation doesn't prevent re-statusing
- Terrain can be overridden by opponent immediately after

### Counters
- **Indirect Damage**: Doesn't trigger from Stealth Rock, status damage, weather damage
- **Magic Guard**: Completely prevents activation  
- **Terrain Override**: Opponents can immediately set their own terrain
- **Status Immunity**: Pokemon with status immunity (Limber, Water Veil, etc.) don't need the healing

### Synergies
- **Terrain Extender**: Extends Grassy Terrain duration to 8 turns
- **Grass-type Partners**: Benefit from terrain damage boost
- **Grounded Partners**: Benefit from HP recovery
- **Status-Vulnerable Teams**: Teams weak to status appreciate the cleansing

### Version History
Elite Redux custom ability - Sets Grassy Terrain when hit while simultaneously providing party-wide status healing, combining terrain control with clerical support in a unique defensive reaction ability.
---
id: 477
name: Generator
status: reviewed
character_count: 256
---

# Generator - Ability ID 477

## In-Game Description
"Charges up once on entry or when electric terrain is active."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Generator charges up the user once upon switching in, doubling Electric-type move power for the next Electric attack. Recharge when Electric Terrain becomes active during battle. The charged state is lost upon switching out or after using an Electric move.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Generator is an offensive ability that provides a powerful one-time boost to Electric-type moves. The ability grants the "charged up" status which doubles the power of the next Electric-type move used.

### Activation Conditions
- **Entry activation**: Charges up once automatically when switching into battle
- **Terrain activation**: Recharges when Electric Terrain becomes active
- **Single use**: Each charge is consumed after using an Electric-type move
- **Persistent**: The ability continues working across turns until switched out

### Power Mechanics
- **Damage multiplier**: 2.0x power boost to Electric-type moves
- **Status requirement**: Must have STATUS3_CHARGED_UP status active
- **Move requirement**: Only applies to Electric-type attacking moves
- **Consumption**: Status is removed after using an Electric-type move

### Technical Implementation
```c
// Generator activates on entry or Electric Terrain
constexpr Ability Generator = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gStatuses3[battler] & STATUS3_CHARGED_UP)
        
        int any = FALSE;
        if (IsTerrainActive(STATUS_FIELD_ELECTRIC_TERRAIN)) {
            any = TRUE;
        } else if (!GetSingleUseAbilityCounter(battler, ability)) {
            SetSingleUseAbilityCounter(battler, ability, TRUE);
            any = TRUE;
        }
        
        CHECK(any)
        gStackBattler1 = battler;
        BattleScriptPushCursorAndCallback(BattleScript_GeneratorActivates);
        return TRUE;
    },
    .onTerrain = +[](ON_TERRAIN) -> int {
        CHECK_NOT(gStatuses3[battler] & STATUS3_CHARGED_UP)
        CHECK(IsTerrainActive(STATUS_FIELD_ELECTRIC_TERRAIN))
        
        gStackBattler1 = battler;
        BattleScriptCall(BattleScript_GeneratorActivatesRet);
        return TRUE;
    },
    .onExit = +[](ON_EXIT) -> int {
        CHECK(gStatuses3[battler] & STATUS3_CHARGED_UP)
        SetSingleUseAbilityCounter(battler, ability, FALSE);
        return FALSE;
    },
    .persistent = TRUE,
};

// Damage calculation includes charged up bonus
if (gStatuses3[battlerAtk] & STATUS3_CHARGED_UP && moveType == TYPE_ELECTRIC) 
    MulModifier(&modifier, UQ_4_12(2.0));
```

### Terrain Interaction
- **Electric Terrain synergy**: Can recharge multiple times if terrain is repeatedly set
- **Terrain timing**: Activates when terrain becomes active, not just when present
- **Multiple activations**: Unlike entry activation, terrain activation can occur multiple times
- **Priority**: Electric Terrain setters disable Generator's entry activation to prevent double charging

### Important Interactions
- **Single-use counter**: Entry activation is limited to once per switch-in
- **Terrain recharging**: Electric Terrain can recharge the ability even after use
- **Switch reset**: Counter resets when switching out, allowing reactivation on re-entry
- **Move consumption**: Charged status is consumed when using any Electric-type move
- **Power stacking**: Stacks multiplicatively with other damage modifiers

### Ability Suppression
- **Mold Breaker effects**: Cannot bypass Generator's charging mechanism
- **Neutralizing Gas**: Prevents charging while active
- **Gastro Acid**: Disables the ability but doesn't remove existing charge
- **Simple Beam**: Replaces ability and removes charged status

### Strategic Implications
- **Immediate threat**: Creates instant offensive pressure upon switch-in
- **Terrain synergy**: Excellent on Electric Terrain teams for multiple charges
- **One-shot potential**: Can secure crucial KOs with doubled Electric moves
- **Prediction based**: Opponents must respect potential doubled damage
- **Resource management**: Timing Electric moves becomes crucial

### Common Users
- Electric-type attackers with powerful Electric moves
- Pokemon with access to high BP Electric moves (Thunderbolt, Thunder, etc.)
- Mixed attackers who can utilize both physical and special Electric moves
- Terrain team supporters who benefit from Electric Terrain

### Competitive Usage Notes
- **Entry hazard immunity**: Not affected by entry hazards unlike other entry abilities
- **Immediate impact**: Unlike setup moves, provides instant power boost
- **Terrain team core**: Essential ability for Electric Terrain strategies
- **Wallbreaking**: Can break through typical Electric-type resists with doubled power
- **Priority moves**: Works with Electric-type priority moves like Thunder Wave (damage dealing)

### Optimal Movesets
- **High power Electric moves**: Thunderbolt, Discharge, Thunder
- **STAB Electric types**: Maximizes damage potential with STAB + Generator
- **Mixed coverage**: Physical and special Electric moves for versatility
- **Terrain setting**: Moves like Electric Terrain for self-recharging

### Counters
- **Ground-type immunity**: Completely immune to Electric-type moves
- **Lightning Rod/Motor Drive**: Redirects or absorbs Electric attacks
- **Volt Absorb**: Heals from Electric-type moves instead of taking damage
- **Ability changing**: Simple Beam, Worry Seed remove the charging capability
- **Weather override**: Weather Ball users can avoid Electric-type attacks

### Synergies
- **Electric Terrain**: Essential for multiple charges and team support
- **Thunder**: Perfect accuracy in rain combines with doubled power
- **Choice items**: Can be used with Choice Band/Specs for massive damage
- **Life Orb**: Stacks multiplicatively for extreme power
- **Magnet**: Boosts Electric moves further when combined with charge

### Related Abilities
- **Energized**: Enhanced version that also charges on Electric-type KOs
- **Battery**: Team support that boosts Special Attack for Electric moves
- **Electric Surge**: Sets Electric Terrain to enable recharging
- **Motor Drive**: Immunity to Electric moves that would otherwise be boosted

### Version History
- Introduced in Elite Redux as ID 477
- Part of the terrain interaction ability family
- Designed to reward aggressive Electric-type play
- Synergizes with the expanded terrain mechanics in Elite Redux
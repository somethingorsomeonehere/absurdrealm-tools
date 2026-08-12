---
id: 228
name: Misty Surge
status: reviewed
character_count: 205
---

# Misty Surge - Ability ID 228

## In-Game Description
"Casts Misty Terrain on entry. Lasts 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Creates Misty Terrain on entry, lasting 8 turns (12 with Terrain Extender). Misty Terrain prevents all status conditions for grounded Pokemon and boosts Fairy-type moves by 30%. Overrides existing terrain.

## Detailed Mechanical Explanation
*For Discord/reference use*

Misty Surge is an automatic terrain-setting ability that activates when the Pokemon enters battle.

### Core Mechanics
- **Activation**: Triggers immediately upon switching in or at the start of battle
- **Duration**: Sets Misty Terrain for exactly 8 turns (reduced from infinite in some games)
- **Priority**: Activates before most other entry abilities
- **Overrides**: Replaces any existing terrain when activated

### Misty Terrain Effects
1. **Status Immunity**: Grounded Pokemon are completely immune to all major status conditions (Sleep, Poison, Burn, Paralysis, Freeze/Frostbite, Bleed)
2. **Fairy-type Move Boost**: Fairy-type moves used by grounded Pokemon receive a 30% power increase
3. **Item Activation**: Automatically activates Misty Seeds held by grounded Pokemon, boosting Special Defense by 1 stage
4. **Move Interactions**: 
   - Misty Explosion receives 1.5x power when used in Misty Terrain
   - Moves with terrain-boosting effects get enhanced power (30% boost for certain moves)

### Technical Implementation
```cpp
constexpr Ability MistySurge = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK(TryChangeBattleTerrain(battler, STATUS_FIELD_MISTY_TERRAIN, &gFieldTimers.terrainTimer))
        
        gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_TERRAINBECOMESMISTY;
        BattleScriptPushCursorAndCallback(BattleScript_SurgeActivates);
        return TRUE;
    },
    .allowTerrainIfAirborne = TERRAIN_MISTY,
};
```

### Affected Moves
**Boosted by Misty Terrain:**
- All Fairy-type moves (30% power increase for grounded users)
- Misty Explosion (50% power increase)
- Nature Power (becomes Moonblast)
- Terrain-specific moves with EFFECT_MISTY_TERRAIN_BOOST

### Interactions with Other Abilities/Mechanics
- **Overrides**: Electric Surge, Grassy Surge, Psychic Surge, Toxic Surge
- **Terrain Extenders**: Terrain Extender item extends duration from 8 to 12 turns
- **Airborne Pokemon**: Flying-types and Levitate users are unaffected by terrain benefits but still affected by Fairy-type boost if grounded by moves like Smack Down
- **Infiltrator**: Does not bypass terrain effects (terrain affects the field, not sides)

### Strategic Implications
- **Defensive Utility**: Provides team-wide status protection, making it excellent for stall teams
- **Fairy-type Support**: Essential for Fairy-type sweepers and teams
- **Priority Control**: Sets terrain immediately, potentially disrupting opponent's terrain-based strategies
- **Utility Support**: Activates beneficial seeds and terrain-based item effects

### Common Users
In Elite Redux, Misty Surge is typically found on:
- Tapu Fini (primary user)
- Other Fairy-type legendaries or specially designed Pokemon
- Custom Elite Redux Pokemon designed for terrain support

### Competitive Usage Notes
- **Team Building**: Often paired with Fairy-type attackers and defensive Pokemon vulnerable to status
- **Lead Position**: Commonly used as a lead to establish terrain control early
- **Switching Strategy**: Can be brought in mid-battle to reset terrain and provide status immunity
- **Terrain Wars**: Priority in terrain setting often determines matchup outcomes

### Counters
- **Terrain Override**: Other Surge abilities, Terrain moves, or abilities that change terrain
- **Airborne Moves**: Magnet Rise, Telekinesis make Pokemon immune to terrain effects
- **Utility**: Pokemon with Natural Cure or other status-clearing abilities reduce the defensive value

### Synergies
- **Fairy-type Attackers**: Pixilate, Sylveon, Gardevoir benefit from terrain boost
- **Status-Vulnerable Pokemon**: Physical attackers weak to burn, fast Pokemon weak to paralysis
- **Seed Users**: Pokemon holding Misty Seeds get immediate Special Defense boost
- **Defensive Cores**: Pairs well with other defensive abilities and moves

### Version History
- Originally introduced in Generation 7 as Tapu Fini's signature ability
- Elite Redux: Maintains 8-turn duration and standard effects
- No significant changes from original implementation in Elite Redux

### Numerical Values
- **Terrain Duration**: 8 turns (12 with Terrain Extender)
- **Fairy Move Boost**: 30% power increase (1.3x multiplier)
- **Status Immunity**: 100% for all major status conditions
- **Seed Boost**: +1 Special Defense stage when activated
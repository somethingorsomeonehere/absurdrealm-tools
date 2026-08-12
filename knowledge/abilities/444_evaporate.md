---
id: 444
name: Evaporate
status: reviewed
character_count: 194
---

# Evaporate - Ability ID 444

## In-Game Description
"Takes no damage and sets Mist if hit by water."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Evaporate negates all damage from Water-type moves and sets Mist for 5 turns on the user's side when hit by Water moves. Mist protects the entire team from stat reductions, including self drops. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Evaporate is a defensive ability that provides complete immunity to Water-type moves while also setting up team-wide protection. When hit by a Water-type move, the Pokemon takes no damage and automatically sets Mist if it's not already active.

### Activation Conditions
- **Move type requirement**: Only triggers on Water-type moves
- **Damage negation**: Completely negates all damage from Water-type moves
- **Mist condition**: Only sets Mist if not already active on the user's side
- **Duration**: Mist lasts for 5 turns when activated
- **Breakable**: Can be suppressed by Mold Breaker and similar abilities

### Technical Implementation
```c
// Evaporate in abilities.cc
constexpr Ability Evaporate = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_WATER)
        return ABSORB_RESULT_EVAPORATE;
    },
    .breakable = TRUE,
};

// In battle_util.c - handles Mist setting
if (effect & ABSORB_RESULT_EVAPORATE && !gSideTimers[GetBattlerSide(battler)].mistTimer) {
    int side = GetBattlerSide(battler);
    gSideStatuses[side] |= SIDE_STATUS_MIST;
    gSideTimers[side].mistTimer = SCREEN_DURATION; // 5 turns
    // Trigger "became shrouded in Mist!" message
}
```

### Mist Effects
- **Stat protection**: Prevents all stat reductions for the entire team
- **Duration**: 5 turns (SCREEN_DURATION constant)
- **Team-wide**: Protects all Pokemon on the user's side
- **Message**: Displays "{Pokemon} became shrouded in Mist!" when activated
- **Overwrite protection**: Won't activate if Mist is already active

### Important Interactions
- **Multi-hit Water moves**: Each hit triggers absorption, but Mist only set once
- **Status effects**: Water moves with secondary effects (like Scald's burn) are completely negated
- **Substitute**: Bypasses Substitute since it's an absorbing ability
- **Z-Moves**: Completely negates Z-powered Water moves
- **Max Moves**: Negates damage but may not prevent secondary effects from Max Geyser
- **Ability suppression**: Disabled by Mold Breaker, Teravolt, Turboblaze, and Neutralizing Gas

### Water Move Coverage
Evaporate provides immunity to all Water-type moves including:
- **Physical**: Waterfall, Aqua Jet, Liquidation, Crabhammer
- **Special**: Surf, Hydro Pump, Scald, Water Pulse
- **Status**: No Water-type status moves to absorb
- **Multi-hit**: Scale Shot (if Water-type), etc.
- **Priority**: Aqua Jet immunity
- **Signature moves**: Steam Eruption, Origin Pulse, Prismatic Laser (if Water)

### Strategic Applications
- **Water immunity**: Complete shutdown of Water-type attackers
- **Team support**: Provides stat reduction protection for entire team
- **Stall counter**: Mist blocks stat drops from moves like Tickle, Charm, etc.
- **Intimidate counter**: Mist prevents Attack drops from Intimidate
- **Pivot utility**: Safe switch-in against Water moves with team benefits

### Synergies
- **Fire types**: Covers Water weakness while providing utility
- **Stat boosting**: Protects setup sweepers from stat drops
- **Clerical support**: Excellent on support Pokemon
- **Anti-stall**: Counters defensive strategies using stat drops
- **Team building**: Valuable on teams weak to Water coverage

### Counters and Limitations
- **Non-Water coverage**: Vulnerable to all other attacking types
- **Mist limitation**: No benefit if Mist is already active
- **Ability suppression**: Completely disabled by Mold Breaker variants
- **Weather immunity**: Cloud Nine/Air Lock don't affect this ability
- **Gastro Acid**: Can remove the ability entirely
- **Role Play/Skill Swap**: Can be copied or swapped away

### Competitive Usage
- **Water check**: Hard counter to Water-type attackers
- **Utility role**: Provides team support through Mist
- **Switch-in**: Safe entry against predicted Water moves
- **Anti-meta**: Effective against Water-heavy team compositions
- **Durability**: Increases effective bulk against Water coverage

### Common Matchups
- **Dominates**: Water-type specialists, mixed attackers with Water coverage
- **Supports**: Setup sweepers, frail teammates vulnerable to stat drops
- **Struggles against**: Pure physical/special attackers without Water moves
- **Neutral**: Most other type matchups remain unchanged

### Version History
- Custom Elite Redux ability (ID 444)
- Unique mechanic combining damage absorption with field effect
- Part of the expanded ability roster for competitive diversity
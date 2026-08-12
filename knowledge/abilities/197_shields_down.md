---
id: 197
name: Shields Down
status: reviewed
character_count: 283
---

# Shields Down - Ability ID 197

## In-Game Description
"At 1/2 of max HP or below, transforms into Core form."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transforms Minior from Meteor Form to Core Form when HP drops to 50% or below. In Meteor Form, grants immunity to all status conditions. When using Shell Smash, immediately transforms to Core Form regardless of current HP. Cannot revert to Meteor Form once transformed during battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Shields Down is Minior's signature ability that manages its unique dual-form system:

1. **Form Transformation**: Automatically transforms from Meteor Form to Core Form when HP falls to 50% or below
2. **Status Immunity**: While in Meteor Form, grants complete immunity to all status conditions (poison, burn, paralysis, sleep, freeze)
3. **Shell Smash Trigger**: Using Shell Smash immediately forces transformation to Core Form regardless of current HP
4. **One-Way Transformation**: Cannot revert back to Meteor Form during battle once transformed

### Technical Implementation
The ability uses the HP transformation system with these parameters:
```c
// HP fraction of 2 means transforms at 1/2 (50%) HP
{ABILITY_SHIELDS_DOWN, SPECIES_MINIOR, SPECIES_MINIOR_CORE_RED, 2}
```

Key code components:
- **Status Immunity**: Checks if battler is in Meteor Form and blocks all status conditions
- **HP-Based Check**: Monitors HP every turn and triggers transformation at 50% HP threshold
- **Shell Smash Override**: Uses `EFFECT_SHELL_SMASH` detection to force immediate transformation
- **Ability State**: Uses ability state tracking to prevent reverting to Meteor Form

### Affected Pokemon
- **Minior** (all color variants):
  - Meteor Orange to Core Orange
  - Meteor Yellow to Core Yellow
  - Meteor Green to Core Green
  - Meteor Blue to Core Blue
  - Meteor Indigo to Core Indigo
  - Meteor Violet to Core Violet
  - Red (default) to Core Red

### Strategic Implications
**Meteor Form Advantages:**
- Complete status immunity
- Higher defensive stats
- Protection from indirect damage sources

**Core Form Advantages:**
- Higher Speed and offensive stats
- Access to full moveset effectiveness
- Better sweeping potential

**Shell Smash Strategy:**
- Can voluntarily trigger transformation with Shell Smash
- Combines stat boosts with form change
- Allows strategic timing of transformation

### Interactions with Other Mechanics
- **Unsuppressable**: Cannot be suppressed by abilities like Gastro Acid
- **Transform Protection**: Cannot be copied by Transform or Imposter
- **Weather Independence**: Unlike Forecast, not affected by weather changes
- **Entry/End Turn**: Shares transformation checking with Forecast ability

### Counters
- **Indirect Damage**: Use entry hazards or weather to chip HP in Meteor Form
- **Multi-Hit Moves**: Can break through and trigger transformation mid-attack
- **Status After Transform**: Can inflict status once in Core Form
- **Priority Moves**: Effective against fast Core Form

### Version History
- Elite Redux implementation includes all Minior color variants
- Maintains official Pokemon mechanics with enhanced form variety
- Integrated with the game's HP transformation system
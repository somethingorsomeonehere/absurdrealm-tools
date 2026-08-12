---
id: 719
name: Tar Toss
status: reviewed
character_count: 188
---

# Tar Toss - Ability ID 719

## In-Game Description
"Uses Tar Shot on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Tar Shot on switch in, lowering the target's Speed by one stage and making them take double damage from Fire-type moves. Does not stack the Fire-type damage debuff on successive uses.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Tar Toss is an entry ability that automatically uses the move Tar Shot against opponents when the Pokemon switches into battle. This creates immediate battlefield control through both speed reduction and Fire-type vulnerability.

### Activation Conditions
- **Trigger**: Activates automatically on switch-in
- **Targeting**: Targets opposing Pokemon present on the field
- **Usage**: Functions exactly like using the move Tar Shot with 100% accuracy
- **Priority**: Executes as soon as the Pokemon enters battle

### Tar Shot Effects Applied
1. **Speed Reduction**: Lowers target's Speed by one stage (same as -1 Speed)
2. **Fire Weakness**: Target takes double damage from Fire-type moves (2.0x multiplier)
3. **Volatile Status**: Applied as `tarShot` volatile status that persists until switching out
4. **One-Time Effect**: Cannot apply tar to the same target twice per battle

### Technical Implementation
```c
// Tar Toss ability definition
constexpr Ability TarToss = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_TAR_SHOT, 0); 
    },
};

// Fire-type damage calculation with tar shot
if (moveType == TYPE_FIRE && gVolatileStructs[battlerDef].tarShot) 
    mod = UQ_4_12(2.0);  // Double damage
```

### Move Details (Tar Shot)
- **Type**: Rock
- **Category**: Status
- **Accuracy**: 100%
- **PP**: 15
- **Target**: Selected opponent
- **Effects**: 
  - Lowers Speed by 1 stage
  - Applies Fire-type vulnerability (2.0x damage)
  - Blocked by Magic Coat/Magic Bounce
  - Enhanced by Mega Launcher ability

### Important Interactions
- **Speed Stages**: Will fail speed reduction if target is already at -6 Speed
- **Fire Immunity**: Fire-immune Pokemon still get speed reduction but no Fire weakness
- **Status Persistence**: Tar effect lasts until the affected Pokemon switches out
- **Battle Reset**: Each new battle allows tar to be applied again to same species
- **Multi-Target**: In doubles, can potentially affect multiple opponents

### Failure Conditions
- **Already Tarred**: Cannot tar the same Pokemon twice in one battle
- **Magic Coat/Bounce**: Reflected back to user
- **Speed at Minimum**: Speed reduction fails if target at -6 Speed (but Fire weakness still applies)
- **Substitute**: Blocked by Substitute

### Strategic Applications
- **Fire Team Support**: Essential for Fire-type spam teams
- **Speed Control**: Immediate speed reduction for turn order manipulation  
- **Entry Hazard Alternative**: Provides immediate battlefield control
- **Doubles Strategy**: Can slow multiple opponents in double battles
- **Late Game Setup**: Perfect for bringing in Fire-type closers

### Synergies
- **Fire-type attackers**: All Fire moves deal double damage to tarred opponents
- **Heat Wave/Eruption**: Devastating in doubles when opponents are tarred
- **Sun teams**: Combines with Solar Beam and Fire-type synergy
- **Flame Charge**: Speed boost while opponent is slowed
- **Choice Band/Specs**: Guaranteed setup for powerful Fire attacks

### Counters
- **Magic Bounce**: Bounces Tar Shot back to user
- **Substitute**: Blocks the tar application entirely  
- **Rapid switch-outs**: Opponents can switch to remove tar status
- **Clear Body/White Smoke**: Prevents speed reduction (but not Fire weakness)
- **Fire immunity**: Flash Fire, Water Veil, etc. negate Fire weakness portion

### Team Building Considerations
- **Fire-type core**: Build team around Fire-type sweepers
- **Entry timing**: Best used when opponent has key threats on field
- **Switch initiative**: Provides immediate impact unlike passive abilities
- **Coverage gaps**: Helps Fire types hit Steel/Water types harder with setup

### Competitive Usage Notes
- Excellent lead ability for Fire-focused teams
- Forces immediate switches or gives Fire types free setup
- Particularly strong in formats with limited switching
- Can turn neutral matchups into favorable ones for Fire types
- Provides both offensive and speed control utility

### Version History
- Added in Elite Redux as unique entry ability
- Implemented using standard UseEntryMove framework
- Based on Generation VIII move Tar Shot mechanics
- Enhanced with persistent Fire weakness effect
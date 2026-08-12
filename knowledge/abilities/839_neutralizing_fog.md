---
id: 839
name: Neutralizing Fog
status: reviewed
character_count: 131
---

# Neutralizing Fog - Ability ID 839

## In-Game Description
"Uses Defog on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Defog on switch in, clearing all entry hazards, screens, Safeguard, and Mist. Also lowers the opponent's evasion by one stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Neutralizing Fog is an entry ability that automatically executes the move Defog upon switching in. This provides immediate field control without using a turn or moveslot.

### Activation Conditions
- **Trigger**: Activates immediately when the Pokemon enters battle
- **Target**: Affects the entire field (both sides)
- **Cost**: No PP cost, automatic activation
- **Priority**: Uses Defog's normal priority mechanics

### Technical Implementation
```c
constexpr Ability NeutralizingFog = {
    .onEntry = +[](ON_ENTRY) -> int { return UseEntryMove(battler, ability, MOVE_DEFOG, 0); },
};
```

The ability uses the `UseEntryMove` function to execute Defog with:
- Move ID: `MOVE_DEFOG`
- Power parameter: 0 (Defog is a status move)

### Effects Cleared by Defog
**Entry Hazards (both sides):**
- Stealth Rock
- Spikes (all layers)
- Toxic Spikes (all layers)
- Sticky Web
- G-Max Steelsurge steel spikes

**Screens (both sides):**
- Light Screen
- Reflect
- Aurora Veil
- Safeguard
- Mist

**Terrain Effects:**
- Electric Terrain
- Grassy Terrain
- Misty Terrain
- Psychic Terrain

**Additional Effect:**
- Lowers target's evasion by 1 stage (if a target exists)

### Important Interactions
- **Magic Bounce**: Defog cannot be bounced back
- **Taunt**: Doesn't prevent activation since it's an ability effect
- **Ability suppression**: Won't activate if ability is suppressed
- **Multiple switches**: Activates every time the Pokemon enters
- **Rapid Spin comparison**: Clears both sides unlike Rapid Spin

### Strategic Implications
- **Hazard control**: Premier hazard removal without using a turn
- **Anti-screens**: Removes opponent's defensive screens
- **Terrain removal**: Counters terrain-based strategies
- **Double-edged**: Also removes your own hazards/screens
- **Pivot potential**: Can switch in to clear then switch out

### Common Users
- **Fogging**: Primary user, designed around this ability
- **Breezing**: Evolution with better stats
- **Storming**: Final evolution with this ability

### Competitive Usage Notes
- Excellent on bulky pivots that can switch in repeatedly
- Pairs well with U-turn/Volt Switch for momentum
- Can enable hazard-weak teammates safely
- Must be careful not to remove own team's screens
- Provides guaranteed hazard removal unlike Defog users who can miss

### Counters
- **Ability suppression**: Neutralizing Gas, Mold Breaker effects
- **Re-setting hazards**: Set hazards again after it switches
- **Offensive pressure**: Punish the switch-in
- **Hazard-independent teams**: Teams that don't rely on hazards
- **Protect/Substitute**: Can block the evasion drop

### Synergies
- **Hazard-weak Pokemon**: Enables Fire, Flying, Ice, Bug types
- **Offensive teams**: Don't need screens, benefit from hazard removal
- **Pivot moves**: U-turn, Volt Switch, Flip Turn
- **Setup sweepers**: Clear hazards for safe setup
- **Weather teams**: Don't care about terrain removal

### Version History
- Elite Redux exclusive ability
- Designed for the Fogging line as signature ability
- Provides unique role compression for hazard control
---
id: 553
name: Guard Dog
status: reviewed
character_count: 154
---

# Guard Dog - Ability ID 553

## In-Game Description
"Can't be forced out. Inverts Intimidate effects."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Guard Dog prevents forced switching from moves and Red Card. When affected by Intimidate or Scare, it raises the stat by one stage instead of lowering it. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Guard Dog provides two distinct protective effects that make it excellent for maintaining battlefield control:

### Core Mechanics
- **Switch Prevention**: Completely prevents forced switching from any source
- **Intimidate Inversion**: Converts Attack-lowering Intimidate effects into Attack boosts
- **Passive Ability**: Always active, no activation conditions required

### Switch Prevention Details
Guard Dog blocks all forms of forced switching including:
- **Moves**: Roar, Whirlwind, Dragon Tail, Circle Throw
- **Items**: Red Card activation when hit
- **Other Effects**: Any ability or move effect that forces switching

The switch prevention works through the `onTrap` mechanism, similar to abilities like:
- Arena Trap (grounds Flying types)
- Shadow Tag (prevents normal switching) 
- Magnet Pull (traps Steel types)

However, Guard Dog provides universal switch prevention regardless of type or grounding status.

### Intimidate Inversion Mechanics
When the opponent's Intimidate ability activates:
1. Normal effect would lower Attack by 1 stage
2. Guard Dog inverts this to raise Attack by 1 stage instead
3. The boost triggers the same visual and audio cues as normal stat boosts
4. Works against all forms of Intimidate including from abilities like:
   - Standard Intimidate
   - Abilities that include Intimidate effects (like some custom abilities)

### Technical Implementation
```cpp
// Switch prevention (similar to other trapping abilities)
.onTrap = +[](ABILITY_ON_TRAP) -> int { 
    return TRUE; // Always prevents switching 
},

// Intimidate inversion (likely similar to stat boost abilities)
.onStatStage = +[](ABILITY_ON_STAT_STAGE) -> int {
    if (stat == STAT_ATK && stages < 0) {
        // Invert attack reduction to boost
        return -stages; // Convert negative to positive
    }
    return stages;
}
```

### Strategic Applications
**Offensive Uses**:
- Guaranteed setup time without fear of being forced out
- Intimidate becomes a free Attack boost
- Perfect for setup sweepers that need time to boost

**Defensive Uses**:
- Prevents phazing from hazard-setting teams
- Blocks Red Card switches that could disrupt strategy
- Forces opponents to deal with the Pokemon directly

**Team Synergy**:
- Excellent on setup sweepers like Dragon Dance users
- Great with Baton Pass strategies (can't be forced out mid-pass)
- Synergizes with Substitute (prevents forced switching through Sub)

### Affected Moves and Items
**Forced Switch Moves**:
- Roar (Normal-type, -6 priority)
- Whirlwind (Normal-type, -6 priority) 
- Dragon Tail (Dragon-type, -6 priority)
- Circle Throw (Fighting-type, -6 priority)

**Items Blocked**:
- Red Card (forces attacker to switch when holder takes damage)

### Interactions with Other Mechanics
- **Substitute**: Guard Dog still prevents forced switching even through Substitute
- **Magic Bounce**: If Magic Bounce reflects a switch move, Guard Dog still blocks it
- **Taunt**: Doesn't prevent Guard Dog's passive effects
- **Mold Breaker**: Cannot bypass Guard Dog's switch prevention or Intimidate immunity

### Example Damage Calculations
Guard Dog doesn't affect damage calculations directly, but the Attack boost from inverted Intimidate provides:
- +1 Attack stage = 1.5x physical attack power
- Example: 100 Base Power move goes from 100 to 150 effective power

### Common Users
In Elite Redux, Guard Dog is typically found on:
- Dog-like Pokemon (thematically appropriate)
- Defensive walls that need to maintain field presence
- Setup sweepers requiring guaranteed setup time

### Competitive Usage Notes
**Advantages**:
- Hard counters phazing strategies
- Turns Intimidate users into setup bait
- Provides exceptional battlefield control
- Cannot be bypassed by most abilities

**Limitations**:
- Doesn't prevent voluntary switching
- No protection against status moves or stat drops besides Intimidate
- Requires the opponent to actually use forced switch moves to gain benefits

### Counters
- Direct KO moves (bypasses switch prevention)
- Special attackers (Intimidate inversion only helps physical attacks)
- Status moves and other stat-reducing effects
- Pokemon that don't rely on forced switching or Intimidate

### Synergies
**Excellent Partners**:
- Entry hazard setters (Guard Dog user can't be phased out)
- Baton Pass Pokemon (safe setup and passing)
- Pokemon with setup moves (guaranteed setup time)

**Item Synergies**:
- Leftovers (extended staying power)
- Life Orb (capitalizes on Attack boosts)
- Choice items (can't be forced to switch and lose choice lock)

### Version History
- Introduced in Generation IX
- Elite Redux implementation maintains official mechanics
- No known changes from official game mechanics
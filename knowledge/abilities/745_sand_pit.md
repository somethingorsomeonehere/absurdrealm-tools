---
id: 745
name: Sand Pit
status: reviewed
character_count: 175
---

# Sand Pit - Ability ID 745

## In-Game Description
"Attacks with 20BP Sand Tomb on switch-in."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Uses Sand Tomb with 20 BP on switch in. Hits all opposing Pokemon and traps them for 4-5 turns, making them lose 1/8 max HP each turn. Cannot miss and ignores accuracy checks. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sand Pit is an offensive entry ability that automatically uses a weakened version of Sand Tomb when the Pokemon switches into battle. This creates immediate battlefield control by trapping opponents.

### Implementation Details
```c
constexpr Ability SandPit = {
    .onEntry = +[](ON_ENTRY) -> int { return UseEntryMove(battler, ability, MOVE_SAND_TOMB, 20); },
};
```

The ability uses the `UseEntryMove` function with:
- **Move**: `MOVE_SAND_TOMB` 
- **Base Power**: 20 (instead of Sand Tomb's normal 50 power)
- **Trigger**: On switch-in (.onEntry)

### Sand Tomb Move Properties
- **Type**: Ground
- **Category**: Physical
- **Normal Power**: 50 (reduced to 20 by this ability)
- **Accuracy**: 90% (but entry moves typically don't miss)
- **Effect**: EFFECT_TRAP - traps target for 2-5 turns
- **Target**: Selected opponent
- **PP**: 10 (irrelevant for ability usage)

### Activation Conditions
- **Switch-in trigger**: Activates when the Pokemon enters battle
- **Valid targets**: Must have at least one opposing Pokemon
- **No immunities**: Works regardless of opponent's abilities or types
- **Single use**: Activates once per switch-in

### Trap Mechanics
Once Sand Tomb hits:
- **Duration**: Traps for 2-5 turns (random)
- **Damage per turn**: 1/8 of target's max HP
- **Movement restriction**: Target cannot switch out
- **Turn-by-turn damage**: Occurs at end of each turn
- **Multiple targets**: Can trap multiple opponents in doubles/triples

### Technical Implementation Notes
The `UseEntryMove` function handles:
- Target selection (all valid opposing battlers)
- Power override (20 instead of normal move power)
- Animation and message display
- Battle script execution
- Damage calculation with custom power

### Important Interactions
- **Type effectiveness**: Ground-type, so doesn't affect Flying types or Pokemon with Levitate
- **Ability interactions**: Can be blocked by abilities like Sturdy or Wonder Guard
- **Item interactions**: Affected by items like Ground Gem or Soft Sand
- **Weather effects**: No special weather interactions
- **Terrain effects**: Not affected by terrain since it's not grounded when used

### Strategic Applications
- **Entry hazard alternative**: Provides immediate battlefield control
- **Pivot punishment**: Punishes opponents for switching
- **Doubles synergy**: Can trap multiple opponents simultaneously  
- **Stall breaking**: Forces trapped opponents to stay and take damage
- **Setup enabler**: Buys time for team setup while opponents are trapped

### Limitations
- **Type immunity**: Completely ineffective against Flying types and Levitate users
- **Low damage**: 20 base power makes it more utility than damage
- **Single activation**: Only works once per switch-in
- **No accuracy bypass**: Unlike some entry moves, this can still miss
- **Ground immunity**: Common immunities reduce effectiveness

### Comparison to Similar Abilities
- **Versus status entry moves**: Provides damage instead of status
- **Versus weather abilities**: More direct battlefield impact
- **Versus stat-changing entries**: Immediate trapping vs. long-term benefits
- **Versus other trap moves**: Weaker but automatic activation

### Competitive Viability
- **Role compression**: Combines entry presence with field control
- **Doubles potential**: More valuable in multi-target formats
- **Niche usage**: Useful on specific team archetypes
- **Prediction reward**: Benefits from good switch timing
- **Meta dependent**: Effectiveness varies with Flying-type usage

### Pokemon That Could Use This Ability
This ability would be thematically appropriate for:
- Ground-type Pokemon with sandy/desert themes
- Pokemon associated with traps or pits
- Defensive Pokemon that want to control switches
- Desert-dwelling species

### Synergistic Moves and Items
- **Arena Trap**: Stack with Arena Trap for enhanced trapping
- **Binding Band**: Extends trap damage duration
- **Grip Claw**: Guarantees maximum trap duration (5 turns)
- **Soft Sand**: Boosts the Ground-type damage
- **Leftovers**: Sustain while opponents take trap damage

### Counters and Counterplay
- **Flying types**: Complete immunity to Ground-type moves
- **Levitate ability**: Immune to Ground-type attacks
- **Rapid switching**: Minimize exposure to the ability
- **Ghost types**: Can switch out despite being trapped (generation dependent)
- **Shed Shell**: Holder can switch out of traps
- **Teleport/U-turn**: Priority switching moves may escape

### Version History and Elite Redux Context
- **Elite Redux addition**: Custom ability not in base games
- **Power balancing**: 20 power prevents it from being overpowered
- **Entry move system**: Uses established UseEntryMove framework
- **Competitive integration**: Designed for strategic depth without being oppressive

This ability represents Elite Redux's philosophy of creating unique, strategic abilities that add depth without overwhelming power levels.
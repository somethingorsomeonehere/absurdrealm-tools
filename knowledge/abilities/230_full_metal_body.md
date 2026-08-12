---
id: 230
name: Full Metal Body
status: reviewed
character_count: 130
---

# Full Metal Body - Ability ID 230

## In-Game Description
"Immune to stat drops."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Full Metal Body gives immunity to all stat reductions from moves and abilities. Includes self stat drops from moves like Overheat.

## Detailed Mechanical Explanation
*For Discord/reference use*

Full Metal Body is a defensive ability that provides complete immunity to stat drops, functioning as an enhanced version of Clear Body with additional protective properties.

### Core Mechanics
- **Stat Drop Immunity**: Completely prevents all stat reductions to Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, and Evasion
- **Universal Protection**: Works against all sources of stat reduction including moves, abilities, items, and field effects
- **No Exceptions**: Unlike Clear Body, provides protection even against "forced" stat drops that bypass other immunities

### Technical Implementation
The ability works through multiple battle system checks:

```c
// Primary stat change prevention (battle_script_commands.c:4045)
if (!BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_CLEAR_BODY) && 
    !BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_FULL_METAL_BODY)) {
    // Allow stat reduction
}

// Enhanced protection against forced reductions (battle_script_commands.c:4038)
if (flags & STAT_CHANGE_CANT_PREVENT && 
    !BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_CLEAR_BODY) &&
    !BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_FULL_METAL_BODY)) {
    // Allow "unpreventable" stat reduction
}

// Octolock immunity (battle_util.c:2563)
if (!(BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_CLEAR_BODY) || 
      BATTLER_HAS_ABILITY(gActiveBattler, ABILITY_FULL_METAL_BODY) ||
      GetBattlerHoldEffect(gActiveBattler, TRUE) == HOLD_EFFECT_CLEAR_AMULET)) {
    // Apply Octolock stat drops
}
```

### Activation Conditions
- **Passive Effect**: Always active when the Pokemon has this ability
- **No Announcement**: Does not trigger ability activation messages when preventing stat drops
- **Battle Only**: Only functions during battle encounters

### Protected Against
- **Direct Stat Moves**: Growl, Screech, Leer, Intimidate, etc.
- **Ability Effects**: Intimidate, Download (negative), Sticky Web entry, etc.
- **Item Effects**: King's Rock, Starf Berry side effects, etc.
- **Field Effects**: Octolock, certain terrain effects
- **Forced Reductions**: Moves with STAT_CHANGE_CANT_PREVENT flag
- **Multi-stat Moves**: Charm, Eerie Impulse, Noble Roar, etc.

### Differences from Clear Body
1. **Enhanced Protection**: Full Metal Body protects against forced stat drops that bypass Clear Body
2. **Identical Basic Function**: Both prevent standard stat reductions equally
3. **Code Implementation**: Uses the same battle system checks but with additional coverage

### Strategic Implications
- **Setup Sweepers**: Excellent for Pokemon that rely on stat boosts, as opponents cannot reduce their enhanced stats
- **Defensive Cores**: Maintains defensive stats against repeated stat-dropping attacks
- **Intimidate Counter**: Perfect answer to Intimidate-based team strategies
- **Hazard Immunity**: Prevents Sticky Web stat drops on switch-in

### Common Users
Full Metal Body is typically found on:
- **Steel-type Pokemon**: Thematically appropriate for metallic, rigid Pokemon
- **Defensive Walls**: Pokemon that need to maintain their defensive capabilities
- **Setup Pokemon**: Those that use stat-boosting moves and need protection

### Competitive Usage Notes
- **Priority Target**: Pokemon with Full Metal Body become high-priority targets for direct damage
- **Status Vulnerability**: Still vulnerable to status conditions (poison, burn, paralysis, etc.)
- **Taunt Weakness**: Can be shut down by Taunt if relying on setup moves
- **Entry Hazard Immunity**: Provides indirect Sticky Web immunity

### Interactions with Other Abilities/Mechanics
- **Stacks with Mist**: Works alongside team Mist support for redundant protection
- **Clear Amulet**: Provides same protection as held item alternative
- **Hyper Cutter**: Overlaps with Hyper Cutter's Attack protection
- **Keen Eye**: Overlaps with Keen Eye's Accuracy protection

### Counters
- **Direct Damage**: Focus on raw damage output rather than stat manipulation
- **Status Conditions**: Use poison, burn, paralysis to wear down the opponent
- **Taunt**: Prevent setup moves if the Pokemon relies on stat boosts
- **Entry Hazards**: Stealth Rock, Spikes still deal damage on switch-in
- **Weather**: Sandstorm and Hail chip damage (unless immune)

### Synergies
- **Stat-Boosting Moves**: Calm Mind, Swords Dance, Dragon Dance become more reliable
- **Leftovers**: Passive recovery helps maintain longevity
- **Assault Vest**: Special bulk items work well with guaranteed stat maintenance
- **Choice Items**: Can maintain stat integrity while locked into powerful moves

### Version History
- **Elite Redux**: Full Metal Body provides enhanced protection compared to standard Clear Body
- **Unique Implementation**: Features additional safeguards against forced stat reductions
- **Battle System Integration**: Deeply integrated into the battle engine's stat change logic

### Example Damage Calculations
Since Full Metal Body prevents stat drops rather than modifying damage, there are no direct damage calculations. However, the ability ensures that:
- Base damage calculations remain consistent throughout battle
- Defensive stats maintain their full effectiveness
- Setup sweepers can maintain their boosted offensive stats

### Ability Priority
Full Metal Body takes precedence over most stat-reducing effects, functioning as a hard immunity rather than a resistive effect.
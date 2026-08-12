---
id: 52
name: Hyper Cutter
status: reviewed
character_count: 186
---

# Hyper Cutter - Ability ID 52

## In-Game Description
"Enemies can't lower Atk/SpAtk. Contact moves get +1 Crit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Hyper Cutter prevents enemies from lowering the user's Attack stat through moves or abilities. All contact moves used by this Pokemon have their critical hit rate increased by one stage.

## Detailed Mechanical Explanation
*For Discord/reference use*

**HYPER CUTTER** is a dual-function ability that provides both stat protection and offensive enhancement in Elite Redux.

### Stat Protection Mechanics:
- **Protection**: Prevents Attack and Special Attack from being lowered by opposing moves or abilities
- **Trigger**: Activates when any opposing source attempts to reduce STAT_ATK or STAT_SPATK
- **Protected Stats**: Attack (-1 to -6 stages) and Special Attack (-1 to -6 stages)
- **Unprotected Stats**: Defense, Special Defense, Speed, Accuracy, Evasion can still be lowered
- **Message**: Shows ability popup and "It doesn't affect [Pokemon]!" when protection activates

### Critical Hit Enhancement:
- **Trigger**: All contact moves (physical moves that make contact with the target)
- **Effect**: +1 critical hit stage (doubles the base critical hit ratio)
- **Base Crit Rate**: Most moves go from 6.25% (1/16) to 12.5% (1/8) critical hit chance
- **Stacking**: Works with other crit-boosting effects (high crit ratio moves, items, etc.)

### Technical Implementation:
```c
constexpr Ability HyperCutter = {
    .onCrit = +[](ON_CRIT) -> int {
        CHECK(IsMoveMakingContact(move, battler))
        return 1;  // +1 crit stage for contact moves
    },
    .breakable = TRUE,  // Can be suppressed by Mold Breaker
};

// Stat protection handled in battle_script_commands.c:
// Blocks stat reduction when:
// (BATTLER_HAS_ABILITY(battler, ABILITY_HYPER_CUTTER) && 
//  (statId == STAT_ATK || statId == STAT_SPATK))
```

### Contact Move Examples:
**Common Contact Moves that get +1 Crit:**
- Tackle, Quick Attack, Body Slam, Double-Edge
- Punch moves: Mach Punch, Ice Punch, Fire Punch, Thunder Punch
- Slash, Night Slash, Psycho Cut, Leaf Blade (already high crit + Hyper Cutter = very high crit)
- U-turn, Flip Turn (pivoting moves)
- Most physical moves except: Earthquake, Rock Slide, Stone Edge, Flamethrower-type moves

**Non-Contact Moves (no crit bonus):**
- Earthquake, Rock Slide, Surf, Flamethrower
- Projectile moves: Shadow Ball, Aura Sphere, Focus Blast
- Most special attacks

### Stat Protection Interactions:
**Blocked Moves/Effects:**
- Intimidate: Complete immunity, no Attack reduction
- Growl, Leer (Attack reduction portion), Tickle (Attack portion)
- Charm, Sweet Kiss effects on Attack/Special Attack
- Stat-lowering secondary effects on protected stats

**NOT Blocked:**
- Self-inflicted stat drops (Overheat reducing own Special Attack)
- Stat drops from abilities that affect the user
- Other stat reductions (Defense, Speed, etc.)
- Stat reductions from status conditions

### Competitive Applications:

**Offensive Synergy:**
- High-crit contact moves become extremely reliable (Leaf Blade, Night Slash, etc.)
- Pairs well with Scope Lens or Razor Claw for even higher crit rates
- Physical attackers benefit from both crit boost and Attack protection
- Excellent for revenge killers and physical sweepers

**Defensive Utility:**
- Complete immunity to Intimidate cycling strategies
- Protects setup sweepers from having Attack/Special Attack weakened
- Maintains offensive pressure even against stat-lowering teams
- Valuable against utility moves like Growl, Charm, and Tickle

**Strategic Considerations:**
- **Limited Protection**: Only covers Attack and Special Attack, not all stats
- **Mold Breaker Vulnerability**: Can be bypassed by Mold Breaker abilities
- **Contact Requirement**: Crit bonus only applies to contact moves
- **Physical Focus**: Benefits physical attackers more than special attackers

### Notable Users:
- **Galarian Farfetch'd**: Combines with Fighting-type STAB contact moves
- **Crabominable**: Benefits both abilities with powerful contact Ice/Fighting moves
- **Various Rock/Water types**: Access to contact moves like Aqua Jet, Ice Punch

### Interaction Priority:
- Stat protection activates during damage calculation/stat modification phase
- Critical hit bonus calculated during hit chance determination
- Works alongside other crit-enhancing abilities (does not stack with Super Luck)
- Protection cannot be bypassed except by Mold Breaker variants

### Version Notes:
- Elite Redux: Enhanced from original with critical hit bonus addition
- Original games: Only provided Attack stat protection (not Special Attack)
- Elite Redux expansion: Both Attack AND Special Attack protection + crit bonus
- Message: Uses standard "It doesn't affect [Pokemon]!" for stat protection
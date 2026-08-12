---
id: 219
name: Dazzling
status: reviewed
character_count: 79
---

# Dazzling - Ability ID 219

## In-Game Description
"Protects itself and ally from priority moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Dazzling blocks all priority moves from opponents targeting the user or allies.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- Blocks any move with priority greater than 0 from opposing Pokemon
- Provides protection to both the user and any ally Pokemon (in doubles/multi battles)
- Uses the same immunity system as Queenly Majesty - they share identical code implementation
- Cannot be bypassed by Mold Breaker or similar ignore-ability effects (ability is marked as unbreakable: FALSE, meaning it CAN be broken)

### Activation Conditions
- Only blocks moves from opposing Pokemon (same-side moves are unaffected)
- Does not activate during "extra attacks" (follow-up moves, retaliation effects)
- Must be an attack or status move with positive priority
- Works in all battle formats (singles, doubles, multi battles)

### Technical Implementation
```cpp
constexpr Ability Dazzling = {
    .onImmune = QueenlyMajesty.onImmune,  // Shares code with Queenly Majesty
    .onImmuneFor = APPLY_ON_ALLY,         // Protects allies too
    .breakable = TRUE,                    // Can be bypassed by Mold Breaker
};

// The actual blocking logic (from QueenlyMajesty):
.onImmune = +[](ON_IMMUNE) -> int {
    CHECK_NOT(gProcessingExtraAttacks)                    // No blocking during extra attacks
    CHECK(GetBattlerSide(attacker) != GetBattlerSide(battler))  // Only block opponents
    CHECK(GetMovePriority(attacker, move, battler) > 0);  // Only priority moves
    *immunityScript = BattleScript_DazzlingProtected;     // Display protection message
    return TRUE;
},
```

### Complete List of Blocked Moves
**Priority +1 Moves:** Quick Attack, Aqua Jet, Bullet Punch, Mach Punch, Shadow Sneak, Ice Shard, Vacuum Wave, Water Shuriken

**Priority +2 Moves:** Extremespeed, Feint, First Impression

**Priority +3 Moves:** Fake Out, Quick Guard

**Priority Status Moves:** Thunder Wave (+1), Spore (+1), Sleep Powder (+1), Stun Spore (+1), Paralyze moves with Prankster (+1)

**Priority Switching:** U-turn/Volt Switch with increased priority from abilities

### Interactions with Other Abilities/Mechanics
- **Mold Breaker/Teravolt/Turboblaze:** CAN bypass Dazzling (breakable = TRUE)
- **Prankster:** Status moves gain +1 priority and are blocked by Dazzling
- **Queenly Majesty:** Identical effect - they use the same implementation code
- **Triage:** Healing moves gain +3 priority and are blocked
- **Gale Wings:** Flying moves gain +1 priority and are blocked
- **Quick Claw/Custap Berry:** These affect turn order, not move priority - NOT blocked

### Strategic Implications
- **Offensive Use:** Protects frail but powerful Pokemon from priority revenge kills
- **Defensive Use:** Prevents priority status moves from shutting down setup sweepers
- **Team Support:** In doubles, protects both team members from priority harassment
- **Anti-Meta:** Counters priority-reliant strategies and Prankster users

### Example Damage Calculations
Dazzling doesn't affect damage calculations - it provides complete immunity to priority moves. When activated, the attacking move fails entirely with the message "Dazzling protected [Pokemon]!"

### Common Users in Elite Redux
Based on the species list analysis, Dazzling appears on various Pokemon types:
- **Fairy-types:** Often as support for team protection
- **Electric-types:** Combined with offensive abilities for safe setup
- **Water-types:** Protecting Swift Swim sweepers from priority moves
- **Psychic-types:** Supporting frail special attackers
- **Mixed roles:** Both as innate and regular abilities across different tiers

### Competitive Usage Notes
- **Priority:** High priority in formats with common priority moves
- **Doubles/Multi:** More valuable due to ally protection
- **Setup Teams:** Essential for protecting setup sweepers
- **Anti-Prankster:** Hard counters Prankster-based strategies
- **Tier Placement:** Appears across all difficulty tiers in Elite Redux

### Counters
- **Mold Breaker family:** Bypasses the immunity entirely
- **Non-priority moves:** Standard speed-based attacks work normally  
- **Status immunity:** Pokemon immune to status aren't affected by priority status protection
- **Switching:** Forces switches still work if they don't rely on priority

### Synergies  
- **Setup moves:** Protects during Calm Mind, Dragon Dance, etc.
- **Frail sweepers:** Prevents revenge killing of glass cannons
- **Status spreaders:** Safe setup for Toxic Spikes, Stealth Rock users
- **Speed control:** Works well with Tailwind, Trick Room teams

### Version History
- Introduced in Generation VII (Sun/Moon)
- Elite Redux implementation: Identical to mainline games
- Coding: Shares implementation with Queenly Majesty for consistency
- No unique Elite Redux modifications - standard priority blocking behavior
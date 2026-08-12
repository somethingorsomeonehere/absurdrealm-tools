---
id: 235
name: Dauntless Shield
status: reviewed
character_count: 78
---

# Dauntless Shield - Ability ID 235

## In-Game Description
"On entry, raises Defense by one stage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Dauntless Shield immediately raises Defense by one stage when entering battle.

## Detailed Mechanical Explanation
*For Discord/reference use*

Dauntless Shield is an entry-based ability that provides an immediate defensive boost upon entering battle. Here's how it works:

### Activation Conditions
- Triggers when the Pokemon enters battle through any means:
  - Normal switching
  - Battle start
  - Revival from fainting
  - Forced switching (Roar, Whirlwind, etc.)

### Mechanics
- Raises Defense by exactly 1 stage (+50% Defense)
- Uses the standard stat boost system (same as Defense Curl, Harden, etc.)
- Cannot be prevented by abilities like Clear Body or White Smoke
- Will not activate if Defense is already at maximum (+6 stages)
- Stacks with other Defense boosts and items

### Strategic Applications
- Provides immediate bulk for defensive Pokemon
- Particularly valuable on switch-ins to resist physical attacks
- Synergizes well with other defensive abilities and items
- Most effective on Pokemon with already high Defense stats

### Interactions
- Works with Eviolite and other defensive items
- Stacks with other stat-boosting abilities
- Can be copied by Trace but not by abilities like Skill Swap
- Unaffected by Mold Breaker or similar abilities

### Elite Redux Context
In Elite Redux's 4-ability system, Dauntless Shield appears as both a regular ability and an innate ability on various defensive Pokemon, providing consistent defensive utility alongside other abilities. It's particularly common on Steel-type and defensive Pokemon that benefit from the immediate bulk increase.

The ability is implemented using the standard onEntry callback system and uses the same stat modification mechanics as other stat-boosting abilities in the game.
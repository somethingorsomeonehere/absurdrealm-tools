---
id: 546
name: Salt Circle
status: reviewed
character_count: 177
---

# Salt Circle - Ability ID 546

## In-Game Description
"Automatically traps all opposing Pokemon when entering battle."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all opposing Pokemon from fleeing or switching when user enters battle. Effect lasts until user leaves field. Forced switches and pivot moves like Flip Turn still work.

## Detailed Mechanical Explanation

Salt Circle automatically traps all opposing Pokemon when the user enters battle, preventing them from fleeing or switching out normally. Functions as an automatic Mean Look that affects all opponents simultaneously.

### Mechanics
- **Trigger**: On entry to battle (switch-in or battle start)
- **Effect**: Applies STATUS2_ESCAPE_PREVENTION to all opposing Pokemon
- **Scope**:
  - Singles: Affects the single opponent
  - Doubles: Affects BOTH opponents
- **Duration**: Persists as long as the user remains on field
- **Message**: Announces the trapping effect on switch-in

### Code Implementation
Located in `src/abilities.cc` as an onEntry effect:
1. Checks if opposing Pokemon are alive
2. Applies escape prevention status if not already present
3. Records which Pokemon is preventing escape
4. Displays switch-in message

### What It Prevents
- **Wild Pokemon**: Cannot flee or run away
- **Trainer Battles**: Pokemon cannot switch out normally
- **NOT Prevented**: Forced switches (Roar, Whirlwind, U-turn, Volt Switch, etc.)

### AI Scoring
Uses `AI_SCORE_TRAP` for both opponents in doubles:
```c
AI_SCORE_TRAP(battlerDef) + AI_SCORE_TRAP(BATTLE_PARTNER(battlerDef))
```

### Strategic Applications
- **Matchup Lock**: Forces opponents to stay in unfavorable matchups
- **Setup Enabler**: Prevents switching while setting up
- **Hazard Synergy**: Maximizes entry hazard damage
- **Catch Rate**: Guarantees wild Pokemon cannot flee
- **Double Battle Control**: Traps both opponents simultaneously


---
id: 326
name: Impenetrable
status: reviewed
character_count: 133
---

# Impenetrable - Ability ID 326

## In-Game Description
Provides comprehensive protection against all forms of indirect damage.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Impenetrable grants immunity to all non-attack damage sources including entry hazards, weather damage, status conditions, and recoil.

## Detailed Mechanical Explanation

### Mechanics

### Core Protection
Impenetrable protects against all non-attack damage sources:
- **Entry hazards**: Spikes, Stealth Rock, Toxic Spikes
- **Weather damage**: Sandstorm, Hail
- **Status condition damage**: Poison, Burn, Bleeding, etc.
- **Recoil damage**: From moves like Take Down, Double-Edge
- **Other indirect damage**: Life Orb recoil, Curse damage, etc.

### Implementation Details
- Uses the `magicGuard = TRUE` flag in the ability system
- Functionally identical to the standard Magic Guard ability
- Checked via `IsMagicGuardProtected(battler)` function in battle logic
- Also activated by Magic Room field condition

### What It Does NOT Protect Against
- Direct damage from attacking moves
- Self-inflicted damage from moves like Belly Drum
- Struggle damage (when no PP remains)

## Extended In-Game Description
**Character Count Check**: Let me count the extended description characters:

"Immune to all indirect damage sources: entry hazards (Spikes/Stealth Rock/Toxic Spikes), weather damage (Sandstorm/Hail), status damage (Poison/Burn/Bleeding), recoil damage (from moves/Life Orb), and other non-attack damage. Only direct attack moves can hurt this Pkmn. Struggle still damages."

Let me count: "Immune to all indirect damage sources: entry hazards (Spikes/Stealth Rock/Toxic Spikes), weather damage (Sandstorm/Hail), status damage (Poison/Burn/Bleeding), recoil damage (from moves/Life Orb), and other non-attack damage. Only direct attack moves can hurt this Pkmn. Struggle still damages." = 292 characters.

**Extended Description (292 characters):**
"Immune to all indirect damage sources: entry hazards (Spikes/Stealth Rock/Toxic Spikes), weather damage (Sandstorm/Hail), status damage (Poison/Burn/Bleeding), recoil damage (from moves/Life Orb), and other non-attack damage. Only direct attack moves can hurt this Pkmn. Struggle still damages."

## Battle Applications

### Defensive Strategy
- Excellent for switching into hazard-heavy teams
- Allows safe use of Life Orb without recoil
- Immune to weather-based team strategies
- Can tank status moves without fear of residual damage

### Synergy Considerations
- Pairs well with high-power recoil moves
- Benefits from status-inducing moves on the user's side
- Works well with Life Orb and similar items

## Code Implementation

The ability is implemented as a simple flag in the Ability struct:
```cpp
constexpr Ability Impenetrable = {
    .magicGuard = TRUE,
};
```

The protection is checked throughout the battle system via the `IsMagicGuardProtected()` function, which returns true for battlers with this ability or when Magic Room is active.

## Related Systems
- **Magic Room**: Field condition that grants Magic Guard effect to all Pokemon
- **IsMagicGuardProtected()**: Central function for checking protection
- **Entry hazard system**: Spikes and Stealth Rock damage calculation
- **Weather damage system**: Sandstorm and Hail end-of-turn effects
- **Status damage system**: Poison, Burn, and other DoT effects

## Competitive Impact

### Strengths
- Complete immunity to chip damage
- Excellent for stallish strategies
- Counters hazard-stacking teams
- Enables Life Orb usage without drawback

### Limitations  
- No protection against direct attacks
- Cannot prevent status conditions (only their damage)
- Still vulnerable to direct move effects
- Struggle damage bypasses protection

## Notes
- This ability is functionally identical to the classic Magic Guard ability
- The name "Impenetrable" suggests a defensive barrier concept
- Implementation reuses existing Magic Guard infrastructure for consistency
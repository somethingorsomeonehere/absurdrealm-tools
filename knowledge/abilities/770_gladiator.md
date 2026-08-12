---
id: 770
name: Gladiator
status: reviewed
character_count: 77
---

# Gladiator - Ability ID 770

## In-Game Description
"Boosts Fighting-type moves by 1.3x, or 1.8x when below 1/3 HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of Fighting-type moves by 30%, or by 80% at 1/3 HP or lower.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Gladiator** is a powerful Fighting-type boosting ability that operates on a two-tier damage multiplier system based on the user's current HP percentage:

### Damage Multipliers
- **Normal State (HP > 1/3)**: Fighting-type moves deal 1.3x damage (30% increase)
- **Desperate State (HP <= 1/3)**: Fighting-type moves deal 1.8x damage (80% increase)

### Implementation Details
- Uses the `BOOSTED_SWARM_MULTIPLIER(TYPE_FIGHTING)` macro in the codebase
- Triggers on `onOffensiveMultiplier` when the move type matches `TYPE_FIGHTING`
- HP threshold calculation: `gBattleMons[battler].hp <= (gBattleMons[battler].maxHP / 3)`
- Only affects moves of Fighting type - does not boost other types

### Strategic Applications
1. **Early Game Pressure**: The 30% boost makes Fighting moves significantly more threatening from the start
2. **Comeback Potential**: The 80% boost at low HP can turn desperate situations into victory
3. **Risk/Reward Gameplay**: Encourages risky play to reach the desperate state for maximum damage
4. **STAB Synergy**: Stacks multiplicatively with STAB (Same Type Attack Bonus) for devastating damage

### Similar Abilities
- **Hellblaze** (Fire-type version)
- **Riptide** (Water-type version) 
- **Forest Rage** (Grass-type version)
- **Purgatory** (Ghost-type version)
- **Rockhard Shaft** (Rock-type version)

### Competitive Viability
Gladiator is exceptionally powerful on Fighting-type Pokemon, especially those with:
- High Attack stats to maximize the damage boost
- Access to powerful Fighting moves like Close Combat, Superpower
- Bulk to survive long enough to reach the desperate state
- Priority moves to capitalize on the low-HP boost

The ability transforms the user into a formidable late-game threat while maintaining early-game pressure, making it one of the strongest type-boosting abilities in Elite Redux.
---
id: 138
name: Flare Boost
status: reviewed
character_count: 122
---

# Flare Boost - Ability ID 138

## In-Game Description
"Ups Sp. Atk by 1.5x if burned. Ignites in fog."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Raises the Pokemon's Special Attack stat by 50% when burned. Negates burn damage. Immediately applies burn to self in fog. 

## Detailed Mechanical Explanation

Flare Boost is a powerful ability designed for special attackers that turns the normally detrimental burn status into an offensive advantage:

### Primary Effects:
1. **Special Attack Boost**: When burned, the Pokemon's Special Attack is multiplied by 1.5x (50% increase)
2. **Burn Damage Immunity**: The Pokemon takes no damage from burn status at the end of each turn
3. **Attack Reduction**: The normal burn effect of halving physical Attack still applies (though this typically doesn't matter for special attackers)

### Auto-Burn Mechanics:
1. **On Entry**: When the Pokemon enters battle, it automatically burns itself (if it can be burned)
2. **Fog Activation**: When fog weather begins while the Pokemon is on the field, it automatically burns itself
3. **Burn Check**: The auto-burn only triggers if the Pokemon can actually be burned (not already burned, not Fire-type)

### Technical Details:
- The ability uses a handler function that checks if the Pokemon can be burned and if it's affected by fog weather
- The Special Attack boost is applied through the onStat callback, specifically checking for STAT_SPATK
- The burn damage immunity is implemented through a check in the end-turn effects that skips burn damage for Flare Boost users
- Fire Sea terrain damage still affects the Pokemon normally (only burn status damage is negated)

### Strategic Considerations:
- Excellent for special attackers who don't rely on physical moves
- Provides status immunity to other conditions since burn takes priority
- Synergizes with fog teams or self-inflicted burn strategies
- The automatic burn can be prevented by being Fire-type or already having a status condition

### Comparison to Similar Abilities:
- Similar to Toxic Boost but for Special Attack and burn instead of Physical Attack and poison
- Unlike Guts, only boosts Special Attack and doesn't ignore the Attack reduction from burn
- More reliable than abilities requiring specific weather since it can self-activate
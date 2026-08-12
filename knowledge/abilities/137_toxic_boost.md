---
id: 137
name: Toxic Boost
status: reviewed
character_count: 210
---

# Toxic Boost - Ability ID 137

## In-Game Description
"Ups Atk by 1.5x if poisoned. Immune to Poison status damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Increases the Pokemon's Attack stat by 50% when poisoned (regular or badly poisoned). Immediately applies poison to user when in Toxic Terrain, regardless of them being grounded or not. Nullifies poison damage.

## Detailed Mechanical Explanation
Toxic Boost is a powerful ability that turns the normally harmful poison status into an offensive advantage:

**Attack Boost Mechanics:**
- Grants a 1.5x multiplier to physical Attack when the Pokemon is poisoned
- Works with both regular poison and badly poisoned (toxic) status
- The boost applies only to physical moves, not special moves
- Calculated as a damage multiplier during damage calculation, not a stat stage change
- Stacks multiplicatively with other damage modifiers like Choice Band or STAB

**Poison Immunity Mechanics:**
- Completely prevents all poison damage, including:
  - Regular poison damage (1/8 max HP per turn)
  - Badly poisoned increasing damage (1/16, 2/16, 3/16, etc.)
  - Field poison damage when walking in the overworld
- The Pokemon can still become poisoned and suffers other poison effects (like being unable to use Rest)
- Toxic Waste field effect damage is also prevented

**Strategic Applications:**
- Commonly paired with Toxic Orb to self-inflict poison for a reliable Attack boost
- Provides a safer alternative to Guts since it prevents the damage from poison
- Particularly effective on physical attackers who can afford the item slot for Toxic Orb
- Can switch into Toxic or poison moves to activate the boost
- Synergizes well with Facade, which has increased power when statused

**Comparison to Similar Abilities:**
- Similar to Guts but only boosts Attack when poisoned (not other statuses)
- Unlike Guts, prevents the poison damage entirely
- Flare Boost is the special attack equivalent for burn status
- More specialized than Guts but provides complete immunity to poison damage as compensation

The ability is coded to check for any poison status (`STATUS1_PSN_ANY`) and applies the multiplier during the offensive damage calculation phase, making it a clean and efficient implementation that doesn't interfere with other damage calculations.
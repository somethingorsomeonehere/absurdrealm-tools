---
id: 239
name: Propeller Tail
status: reviewed
character_count: 145
---

# Propeller Tail - Ability ID 239

## In-Game Description
"Swift Swim + Redirection Immunity."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Propeller Tail boosts the user's Speed by 50% during rain and grants immunity to redirection effects. The speed boost works in all forms of rain. 

## Detailed Mechanical Explanation
*For Discord/reference use*

Propeller Tail is a combination ability that provides two distinct effects:

### Swift Swim Component
- Increases Speed stat by 50% (multiplier of 1.5) when rain weather is active
- Activates during any form of rain weather (regular rain, heavy rain, Primordial Sea)
- The speed boost applies immediately when rain becomes active and disappears when rain ends
- Stacks multiplicatively with other speed modifiers like Choice Scarf or speed stages

### Redirection Immunity Component
- Prevents the Pokemon's moves from being redirected by opponent abilities
- Immunity applies to all redirection abilities including:
  - Lightning Rod (Electric-type moves)
  - Storm Drain (Water-type moves)
  - Sap Sipper (Grass-type moves)
  - Flash Fire (Fire-type moves)
  - Water Absorb (Water-type moves)
  - Volt Absorb (Electric-type moves)
  - Motor Drive (Electric-type moves)
  - And other custom redirection abilities in Elite Redux

### Technical Implementation
- The ability uses the same `onStat` function as Swift Swim for the speed boost
- Redirection immunity is implemented in the `HasRedirectionAbility` function in battle_util.c
- When a Pokemon with Propeller Tail attacks, `HasRedirectionAbility` returns `ABILITY_NONE`, preventing redirection
- This immunity works similarly to the moves that naturally bypass redirection (like Snipe Shot)

### Strategic Applications
- Excellent for fast Rain Dance sweepers that need guaranteed target accuracy
- Prevents opponents from using redirection abilities to protect frail teammates
- Particularly useful in doubles battles where redirection is more common
- The combination makes it ideal for fast, precise attackers in rain teams

### Pokemon with Propeller Tail
This ability is typically found on aquatic Pokemon with propeller-like tails or fins, reflecting both the speed boost in rain and the precision targeting theme.
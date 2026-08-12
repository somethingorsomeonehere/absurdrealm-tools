---
id: 242
name: Stalwart
status: reviewed
character_count: 126
---

# Stalwart - Ability ID 242

## In-Game Description
"Isn't affected by target redirection."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Stalwart prevents the Pokemon from being affected by target redirection effects and effects that remove or suppress abilities.

## Detailed Mechanical Explanation
*For Discord/reference use*

Stalwart is a defensive ability that provides immunity to all forms of target redirection in battle. When a Pokemon with Stalwart uses a move, that move cannot be redirected by:

### Target Redirection Abilities Blocked:
- **Lightning Rod**: Usually redirects Electric-type moves and boosts Special Attack
- **Storm Drain**: Usually redirects Water-type moves and boosts Special Attack  
- **Sap Sipper**: Usually redirects Grass-type moves and boosts Attack
- **Reservoir**: Elite Redux custom ability that redirects Water-type moves
- **Heat Sink**: Elite Redux custom ability that redirects Fire-type moves
- **Ice Dew**: Elite Redux custom ability that redirects Ice-type moves
- **Any other ability with a `redirectType` flag**

### Target Redirection Moves Blocked:
- **Follow Me**: Forces all opposing moves to target the user
- **Rage Powder**: Forces all opposing moves to target the user (except Grass-types and Overcoat users)

### Technical Implementation:
The ability works by making the `HasRedirectionAbility()` function return `ABILITY_NONE` when the attacking Pokemon has Stalwart. This is implemented alongside Propeller Tail and the move Snipe Shot, which have similar redirection immunity.

The key code check occurs in battle calculations:
```c
if (BattlerHasAbility(battlerAtk, ABILITY_STALWART, FALSE)) 
    return ABILITY_NONE;
```

### Strategic Applications:
1. **Breaking through defensive strategies** that rely on redirecting powerful moves away from frail sweepers
2. **Guaranteed targeting** in doubles/multi battles where opponents use Follow Me or similar tactics
3. **Countering specific team compositions** built around Lightning Rod/Storm Drain users
4. **Reliable move execution** without worrying about redirection interference

### Similar Effects:
- **Propeller Tail**: Has the same redirection immunity plus Swift Swim
- **Snipe Shot (move)**: Individual move with redirection immunity plus high critical hit ratio

Stalwurt is particularly valuable in doubles and multi battles where target redirection is more common and can significantly disrupt offensive strategies.
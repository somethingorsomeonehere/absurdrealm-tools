---
id: 532
name: Permanence
status: reviewed
character_count: 252
---

# Permanence - Ability ID 532

## In-Game Description
"Foes can't heal in any way."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Prevents all opposing Pokemon from healing through any means. Blocks healing moves like Recover, absorbing moves like Drain Punch, passive healing from Leftovers and abilities like Regenerator, and prevents health recovery from berries and other items.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Permanence completely prevents all forms of healing for opposing Pokemon while the user is on the field. This includes:

**Healing Moves Blocked:**
- Direct healing moves: Recover, Roost, Synthesis, Moonlight, Morning Sun, Soft-Boiled, Milk Drink, Slack Off, Heal Order, Shore Up
- Draining moves: Absorb, Mega Drain, Giga Drain, Drain Punch, Draining Kiss, Dream Eater, Leech Life, Horn Leech, Parabolic Charge
- Wish and Healing Wish
- Strength Sap
- Heal Pulse (targeting opposing Pokemon)
- Revival Blessing
- Jungle Healing
- Rest (prevents the healing portion)

**Passive Healing Blocked:**
- Leftovers item
- Black Sludge (for Poison types)
- Shell Bell
- Sitrus Berry and other healing berries
- Ability-based healing: Regenerator, Poison Heal, Rain Dish, Dry Skin (healing portion), Ice Body, Hydration (healing portion)
- End-of-turn healing: Ingrain, Aqua Ring
- Contact healing: Rough Skin (when it heals), Effect Spore (healing variants)
- Cheek Pouch (Gluttony/Sugar Rush berry healing)

### Activation Conditions
- Ability activates immediately when the Pokemon enters battle
- Effects all opposing Pokemon while the user remains on the field
- Displays a switch-in message: "{Pokemon}'s Permanence prevents healing!"

### Technical Implementation
```c
// From battle_util.c CanBattlerHeal function
if (IsAbilityOnOpposingSide(battler, ABILITY_PERMANENCE)) return FALSE;
```

The ability works by making the `CanBattlerHeal()` function return FALSE for any Pokemon on the opposing side. This is checked before any healing effect is applied, making the prevention absolute.

### Interactions with Other Mechanics
- **Heal Block**: Functions similarly to the Heal Block status condition but is permanent while the user is active
- **Hemolysis**: Works alongside Permanence - Hemolysis prevents healing for poisoned Pokemon specifically
- **Blood Stain**: Another healing prevention effect that works independently
- **Bleed Status**: Also prevents healing but is a status condition rather than an ability
- **Magic Guard**: Cannot bypass Permanence prevention
- **Big Root**: Cannot amplify healing that is prevented by Permanence

### Strategic Implications
**Offensive Use:**
- Excellent for stall-breaking and preventing defensive Pokemon from recovering
- Forces opponents to rely on switching out to heal via Pokemon Center
- Particularly effective against walls that rely on recovery moves
- Pairs well with chip damage strategies (Stealth Rock, Spikes, Toxic)

**Counters:**
- Switching out removes the healing prevention
- Magic Bounce cannot reflect the ability's effects
- Mold Breaker/Teravolt/Turboblaze cannot bypass the healing prevention
- Gastro Acid can remove the ability

### Example Damage Calculations
Against a Pokemon with Leftovers that would normally heal 1/16 HP per turn:
- **Without Permanence**: Recovers 6.25% HP each turn
- **With Permanence**: 0% HP recovery, takes full chip damage

Against Regenerator Pokemon:
- **Without Permanence**: Recovers 33% HP when switching out
- **With Permanence**: 0% HP recovery when switching out

### Common Users
- **Galarian Slowking**: Bulky Psychic/Poison type with innate Permanence
- **Mega Garbodor**: Poison/Steel defensive pivot
- **Mega Galarian Slowking**: Enhanced bulk with permanent healing prevention

### Competitive Usage Notes
**Tier 4 Viability**: Permanence users are in Tier 4, making them viable for high-level competitive play.

**Team Synergy:**
- Pairs excellently with hazard setters (Stealth Rock, Spikes, Toxic Spikes)
- Works well with Toxic and other residual damage sources
- Strong anti-stall presence on balanced teams

**Meta Impact:**
- Forces defensive teams to play more aggressively
- Makes recovery moves significantly less reliable as win conditions
- Encourages more offensive team structures

### Version History
- Added in Elite Redux as a unique healing prevention ability
- Distinguished from temporary Heal Block by being permanent while user is active
- Part of the expanded ability system with ID 532

### Related Abilities
- **Heal Block** (move effect): Temporary healing prevention
- **Hemolysis**: Healing prevention specifically for poisoned foes
- **Blood Stain**: Area-based healing prevention

This ability represents one of the most comprehensive anti-healing tools in Elite Redux, fundamentally changing how defensive strategies must be approached in its presence.
---
id: 681
name: Atomic Punch
status: reviewed
character_count: 200
---

# Atomic Punch - Ability ID 681

## In-Game Description
"Iron Fist + 30% Steel type damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts the power of punching moves by 30%. Converts Normal-type moves to Steel-type and grants STAB for Steel moves regardless of typing. Additionally takes half damage from Dark and Ghost-type moves.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
- **Iron Fist Component**: Provides a 1.3x damage multiplier to all punching moves
- **Steely Spirit Component**: Provides a 1.3x damage multiplier to all Steel-type moves
- **Stacking**: When using Steel-type punching moves, both multipliers apply multiplicatively (1.3 × 1.3 = 1.69x total boost)

### Activation Conditions
- Iron Fist boost: Automatically applies to any punching move (Thunder Punch, Fire Punch, Ice Punch, Bullet Punch, Meteor Mash, Mach Punch, Hammer Arm, etc.)
- Steel boost: Automatically applies to any Steel-type move regardless of physical/special category
- No weather, terrain, or other conditions required

### Technical Implementation
- Implemented in `abilities.cc` as a combination ability
- Uses both `IronFist.onOffensiveMultiplier` and `SteelySpirit.onOffensiveMultiplier`
- Both effects are calculated in the damage formula during the offensive multiplier phase

### Interactions with Other Mechanics
- **STAB**: Stacks multiplicatively with Same Type Attack Bonus
- **Items**: Stacks with Choice Band, Life Orb, and other damage-boosting items
- **Weather/Terrain**: No special interactions, but benefits stack
- **Critical Hits**: Applies before critical hit calculation
- **Type Effectiveness**: Applies after type effectiveness calculation

### Strategic Implications
- Creates one of the strongest physical Steel-type attackers in the game
- Particularly powerful on Pokemon with access to Bullet Punch for priority
- Makes Meteor Mash an extremely powerful option with its chance to boost Attack
- Encourages a mixed moveset of both punching and Steel-type coverage

### Common Users
- **Mega Melmetal**: The signature user, having this as its only ability option
- Benefits from high Attack stat and access to powerful Steel-type punching moves
- Also has Iron Giant and Steely Spirit as innate abilities for additional synergy

### Competitive Usage Notes
- Essential for physical Steel-type sweepers and wallbreakers
- Priority Bullet Punch with this ability can revenge kill many threats
- The dual boost makes even resisted hits deal significant damage
- Particularly effective against Fairy and Ice types

### Counters and Counterplay
- Fire-type Pokemon resist Steel moves and threaten with super effective damage
- Burn status reduces physical damage output
- Intimidate can help reduce the threat
- Ghost types are immune to most punching moves
- Protective Pads item negates contact move effects

### Synergies
- **Choice Band**: Further amplifies the already boosted damage
- **Adamant/Brave Nature**: Maximizes Attack for devastating hits
- **Trick Room**: Compensates for typically slow Steel-type users
- **Dual Screens**: Provides setup opportunity for slower attackers
- **Entry Hazard Support**: Helps secure KOs with chip damage
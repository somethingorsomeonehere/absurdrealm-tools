---
id: 456
name: Cryomancy
status: reviewed
character_count: 115
---

# Cryomancy - Ability ID 456

## In-Game Description
"Moves inflict frostbite 5x as often."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Cryomancy multiplies the chance of inflicting frostbite by 5x on all moves. 
Does not interact with Freezing Point.
## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cryomancy is an offensive ability that dramatically increases the likelihood of inflicting the frostbite status condition. When a Pokemon with Cryomancy uses a move that has a chance to cause frostbite, that chance is multiplied by 5.

### Activation Conditions
- **Move requirement**: Must use a move that can inflict frostbite
- **Effect multiplication**: Takes the base frostbite chance and multiplies by 5
- **Examples**:
  - Ice Fang: 10% base chance becomes 50% with Cryomancy
  - Bitter Malice: 30% base chance becomes 150% (guaranteed frostbite)

### Frostbite Status Condition
Frostbite is a status condition similar to burn but affecting special attacks:
- **Damage**: Deals 1/16 of max HP each turn (same as burn in Gen 7+)
- **Special Attack reduction**: Halves special attack power
- **Cure conditions**: Can be cured by moves with FLAG_THAW_USER or berries that cure freeze
- **Facade interaction**: Frostbite doubles Facade's power
- **Visual**: Uses the same icon as freeze status

### Technical Implementation
```c
constexpr Ability Cryomancy = {
    .onModifyEffectChance =
        +[](ON_MODIFY_EFFECT_CHANCE) {
            if (moveEffect == MOVE_EFFECT_FROSTBITE) *effectChance *= 5;
        },
};
```

### Moves That Can Inflict Frostbite
- **Ice Fang**: Physical Ice move, 10% base chance (50% with Cryomancy)
- **Bitter Malice**: Special Ghost move, 30% base chance (guaranteed with Cryomancy)

### Important Interactions
- **Sheer Force**: Removes secondary effects, so Cryomancy won't work with Sheer Force
- **Kings Rock/Razor Fang**: Stacks with Cryomancy for additional flinch chance
- **Serene Grace**: Would stack multiplicatively (5x from Cryomancy, then 2x from Serene Grace)
- **Effect chance cap**: Chances above 100% guarantee the effect

### Frostbite vs Freeze Comparison
- **Freeze**: Completely prevents action (25% thaw chance per turn)
- **Frostbite**: Allows action but reduces special attack and deals damage
- **Curing**: Both use similar curing mechanisms (thaw moves, fire moves)
- **Strategy**: Frostbite is more reliable for offense, freeze is better for stall

### Strategic Applications
- **Special wall breaking**: Frostbite halves special attack, making special walls more effective
- **Chip damage**: Consistent 1/16 HP damage adds up over time
- **Status spreading**: High frostbite chance allows reliable status spreading
- **Anti-special sweeper**: Cripples special attackers more than burn affects physical ones

### Competitive Viability
- **Niche but powerful**: High status infliction rate makes it valuable
- **Ice-type synergy**: Works well with Ice-type moves and Pokemon
- **Limited move pool**: Only two moves can currently inflict frostbite
- **Status immunity**: Stopped by status immunity abilities or items

### Counters
- **Status immunity**: Limber, Guts, Natural Cure, etc.
- **Substitute**: Protects from status infliction
- **Heal Bell/Aromatherapy**: Team-wide status cure
- **Lum Berry/Pecha Berry**: Immediate status cure
- **Magic Guard**: Prevents frostbite damage

### Synergies
- **Kings Rock/Razor Fang**: Additional secondary effect chance
- **Wide Lens/Zoom Lens**: Improves accuracy of frostbite moves
- **Choice items**: Allows spamming of frostbite-inducing moves
- **Pressure/Scary Face**: Pairs well with status spreading strategy

### Team Building Considerations
- **Ice Fang users**: Physical attackers that can learn Ice Fang
- **Bitter Malice users**: Special Ghost types with access to the move
- **Status support**: Benefits from team members that can heal status
- **Hazard setters**: Pairs well with entry hazards for additional pressure

### Version History
- Elite Redux exclusive ability
- Designed to make frostbite a more viable status condition
- Part of the expanded status condition system in Elite Redux
- ID 456 in the ability list

### Related Abilities
- **Flame Body**: Similar concept but for burn status
- **Static**: Similar concept but for paralysis
- **Poison Point**: Similar concept but for poison
- **Effect Spore**: Random status infliction on contact
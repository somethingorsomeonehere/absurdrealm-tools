---
id: 471
name: Cold Plasma
status: reviewed
character_count: 64
---

# Cold Plasma - Ability ID 471

## In-Game Description
"Electric type moves now inflict burn instead of paralysis."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Causes Electric-type moves to inflict burn instead of paralysis. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Cold Plasma is a status conversion ability that modifies the secondary effects of Electric-type moves. When a Pokemon with Cold Plasma uses an Electric-type move that would normally have a chance to inflict paralysis, it instead has the same chance to inflict burn status.

### Activation Conditions
- **Move type requirement**: Only affects Electric-type moves
- **Status effect requirement**: Only affects moves that normally inflict paralysis
- **Automatic activation**: Triggers whenever using qualifying Electric moves
- **Probability unchanged**: Uses the same chance as the original paralysis effect

### Affected Moves
Electric-type moves that normally inflict paralysis:
- **Thunderbolt** (10% paralysis to 10% burn)
- **Thunder** (30% paralysis to 30% burn)
- **Discharge** (30% paralysis to 30% burn)
- **Thunder Wave** (100% paralysis to 100% burn)
- **Spark** (30% paralysis to 30% burn)
- **Thunder Punch** (10% paralysis to 10% burn)
- **Thundershock** (10% paralysis to 10% burn)
- **Bolt Strike** (20% paralysis to 20% burn)

### Technical Implementation
**Status:** This ability appears to be defined in the proto files but not yet implemented in the core battle engine. The implementation would likely involve:

```c
// Hypothetical implementation in abilities.cc
constexpr Ability ColdPlasma = {
    .onModifyMoveEffect = 
        +[](ON_MODIFY_MOVE_EFFECT) {
            if (GetMoveType(move) == TYPE_ELECTRIC && 
                moveEffect == MOVE_EFFECT_PARALYSIS) {
                return MOVE_EFFECT_BURN;
            }
            return moveEffect;
        },
};
```

### Important Interactions
- **Type effectiveness**: Electric moves still follow normal type effectiveness
- **Immunities**: Fire types and Pokemon with Water Veil are immune to burn
- **Existing status**: Cannot burn already statused Pokemon
- **Limber immunity**: Limber Pokemon are not affected by this ability change
- **Status move conversion**: Thunder Wave becomes a 100% burn move

### Strategic Implications
- **Offensive utility**: Burn reduces Attack stat, helping against physical attackers
- **Damage over time**: Burn deals consistent damage unlike paralysis
- **Speed control**: Loses speed reduction effect of paralysis
- **Wall breaking**: More effective against defensive Pokemon than paralysis
- **Type synergy**: Works well with Fire-type coverage moves

### Burn vs Paralysis Comparison
**Burn advantages:**
- Deals 1/16 max HP damage each turn
- Reduces Attack stat by 50%
- Better against physical walls
- More consistent damage output

**Paralysis advantages:**
- Reduces Speed by 50%
- 25% chance to be unable to move
- Speed control utility
- Better against fast setup sweepers

### Potential Users
This ability would be ideal for:
- Electric-type Pokemon with mixed offensive stats
- Pokemon that want to pressure physical attackers
- Team builds focusing on residual damage
- Pokemon with Fire-type coverage moves

### Competitive Considerations
- **Anti-physical**: Excellent against physical attackers
- **Stall breaking**: Burn helps overcome defensive strategies
- **Trade-offs**: Loses speed control utility of paralysis
- **Synergy potential**: Pairs well with other burn-inducing effects
- **Counterplay**: Fire types become complete immunities

### Implementation Status
**Note:** This ability is currently defined in the proto files but does not appear to have active implementation in the battle engine. The mechanical analysis above is based on the described functionality and standard Elite Redux ability patterns.

### Version History
- Added to Elite Redux proto files as ability ID 471
- Implementation pending in core battle system
- Represents unique status conversion mechanic

### Synergies
- **Hex/Venoshock**: Boosted damage against burned targets
- **Fire-type moves**: Thematic synergy with burn status
- **Guts**: Ironically helps opposing Guts users
- **Facade**: Boosts opposing Facade users' power

### Counters
- **Fire-type Pokemon**: Immune to burn status
- **Water Veil**: Ability prevents burn
- **Aromatherapy/Heal Bell**: Removes burn status
- **Lum Berry**: Cures burn status once
- **Switching**: Removes burn when switching out
---
id: 874
name: Winter Throne
status: reviewed
character_count: 125
---

# Winter Throne - Ability ID 874

## In-Game Description
"1/8 Damage each turn to non-ice. Heals Ice 1/8 each turn."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

All non-Ice-types lose 1/8 of their max HP at the end of each turn. Restores 1/8 max HP to Ice-types at the end of each turn.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Winter Throne is a powerful field control ability that creates a dichotomy between Ice-type and non-Ice-type Pokemon. It activates at the end of each turn, dealing damage to enemies while healing allies of the appropriate type.

### Activation Conditions
- **Timing**: Activates at the end of turn for all Pokemon on the field
- **Damage targets**: All non-Ice-type Pokemon (including allies in doubles)
- **Healing targets**: All Ice-type Pokemon (including the user)
- **HP calculation**: 1/8 of the target's maximum HP per turn

### Affected Pokemon
- **Takes damage**: Any Pokemon without Ice as primary or secondary type
- **Gets healed**: Any Pokemon with Ice as primary or secondary type
- **Minimum values**: 1 HP minimum for both damage and healing

### Technical Implementation
```c
// Winter Throne triggers at end of turn for all battlers
if (ability == ABILITY_WINTER_THRONE) {
    for (battler = 0; battler < MAX_BATTLERS_COUNT; battler++) {
        if (IS_BATTLER_OF_TYPE(battler, TYPE_ICE)) {
            // Heal Ice types for 1/8 HP
            if (!BATTLER_MAX_HP(battler) && CanBattlerHeal(battler)) {
                gBattleMoveDamage = -gBattleMons[battler].maxHP / 8;
                if (gBattleMoveDamage == 0) gBattleMoveDamage = -1;
                // Heal battler
            }
        } else {
            // Damage non-Ice types for 1/8 HP
            gBattleMoveDamage = gBattleMons[battler].maxHP / 8;
            if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
            // Damage battler
        }
    }
}
```

### Important Interactions
- **Type changes**: Effect changes if Pokemon's type changes mid-battle
- **Dual typing**: Works if Ice is either primary or secondary type
- **Ability suppression**: Doesn't work if ability is suppressed (Mold Breaker, etc.)
- **Substitute**: Damage/healing may be blocked by Substitute
- **Magic Guard**: Magic Guard prevents the damage but not the healing

### Strategic Implications
- **Field control**: Dramatically shifts battle dynamics in favor of Ice types
- **Stall potential**: Makes Ice types extremely difficult to wear down
- **Team building**: Encourages Ice-heavy team compositions
- **Counter strategies**: Forces opponents to end battles quickly
- **Doubles synergy**: Affects all Pokemon, creating complex field states

### Damage Calculations
- **1/8 HP per turn**: Significant but not overwhelming
- **300 HP Pokemon**: Takes 37 damage per turn (heals 37 if Ice type)
- **400 HP Pokemon**: Takes 50 damage per turn (heals 50 if Ice type)
- **Cumulative effect**: Can determine long battles

### Counters
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the effect
- **Type changing**: Forest's Curse, Trick-or-Treat can add/remove Ice typing
- **Quick wins**: End battles before cumulative damage becomes decisive
- **Magic Guard**: Protects non-Ice types from the damage
- **Substitute**: May block damage (but not healing)

### Synergies
- **Ice-type teams**: Maximizes the healing benefit
- **Bulk building**: Leftovers + Winter Throne creates massive sustain
- **Stall tactics**: Combines with defensive moves for attrition wins
- **Entry hazards**: Complements chip damage strategies
- **Weather immunity**: Not dependent on weather unlike similar abilities

### Competitive Usage Notes
- **Unique effect**: No other ability provides both damage and healing simultaneously
- **Field presence**: Changes how both players approach the battle
- **Late game impact**: Becomes more powerful as battles extend
- **Team archetype**: Enables Ice-type stall/balance teams
- **Doubles consideration**: Affects teammates, requiring careful team construction

### Common Users
- Bulky Ice-type Pokemon who can capitalize on the healing
- Ice-type walls and defensive pivots
- Pokemon designed to outlast opponents through sustain
- Ice-type setup sweepers who need longevity

### Version History
- New ability in Elite Redux
- Part of the extended ability roster (800+ series)
- Designed to make Ice types more viable in competitive play
- Unique field control mechanism not found in official games
---
id: 478
name: Moon Spirit
status: reviewed
character_count: 195
---

# Moon Spirit - Ability ID 478

## In-Game Description
"Fairy & Dark gains STAB. Moonlight recovers 75% HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Moon Spirit grants STAB to all Fairy and Dark-type moves regardless of the user's typing. When using Moonlight, recovery increases to 75% max HP instead of normal 50% or weather-modified amounts. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Moon Spirit is a unique dual-function ability that provides both offensive and defensive benefits. It grants Same Type Attack Bonus (STAB) to Fairy and Dark-type moves regardless of the Pokemon's actual typing, and enhances Moonlight recovery.

### STAB Function
- **Affected move types**: Fairy and Dark moves only
- **Damage multiplier**: 1.5x (standard STAB bonus)
- **Type independence**: Works regardless of Pokemon's actual typing
- **Stacking**: Does not stack with natural STAB (if Pokemon is already Fairy/Dark type)

### Moonlight Enhancement
- **Base recovery**: 75% of max HP (3/4 of max HP)
- **Weather override**: Ignores all weather effects on Moonlight
- **Priority**: Takes precedence over weather-based recovery modifications

### Technical Implementation
```c
// STAB for Fairy and Dark moves
constexpr Ability MoonSpirit = {
    .onStab = +[](ON_STAB) -> int { 
        return moveType == TYPE_FAIRY || moveType == TYPE_DARK; 
    },
};

// Moonlight recovery enhancement
if (gCurrentMove == MOVE_MOONLIGHT && BATTLER_HAS_ABILITY(gBattlerAttacker, ABILITY_MOON_SPIRIT)) {
    gBattleMoveDamage = gBattleMons[gBattlerAttacker].maxHP * 3 / 4;  // 75% recovery
}
```

### Weather Interaction Details
Normal Moonlight recovery is weather-dependent:
- **Sunny weather**: 2/3 HP (66.7%)
- **Neutral weather**: 1/2 HP (50%)
- **Rain/Sandstorm/Hail/Fog**: 1/4 HP (25%)

With Moon Spirit:
- **All weather conditions**: 3/4 HP (75%)
- **Consistent recovery**: Weather independence provides reliability

### Offensive Applications
Moon Spirit allows any Pokemon to use Fairy and Dark moves with STAB effectiveness:
- **Fairy moves**: Moonblast, Dazzling Gleam, Play Rough, Moonbeam
- **Dark moves**: Dark Pulse, Foul Play, Crunch, Sucker Punch
- **Coverage potential**: Grants neutral Pokemon access to two strong offensive types
- **Surprise factor**: Unexpected STAB moves from non-Fairy/Dark Pokemon

### Defensive Applications
Enhanced Moonlight provides superior recovery:
- **Weather immunity**: No reduction in harsh weather
- **Consistent healing**: Always 75% recovery regardless of conditions
- **Bulky sets**: Enables defensive playstyles with reliable recovery
- **Status absorption**: Can afford to take status conditions with strong healing

### Strategic Implications
- **Dual-type coverage**: Effective against Psychic, Fighting, Ghost, and other types
- **Weather independence**: Doesn't rely on weather for maximum effectiveness
- **Versatile**: Suits both offensive and defensive strategies
- **Typing flexibility**: Makes non-Fairy/Dark Pokemon viable with these move types

### Synergistic Moves
**Fairy moves that benefit:**
- Moonblast (95 BP to 142 BP with STAB)
- Play Rough (90 BP to 135 BP with STAB)
- Dazzling Gleam (80 BP to 120 BP with STAB)

**Dark moves that benefit:**
- Dark Pulse (80 BP to 120 BP with STAB)
- Foul Play (95 BP to 142 BP with STAB)
- Crunch (80 BP to 120 BP with STAB)

### Common User Profiles
- **Psychic-types**: Gain Dark STAB for coverage against other Psychics
- **Normal-types**: Access to two powerful offensive types
- **Bulky attackers**: Can use Moonlight + offensive moves effectively
- **Mixed attackers**: Physical Dark moves + Special Fairy moves

### Competitive Applications
- **Wallbreaking**: Unexpected STAB moves can break through typical counters
- **Pivot role**: Strong attacks + reliable healing enable switching
- **Late-game cleaning**: Moonlight sustain with STAB coverage
- **Anti-meta**: Counters common defensive cores with dual typing

### Limitations
- **Move dependency**: Requires learning Fairy/Dark moves to benefit from STAB
- **Moonlight requirement**: Recovery benefit only applies to one specific move
- **Type distribution**: Limited to Pokemon that can learn relevant moves
- **Ability competition**: May compete with other strong abilities

### Interaction Notes
- **Natural typing**: If Pokemon is already Fairy or Dark type, STAB doesn't stack
- **Hidden Power**: Does not affect Hidden Power regardless of type
- **Multi-hit moves**: Each hit receives the STAB bonus
- **Critical hits**: STAB applies before critical hit calculation

### Team Building Considerations
- **Move tutoring**: Requires access to Fairy/Dark moves through breeding/tutors
- **Recovery stacking**: Can combine with other healing moves for sustainability
- **Type coverage**: Complements existing movepool with new offensive options
- **Weather teams**: Less dependent on weather than typical Moonlight users

### Version History
- Elite Redux exclusive ability (ID 478)
- Part of the extended ability system push to 500+ abilities
- Designed to create unique dual-type offensive potential
- Provides weather-independent recovery option

### Comparison to Similar Abilities
- **Mystic Power**: Grants universal STAB but lacks healing component
- **Natural STAB**: Only applies to Pokemon's actual types
- **Big Root**: Enhances all recovery moves but by smaller amount
- **Weather abilities**: Affect Moonlight but don't provide offensive benefits
---
id: 32
name: Serene Grace
status: reviewed
character_count: 79
---

# Serene Grace - Ability ID 32

## In-Game Description
"Doubles chance of secondary effects on its own moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Doubles the activation chance of the user's secondary effects on their attacks.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Serene Grace doubles the probability of any secondary effect on moves used by the ability holder. This simple multiplication creates dramatic changes in move reliability.

### Technical Implementation
From `/src/abilities.cc`:
```cpp
constexpr Ability SereneGrace = {
    .onModifyEffectChance = +[](ON_MODIFY_EFFECT_CHANCE) { *effectChance *= 2; },
};
```

The implementation:
- Uses `onModifyEffectChance` callback
- Multiplies effect chance by 2
- Caps at 100% after all modifiers
- Applies only to user's moves

### Affected Move Properties

**Status effects:**
- Burn chance (Fire Punch: 10% to 20%)
- Freeze chance (Ice Beam: 10% to 20%) 
- Paralysis chance (Thunder: 30% to 60%)
- Poison chance (Sludge Bomb: 30% to 60%)

**Stat changes:**
- Attack drops (Aurora Beam: 10% to 20%)
- Defense drops (Crunch: 20% to 40%)
- Speed drops (Icy Wind: 100% to still 100%)
- Accuracy drops (Muddy Water: 30% to 60%)

**Flinch chances:**
- Bite/Air Slash: 30% to 60%
- Iron Head: 30% to 60%
- Headbutt: 30% to 60%

**Other effects:**
- Confusion (Water Pulse: 20% to 40%)
- Item removal (Knock Off: always 100%)

### Notable Move Interactions

**High-impact combinations:**
- **Thunder**: 30% to 60% paralysis (70% with ParaFlinch builds)
- **Air Slash**: 30% to 60% flinch (infamous paraflinch)
- **Iron Head**: 30% to 60% flinch
- **Rock Slide**: 30% to 60% flinch (doubles)
- **Scald**: 30% to 60% burn

**Already 100% effects:**
- Icy Wind, Bulldoze (speed drops)
- Psychic (rare 10% to 20% SpDef drop)

### Rainbow Weather Interaction
- Rainbow weather also doubles effect chances
- Stacks multiplicatively with Serene Grace
- Results in 4x effect chance (capped at 100%)
- Example: Thunder gets 100% paralysis chance

### Related Abilities
**Lucky Wings**: Combines Serene Grace effect with Giant Wings (1.3x boost to wing/wind moves)

### Strategic Applications

**Paraflinch Strategy:**
- Thunder Wave + Air Slash/Iron Head
- 60% flinch + 25% paralysis = ~70% no move
- Extremely frustrating but effective

**Status Spreading:**
- Reliable burn/poison application
- Scald becomes premier burn move (60%)
- Thunder becomes paralysis machine

**Stat Control:**
- Crunch for consistent Defense drops
- Psychic for Special Defense pressure
- Shadow Ball becomes 40% SpDef drop

### Common Serene Grace Users
- Togekiss (paraflinch master)
- Jirachi (Iron Head flinches)
- Dunsparce/Dudunsparce
- Blissey (status spreading)
- Deerling/Sawsbuck
- Various Elite Redux additions

### Damage vs Effect Consideration
While Serene Grace doesn't boost damage, the utility often outweighs raw power:
- 60% flinch effectively prevents damage
- 60% burn halves physical damage
- Status conditions provide lasting value

### Synergies
- **Paralysis support**: Thunder Wave enables flinch abuse
- **Speed control**: Ensures moving first for flinches  
- **Substitute**: Protects while fishing for effects
- **King's Rock/Razor Fang**: Additional flinch chances

### Counters
- **Inner Focus**: Flinch immunity
- **Shield Dust**: Blocks secondary effects
- **Substitute**: Blocks most effects
- **Covert Cloak**: Prevents secondary effects
- **Magic Guard**: Immune to status damage
- **Taunt**: Prevents setup

### Competitive Usage Notes
Serene Grace transforms unreliable secondary effects into core strategies. The ability is most valuable on Pokemon with:
1. Access to high-flinch moves
2. Good speed tiers or priority
3. Moves with powerful secondary effects
4. Defensive stats to abuse multiple turns

The psychological impact is significant - opponents must respect even low-chance effects.

### Mathematical Examples
- 10% effect to 20% (1 in 5 chance)
- 20% effect to 40% (2 in 5 chance)
- 30% effect to 60% (3 in 5 chance)
- 50% effect to 100% (guaranteed)

### AI Behavior
- Values moves with secondary effects higher
- Recognizes increased effect chances
- May prioritize status/flinch strategies

### Version History
Serene Grace has remained mechanically consistent since Generation 3, always doubling effect chances. The ability's simplicity and effectiveness have made it a competitive staple, particularly on Togekiss and Jirachi.
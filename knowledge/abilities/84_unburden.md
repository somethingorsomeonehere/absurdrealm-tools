---
id: 84
name: Unburden
status: reviewed
character_count: 169
---

# Unburden - Ability ID 84

## In-Game Description
"Consuming its held item doubles Speed until switched out."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When consuming or losing a held item, the user's base Speed stat is multiplied by x2. Boost goes away when switching out, gaining a new item, or upon losing the ability. 

## Detailed Mechanical Explanation
*For Discord/reference use*

**UNBURDEN** is a Speed-boosting ability that activates when the Pokemon loses its held item through any means.

### Activation Mechanics:
- **Trigger**: When the Pokemon's held item becomes ITEM_NONE (removed/consumed)
- **Speed Boost**: Doubles Speed stat (2x multiplier)
- **Duration**: Until the Pokemon switches out or gains a new item
- **State Management**: Uses SetAbilityState/GetAbilityState system

### Technical Implementation:
```c
constexpr Ability Unburden = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && GetAbilityState(battler, ability)) *stat *= 2;
        },
};
```

### Item Loss Triggers:
1. **Berry Consumption**: Natural consumption when conditions are met
   - Sitrus Berry (HP drop), Lum Berry (status), etc.
   - Bug Bite/Pluck eating target's berry
   
2. **Gem Activation**: Type gems consumed when using matching move type
   - Flying Gem, Fire Gem, etc.
   
3. **Other Consumables**:
   - White Herb (stat drops), Mental Herb (attraction/taunt)
   - Focus Sash (survive lethal hit), Air Balloon (hit by Ground move)
   - Weakness Policy, Cell Battery, etc.

4. **Forced Item Removal**:
   - Knock Off (removes and damages)
   - Incinerate (destroys berries/gems)
   - Pickpocket (steals on contact)
   - Covet/Thief (steals via moves)
   - Magic Room (temporary item nullification ending)

### State Management:
```c
// In UpdateBattlerItem function:
if (oldItem == ITEM_NONE)
    SetAbilityState(battler, ABILITY_UNBURDEN, FALSE);  // Gained item - disable
else if (newItem == ITEM_NONE)
    SetAbilityState(battler, ABILITY_UNBURDEN, TRUE);   // Lost item - enable
```

### Interaction Rules:
- **Gaining Items**: Speed boost immediately deactivates if Pokemon receives any item
- **Switch Out**: Speed boost is lost when Pokemon leaves battle
- **Multiple Activations**: Can activate multiple times per battle if item is lost again
- **Sticky Hold**: Prevents forced item removal, so Unburden won't activate from Knock Off/etc.

### Speed Calculation Priority:
Unburden applies during stat calculation phase:
1. Base Speed stat
2. Nature modifier
3. Ability modifiers (Unburden: 2x)
4. Item modifiers (Choice Scarf, etc.)
5. Status conditions (paralysis: 0.25x)

### Strategic Applications:
1. **Berry Strategies**:
   - Sitrus Berry + Belly Drum combo
   - Salac Berry for stacked Speed boosts
   - Petaya/Apicot berries for additional stat boosts

2. **Gem Sweeping**:
   - Normal Gem + Fake Out for priority
   - Flying Gem + Acrobatics (double power when itemless)

3. **Sacrifice Items**:
   - Focus Sash for setup opportunities
   - Weakness Policy for offensive boosts

### Common Users:
- **Hawlucha**: Flying/Fighting with Acrobatics synergy
- **Treecko line**: Fast Grass types with access to berries
- **Slurpuff**: Fairy type with natural berry synergy
- **Hitmonlee**: Fast Fighting type for physical sweeping
- **Various custom Elite Redux Pokemon**: Speed-focused builds

### Competitive Interactions:
- **Acrobatics Synergy**: Flying move doubles power when user has no item
- **Belly Drum**: Max Attack + Unburden speed for physical sweeping
- **Priority Moves**: Enhanced by superior Speed for move order
- **Choice Items**: Cannot benefit as item isn't consumed, only locked

### Counters:
1. **Trick/Switcheroo**: Force an item onto the Pokemon
2. **Priority Moves**: Bypass Speed advantage
3. **Status Moves**: Paralysis cuts Speed, burns reduce Attack
4. **Sticky Hold**: Prevents item removal on opposing Pokemon

### Synergies:
- **White Herb**: Remove negative stat drops and gain Speed
- **Terrain Seeds**: Stat boost + Speed boost combo
- **Endure + Salac Berry**: Guaranteed Speed boost at low HP
- **Substitute**: Protect setup while item activates

### Version History:
- **Gen 4 Introduction**: Original implementation
- **Gen 5+**: Consistent across generations
- **Elite Redux**: Maintained standard mechanics with expanded item interactions

### Example Damage Calculations:
**Hawlucha @ Flying Gem**
- Base Speed: 118
- After Flying Gem consumed: 236 effective Speed
- Acrobatics: 55 BP to 110 BP (no item) + STAB + gem boost
- Result: Extremely fast, powerful Flying attack

**Common Competitive Set:**
```
Hawlucha @ Flying Gem
Ability: Unburden
- Acrobatics (powered up when itemless)
- High Jump Kick/Close Combat
- Swords Dance/Substitute
- Roost/U-turn
```
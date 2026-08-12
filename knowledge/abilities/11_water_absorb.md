---
id: 11
name: Water Absorb
status: reviewed
character_count: 99
---

# Water Absorb - Ability ID 11

## In-Game Description
"Heals 25% of max HP when hit by a Water-type move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user gains immunity to Water-type moves and they heal for 25% of their max HP when hit by them.


## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Water Absorb provides Water-type immunity with healing benefit:

1. **Complete Absorption**
   - Negates all damage from Water-type moves
   - Prevents secondary effects (stat drops, etc.)
   - Works on all Water moves including status moves

2. **Healing Mechanism**
   - Restores exactly 25% of maximum HP (maxHP / 4)
   - Minimum 1 HP healing if calculation rounds down
   - Still absorbs at full HP (no overflow damage)

### Technical Implementation

**Code Structure** (`src/abilities.cc`):
```cpp
constexpr Ability WaterAbsorb = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_WATER)
        return ABSORB_RESULT_HEAL;
    },
    .breakable = TRUE,
};
```

Identical implementation to Volt Absorb but checking for Water-type.

### Healing Calculation
For various HP values:
- 404 HP Pokemon: Heals 101 HP per trigger
- 352 HP Pokemon: Heals 88 HP per trigger
- 4 HP Pokemon: Heals 1 HP (minimum)

### Strategic Implications

1. **Type Advantage Negation**
   - Fire-types lose Water weakness
   - Ground/Rock-types become viable Water switch-ins
   - Removes 4x weakness for Fire/Rock, Fire/Ground

2. **Defensive Utility**
   - Safe switch into Scald (no burn risk)
   - Absorbs Surf/Muddy Water in doubles
   - Negates rain-boosted Water moves

3. **Recovery Option**
   - 25% healing is significant
   - Can full heal in 4 Water attacks
   - Partner healing in doubles

### Interactions with Other Abilities/Mechanics
- **Storm Drain**: Would redirect but Water Absorb triggers
- **Dry Skin**: Has Water Absorb effect plus weather interaction
- **Mold Breaker**: Bypasses Water Absorb
- **Freeze-Dry**: Ice-type move, not absorbed
- **Soak**: Changes target to Water-type, not absorbed

### Common Water Absorb Users
- **Poliwrath**: Fighting/Water with absorption
- **Toxapex**: Poison/Water defensive wall
- **Lanturn**: Water/Electric with dual absorptions
- **Mantine**: Water/Flying special wall
- **Lapras**: Water/Ice bulky support

### Double Battle Applications
**Surf Spam**: Partner uses Surf for healing + damage
**Water Pledge**: Healing while setting up combos
**Scald Support**: Risk-free healing from partner

### Competitive Usage Notes
- S-tier on Fire/Ground/Rock types
- Excellent defensive ability
- Enables new defensive cores
- Counters rain teams effectively
- Provides momentum through free switches

### Mathematical Analysis
Against common Water moves:
- Hydro Pump (110 BP): 0 damage, heal 25%
- Scald (80 BP): 0 damage, heal 25%, no burn
- Surf in doubles: Damages enemies, heals ally
- Aqua Jet priority: 0 damage, heal 25%

### Counters
- **Freeze-Dry**: Super effective on Water, not absorbed
- **Grass moves**: Alternative coverage
- **Electric moves**: Alternative coverage
- **Mold Breaker**: Ignores ability
- **Status moves**: Toxic, Thunder Wave work normally

### Synergies
- **Fire-types**: Remove major weakness
- **Ground-types**: Defensive synergy
- **Rain teams**: Absorb opposing rain-boosted attacks
- **Substitute**: Bait Water moves safely
- **Wish/Protect**: Stack recovery options

### Related Abilities
- **Volt Absorb**: Electric-type equivalent
- **Flash Fire**: Fire absorption with boost
- **Sap Sipper**: Grass absorption with Attack boost
- **Earth Eater**: Ground absorption with healing
- **Dry Skin**: Includes Water Absorb plus rain healing

### Weather Considerations
In rain:
- Absorbs boosted Water moves (1.5x becomes 0x)
- Doesn't boost healing amount
- Excellent rain counter

### AI Behavior
The AI recognizes Water Absorb and:
- Avoids Water moves entirely
- May heal allies intentionally in doubles
- Switches to alternative coverage
- Respects the immunity when choosing moves

### Version History
- **Gen III+**: Consistent 25% healing mechanic
- **Elite Redux**: Identical function with strategic importance
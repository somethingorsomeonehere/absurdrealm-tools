---
id: 10
name: Volt Absorb
status: reviewed
character_count: 289
---

# Volt Absorb - Ability ID 10

## In-Game Description
"Heals 25% of max HP when hit by an Electric-type move."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

This Pokemon absorbs Electric-type moves completely, converting them into energy that restores 25% of its maximum HP. Provides complete immunity to Electric damage and effects like paralysis from Thunder Wave. Absolutely perfect for Water/Flying types to remove their 4x Electric weakness.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Volt Absorb provides Electric-type immunity with healing benefit:

1. **Complete Absorption**
   - Negates all damage from Electric-type moves
   - Prevents secondary effects of Electric moves
   - Absorbs Electric-type status moves (Thunder Wave)

2. **Healing Effect**
   - Restores exactly 25% of maximum HP
   - Minimum 1 HP if calculation rounds to 0
   - No healing if already at full HP (still absorbs)

### Technical Implementation

**Code Structure** (`src/abilities.cc`):
```cpp
constexpr Ability VoltAbsorb = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_ELECTRIC)
        return ABSORB_RESULT_HEAL;
    },
    .breakable = TRUE,
};
```

**Healing Calculation** (`src/battle_util.c`):
```c
gBattleMoveDamage = gBattleMons[battler].maxHP / 4;
if (gBattleMoveDamage == 0) 
    gBattleMoveDamage = 1;
gBattleMoveDamage *= -1;  // Negative = healing
```

### Key Properties
- **Breakable**: Bypassed by Mold Breaker abilities
- **Priority**: Triggers before damage calculation
- **Multi-hit**: Only heals once per move
- **Status moves**: Also absorbed (Thunder Wave fails)

### Healing Examples
For a Pokemon with 400 HP:
- Thunder hits: Heal 100 HP
- Thunderbolt hits: Heal 100 HP  
- Thunder Wave: No damage, no paralysis, heal 100 HP
- Electroweb: No damage, no speed drop, heal 100 HP

### Strategic Implications
1. **Switch-in**: Safe Electric immunity with healing bonus
2. **Doubles Support**: Partner can heal with weak Electric moves
3. **Momentum**: Free turn + healing vs Electric attacks
4. **Type Coverage**: Removes Electric weakness entirely
5. **Sustain**: Built-in recovery mechanism

### Interactions with Other Abilities/Mechanics
- **Lightning Rod**: Would redirect but Volt Absorb takes priority
- **Motor Drive**: Similar immunity but Speed boost instead
- **Mold Breaker**: Bypasses Volt Absorb entirely
- **Normalize**: Makes all moves Normal-type, avoiding absorption
- **Ion Deluge**: Can create more Electric moves to absorb

### Competitive Usage Notes
- S-tier ability for Water/Flying types
- Provides crucial Electric immunity
- Healing is significant (25% is substantial)
- Excellent on defensive pivots
- Can bait predictable Electric attacks

### Double Battle Strategies
**Heal Support**: Partner uses weak Electric move for healing
**Discharge Spam**: Partner with Telepathy uses Discharge
**Redirection**: Combine with Follow Me for guaranteed healing

### Common Volt Absorb Users
- **Jolteon**: Pure Electric with healing option
- **Lanturn**: Water/Electric defensive pivot
- **Thundurus**: Flying/Electric with recovery
- Various Water-types needing Electric coverage

### Mathematical Efficiency
Switching into predicted Electric moves:
- Turn 1: Take 0 damage, heal 25%
- Effective HP swing: 50%+ (damage prevented + healing)
- Can fully heal in 4 Electric hits

### Counters
- **Ground moves**: Alternative super effective damage
- **Mold Breaker**: Ignores the ability
- **Non-Electric coverage**: Use other move types
- **Status moves**: Toxic, Will-O-Wisp still work
- **Entry hazards**: Damage on switch-in

### Synergies
- **Water-types**: Remove Electric weakness
- **Flying-types**: Remove 4x Electric weakness
- **Wish support**: Stack healing effects
- **Substitute**: Protect while baiting Electric moves
- **Baton Pass chains**: Safe Electric immunity

### Related Absorb Abilities
- **Water Absorb**: Identical but for Water-type
- **Flash Fire**: Fire immunity with power boost
- **Sap Sipper**: Grass immunity with Attack boost
- **Earth Eater**: Ground immunity with healing
- **Levitate**: Ground immunity without healing

### AI Behavior
The AI recognizes Volt Absorb and will:
- Avoid using Electric moves
- Switch to non-Electric attackers
- May use Electric moves to heal allies in doubles
- Prioritize other super effective coverage

### Version History
- **All Generations**: Consistent 25% healing from Electric moves
- **Elite Redux**: Functions identically with enhanced AI integration
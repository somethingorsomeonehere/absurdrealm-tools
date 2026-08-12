---
id: 708
name: Roused Fangs
status: reviewed
character_count: 117
---

# Roused Fangs - Ability ID 708

## In-Game Description
"Biting moves use SpAtk and deal 30% more damage."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Biting moves use the Special Attack (still targets enemy's Defense unless stated otherwise) and deal 30% more damage. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Roused Fangs is a unique offensive ability that fundamentally changes how biting moves function for the Pokemon. It serves dual purposes: converting the attacking stat used and providing a damage boost.

### Ability Effects
1. **Stat Conversion**: All biting moves use Special Attack instead of Attack for damage calculation
2. **Damage Boost**: All biting moves deal 30% more damage (1.3x multiplier)
3. **Move Classification**: Affects all moves with the `FLAG_STRONG_JAW_BOOST` flag

### Affected Moves
Biting moves that benefit from Roused Fangs include:
- **Bite**: Dark-type physical move becomes special
- **Crunch**: Dark-type physical move becomes special  
- **Fire Fang**: Fire-type physical move becomes special
- **Ice Fang**: Ice-type physical move becomes special
- **Thunder Fang**: Electric-type physical move becomes special
- **Poison Fang**: Poison-type physical move becomes special
- **Psychic Fangs**: Psychic-type physical move becomes special
- **Hyper Fang**: Normal-type physical move becomes special
- And other moves with the Strong Jaw boost flag

### Technical Implementation
```c
// Roused Fangs combines two effects:
constexpr Ability RousedFangs = {
    .onOffensiveMultiplier = StrongJaw.onOffensiveMultiplier,  // 1.3x damage
    .onChooseOffensiveStat = MindCrush.onChooseOffensiveStat,  // Use SpAtk
};

// StrongJaw multiplier
if (gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST) MUL(1.3);

// MindCrush stat conversion  
if (gBattleMoves[move].flags & FLAG_STRONG_JAW_BOOST) *atkStatToUse = STAT_SPATK;
```

### Strategic Implications
- **Build Flexibility**: Allows physical Pokemon to run special attacking sets
- **STAB Synergy**: Dark-types gain special STAB options with Bite/Crunch
- **Coverage Enhancement**: Elemental fangs become special coverage moves
- **Stat Optimization**: Invest in Special Attack instead of Attack
- **Item Synergy**: Benefits from special attack boosting items and abilities

### Competitive Advantages
- **Unexpected Damage**: Physical walls may not expect special attacks
- **Dual Threat Potential**: Can run mixed sets with both physical and special moves
- **Enhanced Coverage**: Elemental fangs provide special type coverage
- **Intimidate Immunity**: Special attacks aren't affected by Intimidate
- **Burns Don't Matter**: Special attacks unaffected by burn status

### Important Interactions
- **Contact vs Non-Contact**: Move contact classification remains unchanged
- **Critical Hits**: Still calculated normally with 30% damage boost
- **Weather Effects**: Special Attack can be boosted by Modest nature, etc.
- **Abilities Stack**: Works with other damage-boosting abilities
- **Priority Unchanged**: Move priority remains the same

### Team Building Considerations
- **Special Attack EVs**: Max Special Attack instead of Attack
- **Nature Selection**: Modest/Quiet nature for Special Attack boost
- **Item Choices**: 
  - Choice Specs for massive special power
  - Life Orb for flexible special boost
  - Assault Vest for special bulk while maintaining offense
- **Move Coverage**: Combine elemental fangs for broad special coverage

### Pokemon Synergy
Ideal for Pokemon that:
- Have access to multiple biting moves
- Possess decent Special Attack stats
- Want to surprise physical walls
- Need special coverage options
- Can benefit from mixed attacking sets

### Counters and Checks
- **Special Walls**: High Special Defense Pokemon resist the boosted damage
- **Ability Suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Status Effects**: Sleep, paralysis still affect the user normally
- **Type Resistances**: Resistant types still take reduced damage despite the boost
- **Priority Moves**: Faster Pokemon can still outspeed and KO

### Synergies
- **Choice Specs**: Massive power boost to special attacks
- **Nasty Plot/Calm Mind**: Special Attack boosts enhance damage further  
- **Drought/Sun**: Boosts Fire Fang damage in sun
- **Rain**: No direct synergy but doesn't hurt special attacks
- **Terrain Effects**: Psychic Terrain boosts Psychic Fangs further

### Version History
- Introduced in Elite Redux as ability ID 708
- Originally named "Megabite" in protobuf but properly called "Roused Fangs"
- Part of the expanded ability system with unique stat conversion mechanics
- Combines Strong Jaw's damage boost with Mind Crush's stat conversion

### Usage Tips
1. **EV Spread**: Invest in Special Attack, not Attack
2. **Move Selection**: Prioritize biting moves for maximum benefit
3. **Surprise Factor**: Use against teams expecting physical attacks
4. **Coverage Options**: Elemental fangs provide excellent special type coverage
5. **Item Synergy**: Special Attack boosting items maximize potential

### Notable Users
Pokemon that commonly have Roused Fangs as an ability option in Elite Redux, typically those with:
- Natural access to multiple biting moves
- Decent Special Attack base stats
- Mixed offensive potential
- Dark typing for STAB synergy with Bite/Crunch
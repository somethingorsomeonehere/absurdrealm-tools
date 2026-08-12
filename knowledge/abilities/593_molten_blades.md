---
id: 593
name: Molten Blades
status: reviewed
character_count: 72
---

# Molten Blades - Ability ID 593

## In-Game Description
"Slicing moves gain 30% power and 20% burn chance."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Keen Edge moves are boosted by 30% and have a 20% chance to burn on hit.

## Detailed Mechanical Explanation

Molten Blades enhances slicing and cutting moves with both raw power and searing heat. This ability combines the damage boost of Keen Edge with a burn chance, creating a dual-threat offensive ability that punishes physical defenders while amplifying slicing move damage.

### Technical Implementation

### Code Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Implementation**: Combines Keen Edge boost with burn effect

### Core Mechanics
```cpp
constexpr Ability MoltenBlades = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(target))
        CHECK(CanBeBurned(target))
        CHECK(gBattleMoves[move].flags & FLAG_KEEN_EDGE_BOOST)
        CHECK(Random() % 100 < 20)

        return AbilityStatusEffect(MOVE_EFFECT_BURN);
    },
    .onOffensiveMultiplier = KeenEdge.onOffensiveMultiplier,
};
```

### Effect Components
1. **Damage Boost**: 30% increase (1.3x) to all slicing moves
2. **Burn Chance**: 20% chance to burn on hit
3. **Move Requirement**: Must have FLAG_KEEN_EDGE_BOOST flag

### Compatible Moves

### Common Slicing Moves
- **Slash**: Basic slicing move with high crit rate
- **Night Slash**: Dark-type slice with high crit rate
- **Psycho Cut**: Psychic-type slice with high crit rate
- **Leaf Blade**: Grass-type slice with high crit rate
- **Sacred Sword**: Ignores stat changes
- **X-Scissor**: Bug-type crossing slice
- **Cross Chop**: Fighting-type cross slice
- **Razor Wind**: Normal-type special slice

### Multi-Hit Slicing
- **Fury Cutter**: Growing power with consecutive use
- **Dual Chop**: Dragon-type double hit
- **Razor Shell**: Water-type with defense drops

### Elite Redux Slicing Moves
- **Ceaseless Edge**: Sets hazards while slicing
- **Kowtow Cleave**: Dark-type never-miss slice
- **Bitter Blade**: Grass-type with HP drain
- Various other custom slicing moves

### Strategic Applications

### Physical Wallbreaker
- 30% damage boost breaks through defenses
- Burn halves opponent's Attack stat
- Double punishment for physical walls
- Forces switches from burned defenders

### Burn Spreader
- 20% burn chance is reliable over time
- Each slicing move can inflict burn
- Synergizes with other burn strategies
- Reduces physical threats consistently

### Coverage Enhancement
- Makes slicing moves viable coverage options
- Burn chance adds utility to attacks
- Rewards diverse slicing movepool
- Creates pressure even on resisted hits

### Damage Calculations

### Base Power Examples
- Slash: 70 to 91 effective power
- Night Slash: 70 to 91 effective power
- Leaf Blade: 90 to 117 effective power
- Sacred Sword: 90 to 117 effective power
- X-Scissor: 80 to 104 effective power

### Burn Impact
- Halves opponent's Attack stat
- Deals 1/8 max HP per turn (1/16 in Gen 7+)
- Prevents physical attackers from threatening
- Stacks with Intimidate for -2 Attack effectively

### Synergies and Interactions

### Ability Synergies
- **Swords Dance**: Multiplies with the 30% boost
- **Technician**: Fury Cutter benefits from both
- **Sharpness**: Would stack if both boost same moves
- **Guts**: Opponents with Guts ignore burn Attack drop

### Type Synergies
- Fire-types can't be burned (know your matchups)
- Physical attackers benefit most from opponent burns
- Grass-types resist common Water counters
- Steel-types provide defensive backbone

### Team Synergies
- Hazard setters capitalize on forced switches
- Special attackers abuse burned physical walls
- Wish support keeps Molten Blades user healthy
- Status spreaders create burn + para/poison combos

### Competitive Analysis

### Tier: Medium-High
Molten Blades earns Medium-High tier for combining consistent damage with valuable utility.

### Strengths
1. **Dual Purpose**: Damage boost + status chance
2. **Anti-Physical**: Burns cripple physical attackers
3. **Move Variety**: Many compatible slicing moves
4. **No Setup**: Immediate impact from turn one

### Weaknesses
1. **Move Restriction**: Only works on slicing moves
2. **Fire Immunity**: Fire-types block burn
3. **Special Attackers**: Burn doesn't reduce Sp. Atk
4. **Guts/Facade**: Some abilities benefit from burn

### Usage Strategies

### Lead Pressure
- Open with boosted slicing moves
- Fish for early burns on physical threats
- Force switches to gain momentum
- Set pace of battle

### Mid-Game Control
- Target physical attackers for burns
- Use boosted moves to break walls
- Spread burns across team
- Maintain offensive pressure

### Late-Game Cleanup
- Burned opponents easier to outspeed/tank
- Boosted moves secure KOs
- Burn damage adds up over time
- Win through attrition + power

### Counter Strategies

### Type-Based Counters
- Fire-types immune to burn
- Special attackers ignore burn drawback
- Bulky Waters resist fire association
- Heal Bell/Aromatherapy cleanse burns

### Ability Counters
- Water Veil prevents burns
- Guts turns burn into Attack boost
- Magic Guard ignores burn damage
- Natural Cure heals burn on switch

### Strategic Counters
- Substitute blocks burn chance
- Protect scouts for burns
- Special-based teams minimize impact
- Quick KOs prevent burn accumulation

### Conclusion

Molten Blades exemplifies Elite Redux's design philosophy of combining existing mechanics in creative ways. By merging Keen Edge's reliable damage boost with burn utility, it creates an ability that's both powerful and strategic. The 20% burn chance is high enough to be threatening but not overwhelming, while the 30% damage boost ensures immediate impact.

This ability rewards players who can effectively utilize slicing moves while punishing physical-based teams. Its Medium-High tier reflects its consistent value without being oppressive, making it an excellent choice for Pokemon with access to diverse slicing moves who want to combine offensive pressure with defensive utility.
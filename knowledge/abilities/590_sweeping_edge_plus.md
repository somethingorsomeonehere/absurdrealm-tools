---
id: 590
name: Sweeping Edge Plus
status: reviewed
character_count: 172
---

# Sweeping Edge Plus - Ability ID 590

## In-Game Description
"Sweeping Edge + Keen Edge."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Makes all Keen Edge moves never miss and hit both opposing Pokemon in double battles. Multihit moves will only hit each target one time. Also boosts Keen Edge moves by 30%.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sweeping Edge Plus (also known as "Blademaster") is an upgraded combination ability that merges the effects of two powerful abilities: Keen Edge and Sweeping Edge. This creates a supremely powerful offensive ability for Pokemon that rely on slicing attacks.

### Technical Implementation
```cpp
// From src/abilities.cc - Sweeping Edge Plus definition
constexpr Ability SweepingEdgePlus = {
    .onOffensiveMultiplier = KeenEdge.onOffensiveMultiplier,
    .onAccuracy = SweepingEdge.onAccuracy,
};
```

### Ability Effects
Sweeping Edge Plus provides three distinct enhancements to Keen Edge moves:

1. **30% Damage Boost**: All Keen Edge moves deal 1.3x damage (inherited from Keen Edge ability)
2. **Perfect Accuracy**: All Keen Edge moves become unable to miss (inherited from Sweeping Edge ability)
3. **Multi-Target**: In double battles, Keen Edge moves hit both opposing Pokemon instead of just one (inherited from Sweeping Edge ability)

### Activation Conditions
- **Move requirement**: The move must have the `FLAG_KEEN_EDGE_BOOST` flag
- **Always active**: All three effects apply automatically when using eligible moves
- **Battle format**: Multi-target effect only applies in double battles where there are two opponents

### Keen Edge Move Categories
Keen Edge moves are slicing, cutting, or chopping attacks that have been designated with the `FLAG_KEEN_EDGE_BOOST` flag. All moves affected by the base Keen Edge and Sweeping Edge abilities are enhanced by Sweeping Edge Plus:

**Physical Slicing Moves:**
- Slash - High critical hit ratio, now hits both foes with 30% boost
- Leaf Blade - Grass-type blade attack with perfect accuracy and damage boost
- Dragon Claw - Dragon-type slashing move, enhanced for multi-target
- Night Slash - Dark-type blade attack with guaranteed hits
- Psycho Cut - Psychic-type cutting move with multi-target capability
- Cross Chop - Fighting-type crossing attack with perfect accuracy
- Karate Chop - Fighting-type chopping attack, boosted and multi-hit

**Special Slicing Moves:**
- Air Slash - 30% flinch chance + 30% damage boost + perfect accuracy + multi-target

### Battle Interactions
- **Double battles**: Keen Edge moves hit both opposing Pokemon with full damage and accuracy
- **Single battles**: Provides 30% damage boost and perfect accuracy
- **Accuracy bypass**: Completely ignores accuracy reductions, evasion boosts, and weather effects
- **Critical hits**: Each target is calculated independently for critical hits
- **Contact moves**: Contact effects can trigger from both targets independently
- **Damage calculation**: Each target receives the full 30% damage boost

### Strategic Applications
- **Ultimate offensive ability**: Combines three powerful enhancements into one ability slot
- **Double battle dominance**: Transforms single-target moves into devastating spread attacks
- **Accuracy independence**: Never misses regardless of battlefield conditions
- **Damage maximization**: Effectively increases damage output by 30% while doubling targets
- **Moveset flexibility**: Encourages diverse Keen Edge movesets for maximum coverage

### Comparison to Component Abilities
**vs. Keen Edge (ID 271):**
- Sweeping Edge Plus adds perfect accuracy and multi-target effects
- Same 30% damage multiplier for eligible moves

**vs. Sweeping Edge (ID 421):**
- Sweeping Edge Plus adds the 30% damage boost
- Same perfect accuracy and multi-target effects

**Combined Power:**
- Takes the best aspects of both parent abilities
- No drawbacks or limitations beyond those of the individual components
- Represents the pinnacle of slicing-based offensive abilities

### Example Damage Calculations
**Leaf Blade (90 BP) in Double Battle:**
- Without ability: 90 BP to one target
- With Sweeping Edge Plus: 117 BP effective (90 x 1.3) to BOTH targets

**Air Slash (75 BP Special) in Double Battle:**
- Without ability: 75 BP to one target, can miss
- With Sweeping Edge Plus: 97.5 BP effective (75 x 1.3) to BOTH targets, always hits

### Competitive Usage Notes
- **Elite tier ability**: One of the most powerful offensive abilities in Elite Redux
- **VGC dominance**: Extremely powerful in double battle formats
- **Immediate impact**: No setup required, effects apply instantly
- **Type coverage**: Works across multiple move types with slicing motions
- **Crit synergy**: Many Keen Edge moves have high critical hit ratios

### Common Users
This ability is typically found on:
- Elite-tier Pokemon with access to multiple Keen Edge moves
- Physical attackers with diverse slicing movesets
- Pokemon designed for double battle formats
- Late-game or legendary Pokemon with enhanced ability sets

### Important Interactions
- **Priority moves**: Keen Edge priority moves maintain their speed tier
- **Multi-hit moves**: Each hit gains perfect accuracy and damage boost
- **Protection moves**: Each target's Protect/Detect is calculated separately
- **Abilities that trigger on hit**: Abilities like Static or Rough Skin can trigger from both targets
- **Entry hazards**: Spikes/Stealth Rock damage both targets after spread moves

### Counters
- **Wide Guard**: Blocks the spread effect of converted moves in double battles
- **Ability suppression**: Mold Breaker, Neutralizing Gas, or similar abilities
- **Single battles**: Reduces effectiveness by removing multi-target component
- **Non-Keen Edge moves**: Ability doesn't affect moves without the appropriate flag
- **Type immunity**: Ghost types immune to Normal/Fighting Keen Edge moves
- **Extremely high defensive stats**: May still wall even boosted attacks

### Synergies
- **High critical hit ratio**: Many Keen Edge moves have increased crit rates
- **STAB bonus**: Same-type attack bonus stacks multiplicatively
- **Choice items**: Choice Band/Specs further amplify already-boosted moves
- **Weather effects**: Sun/Rain can boost Fire/Water-type slicing moves
- **Setup moves**: Works excellently after Swords Dance or similar attack boosts

### Version History
- Elite Redux exclusive ability (ID 590)
- Represents the ultimate evolution of slicing-based abilities
- Combines two pre-existing abilities into one superior version
- Part of the "Plus" series of upgraded combination abilities

### Move Compatibility
Only moves with the `FLAG_KEEN_EDGE_BOOST` flag are affected. This includes most slicing, cutting, and chopping attacks, but not all blade-themed moves necessarily qualify. Check individual move descriptions for "Keen Edge boost" to confirm compatibility.

### Design Philosophy
Sweeping Edge Plus represents the concept of a master swordsman or blade specialist who has perfected their craft. The ability embodies the idea of surgical precision (perfect accuracy), enhanced technique (damage boost), and sweeping strikes (multi-target capability) that define a true blademaster in combat.
---
id: 421
name: Sweeping Edge
status: reviewed
character_count: 150
---

# Sweeping Edge - Ability ID 421

## In-Game Description
"Keen Edge moves always hit and hit both foes."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sweeping Edge makes all Keen Edge moves never miss and hit both opposing Pokemon in double battles. Multihit moves will only hit each target one time.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sweeping Edge is an offensive ability that enhances Keen Edge moves with two powerful effects: guaranteed accuracy and multi-target capability in double battles. This transforms single-target slicing moves into devastating area-of-effect attacks.

### Ability Effects
1. **Perfect Accuracy**: All Keen Edge moves become unable to miss (100% accuracy)
2. **Multi-Target**: In double battles, Keen Edge moves that normally target one opponent now hit both opposing Pokemon

### Keen Edge Move Categories
Keen Edge moves are typically slicing, cutting, or chopping attacks that have been designated with the `FLAG_KEEN_EDGE_BOOST` flag. Common examples include:

**Physical Slicing Moves:**
- Slash - High critical hit ratio
- Leaf Blade - Grass-type blade attack
- Dragon Claw - Dragon-type slashing move
- Karate Chop - Fighting-type chopping attack
- Night Slash - Dark-type blade attack
- Psycho Cut - Psychic-type cutting move
- Cross Chop - Fighting-type crossing attack
- Crab Hammer - Water-type claw attack

### Technical Implementation
```cpp
// From src/abilities.cc - Sweeping Edge definition
constexpr Ability SweepingEdge = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        // Check if the move has the Keen Edge flag
        CHECK(gBattleMoves[move].flags & FLAG_KEEN_EDGE_BOOST)
        // Make the move always hit
        return ACCURACY_HITS_IF_POSSIBLE;
    },
};

// From src/battle_util.c - Multi-target conversion
u8 GetBattlerBattleMoveTargetFlags(MoveEnum moveId, u8 battler) {
    // Convert single-target Keen Edge moves to multi-target
    if ((BATTLER_HAS_ABILITY(battler, ABILITY_SWEEPING_EDGE) || 
         BATTLER_HAS_ABILITY(battler, ABILITY_SWEEPING_EDGE_PLUS)) &&
        (gBattleMoves[moveId].flags & FLAG_KEEN_EDGE_BOOST) && 
        gBattleMoves[moveId].target == MOVE_TARGET_SELECTED)
        return MOVE_TARGET_BOTH;
}
```

### Activation Conditions
- **Move requirement**: The move must have the `FLAG_KEEN_EDGE_BOOST` flag
- **Target requirement**: For multi-target effect, the move must normally target a single selected opponent
- **Battle format**: Multi-target effect only applies in double battles where there are two opponents

### Battle Interactions
- **Double battles**: Keen Edge moves hit both opposing Pokemon instead of just one
- **Single battles**: Only the accuracy boost applies (no second target to hit)
- **Accuracy bypass**: Ignores accuracy reductions, evasion boosts, and moves like Sand Attack
- **Critical hits**: Each target is calculated independently for critical hits
- **Contact moves**: Contact effects (like Static, Rough Skin) can trigger from both targets

### Important Interactions
- **Priority moves**: Keen Edge priority moves (if any exist) maintain their priority
- **Multi-hit moves**: Each hit gains perfect accuracy if the move has Keen Edge flag
- **Substitute**: Can hit through Substitute due to perfect accuracy mechanics
- **Protection moves**: Each target's Protect/Detect is calculated separately
- **Abilities that trigger on hit**: Abilities like Color Change trigger separately for each target

### Strategic Applications
- **Double battle dominance**: Transforms single-target slicing moves into powerful spread attacks
- **Accuracy independence**: Never misses regardless of weather, abilities, or stat changes
- **Coverage expansion**: Allows Keen Edge moves to pressure both opponents simultaneously
- **Crit fishing**: More opportunities for critical hits when hitting multiple targets
- **Damage maximization**: Effectively doubles damage output in double battles

### Upgraded Version
**Sweeping Edge Plus (ID 590)** includes the same effects as Sweeping Edge but also gains the offensive power boost from Keen Edge ability, increasing the power of Keen Edge moves by 30%.

### Common Users
Pokemon with access to multiple Keen Edge moves benefit most from this ability:
- Physical attackers with diverse slicing movesets
- Pokemon with high critical hit ratios
- Double battle specialists
- Pokemon that learn moves like Slash, Leaf Blade, Night Slash

### Competitive Usage Notes
- **Double battle meta**: Extremely powerful in VGC-style formats
- **Move selection**: Prioritize Keen Edge moves in moveset planning
- **Team positioning**: Pair with Pokemon that can set up favorable double battle scenarios
- **Damage calculation**: Remember that spread moves typically deal reduced damage in official formats

### Counters
- **Wide Guard**: Blocks the spread effect of converted moves
- **Ability suppression**: Mold Breaker, Neutralizing Gas disable the ability
- **Single battles**: Reduces effectiveness to accuracy boost only
- **Non-Keen Edge moves**: Ability doesn't affect moves without the flag
- **Ghost types**: Immune to Normal/Fighting Keen Edge moves

### Synergies
- **High critical hit ratio**: Many Keen Edge moves have increased crit rates
- **Speed control**: Pair with fast Pokemon to move first in double battles  
- **Setup moves**: Works well after Swords Dance or similar attack boosts
- **Entry hazards**: Spikes/Stealth Rock damage both targets after spread moves
- **Follow-up attacks**: Weakened opponents from spread moves easier to finish

### Move Compatibility
Not all slicing moves are Keen Edge moves. The ability only affects moves specifically flagged with `FLAG_KEEN_EDGE_BOOST`. Check individual move descriptions for "Keen Edge boost" to confirm compatibility.

### Version History
- Elite Redux exclusive ability (ID 421)
- Upgraded version Sweeping Edge Plus available (ID 590)
- Part of the expanded ability system focusing on move type synergies
---
id: 439
name: Angel's Wrath
status: reviewed
character_count: 295
---

# Angel's Wrath - Ability ID 439

## In-Game Description
"Drastically alters all of the users moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Tackle Encores+Disables, String Shot sets all hazards, Harden omniboosts by one stage, Iron Defense becomes a King's Shield that drops all stats, Electroweb traps, Bug Bite heals damage dealt, Poison Sting badly poisons+is super-effective on Steel. All enhanced attacks get a large damage boost.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Angel's Wrath is a unique transformation ability that completely replaces the effects of six specific moves when used by a Pokemon with this ability. Each transformed move gains powerful new effects that are drastically different from their original functions.

### Move Transformations

#### Tackle to Control Moves
- **Effect**: Applies both Encore and Disable to the target
- **Encore Duration**: 2 turns (forces opponent to use their first move)
- **Disable Duration**: 2 turns (prevents use of their first move)
- **Accuracy**: Always hits (ACCURACY_HITS_IF_POSSIBLE)
- **Condition**: Requires successful hit and target not protected from status

#### String Shot to Full Hazard Setup  
- **Effect**: Sets all four entry hazards on opponent's side simultaneously
- **Hazards Applied**:
  - Stealth Rock (Rock-type)
  - Toxic Spikes (2 layers for badly poisoned)
  - Spikes (3 layers for maximum damage)  
  - Sticky Web (speed reduction)
- **Condition**: Only applies hazards that aren't already present

#### Harden to Omni-Boost
- **Effect**: Boosts all stats except Defense by +1 stage
- **Stats Boosted**: Attack, Special Attack, Special Defense, Speed
- **Condition**: Must have at least one stat that can be raised

#### Iron Defense to Angel's Protection
- **Effect**: Grants protection status similar to King's Shield
- **Protection**: Blocks all damaging moves for the turn
- **Counter-Effect**: When protection is triggered, applies special effect to attacker
- **Duration**: One turn (like other protection moves)

#### Electroweb to Speed Control
- **Effect**: Minimizes target's Speed and traps them
- **Speed Reduction**: Sets Speed to minimum stage (-6)
- **Trapping**: Applies escape prevention (like Block/Mean Look)
- **Type Effectiveness**: Super effective against Ground types (2x damage)
- **Accuracy**: Always hits (ACCURACY_HITS_IF_POSSIBLE)

#### Bug Bite to Healing Bite
- **Effect**: Heals user for damage dealt to opponent
- **Healing Amount**: Restores HP equal to damage inflicted
- **Minimum Heal**: At least 1 HP if no damage dealt
- **Condition**: User must not be at full HP and must be able to heal

### Technical Implementation
```c
// Angel's Wrath ability structure
constexpr Ability AngelsWrath = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        // Move-specific transformations
        switch (move) {
            case MOVE_TACKLE:
                // Apply Encore + Disable effects
                break;
            case MOVE_STRING_SHOT:
                // Set all entry hazards
                break;
            // ... other transformations
        }
    },
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        // Most transformed moves always hit
        return ACCURACY_HITS_IF_POSSIBLE;
    },
    .onTypeEffectiveness = +[](ON_TYPE_EFFECTIVENESS) -> int {
        // Special type effectiveness overrides
    }
};
```

### Strategic Applications

#### Control Strategy
- **Tackle**: Creates a paradox where opponent is forced to use a disabled move
- **String Shot**: Instant full hazard setup in one turn
- **Electroweb**: Complete speed control and trapping

#### Support Strategy  
- **Harden**: Provides immediate stat boosts for sweeping
- **Iron Defense**: Defensive utility with protection
- **Bug Bite**: Sustain and longevity through healing

#### Team Synergy
- **Hazard Support**: String Shot provides instant hazard pressure
- **Speed Control**: Electroweb enables slower teammates
- **Stat Passing**: Harden boosts can support Baton Pass strategies

### Competitive Implications

#### Advantages
- **Versatility**: Six different utility options in one ability
- **Unpredictability**: Opponents must prepare for multiple threats
- **Action Economy**: Each move provides multiple effects
- **Accuracy Override**: Most moves become impossible to miss

#### Limitations  
- **Move Dependence**: Requires specific moves in moveset
- **Predictability**: Effects are known once ability is revealed
- **Move Slot Competition**: Must sacrifice moveset diversity
- **Counters**: Standard ability suppression stops all effects

### Counters and Interactions

#### Ability Suppression
- **Mold Breaker**: Ignores Angel's Wrath entirely
- **Neutralizing Gas**: Disables all transformations
- **Skill Swap/Role Play**: Can transfer or copy the ability

#### Status Protection
- **Encore/Disable**: Mental Herb, Own Tempo, Oblivious
- **Trapping**: Ghost types immune to Electroweb trapping
- **Entry Hazards**: Magic Bounce reflects String Shot hazards

#### Protection Moves
- **Angel's Protection**: Functions like other protection moves
- **Consecutive Use**: Decreasing success rate with repeated use
- **Piercing Moves**: Feint can break the protection

### Movepool Considerations

#### Required Moves for Full Utility
1. **Tackle** - Control and disruption  
2. **String Shot** - Hazard setup
3. **Harden** - Stat boosting
4. **Iron Defense** - Protection
5. **Electroweb** - Speed control and trapping
6. **Bug Bite** - Healing and sustain

#### Moveset Planning
- **Core Coverage**: 2-3 transformed moves typically sufficient
- **Coverage Moves**: Reserve slots for type coverage
- **Priority Selection**: Choose based on team role and strategy

### Usage Examples

#### Hazard Setter Build
- String Shot (full hazards)
- Harden (setup boosts)  
- Coverage move
- Recovery/utility move

#### Control Build  
- Tackle (Encore+Disable)
- Electroweb (trap+speed)
- Iron Defense (protection)
- Coverage move

#### Sustain Build
- Bug Bite (healing)
- Harden (stat boosts)
- Iron Defense (protection)
- Coverage move

### Pokemon Compatibility
Angel's Wrath works best on Pokemon that can naturally learn multiple transformation moves and benefit from the diverse utility effects. The ability is particularly valuable on support-oriented Pokemon that can capitalize on the control and setup aspects.

### Version Notes
- Unique to Elite Redux
- One of the most complex transformation abilities
- Requires understanding of multiple game mechanics
- Each transformation has specific activation conditions
- Protection effect follows standard protection move rules
---
id: 150
name: Imposter
status: reviewed
character_count: 289
---

# Imposter - Ability ID 150

## In-Game Description
"Transforms into the foe on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Transforms the Pokemon into the opponent upon switching in. Copies their appearance, stats (minus HP), types, abilities, moves, and stat changes. Each copied move has 5 PP. Cannot transform if the target has Substitute, is already transformed, has Illusion active, or is semi-invulnerable.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Imposter activates automatically when the Pokemon enters battle (switch-in or battle start). It copies the target's complete battle data using the same transformation mechanics as the move Transform.

### Target Selection Priority
1. **Primary Target**: Direct opponent (opposite battler)
2. **Fallback Target**: Opponent's partner if primary target is fainted (doubles)
3. **No Valid Target**: Ability fails if no alive opponents exist

### Transformation Process
The ability performs a complete transformation that copies:
- **Species**: Visual appearance changes to match target
- **Stats**: All battle stats (Attack, Defense, Special Attack, Special Defense, Speed)
- **Types**: Primary, secondary, and tertiary types
- **Abilities**: All four abilities (1 changeable + 3 innates in Elite Redux)
- **Movesets**: All four moves from the target
- **Stat Stages**: Current stat modifications (+1 Attack, -2 Speed, etc.)

### PP Management
Each copied move receives PP according to these rules:
```c
if (move's base PP < 5)
    copied_move_pp = move's base PP
else
    copied_move_pp = 5
```

### Activation Restrictions
Imposter **CANNOT** transform if the target:
- Has STATUS2_TRANSFORMED (already transformed via Transform move or another Imposter)
- Has STATUS2_SUBSTITUTE (behind a Substitute)
- Has active Illusion ability effect
- Has STATUS3_SEMI_INVULNERABLE (using moves like Fly, Dig, Dive)

### Battle Message
Upon successful transformation: "*{Pokemon} transformed into {Target} using Imposter!*"

### Interaction with Elite Redux Multi-Ability System
In Elite Redux's 4-ability system, Imposter copies:
- **Changeable Ability**: The target's currently active changeable ability
- **Fixed Innate Abilities**: All three of the target's innate abilities
- This makes Imposter extremely powerful as it gains access to four abilities simultaneously

### Strategic Applications
1. **Scouting**: Reveals opponent's exact stats, moves, and abilities
2. **Stat Stealing**: Inherits any stat boosts the target accumulated
3. **Type Advantage**: Can gain favorable typing matchups
4. **Movepool Access**: Gains access to the target's entire moveset
5. **Ability Stacking**: In Elite Redux, gains up to 4 abilities from the target

### Technical Implementation
- **Entry Point**: `abilities.cc` line ~1715 in `Imposter` ability definition
- **Battle Script**: `BattleScript_ImposterActivates` handles animation and message
- **Transform Command**: Uses `transformdataexecution` battle script command
- **Status Flag**: Sets STATUS2_TRANSFORMED to prevent re-transformation

### Common Users in Elite Redux
- **Ditto**: Primary Imposter user with supporting innate abilities
- **Mew**: Alternative Imposter user with enhanced versatility
- **Other species**: Various Pokemon may have Imposter as an ability option

### Counters and Limitations
1. **Substitute**: Blocks transformation entirely
2. **Illusion**: Prevents targeting the real Pokemon
3. **Semi-invulnerable states**: Flying, underground, or underwater Pokemon cannot be copied
4. **Pre-transformation**: Already transformed Pokemon cannot be targeted
5. **Low PP**: Copied moves only have 5 PP maximum

### Example Scenarios
**Scenario 1 - Basic Transformation**:
- Ditto with Imposter switches in against Garchomp
- Ditto becomes Garchomp with all its stats, moves, and abilities
- Each copied move has 5 PP

**Scenario 2 - Stat Boost Inheritance**:
- Target Dragonite has +2 Attack from Dragon Dance
- Imposter copies Dragonite including the +2 Attack boost
- Transformed Pokemon starts with boosted stats

**Scenario 3 - Blocked by Substitute**:
- Target Pokemon is behind Substitute
- Imposter fails to activate
- Original Pokemon remains unchanged

### Damage Calculations
Imposter doesn't directly affect damage calculations but provides access to the target's full combat potential, including their base stats, STAB bonuses, and ability effects.
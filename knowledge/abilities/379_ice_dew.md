---
id: 379
name: Ice Dew
status: reviewed
character_count: 165
---

# Ice Dew - Ability ID 379

## In-Game Description
"Redirects Ice moves to self and boosts highest attacking stat."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Redirects all Ice-type moves to this Pokemon and absorbs them. Upon absorbing an Ice move, boosts either Attack or Special Attack (whichever is higher) by one stage.

## Detailed Mechanical Explanation

### Overview
Ice Dew is a defensive redirection ability that automatically absorbs all Ice-type moves targeted at the user or their allies, completely negating their damage while providing a valuable stat boost. This ability makes the user immune to Ice-type attacks while turning them into an opportunity for offensive momentum.

## Technical Implementation

### Core Mechanism
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc` (Lines 3935-3943)

```cpp
constexpr Ability IceDew = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_ICE);
        *statId = GetHighestAttackingStatId(battler, TRUE);
        return ABSORB_RESULT_STAT;
    },
    .redirectType = TYPE_ICE,
    .breakable = TRUE,
};
```

### Stat Selection Logic
**File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/battle_util.c` (Lines 8585-8603)

The `GetHighestAttackingStatId` function determines whether to boost Attack or Special Attack:
- Compares the user's current Attack and Special Attack stats (including stat stage modifications)
- Always chooses the higher of the two attacking stats
- If both stats are equal, defaults to Attack
- Takes into account current stat stage boosts/drops when making the determination

### Key Properties
- **Redirection**: `redirectType = TYPE_ICE` - All Ice moves are redirected to this Pokemon
- **Breakable**: `breakable = TRUE` - Can be suppressed by Mold Breaker and similar abilities
- **Absorption Result**: `ABSORB_RESULT_STAT` - Provides a stat boost upon successful absorption

## Battle Mechanics

### Activation Conditions
1. An Ice-type move is used anywhere on the battlefield
2. The move would normally target any Pokemon other than the Ice Dew user
3. The ability has not been suppressed by Mold Breaker effects

### Effect Resolution
1. **Move Redirection**: The Ice move is automatically redirected to the Ice Dew user
2. **Damage Negation**: The move deals 0 damage to the Ice Dew user
3. **Stat Boost**: The user's highest attacking stat is raised by 1 stage
4. **Priority**: The stat boost occurs immediately after move redirection

### Interaction with Multi-Target Moves
- Ice moves that target multiple Pokemon (like Blizzard) will be completely redirected to the Ice Dew user
- Only one stat boost is gained regardless of how many targets the original move had

## Strategic Applications

### Defensive Utility
- **Ice Immunity**: Provides complete protection from Ice-type attacks
- **Team Protection**: Protects all team members from Ice moves, not just the user
- **Hail Immunity**: While not explicitly stated, the redirection prevents Ice-type moves from hitting during Hail

### Offensive Momentum
- **Reliable Boost**: Guaranteed stat increase when absorbing Ice moves
- **Flexible Enhancement**: Boosts the user's better attacking stat, adapting to their stat spread
- **Setup Opportunity**: Can be used to set up sweeps by intentionally absorbing Ice moves

### Doubles/Triples Strategy
- **Team Synergy**: Particularly valuable in multi-battle formats where allies can be protected
- **Pivot Role**: Can serve as a defensive pivot that gains offensive momentum
- **Weather Teams**: Synergizes well with Hail teams that might face Ice-type counters

## Competitive Analysis

### Strengths
1. **Complete Ice Immunity**: Total protection from a common attacking type
2. **Offensive Momentum**: Turns defensive plays into offensive opportunities  
3. **Team Support**: Protects entire team from Ice-type moves
4. **Adaptive Boosting**: Always enhances the user's better attacking stat
5. **Predictable Benefit**: Reliable stat boost unlike RNG-dependent abilities

### Weaknesses
1. **Mold Breaker Vulnerability**: Can be completely bypassed by certain abilities
2. **Limited Type Coverage**: Only affects Ice-type moves
3. **Situational Activation**: Requires opponents to use Ice-type attacks
4. **Single Boost**: Only provides +1 stat boost per activation
5. **Setup Dependency**: Best utilized by Pokemon that can capitalize on stat boosts

### Meta Game Impact
- **Tier Rating**: Medium - Strong defensive utility but limited by situational nature
- **Team Building**: Excellent on teams weak to Ice-type moves
- **Counter Play**: Opponents may avoid Ice moves entirely, reducing ability value
- **Synergy Potential**: High synergy with other setup abilities and stat-based strategies

## Notable Users

### Primary Ability Users
- **Alolan Vulpix** - Benefits from Special Attack boosts for special sweeping
- **Pikachu-Belle** - Electric/Ice typing with flexible stat boosting
- **Rotom-Frost** - Defensive pivot that can transition to offense
- **Silvally-Ice** - Adaptable stat distribution makes either Attack or Special Attack viable
- **Eiscue-Noice Face** - Physical attacker that appreciates Attack boosts

### Team Composition Roles
- **Defensive Core**: Serves as an Ice-type answer for teams weak to Ice moves
- **Setup Sweeper**: Can use absorbed moves as setup opportunities
- **Utility Pivot**: Provides team support while maintaining offensive presence

## Related Abilities

### Similar Redirection Abilities
- **Lightning Rod** (Ability #31): Redirects Electric moves, raises Special Attack
- **Storm Drain** (Ability #114): Redirects Water moves, raises Special Attack  
- **Sap Sipper** (Ability #157): Redirects Grass moves, raises Attack
- **Heat Sink** (Custom): Redirects Fire moves, raises highest attacking stat

### Key Differences
- **Stat Selection**: Ice Dew and Heat Sink dynamically choose between Attack/Special Attack
- **Type Coverage**: Each redirection ability covers a different offensive type
- **Strategic Niche**: Ice Dew specifically counters Ice-type offensive strategies

### Synergistic Abilities
- **Refrigerate**: Converts Normal moves to Ice-type, potentially triggering ally Ice Dew
- **Snow Warning**: Sets up Hail, which may prompt opponents to use Ice moves
- **Ice Body**: Provides passive healing in Hail while Ice Dew handles offensive Ice moves

## Counterplay and Responses

### Direct Counters
- **Mold Breaker**: Completely bypasses the ability
- **Teravolt/Turboblaze**: Ignores the redirection effect
- **Type Coverage**: Use non-Ice moves to avoid triggering the ability

### Strategic Adaptations
- **Move Selection**: Avoid Ice-type moves when facing Ice Dew users
- **Ability Suppression**: Use abilities or moves that can disable Ice Dew
- **Priority Moves**: Fast moves that can potentially KO before setup occurs

## Version History and Balance

### Implementation Status
- **Current Status**: Fully implemented and functional
- **Balance State**: Well-balanced defensive ability with clear counterplay
- **Usage Rate**: Moderate usage among Ice-type specialists and defensive teams

### Design Philosophy
Ice Dew follows the established pattern of type-specific redirection abilities while adding the innovative mechanic of flexible stat boosting. This creates a more adaptable ability that can benefit both physical and special attackers depending on their stat distribution.

## Conclusion

Ice Dew represents a well-designed defensive ability that provides reliable protection from Ice-type moves while offering meaningful offensive momentum. Its adaptive stat boosting mechanism makes it valuable for a variety of Pokemon builds, while its clear limitations and counterplay options keep it balanced. The ability excels in its niche of Ice-type defense while maintaining strategic depth through its flexible boosting mechanics.


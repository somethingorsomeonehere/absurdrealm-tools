---
id: 871
name: Fire Aspect
status: reviewed
character_count: 145
---

# Fire Aspect - Ability ID 871

## In-Game Description
"Absorbs fire moves and always burns with fire."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

The user gains immunity to Fire-type moves and they heal for 25% of their max HP when hit by them. Always burn with moves that can activate them.

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Fire Aspect is an absorption ability that completely negates Fire-type moves while providing significant healing. When targeted by any Fire-type move, the user absorbs the attack and converts it into HP recovery.

### Activation Conditions
- **Move requirement**: Any Fire-type move targeting the user
- **Absorption scope**: All fire moves (physical, special, and status moves)
- **Healing amount**: 25% of maximum HP restored
- **Damage negation**: User takes no damage from the absorbed move
- **Secondary effects**: Move's secondary effects are also negated

### Technical Implementation
```c
constexpr Ability FireAspect = {
    .onAbsorb = +[](ON_ABSORB) -> int {
        CHECK(moveType == TYPE_FIRE)
        return ABSORB_RESULT_HEAL;
    },
    .breakable = TRUE,
};
```

### Important Interactions
- **Status moves**: Absorbs Fire-type status moves (Will-O-Wisp, etc.)
- **Multi-hit moves**: Each hit is absorbed and heals separately
- **HP recovery**: Works even at full HP (move still fails to deal damage)
- **Ability suppression**: Doesn't work if ability is suppressed (Mold Breaker, etc.)
- **Redirection**: Can absorb redirected fire moves from Storm Drain, etc.

### Move Coverage
Fire Aspect absorbs all Fire-type moves including:
- **Physical**: Flare Blitz, Fire Punch, Flame Wheel, etc.
- **Special**: Flamethrower, Fire Blast, Overheat, etc.
- **Status**: Will-O-Wisp, Sunny Day (if Fire-typed), etc.
- **Z-moves**: Fire-type Z-moves are completely absorbed
- **Max moves**: Max Flare and other fire Max moves

### "Always Burns With Fire" Effect
The description suggests thematic constant burning, which may represent:
- The user's internal fire being fueled by absorbed flames
- Persistent fire energy within the Pokemon
- Possible future implementation of self-burn status with benefits
- Currently implemented as standard fire absorption with healing

### Strategic Implications
- **Fire immunity**: Complete immunity to all Fire-type attacks
- **Healing factor**: Turns weaknesses into recovery opportunities  
- **Switch-in value**: Excellent for switching into predicted fire moves
- **Stall potential**: Can repeatedly heal against fire-type attackers
- **Team synergy**: Protects team from fire moves in doubles

### Common Users
- Fire/Water dual-types that resist their own type
- Defensive Pokemon that can wall fire attackers
- Pokemon with secondary Fire typing
- Mixed walls that need fire immunity

### Competitive Usage Notes
- Excellent against Fire-type spam teams
- Provides reliable healing against fire attackers
- Can bait fire moves for free recovery
- Pairs well with other absorption abilities for type coverage
- Strong in metagames with prevalent fire moves

### Counters
- **Non-fire coverage**: Use non-Fire attacks to bypass absorption
- **Ability suppression**: Mold Breaker, Neutralizing Gas, etc.
- **Indirect damage**: Entry hazards, weather damage, status
- **Setup opportunities**: Use fire immunity to set up stats
- **Taunt**: Prevent defensive plays while they heal

### Synergies
- **Other absorb abilities**: Stack type immunities (Water Absorb, etc.)
- **Recovery moves**: Combine with Recover for exceptional bulk
- **Defensive investment**: Maximize bulk to wall physical attackers
- **Fire resistance**: Stack with natural fire resistance for redundancy
- **Healing items**: Leftovers/Black Sludge for passive recovery

### Version History
- Elite Redux exclusive ability
- Part of the expanded absorption ability family
- ID 871 in the ability enum
- Breakable ability (can be suppressed)
- May receive future updates to "burns with fire" mechanic

### Comparison to Similar Abilities
- **Flash Fire**: Fire Aspect heals instead of boosting attack
- **Water Absorb**: Same healing mechanism, different type
- **Volt Absorb**: Identical function for Electric-type moves
- **Dry Skin**: Fire Aspect only benefits from fire (no drawbacks)
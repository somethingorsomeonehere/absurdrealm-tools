---
id: 506
name: Determination
status: reviewed
character_count: 141
---

# Determination - Ability ID 506

## In-Game Description
"Ups Special Attack by 50% if suffering."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Boosts Special Attack stat by 50% when the Pokemon has any status condition. Also prevents the frostbite status from reducing Special Attack. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Determination is an offensive ability that provides a substantial power boost to special attacks when the Pokemon is afflicted with status conditions. The ability specifically targets special moves and provides damage immunity negation.

### Activation Conditions
- **Status requirement**: Any status condition must be present:
  - Burn
  - Poison (including badly poisoned)
  - Paralysis
  - Sleep
  - Freeze
  - Comatose ability active
  - Blood Stain effects (Elite Redux specific)
- **Move type**: Only affects special moves (Special Attack-based)
- **Damage boost**: Exactly 50% increase (multiplier of 1.5)

### Technical Implementation
```c
constexpr Ability Determination = {
    .onOffensiveMultiplier =
        +[](ON_OFFENSIVE_MULTIPLIER) {
            if (HasAnyStatusOrAbility(battler) && IS_MOVE_SPECIAL(move)) MUL(1.5);
        },
    .negatesFrzSpatkDrop = TRUE,
};
```

### Special Properties
- **Freeze immunity negation**: Prevents the freeze status from reducing Special Attack
- **Special move only**: Only affects moves that use the Special Attack stat
- **Status dependency**: Requires status condition to activate

### Important Interactions
- **Guts comparison**: Similar to Guts but for special moves instead of physical
- **Comatose synergy**: Always active with Comatose ability users
- **Status absorption**: Can benefit from intentional status infliction
- **Freeze protection**: Unique property among status-boosting abilities
- **Multi-hit moves**: Boost applies to each hit if special-based

### HasAnyStatusOrAbility Function
The ability uses a specific function that checks for:
- Any STATUS1 status condition
- Comatose ability (counts as permanent "status")
- Blood Stain effects (Elite Redux mechanic)

### Strategic Implications
- **Status synergy**: Benefits from being statused unlike most Pokemon
- **Special wallbreaker**: Turns status conditions into offensive pressure
- **Risk/reward**: High power boost compensates for status drawbacks
- **Anti-freeze**: Maintains Special Attack power even when frozen
- **Team support**: Can be paired with status inflictors

### Common Users
- Special attacking Pokemon who can afford status conditions
- Bulky special attackers who can survive status damage
- Pokemon with status-healing moves or abilities
- Rest users who can sleep safely

### Competitive Usage Notes
- **Flame Orb/Toxic Orb synergy**: Intentional status for guaranteed boost
- **Rest compatibility**: Can sleep and still hit hard
- **Status immunity bypass**: Makes status moves beneficial rather than harmful
- **Freeze counter**: Unique in not losing Special Attack when frozen
- **Defensive pivot**: Can switch into status moves for offensive gains

### Counters
- **Physical attackers**: Ability doesn't boost physical moves
- **Status cure**: Healing status removes the damage boost
- **Ability suppression**: Mold Breaker, Neutralizing Gas
- **Taunt**: Prevents Rest or status-healing moves
- **Magic Guard**: Negates status damage while keeping boost

### Synergies
- **Status Orbs**: Flame Orb, Toxic Orb for guaranteed activation
- **Rest**: Sleep status provides boost while healing
- **Aromatherapy/Heal Bell**: Can remove status when boost isn't needed
- **Substitute**: Protects from status while keeping existing conditions
- **Safeguard**: Can prevent unwanted status changes

### Comparison to Similar Abilities
- **Guts**: Physical equivalent, also has burn attack negation
- **Quick Feet**: Speed boost from status instead of attack
- **Marvel Scale**: Defense boost from status conditions
- **Poison Heal**: Healing from poison instead of attack boost

### Version History
- Elite Redux custom ability
- Part of the extended ability system
- Similar design to Guts but for special attackers
- Includes unique freeze Special Attack protection

### Elite Redux Specific Notes
- Benefits from the 4-ability system as innate or changeable ability
- Synergizes with other status-based abilities in multi-ability builds
- Can be combined with defensive abilities for status tank builds
- Blood Stain interaction is unique to Elite Redux mechanics
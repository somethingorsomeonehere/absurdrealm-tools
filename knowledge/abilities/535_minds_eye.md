---
id: 535
name: Mind's Eye
status: reviewed
character_count: 213
---

# Mind's Eye - Ability ID 535

## In-Game Description
"Hits Ghost-type Pokemon. Accuracy can't be lowered."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Mind's Eye allows Normal and Fighting-type moves to hit Ghost-type Pokemon with normal effectiveness. Additionally, this ability prevents the user's accuracy stat from being lowered by opposing moves or abilities.

## Detailed Mechanical Explanation
*For Discord/reference use*

Mind's Eye is a dual-purpose ability that provides both offensive and defensive benefits:

### Core Mechanics

1. **Ghost-type Immunity Bypass**: 
   - Normal and Fighting-type moves used by the Mind's Eye user can hit Ghost-type Pokemon
   - These moves deal normal (1.0x) effectiveness damage instead of having no effect (0.0x)
   - Uses the same mechanism as Scrappy ability's `onTypeEffectiveness` function

2. **Accuracy Protection**:
   - Prevents the user's accuracy stat from being lowered below its starting value
   - Protects against moves like Sand Attack, Mud-Slap, Flash, Smokescreen
   - Protects against abilities that lower accuracy
   - Does NOT protect against evasion boosts on the opponent

### Technical Implementation

```cpp
constexpr Ability MindsEye = {
    .onTypeEffectiveness = Scrappy.onTypeEffectiveness,  // Ghost immunity bypass
    .breakable = TRUE,
};
```

**Accuracy Protection Code**:
```cpp
// In battle script commands - prevents accuracy lowering
if (BATTLER_HAS_ABILITY(battler, ABILITY_MINDS_EYE) && statId == STAT_ACC) {
    // Trigger ability popup and prevent stat reduction
    gBattleScripting.abilityPopupOverwrite = ABILITY_MINDS_EYE;
    // Ability prevents the accuracy drop
}

// In accuracy calculation - ignores negative evasion stages
if (BATTLER_HAS_ABILITY(battlerAtk, ABILITY_MINDS_EYE))
    evasionStage = min(evasionStage, DEFAULT_STAT_STAGE);
```

### Activation Conditions

1. **Ghost-type Bypass**: Activates when using Normal or Fighting-type moves against Ghost-type targets
2. **Accuracy Protection**: Activates when opponent attempts to lower the user's accuracy stat

### Affected Moves (Accuracy Lowering)

Mind's Eye protects against accuracy-lowering effects from:
- Sand Attack, Mud-Slap, Muddy Water
- Flash, Smokescreen, Octazooka
- Any move with secondary effect that lowers accuracy
- Abilities like Tangling Hair (when it affects accuracy)

### Interactions with Other Mechanics

- **Mold Breaker**: Mind's Eye is breakable, so Mold Breaker bypasses both effects
- **Foresight/Odor Sleuth**: Mind's Eye provides the same Ghost-hitting effect as these moves
- **Clear Amulet**: Item-based accuracy protection stacks with Mind's Eye
- **Keen Eye**: Similar accuracy protection but different implementation

### Strategic Implications

**Offensive Benefits**:
- Allows Normal and Fighting-type attackers to threaten Ghost-types
- Particularly valuable for physical attackers using moves like Body Slam, Close Combat
- Enables STAB Normal/Fighting moves to have universal coverage

**Defensive Benefits**:
- Maintains consistent accuracy throughout battle
- Counters accuracy-dropping strategies
- Valuable against Pokemon that rely on evasion tactics

### Common Users

Based on the codebase analysis, Mind's Eye appears as an innate ability on certain Pokemon, providing consistent utility throughout battle.

### Competitive Usage Notes

- **Offensive Role**: Best used on physically offensive Normal or Fighting-types
- **Anti-Evasion**: Counters opponents who rely on accuracy drops for survivability
- **Consistent Performance**: Ensures reliable hit rates for powerful moves
- **Ghost Coverage**: Provides crucial coverage against Ghost-type switch-ins

### Counters

- **Mold Breaker**: Completely bypasses both effects
- **Type Resistances**: Ghost-types can still resist the attacks (just not be immune)
- **Other Stat Drops**: Doesn't protect against Attack, Speed, or other stat reductions

### Synergies

- **High-power Normal/Fighting moves**: Body Slam, Close Combat, Double-Edge
- **Accuracy-dependent moves**: Focus Blast, Dynamic Punch benefit from consistent accuracy
- **Physical attackers**: Pairs well with strong physical movesets
- **Choice items**: Maintains accuracy while locked into moves

### Version History

Mind's Eye was implemented in Elite Redux as ability ID 535, combining the Ghost-hitting effect of Scrappy with the accuracy protection similar to Keen Eye, creating a unique dual-purpose ability for balanced offensive and defensive utility.
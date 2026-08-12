---
id: 436
name: Atlas
status: reviewed
character_count: 249
---

# Atlas - Ability ID 436

## In-Game Description
"Sets Gravity on entry for 8 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Atlas sets Gravity upon entering battle for 8 turns. Gravity prevents levitating moves like Fly; grounds all Pokemon making them vulnerable to Ground moves, Arena Trap, and hazards; boosts Grav Apple's damage by 50%; and boosts move accuracy by 66%. 

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Atlas is an entry ability that automatically activates the Gravity field condition when the Pokemon enters battle. This field effect lasts for 8 turns, which is longer than the standard 5-turn Gravity duration from the move or Gravity Well ability.

### Activation Conditions
- **Entry trigger**: Activates automatically when the Pokemon switches in or battle begins
- **Fails if**: Gravity is already active on the field
- **Duration**: 8 turns (GRAVITY_DURATION_EXTENDED vs standard 5 turns)
- **Cannot be extended**: Once set, the duration is fixed

### Gravity Field Effects
When Gravity is active, it affects all battlers with the following changes:

#### Move Restrictions
Gravity prevents the use of several levitating moves:
- **Bounce**: Two-turn flying move
- **Fly**: Two-turn flying move
- **Flying Press**: Flying-type contact move
- **High Jump Kick**: High-damage Fighting move
- **Jump Kick**: Lower-damage Fighting move
- **Magnet Rise**: Self-levitation move
- **Sky Drop**: Two-turn carry move
- **Splash**: Non-damaging Normal move
- **Telekinesis**: Levitation status move
- **Floaty Fall**: Flying-type move
- **Seismic Toss**: Fixed damage move

#### Accuracy Boost
- **All moves**: +66% accuracy (multiplied by 5/3)
- **Stacks with**: Other accuracy modifiers
- **Applies to**: All Pokemon on the field

#### Grounding Effects
- **All Pokemon**: Become grounded regardless of type or ability
- **Ground immunity**: Flying types and Levitate users lose Ground immunity
- **Magnet Rise**: Cannot be used and existing effects are suppressed
- **Telekinesis**: Cannot be used and existing effects end
- **Air Balloon**: Effect is suppressed but item isn't consumed

### Technical Implementation
```c
// Atlas triggers on entry with extended duration
constexpr Ability Atlas = {
    .onEntry = +[](ON_ENTRY) -> int {
        CHECK_NOT(gFieldStatuses & STATUS_FIELD_GRAVITY)

        gFieldTimers.started.gravity = TRUE;
        gFieldTimers.gravityTimer = GRAVITY_DURATION_EXTENDED; // 8 turns
        gFieldStatuses |= STATUS_FIELD_GRAVITY;
        BattleScriptPushCursorAndCallback(BattleScript_GravityStarts);
        return TRUE;
    },
};
```

### Important Interactions
- **Clueless ability**: Completely negates Gravity effects
- **Multiple entries**: Does not refresh duration if already active
- **Field conditions**: Cannot be stacked with other Gravity sources
- **Grav Apple**: Gains 50% power boost under Gravity
- **Iron Ball**: Redundant grounding effect but stacks with accuracy

### Comparison with Related Abilities
- **Gravity Well (ID 413)**: Sets Gravity for only 5 turns (standard duration)
- **Gravity move**: Also 5 turns but uses a move slot
- **Atlas advantage**: Longest Gravity duration available

### Strategic Implications
- **Team support**: Excellent for teams with low-accuracy moves
- **Ground coverage**: Enables Ground moves against Flying types
- **Anti-evasion**: Counters Double Team and other evasion strategies
- **Entry punishment**: Forces opponents to adapt their strategy immediately
- **No downsides**: Pure beneficial field effect for most teams

### Common Users
Atlas is typically found on:
- Ground-type Pokemon who benefit from hitting Flying types
- Pokemon with low-accuracy but high-power moves
- Support Pokemon designed to assist their team
- Bulky entry hazard setters who can afford an entry ability

### Competitive Usage Notes
- **Pivot potential**: Switch in to set Gravity, then pivot out
- **Wallbreaker support**: Helps wallbreakers land crucial moves
- **Sleep teams**: Enables reliable Sleep Powder/Hypnosis accuracy
- **OHKO moves**: Massive accuracy boost for Fissure, Horn Drill, etc.
- **Duration management**: Plan team strategy around 8-turn window

### Counters
- **Clueless ability**: Completely negates all Gravity effects
- **Switching**: Remove the Atlas user to prevent reactivation
- **Weather override**: No direct counter, must wait out duration
- **High-accuracy moves**: Less benefit from the accuracy boost

### Synergies
- **Low-accuracy moves**: Hypnosis, Focus Blast, Stone Edge
- **Ground moves**: Earthquake, Earth Power against Flying types
- **OHKO moves**: Fissure, Horn Drill, Sheer Cold, Guillotine
- **Grav Apple users**: 50% power boost from Gravity
- **Status moves**: Sleep Powder, Will-O-Wisp accuracy boost

### Version History
- Elite Redux exclusive ability
- Provides longest Gravity duration in the game
- Designed as an entry hazard support ability
- More reliable than move-based Gravity setup

### Ability ID Conflicts
Be careful not to confuse with:
- **Gravity Well (ID 413)**: Only 5-turn duration
- **Regular Gravity move**: Also 5-turn duration
- Atlas provides superior 8-turn extended effect
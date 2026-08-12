---
id: 552
name: Terminal Velocity
status: reviewed
character_count: 116
---

# Terminal Velocity - Ability ID 552

## In-Game Description
"Special moves use 20% of its Speed stat additionally."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Adds 20% of the user's Speed stat to damage when using non-contact moves. Choice Scarf does not affect this ability.

## Detailed Mechanical Explanation
*For Discord/reference use*

Terminal Velocity is a powerful offensive ability that enhances special attacks by incorporating the user's Speed stat into damage calculations.

### Core Mechanics
- **Activation**: Triggers automatically when using any special move (split == SPLIT_SPECIAL)
- **Effect**: Adds 20% of the user's current Speed stat to the Special Attack stat for damage calculation
- **Implementation**: Uses the `onChooseOffensiveStat` hook with `secondaryAtkStatToUse[STAT_SPEED] += 20`

### Technical Implementation
The ability works through Elite Redux's secondary stat system:

```c
constexpr Ability TerminalVelocity = {
    .onChooseOffensiveStat =
        +[](ON_CHOOSE_OFFENSIVE_STAT) {
            if (IS_MOVE_SPECIAL(move)) secondaryAtkStatToUse[STAT_SPEED] += 20;
        },
};
```

In the damage calculation (`CalculateStat` function):
```c
// Line 7083: Add 20% of current Speed stat to Special Attack
statBase += CalculateStat(battler, STAT_SPEED, 0, move, isAttack, isCrit, isUnaware, TRUE) * 20 / 100;
```

### Calculation Order
1. Base Special Attack stat is calculated with stages/modifiers
2. Current Speed stat is calculated with stages/modifiers  
3. 20% of Speed (Speed x 0.2) is added to Special Attack
4. Final Special Attack value is used in damage formula

### Affected Moves
- **All Special Moves**: Any move with split == SPLIT_SPECIAL
- **Status Moves**: Not affected (only damaging special moves)
- **Physical Moves**: Not affected
- **Multi-hit Moves**: Each hit benefits from the Speed bonus
- **Signature Moves**: Includes custom Elite Redux special moves

### Interactions with Other Mechanics
- **Stat Stages**: Speed boosts directly increase the damage bonus
- **Wonder Room**: If Wonder Room swaps Attack/Sp.Attack, Terminal Velocity still adds Speed to the effective attacking stat
- **Critical Hits**: Speed bonus applies regardless of critical hit status
- **Weather**: Speed modifiers from weather (Swift Swim, Chlorophyll) enhance the damage bonus
- **Items**: Choice Scarf and other Speed-boosting items increase the damage bonus
- **Abilities**: Speed-boosting abilities like Speed Boost multiply the Terminal Velocity effect

### Strategic Implications
- **Ideal Users**: Fast special attackers (130+ Speed, 100+ Sp.Attack)
- **Speed Investment**: EVs in Speed provide both priority and damage
- **Speed Control**: Tailwind, Agility, and other speed boosts increase damage output
- **Late Game Power**: Becomes stronger as Speed is boosted throughout battle

### Example Damage Calculations
**Base Scenario**: Pokemon with 300 Sp.Attack, 400 Speed
- Normal Special Attack: 300
- With Terminal Velocity: 300 + (400 x 0.2) = 380 Special Attack
- **Damage Increase**: ~26.7%

**After Speed Boost**: Same Pokemon with +1 Speed (600 Speed)
- With Terminal Velocity: 300 + (600 x 0.2) = 420 Special Attack  
- **Damage Increase**: ~40%

**Choice Scarf Scenario**: 400 Speed to 600 Speed (1.5x modifier)
- With Terminal Velocity: 300 + (600 x 0.2) = 420 Special Attack
- **Total multiplier from Scarf + Terminal Velocity**: Significant damage increase

### Common Users
Based on SpeciesList.textproto analysis:
- **Kilowattrel line**: Electric/Flying types with high Speed (125 base)
- **Iron Valiant**: Psychic/Fairy legendary with 135 Speed
- Various fast special attackers across different tiers
- Often paired with other Speed-boosting abilities as innates

### Competitive Usage Notes
- **Team Role**: Primary special sweeper or speed control abuser  
- **Setup Requirements**: Benefits from speed control moves (Tailwind, Agility)
- **Priority Targets**: Pokemon that can boost Speed reliably
- **Synergy Abilities**: Speed Boost, Swift Swim, Chlorophyll as innate abilities

### Counters
- **Speed Control**: Trick Room negates Speed advantage
- **Priority Moves**: Bypass Speed advantage entirely  
- **Special Walls**: High Sp.Defense still tanks boosted attacks
- **Status Effects**: Paralysis cuts Speed and damage bonus in half
- **Intimidate**: While it doesn't affect Sp.Attack directly, it can force switches

### Synergies
- **Speed Boost**: Continuously increases damage output each turn
- **Swift Swim/Chlorophyll**: Weather-based Speed doubling
- **Choice Scarf**: 1.5x Speed multiplier enhances damage bonus
- **Agility/Rock Polish**: Manual Speed boosting for immediate power spike
- **Tailwind**: Team-wide Speed doubling benefits entire team

### Version History
- Added in Elite Redux as part of the expanded ability system
- Part of the advanced stat interaction mechanics unique to Elite Redux
- Designed to reward Speed investment on special attackers